# Lab 02: Formulasi Masalah dan *Baseline*

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 2 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-02 |
| Durasi | 100 menit |
| Prasyarat | Lab 1 selesai |
| Bobot | 1,9% (Observasi) |

---

## Tujuan Praktikum

1. Merumuskan masalah nyata menjadi spesifikasi *task* ML yang lengkap.
2. Memilih metrik berdasarkan dampak kesalahan.
3. Membangun *baseline* dan menafsirkan selisih terhadapnya.
4. Mengenali fitur yang tidak boleh dipakai.

---

## Persiapan

- Notebook baru bernama `NIM_Nama_Lab02.ipynb`.
- Salin sel pembuka baku dari Lab 1.

---

## Langkah-langkah

### LANGKAH 1: Memilih Masalah

```python
# =============================================
# LANGKAH 1: Pilih SATU masalah
# =============================================
# Pilih satu dari daftar berikut, atau ajukan masalah sendiri:
#
# A. Puskesmas ingin mengenali pasien yang berisiko tidak
#    kembali untuk pengobatan lanjutan.
# B. Koperasi simpan pinjam ingin menurunkan kredit macet.
# C. Kampus ingin mengenali mahasiswa yang berisiko putus kuliah.
# D. Dinas perhubungan ingin memperkirakan kepadatan penumpang
#    TransJakarta per koridor per jam.
# E. Toko daring ingin mengenali ulasan produk yang tidak wajar.
```

### LANGKAH 2: Tujuh Pertanyaan Formulasi

```python
# =============================================
# LANGKAH 2: Formulasi (dikerjakan di sel Markdown)
# =============================================
# Jawab TUJUH pertanyaan berikut. Jawaban harus spesifik,
# bukan umum.
#
# | # | Pertanyaan                                    | Jawaban |
# |---|-----------------------------------------------|---------|
# | 1 | Keputusan apa yang diambil dari keluaran?     |         |
# | 2 | Apa TARGETNYA, tepatnya?                      |         |
# | 3 | KAPAN prediksi dibutuhkan?                    |         |
# | 4 | Fitur apa yang tersedia PADA SAAT ITU?        |         |
# | 5 | Kesalahan jenis mana yang lebih merugikan?    |         |
# | 6 | Metrik apa yang mencerminkan dampak itu?      |         |
# | 7 | Apa PEMBANDING yang harus dikalahkan?         |         |
#
# Pertanyaan 2 harus sangat tepat. "Gagal bayar" tidak cukup;
# yang dibutuhkan misalnya "menunggak >= 90 hari dalam 12 bulan
# sejak pencairan".
```

### LANGKAH 3: Daftar Fitur Terlarang

```python
# =============================================
# LANGKAH 3: Fitur yang TIDAK BOLEH dipakai
# =============================================
# Untuk masalah yang dipilih, sebutkan minimal TIGA fitur yang
# secara teknis tersedia dalam data tetapi TIDAK BOLEH dipakai,
# beserta alasannya.
#
# | Fitur | Mengapa tidak boleh |
# |-------|---------------------|
# |       |                     |
#
# Uji tiap fitur dengan pertanyaan:
# "Apakah nilai ini sudah ada pada saat prediksi dibutuhkan?"
# Bila jawabannya tidak — fitur itu bocor.
```

### LANGKAH 4: Menyiapkan Data

