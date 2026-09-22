# Lab 05: Rekayasa Fitur

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 5 |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-05 |
| Durasi | 100 menit |
| Prasyarat | Lab 4 selesai |
| Bobot | 1,9% (Observasi) |

---

## Tujuan Praktikum

1. Merancang fitur baru dari data mentah dengan pengetahuan domain.
2. Mengukur sumbangan tiap kelompok fitur terhadap kinerja validasi.
3. Memeriksa setiap fitur baru terhadap risiko kebocoran.
4. Menerapkan pemilihan fitur di dalam `Pipeline`.

---

## Ketentuan Khusus Lab Ini

> **Model dan hiperparameter DIKUNCI.** Hanya fitur yang boleh diubah. Dengan begitu, setiap peningkatan yang terjadi **hanya** dapat berasal dari rekayasa fitur — bukan dari penggantian model.

---

## Langkah-langkah

### LANGKAH 1: Data dengan Fitur Mentah

```python
# =============================================
# LANGKAH 1: Data kemacetan — fitur mentah
# =============================================
import numpy as np, pandas as pd
rng = np.random.default_rng(RANDOM_STATE)
n = 6000

tanggal = pd.date_range("2026-01-01", periods=n, freq="h")
df = pd.DataFrame({"waktu": tanggal})

jam = df["waktu"].dt.hour
hari = df["waktu"].dt.dayofweek

# Kemacetan bergantung pada jam sibuk dan hari kerja
p_macet = 0.10
p_macet = p_macet + 0.45 * jam.isin([6, 7, 8, 16, 17, 18, 19]).astype(float)
p_macet = p_macet - 0.20 * (hari >= 5).astype(float)
p_macet = p_macet + rng.normal(0, 0.05, size=n)
df["macet"] = rng.binomial(1, p_macet.clip(0.02, 0.95))

# Fitur tambahan
df["curah_hujan_mm"] = rng.gamma(1.2, 2.5, size=n).round(1)
df["jumlah_kendaraan"] = (rng.poisson(800, size=n)
                          + 400 * jam.isin([6,7,8,16,17,18,19])).astype(int)
df["ruas"] = rng.choice(["Sudirman", "Gatot Subroto", "Kuningan", "Cawang"], size=n)

print("Dimensi:", df.shape)
print("Proporsi macet:", df["macet"].mean().round(3))
display(df.head())
```

### LANGKAH 2: Model yang Dikunci

```python
# =============================================
# LANGKAH 2: Model DIKUNCI — tidak boleh diubah
# =============================================
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import cross_val_score, StratifiedKFold

# KUNCI: parameter ini tidak boleh diubah sepanjang lab
MODEL_TERKUNCI = RandomForestClassifier(
    n_estimators=200, max_depth=8, min_samples_leaf=20,
    random_state=RANDOM_STATE, n_jobs=-1,
)
CV = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

def evaluasi(X, y, nama):
    kol_kat = X.select_dtypes(include="object").columns.tolist()
    kol_num = X.select_dtypes(include=[np.number]).columns.tolist()
    pra = ColumnTransformer([
        ("num", "passthrough", kol_num),
        ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), kol_kat),
    ])
    pipa = Pipeline([("pra", pra), ("clf", MODEL_TERKUNCI)])
    skor = cross_val_score(pipa, X, y, cv=CV, scoring="f1", n_jobs=-1)
    print(f"{nama:38s} F1 = {skor.mean():.4f} ± {skor.std():.4f}  "
          f"({X.shape[1]} fitur)")
    return skor.mean(), skor.std()

y = df["macet"]
hasil = []
```

### LANGKAH 3: *Baseline* — Waktu sebagai Angka Mentah

```python
# =============================================
# LANGKAH 3: BASELINE — timestamp mentah
# =============================================
X0 = pd.DataFrame({
    "waktu_epoch": df["waktu"].astype("int64") // 10**9,   # detik sejak 1970
    "curah_hujan_mm": df["curah_hujan_mm"],
    "jumlah_kendaraan": df["jumlah_kendaraan"],
    "ruas": df["ruas"],
})
m, s = evaluasi(X0, y, "0. Baseline (timestamp mentah)")
hasil.append({"Tahap": "0. Baseline", "F1": m, "Simpangan": s, "Fitur": X0.shape[1]})
```

### LANGKAH 4: Menambah Fitur Waktu

