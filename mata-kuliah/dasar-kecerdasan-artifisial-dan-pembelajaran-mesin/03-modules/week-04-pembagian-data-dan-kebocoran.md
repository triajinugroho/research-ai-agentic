# Minggu 4: Pembagian Data dan Kebocoran Data

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 4 dari 16 |
| Topik | *Train/validation/test*, validasi silang, enam jenis kebocoran data |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-04 |
| Bloom | C3 (Menerapkan) → C4 (Menganalisis) |
| Durasi | 150 menit |
| Metode | Kuliah · Demonstrasi kegagalan · Praktikum |
| Penilaian | Observasi (Lab 4) · **Kuis 1** |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menjelaskan** (C2) peran berbeda antara data latih, validasi, dan uji.
2. **Menerapkan** (C3) strategi pembagian data yang sesuai sifat datanya: acak, stratifikasi, temporal, atau berkelompok.
3. **Menerapkan** (C3) validasi silang dan menafsirkan sebaran skor antarlipatan.
4. **Menganalisis** (C4) sebuah *pipeline* dan menemukan kebocoran data di dalamnya.
5. **Memperbaiki** (C5) kebocoran yang ditemukan dan melaporkan dampaknya terhadap skor.

---

## Materi Pembelajaran

### 4.1 Mengapa Satu Pertemuan Penuh untuk Ini

Kapoor dan Narayanan (2023) menelaah 294 makalah ilmiah dari 17 bidang yang memakai ML, dan menemukan **kebocoran data pada sebagian besar di antaranya**. Akibatnya: hasil yang dilaporkan tidak dapat diulang, dan sebagian kesimpulan ilmiah yang telah dipublikasikan ternyata keliru.

Ini bukan kesalahan pemula. Ini kesalahan yang terjadi pada peneliti terlatih, berulang kali, karena kebocoran **tidak menghasilkan pesan galat**. Ia menghasilkan skor yang bagus.

> **Kebocoran data adalah satu-satunya jenis kesalahan dalam ML yang *memberi hadiah* ketika dilakukan.** Itulah yang membuatnya berbahaya.

---

### 4.2 Tiga Peran Data

```
┌────────────────────────────────────────────────────────────┐
│                     SELURUH DATA                           │
├──────────────────────────┬──────────────┬──────────────────┤
│         LATIH            │   VALIDASI   │       UJI        │
│         (60%)            │    (20%)     │      (20%)       │
├──────────────────────────┼──────────────┼──────────────────┤
│ Model belajar dari sini  │ Memilih model│ Menaksir kinerja │
│                          │ dan menyetel │ pada data baru   │
│                          │ hiperparameter│                 │
├──────────────────────────┼──────────────┼──────────────────┤
│ Dilihat model: berkali-  │ Dilihat:     │ Dilihat: SEKALI, │
│ kali                     │ berkali-kali │ di paling akhir  │
└──────────────────────────┴──────────────┴──────────────────┘
```

| Bagian | Peran | Aturan |
|--------|-------|--------|
| **Latih** | Model mempelajari pola | Boleh dipakai berulang |
| **Validasi** | Memilih model dan hiperparameter | Boleh dipakai berulang, tetapi setiap pemakaian mengurangi kejujurannya |
| **Uji** | Menaksir kinerja pada data yang belum pernah dilihat | **Dipakai satu kali, di paling akhir** |

#### 4.2.1 Mengapa Data Uji Hanya Sekali

Setiap kali keputusan diambil berdasarkan skor data uji — "model A lebih baik, mari pakai A" — informasi dari data uji masuk ke dalam pilihan. Setelah beberapa kali, skor data uji berhenti menjadi taksiran kinerja pada data baru, dan menjadi skor pada data yang sudah ikut membentuk model.

Fenomena ini disebut **kebocoran melalui pemilihan berulang**. Ia halus, tidak menghasilkan galat, dan hampir selalu terjadi bila data uji dipakai lebih dari sekali.

---

### 4.3 Strategi Pembagian sesuai Sifat Data

| Sifat data | Strategi | Alat |
|------------|----------|------|
| Biasa, kelas seimbang | Acak | `train_test_split` |
| Kelas tak seimbang | **Stratifikasi** | `train_test_split(stratify=y)` |
| Ada urutan waktu | **Temporal** | `TimeSeriesSplit` |
| Ada pengelompokan (pasien, pengguna, wilayah) | **Berkelompok** | `GroupKFold` |
| Data sangat sedikit | Validasi silang berlipat banyak | `KFold(n_splits=10)` atau LOOCV |

#### 4.3.1 Stratifikasi

```python
from sklearn.model_selection import train_test_split

# Tanpa stratifikasi pada data tak seimbang, satu bagian bisa
# tidak memuat kelas minoritas sama sekali
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
```

#### 4.3.2 Pembagian Temporal

Ketika data memiliki urutan waktu, pembagian acak **selalu** menghasilkan kebocoran: model belajar dari masa depan untuk memprediksi masa lalu.

