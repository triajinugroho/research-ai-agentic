# Lab 04: Validasi Silang dan Perburuan Kebocoran

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 4 |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-04 |
| Durasi | 100 menit |
| Prasyarat | Lab 3 selesai |
| Bobot | 2,0% (Observasi, Sub-CPMK102-1) |
| Diuji pada | scikit-learn 1.6 dan 1.9, pandas 2.2 dan 3.0 (Oktober 2026) |

---

## Tujuan Praktikum

1. Menemukan dan menjelaskan mekanisme kebocoran data — empat kebocoran pada notebook yang salah, ditambah kebocoran kelompok.
2. Memperbaiki kebocoran dan mengukur dampaknya terhadap skor.
3. Menerapkan strategi pembagian data yang sesuai sifat datanya: acak, berkelompok, atau temporal.
4. Menafsirkan sebaran skor antarlipatan pada validasi silang.

---

## Persiapan

1. Buat notebook baru bernama `NIM_Nama_Lab04.ipynb`.
2. Jalankan **sel pembuka baku** di [Lampiran D](../06-buku-ajar/lampiran.md#lampiran-d-sel-pembuka-baku) — mengimpor pustaka, mencatat versi, dan menetapkan `RANDOM_STATE = 42`. Seluruh langkah di bawah mengandaikan sel itu sudah dijalankan.
3. **Data:** seluruh data lab ini adalah **data sintetis (simulasi)** yang meniru pola transaksi *e-commerce* Indonesia; **bukan data resmi BPS/lembaga** mana pun. Data dibangkitkan pada Langkah 1 (transaksi) dan Langkah 5 (data "lebar"). Karena sintetis, kita tahu "kebenarannya" — struktur yang rawan bocor sengaja ditanam agar dampak setiap kebocoran dapat **diukur**, bukan sekadar diceritakan.

---

## Langkah-langkah

### LANGKAH 1: Data Transaksi yang Rawan Bocor

> **Data sintetis (simulasi)** yang meniru pola transaksi *e-commerce* Indonesia; bukan data resmi BPS/lembaga. Tiga struktur sengaja ditanam: (a) **pelanggan berulang** — setiap pelanggan muncul ±12 kali dan punya kecenderungan membeli bawaan (efek acak per pelanggan) yang **tidak tercatat** di kolom mana pun; (b) **pergeseran perilaku** (*drift*) setelah pembaruan aplikasi fiktif pada 15 Juli 2025; (c) kolom `nomor_invoice` yang hanya ada **setelah** pembelian terjadi.

```python
# =============================================
# LANGKAH 1: Data transaksi SINTETIS dengan struktur yang rawan bocor
# (simulasi e-commerce — bukan data resmi BPS/lembaga)
# =============================================
import numpy as np, pandas as pd
rng = np.random.default_rng(RANDOM_STATE)
n, n_pelanggan = 3000, 250

tanggal = pd.date_range("2024-01-01", periods=n, freq="6h")   # baris URUT waktu

# --- Atribut tetap per pelanggan (pola individual) ---
umur_p  = rng.integers(18, 56, size=n_pelanggan)
jarak_p = rng.gamma(2.0, 6.0, size=n_pelanggan).round(2)      # km ke gudang terdekat
efek_p  = rng.normal(0, 2.5, size=n_pelanggan)  # kecenderungan bawaan: ada yang rajin
                                                # membeli, ada yang sekadar melihat-lihat.
                                                # TIDAK tersimpan di kolom mana pun.
id_p = rng.integers(0, n_pelanggan, size=n)     # pelanggan BERULANG

df = pd.DataFrame({
    "tanggal":         tanggal,
    "id_pelanggan":    id_p + 1,
    "umur":            umur_p[id_p],
    "jarak_gudang_km": jarak_p[id_p],
    "durasi_sesi":     rng.gamma(2.0, 8, size=n).round(1),     # menit
    "jumlah_klik":     rng.poisson(12, size=n),
    "nilai_keranjang": rng.gamma(2.0, 150_000, size=n).round(0),  # rupiah
    "pakai_voucher":   rng.binomial(1, 0.35, size=n),
    "kategori":        rng.choice(["Elektronik", "Fashion", "Makanan", "Buku"], size=n),
})

# --- DRIFT: pembaruan aplikasi (fiktif) 15 Juli 2025, fitur "checkout kilat" ---
# Sebelum: sesi panjang = sedang memilih barang  -> lebih mungkin membeli
# Sesudah: pembeli selesai cepat; sesi panjang  -> sekadar melihat-lihat
#          (arah pengaruh durasi_sesi BERBALIK)
TGL_PEMBARUAN = pd.Timestamp("2025-07-15")
setelah = (df["tanggal"] >= TGL_PEMBARUAN).to_numpy()
efek_durasi = np.where(setelah, -0.04, 0.08)

# Target: pembelian terjadi (1) atau tidak (0)
logit = (-0.6
         + efek_durasi * (df["durasi_sesi"].to_numpy() - 16)
         + 0.12 * (df["jumlah_klik"].to_numpy() - 12)
         + 1.5 * df["pakai_voucher"].to_numpy()
         - 0.08 * (df["jarak_gudang_km"].to_numpy() - 12)     # ongkos kirim
         + 0.0000012 * (df["nilai_keranjang"].to_numpy() - 300_000)
         + efek_p[id_p])
df["beli"] = rng.binomial(1, 1 / (1 + np.exp(-logit)))

# KEBOCORAN TARGET: kolom yang hanya ada SETELAH pembelian terjadi
df["nomor_invoice"] = np.where(df["beli"] == 1,
                               rng.integers(10_000, 99_999, size=n), 0)

print("Dimensi:", df.shape)
print("Rentang waktu:", df["tanggal"].min().date(), "s.d.", df["tanggal"].max().date())
print("Proporsi target:", round(df["beli"].mean(), 3))
print("Pelanggan unik:", df["id_pelanggan"].nunique(), "dari", n, "baris",
      f"(rata-rata {n / df['id_pelanggan'].nunique():.1f} transaksi per pelanggan)")
print(f"Transaksi setelah pembaruan aplikasi: {setelah.mean():.1%}")
print(df.head())
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

kol_bersih = ["umur", "jarak_gudang_km", "durasi_sesi",
              "jumlah_klik", "nilai_keranjang", "pakai_voucher"]
kol_fitur = kol_bersih + ["nomor_invoice"]
X_salah = df[kol_fitur].copy()
y = df["beli"]

# BOCOR 1: penskalaan pada SELURUH data
X_salah = pd.DataFrame(StandardScaler().fit_transform(X_salah),
                       columns=kol_fitur)

# BOCOR 2: pemilihan fitur memakai SELURUH y
pemilih = SelectKBest(f_classif, k=5).fit(X_salah, y)
kol_terpilih = np.array(kol_fitur)[pemilih.get_support()]
X_salah = pd.DataFrame(pemilih.transform(X_salah), columns=kol_terpilih)
print("Fitur terpilih:", kol_terpilih.tolist())

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

Setiap tahap memperbaiki **satu** hal dan mempertahankan yang lain, sehingga perubahan skor dapat dikaitkan dengan perbaikan itu.

```python
# =============================================
# LANGKAH 3: Perbaikan bertahap — ukur dampak tiap perbaikan
# =============================================
from sklearn.pipeline import Pipeline

def buat_pipa():
    """Pipeline yang benar: skala dan seleksi di-fit pada data latih saja."""
    return Pipeline([
        ("skala", StandardScaler()),
        ("pilih", SelectKBest(f_classif, k=5)),
        ("clf",   RandomForestClassifier(n_estimators=200,
                                         random_state=RANDOM_STATE, n_jobs=-1)),
    ])

def auc_uji(model, Xtr, Xte, ytr, yte):
    model.fit(Xtr, ytr)
    return roc_auc_score(yte, model.predict_proba(Xte)[:, 1])

hasil = [{"Tahap": "Seluruh kebocoran", "ROC-AUC": auc_salah}]
X = df[kol_bersih]

# Perbaikan 1: buang kolom bocor target
# (penskalaan dan seleksi MASIH di-fit pada seluruh data, pembagian masih acak)
X_semua = SelectKBest(f_classif, k=5).fit_transform(
    StandardScaler().fit_transform(X), y)
Xtr, Xte, ytr, yte = train_test_split(X_semua, y, test_size=0.2,
                                      random_state=RANDOM_STATE)
auc_tanpa_invoice = auc_uji(
    RandomForestClassifier(n_estimators=200, random_state=RANDOM_STATE, n_jobs=-1),
    Xtr, Xte, ytr, yte)
hasil.append({"Tahap": "+ buang nomor_invoice", "ROC-AUC": auc_tanpa_invoice})

# Perbaikan 2: penskalaan dan seleksi di DALAM Pipeline (pembagian masih acak;
# random_state sama -> baris uji sama dengan Perbaikan 1)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                      random_state=RANDOM_STATE)
auc_acak = auc_uji(buat_pipa(), Xtr, Xte, ytr, yte)
hasil.append({"Tahap": "+ skala & seleksi di dalam Pipeline", "ROC-AUC": auc_acak})

# Perbaikan 3: pembagian TEMPORAL — latih pada 80% awal, uji pada 20% akhir
batas = int(len(df) * 0.8)
auc_temporal = auc_uji(buat_pipa(), X.iloc[:batas], X.iloc[batas:],
                       y.iloc[:batas], y.iloc[batas:])
hasil.append({"Tahap": "+ pembagian temporal", "ROC-AUC": auc_temporal})
print(f"Temporal: latih {df['tanggal'].iloc[0].date()} s.d. "
      f"{df['tanggal'].iloc[batas - 1].date()}, uji {df['tanggal'].iloc[batas].date()} "
      f"s.d. {df['tanggal'].iloc[-1].date()}\n")

tabel = pd.DataFrame(hasil)
tabel["Perubahan"] = tabel["ROC-AUC"].diff()
print(tabel.round(4).to_string(index=False))

# Kesimpulan DIHITUNG dari hasil, bukan ditulis tetap
i_terbesar = tabel["Perubahan"].abs().idxmax()
print(f"\nPerbaikan berdampak terbesar: '{tabel.loc[i_terbesar, 'Tahap']}' "
      f"({tabel.loc[i_terbesar, 'Perubahan']:+.4f})")
d_pipa = auc_acak - auc_tanpa_invoice
if abs(d_pipa) < 0.01:
    print(f"Memindahkan skala & seleksi ke dalam Pipeline hampir tidak mengubah skor "
          f"({d_pipa:+.4f}): Random Forest tidak peka penskalaan, dan memilih 5 dari "
          "6 fitur pada 3.000 baris menyisakan sedikit ruang bagi kebetulan. "
          "Prosedurnya tetap salah — Langkah 5 menunjukkan kapan dampaknya besar.")
else:
    print(f"Memindahkan skala & seleksi ke dalam Pipeline mengubah skor {d_pipa:+.4f}.")
d_waktu = auc_acak - auc_temporal
if d_waktu >= 0.03:
    print(f"Pembagian acak {d_waktu:.3f} lebih optimistis daripada pembagian temporal: "
          "model yang akan dipakai di MASA DEPAN dinilai dengan data campuran "
          "masa lalu dan masa depan.")
else:
    print(f"Selisih acak vs temporal kecil ({d_waktu:+.4f}).")

# Jejak drift di data: arah hubungan durasi_sesi–beli sebelum vs sesudah pembaruan
r_sebelum = df.loc[~setelah, "durasi_sesi"].corr(df.loc[~setelah, "beli"])
r_sesudah = df.loc[setelah, "durasi_sesi"].corr(df.loc[setelah, "beli"])
print(f"Korelasi durasi_sesi–beli: sebelum pembaruan {r_sebelum:+.3f}, "
      f"sesudah pembaruan {r_sesudah:+.3f}")
```

**Pemeriksaan otomatis.** Sel berikut harus lulus tanpa `AssertionError`; bila gagal, pesannya menunjukkan apa yang perlu diperiksa.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 2 dan 3
# =============================================
assert "nomor_invoice" in kol_terpilih, (
    "SelectKBest seharusnya memilih nomor_invoice — ia paling 'berhubungan' dengan target")
assert auc_salah > 0.95, (
    f"Dengan nomor_invoice, ROC-AUC seharusnya nyaris sempurna (sekarang {auc_salah:.4f})")
assert auc_salah - auc_tanpa_invoice > 0.2, (
    "Membuang nomor_invoice seharusnya menurunkan skor secara tajam — periksa Langkah 2")
assert df["tanggal"].iloc[batas] >= TGL_PEMBARUAN, (
    "Data uji temporal seharusnya seluruhnya berasal dari periode SETELAH pembaruan "
    "aplikasi — periksa batas pembagian temporal di Langkah 3")
assert r_sebelum > 0.1 and r_sesudah < -0.05, (
    f"Arah hubungan durasi_sesi–beli seharusnya berbalik setelah pembaruan (sekarang "
    f"{r_sebelum:+.3f} -> {r_sesudah:+.3f}) — periksa drift (efek_durasi) di Langkah 1")
assert auc_acak - auc_temporal >= 0.07, (
    f"Pembagian acak seharusnya minimal 0,07 lebih optimistis daripada pembagian "
    f"temporal (sekarang {auc_acak - auc_temporal:+.4f}); tanpa drift selisihnya "
    f"hanya ≈ 0,04 — periksa drift di Langkah 1")
print("Pemeriksaan otomatis lulus.")
```

Pada data lab ini (diuji pada scikit-learn 1.6 dan 1.9), ROC-AUC turun dari ≈ 1,00 (seluruh kebocoran) ke ≈ 0,69 setelah `nomor_invoice` dibuang, praktis tidak berubah (selisih < 0,001) ketika penskalaan dan seleksi dipindahkan ke dalam `Pipeline`, lalu turun lagi ke ≈ 0,58 dengan pembagian temporal — selisih acak vs temporal ≈ 0,11. Drift itu tampak langsung di data: korelasi `durasi_sesi`–`beli` ≈ +0,25 sebelum pembaruan aplikasi dan ≈ −0,13 sesudahnya. Bila drift dihapus (`efek_durasi` dibuat tetap 0,08 di Langkah 1), selisih acak vs temporal menyusut ke ≈ 0,04 — sebagian besar selisih memang berasal dari drift, dan karena itu pemeriksaan otomatis memakai ambang 0,07.

**Tulis kesimpulan:**

1. Perbaikan mana yang paling besar dampaknya? Mengapa?
2. Mengapa pembagian acak lebih optimistis daripada pembagian temporal pada data ini? *Petunjuk:* bandingkan tanggal pembaruan aplikasi di Langkah 1 dengan rentang data latih dan uji temporal. Data uji acak berisi baris dari periode mana saja?
3. Memindahkan penskalaan ke dalam `Pipeline` hampir tidak mengubah skor. Apakah itu berarti penskalaan pada seluruh data boleh dilakukan? Jelaskan.

### LANGKAH 4: Pembagian Berkelompok

```python
# =============================================
# LANGKAH 4: Kebocoran kelompok — pelanggan berulang
# =============================================
from sklearn.model_selection import GroupKFold, cross_val_score, StratifiedKFold

grup = df["id_pelanggan"]
pipa = buat_pipa()

# Tanpa memperhatikan kelompok — pelanggan yang sama ada di latih DAN uji
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
skor_biasa = cross_val_score(pipa, X, y, cv=skf, scoring="roc_auc", n_jobs=-1)

# Dengan GroupKFold — seluruh baris satu pelanggan di lipatan yang sama
gkf = GroupKFold(n_splits=5)
skor_grup = cross_val_score(pipa, X, y, cv=gkf, groups=grup,
                            scoring="roc_auc", n_jobs=-1)

# Simpangan baku antarlipatan = simpangan baku SAMPEL (ddof=1), sama dengan pd.Series.std()
print(f"StratifiedKFold : {skor_biasa.mean():.4f} ± {skor_biasa.std(ddof=1):.4f}")
print(f"GroupKFold      : {skor_grup.mean():.4f} ± {skor_grup.std(ddof=1):.4f}")
d_grup = skor_biasa.mean() - skor_grup.mean()
print(f"Selisih         : {d_grup:+.4f}")

# Mengapa model bisa "mengenali" pelanggan padahal id_pelanggan bukan fitur?
print(f"\nNilai unik jarak_gudang_km: {df['jarak_gudang_km'].nunique()} "
      f"untuk {df['id_pelanggan'].nunique()} pelanggan")
if d_grup >= 0.03:
    print("Validasi silang acak menaksir terlalu tinggi: model menghafal pelanggan "
          "lewat 'sidik jari' fitur tetapnya, bukan mempelajari pola yang berlaku "
          "untuk pelanggan BARU.")
else:
    print("Selisih kecil: pada data ini model tidak banyak memperoleh dari "
          "menghafal pelanggan.")
```

```python
# =============================================
# Pemeriksaan otomatis — Langkah 4
# =============================================
assert d_grup >= 0.03, (
    f"Validasi silang acak seharusnya minimal 0,03 lebih tinggi daripada GroupKFold "
    f"(sekarang {d_grup:+.4f}) — periksa apakah groups=id_pelanggan dipakai")
print("Pemeriksaan otomatis lulus.")
```

> Pada data ini 250 pelanggan menghasilkan 3.000 baris — rata-rata 12 baris per pelanggan — dan validasi silang acak menaksir ROC-AUC ≈ 0,70, sedangkan `GroupKFold` hanya ≈ 0,60–0,61: selisih ≈ 0,09–0,10 (diuji pada scikit-learn 1.6 dan 1.9; pembagian lipatan `GroupKFold` sedikit berbeda antarversi). `id_pelanggan` tidak dipakai sebagai fitur, tetapi `jarak_gudang_km` bernilai tetap untuk setiap pelanggan dan hampir unik (238 nilai untuk 250 pelanggan), sehingga menjadi **sidik jari**: model dapat mengenali pelanggan yang sudah dikenalnya dan "mengingat" kecenderungan bawaannya. Umumnya, semakin banyak baris per entitas dan semakin kuat pola individualnya, semakin besar selisihnya.

**Tulis penjelasan:** taksiran mana yang jujur bila model akan dipakai untuk pelanggan **baru**? Dan bila model hanya dipakai untuk pelanggan lama?

### LANGKAH 5: Kebocoran Seleksi Fitur pada Data Lebar

Pada Langkah 3, seleksi fitur di luar `Pipeline` hampir tidak berdampak karena hanya ada 6 fitur dan 3.000 baris. Dampaknya besar ketika **fitur jauh lebih banyak daripada baris** — keadaan yang lazim pada data log klik, teks, atau genomik.

> **Data sintetis (simulasi):** 150 pelanggan peserta uji coba program langganan, dengan 2.000 kolom jumlah kunjungan ke halaman produk. Target `ikut_langganan` diundi **terpisah** dari seluruh fitur — tidak ada sinyal sama sekali, sehingga ROC-AUC yang jujur seharusnya ≈ 0,5.

```python
# =============================================
# LANGKAH 5: Seleksi fitur di luar vs di dalam Pipeline
# (data SINTETIS lebar — bukan data resmi BPS/lembaga)
# =============================================
from sklearn.linear_model import LogisticRegression

rng_lebar = np.random.default_rng(RANDOM_STATE + 1)
n_lebar, p_lebar = 150, 2000
X_lebar = pd.DataFrame(rng_lebar.poisson(3, size=(n_lebar, p_lebar)),
                       columns=[f"kunjungan_hal_{i:04d}" for i in range(p_lebar)])
y_lebar = pd.Series(rng_lebar.binomial(1, 0.5, size=n_lebar), name="ikut_langganan")

cv5 = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

# SALAH: pilih 20 fitur terbaik memakai SELURUH y, baru validasi silang
pilih_luar = SelectKBest(f_classif, k=20).fit(X_lebar, y_lebar)
X_terpilih = X_lebar.loc[:, pilih_luar.get_support()]
pipa_luar = Pipeline([("skala", StandardScaler()),
                      ("clf", LogisticRegression(solver="liblinear"))])
skor_luar = cross_val_score(pipa_luar, X_terpilih, y_lebar, cv=cv5, scoring="roc_auc")

# BENAR: seleksi di DALAM Pipeline — diulang pada data latih tiap lipatan
pipa_dalam = Pipeline([("skala", StandardScaler()),
                       ("pilih", SelectKBest(f_classif, k=20)),
                       ("clf", LogisticRegression(solver="liblinear"))])
skor_dalam = cross_val_score(pipa_dalam, X_lebar, y_lebar, cv=cv5, scoring="roc_auc")

print(f"Seleksi di LUAR Pipeline : {skor_luar.mean():.4f} ± {skor_luar.std(ddof=1):.4f}")
print(f"Seleksi di DALAM Pipeline: {skor_dalam.mean():.4f} ± {skor_dalam.std(ddof=1):.4f}")
d_seleksi = skor_luar.mean() - skor_dalam.mean()
print(f"Selisih                  : {d_seleksi:+.4f}")
if d_seleksi >= 0.2:
    print("Pada data TANPA sinyal, seleksi di luar Pipeline menghasilkan skor yang "
          "tampak meyakinkan: 20 fitur dipilih justru karena kebetulan cocok dengan "
          "y — termasuk y milik baris yang nanti menjadi data validasi.")
```

```python
# =============================================
# Pemeriksaan otomatis — Langkah 5
# =============================================
assert d_seleksi >= 0.2, (
    f"Seleksi di luar Pipeline seharusnya menggelembungkan skor minimal 0,2 "
    f"(sekarang {d_seleksi:+.4f}) — periksa apakah SelectKBest di-fit pada seluruh y")
assert abs(skor_dalam.mean() - 0.5) < 0.15, (
    f"Target diundi acak; skor jujur seharusnya dekat 0,5 (sekarang "
    f"{skor_dalam.mean():.4f}) — periksa apakah SelectKBest berada di dalam Pipeline")
print("Pemeriksaan otomatis lulus.")
```

Pada data lab ini (diuji pada scikit-learn 1.6 dan 1.9), seleksi di luar `Pipeline` menghasilkan ROC-AUC ≈ 0,93 pada data yang **sama sekali tidak mengandung sinyal**, sedangkan seleksi di dalam `Pipeline` memberi ≈ 0,56 ± 0,09 (simpangan baku sampel, `ddof=1`) — tidak jauh dari 0,5, taksiran yang jujur untuk data tanpa sinyal.

**Tulis penjelasan:** mengapa seleksi di luar `Pipeline` tetap bocor meskipun model dilatih ulang pada setiap lipatan? Mengapa dampaknya jauh lebih besar di sini daripada di Langkah 3?

### LANGKAH 6: Pembagian Temporal dengan `TimeSeriesSplit`

```python
# =============================================
# LANGKAH 6: TimeSeriesSplit
# =============================================
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
skor_ts = cross_val_score(pipa, X, y, cv=tscv, scoring="roc_auc", n_jobs=-1)

print("Struktur lipatan temporal:")
for i, ((i_tr, i_te), s) in enumerate(zip(tscv.split(X), skor_ts), 1):
    awal, akhir = df["tanggal"].iloc[i_te[0]], df["tanggal"].iloc[i_te[-1]]
    print(f"  Lipatan {i}: latih=[0:{i_tr[-1]+1}]  uji=[{i_te[0]}:{i_te[-1]+1}]  "
          f"({awal.date()} s.d. {akhir.date()})  ROC-AUC={s:.4f}")
print(f"\nRerata: {skor_ts.mean():.4f} ± {skor_ts.std(ddof=1):.4f}")

# Lipatan terendah — kesimpulan dihitung dari hasil
i_min = int(np.argmin(skor_ts))
i_te_min = list(tscv.split(X))[i_min][1]
porsi_baru = (df["tanggal"].iloc[i_te_min] >= TGL_PEMBARUAN).mean()
print(f"Lipatan terendah: {i_min + 1} — {porsi_baru:.0%} data ujinya berasal dari "
      f"periode SETELAH pembaruan aplikasi ({TGL_PEMBARUAN.date()}).")
```

**Perhatikan:** pada `TimeSeriesSplit`, data latih selalu **mendahului** data uji, dan ukurannya bertambah tiap lipatan. Skor per lipatan memperlihatkan **kapan** model mulai gagal — informasi yang hilang bila hanya rerata yang dilaporkan. Pada data lab ini, skor lipatan 1–4 berkisar ≈ 0,63–0,68, lalu turun ke ≈ 0,59 pada lipatan 5 — lipatan yang seluruh data ujinya berasal dari periode setelah pembaruan aplikasi.

### LANGKAH 7: Membaca Sebaran Antarlipatan

```python
# =============================================
# LANGKAH 7: Rerata saja menyembunyikan informasi
# =============================================
import matplotlib.pyplot as plt

perbandingan = pd.DataFrame({
    "StratifiedKFold": skor_biasa,
    "GroupKFold":      skor_grup,
    "TimeSeriesSplit": skor_ts,
})

# describe() dan DataFrame.std() pandas memakai ddof=1 — sama dengan .std(ddof=1)
# pada Langkah 4–6, sehingga angka simpangan di seluruh lab ini dapat dibandingkan
print(perbandingan.describe().T[["mean", "std", "min", "max"]].round(4))

def tafsir_simpangan(s):
    # Ambang mengikuti tabel di bawah (simpangan baku sampel; metrik berskala 0–1)
    if s < 0.02:
        return "kinerja stabil"
    elif s < 0.05:
        return "wajar pada data terbatas"
    elif s <= 0.10:
        return "cukup besar — periksa skor per lipatan"
    return "besar — selidiki lipatan yang menyimpang"

# Tafsir DIHITUNG dari simpangan, bukan ditulis tetap
print()
for nama, s in perbandingan.std().items():
    print(f"{nama:16s}: simpangan {s:.4f} -> {tafsir_simpangan(s)}")
print(f"{'Seleksi (L5)':16s}: simpangan {skor_dalam.std(ddof=1):.4f} -> "
      f"{tafsir_simpangan(skor_dalam.std(ddof=1))}  (150 baris saja)")

perbandingan.plot(kind="box", figsize=(8, 4.5))
plt.ylabel("ROC-AUC")
plt.title(f"Sebaran skor antarlipatan menurut strategi pembagian (n={len(df)})")
plt.tight_layout(); plt.show()
```

Ambang di bawah adalah **aturan praktis** untuk simpangan baku sampel (`ddof=1`) dari metrik berskala 0–1 seperti ROC-AUC, F1, atau akurasi. Rentangnya bersambung tanpa celah.

| Simpangan baku antarlipatan | Tafsir |
|-----------------------------|--------|
| < 0,02 | Kinerja stabil |
| 0,02 sampai < 0,05 | Wajar pada data terbatas — laporkan rerata **dan** simpangannya |
| 0,05 sampai 0,10 | Cukup besar — periksa skor per lipatan; selisih rerata yang kecil antarmodel belum dapat dipercaya |
| > 0,10 | Besar — selidiki lipatan yang menyimpang |

Pada data lab ini, simpangan ketiga strategi pembagian berada pada rentang 0,02 sampai < 0,05, sedangkan seleksi di dalam `Pipeline` pada data lebar Langkah 5 (hanya 150 baris) masuk rentang 0,05 sampai 0,10. Satu lipatan yang jauh lebih rendah daripada yang lain — seperti lipatan 5 `TimeSeriesSplit` — patut diselidiki **apa pun** besar simpangannya.

### LANGKAH 8: Daftar Periksa Kebocoran

```python
# =============================================
# LANGKAH 8: Daftar periksa — jalankan sebelum mengumpulkan
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

### Tantangan 1 — Menyusun Kebocoran Sendiri: *Oversampling* sebelum Pembagian

Kebocoran berbasis target (*target encoding* di luar `Pipeline`) sudah didemonstrasikan di [Lab 3 Langkah 6](lab-03-pipeline-prapemrosesan.md#langkah-6-demonstrasi-kebocoran). Tantangan ini menyusun jenis yang belum ada di Lab 3 maupun lab ini: **menggandakan kelas minoritas sebelum validasi silang** (*random oversampling* — teknik penyeimbangan kelas yang paling sederhana; SMOTE membangkitkan contoh sintetis, bukan salinan, tetapi kebocorannya serupa bila diterapkan sebelum pembagian). Cukup dengan scikit-learn; `imbalanced-learn` tidak diperlukan.

1. **Buat data timpang.** Data Langkah 1 hampir seimbang, jadi ambil seluruh baris `beli = 0` dan hanya 20% baris `beli = 1`, misalnya `minor = df[df["beli"] == 1].sample(frac=0.2, random_state=RANDOM_STATE)`, lalu gabungkan dengan `timpang = pd.concat([df[df["beli"] == 0], minor]).sort_index()` — `.sort_index()` mengembalikan urutan waktu asli sehingga lipatan `skf` dapat direproduksi. Hitung proporsi kelas minoritasnya (≈ 0,15).
2. **Cara salah.** Gandakan baris minoritas secara acak dengan `sklearn.utils.resample(..., replace=True, n_samples=<jumlah baris mayoritas>, random_state=RANDOM_STATE)` hingga kedua kelas seimbang, gabungkan, **baru** jalankan `cross_val_score(buat_pipa(), ..., cv=skf, scoring="roc_auc")`.
3. **Cara benar.** Tulis perulangan manual atas `skf.split(X_timpang, y_timpang)`: gandakan kelas minoritas **hanya pada indeks latih** lipatan itu, latih `buat_pipa()`, lalu nilai pada lipatan validasi yang **asli** (tanpa salinan). Bandingkan pula dengan tanpa *oversampling* sama sekali.
4. **Jelaskan mekanismenya.** Salinan baris yang sama dapat jatuh di data latih **dan** data validasi sekaligus, sehingga model cukup "mengenali" baris yang sudah dihafalnya — mirip sidik jari pelanggan di Langkah 4, tetapi kali ini salinannya identik. Mengapa `class_weight="balanced"` (Lab 7) tidak menimbulkan masalah ini?

Yang perlu tampak: skor cara salah melonjak mendekati 1, sedangkan skor cara benar kembali ke kisaran skor tanpa *oversampling*. Dengan pengaturan di atas (diuji pada scikit-learn 1.6 dan 1.9; hasilnya sama), ROC-AUC cara salah ≈ 0,99, cara benar ≈ 0,69, dan tanpa *oversampling* ≈ 0,70. Dua angka terakhir bergantung pada urutan baris, karena `skf` membagi lipatan menurut posisi baris: tanpa `.sort_index()` keduanya menjadi ≈ 0,68 dan ≈ 0,69, dan cara penggandaan yang sedikit berbeda juga dapat menggeser angka persisnya. Selisih ≈ 0,3 antara cara salah dan cara benar tetap. Menggandakan baris tidak menambah informasi baru; efeknya kurang lebih sama dengan memberi bobot lebih pada kelas minoritas. SMOTE di dalam `imblearn.pipeline.Pipeline` dibahas di Lab 7 Tantangan 3.

### Tantangan 2 — Berapa Banyak Data yang Dibutuhkan

Jalankan validasi silang dengan `n_splits` 3, 5, dan 10. Bandingkan rerata dan simpangannya (`ddof=1`). Apa yang terjadi pada simpangan seiring bertambahnya lipatan, dan mengapa?

### Tantangan 3 — Sidik Jari Pelanggan

Ulangi Langkah 4 dengan empat himpunan fitur: semua `kol_bersih`, tanpa `jarak_gudang_km`, tanpa `umur`, dan tanpa keduanya. Pada keempat percobaan pakai `SelectKBest(f_classif, k="all")` — artinya **tanpa seleksi** (ubah `buat_pipa()` agar menerima argumen `k`) — sehingga yang dibandingkan hanya keberadaan kolom, bukan pilihan `SelectKBest`.

1. Bagaimana selisih `StratifiedKFold` − `GroupKFold` berubah antarpercobaan? Bandingkan terutama *tanpa `jarak_gudang_km`* dengan *tanpa keduanya*: apakah `umur` — yang sama sekali tidak memengaruhi target pada Langkah 1 — ikut memperbesar selisih? Mengapa bisa demikian? *Petunjuk:* rata-rata berapa pelanggan berbagi satu nilai `umur`?
2. Periksa apakah `SelectKBest(k=5)` di Langkah 4 memilih `umur` pada setiap lipatan (pakai `cross_validate(..., return_estimator=True)`, lalu `get_support()` pada langkah `"pilih"`). Mengapa percobaan nomor 1 sulit ditafsirkan bila `k` sekadar diturunkan satu setiap kali sebuah kolom dibuang?

### Tantangan 4 — Menelusuri Lipatan yang Menyimpang

Pada `GroupKFold`, temukan lipatan dengan skor terendah. Periksa ciri pelanggan pada lipatan itu — adakah yang membedakannya? Temuan semacam ini sering mengungkap kelompok yang kurang terwakili.

---

## Checklist Penyelesaian

- [ ] Keempat kebocoran pada Langkah 2 ditemukan dan **mekanismenya dijelaskan**
- [ ] Dampak tiap perbaikan diukur dan dilaporkan
- [ ] `GroupKFold` diterapkan dan selisihnya dibahas
- [ ] Kebocoran seleksi fitur pada data lebar ditunjukkan (di luar vs di dalam `Pipeline`)
- [ ] `TimeSeriesSplit` diterapkan dan struktur lipatannya ditampilkan
- [ ] **Rerata dan simpangan** dilaporkan, bukan rerata saja
- [ ] Sebaran antarlipatan divisualisasikan
- [ ] Seluruh sel pemeriksaan otomatis lulus
- [ ] Daftar periksa kebocoran dicentang
- [ ] Laporan temuan satu halaman disertakan
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 4](../03-modules/week-04-pembagian-data-dan-kebocoran.md)
2. [Bab 4 buku ajar](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md)
3. Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns*, 4(9), 100804.
4. Dokumentasi scikit-learn — *Cross-validation*. <https://scikit-learn.org/stable/modules/cross_validation.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
