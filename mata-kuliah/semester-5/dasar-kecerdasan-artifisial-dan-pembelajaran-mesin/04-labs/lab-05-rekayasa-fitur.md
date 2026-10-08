# Lab 05: Rekayasa Fitur

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 5 |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-05 |
| Durasi | 100 menit |
| Prasyarat | Lab 4 selesai |
| Bobot | 2,0% (Observasi, Sub-CPMK102-1) |
| Diuji pada | scikit-learn 1.6 dan 1.9, pandas 2.2 dan 3.0 (Oktober 2026) |

---

## Tujuan Praktikum

1. Merancang fitur baru dari data mentah dengan pengetahuan domain.
2. Mengukur sumbangan tiap kelompok fitur terhadap kinerja validasi.
3. Memeriksa setiap fitur baru terhadap risiko kebocoran.
4. Menerapkan pemilihan fitur di dalam `Pipeline`.

---

## Ketentuan Khusus Lab Ini

> **Model dan hiperparameter DIKUNCI.** Hanya fitur yang boleh diubah. Dengan begitu, setiap peningkatan yang terjadi **hanya** dapat berasal dari rekayasa fitur — bukan dari penggantian model.

> **Data per jam adalah deret waktu.** Karena itu seluruh lab ini memakai validasi silang **temporal** (`TimeSeriesSplit`): setiap lipatan berlatih pada masa lalu dan diuji pada periode **sesudahnya**. Lipatan acak (`StratifiedKFold(shuffle=True)`) tidak dipakai — pembagian acak pada data deret waktu membuat model berlatih pada jam-jam **sesudah** jam yang diujinya, yaitu kebocoran temporal ([Modul Minggu 4 §4.3.2](../03-modules/week-04-pembagian-data-dan-kebocoran.md#432-pembagian-temporal)).

---

## Persiapan

1. Buat notebook baru bernama `NIM_Nama_Lab05.ipynb`.
2. Jalankan **sel pembuka baku** di [Lampiran D](../06-buku-ajar/lampiran.md#lampiran-d-sel-pembuka-baku) — mengimpor pustaka, mencatat versi, dan menetapkan `RANDOM_STATE = 42`. Seluruh langkah di bawah mengandaikan sel itu sudah dijalankan.
3. **Data:** data kemacetan lab ini adalah **data sintetis (simulasi)** yang meniru pola kemacetan ruas jalan Jakarta — jam sibuk pagi dan sore, hari kerja vs. akhir pekan; **bukan data resmi BPS/lembaga** mana pun (termasuk dinas perhubungan). Data dibangkitkan pada Langkah 1: 6.000 baris — satu baris per jam, 250 hari pengamatan — dari 1 Januari 2026 pukul 00.00 s.d. 7 September 2026 pukul 23.00. Karena sintetis, aturan pembangkitnya dapat dibaca langsung di kode — manfaatkan itu saat menjawab pertanyaan Langkah 8 tentang fitur yang **tidak** membantu.

---

## Langkah-langkah

### LANGKAH 1: Data dengan Fitur Mentah

> **Data sintetis (simulasi)** yang meniru pola kemacetan ruas jalan Jakarta; bukan data resmi BPS/lembaga. Peluang macet hanya dibangkitkan dari **jam sibuk** dan **hari kerja/akhir pekan**, ditambah derau. Curah hujan, ruas, dan hari libur **tidak** ikut menentukan target; jumlah kendaraan dibuat lebih tinggi pada jam sibuk.

```python
# =============================================
# LANGKAH 1: Data kemacetan SINTETIS — fitur mentah
# (simulasi pola lalu lintas Jakarta — bukan data resmi BPS/lembaga)
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
print("Rentang waktu:", df["waktu"].min(), "s.d.", df["waktu"].max())
print("Proporsi macet:", round(df["macet"].mean(), 3))
print(df.head())
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
from sklearn.model_selection import cross_val_score, TimeSeriesSplit

# KUNCI: parameter ini tidak boleh diubah sepanjang lab
MODEL_TERKUNCI = RandomForestClassifier(
    n_estimators=200, max_depth=8, min_samples_leaf=20,
    random_state=RANDOM_STATE, n_jobs=-1,
)

# Data per jam = DERET WAKTU -> validasi silang TEMPORAL, bukan lipatan acak.
# TimeSeriesSplit mensyaratkan baris sudah urut waktu.
assert df["waktu"].is_monotonic_increasing, "Urutkan df menurut kolom waktu lebih dahulu"
CV = TimeSeriesSplit(n_splits=5)
for i, (idx_latih, idx_uji) in enumerate(CV.split(df), start=1):
    print(f"Lipatan {i}: latih {len(idx_latih):4d} jam s.d. "
          f"{df['waktu'].iloc[idx_latih[-1]]:%d-%m-%Y} | uji "
          f"{df['waktu'].iloc[idx_uji[0]]:%d-%m-%Y} s.d. "
          f"{df['waktu'].iloc[idx_uji[-1]]:%d-%m-%Y}")

def evaluasi(X, y, nama):
    # Kolom kategorik = semua kolom non-numerik (aman untuk pandas 2 dan 3)
    kol_num = X.select_dtypes(include=[np.number]).columns.tolist()
    kol_kat = [k for k in X.columns if k not in kol_num]
    pra = ColumnTransformer([
        ("num", "passthrough", kol_num),
        ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), kol_kat),
    ])
    pipa = Pipeline([("pra", pra), ("clf", MODEL_TERKUNCI)])
    skor = cross_val_score(pipa, X, y, cv=CV, scoring="f1", n_jobs=-1)
    print(f"{nama:38s} F1 = {skor.mean():.4f} ± {skor.std(ddof=1):.4f}  "
          f"({X.shape[1]} fitur)")
    return skor            # skor per lipatan (urutan lipatan selalu sama)

def banding_berpasangan(skor_a, skor_b):
    # Membandingkan dua model yang dinilai pada lipatan YANG SAMA (skor berpasangan).
    # d_i = skor_A,i - skor_B,i ; simpangan baku sampel s_d (ddof=1) ; SE = s_d / akar(k)
    # Aturan praktis mata kuliah: selisih BERMAKNA bila |d̄| > 2·SE DAN arah selisih
    # sama dengan d̄ pada sebagian besar lipatan (di sini: >= 80%, yaitu 4 dari 5).
    d = np.asarray(skor_a) - np.asarray(skor_b)
    k = len(d)
    d_bar = d.mean()
    s_d = d.std(ddof=1)
    se = s_d / np.sqrt(k)
    searah = int((np.sign(d) == np.sign(d_bar)).sum())
    bermakna = bool(abs(d_bar) > 2 * se and searah >= 0.8 * k)
    return {"d": d, "k": k, "d_bar": d_bar, "s_d": s_d, "SE": se,
            "searah": searah, "bermakna": bermakna}

y = df["macet"]
hasil = []
lipatan = {}               # skor per lipatan untuk perbandingan berpasangan
```

> Dengan `TimeSeriesSplit(n_splits=5)`, lipatan pertama hanya berlatih pada 1.000 jam pertama (±6 minggu) dan lipatan terakhir pada 5.000 jam; setiap lipatan diuji pada 1.000 jam berikutnya. Karena data latih lipatan awal sedikit, wajar bila skor antarlipatan lebih bergejolak daripada lipatan acak.
>
> Fungsi `banding_berpasangan` dipakai di Langkah 8 untuk menilai sumbangan tiap tahap. Karena semua tahap dinilai dengan objek `CV` yang **sama**, skor dua tahap pada lipatan ke-$i$ berpasangan; aturannya dijelaskan di [Bab 9 §9.4.2](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md#942-membaca-hasil-perbandingan) dan [Lampiran A.10](../06-buku-ajar/lampiran.md#a10-perbandingan-model). Seluruh simpangan baku skor lipatan di lab ini memakai **`ddof=1`** (simpangan baku sampel), sama dengan `pd.Series.std()`.

### LANGKAH 3: *Baseline* — Waktu sebagai Angka Mentah

```python
# =============================================
# LANGKAH 3: BASELINE — timestamp mentah
# =============================================
X0 = pd.DataFrame({
    # detik sejak 1970; resolusi detik ditetapkan eksplisit karena pada pandas 3
    # kolom ini beresolusi mikrodetik (pada pandas 2: nanodetik)
    "waktu_epoch": df["waktu"].astype("datetime64[s]").astype("int64"),
    "curah_hujan_mm": df["curah_hujan_mm"],
    "jumlah_kendaraan": df["jumlah_kendaraan"],
    "ruas": df["ruas"],
})
skor = evaluasi(X0, y, "0. Baseline (timestamp mentah)")
hasil.append({"Tahap": "0. Baseline", "F1": skor.mean(), "Simpangan": skor.std(ddof=1),
              "Fitur": X0.shape[1]})
lipatan["0. Baseline"] = skor
print("F1 per lipatan:", skor.round(3))
```

> Pada validasi temporal, `waktu_epoch` di lipatan uji **selalu** lebih besar daripada seluruh nilai di data latih, sehingga pohon keputusan tidak dapat memanfaatkannya (pohon tidak mengekstrapolasi). Perhatikan juga betapa besarnya simpangan *baseline* antarlipatan.

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

skor = evaluasi(X1, y, "1. + fitur waktu terurai")
hasil.append({"Tahap": "1. + waktu terurai", "F1": skor.mean(), "Simpangan": skor.std(ddof=1),
              "Fitur": X1.shape[1]})
lipatan["1. + waktu terurai"] = skor
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

skor = evaluasi(X2, y, "2. + penyandian siklik")
hasil.append({"Tahap": "2. + siklik", "F1": skor.mean(), "Simpangan": skor.std(ddof=1),
              "Fitur": X2.shape[1]})
lipatan["2. + siklik"] = skor
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

# Sebagian hari libur nasional 2026 (SKB 3 Menteri tentang libur nasional dan
# cuti bersama 2026): Tahun Baru, Idulfitri 1447 H (21-22 Maret), Hari Buruh,
# Kenaikan Yesus Kristus, dan HUT RI. Cuti bersama (mis. 20 Maret) tidak dimasukkan.
libur = pd.to_datetime(["2026-01-01", "2026-03-21", "2026-03-22",
                        "2026-05-01", "2026-05-14", "2026-08-17"])
X3["hari_libur"] = df["waktu"].dt.normalize().isin(libur).astype(int)

skor = evaluasi(X3, y, "3. + pengetahuan domain")
hasil.append({"Tahap": "3. + domain", "F1": skor.mean(), "Simpangan": skor.std(ddof=1),
              "Fitur": X3.shape[1]})
lipatan["3. + domain"] = skor
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
# PERHATIAN: dihitung dari data lengkap (termasuk MASA DEPAN) -> RAWAN KEBOCORAN.
# Di sini hanya untuk demonstrasi; pada proyek harus di dalam Pipeline.
rata_ruas = df.groupby("ruas")["jumlah_kendaraan"].transform("mean")
X4["kendaraan_relatif"] = X4["jumlah_kendaraan"] / rata_ruas

skor = evaluasi(X4, y, "4. + rasio dan transformasi")
hasil.append({"Tahap": "4. + rasio", "F1": skor.mean(), "Simpangan": skor.std(ddof=1),
              "Fitur": X4.shape[1]})
lipatan["4. + rasio"] = skor
```

> **Catat sebagai temuan:** fitur `kendaraan_relatif` dihitung dari seluruh data — termasuk jam-jam yang pada validasi temporal berada di **masa depan** lipatan latih — dan karena itu **berisiko bocor**. Pada proyek, perhitungan semacam ini harus berada di dalam `Pipeline` sebagai transformer sendiri, agar di-*fit* hanya pada lipatan latih.

### LANGKAH 8: Ringkasan dan Analisis

```python
# =============================================
# LANGKAH 8: Ringkasan peningkatan
# =============================================
import matplotlib.pyplot as plt

tabel = pd.DataFrame(hasil)
tabel["Peningkatan"] = tabel["F1"] - tabel["F1"].iloc[0]
tabel["Sumbangan tahap"] = tabel["F1"].diff()
print(tabel.round(4).to_string(index=False))

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.errorbar(range(len(tabel)), tabel["F1"], yerr=tabel["Simpangan"],
            fmt="o-", capsize=5)
ax.set_xticks(range(len(tabel)))
ax.set_xticklabels(tabel["Tahap"], rotation=20, ha="right")
ax.set_ylabel("F1 (validasi silang temporal, 5 lipatan)")
ax.set_title(f"Peningkatan dari rekayasa fitur — model dikunci (n={len(df)})")
plt.tight_layout(); plt.show()

# Kesimpulan DIHITUNG dari hasil — bukan teks tetap.
# Setiap tahap dibandingkan dengan tahap SEBELUMNYA secara BERPASANGAN per lipatan:
# semua tahap dinilai dengan objek CV yang sama, jadi lipatan ke-i dapat dipasangkan.
tahap = tabel["Tahap"].tolist()
print(f"\nSumbangan terbesar: {tabel.loc[tabel['Sumbangan tahap'].idxmax(), 'Tahap']}")
banding_tahap = {}
for i in range(1, len(tahap)):
    b = banding_berpasangan(lipatan[tahap[i]], lipatan[tahap[i - 1]])
    banding_tahap[tahap[i]] = b
    if b["bermakna"] and b["d_bar"] > 0:
        status = "membantu (|d̄| > 2·SE dan searah di sebagian besar lipatan)"
    elif b["bermakna"]:
        status = "MERUGIKAN — F1 turun secara bermakna"
    elif b["d_bar"] <= 0:
        status = "TIDAK membantu (F1 rata-rata tidak naik)"
    else:
        status = "naik, tetapi belum bermakna menurut aturan |d̄| > 2·SE — belum meyakinkan"
    print(f"  {tahap[i]:20s} d̄ = {b['d_bar']:+.4f} | s_d = {b['s_d']:.4f} | "
          f"SE = {b['SE']:.4f} | 2·SE = {2 * b['SE']:.4f} | "
          f"searah {b['searah']}/{b['k']}: {status}")
    print(f"  {'':20s} selisih per lipatan: {np.round(b['d'], 4)}")

# Kumulatif: tahap domain dibandingkan langsung dengan baseline
b_kumulatif = banding_berpasangan(lipatan["3. + domain"], lipatan["0. Baseline"])
print(f"\nKumulatif '3. + domain' − '0. Baseline': d̄ = {b_kumulatif['d_bar']:+.4f} | "
      f"s_d = {b_kumulatif['s_d']:.4f} | SE = {b_kumulatif['SE']:.4f} | "
      f"2·SE = {2 * b_kumulatif['SE']:.4f} | "
      f"searah {b_kumulatif['searah']}/{b_kumulatif['k']} | "
      f"bermakna: {'ya' if b_kumulatif['bermakna'] else 'tidak'}")
```

> **Mengapa berpasangan?** Kolom `Sumbangan tahap` adalah rerata selisih $\bar d$. Membandingkannya dengan kolom `Simpangan` (simpangan baku skor **satu** tahap) keliru: sebagian besar simpangan itu berasal dari lipatannya sendiri — lipatan 1, yang data latihnya paling sedikit, memberi skor terendah di setiap tahap — dan variasi bersama itu hilang ketika skor dua tahap dikurangkan per lipatan. Ketidakpastian $\bar d$ diukur oleh galat baku $SE = s_d/\sqrt{k}$ dari selisih per lipatan. Hilangnya variasi bersama tidak menjamin $s_d$ selalu lebih kecil daripada `Simpangan`: perbandingan lama memakai besaran yang salah (simpangan baku skor satu tahap, bukan galat baku selisih per lipatan), sehingga dapat keliru **ke dua arah**. Pada data lab ini, cara lama itu menyembunyikan kenaikan yang konsisten — *+ siklik* ($\bar d \approx 0{,}03$ < `Simpangan` ≈ 0,09) akan dinyatakan "belum meyakinkan", padahal naik di 4–5 dari 5 lipatan dan lolos aturan $2 \cdot SE$ — sekaligus meloloskan kenaikan yang terpusat di satu lipatan: *+ domain* ($\bar d \approx 0{,}045$ > `Simpangan` ≈ 0,036) akan dinyatakan "membantu", padahal $s_d \approx 0{,}054$–$0{,}056$ justru lebih besar daripada `Simpangan` tahap itu dan $|\bar d| < 2 \cdot SE$. **Aturan praktis mata kuliah:** sumbangan dianggap bermakna bila $|\bar d| > 2 \cdot SE$ **dan** arahnya konsisten di minimal 4 dari 5 lipatan ([Bab 9 §9.4.2](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md#942-membaca-hasil-perbandingan), [Lampiran A.10](../06-buku-ajar/lampiran.md#a10-perbandingan-model)). Aturan ini hanya penyaring kasar — pada `TimeSeriesSplit` data latih antarlipatan pun bertumpuk, sehingga skornya tidak saling bebas. Untuk analisis formal, gunakan *corrected resampled t-test* (Nadeau & Bengio, 2003).

**Pemeriksaan otomatis.** Sel berikut harus lulus tanpa `AssertionError`; bila gagal, pesannya menunjukkan apa yang perlu diperiksa.

```python
# =============================================
# Pemeriksaan otomatis — pelajaran kunci Lab 5
# =============================================
f1_dasar = tabel["F1"].iloc[0]
f1_terbaik = tabel["F1"].max()
assert f1_terbaik - f1_dasar > 0.15, (
    f"Dengan model TERKUNCI, rekayasa fitur seharusnya menaikkan F1 validasi jauh di atas "
    f"baseline (sekarang {f1_terbaik - f1_dasar:+.4f}) — periksa MODEL_TERKUNCI dan CV")
assert b_kumulatif["bermakna"] and b_kumulatif["d_bar"] > 0, (
    f"Fitur waktu + domain seharusnya mengungguli timestamp mentah secara bermakna "
    f"(sekarang d̄ = {b_kumulatif['d_bar']:+.4f}, SE = {b_kumulatif['SE']:.4f}, searah "
    f"{b_kumulatif['searah']}/{b_kumulatif['k']} lipatan) — periksa Langkah 4–6")
assert not banding_tahap["4. + rasio"]["bermakna"], (
    "Tahap rasio dan transformasi seharusnya TIDAK membantu secara bermakna: curah hujan "
    "dan ruas tidak ikut menentukan target di Langkah 1 — periksa Langkah 7")
d_uji = lipatan["2. + siklik"] - lipatan["1. + waktu terurai"]
assert np.isclose(banding_tahap["2. + siklik"]["SE"],
                  pd.Series(d_uji).std() / np.sqrt(len(d_uji))), (
    "SE harus = s_d/√k dengan s_d simpangan baku SAMPEL (ddof=1) dari selisih per lipatan")
print("Pemeriksaan otomatis lulus.")
```

Pada data lab ini (diuji pada scikit-learn 1.6 dan 1.9), F1 validasi temporal naik dari ≈ 0,20 (± 0,21) pada *baseline* ke ≈ 0,50 (± 0,04) setelah fitur waktu dan domain ditambahkan — tanpa satu pun hiperparameter diubah. Menurut aturan berpasangan:

- **+ waktu terurai** memberi lompatan terbesar: $\bar d \approx +0{,}22$ dengan $2 \cdot SE \approx 0{,}14$, naik di 5 dari 5 lipatan — **membantu**.
- **+ siklik**: $\bar d \approx +0{,}03$ dengan $2 \cdot SE \approx 0{,}024$–$0{,}028$, searah di 4–5 dari 5 lipatan (bergantung versi) — **membantu**, tetapi tipis ($|\bar d|$ hanya ≈ 2,1–2,3 kali $SE$).
- **+ domain** naik di kelima lipatan ($\bar d \approx +0{,}045$–$0{,}047$), tetapi **belum lolos** aturan $2 \cdot SE$ ($2 \cdot SE \approx 0{,}05$): kenaikannya terpusat di lipatan 1 (≈ +0,14–0,15), sedangkan di lipatan 2–5 hanya +0,01 s.d. +0,04. Secara kumulatif, tahap ini jelas mengungguli *baseline* ($\bar d \approx +0{,}30$, $SE \approx 0{,}08$, searah 5/5).
- **+ rasio dan transformasi**: $\bar d \approx +0{,}005$ dan searah hanya di 3 dari 5 lipatan — **belum meyakinkan**; praktis tidak menambah apa-apa.

**Yang harus ditulis di sel Markdown:**
- Kelompok fitur mana yang memberi peningkatan terbesar?
- Adakah kelompok fitur yang **tidak** membantu? Apa dugaan sebabnya? *Petunjuk:* bandingkan dengan aturan pembangkit data di Langkah 1.
- Untuk tiap tahap, berapa selisih berpasangan terhadap tahap sebelumnya ($\bar d$, $s_d$, $SE$)? Apakah $|\bar d| > 2 \cdot SE$ dan arahnya konsisten (minimal 4 dari 5 lipatan)? Mengapa membandingkan $\bar d$ dengan kolom `Simpangan` keliru?
- Tahap *+ domain* naik di kelima lipatan, tetapi belum lolos aturan $2 \cdot SE$. Di lipatan mana kenaikannya terbesar, dan berapa jam data latih lipatan itu? Apa artinya bagi manfaat fitur pengetahuan domain ketika data latih masih sedikit?
- Mengapa simpangan *baseline* jauh lebih besar daripada tahap lain? *Petunjuk:* hitung `df.groupby(df["waktu"].dt.hour.isin([6, 7, 8, 16, 17, 18, 19]))["macet"].mean()` — berapa peluang macet pada jam sibuk bila hari kerja dan akhir pekan tidak dibedakan?

### LANGKAH 9: Pemilihan Fitur di Dalam `Pipeline`

```python
# =============================================
# LANGKAH 9: Pemilihan fitur — di dalam Pipeline
# =============================================
from sklearn.feature_selection import SelectKBest, f_classif

kol_num = X4.select_dtypes(include=[np.number]).columns.tolist()
kol_kat = [k for k in X4.columns if k not in kol_num]
# Setelah one-hot, 19 kolom numerik + 4 kolom ruas = 23 kolom masuk ke SelectKBest

for k in [5, 10, 15, "all"]:
    pra = ColumnTransformer([
        ("num", "passthrough", kol_num),
        ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), kol_kat),
    ])
    pipa = Pipeline([
        ("pra", pra),
        ("pilih", SelectKBest(f_classif, k=k)),   # DI DALAM Pipeline
        ("clf", MODEL_TERKUNCI),
    ])
    skor = cross_val_score(pipa, X4, y, cv=CV, scoring="f1", n_jobs=-1)
    print(f"k={str(k):>3s}: F1 = {skor.mean():.4f} ± {skor.std(ddof=1):.4f}")
```

> **Perhatikan penempatannya.** `SelectKBest` berada **di dalam** `Pipeline`, sehingga pada tiap lipatan ia di-*fit* ulang hanya dari data latih lipatan itu. Menempatkannya di luar adalah kebocoran — sebagaimana ditunjukkan pada Lab 4. Baris `k=all` memakai seluruh kolom dan karena itu sama dengan tahap 4 pada Langkah 7.

---

## Tantangan Tambahan

### Tantangan 1 — Transformer Agregat yang Aman

Bangun kelas transformer sendiri (turunan `BaseEstimator` dan `TransformerMixin`) yang menghitung `kendaraan_relatif` **di dalam** `Pipeline`, sehingga rata-rata per ruas dihitung hanya dari lipatan latih — tidak pernah dari masa depan. Bandingkan skornya dengan versi yang bocor pada Langkah 7.

### Tantangan 2 — Fitur yang Gagal

Tambahkan lima fitur yang Anda duga akan membantu tetapi ternyata tidak. Catat masing-masing beserta dugaan sebabnya. **Catatan fitur yang gagal dinilai setara dengan yang berhasil.**

### Tantangan 3 — Kutukan Dimensi

Tambahkan `PolynomialFeatures(degree=2)` pada fitur numerik. Berapa kolom yang dihasilkan? Apakah F1 naik atau turun? Jelaskan hubungannya dengan kutukan dimensi dan jumlah baris data.

---

## Checklist Penyelesaian

- [ ] Model dan hiperparameter **tetap terkunci** sepanjang lab
- [ ] *Baseline* dengan fitur mentah dijalankan lebih dahulu
- [ ] Minimal empat kelompok fitur ditambahkan **bertahap**
- [ ] Skor diukur pada **validasi silang temporal** (`TimeSeriesSplit`), bukan pada data latih dan bukan dengan lipatan acak
- [ ] Simpangan antarlipatan (`ddof=1`) dilaporkan di setiap tahap
- [ ] **Sumbangan tiap tahap dinilai dengan selisih berpasangan per lipatan** ($\bar d$, $s_d$ dengan `ddof=1`, $SE = s_d/\sqrt{k}$), bukan dengan membandingkan selisih rerata pada simpangan
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
5. Nadeau, C., & Bengio, Y. (2003). Inference for the Generalization Error. *Machine Learning*, 52(3), 239–281.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
