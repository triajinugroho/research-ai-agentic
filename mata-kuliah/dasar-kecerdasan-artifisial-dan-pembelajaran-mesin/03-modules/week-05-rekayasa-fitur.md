# Minggu 5: Rekayasa Fitur

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 5 dari 16 |
| Topik | Pembuatan fitur, transformasi, pemilihan fitur, kutukan dimensi |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-05 |
| Bloom | C3 (Menerapkan) → C6 (Merancang) |
| Durasi | 150 menit |
| Metode | Kuliah · Praktikum · Kerja kelompok proyek |
| Penilaian | Observasi (Lab 5) · **Proposal proyek (P-00)** |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Merancang** (C6) fitur baru dari data mentah dengan memanfaatkan pengetahuan domain.
2. **Menerapkan** (C3) transformasi yang sesuai bentuk sebaran data.
3. **Menganalisis** (C4) kontribusi tiap fitur terhadap kinerja model.
4. **Mengevaluasi** (C5) apakah sebuah fitur menimbulkan kebocoran.
5. **Menjelaskan** (C2) kutukan dimensi dan kapan pengurangan fitur diperlukan.

---

## Materi Pembelajaran

### 5.1 Fitur Menentukan Batas Atas Kinerja

> *"Rekayasa fitur yang dilakukan dengan baik sering memberi peningkatan lebih besar daripada pergantian algoritma."* — Domingos (2012)

Model hanya dapat belajar dari apa yang diberikan kepadanya. Bila informasi yang dibutuhkan tidak ada dalam fitur, tidak ada algoritma yang dapat memunculkannya.

**Contoh konkret:** memprediksi kemacetan dari kolom `timestamp` mentah. Model kesulitan, karena angka detik sejak 1970 tidak bermakna. Setelah `timestamp` diurai menjadi `jam`, `hari_dalam_minggu`, `hari_libur`, dan `jam_sibuk`, model yang **sama persis** menjadi jauh lebih baik — tanpa satu pun hiperparameter diubah.

Inilah sebabnya Lab 5 mengunci model dan hiperparameter: agar peningkatan yang terjadi **hanya** dapat berasal dari fitur.

---

### 5.2 Membuat Fitur Baru

#### 5.2.1 Fitur Waktu

```python
df["tanggal"] = pd.to_datetime(df["tanggal"])

df["tahun"]        = df["tanggal"].dt.year
df["bulan"]        = df["tanggal"].dt.month
df["hari"]         = df["tanggal"].dt.day
df["hari_minggu"]  = df["tanggal"].dt.dayofweek       # 0 = Senin
df["akhir_pekan"]  = (df["hari_minggu"] >= 5).astype(int)
df["jam"]          = df["tanggal"].dt.hour
df["jam_sibuk"]    = df["jam"].isin([6,7,8,16,17,18,19]).astype(int)

# Hari besar nasional Indonesia — memerlukan pengetahuan domain
libur_nasional = pd.to_datetime(["2026-01-01", "2026-03-20", "2026-05-01"])
df["hari_libur"] = df["tanggal"].dt.normalize().isin(libur_nasional).astype(int)
```

**Penyandian siklik** untuk variabel yang melingkar (jam, bulan, arah):

```python
import numpy as np

# Jam 23 dan jam 0 berdekatan, tetapi selisih angkanya 23.
# Penyandian sinus-kosinus memperbaikinya.
df["jam_sin"] = np.sin(2 * np.pi * df["jam"] / 24)
df["jam_cos"] = np.cos(2 * np.pi * df["jam"] / 24)
```

#### 5.2.2 Fitur Agregat

```python
# Rata-rata omzet per provinsi — PERHATIAN: rawan kebocoran
# bila dihitung pada seluruh data. Harus di dalam Pipeline
# atau dihitung hanya pada lipatan latih.
df["omzet_rata_provinsi"] = df.groupby("provinsi")["omzet"].transform("mean")
df["omzet_relatif"] = df["omzet"] / df["omzet_rata_provinsi"]
```

#### 5.2.3 Fitur Rasio dan Interaksi

Sering lebih informatif daripada komponennya sendiri-sendiri:

| Fitur asal | Fitur turunan | Mengapa lebih baik |
|------------|---------------|--------------------|
| `omzet`, `jumlah_pegawai` | `omzet_per_pegawai` | Produktivitas, bebas skala usaha |
| `luas_bangunan`, `luas_tanah` | `rasio_bangunan` | Kepadatan bangunan |
| `total_pinjaman`, `pendapatan` | `rasio_beban_utang` | **Ukuran baku dalam penilaian kredit** |
| `jarak`, `waktu_tempuh` | `kecepatan_rata` | Kondisi lalu lintas |

> Baris ketiga menunjukkan poin terpenting bab ini: fitur terbaik sering sudah dikenal oleh praktisi bidangnya. **Berbicara dengan ahli domain lebih berguna daripada mencoba seratus kombinasi secara acak.**