```python
# =============================================
# LANGKAH 4: Fitur waktu terurai
# =============================================
X1 = X0.drop(columns=["waktu_epoch"]).copy()
X1["jam"] = df["waktu"].dt.hour
X1["hari_minggu"] = df["waktu"].dt.dayofweek
X1["bulan"] = df["waktu"].dt.month
X1["akhir_pekan"] = (df["waktu"].dt.dayofweek >= 5).astype(int)

m, s = evaluasi(X1, y, "1. + fitur waktu terurai")
hasil.append({"Tahap": "1. + waktu terurai", "F1": m, "Simpangan": s, "Fitur": X1.shape[1]})
```

### LANGKAH 5: Penyandian Siklik

```python
# =============================================
# LANGKAH 5: Penyandian siklik
# =============================================
# Jam 23 dan jam 0 berdekatan, tetapi selisih angkanya 23.
X2 = X1.copy()
X2["jam_sin"] = np.sin(2 * np.pi * X2["jam"] / 24)
X2["jam_cos"] = np.cos(2 * np.pi * X2["jam"] / 24)
X2["hari_sin"] = np.sin(2 * np.pi * X2["hari_minggu"] / 7)
X2["hari_cos"] = np.cos(2 * np.pi * X2["hari_minggu"] / 7)

m, s = evaluasi(X2, y, "2. + penyandian siklik")
hasil.append({"Tahap": "2. + siklik", "F1": m, "Simpangan": s, "Fitur": X2.shape[1]})
```

### LANGKAH 6: Pengetahuan Domain

```python
# =============================================
# LANGKAH 6: Fitur dari pengetahuan domain Indonesia
# =============================================
X3 = X2.copy()

# Jam sibuk Jakarta — pengetahuan domain, bukan dari data
X3["jam_sibuk_pagi"] = X3["jam"].isin([6, 7, 8]).astype(int)
X3["jam_sibuk_sore"] = X3["jam"].isin([16, 17, 18, 19]).astype(int)
X3["jam_sibuk"] = (X3["jam_sibuk_pagi"] | X3["jam_sibuk_sore"]).astype(int)
X3["hari_kerja"] = (X3["hari_minggu"] < 5).astype(int)

# Interaksi: jam sibuk pada hari kerja berbeda dari jam sibuk akhir pekan
X3["sibuk_x_kerja"] = X3["jam_sibuk"] * X3["hari_kerja"]

# Hari besar nasional 2026
libur = pd.to_datetime(["2026-01-01", "2026-03-20", "2026-03-21",
                        "2026-05-01", "2026-05-14", "2026-08-17"])
X3["hari_libur"] = df["waktu"].dt.normalize().isin(libur).astype(int)

m, s = evaluasi(X3, y, "3. + pengetahuan domain")
hasil.append({"Tahap": "3. + domain", "F1": m, "Simpangan": s, "Fitur": X3.shape[1]})
```

### LANGKAH 7: Fitur Rasio dan Transformasi

```python
# =============================================
# LANGKAH 7: Rasio dan transformasi
# =============================================
X4 = X3.copy()

# Transformasi log untuk curah hujan (menceng kanan berat)
X4["hujan_log"] = np.log1p(X4["curah_hujan_mm"])
X4["hujan_deras"] = (X4["curah_hujan_mm"] > 10).astype(int)

# Kepadatan relatif terhadap rata-rata ruas
# PERHATIAN: dihitung dari data lengkap -> RAWAN KEBOCORAN.
# Di sini hanya untuk demonstrasi; pada proyek harus di dalam Pipeline.
rata_ruas = df.groupby("ruas")["jumlah_kendaraan"].transform("mean")
X4["kendaraan_relatif"] = X4["jumlah_kendaraan"] / rata_ruas

m, s = evaluasi(X4, y, "4. + rasio dan transformasi")
hasil.append({"Tahap": "4. + rasio", "F1": m, "Simpangan": s, "Fitur": X4.shape[1]})
```

> **Catat sebagai temuan:** fitur `kendaraan_relatif` dihitung dari seluruh data dan karena itu **berisiko bocor**. Pada proyek, perhitungan semacam ini harus berada di dalam `Pipeline` sebagai transformer sendiri, agar di-*fit* hanya pada lipatan latih.

### LANGKAH 8: Ringkasan dan Analisis

