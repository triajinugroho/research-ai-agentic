# Lab 04: Validasi Silang dan Perburuan Kebocoran

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 4 |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-04 |
| Durasi | 100 menit |
| Prasyarat | Lab 3 selesai |
| Bobot | 1,9% (Observasi) |

---

## Tujuan Praktikum

1. Menemukan dan menjelaskan mekanisme empat jenis kebocoran data.
2. Memperbaiki kebocoran dan mengukur dampaknya terhadap skor.
3. Menerapkan strategi pembagian data yang sesuai sifat datanya.
4. Menafsirkan sebaran skor antarlipatan pada validasi silang.

---

## Langkah-langkah

### LANGKAH 1: Data Uji dengan Empat Kebocoran

```python
# =============================================
# LANGKAH 1: Data dengan struktur yang rawan bocor
# =============================================
import numpy as np, pandas as pd
rng = np.random.default_rng(RANDOM_STATE)
n = 3000

tanggal = pd.date_range("2024-01-01", periods=n, freq="6h")

df = pd.DataFrame({
    "tanggal":        tanggal,
    "id_pelanggan":   rng.integers(1, 401, size=n),   # pelanggan BERULANG
    "durasi_sesi":    rng.gamma(2.0, 8, size=n).round(1),
    "jumlah_klik":    rng.poisson(12, size=n),
    "nilai_keranjang":rng.gamma(2.0, 150_000, size=n).round(0),
    "kategori":       rng.choice(["Elektronik", "Fashion", "Makanan", "Buku"], size=n),
})

# Target: pembelian terjadi atau tidak
logit = (-1.4 + 0.035 * df["durasi_sesi"] + 0.06 * df["jumlah_klik"]
         + 0.0000012 * df["nilai_keranjang"])
df["beli"] = rng.binomial(1, 1 / (1 + np.exp(-logit)))

# KEBOCORAN TARGET: kolom yang hanya ada SETELAH pembelian terjadi
df["nomor_invoice"] = np.where(df["beli"] == 1,
                               rng.integers(10_000, 99_999, size=n), 0)

print("Dimensi:", df.shape)
print("Proporsi target:", df["beli"].mean().round(3))
print("Pelanggan unik:", df["id_pelanggan"].nunique(), "dari", n, "baris")
display(df.head())
```

### LANGKAH 2: Notebook yang Salah — Empat Kebocoran Sekaligus

```python
# =============================================
# LANGKAH 2: KODE YANG SALAH — jangan ditiru
# =============================================
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

kol_fitur = ["durasi_sesi", "jumlah_klik", "nilai_keranjang", "nomor_invoice"]
X_salah = df[kol_fitur].copy()
y = df["beli"]

# BOCOR 1: penskalaan pada SELURUH data
X_salah = pd.DataFrame(StandardScaler().fit_transform(X_salah),
                       columns=kol_fitur)

# BOCOR 2: pemilihan fitur memakai SELURUH y
pemilih = SelectKBest(f_classif, k=3).fit(X_salah, y)
X_salah = pd.DataFrame(pemilih.transform(X_salah),
                       columns=np.array(kol_fitur)[pemilih.get_support()])

# BOCOR 3: pembagian ACAK padahal data punya urutan waktu
# BOCOR 4 (di dalam data): kolom nomor_invoice adalah turunan target
Xtr, Xte, ytr, yte = train_test_split(X_salah, y, test_size=0.2,
                                      random_state=RANDOM_STATE)

m = RandomForestClassifier(n_estimators=200, random_state=RANDOM_STATE, n_jobs=-1)
m.fit(Xtr, ytr)
auc_salah = roc_auc_score(yte, m.predict_proba(Xte)[:, 1])
print(f"ROC-AUC (dengan kebocoran): {auc_salah:.4f}")
```

**Tugas:** tulis di sel Markdown — temukan keempat kebocoran, sebutkan barisnya, dan jelaskan **mekanismenya** (bagaimana informasi berpindah dari tempat yang seharusnya tersembunyi).

### LANGKAH 3: Memperbaiki Kebocoran Satu per Satu