#### 5.2.4 Fitur Geografis Indonesia

```python
# Pengelompokan wilayah — pengetahuan domain Indonesia
wilayah = {
    "DKI Jakarta": "Jawa", "Jawa Barat": "Jawa", "Jawa Tengah": "Jawa",
    "Sumatera Utara": "Sumatera", "Riau": "Sumatera",
    "Kalimantan Timur": "Kalimantan", "Sulawesi Selatan": "Sulawesi",
    "Papua": "Papua", "Bali": "Bali-Nusra",
}
df["pulau"] = df["provinsi"].map(wilayah).fillna("Lainnya")
df["jawa"] = (df["pulau"] == "Jawa").astype(int)
```

---

### 5.3 Transformasi Fitur

| Transformasi | Rumus | Kapan dipakai |
|--------------|-------|---------------|
| Logaritma | $\log(x+1)$ | Menceng kanan berat (pendapatan, populasi) |
| Akar kuadrat | $\sqrt{x}$ | Menceng kanan sedang; data cacahan |
| Box-Cox / Yeo-Johnson | Otomatis | Mencari transformasi terbaik; Yeo-Johnson menerima nilai negatif |
| Binning | Pengelompokan rentang | Hubungan tidak monoton; menambah ketahanan |
| Polinomial | $x, x^2, x_1 x_2$ | Hubungan melengkung dan interaksi |

```python
from sklearn.preprocessing import PowerTransformer, KBinsDiscretizer

# Yeo-Johnson: mencari transformasi yang paling mendekatkan ke normal
pt = PowerTransformer(method="yeo-johnson")

# Binning: usia menjadi kelompok umur
binner = KBinsDiscretizer(n_bins=5, encode="ordinal", strategy="quantile")
```

> **Peringatan:** `PolynomialFeatures(degree=3)` pada 20 fitur menghasilkan lebih dari 1.700 kolom. Kombinasi *overfitting* dan kutukan dimensi hampir dipastikan. Derajat 2 sudah jarang diperlukan.

---

### 5.4 Pemilihan Fitur

#### 5.4.1 Tiga Pendekatan

| Pendekatan | Cara | Kelebihan | Kekurangan |
|------------|------|-----------|------------|
| **Filter** | Berdasarkan statistik (korelasi, uji chi-square, informasi bersama) | Cepat; bebas model | Mengabaikan interaksi antarfitur |
| **Wrapper** | Mencoba himpunan fitur dengan model (RFE) | Memperhitungkan interaksi | Mahal secara komputasi |
| **Embedded** | Terjadi saat pelatihan (Lasso, kepentingan fitur pohon) | Efisien | Terikat pada model tertentu |

```python
from sklearn.feature_selection import SelectKBest, f_classif, RFE
from sklearn.ensemble import RandomForestClassifier

# Filter — 15 fitur terbaik berdasarkan uji F
filter_fitur = SelectKBest(score_func=f_classif, k=15)

# Wrapper — eliminasi bertahap dengan model
rfe = RFE(estimator=RandomForestClassifier(random_state=42), n_features_to_select=15)

# Embedded — kepentingan fitur dari Random Forest
rf = RandomForestClassifier(random_state=42).fit(X_train, y_train)
kepentingan = pd.Series(rf.feature_importances_, index=X_train.columns)
print(kepentingan.sort_values(ascending=False).head(15))
```

#### 5.4.2 Pemilihan Fitur Adalah Sumber Kebocoran yang Sering Luput

```python
# ══════════ SALAH ══════════
# Memilih fitur berdasarkan seluruh data, LALU membagi
X_terpilih = SelectKBest(k=15).fit_transform(X, y)   # ← y seluruhnya dipakai
X_tr, X_te = train_test_split(X_terpilih)
# Informasi target dari data uji sudah masuk ke dalam pemilihan fitur.

# ══════════ BENAR ══════════
model = Pipeline([
    ("pemilihan", SelectKBest(k=15)),
    ("klasifikasi", RandomForestClassifier(random_state=42)),
])
# Di dalam validasi silang, pemilihan fitur di-fit ulang pada tiap lipatan latih.
```

---

### 5.5 Kutukan Dimensi

Ketika jumlah fitur bertambah, data menjadi semakin jarang dalam ruang berdimensi tinggi. Akibatnya:

| Akibat | Penjelasan |
|--------|------------|
| Jarak kehilangan makna | Pada dimensi tinggi, jarak antartitik menjadi hampir sama besar |
| Kebutuhan data meningkat eksponensial | Untuk kerapatan yang sama, jumlah data harus bertambah jauh lebih cepat |
| *Overfitting* lebih mudah terjadi | Model menemukan pola kebetulan dengan lebih mudah |
| Komputasi melonjak | Waktu latih bertambah |

**Kaidah praktis:** jumlah baris sebaiknya jauh lebih besar daripada jumlah fitur. Sebagai ancar-ancar awal, sekurang-kurangnya 10 baris per fitur untuk model linear — lebih banyak lagi untuk model kompleks.

