# Lab 06: Model Regresi dan Metriknya

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 6 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-06 |
| Durasi | 100 menit |
| Prasyarat | Lab 5 selesai |
| Bobot | 1,875% (Observasi, Sub-CPMK082-1) |
| Diuji pada | scikit-learn 1.6 dan 1.9, pandas 2.2 dan 3.0 (Oktober 2026) |

---

## Tujuan Praktikum

1. Membangun dan membandingkan regresi linear, Ridge, dan Lasso.
2. Menentukan α melalui validasi silang, bukan dengan menebak.
3. Menghitung dan menafsirkan MAE, RMSE, R², dan MAPE.
4. Menjelaskan mengapa metrik yang berbeda memberi kesimpulan yang berbeda.

---

## Persiapan

1. Buat notebook baru bernama `NIM_Nama_Lab06.ipynb`.
2. Jalankan **sel pembuka baku** di [Lampiran D](../06-buku-ajar/lampiran.md#lampiran-d-sel-pembuka-baku) — mengimpor pustaka, mencatat versi, dan menetapkan `RANDOM_STATE = 42`. Seluruh langkah di bawah mengandaikan sel itu sudah dijalankan.
3. **Data:** data sintetis (simulasi) yang meniru pola iklan jual rumah di Jabodetabek; **bukan data resmi BPS/lembaga** dan bukan hasil pengambilan dari portal properti mana pun. Data dibangkitkan pada Langkah 1. Karena sintetis, kita tahu "kebenarannya", dan kebenaran itu sengaja dirancang untuk menguji regularisasi:
   - **Fitur inti** (`luas_bangunan`, `luas_tanah`, `kamar_tidur`, `kamar_mandi`, `umur_bangunan`, `jarak_pusat_km`, `kota`) — **hanya** kolom-kolom inilah yang dipakai rumus pembangkit harga.
   - **Fitur kolinear** (`waktu_tempuh_menit`, `daya_listrik_va`) — turunan dari fitur inti (jarak dan luas bangunan), **tidak** dipakai rumus harga; informasinya hampir kembar dengan fitur asalnya (korelasi > 0,9).
   - **Kolom derau** (sepuluh kolom metadata iklan dan alamat, mis. `id_iklan`, `jam_unggah`, `nomor_rumah`) — diundi acak sehingga **tidak berhubungan** dengan harga.

---

## Langkah-langkah

### LANGKAH 1: Data Harga Rumah Jabodetabek (Sintetis)

> **Data sintetis (simulasi)** — lihat Persiapan butir 3. Iklan properti sungguhan memang memuat banyak kolom yang tidak menentukan harga; di sini kolom-kolom itu sengaja ditanam agar kerja Lasso dapat **diperiksa**, bukan sekadar dipercaya.

```python
# =============================================
# LANGKAH 1: Data SINTETIS harga rumah Jabodetabek
# (simulasi iklan jual rumah — bukan data resmi BPS/lembaga)
# =============================================
import numpy as np, pandas as pd
rng = np.random.default_rng(RANDOM_STATE)
n = 1000

# --- Fitur inti: satu-satunya yang dipakai rumus harga ---
df = pd.DataFrame({
    "luas_bangunan": rng.gamma(4.0, 25, size=n).round(0).clip(24, 600),
    "luas_tanah":    rng.gamma(4.0, 30, size=n).round(0).clip(36, 900),
})
# Rumah yang lebih luas wajar memiliki kamar lebih banyak (korelasi alami)
df["kamar_tidur"] = (df["luas_bangunan"] / 35
                     + rng.normal(0, 0.7, size=n)).round(0).clip(1, 6).astype(int)
df["kamar_mandi"] = (df["kamar_tidur"] * 0.6
                     + rng.normal(0, 0.5, size=n)).round(0).clip(1, 4).astype(int)
df["umur_bangunan"]  = rng.gamma(2.0, 6, size=n).round(0).clip(0, 50)
df["jarak_pusat_km"] = rng.gamma(2.5, 5, size=n).round(1).clip(0.5, 60)
df["kota"] = rng.choice(["Jakarta Selatan", "Jakarta Timur", "Tangerang",
                         "Bekasi", "Depok", "Bogor"], size=n,
                        p=[0.18, 0.15, 0.20, 0.20, 0.15, 0.12])

# --- Fitur kolinear: turunan fitur inti, TIDAK dipakai rumus harga ---
KOLOM_KOLINEAR = ["waktu_tempuh_menit", "daya_listrik_va"]
df["waktu_tempuh_menit"] = (df["jarak_pusat_km"] * 2.5
                            + rng.normal(0, 4, size=n)).round(0).clip(lower=5)
df["daya_listrik_va"] = np.select(       # golongan daya listrik rumah tangga
    [df["luas_bangunan"] < 60, df["luas_bangunan"] < 100,
     df["luas_bangunan"] < 150, df["luas_bangunan"] < 220],
    [1300, 2200, 3500, 4400], default=5500)

# --- Kolom derau: metadata iklan yang diundi acak, TIDAK berhubungan dengan harga ---
derau = {
    "id_iklan":              rng.permutation(n) + 100001,
    "nomor_rumah":           rng.integers(1, 151, size=n),
    "nomor_rt":              rng.integers(1, 16, size=n),
    "bulan_tayang":          rng.integers(1, 13, size=n),
    "jam_unggah":            rng.integers(0, 24, size=n),
    "lama_tayang_hari":      rng.integers(1, 181, size=n),
    "jumlah_foto_iklan":     rng.integers(3, 31, size=n),
    "panjang_judul_iklan":   rng.integers(20, 101, size=n),
    "jumlah_kata_deskripsi": rng.integers(30, 301, size=n),
    "digit_akhir_telepon":   rng.integers(0, 10, size=n),
}
for kolom, nilai in derau.items():
    df[kolom] = nilai
KOLOM_DERAU = list(derau)

# --- Rumus pembangkit harga (juta rupiah): HANYA fitur inti ---
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
print(f"Kolom kolinear: {KOLOM_KOLINEAR}")
print(f"Kolom derau   : {len(KOLOM_DERAU)} kolom")
print("\nSebaran harga (juta rupiah):")
print(df["harga_jt"].describe().round(1))
print("\nLima baris pertama (ditranspos agar semua kolom terlihat):")
print(df.head().T)
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

print("Kemencengan harga:", round(df["harga_jt"].skew(), 3))

# Pasangan fitur yang dicurigai kolinear
kol_cek = ["luas_bangunan", "daya_listrik_va", "kamar_tidur",
           "jarak_pusat_km", "waktu_tempuh_menit"]
print("\nKorelasi antar-fitur yang dicurigai kolinear:")
print(df[kol_cek].corr().round(2))
```

**Catat:** (1) apakah sebaran harga menceng? Apa akibatnya bagi pemilihan antara MAE dan RMSE? (2) Pasangan fitur mana yang korelasinya sangat tinggi (> 0,8)? Simpan catatan ini untuk Langkah 6.

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
import warnings
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.exceptions import ConvergenceWarning

kol_kat = ["kota"]
kol_num = [k for k in X.columns if k not in kol_kat]   # fitur inti + kolinear + derau

def buat_pipa(regresor):
    pra = ColumnTransformer([
        # PENSKALAAN WAJIB sebelum regularisasi — dan berada DI DALAM Pipeline
        ("num", StandardScaler(), kol_num),
        # Kota: one-hot dengan Bekasi sebagai kategori acuan (drop="first"
        # menghindari jebakan dummy), lalu ikut diskalakan agar denda α
        # berlaku adil untuk SEMUA kolom
        ("kat", Pipeline([
            ("ohe", OneHotEncoder(drop="first", handle_unknown="ignore",
                                  sparse_output=False)),
            ("skala", StandardScaler()),
        ]), kol_kat),
    ])
    return Pipeline([("pra", pra), ("reg", regresor)])

alphas = np.logspace(-3, 3, 60)          # grid α: 0,001 … 1000
model_kandidat = {
    "Regresi linear": LinearRegression(),
    "Ridge (alpha via CV)": RidgeCV(alphas=alphas, cv=5),
    "Lasso (alpha via CV)": LassoCV(alphas=alphas, cv=5, max_iter=50_000,
                                    random_state=RANDOM_STATE),
}

pipa_terlatih = {}
with warnings.catch_warnings(record=True) as catatan_peringatan:
    warnings.simplefilter("always", ConvergenceWarning)
    for nama, reg in model_kandidat.items():
        pipa = buat_pipa(reg).fit(X_train, y_train)
        pipa_terlatih[nama] = pipa
        hasil.append(metrik(y_test, pipa.predict(X_test), nama))

n_peringatan = sum(issubclass(w.category, ConvergenceWarning)
                   for w in catatan_peringatan)
print(f"ConvergenceWarning selama pelatihan: {n_peringatan}")
for w in catatan_peringatan:        # peringatan lain tetap ditampilkan
    if not issubclass(w.category, ConvergenceWarning):
        print(f"Peringatan lain — {w.category.__name__}: {w.message}")

tabel_hasil = pd.DataFrame(hasil)
print(tabel_hasil.round(3).to_string(index=False))
```

> **Dari mana `ConvergenceWarning` pada Lasso?** Lasso dilatih dengan *coordinate descent*, yang lambat konvergen bila (1) ada kolom yang kembar sempurna — misalnya enam dummy kota bersama intersep (*dummy variable trap*), terutama ketika α sangat kecil — atau (2) skala kolom sangat timpang. Menaikkan `max_iter` mungkin menghilangkan peringatannya, tetapi **tidak** menghilangkan penyebabnya. Pada versi awal lab ini (2.500 baris, enam dummy kota tanpa `drop="first"`), peringatan baru hilang pada `max_iter` = 100.000, namun α terpilih tetap di tepi bawah grid (0,001) dan Lasso menolkan satu dummy kota (`kota_Tangerang`) secara sembarang — bukan karena kota itu tidak berpengaruh, melainkan karena salah satu dari enam dummy selalu dapat dihitung dari intersep dan lima dummy lainnya, sehingga dummy mana pun boleh dibuang. Dengan `drop="first"` saja, peringatan sudah hilang pada `max_iter` = 20.000 dan α terpilih ≈ 0,068. Jadi, hilangkan penyebabnya dengan `drop="first"` dan penskalaan di dalam `Pipeline`, lalu biarkan `max_iter` yang longgar sebagai pengaman. **Jangan membungkam peringatan** — perbaiki penyebabnya.

### LANGKAH 6: α yang Terpilih dan Koefisien

```python
# =============================================
# LANGKAH 6: Alpha dan koefisien
# =============================================
ridge = pipa_terlatih["Ridge (alpha via CV)"].named_steps["reg"]
lasso = pipa_terlatih["Lasso (alpha via CV)"].named_steps["reg"]

def posisi(alpha):
    # α di ujung grid berarti optimum mungkin berada DI LUAR grid
    if alpha <= alphas.min() or alpha >= alphas.max():
        return "DI TEPI grid — perluas rentang alphas!"
    return "di dalam grid"

print(f"Alpha Ridge terpilih: {ridge.alpha_:.4f} ({posisi(ridge.alpha_)})")
print(f"Alpha Lasso terpilih: {lasso.alpha_:.4f} ({posisi(lasso.alpha_)})")

nama_fitur = [f.split("__", 1)[1] for f in
              pipa_terlatih["Ridge (alpha via CV)"].named_steps["pra"].get_feature_names_out()]

def kelompok(fitur):
    if fitur in KOLOM_DERAU:    return "derau"
    if fitur in KOLOM_KOLINEAR: return "kolinear"
    return "inti"               # termasuk dummy kota

koef = pd.DataFrame({
    "Fitur":    nama_fitur,
    "Kelompok": [kelompok(f) for f in nama_fitur],
    "Linear":   pipa_terlatih["Regresi linear"].named_steps["reg"].coef_,
    "Ridge":    ridge.coef_,
    "Lasso":    lasso.coef_,
})
koef["Dinolkan Lasso"] = np.abs(koef["Lasso"]) < 1e-8

print("\nKoefisien (pada skala terstandardisasi, juta Rp per 1 simpangan baku):")
tampil = koef.round(2)
tampil[["Linear", "Ridge", "Lasso"]] += 0.0      # merapikan "-0.00" menjadi "0.00"
print(tampil.to_string(index=False))

# --- Ringkasan per kelompok: dihitung, bukan ditulis tangan ---
ringkas = koef.groupby("Kelompok")["Dinolkan Lasso"].agg(["sum", "count"])
ringkas.columns = ["dinolkan", "jumlah kolom"]
print("\nYang dinolkan Lasso per kelompok:")
print(ringkas.to_string())

n_derau_nol = int(ringkas.loc["derau", "dinolkan"])
n_aktif_lasso = int((~koef["Dinolkan Lasso"]).sum())
print(f"\nFitur aktif: Linear {len(koef)} · Lasso {n_aktif_lasso}")

derau_nol  = koef.query("Kelompok == 'derau' and `Dinolkan Lasso`")["Fitur"].tolist()
derau_lolos = koef.query("Kelompok == 'derau' and not `Dinolkan Lasso`")
inti_nol   = koef.query("Kelompok == 'inti' and `Dinolkan Lasso`")["Fitur"].tolist()

if n_derau_nol == 0:
    print("Lasso TIDAK menolkan satu pun kolom derau — periksa penskalaan dan grid α.")
else:
    print(f"Lasso membuang {n_derau_nol} dari {len(KOLOM_DERAU)} kolom derau: {derau_nol}")
if len(derau_lolos):
    print(f"Kolom derau yang lolos ({len(derau_lolos)}) hanya berkoefisien kecil: "
          f"|koef| maks {derau_lolos['Lasso'].abs().max():.1f}, bandingkan dengan "
          f"luas_bangunan {koef.set_index('Fitur').loc['luas_bangunan', 'Lasso']:.1f}")

# --- Fitur INTI yang ikut dinolkan: alasannya dihitung per fitur, bukan ditulis tangan ---
if inti_nol:
    Z = pd.DataFrame(pipa_terlatih["Lasso (alpha via CV)"].named_steps["pra"]
                     .transform(X_train), columns=nama_fitur)   # data latih terskala
    aktif = koef.loc[~koef["Dinolkan Lasso"], "Fitur"].tolist()
    for f in inti_nol:
        r = Z[aktif].corrwith(Z[f])         # korelasi f dengan tiap fitur yang tetap aktif
        mitra = r.abs().idxmax()
        if abs(r[mitra]) >= 0.5:
            print(f"Lasso menolkan fitur inti {f}: informasinya tumpang tindih dengan "
                  f"{mitra} (r = {r[mitra]:.2f}), yang tetap aktif.")
        else:
            print(f"Lasso menolkan fitur inti {f}: tidak ada fitur aktif yang berkorelasi "
                  f"kuat dengannya (|r| maks {abs(r[mitra]):.2f}, dengan {mitra}) — "
                  f"sumbangannya terlalu kecil untuk melewati denda α.")
    print("→ Fitur di atas DIPAKAI rumus harga: 'dinolkan Lasso' ≠ 'tidak berpengaruh'.")

# --- Pasangan kolinear: siapa yang membagi bobot, siapa yang memilih? ---
print("\nPasangan kolinear:")
print(koef.set_index("Fitur").loc[["luas_bangunan", "daya_listrik_va",
                                   "jarak_pusat_km", "waktu_tempuh_menit"],
                                  ["Linear", "Ridge", "Lasso"]].round(2))
```

**Pemeriksaan otomatis.** Sel berikut harus lulus tanpa `AssertionError`; bila gagal, pesannya menunjukkan apa yang perlu diperiksa.

```python
# =============================================
# Pemeriksaan otomatis — pelajaran kunci Lab 6
# =============================================
assert n_peringatan == 0, (
    f"Lasso memunculkan {n_peringatan} ConvergenceWarning — pastikan penskalaan "
    f"berada di dalam Pipeline, dummy kota memakai drop='first', dan max_iter cukup")
for nama_reg, reg in [("Ridge", ridge), ("Lasso", lasso)]:
    assert alphas.min() < reg.alpha_ < alphas.max(), (
        f"α {nama_reg} = {reg.alpha_:.4g} berada di tepi grid — perluas rentang alphas")
assert n_derau_nol >= 1, (
    "Lasso seharusnya menolkan minimal satu kolom derau — periksa kolom derau "
    "di Langkah 1 dan penskalaan di Langkah 5")
assert n_aktif_lasso < len(koef), (
    "Lasso seharusnya memakai lebih sedikit fitur daripada regresi linear")
print("Pemeriksaan otomatis lulus.")
```

Pada data lab ini (`RANDOM_STATE = 42`; diuji pada scikit-learn 1.6 dan 1.9, hasilnya identik), validasi silang memilih α ≈ 5,8 untuk Ridge dan α ≈ 7,3 untuk Lasso — jauh dari kedua ujung grid (0,001 dan 1000). Lasso menolkan 5 dari 23 koefisien: 4 kolom derau (`nomor_rt`, `jumlah_foto_iklan`, `panjang_judul_iklan`, `digit_akhir_telepon`) dan kolom kolinear `daya_listrik_va`. Enam kolom derau lainnya lolos dengan koefisien kecil (|koef| ≤ 16,5 juta, dibandingkan ≈ 600 juta untuk `luas_bangunan`). Tidak ada fitur inti yang dinolkan pada seed ini. Dengan `RANDOM_STATE` lain, kolom yang dinolkan bisa berbeda, termasuk fitur inti; bila itu terjadi, sel Langkah 6 mencetak alasannya per fitur — dihitung dari korelasinya dengan fitur yang tetap aktif — lihat Tantangan 4.

**Tulis tafsiran:**
- Fitur apa yang dinolkan Lasso? Apakah masuk akal secara domain — misalnya, mungkinkah `nomor_rt` atau `digit_akhir_telepon` memengaruhi harga rumah?
- Mengapa sebagian kolom derau **lolos** dengan koefisien kecil? *Petunjuk:* pada 800 baris latih, kolom acak pun berkorelasi sedikit dengan harga secara kebetulan.
- Pada pasangan kolinear, bandingkan ketiga model. Model mana yang **membagi** bobot di antara dua kolom yang kembar, dan model mana yang cenderung **memilih salah satu**? Bagaimana tanda dan besar koefisien `daya_listrik_va` pada ketiga model — masuk akalkah, mengingat kolom ini tidak dipakai rumus harga?

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

# --- Kesimpulan dihitung dari hasil, bukan ditulis tangan ---
kelompok_model = {
    "Dua baseline": ["Baseline (mean)", "Baseline (median)"],
    "Tiga model regresi": ["Regresi linear", "Ridge (alpha via CV)",
                           "Lasso (alpha via CV)"],
}
for judul, daftar in kelompok_model.items():
    terbaik = {m: t.loc[daftar, m].idxmin() for m in ["MAE", "RMSE", "MAPE%"]}
    print(f"\n{judul} — model terbaik menurut tiap metrik:")
    for m, nama in terbaik.items():
        print(f"  {m:>5}: {nama}")
    if len(set(terbaik.values())) > 1:
        print("  → Metrik yang berbeda memilih model yang BERBEDA.")
    else:
        print("  → Ketiga metrik sepakat.")

tiga = t.loc[kelompok_model["Tiga model regresi"]]
selisih = (tiga["MAE"].max() - tiga["MAE"].min()) / tiga["MAE"].min() * 100
print(f"\nSelisih MAE terbesar di antara tiga model regresi: {selisih:.1f}%")
if selisih < 5:
    print(f"→ Akurasi ketiganya berdekatan ({len(X_train)} baris latih, {len(koef)} kolom). "
          "Perbedaan yang jelas ada pada koefisien (Langkah 6): Lasso hanya memakai "
          f"{n_aktif_lasso} dari {len(koef)} fitur.")
else:
    print("→ Regularisasi mengubah akurasi secara berarti pada data ini.")
```

> **Rasio RMSE/MAE adalah petunjuk.** Rasio mendekati 1 berarti galat tersebar merata; rasio besar berarti ada sedikit galat yang sangat besar dan mendominasi RMSE.

> **Regularisasi tidak selalu menaikkan akurasi secara besar.** Bila baris latih jauh lebih banyak daripada kolom (di sini 800 berbanding 23), regresi linear biasa jarang *overfitting* parah, sehingga Ridge dan Lasso hanya berbeda tipis dari regresi linear — pada data lab ini selisih MAE ketiganya ≈ 2%. Ridge sedikit lebih baik daripada regresi linear pada keempat metrik (pada RMSE dan R² nyaris sama), sedangkan Lasso unggul menurut MAE dan MAPE tetapi sedikit lebih buruk menurut RMSE (471,4 lawan 468,6) dan R² (0,817 lawan 0,819). Karena itu urutannya bergantung pada metrik: MAE dan MAPE memilih Lasso, RMSE memilih Ridge. Manfaat yang jelas di sini adalah **model yang lebih sederhana** (Lasso membuang kolom yang tidak berguna) dan **koefisien yang lebih stabil** pada fitur kolinear (Ridge). Bila akurasinya setara, model dengan lebih sedikit fitur lebih murah datanya dan lebih mudah dijelaskan.

**Tulis penjelasan:** mengapa sebuah model dapat unggul menurut MAE tetapi kalah menurut RMSE? Kaitkan dengan rasio RMSE/MAE tiap model.

### LANGKAH 8: Diagnostik Residual

```python
# =============================================
# LANGKAH 8: Memeriksa residual
# =============================================
# Yang diperiksa: Lasso, model paling sederhana (fitur aktif paling sedikit).
# Diagnostik ini berlaku untuk model mana pun — silakan ganti namanya.
nama_diperiksa = "Lasso (alpha via CV)"
prediksi = pipa_terlatih[nama_diperiksa].predict(X_test)
residual = y_test - prediksi

fig, ax = plt.subplots(1, 3, figsize=(15, 4.2))

ax[0].scatter(prediksi, residual, alpha=0.3)
ax[0].axhline(0, color="red", ls="--")
ax[0].set_xlabel("Prediksi (juta Rp)"); ax[0].set_ylabel("Residual")
ax[0].set_title(f"Residual vs prediksi — {nama_diperiksa}")

ax[1].hist(residual, bins=40, edgecolor="white")
ax[1].set_xlabel("Residual"); ax[1].set_ylabel("Frekuensi")
ax[1].set_title("Sebaran residual")

from scipy import stats
stats.probplot(residual, dist="norm", plot=ax[2])
ax[2].set_title("Q-Q plot residual")

plt.tight_layout(); plt.show()

print("Rata-rata residual:", round(residual.mean(), 2))
print("Kemencengan residual:", round(residual.skew(), 3))
```

**Tulis diagnosis:** adakah pola corong pada grafik pertama? Bila ada, asumsi mana yang dilanggar dan apa akibatnya? *Petunjuk:* lihat kembali rumus pembangkit harga di Langkah 1 — derau dikalikan, bukan ditambahkan.

---

## Tantangan Tambahan

### Tantangan 1 — Transformasi Target

Latih model pada `log(harga)` alih-alih `harga`, lalu kembalikan prediksinya dengan `exp`. Bandingkan MAE, RMSE, dan MAPE dengan model asli. Manakah yang lebih baik, dan mengapa?

### Tantangan 2 — Kurva Regularisasi

Buat grafik R² validasi terhadap α pada rentang `np.logspace(-3, 4, 40)` untuk Ridge. Tandai α optimum. Apa yang terjadi pada kedua ujung rentang?

### Tantangan 3 — Regresi Polinomial

Tambahkan `PolynomialFeatures(degree=2)` sebelum regresi. Bandingkan R² latih dan R² uji. Adakah tanda *overfitting*? Bandingkan pula dengan derajat 3.

### Tantangan 4 — Stabilitas Pemilihan Lasso

Ulangi Langkah 1–6 dengan `RANDOM_STATE` 1 sampai 5. Apakah kolom derau yang dinolkan Lasso selalu sama? Apakah Lasso selalu memilih anggota pasangan kolinear yang sama (`jarak_pusat_km` atau `waktu_tempuh_menit`)? Adakah fitur **inti** yang ikut dinolkan? Bila ada, cocokkan alasan yang dicetak Langkah 6 dengan rumus pembangkit di Langkah 1: seberapa besar efek sebenarnya fitur itu, dan dengan fitur apa ia berkorelasi? Apa artinya bagi tafsiran "fitur yang dibuang Lasso tidak penting"?

*Catatan:* sel Pemeriksaan otomatis disetel untuk `RANDOM_STATE = 42`. Pada uji kami dengan 40 nilai seed, kira-kira 1 dari 10 seed membuat Lasso tidak menolkan satu pun kolom derau sehingga pemeriksaan itu gagal — temuan yang juga layak dibahas.

---

## Checklist Penyelesaian

- [ ] Eksplorasi data dilakukan **sebelum** memodelkan, termasuk korelasi pasangan kolinear
- [ ] *Baseline* `DummyRegressor` dibangun
- [ ] **Perhitungan manual** MAE, RMSE, MAPE diverifikasi dengan sklearn
- [ ] Penskalaan berada **sebelum** regularisasi, di dalam `Pipeline`; tidak ada `ConvergenceWarning`
- [ ] α ditentukan dengan validasi silang, bukan ditebak, dan tidak berada di tepi grid
- [ ] Koefisien ketiga model dibandingkan, termasuk pada pasangan kolinear
- [ ] **Fitur yang dinolkan Lasso** diidentifikasi dan ditafsirkan
- [ ] Sel **Pemeriksaan otomatis** lulus
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
