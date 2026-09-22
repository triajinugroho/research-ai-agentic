# Lab 06: Model Regresi dan Metriknya

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 6 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-06 |
| Durasi | 100 menit |
| Prasyarat | Lab 5 selesai |
| Bobot | 1,9% (Observasi) |

---

## Tujuan Praktikum

1. Membangun dan membandingkan regresi linear, Ridge, dan Lasso.
2. Menentukan α melalui validasi silang, bukan dengan menebak.
3. Menghitung dan menafsirkan MAE, RMSE, R², dan MAPE.
4. Menjelaskan mengapa metrik yang berbeda memberi kesimpulan yang berbeda.

---

## Langkah-langkah

### LANGKAH 1: Data Harga Properti Jabodetabek

```python
# =============================================
# LANGKAH 1: Data
# =============================================
import numpy as np, pandas as pd
rng = np.random.default_rng(RANDOM_STATE)
n = 2500

df = pd.DataFrame({
    "luas_bangunan": rng.gamma(4.0, 25, size=n).round(0).clip(24, 600),
    "luas_tanah":    rng.gamma(4.0, 30, size=n).round(0).clip(36, 900),
    "kamar_tidur":   rng.integers(1, 7, size=n),
    "kamar_mandi":   rng.integers(1, 5, size=n),
    "umur_bangunan": rng.gamma(2.0, 6, size=n).round(0).clip(0, 50),
    "jarak_pusat_km":rng.gamma(2.5, 5, size=n).round(1).clip(0.5, 60),
    "kota": rng.choice(["Jakarta Selatan", "Jakarta Timur", "Tangerang",
                        "Bekasi", "Depok", "Bogor"], size=n,
                       p=[0.18, 0.15, 0.20, 0.20, 0.15, 0.12]),
})

pengali_kota = {"Jakarta Selatan": 2.4, "Jakarta Timur": 1.6, "Tangerang": 1.2,
                "Bekasi": 1.0, "Depok": 1.1, "Bogor": 0.85}

df["harga_jt"] = (
    (8.5 * df["luas_bangunan"] + 4.2 * df["luas_tanah"]
     + 40 * df["kamar_tidur"] + 25 * df["kamar_mandi"]
     - 6 * df["umur_bangunan"] - 9 * df["jarak_pusat_km"])
    * df["kota"].map(pengali_kota)
    * rng.lognormal(0, 0.18, size=n)
).round(0).clip(lower=150)

print("Dimensi:", df.shape)
print("\nSebaran harga (juta rupiah):")
print(df["harga_jt"].describe().round(1))
display(df.head())
```

### LANGKAH 2: Melihat Data Sebelum Memodelkan

```python
# =============================================
# LANGKAH 2: Eksplorasi wajib
# =============================================
import matplotlib.pyplot as plt, seaborn as sns

fig, ax = plt.subplots(1, 3, figsize=(15, 4.2))

ax[0].hist(df["harga_jt"], bins=40, edgecolor="white")
ax[0].set_xlabel("Harga (juta Rp)"); ax[0].set_ylabel("Frekuensi")
ax[0].set_title(f"Sebaran harga (n={len(df)})")

sns.scatterplot(data=df, x="luas_bangunan", y="harga_jt", alpha=0.3, ax=ax[1])
ax[1].set_xlabel("Luas bangunan (m²)"); ax[1].set_ylabel("Harga (juta Rp)")
ax[1].set_title("Luas bangunan vs harga")

sns.boxplot(data=df, x="kota", y="harga_jt", ax=ax[2])
ax[2].set_xlabel(""); ax[2].set_ylabel("Harga (juta Rp)")
ax[2].set_title("Harga per kota")
ax[2].tick_params(axis="x", rotation=35)

plt.tight_layout(); plt.show()

print("Kemencengan harga:", df["harga_jt"].skew().round(3))
```

**Catat:** apakah sebaran harga menceng? Apa akibatnya bagi pemilihan antara MAE dan RMSE?

### LANGKAH 3: Pembagian dan *Baseline*

```python
# =============================================
# LANGKAH 3: Pembagian dan baseline
# =============================================
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.metrics import (mean_absolute_error, mean_squared_error,
                             r2_score, mean_absolute_percentage_error)

X = df.drop(columns=["harga_jt"])
y = df["harga_jt"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE)

def metrik(y_true, y_pred, nama):
    return {
        "Model": nama,
        "MAE":   mean_absolute_error(y_true, y_pred),
        "RMSE":  np.sqrt(mean_squared_error(y_true, y_pred)),
        "R2":    r2_score(y_true, y_pred),
        "MAPE%": mean_absolute_percentage_error(y_true, y_pred) * 100,
    }

hasil = []
for strat in ["mean", "median"]:
    d = DummyRegressor(strategy=strat).fit(X_train, y_train)
    hasil.append(metrik(y_test, d.predict(X_test), f"Baseline ({strat})"))

print(pd.DataFrame(hasil).round(3).to_string(index=False))
```