Cara mengurangi dimensi:
1. Pemilihan fitur (§5.4) — membuang fitur.
2. Reduksi dimensi (PCA, Minggu 12) — meringkas fitur menjadi kombinasi.
3. Regularisasi (Minggu 6) — menekan koefisien fitur yang tidak berguna.

---

### 5.6 Alur Kerja Rekayasa Fitur

```
  1. Pahami domain           ── berbicara dengan ahli, membaca definisi variabel
         ↓
  2. Bangun BASELINE         ── fitur mentah apa adanya
         ↓
  3. Tambah fitur BERTAHAP   ── satu kelompok fitur dalam satu waktu
         ↓
  4. Ukur pada VALIDASI      ── bukan pada data latih, bukan pada data uji
         ↓
  5. Periksa KEBOCORAN       ── "apakah fitur ini tersedia saat prediksi?"
         ↓
  6. Catat: mana yang        ── termasuk yang GAGAL, beserta dugaan sebabnya
     membantu, mana yang
     tidak
```

> **Mencatat fitur yang gagal sama pentingnya dengan mencatat yang berhasil.** Ia mencegah pengulangan percobaan yang sama dan sering mengungkap sesuatu tentang datanya.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 5 buku ajar](../06-buku-ajar/bab-05-rekayasa-fitur.md).
- Menyelesaikan proposal proyek — **dikumpulkan hari ini**.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Tinjauan; **pengumpulan proposal P-00** |
| Konsep | 35' | Pembuatan fitur: waktu, agregat, rasio, geografis |
| Demonstrasi | 30' | **Kegiatan inti:** model dikunci, hanya fitur yang diubah — peningkatan ditunjukkan langsung |
| Konsep | 25' | Transformasi; pemilihan fitur; kebocoran melalui pemilihan |
| Praktik | 35' | Mulai Lab 5 |
| Penutup | 15' | Kutukan dimensi; alur kerja; penugasan |

**Demonstrasi kegiatan inti:** dataset kemacetan dengan `timestamp` mentah.

| Tahap | Fitur | F1 validasi |
|-------|-------|-------------|
| *Baseline* | `timestamp` sebagai angka | 0,52 |
| + fitur waktu | `jam`, `hari_minggu`, `akhir_pekan` | 0,71 |
| + penyandian siklik | `jam_sin`, `jam_cos` | 0,74 |
| + pengetahuan domain | `jam_sibuk`, `hari_libur` | 0,81 |

Model dan hiperparameter **tidak berubah sama sekali** sepanjang keempat tahap.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 5](../04-labs/lab-05-rekayasa-fitur.md).
- Mulai mengerjakan Milestone 1 proyek (jatuh tempo Minggu 7).

---

## Penugasan

**T-05 — Rekayasa Fitur**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook Colab |
| Isi | (a) *Baseline* dengan fitur mentah; (b) Minimal empat kelompok fitur baru, ditambahkan bertahap; (c) Skor validasi setelah tiap penambahan; (d) **Catatan fitur yang gagal** beserta dugaan sebabnya; (e) Pemeriksaan kebocoran untuk setiap fitur baru |
| Ketentuan khusus | **Model dan hiperparameter dikunci** — hanya fitur yang boleh diubah |
| Tenggat | Awal pertemuan Minggu 6 |
| Bobot | 1,9% (Observasi) |

---

## Rangkuman

1. **Fitur menentukan batas atas kinerja.** Model tidak dapat memunculkan informasi yang tidak ada.
2. Fitur waktu harus **diurai**; variabel siklik disandikan **sinus-kosinus**.
3. **Fitur rasio dan interaksi** sering lebih informatif daripada komponennya sendiri-sendiri.
4. Fitur terbaik sering sudah dikenal praktisi bidangnya — **berbicara dengan ahli domain** lebih berguna daripada mencoba acak.
5. Transformasi log/akar untuk sebaran menceng; polinomial derajat tinggi hampir selalu berlebihan.
6. Tiga pendekatan pemilihan fitur: **filter, wrapper, embedded**.
7. **Pemilihan fitur di luar `Pipeline` adalah kebocoran** yang sering luput.
8. **Kutukan dimensi:** data menjadi jarang; *overfitting* lebih mudah terjadi.
9. Tambahkan fitur **bertahap**, ukur pada **validasi**, dan **catat yang gagal**.

---

## Referensi

1. Zheng, A., & Casari, A. (2018). *Feature Engineering for Machine Learning*. O'Reilly.
2. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 2. O'Reilly.
3. Domingos, P. (2012). A Few Useful Things to Know About Machine Learning. *CACM*, 55(10), 78–87.
4. Kuhn, M., & Johnson, K. (2019). *Feature Engineering and Selection*. CRC Press.
5. Dokumentasi scikit-learn — *Feature selection*. <https://scikit-learn.org/stable/modules/feature_selection.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
