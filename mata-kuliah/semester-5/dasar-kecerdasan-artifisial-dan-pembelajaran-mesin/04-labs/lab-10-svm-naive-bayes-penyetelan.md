# Lab 10: SVM, Naive Bayes, dan Penyetelan Hiperparameter

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 10 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-09 |
| Durasi | 100 menit |
| Prasyarat | Lab 9 selesai |
| Bobot | 1,875% (Observasi, Sub-CPMK082-1) |
| Diuji pada | scikit-learn 1.6 dan 1.9, pandas 2.2 dan 3.0 (Oktober 2026) |

---

## Tujuan Praktikum

1. Menerapkan SVM dengan berbagai *kernel* dan menyetel `C` serta `gamma`.
2. Menerapkan Naive Bayes sebagai pembanding cepat.
3. Menyetel hiperparameter pada data latih saja.
4. Merancang dan menjalankan perbandingan lima model yang adil: lipatan yang sama untuk semua model, SVM tersetel dinilai dengan **validasi silang bersarang** (*nested cross-validation*), dan selisih antarmodel dinilai **secara berpasangan** per lipatan.

---

## Persiapan

1. Buat notebook baru bernama `NIM_Nama_Lab10.ipynb`.
2. Jalankan **sel pembuka baku** di [Lampiran D](../06-buku-ajar/lampiran.md#lampiran-d-sel-pembuka-baku) — mengimpor pustaka, mencatat versi, dan menetapkan `RANDOM_STATE = 42`. Seluruh langkah di bawah mengandaikan sel itu sudah dijalankan.
3. **Data:** data sesi belanja lab ini adalah **data sintetis (simulasi)** yang meniru pola kunjungan ke lokapasar (*e-commerce*) di Indonesia; **bukan data resmi BPS/lembaga** mana pun (termasuk platform lokapasar). Data dibangkitkan pada Langkah 1: 3.000 sesi dengan ±49% berakhir dengan pembelian. Aturan pembangkit label (kunjungan lebih lama, lebih banyak halaman dibuka, nilai keranjang lebih besar, dan diskon lebih tinggi → peluang membeli naik) adalah **asumsi ilustratif**, bukan temuan empiris tentang perilaku konsumen; `usia_akun_hari`, `perangkat`, dan `kanal` sengaja **tidak** ikut menentukan label. Hubungan fitur–label sengaja dibuat lemah (ROC-AUC terbaik ±0,65), sehingga selisih antarmodel kecil — situasi yang tepat untuk berlatih memutuskan apakah suatu selisih **bermakna** atau hanya kebetulan lipatan.
4. Langkah 6, 8, dan 9 melatih ratusan SVM. Seluruh notebook biasanya selesai dalam beberapa menit; tunggu sampai sel selesai sebelum menjalankan sel berikutnya.

---

## Langkah-langkah

### LANGKAH 1: Data Sintetis dan Pembagian

> **Data sintetis (simulasi)** yang meniru pola sesi belanja di lokapasar Indonesia; bukan data resmi BPS/lembaga. Peluang membeli dibangkitkan dari durasi kunjungan, jumlah halaman, nilai keranjang, dan diskon, ditambah keacakan.

```python
# =============================================
# LANGKAH 1: Data SINTETIS sesi belanja daring (±49% membeli)
# (simulasi, bukan data resmi BPS/lembaga)
# =============================================
import numpy as np, pandas as pd, time
from sklearn.model_selection import train_test_split, StratifiedKFold

rng = np.random.default_rng(RANDOM_STATE)
n = 3000

df = pd.DataFrame({
    "durasi_kunjungan_mnt": rng.gamma(2.0, 12, size=n).round(1),
    "jumlah_halaman":       rng.poisson(6, size=n) + 1,
    "nilai_keranjang_rb":   rng.gamma(2.0, 200, size=n).round(0),
    "usia_akun_hari":       rng.gamma(3.0, 150, size=n).round(0),
    "diskon_persen":        rng.choice([0, 5, 10, 15, 20, 30], size=n),
    "perangkat":            rng.choice(["Android","iOS","Web"], size=n,
                                       p=[0.55, 0.30, 0.15]),
    "kanal":                rng.choice(["Organik","Iklan","Referal","Surel"], size=n),
})

# Aturan pembangkit label (asumsi ilustratif): durasi, jumlah halaman, nilai keranjang,
# dan diskon menaikkan peluang membeli. usia_akun_hari, perangkat, dan kanal
# TIDAK ikut menentukan label.
logit = (-2.0 + 0.018 * df["durasi_kunjungan_mnt"] + 0.10 * df["jumlah_halaman"]
         + 0.0011 * df["nilai_keranjang_rb"] + 0.028 * df["diskon_persen"])
df["beli"] = rng.binomial(1, 1 / (1 + np.exp(-logit)))

X = df.drop(columns=["beli"]); y = df["beli"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE)

print("Dimensi:", df.shape, "| Proporsi positif:", round(y.mean(), 3))
print("Latih:", X_train.shape, "| Uji:", X_test.shape)
```

### LANGKAH 2: `Pipeline` Dasar dan Alat Pembanding Berpasangan

```python
# =============================================
# LANGKAH 2: Pipeline yang dipakai seluruh model
# =============================================
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

kol_kat = ["perangkat", "kanal"]
kol_num = [c for c in X.columns if c not in kol_kat]

def buat_pipa(clf, skala=True):
    pra = ColumnTransformer([
        ("num", StandardScaler() if skala else "passthrough", kol_num),
        ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), kol_kat),
    ])
    return Pipeline([("pra", pra), ("clf", clf)])

# Satu objek lipatan untuk SEMUA perbandingan: setiap model dinilai pada lipatan yang sama
CV = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

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
```

> Fungsi `banding_berpasangan` dipakai di Langkah 4, 8, dan 9; alasannya dijelaskan di Langkah 8. Seluruh simpangan baku skor lipatan di lab ini memakai **`ddof=1`** (simpangan baku sampel), sama dengan `pd.Series.std()`.

### LANGKAH 3: SVM dengan Tiga *Kernel*

```python
# =============================================
# LANGKAH 3: SVM — penskalaan WAJIB
# =============================================
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

baris = []
for kernel in ["linear", "rbf", "poly"]:
    pipa = buat_pipa(SVC(kernel=kernel, C=1.0, gamma="scale",
                         random_state=RANDOM_STATE))
    t0 = time.time()
    skor = cross_val_score(pipa, X_train, y_train, cv=CV,
                           scoring="roc_auc", n_jobs=-1)
    baris.append({"Kernel": kernel, "ROC-AUC": skor.mean(),
                  "Simpangan": skor.std(ddof=1), "Waktu (s)": time.time() - t0})

print(pd.DataFrame(baris).round(4).to_string(index=False))
```

### LANGKAH 4: Membuktikan Penskalaan Itu Wajib

```python
# =============================================
# LANGKAH 4: SVM tanpa penskalaan
# =============================================
pipa_skala = buat_pipa(SVC(kernel="rbf", random_state=RANDOM_STATE), skala=True)
pipa_tanpa = buat_pipa(SVC(kernel="rbf", random_state=RANDOM_STATE), skala=False)

s1 = cross_val_score(pipa_skala, X_train, y_train, cv=CV, scoring="roc_auc", n_jobs=-1)
s2 = cross_val_score(pipa_tanpa, X_train, y_train, cv=CV, scoring="roc_auc", n_jobs=-1)

print(f"SVM DENGAN penskalaan : {s1.mean():.4f} ± {s1.std(ddof=1):.4f}")
print(f"SVM TANPA penskalaan  : {s2.mean():.4f} ± {s2.std(ddof=1):.4f}")

# Kedua pipa dinilai pada lipatan yang SAMA -> bandingkan selisih per lipatan
b_skala = banding_berpasangan(s1, s2)
print("Selisih per lipatan   :", np.round(b_skala["d"], 4))
print(f"Rerata selisih d̄      : {b_skala['d_bar']:+.4f} "
      f"(SE = {b_skala['SE']:.4f}; searah pada {b_skala['searah']} dari {b_skala['k']} lipatan)")

# --- Kesimpulan dihitung dari hasil ---
if b_skala["bermakna"] and b_skala["d_bar"] > 0:
    print("Kesimpulan: penskalaan menaikkan ROC-AUC SVM secara bermakna.")
elif b_skala["bermakna"]:
    print("Kesimpulan: tanpa penskalaan justru lebih baik — periksa buat_pipa().")
else:
    print("Kesimpulan: selisih belum bermakna menurut aturan |d̄| > 2·SE.")
```

**Tulis penjelasan:** mengapa `nilai_keranjang_rb` (ratusan) menenggelamkan `jumlah_halaman` (satuan) pada perhitungan jarak?

### LANGKAH 5: Naive Bayes sebagai Pembanding Cepat

```python
# =============================================
# LANGKAH 5: Naive Bayes
# =============================================
from sklearn.naive_bayes import GaussianNB

pipa_nb = buat_pipa(GaussianNB())
t0 = time.time()
s_nb = cross_val_score(pipa_nb, X_train, y_train, cv=CV, scoring="roc_auc", n_jobs=-1)
print(f"GaussianNB: {s_nb.mean():.4f} ± {s_nb.std(ddof=1):.4f}  "
      f"({time.time()-t0:.2f} s)")

# Memeriksa asumsi kebebasan: apakah fitur saling berkorelasi?
korelasi = X_train[kol_num].corr()
segitiga_atas = korelasi.where(np.triu(np.ones(korelasi.shape), k=1).astype(bool)).stack()
kuat = segitiga_atas[segitiga_atas.abs() > 0.3]
print("\nKorelasi antarfitur numerik (nilai absolut > 0,3):")
if len(kuat) > 0:
    print(kuat.round(3).to_string())
else:
    print(f"  (tidak ada; korelasi absolut terbesar {segitiga_atas.abs().max():.3f})")
```

> Asumsi kebebasan Naive Bayes hampir selalu dilanggar pada data nyata. Pada data sintetis ini fitur numerik dibangkitkan **saling bebas**, sehingga korelasinya mendekati nol — tetapi asumsi lain GaussianNB (sebaran normal per kelas) tetap dilanggar oleh fitur `gamma`/Poisson dan fitur *one-hot*. Yang penting bukan apakah asumsi dilanggar, melainkan **apakah modelnya tetap berguna** — dan itu diukur, bukan diandaikan.

### LANGKAH 6: Penyetelan Hiperparameter

```python
# =============================================
# LANGKAH 6: GridSearchCV — HANYA pada data latih
# =============================================
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import loguniform

ruang = {
    "clf__C":     [0.1, 1, 10, 100],
    "clf__gamma": [0.001, 0.01, 0.1, "scale"],
}

pencarian = GridSearchCV(
    buat_pipa(SVC(kernel="rbf", random_state=RANDOM_STATE)),
    ruang, cv=CV, scoring="roc_auc", n_jobs=-1, return_train_score=True,
)
t0 = time.time()
pencarian.fit(X_train, y_train)          # data uji TIDAK disentuh
print(f"Grid search selesai dalam {time.time()-t0:.1f} s")
print("Parameter terbaik:", pencarian.best_params_)
print(f"Skor CV terbaik  : {pencarian.best_score_:.4f}")

# Memeriksa apakah optimum berada di TEPI ruang pencarian
hasil_cv = pd.DataFrame(pencarian.cv_results_)
# std_test_score bawaan scikit-learn memakai ddof=0; agar seragam dengan langkah lain,
# simpangan baku antarlipatan dihitung ulang dengan ddof=1 dari skor tiap lipatan
kol_lipatan = [f"split{i}_test_score" for i in range(CV.get_n_splits())]
hasil_cv["sd_lipatan"] = hasil_cv[kol_lipatan].std(axis=1, ddof=1)
print("\nLima kombinasi teratas:")
print(hasil_cv.nlargest(5, "mean_test_score")[
    ["param_clf__C", "param_clf__gamma", "mean_test_score", "sd_lipatan"]
].round(4).to_string(index=False))
```

**Periksa:** apakah nilai `C` atau `gamma` terbaik berada di ujung rentang yang dicoba? Bila ya, ruang pencarian perlu diperluas.

### LANGKAH 7: `best_score_` Bukan Kinerja Akhir

```python
# =============================================
# LANGKAH 7: Perbedaan best_score_ dan skor uji
# =============================================
from sklearn.metrics import roc_auc_score

# SVC tanpa probability=True tidak memiliki predict_proba; ROC-AUC cukup memakai
# skor keputusan (decision_function) karena yang dinilai hanya urutan skornya.
skor_uji = roc_auc_score(y_test, pencarian.best_estimator_.decision_function(X_test))

print(f"best_score_ (CV data latih): {pencarian.best_score_:.4f}")
print(f"Skor pada data uji         : {skor_uji:.4f}")
print(f"Selisih                    : {pencarian.best_score_ - skor_uji:+.4f}")

# --- Kesimpulan dihitung dari hasil ---
print("\nbest_score_ sudah DIOPTIMALKAN atas ruang pencarian, sehingga secara rata-rata")
print("cenderung lebih tinggi daripada kinerja sebenarnya (bias seleksi).")
if pencarian.best_score_ > skor_uji:
    print("Pada data ini pun best_score_ > skor uji, sesuai kecenderungan tersebut.")
else:
    print("Pada data ini skor uji justru >= best_score_: satu data uji (600 baris) juga")
    print("mengandung variasi acak, sehingga satu pembagian tidak dapat membuktikan atau")
    print("membantah bias seleksi. Besarnya bias diukur dengan CV bersarang (Langkah 8–9).")
print("Yang dilaporkan sebagai kinerja akhir adalah skor pada data uji.")
```

### LANGKAH 8: Perbandingan Lima Model yang Adil

Dua syarat keadilan dipakai sekaligus:

1. **Lipatan yang sama** (`CV`) untuk semua model, sehingga skor kedua model pada lipatan ke-*i* **berpasangan**: keduanya dinilai pada baris uji yang persis sama.
2. **SVM tersetel dinilai dengan CV bersarang.** Memasukkan `pencarian.best_estimator_` ke tabel berarti menilai SVM pada lipatan yang **sudah dipakai untuk memilih** `C` dan `gamma`-nya — skornya akan sama persis dengan `best_score_` (dibuktikan di Langkah 9) dan memihak SVM. Karena itu yang dimasukkan adalah **objek `GridSearchCV` yang belum dilatih**: pada setiap lipatan luar, pencarian diulang hanya pada 4/5 data latih lipatan itu (dengan lipatan dalam `CV_DALAM`), lalu model terpilih dinilai pada lipatan luar yang tidak ikut memilihnya.

```python
# =============================================
# LANGKAH 8: Perbandingan — lipatan SAMA untuk semua, SVM dengan CV bersarang
# =============================================
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier

# Lipatan DALAM untuk penyetelan di dalam setiap lipatan luar (3 lipatan agar lebih cepat)
CV_DALAM = StratifiedKFold(n_splits=3, shuffle=True, random_state=RANDOM_STATE)
svm_bersarang = GridSearchCV(                        # BELUM dilatih
    buat_pipa(SVC(kernel="rbf", random_state=RANDOM_STATE)),
    ruang, cv=CV_DALAM, scoring="roc_auc", n_jobs=-1)

kandidat = {
    "Baseline (mayoritas)": buat_pipa(DummyClassifier(strategy="most_frequent")),
    "Naive Bayes":          buat_pipa(GaussianNB()),
    "Regresi logistik":     buat_pipa(LogisticRegression(max_iter=1000,
                                                         random_state=RANDOM_STATE)),
    "SVM (RBF, disetel)":   svm_bersarang,           # BUKAN pencarian.best_estimator_
    "Random Forest":        buat_pipa(RandomForestClassifier(
                                n_estimators=300, random_state=RANDOM_STATE, n_jobs=-1),
                                skala=False),
    "Gradient Boosting":    buat_pipa(HistGradientBoostingClassifier(
                                max_iter=300, early_stopping=True,
                                random_state=RANDOM_STATE), skala=False),
}

baris, skor_lipatan = [], {}
for nama, pipa in kandidat.items():
    t0 = time.time()
    skor = cross_val_score(pipa, X_train, y_train, cv=CV,   # CV luar yang SAMA
                           scoring="roc_auc", n_jobs=-1)
    skor_lipatan[nama] = skor                                # disimpan untuk uji berpasangan
    baris.append({"Model": nama, "ROC-AUC": skor.mean(), "Simpangan": skor.std(ddof=1),
                  "Min": skor.min(), "Maks": skor.max(),
                  "Waktu (s)": time.time() - t0})

tabel = (pd.DataFrame(baris).sort_values("ROC-AUC", ascending=False)
           .reset_index(drop=True))
print(tabel.round(4).to_string(index=False))
print("(Waktu SVM mencakup penyetelan ulang di setiap lipatan luar.)")

# Setiap model dibandingkan dengan peringkat 1 secara BERPASANGAN per lipatan
juara = tabel.loc[0, "Model"]
banding = []
for nama in tabel["Model"][1:]:
    b = banding_berpasangan(skor_lipatan[juara], skor_lipatan[nama])
    banding.append({"Dibandingkan dengan": nama, "d̄": b["d_bar"], "s_d": b["s_d"],
                    "SE": b["SE"], "|d̄|/SE": abs(b["d_bar"]) / b["SE"] if b["SE"] > 0 else np.inf,
                    "Searah": f"{b['searah']}/{b['k']}",
                    "Bermakna?": "ya" if b["bermakna"] else "tidak"})
print(f"\nSelisih berpasangan: '{juara}' dikurangi model lain (per lipatan)")
print(pd.DataFrame(banding).round(4).to_string(index=False))

# --- Kesimpulan peringkat 1 vs 2, dihitung dari hasil ---
kedua = tabel.loc[1, "Model"]
b12 = banding_berpasangan(skor_lipatan[juara], skor_lipatan[kedua])
print(f"\nPeringkat 1 vs 2: {juara} − {kedua}")
print("  selisih per lipatan:", np.round(b12["d"], 4))
print(f"  d̄ = {b12['d_bar']:+.4f} | s_d = {b12['s_d']:.4f} | SE = {b12['SE']:.4f} "
      f"| batas 2·SE = {2 * b12['SE']:.4f} | searah {b12['searah']}/{b12['k']}")
if b12["bermakna"]:
    print(f"Kesimpulan: {juara} lebih baik daripada {kedua} secara bermakna "
          f"(|d̄| > 2·SE dan searah di sebagian besar lipatan).")
else:
    print(f"Kesimpulan: TIDAK DAPAT DISIMPULKAN bahwa {juara} lebih baik daripada {kedua};"
          f"\n  selisihnya masih dalam jangkauan variasi antarlipatan.")
```

> **Mengapa berpasangan, dan mengapa SE?** Karena semua model dinilai pada lipatan yang **sama**, sebagian variasi skor berasal dari lipatannya sendiri (ada lipatan yang "mudah", ada yang "sulit") dan dialami semua model bersama-sama. Selisih per lipatan $d_i = \text{skor}_{A,i} - \text{skor}_{B,i}$ menghapus variasi bersama itu. Ketidakpastian **rerata** selisih diukur oleh galat baku $SE = s_d/\sqrt{k}$ — bukan oleh simpangan baku skor masing-masing model. Rumus "simpangan gabungan" $\sqrt{s_1^2+s_2^2}$ **tidak dipakai**: rumus itu memperlakukan skor kedua model seolah-olah tidak berpasangan dan memakai simpangan baku (SD) alih-alih galat baku (SE).
>
> **Aturan praktis mata kuliah:** selisih dianggap bermakna bila $|\bar d| > 2 \cdot SE$ **dan** arahnya konsisten di sebagian besar lipatan (di lab ini: minimal 4 dari 5). Aturan ini hanya penyaring kasar: skor antarlipatan tidak benar-benar saling bebas (data latihnya tumpang-tindih), sehingga $SE$ cenderung terlalu kecil. Untuk analisis formal, gunakan *corrected resampled t-test* (Nadeau & Bengio, 2003) — lihat Tantangan 4.

**Membaca hasil pada data lab ini** (sama pada scikit-learn 1.6 dan 1.9; hanya angka *Gradient Boosting* yang sedikit bergeser): regresi logistik (±0,645) dan SVM tersetel dengan CV bersarang (±0,645) praktis seri — $\bar d \approx +0{,}0005$ dengan $2 \cdot SE \approx 0{,}008$, dan "juara" kalah di 3 dari 5 lipatan — sehingga kesimpulannya **tidak dapat disimpulkan**. Seandainya `pencarian.best_estimator_` yang dimasukkan, SVM akan tampil sebagai juara dengan 0,6513 (persis `best_score_`) — keunggulan semu hasil kebocoran seleksi. Regresi logistik unggul bermakna atas Naive Bayes, *Random Forest*, *Gradient Boosting*, dan *baseline* (searah di 5 dari 5 lipatan). **Tulis interpretasi:** mengapa model sederhana dapat menyamai SVM pada data ini? (Petunjuk: lihat bentuk `logit` di Langkah 1 dan parameter terbaik di Langkah 6.)

**Pemeriksaan otomatis.** Sel berikut harus lulus tanpa `AssertionError`; bila gagal, pesannya menunjukkan apa yang perlu diperiksa.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 4 dan 8
# =============================================
assert b_skala["bermakna"] and b_skala["d_bar"] > 0.01, (
    f"Penskalaan seharusnya menaikkan ROC-AUC SVM secara bermakna (Langkah 4); "
    f"sekarang d̄ = {b_skala['d_bar']:+.4f}, SE = {b_skala['SE']:.4f} — periksa buat_pipa(skala=...)")
assert isinstance(kandidat["SVM (RBF, disetel)"], GridSearchCV), (
    "SVM di tabel perbandingan harus berupa GridSearchCV yang BELUM dilatih (CV bersarang), "
    "bukan pencarian.best_estimator_")
assert np.allclose(skor_lipatan["Baseline (mayoritas)"], 0.5), (
    "Baseline mayoritas seharusnya ROC-AUC = 0,5 di setiap lipatan")
assert all(skor_lipatan[m].mean() > 0.55 for m in kandidat if m != "Baseline (mayoritas)"), (
    "Setiap model sungguhan seharusnya mengungguli baseline (ROC-AUC > 0,55) — periksa data Langkah 1")
d_uji = skor_lipatan[juara] - skor_lipatan[kedua]
assert np.isclose(b12["s_d"], pd.Series(d_uji).std()) and np.isclose(
    b12["SE"], pd.Series(d_uji).std() / np.sqrt(len(d_uji))), (
    "SE harus = s_d/√k dengan s_d simpangan baku SAMPEL (ddof=1) dari selisih per lipatan")
print("Pemeriksaan otomatis lulus.")
```

### LANGKAH 9: Validasi Silang Bersarang — Seberapa Optimistis `best_score_`?

```python
# =============================================
# LANGKAH 9: CV biasa vs CV bersarang pada lipatan luar yang SAMA (hanya data latih)
# =============================================
from sklearn.model_selection import cross_validate

# (a) Cara KELIRU: menilai best_estimator_ pada lipatan yang dipakai untuk memilihnya
skor_tak_bersarang = cross_val_score(pencarian.best_estimator_, X_train, y_train,
                                     cv=CV, scoring="roc_auc", n_jobs=-1)

# (b) CV bersarang: penyetelan diulang di dalam setiap lipatan luar (data uji TIDAK dipakai)
hasil_bersarang = cross_validate(svm_bersarang, X_train, y_train, cv=CV,
                                 scoring="roc_auc", n_jobs=-1, return_estimator=True)
skor_bersarang = hasil_bersarang["test_score"]

print(f"best_score_ (Langkah 6)            : {pencarian.best_score_:.4f}")
print(f"CV biasa atas best_estimator_      : {skor_tak_bersarang.mean():.4f}  <- sama dengan best_score_")
print(f"CV bersarang (bebas bias seleksi)  : {skor_bersarang.mean():.4f} "
      f"± {skor_bersarang.std(ddof=1):.4f}")

print("\nParameter terpilih di setiap lipatan luar:")
print(pd.DataFrame([
    {"Lipatan": i + 1, "C": est.best_params_["clf__C"],
     "gamma": est.best_params_["clf__gamma"],
     "Skor dalam": est.best_score_, "Skor luar": s}
    for i, (est, s) in enumerate(zip(hasil_bersarang["estimator"], skor_bersarang))
]).round(4).to_string(index=False))

# Lipatan luar sama -> selisih per lipatan berpasangan
b_opt = banding_berpasangan(skor_tak_bersarang, skor_bersarang)
print(f"\nOptimisme best_score_ (CV biasa − bersarang): d̄ = {b_opt['d_bar']:+.4f}, "
      f"SE = {b_opt['SE']:.4f}, searah {b_opt['searah']}/{b_opt['k']}")

# --- Kesimpulan dihitung dari hasil ---
if b_opt["bermakna"] and b_opt["d_bar"] > 0:
    print("Kesimpulan: best_score_ optimistis secara bermakna pada data ini; sebagai taksiran CV,")
    print("gunakan taksiran bersarang — bukan best_score_ (kinerja akhir tetap skor uji Langkah 7).")
elif b_opt["d_bar"] > 0:
    print("Kesimpulan: best_score_ sedikit lebih tinggi daripada taksiran bersarang, tetapi")
    print("selisihnya belum bermakna — bias seleksi kecil di sini (16 kombinasi, banyak yang")
    print("skornya hampir sama). Besarnya bias baru diketahui SETELAH CV bersarang dijalankan.")
else:
    print("Kesimpulan: pada data ini taksiran bersarang tidak lebih rendah daripada best_score_;")
    print("bias seleksi tidak terlihat. Besarnya bias baru diketahui SETELAH CV bersarang dijalankan.")
```

> CV bersarang menilai **prosedur penyetelan** (ruang pencarian + CV dalam), bukan satu pasangan `C`/`gamma`. Karena itu parameter terpilih boleh berbeda antarlipatan luar; bila sangat berbeda, penyetelannya tidak stabil. Model akhir tetap `pencarian.best_estimator_` (dilatih pada seluruh data latih) dan kinerja akhirnya tetap skor data uji di Langkah 7.

**Pemeriksaan otomatis.**

```python
# =============================================
# Pemeriksaan otomatis — Langkah 9
# =============================================
assert np.isclose(skor_tak_bersarang.mean(), pencarian.best_score_), (
    "Menilai best_estimator_ pada lipatan CV yang sama seharusnya MENGULANG best_score_ — "
    "inilah kebocoran seleksi; periksa apakah cv=CV dipakai di Langkah 6 dan 9")
assert np.allclose(skor_bersarang, skor_lipatan["SVM (RBF, disetel)"]), (
    "Skor CV bersarang Langkah 9 seharusnya sama dengan baris SVM di tabel Langkah 8 — "
    "periksa apakah keduanya memakai svm_bersarang dan CV yang sama")
assert len(hasil_bersarang["estimator"]) == CV.get_n_splits() and all(
    hasattr(est, "best_params_") for est in hasil_bersarang["estimator"]), (
    "Setiap lipatan luar harus menjalankan penyetelannya sendiri (GridSearchCV di dalam CV)")
print("Pemeriksaan otomatis lulus.")
```

---

## Tantangan Tambahan

### Tantangan 1 — *Grid* vs *Random Search*

Jalankan `RandomizedSearchCV` dengan `n_iter=16` (sama banyaknya dengan kombinasi *grid* 4×4) memakai `loguniform`. Bandingkan skor terbaik dan waktunya. Mana yang lebih efisien pada ruang besar, dan mengapa? Bila ingin membandingkan keduanya secara adil, nilai keduanya dengan CV bersarang pada lipatan luar `CV` yang sama dan gunakan `banding_berpasangan`.

### Tantangan 2 — Skala Data dan SVM

Kurangi data menjadi 500, 1.000, 2.000, dan 3.000 baris. Catat waktu pelatihan SVM pada masing-masing. Buat grafik waktu terhadap jumlah baris. Bagaimana bentuk kurvanya, dan apa implikasinya untuk data besar?

### Tantangan 3 — Anggaran Penyetelan yang Tidak Setara

Setel *Random Forest* dengan 4 kombinasi dan SVM dengan 64 kombinasi, lalu bandingkan. Apakah perbandingan itu adil? Jelaskan mengapa anggaran penyetelan yang setara merupakan salah satu syarat perbandingan yang sah.

### Tantangan 4 — Uji Formal: *Corrected Resampled t-test*

Aturan $|\bar d| > 2 \cdot SE$ mengabaikan kenyataan bahwa data latih antarlipatan tumpang-tindih. Nadeau & Bengio (2003) mengoreksi varians selisih menjadi $\left(\frac{1}{k} + \frac{n_\text{uji}}{n_\text{latih}}\right) s_d^2$, sehingga statistiknya $t = \bar d \,/\, \sqrt{\left(\frac{1}{k} + \frac{n_\text{uji}}{n_\text{latih}}\right) s_d^2}$ dengan derajat bebas $k-1$ (pada *k-fold*, $n_\text{uji}/n_\text{latih} = 1/(k-1)$). Hitung $t$ dan nilai-$p$-nya (`scipy.stats.t.sf`) untuk perbandingan peringkat 1 vs 2 di Langkah 8. Apakah kesimpulannya sama dengan aturan praktis? Mana yang lebih konservatif, dan mengapa?

---

## Checklist Penyelesaian

- [ ] SVM dijalankan dengan tiga *kernel* di dalam `Pipeline` berpenskalaan
- [ ] Dampak tidak adanya penskalaan pada SVM **ditunjukkan dengan angka** (selisih berpasangan per lipatan)
- [ ] Naive Bayes dijalankan sebagai pembanding cepat
- [ ] Asumsi kebebasan diperiksa melalui korelasi antarfitur
- [ ] `GridSearchCV` dijalankan **hanya pada data latih**
- [ ] Diperiksa apakah optimum berada di tepi ruang pencarian
- [ ] Perbedaan `best_score_` dan skor uji dijelaskan
- [ ] Lima model dibandingkan dengan **lipatan yang sama**, dan SVM tersetel dinilai dengan **CV bersarang** (bukan `best_estimator_`)
- [ ] **Kesimpulan memakai selisih berpasangan per lipatan** ($\bar d$, $s_d$ dengan `ddof=1`, $SE = s_d/\sqrt{k}$), bukan hanya rerata
- [ ] Validasi silang bersarang dijalankan **pada data latih** dan dibandingkan dengan `best_score_`
- [ ] Seluruh sel **Pemeriksaan otomatis** lulus
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 10](../03-modules/week-10-svm-naive-bayes-pemilihan-model.md)
2. [Bab 9 buku ajar](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md)
3. Cawley, G. C., & Talbot, N. L. C. (2010). On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation. *Journal of Machine Learning Research*, 11, 2079–2107.
4. Nadeau, C., & Bengio, Y. (2003). Inference for the Generalization Error. *Machine Learning*, 52(3), 239–281.
5. Dokumentasi scikit-learn — *Tuning the hyper-parameters of an estimator* dan *Nested versus non-nested cross-validation*. <https://scikit-learn.org/stable/modules/grid_search.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