```
  SALAH (acak):
  ─────────────────────────────────────────────────────────►  waktu
  [U][L][L][U][L][U][L][L][U][L]    ← uji tersebar di antara latih
     Model "melihat masa depan"

  BENAR (temporal):
  ─────────────────────────────────────────────────────────►  waktu
  [L][L][L][L][L][L][L][V][V][U][U] ← uji selalu setelah latih
```

```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
for i, (idx_latih, idx_uji) in enumerate(tscv.split(X)):
    # Setiap lipatan: data latih selalu MENDAHULUI data uji
    print(f"Lipatan {i}: latih={len(idx_latih):5d}, uji={len(idx_uji):5d}")
```

#### 4.3.3 Pembagian Berkelompok

Bila satu entitas (pasien, pelanggan, mahasiswa) muncul dalam beberapa baris, membaginya secara acak membuat entitas yang sama hadir di latih **dan** uji. Model dapat "mengenali" entitas itu, bukan mempelajari polanya.

```python
from sklearn.model_selection import GroupKFold

# grup = id_pasien — seluruh baris satu pasien masuk lipatan yang sama
gkf = GroupKFold(n_splits=5)
for idx_latih, idx_uji in gkf.split(X, y, groups=id_pasien):
    ...
```

---

### 4.4 Validasi Silang

#### 4.4.1 k-Fold

```
  Data dibagi 5 lipatan; tiap lipatan bergiliran menjadi validasi
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

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold
import numpy as np

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# PENTING: yang divalidasi-silang adalah PIPELINE, bukan model saja.
# Dengan begitu prapemrosesan di-fit ulang pada tiap lipatan.
skor = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring="f1")

print(f"F1 = {skor.mean():.3f} ± {skor.std():.3f}")
print("Per lipatan:", np.round(skor, 3))
```

#### 4.4.2 Membaca Simpangan Antarlipatan

| Keadaan | Tafsir | Tindakan |
|---------|--------|----------|
| Simpangan kecil (< 0,02) | Kinerja stabil | Dapat dipercaya |
| Simpangan sedang (0,02–0,05) | Wajar pada data terbatas | Laporkan rerata **dan** simpangannya |
| Simpangan besar (> 0,10) | Data sedikit, atau ada lipatan yang sangat berbeda | Selidiki lipatan yang menyimpang |
| Satu lipatan jauh lebih rendah | Kemungkinan ada kelompok/periode yang berbeda sifat | Periksa apakah strategi pembagian sudah tepat |

> **Melaporkan rerata tanpa simpangan menyembunyikan informasi penting.** Rerata 0,80 dari skor {0,79; 0,80; 0,81} sangat berbeda artinya dari rerata 0,80 dari skor {0,60; 0,80; 1,00}.

---

### 4.5 Enam Jenis Kebocoran Data

#### 4.5.1 Kebocoran Prapemrosesan

Transformasi di-*fit* pada seluruh data sebelum pembagian.

```python
# SALAH
X_scaled = StandardScaler().fit_transform(X)      # ← seluruh data
X_tr, X_te = train_test_split(X_scaled)

# BENAR: gunakan Pipeline
model = Pipeline([("skala", StandardScaler()), ("clf", LogisticRegression())])
```

#### 4.5.2 Kebocoran Temporal

Fitur memuat informasi yang belum tersedia pada saat prediksi dibutuhkan.

| Kasus | Fitur yang bocor |
|-------|------------------|
| Prediksi gagal bayar saat pengajuan | Riwayat pembayaran setelah pencairan |
| Prediksi keterlambatan saat paket masuk gudang | Status perjalanan berikutnya |
| Prediksi putus kuliah pada semester 3 | IPK semester 5 |

**Pencegahnya** adalah menjawab jujur pertanyaan 3 dan 4 pada formulasi Minggu 2: *kapan prediksi dibutuhkan, dan apa yang tersedia saat itu?*

#### 4.5.3 Kebocoran Duplikat

Baris yang sama (atau nyaris sama) muncul di latih dan uji.

```python
# Periksa sebelum membagi
print("Duplikat penuh:", df.duplicated().sum())
print("Duplikat tanpa kolom id:", df.drop(columns=["id"]).duplicated().sum())
```

#### 4.5.4 Kebocoran Kelompok

Satu entitas tersebar di latih dan uji. Diatasi dengan `GroupKFold` (§4.3.3).

#### 4.5.5 Kebocoran Target

Fitur yang sebenarnya merupakan turunan dari target.

| Fitur mencurigakan | Mengapa bocor |
|--------------------|---------------|
| `jumlah_tagihan_tertunggak` untuk memprediksi gagal bayar | Ia *adalah* gagal bayar |
| `lama_dirawat` untuk memprediksi keparahan penyakit | Akibat, bukan sebab |
| `jumlah_keluhan` untuk memprediksi *churn* | Terjadi setelah keputusan berhenti |

