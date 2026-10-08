# Lab 12: PCA dan Visualisasi Kinerja Model

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 12 |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-11 |
| Durasi | 100 menit |
| Prasyarat | Lab 11 selesai |
| Bobot | 2,0% (Observasi, Sub-CPMK102-1) |
| Diuji pada | scikit-learn 1.6 dan 1.9, pandas 2.2 dan 3.0 (Oktober 2026) |

---

## Tujuan Praktikum

1. Menerapkan PCA dan menafsirkan *explained variance* serta *loading*.
2. Membuat dan membaca kurva pembelajaran untuk mendiagnosis kondisi model.
3. Membuat dan membaca kurva validasi untuk menentukan hiperparameter.
4. Menyusun lima grafik diagnostik lengkap dan menuliskan diagnosisnya.

---

## Persiapan

1. Buat notebook baru bernama `NIM_Nama_Lab12.ipynb`.
2. Jalankan **sel pembuka baku** di [Lampiran D](../06-buku-ajar/lampiran.md#lampiran-d-sel-pembuka-baku) — mengimpor pustaka, mencatat versi, dan menetapkan `RANDOM_STATE = 42`. Seluruh langkah di bawah mengandaikan sel itu sudah dijalankan.
3. **Data:** seluruh data lab ini adalah **data sintetis (simulasi)** yang dibangkitkan dengan `make_classification` — tabel klasifikasi biner generik dengan 24 fitur anonim (`fitur_00` … `fitur_23`); **bukan data resmi BPS/lembaga** dan tidak meniru kumpulan data nyata mana pun. Data generik dipilih karena strukturnya **diketahui pasti** (8 fitur informatif, 6 redundan, 2 duplikat, 8 derau), sehingga hasil PCA dan diagnosis kurva dapat dicocokkan dengan "kebenaran"-nya.

---

## Langkah-langkah

### LANGKAH 1: Data Berdimensi Sedang

> **Data sintetis (simulasi)** dari `make_classification`; bukan data resmi BPS/lembaga. Kolom redundan dibentuk sebagai kombinasi linear kolom informatif dan kolom duplikat adalah salinan — keduanya tidak menambah informasi baru.

```python
# =============================================
# LANGKAH 1: Data SINTETIS (make_classification — bukan data resmi BPS/lembaga)
# =============================================
import numpy as np, pandas as pd
from sklearn.datasets import make_classification

X_arr, y_arr = make_classification(
    n_samples=2500, n_features=24, n_informative=8, n_redundant=6,
    n_repeated=2, n_classes=2, weights=[0.75, 0.25],
    flip_y=0.03, class_sep=1.0, random_state=RANDOM_STATE)

X = pd.DataFrame(X_arr, columns=[f"fitur_{i:02d}" for i in range(24)])
y = pd.Series(y_arr, name="target")

print("Dimensi:", X.shape)
print("Proporsi positif:", round(y.mean(), 3))
print("\nCatatan: 8 fitur informatif, 6 redundan, 2 duplikat, 8 derau.")
```

### LANGKAH 2: PCA

```python
# =============================================
# LANGKAH 2: PCA — penskalaan WAJIB
# =============================================
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE)

alur_pca = Pipeline([("skala", StandardScaler()),
                     ("pca", PCA(random_state=RANDOM_STATE))]).fit(X_train)
pca = alur_pca.named_steps["pca"]

rasio = pca.explained_variance_ratio_
kumulatif = np.cumsum(rasio)

tabel = pd.DataFrame({
    "PC": [f"PC{i+1}" for i in range(len(rasio))],
    "Varians": rasio.round(4),
    "Kumulatif": kumulatif.round(4),
})
print(tabel.head(15).to_string(index=False))

for ambang in [0.80, 0.90, 0.95, 0.99]:
    k = int(np.searchsorted(kumulatif, ambang) + 1)
    print(f"Komponen untuk {ambang:.0%} varians: {k} dari {X.shape[1]}")

print(f"\n16 komponen pertama menjelaskan {kumulatif[15]:.4%} varians; "
      f"komponen 17–24 hanya {rasio[16:].sum():.1e}")
```

**Pemeriksaan otomatis.** Sel berikut harus lulus tanpa `AssertionError`; bila gagal, pesannya menunjukkan apa yang perlu diperiksa.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 2 (varians PCA)
# =============================================
# 24 kolom, tetapi hanya 8 informatif + 8 derau yang "bebas"; 6 kolom redundan
# (kombinasi linear) dan 2 duplikat tidak menambah dimensi -> sisanya bervarians nol.
assert kumulatif[15] > 0.999, (
    f"16 komponen seharusnya menjelaskan ≈100% varians (sekarang {kumulatif[15]:.4f}) "
    "— periksa parameter make_classification dan StandardScaler")
assert rasio[16:].sum() < 1e-6, (
    "Komponen 17–24 seharusnya bervarians ≈0 — kolom redundan/duplikat tidak membawa informasi baru")
print("Pemeriksaan otomatis lulus.")
```

> Pada data ini (diuji pada scikit-learn 1.6 dan 1.9), 80% varians dicapai dengan 11 komponen, 95% dengan 15, dan 99% dengan 16 komponen — sama dengan jumlah kolom yang benar-benar bebas. Kolom redundan dan duplikat **menggelembungkan jumlah kolom tanpa menambah informasi**, dan PCA mengungkapnya.

### LANGKAH 3: *Scree Plot* dan *Loading*

```python
# =============================================
# LANGKAH 3: Scree plot dan loading
# =============================================
fig, ax = plt.subplots(1, 2, figsize=(14, 4.5))

ax[0].bar(range(1, len(rasio)+1), rasio, alpha=0.7, label="Per komponen")
ax[0].plot(range(1, len(rasio)+1), kumulatif, "ro-", label="Kumulatif")
ax[0].axhline(0.95, color="gray", ls="--", lw=1, label="95%")
ax[0].set_xlabel("Komponen utama"); ax[0].set_ylabel("Proporsi varians")
ax[0].set_title(f"Scree plot (n={len(X_train)})"); ax[0].legend()

loading = pd.DataFrame(pca.components_[:3].T,
                       columns=["PC1", "PC2", "PC3"], index=X.columns)
im = ax[1].imshow(loading.values, cmap="RdBu_r", aspect="auto", vmin=-0.5, vmax=0.5)
ax[1].set_xticks(range(3)); ax[1].set_xticklabels(["PC1","PC2","PC3"])
ax[1].set_yticks(range(len(X.columns)))
ax[1].set_yticklabels(X.columns, fontsize=7)
ax[1].set_title("Loading tiga komponen pertama")
plt.colorbar(im, ax=ax[1])
plt.tight_layout(); plt.show()

print("Lima fitur dengan loading |PC1| terbesar:")
print(loading["PC1"].abs().nlargest(5).round(3).to_string())
```

> **Ingat:** setelah PCA tidak ada lagi kolom bernama `fitur_03`. Yang ada adalah PC1 — campuran seluruh kolom. *Loading* adalah satu-satunya jalan memberinya makna.

### LANGKAH 4: PCA sebagai Prapemrosesan Model

```python
# =============================================
# LANGKAH 4: Apakah PCA membantu kinerja?
# =============================================
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold

# Satu objek lipatan untuk SEMUA konfigurasi: setiap konfigurasi dinilai pada lipatan yang sama
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

TANPA = "Tanpa PCA (24)"
baris, skor_lipatan = [], {}
for n_komp in [2, 5, 10, 15, 20, None]:
    langkah = [("skala", StandardScaler())]
    if n_komp is not None:
        langkah.append(("pca", PCA(n_components=n_komp, random_state=RANDOM_STATE)))
    langkah.append(("clf", LogisticRegression(max_iter=1000,
                                              class_weight="balanced",
                                              random_state=RANDOM_STATE)))
    skor = cross_val_score(Pipeline(langkah), X_train, y_train,
                           cv=CV, scoring="roc_auc", n_jobs=-1)   # CV yang SAMA
    label = n_komp if n_komp else TANPA
    skor_lipatan[label] = skor                 # disimpan untuk perbandingan berpasangan
    baris.append({"Komponen": label, "ROC-AUC": skor.mean(),
                  "Simpangan": skor.std(ddof=1)})

tabel_pca = pd.DataFrame(baris)
print(tabel_pca.round(4).to_string(index=False))

# Setiap konfigurasi PCA dibandingkan dengan "tanpa PCA" secara BERPASANGAN per lipatan
banding = []
for label in tabel_pca["Komponen"].iloc[:-1]:
    b = banding_berpasangan(skor_lipatan[label], skor_lipatan[TANPA])
    banding.append({"PCA (komponen)": label, "d̄ (PCA − tanpa)": b["d_bar"],
                    "s_d": b["s_d"], "SE": b["SE"],
                    "Searah": f"{b['searah']}/{b['k']}",
                    "Bermakna?": "ya" if b["bermakna"] else "tidak"})
print("\nSelisih berpasangan per lipatan: konfigurasi PCA dikurangi tanpa PCA")
print(pd.DataFrame(banding).round(4).to_string(index=False))

# Kesimpulan DIHITUNG dari hasil — konfigurasi PCA terbaik vs tanpa PCA
dengan_pca = tabel_pca.iloc[:-1]
terbaik = dengan_pca.loc[dengan_pca["ROC-AUC"].idxmax(), "Komponen"]
b_pca = banding_berpasangan(skor_lipatan[terbaik], skor_lipatan[TANPA])
print(f"\nPCA {terbaik} komponen − tanpa PCA, per lipatan: {np.round(b_pca['d'], 4)}")
print(f"  d̄ = {b_pca['d_bar']:+.4f} | s_d = {b_pca['s_d']:.4f} | SE = {b_pca['SE']:.4f} "
      f"| batas 2·SE = {2 * b_pca['SE']:.4f} | searah {b_pca['searah']}/{b_pca['k']}")
if b_pca["bermakna"] and b_pca["d_bar"] > 0:
    print(f"Kesimpulan: PCA {terbaik} komponen MENINGKATKAN ROC-AUC secara bermakna "
          f"(|d̄| > 2·SE dan searah di sebagian besar lipatan).")
elif b_pca["bermakna"]:
    print(f"Kesimpulan: bahkan konfigurasi PCA terbaik ({terbaik} komponen) MENURUNKAN "
          f"ROC-AUC secara bermakna — PCA tidak membantu di sini.")
else:
    print(f"Kesimpulan: PCA tidak meningkatkan ROC-AUC secara bermakna — konfigurasi terbaik "
          f"({terbaik} komponen) = {skor_lipatan[terbaik].mean():.4f} vs tanpa PCA = "
          f"{skor_lipatan[TANPA].mean():.4f}; selisihnya belum lolos aturan |d̄| > 2·SE "
          f"dan searah di sebagian besar lipatan.")
```

> Karena semua konfigurasi dinilai dengan objek `CV` yang **sama**, skornya berpasangan per lipatan; keputusan "PCA meningkatkan atau tidak" diambil dari selisih per lipatan ($\bar d$, $s_d$ dengan `ddof=1`, $SE = s_d/\sqrt{k}$), bukan dengan membandingkan selisih rerata pada simpangan satu model. Aturannya dijelaskan di [Bab 9 §9.4.2](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md#942-membaca-hasil-perbandingan) dan [Lampiran A.10](../06-buku-ajar/lampiran.md#a10-perbandingan-model). Aturan ini hanya penyaring kasar: skor antarlipatan tidak benar-benar saling bebas (data latihnya tumpang-tindih), sehingga $SE$ cenderung terlalu kecil. Untuk analisis formal, gunakan *corrected resampled t-test* (Nadeau & Bengio, 2003). Seluruh simpangan baku skor lipatan di lab ini memakai **`ddof=1`**, sama dengan `pd.Series.std()`.

**Pemeriksaan otomatis.** Sel berikut harus lulus tanpa `AssertionError`; bila gagal, pesannya menunjukkan apa yang perlu diperiksa.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 4 (PCA vs tanpa PCA, berpasangan)
# =============================================
assert not (b_pca["bermakna"] and b_pca["d_bar"] > 0), (
    "Pada data ini PCA seharusnya TIDAK meningkatkan ROC-AUC secara bermakna — PCA hanya "
    "memutar dan memangkas ruang fitur, tidak menambah informasi; periksa apakah PCA "
    "di-fit di luar Pipeline (kebocoran)")
b_dua = banding_berpasangan(skor_lipatan[2], skor_lipatan[TANPA])
assert b_dua["bermakna"] and b_dua["d_bar"] < 0, (
    f"PCA 2 komponen seharusnya jauh lebih buruk daripada tanpa PCA (sekarang d̄ = "
    f"{b_dua['d_bar']:+.4f}) — komponen bervarians terbesar belum tentu paling berguna "
    f"untuk memprediksi target; periksa n_components")
assert np.isclose(b_pca["SE"], pd.Series(b_pca["d"]).std() / np.sqrt(b_pca["k"])), (
    "SE harus = s_d/√k dengan s_d simpangan baku SAMPEL (ddof=1) dari selisih per lipatan")
print("Pemeriksaan otomatis lulus.")
```

> **Pada data ini** (hasil sama pada scikit-learn 1.6 dan 1.9): konfigurasi PCA terbaik adalah 20 komponen (ROC-AUC ≈ 0,783) — praktis identik dengan tanpa PCA (≈ 0,783; selisihnya nol di 4 dari 5 lipatan), karena 20 komponen sudah memuat seluruh 16 dimensi bebas. Makin sedikit komponen, makin buruk: 15 komponen $\bar d \approx -0{,}008$ (belum bermakna; $2 \cdot SE \approx 0{,}010$), 10 komponen $\bar d \approx -0{,}024$ dan 5 komponen $\bar d \approx -0{,}058$ (keduanya lebih buruk secara bermakna, searah di 5 dari 5 lipatan).

**Tulis kesimpulan:** apakah PCA meningkatkan kinerja? Apa yang **hilang** dengan memakainya? Pada data ini 2 komponen (≈35% varians) hanya memberi ROC-AUC ≈ 0,55 — apa artinya bagi anggapan bahwa komponen dengan varians terbesar pasti paling berguna untuk memprediksi target?

### LANGKAH 5: Kurva Pembelajaran

```python
# =============================================
# LANGKAH 5: Kurva pembelajaran — alat diagnosis utama
# =============================================
from sklearn.model_selection import learning_curve
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

def gambar_kurva_belajar(model, nama, ax):
    ukuran, s_latih, s_val = learning_curve(
        model, X_train, y_train, train_sizes=np.linspace(0.1, 1.0, 10),
        cv=CV, scoring="roc_auc", n_jobs=-1, random_state=RANDOM_STATE)
    ax.plot(ukuran, s_latih.mean(axis=1), "o-", label="Latih")
    ax.plot(ukuran, s_val.mean(axis=1), "s-", label="Validasi")
    sd_val = s_val.std(axis=1, ddof=1)        # simpangan baku antarlipatan (ddof=1)
    ax.fill_between(ukuran, s_val.mean(axis=1)-sd_val,
                    s_val.mean(axis=1)+sd_val, alpha=0.15)
    ax.set_xlabel("Jumlah data latih"); ax.set_ylabel("ROC-AUC")
    ax.set_title(nama); ax.legend(); ax.set_ylim(0.5, 1.02)
    return s_latih.mean(axis=1), s_val.mean(axis=1)   # rerata per ukuran data latih

def diagnosis_kurva(latih, val):
    """Menerapkan tabel diagnosis di bawah dengan ambang praktis lab ini (ROC-AUC)."""
    selisih = latih[-1] - val[-1]
    kenaikan = val[-1] - val[-4]   # kenaikan validasi dari 70% ke 100% data latih
    if latih[-1] < 0.75 and selisih < 0.05:
        return "Underfit — tambah kompleksitas"
    if selisih >= 0.10:
        return "Overfit — regularisasi; tambah data"
    if kenaikan >= 0.02:
        return "Kurang data — menambah data akan membantu"
    return "Pas — menambah data tidak banyak membantu"

model_uji = {
    "UNDERFIT: pohon kedalaman 1": Pipeline([
        ("skala", StandardScaler()),
        ("clf", DecisionTreeClassifier(max_depth=1, random_state=RANDOM_STATE))]),
    "OVERFIT: pohon tanpa batas": Pipeline([
        ("skala", StandardScaler()),
        ("clf", DecisionTreeClassifier(random_state=RANDOM_STATE))]),
    "PAS: Random Forest": Pipeline([
        ("skala", StandardScaler()),
        ("clf", RandomForestClassifier(n_estimators=200, min_samples_leaf=5,
                                       random_state=RANDOM_STATE, n_jobs=-1))]),
}

fig, ax = plt.subplots(1, 3, figsize=(16, 4.5))
diagnosis = []
for (nama, m), a in zip(model_uji.items(), ax):
    latih, val = gambar_kurva_belajar(m, nama, a)
    diagnosis.append({"Model": nama, "Latih akhir": latih[-1],
                      "Validasi akhir": val[-1],
                      "Selisih": latih[-1] - val[-1],
                      "Kenaikan val. 70→100%": val[-1] - val[-4],
                      "Diagnosis": diagnosis_kurva(latih, val)})
plt.tight_layout(); plt.show()

tabel_diag = pd.DataFrame(diagnosis)
print(tabel_diag.round(4).to_string(index=False))
```

**Tulis diagnosis untuk masing-masing:**

| Pola | Diagnosis | Tindakan |
|------|-----------|----------|
| Keduanya rendah, berdekatan, mendatar | *Underfit* | Tambah kompleksitas |
| Latih tinggi, validasi rendah, selisih menetap | *Overfit* | Tambah data; regularisasi |
| Selisih mengecil, validasi belum mendatar | Kurang data | **Menambah data akan membantu** |
| Keduanya tinggi, selisih kecil, mendatar | Pas | Menambah data tidak membantu |

Kolom `Diagnosis` menerapkan tabel ini dengan **ambang praktis** lab ini: *underfit* bila ROC-AUC latih < 0,75 dan selisih < 0,05; *overfit* bila selisih ≥ 0,10; kurang data bila validasi masih naik ≥ 0,02 dari 70% ke 100% data latih; selain itu pas. Ambang ini hanya pegangan — diagnosis tertulis Anda tetap harus membaca **bentuk** kurva, bukan sekadar angka akhirnya.

**Pemeriksaan otomatis.** Diagnosis yang dihitung harus cocok dengan dugaan pada nama model.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 5 (diagnosis kurva pembelajaran)
# =============================================
diag = dict(zip(tabel_diag["Model"], tabel_diag["Diagnosis"]))
assert diag["UNDERFIT: pohon kedalaman 1"].startswith("Underfit"), (
    "Pohon kedalaman 1 seharusnya underfit: latih dan validasi sama-sama rendah dan berdekatan")
assert diag["OVERFIT: pohon tanpa batas"].startswith("Overfit"), (
    "Pohon tanpa batas seharusnya overfit: latih ≈1,0 dengan selisih besar terhadap validasi")
assert diag["PAS: Random Forest"].startswith("Pas"), (
    "Random Forest seharusnya pas: validasi tinggi, selisih kecil, kurva sudah melandai")
print("Pemeriksaan otomatis lulus.")
```

> Pada data ini (diuji pada scikit-learn 1.6 dan 1.9): pohon kedalaman 1 ≈ 0,60 (latih) vs ≈ 0,60 (validasi); pohon tanpa batas 1,00 vs ≈ 0,79 — selisih masih ≈ 0,21, menyempit perlahan dari ≈ 0,34 pada 10% data latih tetapi tetap besar; *Random Forest* ≈ 1,00 vs ≈ 0,95 — selisih ≈ 0,05 dan validasinya hanya naik < 0,01 pada 30% data latih terakhir. Perhatikan bahwa validasi pohon tanpa batas **masih naik** (≈ +0,02 pada 30% data latih terakhir): menambah data membantu sedikit, tetapi tidak menutup selisihnya. Kurva ini sebenarnya juga menunjukkan tanda **kurang data** (selisih mengecil, validasi belum mendatar); `diagnosis_kurva` tetap memberinya label *Overfit* karena aturan selisih ≥ 0,10 diperiksa lebih dahulu — selisih yang besar mendominasi diagnosis. Dalam diagnosis tertulis Anda, sebutkan kedua tanda itu.

### LANGKAH 6: Kurva Validasi

```python
# =============================================
# LANGKAH 6: Kurva validasi — satu hiperparameter
# =============================================
from sklearn.model_selection import validation_curve

rentang = [1, 2, 3, 5, 8, 12, 20, 30, None]
rentang_num = [r if r is not None else 50 for r in rentang]

pipa = Pipeline([("skala", StandardScaler()),
                 ("clf", DecisionTreeClassifier(random_state=RANDOM_STATE))])

s_latih, s_val = validation_curve(
    pipa, X_train, y_train, param_name="clf__max_depth",
    param_range=rentang, cv=CV, scoring="roc_auc", n_jobs=-1)

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(rentang_num, s_latih.mean(axis=1), "o-", label="Latih")
ax.plot(rentang_num, s_val.mean(axis=1), "s-", label="Validasi")
sd_val = s_val.std(axis=1, ddof=1)            # simpangan baku antarlipatan (ddof=1)
ax.fill_between(rentang_num, s_val.mean(axis=1)-sd_val,
                s_val.mean(axis=1)+sd_val, alpha=0.15)
optimum = rentang_num[int(np.argmax(s_val.mean(axis=1)))]
ax.axvline(optimum, color="red", ls="--", label=f"Optimum: max_depth={optimum}")
ax.set_xlabel("max_depth"); ax.set_ylabel("ROC-AUC")
ax.set_title("Kurva validasi — kedalaman pohon")
ax.legend(); plt.tight_layout(); plt.show()

print(f"max_depth optimum menurut skor VALIDASI: {optimum}")
```

### LANGKAH 7: Lima Grafik Diagnostik

Sel ini menghasilkan **enam panel untuk lima jenis grafik wajib** ([Modul Minggu 12 §12.5](../03-modules/week-12-reduksi-dimensi-dan-visualisasi.md#125-rangkaian-visualisasi-diagnostik)): kurva ROC dan *Precision-Recall* sama-sama jenis ke-2, dan PR wajib di sini karena kelas positif hanya ±26%.

```python
# =============================================
# LANGKAH 7: Rangkaian diagnostik lengkap
# =============================================
from sklearn.metrics import (ConfusionMatrixDisplay, RocCurveDisplay,
                             PrecisionRecallDisplay)
from sklearn.inspection import permutation_importance

model_final = Pipeline([
    ("skala", StandardScaler()),
    ("clf", RandomForestClassifier(n_estimators=300, min_samples_leaf=5,
                                   class_weight="balanced",
                                   random_state=RANDOM_STATE, n_jobs=-1)),
]).fit(X_train, y_train)

fig, ax = plt.subplots(2, 3, figsize=(17, 9))

# (1) Matriks konfusi ternormalisasi
ConfusionMatrixDisplay.from_estimator(model_final, X_test, y_test,
                                      normalize="true", cmap="Blues", ax=ax[0,0])
ax[0,0].set_title("1. Matriks konfusi (ternormalisasi per kelas aktual)")

# (2a) Kurva ROC
RocCurveDisplay.from_estimator(model_final, X_test, y_test, ax=ax[0,1])
ax[0,1].plot([0,1],[0,1],"k--",lw=1)
ax[0,1].set_title("2a. Kurva ROC")

# (2b) Kurva Precision-Recall — pasangan ROC untuk kelas tak seimbang
PrecisionRecallDisplay.from_estimator(model_final, X_test, y_test, ax=ax[0,2])
ax[0,2].axhline(y_test.mean(), color="k", ls="--", lw=1)
ax[0,2].set_title(f"2b. Precision-Recall (baseline={y_test.mean():.3f})")

# (3) Kurva pembelajaran
gambar_kurva_belajar(model_final, "3. Kurva pembelajaran", ax[1,0])

# (4) Kepentingan fitur (permutasi)
perm = permutation_importance(model_final, X_test, y_test, n_repeats=10,
                              scoring="roc_auc", random_state=RANDOM_STATE, n_jobs=-1)
kepent = pd.Series(perm.importances_mean, index=X.columns).nlargest(10)
ax[1,1].barh(kepent.index[::-1], kepent.values[::-1])
ax[1,1].set_xlabel("Penurunan ROC-AUC saat dipermutasi")
ax[1,1].set_title("4. Kepentingan fitur (permutasi)")

# (5) Distribusi kesalahan
pred = model_final.predict(X_test)
prob = model_final.predict_proba(X_test)[:, 1]
ax[1,2].hist(prob[pred == y_test], bins=30, alpha=0.6, label="Benar")
ax[1,2].hist(prob[pred != y_test], bins=30, alpha=0.6, label="Salah")
ax[1,2].set_xlabel("Probabilitas prediksi"); ax[1,2].set_ylabel("Frekuensi")
ax[1,2].set_title(f"5. Distribusi kesalahan (n uji={len(y_test)})"); ax[1,2].legend()

plt.tight_layout(); plt.show()
```

### LANGKAH 8: Analisis Kesalahan

```python
# =============================================
# LANGKAH 8: Adakah POLA pada kasus yang salah?
# =============================================
salah = pred != y_test
print(f"Jumlah salah: {salah.sum()} dari {len(y_test)} "
      f"({salah.mean():.1%})")

perbandingan = pd.DataFrame({
    "Rata-rata (salah)": X_test[salah].mean(),
    "Rata-rata (benar)": X_test[~salah].mean(),
})
perbandingan["Selisih baku"] = ((perbandingan["Rata-rata (salah)"]
                                 - perbandingan["Rata-rata (benar)"])
                                / X_test.std())
print("\nLima fitur dengan selisih terbesar antara kasus salah dan benar:")
print(perbandingan.reindex(perbandingan["Selisih baku"].abs()
                           .nlargest(5).index).round(3).to_string())

print("\nKesalahan per kelas aktual:")
print(pd.crosstab(y_test, salah, rownames=["Aktual"],
                  colnames=["Salah"], normalize="index").round(3).to_string())
```

**Tulis temuan:** adakah pola pada kasus yang salah? Apakah kesalahan terpusat pada satu kelas atau satu rentang nilai? Temuan semacam ini mengarah langsung pada bahasan *fairness* Minggu 14.

---

## Tantangan Tambahan

### Tantangan 1 — t-SNE dan Keterbatasannya

Terapkan t-SNE dengan `perplexity` 5, 30, dan 50. Bandingkan ketiga hasilnya. Apakah klaster yang terlihat sama? Tuliskan tiga kekeliruan membaca t-SNE dan tunjukkan buktinya dari hasil Anda.

### Tantangan 2 — Kurva Kalibrasi

Gunakan `CalibrationDisplay.from_estimator` untuk memeriksa apakah probabilitas keluaran model terkalibrasi. Bandingkan *Random Forest* dengan regresi logistik. Mana yang lebih terkalibrasi, dan mengapa itu penting bila keluarannya dipakai untuk menentukan ambang?

### Tantangan 3 — Visualisasi yang Menyesatkan

Buat dua versi grafik perbandingan model: satu dengan sumbu-y mulai dari 0, satu dengan sumbu-y dipotong pada rentang sempit. Tunjukkan berdampingan dan jelaskan bagaimana versi kedua dapat menyesatkan pembaca.

---

## Checklist Penyelesaian

- [ ] PCA diterapkan dengan penskalaan lebih dahulu
- [ ] *Explained variance* dan varians kumulatif dilaporkan
- [ ] *Scree plot* dan tabel *loading* ditampilkan dan ditafsirkan
- [ ] Pengaruh jumlah komponen terhadap kinerja diuji
- [ ] **Keputusan "PCA membantu atau tidak" memakai selisih berpasangan per lipatan** ($\bar d$, $s_d$ dengan `ddof=1`, $SE = s_d/\sqrt{k}$) pada objek CV yang sama, bukan hanya rerata
- [ ] **Apa yang hilang dengan memakai PCA** dijelaskan
- [ ] Tiga kurva pembelajaran (*underfit*, *overfit*, pas) dibuat
- [ ] **Diagnosis tertulis** untuk tiap kurva
- [ ] Kurva validasi dibuat dan optimum dibaca dari skor **validasi**
- [ ] **Lima grafik diagnostik** lengkap
- [ ] **Analisis kesalahan** dengan pencarian pola
- [ ] Seluruh grafik memiliki judul, label sumbu, dan n
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 12](../03-modules/week-12-reduksi-dimensi-dan-visualisasi.md)
2. [Bab 11 buku ajar](../06-buku-ajar/bab-11-reduksi-dimensi-dan-visualisasi.md)
3. Wattenberg, M., Viégas, F., & Johnson, I. (2016). How to Use t-SNE Effectively. *Distill*.
4. Dokumentasi scikit-learn — *Validation curves*. <https://scikit-learn.org/stable/modules/learning_curve.html>
5. Nadeau, C., & Bengio, Y. (2003). Inference for the Generalization Error. *Machine Learning*, 52(3), 239–281.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