```python
# =============================================
# LANGKAH 3: Perbaikan bertahap — ukur dampak tiap perbaikan
# =============================================
from sklearn.pipeline import Pipeline

hasil = [{"Tahap": "Seluruh kebocoran", "ROC-AUC": auc_salah}]

# Perbaikan 1: buang kolom bocor target
kol_bersih = ["durasi_sesi", "jumlah_klik", "nilai_keranjang"]
X = df[kol_bersih]

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                      random_state=RANDOM_STATE)
p = Pipeline([("skala", StandardScaler()),
              ("clf", RandomForestClassifier(n_estimators=200,
                                             random_state=RANDOM_STATE, n_jobs=-1))])
p.fit(Xtr, ytr)
hasil.append({"Tahap": "+ buang kolom bocor target",
              "ROC-AUC": roc_auc_score(yte, p.predict_proba(Xte)[:, 1])})

# Perbaikan 2: pembagian TEMPORAL, bukan acak
batas = int(len(df) * 0.8)
Xtr_t, Xte_t = X.iloc[:batas], X.iloc[batas:]
ytr_t, yte_t = y.iloc[:batas], y.iloc[batas:]
p2 = Pipeline([("skala", StandardScaler()),
               ("clf", RandomForestClassifier(n_estimators=200,
                                              random_state=RANDOM_STATE, n_jobs=-1))])
p2.fit(Xtr_t, ytr_t)
hasil.append({"Tahap": "+ pembagian temporal",
              "ROC-AUC": roc_auc_score(yte_t, p2.predict_proba(Xte_t)[:, 1])})

tabel = pd.DataFrame(hasil)
tabel["Penurunan"] = tabel["ROC-AUC"].iloc[0] - tabel["ROC-AUC"]
print(tabel.round(4).to_string(index=False))
```

**Tulis kesimpulan:** perbaikan mana yang paling besar dampaknya? Mengapa?

### LANGKAH 4: Pembagian Berkelompok

```python
# =============================================
# LANGKAH 4: Kebocoran kelompok — pelanggan berulang
# =============================================
from sklearn.model_selection import GroupKFold, cross_val_score, StratifiedKFold

grup = df["id_pelanggan"]

pipa = Pipeline([("skala", StandardScaler()),
                 ("clf", RandomForestClassifier(n_estimators=200,
                                                random_state=RANDOM_STATE, n_jobs=-1))])

# Tanpa memperhatikan kelompok — pelanggan yang sama ada di latih DAN uji
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
skor_biasa = cross_val_score(pipa, X, y, cv=skf, scoring="roc_auc", n_jobs=-1)

# Dengan GroupKFold — seluruh baris satu pelanggan di lipatan yang sama
gkf = GroupKFold(n_splits=5)
skor_grup = cross_val_score(pipa, X, y, cv=gkf, groups=grup,
                            scoring="roc_auc", n_jobs=-1)

print(f"StratifiedKFold : {skor_biasa.mean():.4f} ± {skor_biasa.std():.4f}")
print(f"GroupKFold      : {skor_grup.mean():.4f} ± {skor_grup.std():.4f}")
print(f"Selisih         : {skor_biasa.mean() - skor_grup.mean():+.4f}")
```

> Pada data ini 400 pelanggan menghasilkan 3.000 baris — rata-rata 7,5 baris per pelanggan. Semakin banyak baris per entitas, semakin besar selisihnya.

### LANGKAH 5: Pembagian Temporal dengan `TimeSeriesSplit`

```python
# =============================================
# LANGKAH 5: TimeSeriesSplit
# =============================================
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)

print("Struktur lipatan temporal:")
for i, (i_tr, i_te) in enumerate(tscv.split(X), 1):
    print(f"  Lipatan {i}: latih=[0:{i_tr[-1]+1}]  uji=[{i_te[0]}:{i_te[-1]+1}]")

skor_ts = cross_val_score(pipa, X, y, cv=tscv, scoring="roc_auc", n_jobs=-1)
print(f"\nROC-AUC per lipatan: {np.round(skor_ts, 4)}")
print(f"Rerata: {skor_ts.mean():.4f} ± {skor_ts.std():.4f}")
```