**Tanda pengenalnya:** korelasi terhadap target mendekati sempurna, atau kinerja model jauh di atas yang masuk akal.

#### 4.5.6 Kebocoran melalui Pemilihan Berulang

Data uji dipakai berkali-kali untuk memilih model. Diatasi dengan memakai data validasi untuk pemilihan dan menyentuh data uji **sekali saja**.

---

### 4.6 Daftar Periksa Kebocoran

Wajib dijalankan sebelum mengumpulkan pekerjaan apa pun:

- [ ] Seluruh transformasi berada di dalam `Pipeline`
- [ ] `fit` hanya pernah dipanggil pada data latih
- [ ] Data uji tidak dipakai untuk memilih model, fitur, atau hiperparameter
- [ ] Bila ada urutan waktu: pembagian temporal, bukan acak
- [ ] Bila ada entitas berulang: `GroupKFold`
- [ ] Duplikat diperiksa sebelum pembagian
- [ ] Setiap fitur lolos pertanyaan: *"apakah ini tersedia pada saat prediksi dibutuhkan?"*
- [ ] Tidak ada fitur yang merupakan turunan dari target
- [ ] Skor yang mencurigakan tinggi sudah diselidiki, bukan dirayakan

> **Kaidah praktis:** bila kinerja model jauh melampaui yang masuk akal untuk masalah itu, kemungkinan terbesarnya bukan bahwa modelnya hebat — melainkan bahwa ada kebocoran yang belum ditemukan.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 4 buku ajar](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md).
- Membaca ringkasan Kapoor & Narayanan (2023) tentang kebocoran dalam sains berbasis ML.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Tinjauan; pembahasan T-03 |
| **Kuis 1** | 20' | Kualitas data, prapemrosesan, jenis kebocoran |
| Konsep | 35' | Tiga peran data; strategi pembagian; validasi silang |
| Demonstrasi | 35' | **Kegiatan inti:** notebook dengan empat kebocoran tersembunyi — dibedah bersama, satu per satu |
| Praktik | 40' | Mulai Lab 4: mahasiswa memburu kebocoran sendiri |
| Penutup | 10' | Daftar periksa kebocoran; penugasan |

**Notebook demonstrasi memuat empat kebocoran:**

1. `StandardScaler` di-*fit* sebelum pembagian (prapemrosesan)
2. Pemilihan fitur berdasarkan korelasi terhadap target pada seluruh data (pemilihan)
3. Data deret waktu dibagi secara acak (temporal)
4. Kolom yang merupakan turunan langsung dari target (target)

Skor sebelum perbaikan: 0,97. Setelah keempatnya diperbaiki: 0,71. Selisih inilah pelajarannya.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 4](../04-labs/lab-04-validasi-silang-deteksi-kebocoran.md).
- Menyelesaikan proposal proyek (jatuh tempo Minggu 5).

---

## Penugasan

**T-04 — Validasi Silang dan Perburuan Kebocoran**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook perbaikan + laporan temuan 1 halaman |
| Isi | (a) Menemukan seluruh kebocoran pada notebook yang diberikan; (b) Menjelaskan **mekanisme** tiap kebocoran; (c) Memperbaikinya; (d) Melaporkan skor sebelum dan sesudah; (e) Menerapkan validasi silang yang benar dengan pelaporan rerata ± simpangan |
| Tenggat | Awal pertemuan Minggu 5 |
| Bobot | 1,9% (Observasi) |

---

## Rangkuman

1. **Kebocoran data memberi hadiah ketika dilakukan** — itulah yang membuatnya berbahaya.
2. Data uji **dipakai satu kali, di paling akhir**. Pemakaian berulang merusak kejujurannya.
3. Strategi pembagian mengikuti **sifat data**: stratifikasi untuk kelas tak seimbang, temporal untuk deret waktu, berkelompok untuk entitas berulang.
4. Pembagian acak pada data deret waktu **selalu** menghasilkan kebocoran.
5. Yang divalidasi-silang adalah **`Pipeline`**, bukan model saja.
6. Laporkan **rerata dan simpangan** antarlipatan; rerata saja menyembunyikan informasi.
7. **Enam jenis kebocoran:** prapemrosesan, temporal, duplikat, kelompok, target, dan pemilihan berulang.
8. Skor yang terlalu bagus adalah **tanda bahaya**, bukan tanda keberhasilan.
9. Daftar periksa kebocoran (§4.6) dijalankan sebelum setiap pengumpulan.

---

## Referensi

1. Kapoor, S., & Narayanan, A. (2023). Leakage and the Reproducibility Crisis in ML-based Science. *Patterns*, 4(9), 100804.
2. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 2. O'Reilly.
3. Müller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*, Bab 5. O'Reilly.
4. Kaufman, S., et al. (2012). Leakage in Data Mining. *ACM TKDD*, 6(4), 1–21.
5. Dokumentasi scikit-learn — *Cross-validation*. <https://scikit-learn.org/stable/modules/cross_validation.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
