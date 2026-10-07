# Lab 03: *Pipeline* Prapemrosesan

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 3 |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-03 |
| Durasi | 100 menit |
| Prasyarat | Lab 2 selesai |
| Bobot | 2,0% (Observasi, Sub-CPMK102-1) |
| Diuji pada | scikit-learn 1.6 dan 1.9, pandas 2.2 dan 3.0 (Oktober 2026) |

---

## Tujuan Praktikum

1. Memeriksa kualitas data secara sistematis.
2. Menangani nilai hilang sesuai pola kehilangannya.
3. Menyandikan variabel kategorik dengan tepat.
4. Membangun `Pipeline` dan `ColumnTransformer` yang mencegah kebocoran.

---

## Persiapan

1. Buat notebook baru bernama `NIM_Nama_Lab03.ipynb`.
2. Jalankan **sel pembuka baku** di [Lampiran D](../06-buku-ajar/lampiran.md#lampiran-d-sel-pembuka-baku) — mengimpor pustaka, mencatat versi, dan menetapkan `RANDOM_STATE = 42`. Seluruh langkah di bawah mengandaikan sel itu sudah dijalankan.
3. **Data:** data sintetis (simulasi) yang meniru pola survei UMKM di beberapa provinsi Indonesia; **bukan data resmi BPS/lembaga**. Data dibangkitkan pada Langkah 1, dan masalah kualitasnya **sengaja disisipkan** untuk latihan. Karena sintetis, kita tahu "kebenarannya": target `berkembang` hanya dibangkitkan dari `omzet_bulanan` (hubungan lemah), sedangkan `kode_kelurahan` diundi acak sehingga **tidak berhubungan** dengan target.

---

## Langkah-langkah

### LANGKAH 1: Data yang Sengaja Tidak Bersih

> **Data sintetis (simulasi)** — lihat Persiapan butir 3. Masalah kualitasnya sengaja disisipkan karena lazim dijumpai pada data survei.

```python
# =============================================
# LANGKAH 1: Data mentah SINTETIS dengan masalah yang lazim
# (simulasi survei UMKM — bukan data resmi BPS/lembaga)
# =============================================
import numpy as np, pandas as pd
rng = np.random.default_rng(RANDOM_STATE)
n = 1500

df = pd.DataFrame({
    # Masalah 5: penulisan nama provinsi tidak seragam
    "provinsi": rng.choice(
        ["DKI Jakarta", "dki jakarta", "DKI JAKARTA",      # kapitalisasi beda
         "Jawa Barat", "Jawa barat",
         "D.I. Yogyakarta", "DI Yogyakarta",                # ejaan beda
         "Jawa Timur", "Sumatera Utara", "Bali"], size=n),
    "omzet_bulanan": rng.gamma(2.0, 18, size=n).round(1),
    "lama_usaha":    rng.gamma(2.0, 2.5, size=n).round(1),
    "jumlah_pegawai": rng.poisson(4, size=n) + 1,
    "pendidikan_pemilik": rng.choice(
        ["SD", "SMP", "SMA", "D3", "S1", "S2"], size=n,
        p=[0.08, 0.15, 0.40, 0.15, 0.19, 0.03]),
    "jenis_usaha": rng.choice(["Kuliner", "Retail", "Jasa", "Produksi"], size=n),
})

# Masalah 1: kode nilai hilang yang tidak diterjemahkan
idx = rng.choice(n, size=90, replace=False)
df.loc[idx, "omzet_bulanan"] = -99

# Masalah 2: nilai hilang sesungguhnya (NaN)
idx2 = rng.choice(n, size=140, replace=False)
df.loc[idx2, "lama_usaha"] = np.nan

# Masalah 3: kolom numerik terbaca sebagai teks
df["modal_awal"] = [f"Rp {v:,.0f}".replace(",", ".")
                    for v in rng.gamma(2.0, 30_000_000, size=n)]

# Target: hanya bergantung (lemah) pada omzet_bulanan.
# Dibangkitkan SEBELUM duplikasi agar baris ganda identik penuh, termasuk targetnya.
berkembang = rng.binomial(
    1, 1 / (1 + np.exp(-(-1.0 + 0.012 * df["omzet_bulanan"].clip(lower=0)))))

# Kardinalitas tinggi: 300 kelurahan fiktif, diundi ACAK (tidak terkait target)
df["kode_kelurahan"] = rng.choice([f"KEL-{i:03d}" for i in range(1, 301)], size=n)
df["berkembang"] = berkembang

# Masalah 4: baris duplikat (40 entri ganda)
df = pd.concat([df, df.iloc[:40]], ignore_index=True)

print("Dimensi awal:", df.shape)
print(df.head())
```

### LANGKAH 2: Tujuh Perintah Pembuka

```python
# =============================================
# LANGKAH 2: Pemeriksaan kualitas
# =============================================
print("1. Dimensi:", df.shape, "\n")

print("2. Info:")
df.info()

print("\n3. Ringkasan numerik:")
print(df.describe().T.round(2))

print("\n4. Nilai hilang (%):")
print((df.isna().mean() * 100).round(2).sort_values(ascending=False))

print("\n5. Duplikat penuh:", df.duplicated().sum())

print("\n6. Kardinalitas kolom non-numerik (kategorik/teks):")
for kol in df.select_dtypes(exclude="number").columns:
    print(f"   {kol:22s} {df[kol].nunique():4d} nilai unik")

print("\n7. Sebaran target:")
print(df["berkembang"].value_counts(normalize=True).round(3))
```

**Tulis di sel Markdown: lima masalah apa yang Anda temukan dari keluaran di atas? Kolom kategorik mana yang berkardinalitas tinggi, dan kolom mana yang "kategorik" padahal seharusnya numerik?**

### LANGKAH 3: Memperbaiki Masalah Struktural

Perbaikan struktural dilakukan **sebelum** pembagian data karena tidak melibatkan statistik data — hanya pembacaan ulang nilai.

```python
# =============================================
# LANGKAH 3: Perbaikan struktural
# =============================================
n_awal = len(df)

# (a) Kode nilai hilang -> NaN
n_minus99 = (df["omzet_bulanan"] == -99).sum()
df.loc[df["omzet_bulanan"] == -99, "omzet_bulanan"] = np.nan
print(f"(a) {n_minus99} nilai -99 diubah menjadi NaN")

# (b) Kolom teks -> numerik
df["modal_awal"] = (df["modal_awal"]
                    .str.replace("Rp ", "", regex=False)
                    .str.replace(".", "", regex=False)
                    .astype(float))
print(f"(b) modal_awal dikonversi ke numerik, tipe: {df['modal_awal'].dtype}")

# (c) Pembakuan nama provinsi
df["provinsi"] = (df["provinsi"].str.strip().str.title()
                  .replace({"Dki Jakarta": "DKI Jakarta",
                            "D.I. Yogyakarta": "DI Yogyakarta",
                            "Di Yogyakarta": "DI Yogyakarta"}))
print(f"(c) Provinsi dibakukan: {df['provinsi'].nunique()} nilai unik")

# (d) Duplikat dibuang
n_dup = df.duplicated().sum()
df = df.drop_duplicates().reset_index(drop=True)
print(f"(d) {n_dup} baris duplikat dibuang")

print(f"\nBaris: {n_awal} -> {len(df)} ({(n_awal-len(df))/n_awal*100:.1f}% dibuang)")
```

> **Catat setiap keputusan: apa, berapa banyak, mengapa.** Ini kriteria penilaian `Sub-CPMK102-1`.

### LANGKAH 4: Menganalisis Pola Nilai Hilang

```python
# =============================================
# LANGKAH 4: MCAR, MAR, atau MNAR?
# =============================================
# Periksa apakah kehilangan berkaitan dengan variabel lain
for kol_hilang in ["omzet_bulanan", "lama_usaha"]:
    hilang = df[kol_hilang].isna()
    print(f"\n--- {kol_hilang} ({hilang.sum()} hilang) ---")
    for kol_lain in ["jumlah_pegawai", "modal_awal"]:
        rata_hilang = df.loc[hilang, kol_lain].mean()
        rata_ada    = df.loc[~hilang, kol_lain].mean()
        print(f"  {kol_lain:16s}: hilang={rata_hilang:12.1f} "
              f"ada={rata_ada:12.1f} selisih={abs(rata_hilang-rata_ada)/rata_ada*100:5.1f}%")
```

**Tulis kesimpulan:** bila rata-rata variabel lain sangat berbeda antara baris yang hilang dan yang tidak, kehilangan **tidak acak** (MAR atau MNAR), dan penghapusan baris akan menimbulkan bias.

### LANGKAH 5: Pembagian Data — Sebelum Prapemrosesan Statistik

```python
# =============================================
# LANGKAH 5: Pembagian data
# =============================================
from sklearn.model_selection import train_test_split

X = df.drop(columns=["berkembang"])
y = df["berkembang"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE)

print(f"Latih: {X_train.shape}  Uji: {X_test.shape}")
```

> **Urutannya penting.** Imputasi, penskalaan, dan penyandian dilakukan **setelah** pembagian — dan di dalam `Pipeline` agar terjadi otomatis.

### LANGKAH 6: Demonstrasi Kebocoran

Kebocoran diukur dengan **validasi silang** (*cross-validation*) 5-lipatan pada data **latih** saja — data uji tetap disimpan untuk Langkah 7. `cross_val_score` membagi data latih menjadi 5 lipatan; tiap lipatan bergiliran menjadi "data uji mini" (lipatan validasi) bagi model yang dilatih pada empat lipatan lainnya. Konsep ini dibahas formal pada Minggu 4; di sini cukup dipahami bahwa **lipatan validasi berperan sebagai data uji**, sehingga tidak boleh ikut membentuk prapemrosesan.

Dua skenario dibandingkan:

- **Skenario A — kebocoran statistik kolom:** imputasi median dan penskalaan di-*fit* pada seluruh data latih sebelum validasi silang.
- **Skenario B — kebocoran informasi target:** ditambah *target encoding* `kode_kelurahan` — rata-rata `berkembang` per kelurahan — yang dihitung dari seluruh data latih. `TargetEncoder` pada cara benar tersedia sejak scikit-learn 1.3.

```python
# =============================================
# LANGKAH 6: Menunjukkan dampak kebocoran
# =============================================
import sklearn
from sklearn.preprocessing import StandardScaler, TargetEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import StratifiedKFold, cross_val_score

kol_num = ["omzet_bulanan", "lama_usaha", "jumlah_pegawai", "modal_awal"]

# Validasi silang 5-lipatan pada data LATIH (pembagian lipatan tetap)
lipatan = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

def skor_cv(model, X_, y_):
    """Rata-rata ROC-AUC dari validasi silang 5-lipatan."""
    return cross_val_score(model, X_, y_, cv=lipatan, scoring="roc_auc").mean()

def klasifikasi():
    return LogisticRegression(max_iter=1000, random_state=RANDOM_STATE)

# ---------- Skenario A: imputasi + penskalaan ----------
# CARA SALAH: median, rata-rata, dan simpangan baku dihitung dari SELURUH
# data latih — termasuk baris yang nanti menjadi lipatan validasi
X_bocor_a = pd.DataFrame(
    StandardScaler().fit_transform(
        SimpleImputer(strategy="median").fit_transform(X_train[kol_num])),
    columns=kol_num, index=X_train.index)
auc_bocor_a = skor_cv(klasifikasi(), X_bocor_a, y_train)

# CARA BENAR: Pipeline — imputasi dan penskalaan di-fit ulang
# HANYA pada empat lipatan latih di setiap putaran
alur_num_demo = Pipeline([
    ("imputasi", SimpleImputer(strategy="median")),
    ("skala", StandardScaler()),
])
pipa_a = Pipeline([("pra", alur_num_demo), ("clf", klasifikasi())])
auc_benar_a = skor_cv(pipa_a, X_train[kol_num], y_train)

# ---------- Skenario B: A + target encoding kode_kelurahan ----------
# CARA SALAH: rata-rata target per kelurahan dihitung dari SELURUH data latih.
# Label baris validasi ikut masuk ke rata-rata kelurahannya sendiri.
rata_per_kelurahan = y_train.groupby(X_train["kode_kelurahan"]).mean()
X_bocor_b = X_bocor_a.copy()
X_bocor_b["kelurahan_te"] = X_train["kode_kelurahan"].map(rata_per_kelurahan)
auc_bocor_b = skor_cv(klasifikasi(), X_bocor_b, y_train)

# CARA BENAR: TargetEncoder di dalam Pipeline — rata-rata per kelurahan
# dihitung ulang pada lipatan latih saja (plus cross fitting internal).
# Cara menetapkan seed-nya berubah pada scikit-learn 1.9:
versi_sklearn = tuple(int(b) for b in sklearn.__version__.split(".")[:2])
if versi_sklearn >= (1, 9):
    penyandi_target = TargetEncoder(cv=StratifiedKFold(
        n_splits=5, shuffle=True, random_state=RANDOM_STATE))
else:
    penyandi_target = TargetEncoder(random_state=RANDOM_STATE)

pipa_b = Pipeline([
    ("pra", ColumnTransformer([
        ("num", alur_num_demo, kol_num),
        ("kel", penyandi_target, ["kode_kelurahan"]),
    ])),
    ("clf", klasifikasi()),
])
auc_benar_b = skor_cv(pipa_b, X_train, y_train)

hasil = pd.DataFrame(
    {"Bocor": [auc_bocor_a, auc_bocor_b],
     "Pipeline": [auc_benar_a, auc_benar_b]},
    index=["A. Imputasi + penskalaan", "B. A + target encoding kelurahan"])
hasil["Selisih"] = hasil["Bocor"] - hasil["Pipeline"]
print("ROC-AUC validasi silang 5-lipatan (rata-rata):")
print(hasil.round(4))

# Kesimpulan DIHITUNG dari hasil, bukan teks tetap
for skenario, baris in hasil.iterrows():
    s = baris["Selisih"]
    if s >= 0.03:
        print(f"{skenario}: skor bocor {s:+.4f} lebih tinggi — "
              "kebocoran menggelembungkan skor secara nyata.")
    elif s > 0.005:
        print(f"{skenario}: skor bocor sedikit lebih tinggi ({s:+.4f}).")
    else:
        print(f"{skenario}: selisih {s:+.4f} — skor praktis tidak berubah, "
              "tetapi prosedurnya tetap salah.")
tambahan = auc_benar_b - auc_benar_a
print(f"Menambah kode_kelurahan dengan cara BENAR mengubah skor {tambahan:+.4f} "
      f"— {'tidak ada informasi baru' if tambahan < 0.02 else 'periksa ulang'}.")
```

```python
# =============================================
# Pemeriksaan otomatis — Langkah 6
# =============================================
selisih_b = auc_bocor_b - auc_benar_b
assert selisih_b >= 0.03, (
    f"Target encoding di luar Pipeline seharusnya menaikkan skor CV "
    f"minimal 0,03 (sekarang {selisih_b:+.4f}) — periksa apakah rata-rata "
    "per kelurahan dihitung dari SELURUH data latih")
assert auc_benar_b < auc_benar_a + 0.02, (
    "kode_kelurahan diundi acak; bila disandikan dengan benar, ia tidak boleh "
    "menaikkan skor — periksa apakah TargetEncoder berada di dalam Pipeline")
print(f"Pemeriksaan otomatis lulus: kebocoran skenario B menaikkan skor "
      f"{selisih_b:+.4f}, sedangkan cara benar tidak memperoleh kenaikan "
      "berarti dari kolom acak.")
```

Pada data lab ini (diuji pada scikit-learn 1.6 dan 1.9), selisih skenario A praktis nol, sedangkan skor skenario B melonjak dari sekitar 0,56 (Pipeline) menjadi sekitar 0,80 (bocor) — padahal `kode_kelurahan` diundi acak.

**Tulis penjelasan:**

1. Pada skenario B, mengapa cara pertama menghasilkan skor yang jauh lebih tinggi, dan mengapa skor itu **tidak jujur**? *Petunjuk:* hitung rata-rata jumlah baris per kelurahan di data latih (`X_train["kode_kelurahan"].value_counts().mean()`), lalu pikirkan seberapa besar andil label **satu** baris validasi terhadap nilai `kelurahan_te` miliknya sendiri. Ingat: `kode_kelurahan` diundi acak.
2. Pada skenario A, mengapa selisihnya hampir nol — dan mengapa prosedurnya **tetap** salah?

> Kebocoran statistik kolom (median, rata-rata, simpangan baku) pada data sebesar ini biasanya hanya menggeser skor sedikit — skenario A. Kebocoran yang membawa **informasi target** — *target encoding* atau seleksi fitur yang memakai target, di luar `Pipeline` — dapat menggelembungkan skor jauh, terutama pada kategori berkardinalitas tinggi dengan sedikit baris per kategori — skenario B. Yang keliru bukan besarnya selisih, melainkan **prosedurnya**: cara salah hanya kebetulan "tidak terlihat" pada skenario A.

### LANGKAH 7: `Pipeline` Lengkap dengan `ColumnTransformer`

```python
# =============================================
# LANGKAH 7: Pipeline lengkap
# =============================================
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, RobustScaler
from sklearn.metrics import roc_auc_score

kol_num = ["omzet_bulanan", "lama_usaha", "jumlah_pegawai", "modal_awal"]
kol_nominal = ["provinsi", "jenis_usaha"]
kol_ordinal = ["pendidikan_pemilik"]
# kode_kelurahan sengaja TIDAK dipakai: kardinalitas tinggi dan diundi acak
# (lihat Langkah 6 dan Tantangan 3) — remainder="drop" membuangnya

# Urutan pendidikan DITENTUKAN sendiri, bukan diserahkan ke abjad
urutan_pendidikan = [["SD", "SMP", "SMA", "D3", "S1", "S2"]]

alur_num = Pipeline([
    ("imputasi", SimpleImputer(strategy="median")),
    # RobustScaler karena omzet dan modal sangat menceng kanan
    ("skala", RobustScaler()),
])

alur_nominal = Pipeline([
    ("imputasi", SimpleImputer(strategy="constant", fill_value="TIDAK_DIKETAHUI")),
    ("sandi", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
])

alur_ordinal = Pipeline([
    ("imputasi", SimpleImputer(strategy="most_frequent")),
    ("sandi", OrdinalEncoder(categories=urutan_pendidikan,
                             handle_unknown="use_encoded_value",
                             unknown_value=-1)),
])

prapemrosesan = ColumnTransformer([
    ("num", alur_num, kol_num),
    ("nom", alur_nominal, kol_nominal),
    ("ord", alur_ordinal, kol_ordinal),
], remainder="drop")

model = Pipeline([
    ("pra", prapemrosesan),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced",
                               random_state=RANDOM_STATE)),
])

model.fit(X_train, y_train)
# roc_auc_score mengembalikan float Python: bulatkan dengan round(), bukan .round()
auc_uji = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
print("ROC-AUC data uji:", round(auc_uji, 4))
```

### LANGKAH 8: Memeriksa Hasil Transformasi

```python
# =============================================
# LANGKAH 8: Apa yang dihasilkan prapemrosesan?
# =============================================
X_tr_transformasi = model.named_steps["pra"].transform(X_train)
nama_kolom = model.named_steps["pra"].get_feature_names_out()

print(f"Kolom sebelum : {X_train.shape[1]}")
print(f"Kolom sesudah : {X_tr_transformasi.shape[1]}")
print(f"\nNama kolom hasil ({len(nama_kolom)}):")
for nm in nama_kolom:
    print("  ", nm)

# Periksa: tidak boleh ada NaN yang tersisa
n_nan = int(np.isnan(X_tr_transformasi).sum())
print("\nNaN tersisa:", n_nan)
```

```python
# =============================================
# Pemeriksaan otomatis — Langkah 7 dan 8
# =============================================
assert n_nan == 0, "Masih ada NaN setelah transformasi — periksa langkah imputasi"
assert "kode_kelurahan" not in " ".join(nama_kolom), (
    "kode_kelurahan seharusnya dibuang oleh ColumnTransformer (remainder='drop')")
n_harap = (len(kol_num) + sum(X_train[k].nunique() for k in kol_nominal)
           + len(kol_ordinal))
assert len(nama_kolom) == n_harap, (
    f"Jumlah kolom hasil {len(nama_kolom)}, seharusnya {n_harap}: numerik + "
    "satu kolom per kategori nominal + satu kolom ordinal")
print("Pemeriksaan otomatis lulus.")
```

---

## Tantangan Tambahan

### Tantangan 1 — Membandingkan Strategi Imputasi

Bandingkan `SimpleImputer(strategy="median")` dengan `KNNImputer(n_neighbors=5)` pada kolom numerik. Laporkan selisih ROC-AUC dan waktu komputasi. Apakah peningkatannya sepadan?

### Tantangan 2 — Penanda Nilai Hilang

Tambahkan `SimpleImputer(add_indicator=True)`. Apakah informasi "nilai ini hilang" sendiri membantu prediksi? Bila ya, apa artinya tentang pola kehilangan pada data ini?

### Tantangan 3 — Kardinalitas Tinggi

Kolom `kode_kelurahan` (300 nilai unik) sengaja tidak dipakai pada Langkah 7. Masukkan ke `ColumnTransformer` dengan empat penanganan: *one-hot* penuh, penggabungan kategori jarang menjadi satu kategori "lainnya" (`OneHotEncoder(min_frequency=..., handle_unknown="infrequent_if_exist")`), *frequency encoding*, dan `TargetEncoder` (pengaturan seperti Langkah 6). Laporkan jumlah kolom hasil dan ROC-AUC masing-masing. Karena kolom ini diundi acak, ia tidak membawa informasi: penurunan skor menandakan model *overfitting* pada derau, sedangkan kenaikan besar dari penanganan mana pun patut dicurigai sebagai kebocoran.

### Tantangan 4 — Janji Skor yang Bocor

Latih model skenario B versi bocor pada **seluruh** data latih, lalu ukur ROC-AUC-nya pada `X_test` (petakan `kode_kelurahan` data uji dengan `rata_per_kelurahan`; kelurahan yang tidak muncul di data latih diisi rata-rata target data latih). Bandingkan dengan skor validasi silang bocornya di Langkah 6. Skor mana yang menggambarkan kinerja model pada UMKM baru?

---

## Checklist Penyelesaian

- [ ] Tujuh perintah pembuka dijalankan dan kelima masalah data diidentifikasi
- [ ] Perbaikan struktural dilakukan dan **dicatat: apa, berapa, mengapa**
- [ ] Pola nilai hilang dianalisis (MCAR/MAR/MNAR) dengan bukti
- [ ] Pembagian data dilakukan **sebelum** prapemrosesan statistik
- [ ] Demonstrasi kebocoran (skenario A dan B) dijalankan, pemeriksaan otomatis lulus, dan selisihnya dijelaskan
- [ ] `ColumnTransformer` memisahkan numerik, nominal, dan ordinal
- [ ] **Ordinal disandikan dengan urutan yang ditentukan sendiri**
- [ ] `handle_unknown="ignore"` dipakai pada `OneHotEncoder`
- [ ] Seluruh transformasi berada **di dalam** `Pipeline`
- [ ] Tidak ada NaN tersisa setelah transformasi
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 3](../03-modules/week-03-data-dan-prapemrosesan.md)
2. [Bab 3 buku ajar](../06-buku-ajar/bab-03-data-dan-prapemrosesan.md)
3. Dokumentasi scikit-learn — *Preprocessing*. <https://scikit-learn.org/stable/modules/preprocessing.html>
4. Dokumentasi scikit-learn — *ColumnTransformer*. <https://scikit-learn.org/stable/modules/compose.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