**Perhatikan:** pada `TimeSeriesSplit`, data latih selalu **mendahului** data uji, dan ukurannya bertambah tiap lipatan.

### LANGKAH 6: Membaca Sebaran Antarlipatan

```python
# =============================================
# LANGKAH 6: Rerata saja menyembunyikan informasi
# =============================================
import matplotlib.pyplot as plt

perbandingan = pd.DataFrame({
    "StratifiedKFold": skor_biasa,
    "GroupKFold":      skor_grup,
    "TimeSeriesSplit": skor_ts,
})

print(perbandingan.describe().T[["mean", "std", "min", "max"]].round(4))

perbandingan.plot(kind="box", figsize=(8, 4.5))
plt.ylabel("ROC-AUC")
plt.title(f"Sebaran skor antarlipatan menurut strategi pembagian (n={len(df)})")
plt.tight_layout(); plt.show()
```

| Simpangan | Tafsir |
|-----------|--------|
| < 0,02 | Kinerja stabil |
| 0,02–0,05 | Wajar pada data terbatas |
| > 0,10 | Selidiki lipatan yang menyimpang |

### LANGKAH 7: Daftar Periksa Kebocoran

```python
# =============================================
# LANGKAH 7: Daftar periksa — jalankan sebelum mengumpulkan
# =============================================
# Salin ke sel Markdown dan centang:
#
# - [ ] Seluruh transformasi di dalam Pipeline
# - [ ] fit() hanya pada data latih
# - [ ] Data uji tidak dipakai memilih model/fitur/hiperparameter
# - [ ] Ada urutan waktu -> pembagian temporal
# - [ ] Ada entitas berulang -> GroupKFold
# - [ ] Duplikat diperiksa sebelum pembagian
# - [ ] Tiap fitur lolos: "tersedia saat prediksi dibutuhkan?"
# - [ ] Tidak ada fitur turunan target
# - [ ] Skor mencurigakan tinggi sudah diselidiki
```

---

## Tantangan Tambahan

### Tantangan 1 — Menyusun Kebocoran Sendiri

Buat satu jenis kebocoran baru yang belum ada pada lab ini (misalnya *target encoding* di luar `Pipeline`), tunjukkan dampaknya, lalu perbaiki.

### Tantangan 2 — Berapa Banyak Data yang Dibutuhkan

Jalankan validasi silang dengan `n_splits` 3, 5, dan 10. Bandingkan rerata dan simpangannya. Apa yang terjadi pada simpangan seiring bertambahnya lipatan, dan mengapa?

### Tantangan 3 — Menelusuri Lipatan yang Menyimpang

Pada `GroupKFold`, temukan lipatan dengan skor terendah. Periksa ciri pelanggan pada lipatan itu — adakah yang membedakannya? Temuan semacam ini sering mengungkap kelompok yang kurang terwakili.

---

## Checklist Penyelesaian

- [ ] Keempat kebocoran ditemukan dan **mekanismenya dijelaskan**
- [ ] Dampak tiap perbaikan diukur dan dilaporkan
- [ ] `GroupKFold` diterapkan dan selisihnya dibahas
- [ ] `TimeSeriesSplit` diterapkan dan struktur lipatannya ditampilkan
- [ ] **Rerata dan simpangan** dilaporkan, bukan rerata saja
- [ ] Sebaran antarlipatan divisualisasikan
- [ ] Daftar periksa kebocoran dicentang
- [ ] Laporan temuan satu halaman disertakan
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 4](../03-modules/week-04-pembagian-data-dan-kebocoran.md)
2. [Bab 4 buku ajar](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md)
3. Kapoor, S., & Narayanan, A. (2023). Leakage and the Reproducibility Crisis in ML-based Science. *Patterns*, 4(9).
4. Dokumentasi scikit-learn — *Cross-validation*. <https://scikit-learn.org/stable/modules/cross_validation.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