### LANGKAH 4: Perhitungan Manual Metrik

```python
# =============================================
# LANGKAH 4: Hitung manual, lalu verifikasi
# =============================================
# Lima pengamatan pertama dari data uji
y_contoh = y_test.iloc[:5].values
d = DummyRegressor(strategy="median").fit(X_train, y_train)
p_contoh = d.predict(X_test.iloc[:5])

tabel = pd.DataFrame({
    "Sebenarnya": y_contoh,
    "Prediksi":   p_contoh.round(1),
})
tabel["Galat"]       = (tabel["Prediksi"] - tabel["Sebenarnya"]).round(1)
tabel["|Galat|"]     = tabel["Galat"].abs()
tabel["Galat^2"]     = (tabel["Galat"] ** 2).round(1)
tabel["|Galat|/y"]   = (tabel["|Galat|"] / tabel["Sebenarnya"]).round(4)
print(tabel.to_string(index=False))

mae_manual  = tabel["|Galat|"].mean()
mse_manual  = tabel["Galat^2"].mean()
rmse_manual = np.sqrt(mse_manual)
mape_manual = tabel["|Galat|/y"].mean() * 100

print(f"\nManual — MAE  : {mae_manual:.2f}")
print(f"Manual — RMSE : {rmse_manual:.2f}")
print(f"Manual — MAPE : {mape_manual:.2f}%")

print(f"\nVerifikasi sklearn — MAE : "
      f"{mean_absolute_error(y_contoh, p_contoh):.2f}")
print(f"Verifikasi sklearn — RMSE: "
      f"{np.sqrt(mean_squared_error(y_contoh, p_contoh)):.2f}")
```

> **Bentuk soal ini muncul pada UTS.** Berlatihlah menghitungnya dengan kalkulator, bukan dengan kode.

### LANGKAH 5: Tiga Model Regresi

```python
# =============================================
# LANGKAH 5: Linear, Ridge, Lasso
# =============================================
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV

kol_num = ["luas_bangunan", "luas_tanah", "kamar_tidur", "kamar_mandi",
           "umur_bangunan", "jarak_pusat_km"]
kol_kat = ["kota"]

def buat_pipa(regresor):
    pra = ColumnTransformer([
        # PENSKALAAN WAJIB sebelum regularisasi
        ("num", StandardScaler(), kol_num),
        ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), kol_kat),
    ])
    return Pipeline([("pra", pra), ("reg", regresor)])

alphas = np.logspace(-3, 3, 60)
model_kandidat = {
    "Regresi linear": LinearRegression(),
    "Ridge (alpha via CV)": RidgeCV(alphas=alphas, cv=5),
    "Lasso (alpha via CV)": LassoCV(alphas=alphas, cv=5, max_iter=20000,
                                    random_state=RANDOM_STATE),
}

pipa_terlatih = {}
for nama, reg in model_kandidat.items():
    pipa = buat_pipa(reg).fit(X_train, y_train)
    pipa_terlatih[nama] = pipa
    hasil.append(metrik(y_test, pipa.predict(X_test), nama))

tabel_hasil = pd.DataFrame(hasil)
print(tabel_hasil.round(3).to_string(index=False))
```

### LANGKAH 6: α yang Terpilih dan Koefisien

```python
# =============================================
# LANGKAH 6: Alpha dan koefisien
# =============================================
ridge = pipa_terlatih["Ridge (alpha via CV)"].named_steps["reg"]
lasso = pipa_terlatih["Lasso (alpha via CV)"].named_steps["reg"]

print(f"Alpha Ridge terpilih: {ridge.alpha_:.4f}")
print(f"Alpha Lasso terpilih: {lasso.alpha_:.4f}")

nama_fitur = pipa_terlatih["Ridge (alpha via CV)"].named_steps["pra"].get_feature_names_out()

koef = pd.DataFrame({
    "Fitur":  nama_fitur,
    "Linear": pipa_terlatih["Regresi linear"].named_steps["reg"].coef_,
    "Ridge":  ridge.coef_,
    "Lasso":  lasso.coef_,
}).round(2)

print("\nKoefisien (pada skala terstandardisasi):")
print(koef.to_string(index=False))

n_nol = (np.abs(lasso.coef_) < 1e-8).sum()
print(f"\nKoefisien yang dinolkan Lasso: {n_nol} dari {len(lasso.coef_)}")
if n_nol:
    print("Fitur yang dibuang Lasso:",
          list(koef.loc[np.abs(lasso.coef_) < 1e-8, "Fitur"]))
```