```python
# =============================================
# LANGKAH 4: Data untuk masalah yang dipilih
# =============================================
import numpy as np
import pandas as pd

rng = np.random.default_rng(RANDOM_STATE)
n = 2000

# Data contoh: penilaian kelayakan kredit UMKM.
# Gunakan data nyata bila tersedia; data ini hanya untuk latihan
# alur kerja, dan harus DINYATAKAN sebagai data simulasi.
df = pd.DataFrame({
    "omzet_bulanan_jt":  rng.gamma(shape=2.0, scale=15, size=n).round(1),
    "lama_usaha_thn":    rng.gamma(shape=2.0, scale=2.5, size=n).round(1),
    "jumlah_pegawai":    rng.poisson(4, size=n) + 1,
    "rasio_beban_utang": rng.beta(2, 5, size=n).round(3),
    "jenis_usaha":       rng.choice(["Kuliner", "Retail", "Jasa", "Produksi"],
                                    size=n, p=[0.35, 0.30, 0.20, 0.15]),
    "wilayah":           rng.choice(["Jawa", "Sumatera", "Kalimantan",
                                     "Sulawesi", "Lainnya"],
                                    size=n, p=[0.5, 0.2, 0.12, 0.12, 0.06]),
})

# Target: gagal bayar (1) atau lancar (0) — sengaja TAK SEIMBANG
logit = (-2.2 - 0.030 * df["omzet_bulanan_jt"] - 0.18 * df["lama_usaha_thn"]
         + 3.2 * df["rasio_beban_utang"])
p = 1 / (1 + np.exp(-logit))
df["gagal_bayar"] = rng.binomial(1, p)

print("Dimensi:", df.shape)
print("\nSebaran target:")
print(df["gagal_bayar"].value_counts())
print(df["gagal_bayar"].value_counts(normalize=True).round(3))
```

**Catat di sel Markdown:** berapa persen kelas minoritas? Apa akibatnya bagi pemilihan metrik?

### LANGKAH 5: Pembagian Data yang Benar

```python
# =============================================
# LANGKAH 5: Pembagian data
# =============================================
from sklearn.model_selection import train_test_split

X = df.drop(columns=["gagal_bayar"])
y = df["gagal_bayar"]

# stratify=y WAJIB pada data tak seimbang,
# agar proporsi kelas terjaga di kedua bagian
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE
)

print(f"Latih: {len(X_train)} baris, proporsi positif {y_train.mean():.3f}")
print(f"Uji  : {len(X_test)} baris, proporsi positif {y_test.mean():.3f}")
```

### LANGKAH 6: Membangun *Baseline*

```python
# =============================================
# LANGKAH 6: BASELINE — pembanding wajib
# =============================================
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score)

strategi = {
    "Selalu kelas terbanyak": "most_frequent",
    "Acak berbobot proporsi": "stratified",
    "Selalu kelas positif":   "constant",
}

hasil = []
for nama, strat in strategi.items():
    if strat == "constant":
        dummy = DummyClassifier(strategy=strat, constant=1,
                                random_state=RANDOM_STATE)
    else:
        dummy = DummyClassifier(strategy=strat, random_state=RANDOM_STATE)
    dummy.fit(X_train, y_train)
    pred = dummy.predict(X_test)
    hasil.append({
        "Baseline":  nama,
        "Akurasi":   accuracy_score(y_test, pred),
        "Precision": precision_score(y_test, pred, zero_division=0),
        "Recall":    recall_score(y_test, pred, zero_division=0),
        "F1":        f1_score(y_test, pred, zero_division=0),
    })

tabel_baseline = pd.DataFrame(hasil)
print(tabel_baseline.round(3).to_string(index=False))
```

**Yang harus ditulis di sel Markdown:**
- *Baseline* mana yang berakurasi tertinggi?
- Berapa *recall*-nya?
- Apa yang ditunjukkan oleh selisih antara akurasi dan *recall* itu?

> Inilah demonstrasi pertama bahwa **akurasi tinggi dapat sama sekali tidak berguna** — bahasan lengkapnya pada Minggu 7.

### LANGKAH 7: Model Sederhana sebagai Pembanding