```python
# =============================================
# LANGKAH 8: Ringkasan peningkatan
# =============================================
import matplotlib.pyplot as plt

tabel = pd.DataFrame(hasil)
tabel["Peningkatan"] = tabel["F1"] - tabel["F1"].iloc[0]
print(tabel.round(4).to_string(index=False))

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.errorbar(range(len(tabel)), tabel["F1"], yerr=tabel["Simpangan"],
            fmt="o-", capsize=5)
ax.set_xticks(range(len(tabel)))
ax.set_xticklabels(tabel["Tahap"], rotation=20, ha="right")
ax.set_ylabel("F1 (validasi silang 5 lipatan)")
ax.set_title(f"Peningkatan dari rekayasa fitur — model dikunci (n={len(df)})")
plt.tight_layout(); plt.show()
```

**Yang harus ditulis di sel Markdown:**
- Kelompok fitur mana yang memberi peningkatan terbesar?
- Adakah kelompok fitur yang **tidak** membantu? Apa dugaan sebabnya?
- Apakah peningkatannya lebih besar daripada simpangan antarlipatan?

### LANGKAH 9: Pemilihan Fitur di Dalam `Pipeline`

```python
# =============================================
# LANGKAH 9: Pemilihan fitur — di dalam Pipeline
# =============================================
from sklearn.feature_selection import SelectKBest, f_classif

kol_kat = X4.select_dtypes(include="object").columns.tolist()
kol_num = X4.select_dtypes(include=[np.number]).columns.tolist()

for k in [5, 10, 15, X4.shape[1]]:
    pra = ColumnTransformer([
        ("num", "passthrough", kol_num),
        ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), kol_kat),
    ])
    pipa = Pipeline([
        ("pra", pra),
        ("pilih", SelectKBest(f_classif, k=min(k, 30))),   # DI DALAM Pipeline
        ("clf", MODEL_TERKUNCI),
    ])
    skor = cross_val_score(pipa, X4, y, cv=CV, scoring="f1", n_jobs=-1)
    print(f"k={k:3d}: F1 = {skor.mean():.4f} ± {skor.std():.4f}")
```

> **Perhatikan penempatannya.** `SelectKBest` berada **di dalam** `Pipeline`, sehingga pada tiap lipatan ia di-*fit* ulang hanya dari data latih lipatan itu. Menempatkannya di luar adalah kebocoran — sebagaimana ditunjukkan pada Lab 4.

---

## Tantangan Tambahan

### Tantangan 1 — Transformer Agregat yang Aman

Bangun `FunctionTransformer` atau kelas transformer sendiri yang menghitung `kendaraan_relatif` **di dalam** `Pipeline`, sehingga rata-rata per ruas dihitung hanya dari lipatan latih. Bandingkan skornya dengan versi yang bocor pada Langkah 7.

### Tantangan 2 — Fitur yang Gagal

Tambahkan lima fitur yang Anda duga akan membantu tetapi ternyata tidak. Catat masing-masing beserta dugaan sebabnya. **Catatan fitur yang gagal dinilai setara dengan yang berhasil.**

### Tantangan 3 — Kutukan Dimensi

Tambahkan `PolynomialFeatures(degree=2)` pada fitur numerik. Berapa kolom yang dihasilkan? Apakah F1 naik atau turun? Jelaskan hubungannya dengan kutukan dimensi dan jumlah baris data.

---

## Checklist Penyelesaian

- [ ] Model dan hiperparameter **tetap terkunci** sepanjang lab
- [ ] *Baseline* dengan fitur mentah dijalankan lebih dahulu
- [ ] Minimal empat kelompok fitur ditambahkan **bertahap**
- [ ] Skor diukur pada **validasi silang**, bukan pada data latih
- [ ] Simpangan antarlipatan dilaporkan di setiap tahap
- [ ] **Catatan fitur yang gagal** beserta dugaan sebabnya
- [ ] Fitur berisiko kebocoran diidentifikasi dan dinyatakan
- [ ] Pemilihan fitur ditempatkan **di dalam** `Pipeline`
- [ ] Grafik peningkatan dengan pita simpangan
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 5](../03-modules/week-05-rekayasa-fitur.md)
2. [Bab 5 buku ajar](../06-buku-ajar/bab-05-rekayasa-fitur.md)
3. Zheng, A., & Casari, A. (2018). *Feature Engineering for Machine Learning*. O'Reilly.
4. Dokumentasi scikit-learn — *Feature selection*. <https://scikit-learn.org/stable/modules/feature_selection.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
