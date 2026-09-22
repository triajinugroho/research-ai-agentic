# LAMPIRAN

**Tri Aji Nugroho, S.T., M.T.**
Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (IF52510031) — Program Studi Informatika, Universitas Al Azhar Indonesia

---

## Daftar Lampiran

| Lampiran | Judul | Kegunaan |
|----------|-------|----------|
| [A](#lampiran-a-formularium) | Formularium | **Dibawa saat UTS dan UAS** |
| [B](#lampiran-b-pohon-keputusan-pemilihan-model) | Pohon Keputusan Pemilihan Model | Rujukan cepat |
| [C](#lampiran-c-rujukan-scikit-learn) | Rujukan `scikit-learn` | Praktikum dan proyek |
| [D](#lampiran-d-sel-pembuka-baku) | Sel Pembuka Baku dan Templat Notebook | Setiap notebook |
| [E](#lampiran-e-daftar-periksa) | Daftar Periksa | Sebelum setiap pengumpulan |
| [F](#lampiran-f-glosarium) | Glosarium | Padanan Indonesia–Inggris |
| [G](#lampiran-g-kesalahan-tafsir-yang-sering-terjadi) | Kesalahan Tafsir yang Sering Terjadi | Sebelum menulis laporan |
| [H](#lampiran-h-templat-model-card) | Templat *Model Card* | Laporan proyek |
| [I](#lampiran-i-peta-bab-modul-praktikum) | Peta Bab – Modul – Praktikum | Navigasi materi |

> **Ketentuan ujian:** Lampiran A **boleh dibawa** saat UTS dan UAS dalam bentuk cetak. Lampiran lain tidak. Alat bantu AI **tidak diperkenankan** dalam bentuk apa pun selama ujian.

---

## Lampiran A: Formularium

### A.1 Metrik Klasifikasi

Dari matriks konfusi (TP, TN, FP, FN):

| Metrik | Rumus |
|--------|-------|
| Akurasi | $\dfrac{TP+TN}{TP+TN+FP+FN}$ |
| Precision | $\dfrac{TP}{TP+FP}$ |
| Recall (sensitivitas, TPR) | $\dfrac{TP}{TP+FN}$ |
| Spesifisitas (TNR) | $\dfrac{TN}{TN+FP}$ |
| FPR | $\dfrac{FP}{FP+TN}$ |
| F1 | $2\cdot\dfrac{P\cdot R}{P+R}$ |
| F-beta | $(1+\beta^2)\cdot\dfrac{P\cdot R}{\beta^2 P+R}$ |
| Balanced accuracy | $\dfrac{\text{Recall}+\text{Spesifisitas}}{2}$ |

### A.2 Metrik Regresi

| Metrik | Rumus |
|--------|-------|
| MAE | $\dfrac{1}{n}\sum\lvert y_i-\hat{y}_i\rvert$ |
| MSE | $\dfrac{1}{n}\sum(y_i-\hat{y}_i)^2$ |
| RMSE | $\sqrt{\text{MSE}}$ |
| R² | $1-\dfrac{\sum(y_i-\hat{y}_i)^2}{\sum(y_i-\bar{y})^2}$ |
| MAPE | $\dfrac{100\%}{n}\sum\left\lvert\dfrac{y_i-\hat{y}_i}{y_i}\right\rvert$ |
| RMSLE | $\sqrt{\dfrac{1}{n}\sum(\log(1+y_i)-\log(1+\hat{y}_i))^2}$ |

### A.3 Pohon Keputusan

| Besaran | Rumus |
|---------|-------|
| Entropy | $H(S)=-\sum_i p_i\log_2 p_i$ |
| Gini impurity | $G(S)=1-\sum_i p_i^2$ |
| Information gain | $IG(S,A)=H(S)-\sum_v \dfrac{\lvert S_v\rvert}{\lvert S\rvert}H(S_v)$ |
| Gain ratio | $\dfrac{IG(S,A)}{-\sum_v \frac{\lvert S_v\rvert}{\lvert S\rvert}\log_2\frac{\lvert S_v\rvert}{\lvert S\rvert}}$ |

**Nilai $\log_2$ yang sering dipakai:**

| $p$ | $\log_2 p$ | $-p\log_2 p$ |
|-----|-----------|--------------|
| 0,1 | −3,322 | 0,332 |
| 0,2 | −2,322 | 0,464 |
| 0,25 | −2,000 | 0,500 |
| 0,3 | −1,737 | 0,521 |
| 0,4 | −1,322 | 0,529 |
| 0,5 | −1,000 | 0,500 |
| 0,6 | −0,737 | 0,442 |
| 0,7 | −0,515 | 0,360 |
| 0,75 | −0,415 | 0,311 |
| 0,8 | −0,322 | 0,258 |
| 0,9 | −0,152 | 0,137 |

### A.4 Regresi dan Regularisasi

| Besaran | Rumus |
|---------|-------|
| Model linear | $\hat{y}=\beta_0+\sum_j \beta_j x_j$ |
| Kuadrat terkecil | $\min \sum(y_i-\hat{y}_i)^2$ |
| Ridge (L2) | $\min\left[\sum(y_i-\hat{y}_i)^2+\alpha\sum\beta_j^2\right]$ |
| Lasso (L1) | $\min\left[\sum(y_i-\hat{y}_i)^2+\alpha\sum\lvert\beta_j\rvert\right]$ |
| Elastic Net | $\min\left[\sum(y_i-\hat{y}_i)^2+\alpha\left(\rho\sum\lvert\beta_j\rvert+\frac{1-\rho}{2}\sum\beta_j^2\right)\right]$ |

### A.5 Klasifikasi

| Besaran | Rumus |
|---------|-------|
| Sigmoid | $\sigma(z)=\dfrac{1}{1+e^{-z}}$ |
| Turunan sigmoid | $\sigma'(z)=\sigma(z)\bigl(1-\sigma(z)\bigr)$ |
| Softmax | $\dfrac{e^{z_i}}{\sum_j e^{z_j}}$ |
| Odds | $\dfrac{P}{1-P}$ |
| Rasio odds | $e^{\beta_j}$ |
| Binary cross-entropy | $-\dfrac{1}{n}\sum\bigl[y\log\hat{y}+(1-y)\log(1-\hat{y})\bigr]$ |
| Naive Bayes | $P(y\mid x)\propto P(y)\prod_j P(x_j\mid y)$ |

### A.6 Jaringan Saraf Tiruan

| Besaran | Rumus |
|---------|-------|
| Perambatan maju | $z^{(l)}=W^{(l)}a^{(l-1)}+b^{(l)}$; $a^{(l)}=\sigma(z^{(l)})$ |
| ReLU | $\max(0,z)$ |
| Turunan ReLU | $1$ bila $z>0$, $0$ bila $z<0$ |
| Gradient descent | $w \leftarrow w-\eta\dfrac{\partial L}{\partial w}$ |
| Delta keluaran (MSE + sigmoid) | $\delta_{\text{out}}=-2(y-\hat{y})\cdot\hat{y}(1-\hat{y})$ |
| Delta tersembunyi | $\delta_h=\delta_{\text{out}}\cdot v\cdot h(1-h)$ |

### A.7 *Clustering*

| Besaran | Rumus |
|---------|-------|
| Inersia (WCSS) | $\sum_{k}\sum_{x\in C_k}\lVert x-\mu_k\rVert^2$ |
| Silhouette | $s(i)=\dfrac{b(i)-a(i)}{\max\{a(i),b(i)\}}$ |
| Jarak Euclidean | $\sqrt{\sum_j (x_j-y_j)^2}$ |
| Jarak Manhattan | $\sum_j \lvert x_j-y_j\rvert$ |

### A.8 Penskalaan dan Transformasi

| Penskala | Rumus |
|----------|-------|
| StandardScaler | $\dfrac{x-\mu}{\sigma}$ |
| MinMaxScaler | $\dfrac{x-\min}{\max-\min}$ |
| RobustScaler | $\dfrac{x-Q_2}{Q_3-Q_1}$ |
| Log | $\log(x+1)$ |
| Penyandian siklik | $\sin\left(\dfrac{2\pi x}{T}\right)$, $\cos\left(\dfrac{2\pi x}{T}\right)$ |

### A.9 Ukuran *Fairness*

| Ukuran | Menuntut |
|--------|----------|
| Demographic parity | $P(\hat{y}=1\mid A=a)$ sama untuk semua $a$ |
| Equal opportunity | $P(\hat{y}=1\mid y=1, A=a)$ sama (recall sama) |
| Equalized odds | Recall **dan** FPR sama |
| Predictive parity | $P(y=1\mid \hat{y}=1, A=a)$ sama (precision sama) |

### A.10 Perbandingan Model

| Besaran | Rumus |
|---------|-------|
| Rerata validasi silang | $\bar{s}=\dfrac{1}{k}\sum_i s_i$ |
| Simpangan baku sampel | $s=\sqrt{\dfrac{\sum(s_i-\bar{s})^2}{k-1}}$ |
| Simpangan gabungan dua model | $\sqrt{s_1^2+s_2^2}$ |

> **Kaidah:** selisih antarmodel yang **lebih kecil** daripada simpangan gabungan **bukan perbedaan yang dapat disimpulkan**.

---

## Lampiran B: Pohon Keputusan Pemilihan Model

```
LANGKAH 1 — Apakah ada label?
│
├── ADA LABEL (pembelajaran terbimbing)
│   │
│   └── LANGKAH 2 — Bentuk keluarannya?
│       │
│       ├── ANGKA KONTINU ─────────► REGRESI
│       │   ├── Hubungan linear, perlu keterjelasan
│       │   │                       ► Regresi linear / Ridge / Lasso
│       │   ├── Data tabular, kinerja utama
│       │   │                       ► Gradient Boosting / Random Forest
│       │   └── Data tak terstruktur ► Jaringan saraf (MK lain)
│       │
│       └── KATEGORI ──────────────► KLASIFIKASI
│           ├── Perlu keterjelasan  ► Regresi logistik / pohon dangkal
│           ├── Data tabular        ► Gradient Boosting / Random Forest
│           ├── Data kecil, cepat   ► Naive Bayes / k-NN
│           ├── Dimensi tinggi      ► SVM linear / regresi logistik
│           └── Data tak terstruktur ► Jaringan saraf (MK lain)
│
└── TIDAK ADA LABEL (tanpa supervisi)
    │
    └── LANGKAH 2 — Apa yang dicari?
        ├── KELOMPOK
        │   ├── Klaster bulat, k diketahui   ► K-Means
        │   ├── Struktur bertingkat           ► Hierarchical (Ward)
        │   └── Bentuk sembarang, ada pencilan ► DBSCAN
        ├── REPRESENTASI RINGKAS ─────────────► PCA
        ├── VISUALISASI 2D ───────────────────► t-SNE / UMAP
        └── PENGAMATAN TAK LAZIM ─────────────► Isolation Forest / LOF
```

### B.1 Penskalaan: Siapa yang Membutuhkan

| Wajib diskalakan | Tidak perlu |
|------------------|-------------|
| k-NN, SVM | Pohon keputusan |
| Regresi berregularisasi | Random Forest |
| Jaringan saraf tiruan | Gradient Boosting |
| K-Means, PCA | Naive Bayes (sebagian besar) |

### B.2 Strategi Pembagian Data

| Sifat data | Strategi |
|------------|----------|
| Kelas tak seimbang | `train_test_split(stratify=y)` / `StratifiedKFold` |
| Ada urutan waktu | `TimeSeriesSplit` |
| Entitas berulang | `GroupKFold` |
| Data sedikit | `KFold(n_splits=10)` |
| Penyetelan + penaksiran dari data sama | Validasi silang bersarang |

---

## Lampiran C: Rujukan `scikit-learn`

### C.1 Prapemrosesan

| Keperluan | Perintah |
|-----------|----------|
| Imputasi numerik | `SimpleImputer(strategy="median")` |
| Imputasi kategorik | `SimpleImputer(strategy="constant", fill_value="TIDAK_DIKETAHUI")` |
| Imputasi + penanda | `SimpleImputer(strategy="median", add_indicator=True)` |
| Imputasi tetangga | `KNNImputer(n_neighbors=5)` |
| Standardisasi | `StandardScaler()` |
| Rentang [0,1] | `MinMaxScaler()` |
| Tahan pencilan | `RobustScaler()` |
| One-hot | `OneHotEncoder(handle_unknown="ignore", sparse_output=False)` |
| Ordinal berurutan | `OrdinalEncoder(categories=[[...]])` |
| Transformasi pangkat | `PowerTransformer(method="yeo-johnson")` |
| Binning | `KBinsDiscretizer(n_bins=5, strategy="quantile")` |
| Gabungan per kolom | `ColumnTransformer([...])` |
| Rangkaian langkah | `Pipeline([...])` |

### C.2 Model

| Keperluan | Perintah |
|-----------|----------|
| *Baseline* klasifikasi | `DummyClassifier(strategy="most_frequent")` |
| *Baseline* regresi | `DummyRegressor(strategy="median")` |
| Regresi linear | `LinearRegression()` |
| Ridge dengan CV | `RidgeCV(alphas=np.logspace(-3,3,50), cv=5)` |
| Lasso dengan CV | `LassoCV(alphas=..., cv=5, max_iter=20000)` |
| Regresi logistik | `LogisticRegression(max_iter=1000, class_weight="balanced")` |
| k-NN | `KNeighborsClassifier(n_neighbors=5, weights="distance")` |
| Pohon keputusan | `DecisionTreeClassifier(max_depth=5, min_samples_leaf=10)` |
| Random Forest | `RandomForestClassifier(n_estimators=300, max_features="sqrt", n_jobs=-1)` |
| Gradient Boosting | `HistGradientBoostingClassifier(max_iter=300, early_stopping=True)` |
| SVM | `SVC(kernel="rbf", C=1.0, gamma="scale", probability=True)` |
| Naive Bayes | `GaussianNB()` / `MultinomialNB()` |
| MLP | `MLPClassifier(hidden_layer_sizes=(64,32), early_stopping=True)` |
| K-Means | `KMeans(n_clusters=k, n_init=20)` |
| Hierarchical | `AgglomerativeClustering(n_clusters=k, linkage="ward")` |
| DBSCAN | `DBSCAN(eps=0.5, min_samples=5)` |
| PCA | `PCA(n_components=0.95)` |
| Deteksi anomali | `IsolationForest(contamination=0.05)` |

### C.3 Evaluasi

| Keperluan | Perintah |
|-----------|----------|
| Pembagian data | `train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)` |
| Validasi silang | `cross_val_score(pipa, X, y, cv=cv, scoring="f1")` |
| Validasi silang lengkap | `cross_validate(pipa, X, y, cv=cv, scoring=[...], return_train_score=True)` |
| Lipatan berstratifikasi | `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` |
| Lipatan temporal | `TimeSeriesSplit(n_splits=5)` |
| Lipatan berkelompok | `GroupKFold(n_splits=5)` |
| Grid search | `GridSearchCV(pipa, ruang, cv=cv, scoring="f1", n_jobs=-1)` |
| Random search | `RandomizedSearchCV(pipa, ruang, n_iter=50, cv=cv)` |
| Matriks konfusi | `confusion_matrix(y_true, y_pred)` |
| Laporan lengkap | `classification_report(y_true, y_pred)` |
| ROC-AUC | `roc_auc_score(y_true, y_prob)` |
| PR-AUC | `average_precision_score(y_true, y_prob)` |
| Kurva pembelajaran | `learning_curve(model, X, y, train_sizes=..., cv=cv)` |
| Kurva validasi | `validation_curve(model, X, y, param_name=..., param_range=...)` |
| Kepentingan permutasi | `permutation_importance(model, X_test, y_test, n_repeats=10)` |
| Silhouette | `silhouette_score(X, label)` |
| Davies-Bouldin | `davies_bouldin_score(X, label)` |

### C.4 Visualisasi Bawaan

| Keperluan | Perintah |
|-----------|----------|
| Matriks konfusi | `ConfusionMatrixDisplay.from_estimator(m, X, y, normalize="true")` |
| Kurva ROC | `RocCurveDisplay.from_estimator(m, X, y)` |
| Kurva PR | `PrecisionRecallDisplay.from_estimator(m, X, y)` |
| Kurva kalibrasi | `CalibrationDisplay.from_estimator(m, X, y)` |
| Partial dependence | `PartialDependenceDisplay.from_estimator(m, X, features=[...])` |
| Struktur pohon | `plot_tree(clf, feature_names=..., filled=True)` |
| Pohon sebagai teks | `export_text(clf, feature_names=[...])` |

---

## Lampiran D: Sel Pembuka Baku

```python
# ==========================================================
# SEL PEMBUKA BAKU — dijalankan pada setiap notebook
# ==========================================================
import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

# Pencatatan versi — bagian dari reproduksibilitas,
# yang merupakan kriteria penilaian Sub-CPMK082-1
print("Python      :", sys.version.split()[0])
print("NumPy       :", np.__version__)
print("pandas      :", pd.__version__)
print("matplotlib  :", matplotlib.__version__)
print("seaborn     :", sns.__version__)
print("scikit-learn:", sklearn.__version__)

# Pengaturan tampilan
pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 120)
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (9, 5)
plt.rcParams["figure.dpi"] = 110

# Seed — WAJIB agar hasil dapat diulang
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)
print("\nLingkungan siap. RANDOM_STATE =", RANDOM_STATE)
```

### D.1 Templat Pemeriksaan Data

```python
def periksa_data(df, kolom_target=None):
    # Tujuh perintah pembuka
    print("1. Dimensi:", df.shape, "\n")
    print("2. Info:"); df.info()
    print("\n3. Ringkasan numerik:"); display(df.describe().T.round(2))
    print("\n4. Nilai hilang (%):")
    print((df.isna().mean()*100).round(2).sort_values(ascending=False).head(15))
    print("\n5. Duplikat penuh:", df.duplicated().sum())
    print("\n6. Kardinalitas kategorik:")
    for k in df.select_dtypes(include="object").columns:
        print(f"   {k:25s} {df[k].nunique():5d} unik")
    if kolom_target:
        print(f"\n7. Sebaran {kolom_target}:")
        print(df[kolom_target].value_counts(normalize=True).round(3))
```

### D.2 Templat `Pipeline`

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

def buat_pipeline(kol_num, kol_kat, model, skala=True):
    pra = ColumnTransformer([
        ("num", Pipeline([
            ("imputasi", SimpleImputer(strategy="median")),
            ("skala", StandardScaler() if skala else "passthrough"),
        ]), kol_num),
        ("kat", Pipeline([
            ("imputasi", SimpleImputer(strategy="constant",
                                       fill_value="TIDAK_DIKETAHUI")),
            ("sandi", OneHotEncoder(handle_unknown="ignore",
                                    sparse_output=False)),
        ]), kol_kat),
    ])
    return Pipeline([("pra", pra), ("model", model)])
```

---

## Lampiran E: Daftar Periksa

### E.1 Sebelum Mengumpulkan Praktikum

- [ ] Sel pembuka baku dijalankan; versi pustaka tercatat
- [ ] `RANDOM_STATE` ditetapkan
- [ ] Seluruh transformasi di dalam `Pipeline`
- [ ] `fit` hanya pada data latih
- [ ] *Baseline* disertakan
- [ ] Metrik sesuai jenis masalah; alasan tertulis
- [ ] Setiap keluaran disertai kalimat interpretasi
- [ ] Notebook berjalan ulang dari sel pertama tanpa galat
- [ ] AI Usage Log lengkap dan ditandatangani
- [ ] Penamaan berkas `NIM_Nama_LabNN.ipynb`

### E.2 Daftar Periksa Kebocoran

- [ ] Seluruh transformasi di dalam `Pipeline`
- [ ] Data uji tidak dipakai untuk memilih atau menyetel
- [ ] Ada urutan waktu → pembagian temporal
- [ ] Entitas berulang → `GroupKFold`
- [ ] Duplikat diperiksa sebelum pembagian
- [ ] Tiap fitur lolos: *"tersedia saat prediksi dibutuhkan?"*
- [ ] Tidak ada fitur turunan target
- [ ] Skor mencurigakan tinggi sudah diselidiki

### E.3 Sebelum Mengumpulkan Laporan Proyek

Lihat [Bab 14 §14.8](bab-14-proyek-akhir.md) untuk daftar lengkap.

---

## Lampiran F: Glosarium

| Indonesia | Inggris | Makna ringkas |
|-----------|---------|---------------|
| Ambang keputusan | Decision threshold | Batas probabilitas yang mengubah prediksi menjadi kelas |
| Bias (model) | Bias | Kekeliruan sistematis karena model terlalu sederhana |
| Bias (keadilan) | Bias/unfairness | Ketimpangan kinerja antarkelompok |
| *Clustering* | Clustering | Pengelompokan tanpa label |
| Data latih | Training set | Bagian data tempat model belajar |
| Data uji | Test set | Bagian data untuk menaksir kinerja akhir |
| Data validasi | Validation set | Bagian data untuk memilih dan menyetel |
| Deteksi anomali | Anomaly detection | Penandaan pengamatan tak lazim |
| Fitur | Feature | Variabel masukan model |
| Hiperparameter | Hyperparameter | Pengaturan yang ditetapkan sebelum pelatihan |
| Kebocoran data | Data leakage | Masuknya informasi yang seharusnya tersembunyi |
| Kepentingan fitur | Feature importance | Sumbangan fitur pada kemampuan prediksi |
| Keterjelasan | Explainability | Kemampuan menjelaskan keputusan model |
| Klasifikasi | Classification | Prediksi kategori |
| Kurva pembelajaran | Learning curve | Kinerja terhadap jumlah data latih |
| Kutukan dimensi | Curse of dimensionality | Data menjadi jarang pada dimensi tinggi |
| Laju pembelajaran | Learning rate | Ukuran langkah pembaruan bobot |
| Matriks konfusi | Confusion matrix | Tabel benar/salah per kelas |
| Pembelajaran penguatan | Reinforcement learning | Belajar dari imbalan interaksi |
| Pembelajaran terbimbing | Supervised learning | Belajar dari data berlabel |
| Pembelajaran tanpa supervisi | Unsupervised learning | Belajar dari data tanpa label |
| Pencilan | Outlier | Pengamatan jauh dari pola umum |
| *Pipeline* | Pipeline | Rangkaian langkah prapemrosesan dan model |
| Prapemrosesan | Preprocessing | Penyiapan data sebelum pelatihan |
| Rasio odds | Odds ratio | $e^{\beta}$ pada regresi logistik |
| Reduksi dimensi | Dimensionality reduction | Meringkas banyak fitur menjadi sedikit |
| Regularisasi | Regularization | Denda atas kompleksitas model |
| Rekayasa fitur | Feature engineering | Pembuatan fitur baru dari data mentah |
| Reproduksibilitas | Reproducibility | Kemampuan hasil diulang secara identik |
| Stratifikasi | Stratification | Menjaga proporsi kelas saat pembagian |
| Target | Target/label | Variabel yang diprediksi |
| *Underfitting* | Underfitting | Model terlalu sederhana untuk pola yang ada |
| *Overfitting* | Overfitting | Model menghafal data latih |
| Validasi silang | Cross-validation | Evaluasi dengan lipatan bergantian |
| Varians (model) | Variance | Kepekaan model terhadap data latih |

---

## Lampiran G: Kesalahan Tafsir yang Sering Terjadi

Periksa daftar ini sebelum menyerahkan laporan apa pun.

| # | Kalimat yang keliru | Mengapa keliru | Versi yang benar |
|---|---------------------|----------------|------------------|
| 1 | "Model ini akurat 94%" | Tanpa *baseline* dan tanpa keseimbangan kelas, tidak bermakna | "Akurasi 94%, *baseline* 91%, *recall* kelas positif 0,38" |
| 2 | "Fitur X paling memengaruhi hasil" | Kepentingan fitur bukan sebab-akibat | "Fitur X paling berkontribusi pada kemampuan model membedakan kelas" |
| 3 | "Model A lebih baik (0,852 vs 0,847)" | Selisih lebih kecil daripada simpangan | "Selisih 0,005 dengan simpangan gabungan 0,041 — tidak dapat disimpulkan" |
| 4 | "ROC-AUC 0,98, model sangat baik" | Skor terlalu tinggi adalah tanda bahaya | "ROC-AUC 0,98 — diperiksa terhadap kebocoran; hasilnya: ..." |
| 5 | "Model sudah adil karena kolom gender dibuang" | Proksi tetap ada | "Kinerja diukur per kelompok meski gender tidak dipakai sebagai fitur" |
| 6 | "Tidak ada keterbatasan" | Selalu ada | Tulis minimal empat butir |
| 7 | "Model memutuskan penolakan" | Model tidak memutuskan | "Model memberi skor; keputusan diambil oleh [peran], dengan [mekanisme peninjauan]" |
| 8 | "Kami memakai ambang 0,5" (tanpa alasan) | Ambang adalah pilihan | "Ambang 0,28 dipilih dari analisis biaya FN:FP = 100:1" |
| 9 | "Data sudah dibersihkan dari pencilan" | Pencilan sah bukan kotoran | "3 pencilan diperiksa; terbukti sah, maka dipertahankan" |
| 10 | "Model ini dapat dipakai untuk seluruh Indonesia" | Data hanya mencakup sebagian | "Model berlaku untuk lima provinsi yang tercakup data latih" |
| 11 | "AI yang membuat modelnya, jadi pasti benar" | Tanggung jawab tetap pada analis | "Setiap keputusan diverifikasi; rinciannya pada AI Usage Log" |
| 12 | "*Clustering* menemukan kelompok terbaik dan terburuk" | *Clustering* menemukan kelompok, bukan peringkat | "Klaster dengan IPM tinggi dan kepadatan tinggi" |

---

## Lampiran H: Templat *Model Card*

```markdown
# Model Card — [Nama Model]

## 1. Rincian Model
- Dikembangkan oleh:
- Tanggal:                     Versi:
- Jenis model:
- Sumber dan lisensi data:

## 2. Penggunaan yang Dimaksudkan
- **Untuk:**
- **BUKAN untuk:**
- Pengguna yang dituju:
- Di luar cakupan:

## 3. Data
- Sumber, periode, dimensi:
- Cakupan kelompok:
- **Yang TIDAK tercakup:**
- Prapemrosesan:

## 4. Kinerja
| Kelompok | n | Base rate | Precision | Recall | FPR |
|----------|---|-----------|-----------|--------|-----|
| Keseluruhan | | | | | |
| ... | | | | | |

- Baseline:
- Metrik utama dan alasan pemilihannya:
- Simpangan antarlipatan:

## 5. Keterbatasan
- Kelompok dengan kinerja terendah dan besar selisihnya:
- Kondisi ketika model tidak dapat diandalkan:
- Asumsi yang dapat gugur seiring waktu:

## 6. Pertimbangan Etis
- Siapa yang dapat dirugikan bila model salah:
- **Ukuran fairness yang dipilih DAN ALASANNYA:**
- Apa yang dikorbankan dengan pilihan itu:
- Mekanisme pengawasan manusia:
- Cara mengajukan keberatan:

## 7. Pemeliharaan
- Kapan model harus dilatih ulang:
- Indikator yang dipantau:
- Penanggung jawab:
```

---

## Lampiran I: Peta Bab – Modul – Praktikum

| Mg | Bab | Modul Kuliah | Praktikum |
|----|-----|--------------|-----------|
| 1 | [Bab 1](bab-01-lanskap-kecerdasan-artifisial.md) | [Minggu 1](../03-modules/week-01-lanskap-kecerdasan-artifisial.md) | [Lab 1](../04-labs/lab-01-setup-ekosistem-ml.md) |
| 2 | [Bab 2](bab-02-formulasi-masalah-daur-hidup-ml.md) | [Minggu 2](../03-modules/week-02-formulasi-masalah-daur-hidup-ml.md) | [Lab 2](../04-labs/lab-02-formulasi-masalah-baseline.md) |
| 3 | [Bab 3](bab-03-data-dan-prapemrosesan.md) | [Minggu 3](../03-modules/week-03-data-dan-prapemrosesan.md) | [Lab 3](../04-labs/lab-03-pipeline-prapemrosesan.md) |
| 4 | [Bab 4](bab-04-pembagian-data-dan-kebocoran.md) | [Minggu 4](../03-modules/week-04-pembagian-data-dan-kebocoran.md) | [Lab 4](../04-labs/lab-04-validasi-silang-deteksi-kebocoran.md) |
| 5 | [Bab 5](bab-05-rekayasa-fitur.md) | [Minggu 5](../03-modules/week-05-rekayasa-fitur.md) | [Lab 5](../04-labs/lab-05-rekayasa-fitur.md) |
| 6 | [Bab 6](bab-06-regresi-dan-metriknya.md) | [Minggu 6](../03-modules/week-06-regresi-dan-metriknya.md) | [Lab 6](../04-labs/lab-06-model-regresi-dan-metrik.md) |
| 7 | [Bab 7](bab-07-klasifikasi-dan-metriknya.md) | [Minggu 7](../03-modules/week-07-klasifikasi-dan-metriknya.md) | [Lab 7](../04-labs/lab-07-klasifikasi-dan-metrik.md) |
| 8 | — | [Minggu 8 — UTS](../03-modules/week-08-uts-review-dan-ujian.md) | — |
| 9 | [Bab 8](bab-08-pohon-keputusan-dan-ensemble.md) | [Minggu 9](../03-modules/week-09-pohon-keputusan-dan-ensemble.md) | [Lab 9](../04-labs/lab-09-pohon-keputusan-dan-ensemble.md) |
| 10 | [Bab 9](bab-09-svm-naive-bayes-pemilihan-model.md) | [Minggu 10](../03-modules/week-10-svm-naive-bayes-pemilihan-model.md) | [Lab 10](../04-labs/lab-10-svm-naive-bayes-penyetelan.md) |
| 11 | [Bab 10](bab-10-pembelajaran-tanpa-supervisi.md) | [Minggu 11](../03-modules/week-11-pembelajaran-tanpa-supervisi.md) | [Lab 11](../04-labs/lab-11-clustering-dan-metriknya.md) |
| 12 | [Bab 11](bab-11-reduksi-dimensi-dan-visualisasi.md) | [Minggu 12](../03-modules/week-12-reduksi-dimensi-dan-visualisasi.md) | [Lab 12](../04-labs/lab-12-pca-dan-visualisasi-model.md) |
| 13 | [Bab 12](bab-12-pengantar-jaringan-saraf-tiruan.md) | [Minggu 13](../03-modules/week-13-pengantar-jaringan-saraf-tiruan.md) | [Lab 13](../04-labs/lab-13-jaringan-saraf-tiruan.md) |
| 14 | [Bab 13](bab-13-ai-generatif-dan-ai-bertanggung-jawab.md) · [Bab 14](bab-14-proyek-akhir.md) | [Minggu 14](../03-modules/week-14-ai-generatif-dan-ai-bertanggung-jawab.md) | [Lab 14](../04-labs/lab-14-audit-bias-dan-model-card.md) |
| 15 | [Bab 14](bab-14-proyek-akhir.md) | [Minggu 15](../03-modules/week-15-presentasi-proyek.md) | — |
| 16 | — | [Minggu 16 — UAS](../03-modules/week-16-uas-review-dan-ujian.md) | — |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