**Tulis tafsiran:** fitur apa yang dinolkan Lasso? Apakah masuk akal secara domain?

### LANGKAH 7: Mengapa Metrik Berbeda Kesimpulannya

```python
# =============================================
# LANGKAH 7: Metrik yang berbeda, urutan yang berbeda
# =============================================
t = tabel_hasil.set_index("Model")

print("Peringkat menurut MAE (makin kecil makin baik):")
print(t["MAE"].sort_values().round(2).to_string())
print("\nPeringkat menurut RMSE:")
print(t["RMSE"].sort_values().round(2).to_string())
print("\nPeringkat menurut MAPE%:")
print(t["MAPE%"].sort_values().round(2).to_string())

print("\nRasio RMSE/MAE per model:")
print((t["RMSE"] / t["MAE"]).round(3).to_string())
```

> **Rasio RMSE/MAE adalah petunjuk.** Rasio mendekati 1 berarti galat tersebar merata; rasio besar berarti ada sedikit galat yang sangat besar dan mendominasi RMSE.

### LANGKAH 8: Diagnostik Residual

```python
# =============================================
# LANGKAH 8: Memeriksa residual
# =============================================
model_terbaik = pipa_terlatih["Ridge (alpha via CV)"]
prediksi = model_terbaik.predict(X_test)
residual = y_test - prediksi

fig, ax = plt.subplots(1, 3, figsize=(15, 4.2))

ax[0].scatter(prediksi, residual, alpha=0.3)
ax[0].axhline(0, color="red", ls="--")
ax[0].set_xlabel("Prediksi (juta Rp)"); ax[0].set_ylabel("Residual")
ax[0].set_title("Residual vs prediksi")

ax[1].hist(residual, bins=40, edgecolor="white")
ax[1].set_xlabel("Residual"); ax[1].set_ylabel("Frekuensi")
ax[1].set_title("Sebaran residual")

from scipy import stats
stats.probplot(residual, dist="norm", plot=ax[2])
ax[2].set_title("Q-Q plot residual")

plt.tight_layout(); plt.show()

print("Rata-rata residual:", residual.mean().round(2))
print("Kemencengan residual:", residual.skew().round(3))
```

**Tulis diagnosis:** adakah pola corong pada grafik pertama? Bila ada, asumsi mana yang dilanggar dan apa akibatnya?

---

## Tantangan Tambahan

### Tantangan 1 — Transformasi Target

Latih model pada `log(harga)` alih-alih `harga`, lalu kembalikan prediksinya dengan `exp`. Bandingkan MAE, RMSE, dan MAPE dengan model asli. Manakah yang lebih baik, dan mengapa?

### Tantangan 2 — Kurva Regularisasi

Buat grafik R² validasi terhadap α pada rentang `np.logspace(-3, 4, 40)` untuk Ridge. Tandai α optimum. Apa yang terjadi pada kedua ujung rentang?

### Tantangan 3 — Regresi Polinomial

Tambahkan `PolynomialFeatures(degree=2)` sebelum regresi. Bandingkan R² latih dan R² uji. Adakah tanda *overfitting*? Bandingkan pula dengan derajat 3.

---

## Checklist Penyelesaian

- [ ] Eksplorasi data dilakukan **sebelum** memodelkan
- [ ] *Baseline* `DummyRegressor` dibangun
- [ ] **Perhitungan manual** MAE, RMSE, MAPE diverifikasi dengan sklearn
- [ ] Penskalaan berada **sebelum** regularisasi, di dalam `Pipeline`
- [ ] α ditentukan dengan validasi silang, bukan ditebak
- [ ] Koefisien ketiga model dibandingkan
- [ ] **Fitur yang dinolkan Lasso** diidentifikasi dan ditafsirkan
- [ ] Peringkat menurut metrik berbeda dibandingkan dan dijelaskan
- [ ] Diagnostik residual dijalankan dan didiagnosis
- [ ] Setiap keluaran disertai kalimat penafsiran
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 6](../03-modules/week-06-regresi-dan-metriknya.md)
2. [Bab 6 buku ajar](../06-buku-ajar/bab-06-regresi-dan-metriknya.md)
3. Dokumentasi scikit-learn — *Linear Models*. <https://scikit-learn.org/stable/modules/linear_model.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