```python
# =============================================
# LANGKAH 7: Satu model sederhana
# =============================================
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression

kol_num = ["omzet_bulanan_jt", "lama_usaha_thn", "jumlah_pegawai",
           "rasio_beban_utang"]
kol_kat = ["jenis_usaha", "wilayah"]

pra = ColumnTransformer([
    ("num", StandardScaler(), kol_num),
    ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), kol_kat),
])

model = Pipeline([
    ("pra", pra),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced",
                               random_state=RANDOM_STATE)),
])

model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Model sederhana (regresi logistik):")
print(f"  Akurasi  : {accuracy_score(y_test, pred):.3f}")
print(f"  Precision: {precision_score(y_test, pred, zero_division=0):.3f}")
print(f"  Recall   : {recall_score(y_test, pred, zero_division=0):.3f}")
print(f"  F1       : {f1_score(y_test, pred, zero_division=0):.3f}")
```

### LANGKAH 8: Membaca Selisih terhadap *Baseline*

```python
# =============================================
# LANGKAH 8: Perbandingan menyeluruh
# =============================================
baris_model = {
    "Baseline":  "Regresi logistik",
    "Akurasi":   accuracy_score(y_test, pred),
    "Precision": precision_score(y_test, pred, zero_division=0),
    "Recall":    recall_score(y_test, pred, zero_division=0),
    "F1":        f1_score(y_test, pred, zero_division=0),
}
tabel = pd.concat([tabel_baseline, pd.DataFrame([baris_model])],
                  ignore_index=True)
print(tabel.round(3).to_string(index=False))

# Selisih F1 terhadap baseline terbaik
f1_baseline_terbaik = tabel_baseline["F1"].max()
print(f"\nF1 baseline terbaik : {f1_baseline_terbaik:.3f}")
print(f"F1 model            : {baris_model['F1']:.3f}")
print(f"Selisih             : {baris_model['F1'] - f1_baseline_terbaik:+.3f}")
```

**Tafsirkan selisihnya** menurut tabel pada modul Minggu 2 §2.4.2. Bila selisihnya sangat besar, periksa kebocoran — meski pada lab ini datanya sengaja dibuat bersih.

---

## Tantangan Tambahan

### Tantangan 1 — Metrik yang Berbeda, Kesimpulan yang Berbeda

Urutkan keempat model (tiga *baseline* + satu model) menurut akurasi, lalu menurut *recall*. Apakah urutannya sama? Jelaskan mengapa, dan mana urutan yang lebih relevan untuk masalah kredit macet.

### Tantangan 2 — Ambang Keberhasilan

Tetapkan ambang keberhasilan sebelum melihat hasil: *"model dianggap berhasil bila recall ≥ X dengan precision ≥ Y"*. Tentukan X dan Y beserta alasannya, lalu periksa apakah model memenuhinya.

### Tantangan 3 — *Baseline* dari Aturan

Bangun *baseline* berupa aturan sederhana: `if rasio_beban_utang > 0.5 then gagal_bayar = 1`. Bandingkan dengan `DummyClassifier` dan dengan model. Aturan ini sering lebih baik daripada *dummy* — dan kadang cukup baik sehingga ML tidak diperlukan.

---

## Checklist Penyelesaian

- [ ] Tujuh pertanyaan formulasi dijawab spesifik
- [ ] Target dirumuskan dengan tepat, bukan secara umum
- [ ] Minimal tiga fitur terlarang disebutkan beserta alasannya
- [ ] Pembagian data memakai `stratify=y`
- [ ] Tiga jenis *baseline* dibangun dan dibandingkan
- [ ] **Selisih model terhadap *baseline* dilaporkan dan ditafsirkan**
- [ ] Metrik dipilih beserta alasan yang dikaitkan dengan dampak kesalahan
- [ ] Ambang keberhasilan ditetapkan sebelum melihat hasil
- [ ] Data simulasi dinyatakan secara eksplisit sebagai simulasi
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 2](../03-modules/week-02-formulasi-masalah-daur-hidup-ml.md)
2. [Bab 2 buku ajar](../06-buku-ajar/bab-02-formulasi-masalah-daur-hidup-ml.md)
3. Dokumentasi scikit-learn — *Dummy estimators*. <https://scikit-learn.org/stable/modules/model_evaluation.html#dummy-estimators>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
