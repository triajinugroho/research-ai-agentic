# Lab 07: Model Klasifikasi dan Metriknya

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 7 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-07 |
| Durasi | 100 menit |
| Prasyarat | Lab 6 selesai |
| Bobot | 1,9% (Observasi) |

---

## Tujuan Praktikum

1. Menghitung matriks konfusi dan seluruh metrik turunannya secara manual.
2. Menunjukkan mengapa akurasi menyesatkan pada data tak seimbang.
3. Menentukan ambang keputusan berdasarkan biaya kesalahan.
4. Menafsirkan kurva ROC dan *precision-recall*.

---

## Langkah-langkah

### LANGKAH 1: Data Tak Seimbang

```python
# =============================================
# LANGKAH 1: Deteksi transaksi janggal — 2% positif
# =============================================
import numpy as np, pandas as pd
rng = np.random.default_rng(RANDOM_STATE)
n = 8000

df = pd.DataFrame({
    "nominal_rb":      rng.gamma(2.0, 180, size=n).round(0),
    "jam_transaksi":   rng.integers(0, 24, size=n),
    "jarak_lokasi_km": rng.gamma(1.5, 12, size=n).round(1),
    "frekuensi_harian":rng.poisson(3, size=n) + 1,
    "usia_akun_hari":  rng.gamma(3.0, 200, size=n).round(0),
    "jenis_perangkat": rng.choice(["Android", "iOS", "Web"], size=n,
                                  p=[0.55, 0.30, 0.15]),
})

logit = (-5.0 + 0.0022 * df["nominal_rb"]
         + 0.016 * df["jarak_lokasi_km"]
         + 0.9 * df["jam_transaksi"].isin([0,1,2,3,4]).astype(float)
         - 0.0022 * df["usia_akun_hari"])
df["janggal"] = rng.binomial(1, 1 / (1 + np.exp(-logit)))

print("Dimensi:", df.shape)
print(f"Proporsi janggal: {df['janggal'].mean():.4f} "
      f"({df['janggal'].sum()} dari {len(df)})")
```

### LANGKAH 2: *Baseline* yang Menipu

```python
# =============================================
# LANGKAH 2: Model yang selalu menjawab "wajar"
# =============================================
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (confusion_matrix, accuracy_score,
                             precision_score, recall_score, f1_score)

X = df.drop(columns=["janggal"]); y = df["janggal"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE)

dummy = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
pred_dummy = dummy.predict(X_test)

print("Model yang SELALU menjawab 'wajar':")
print(f"  Akurasi  : {accuracy_score(y_test, pred_dummy):.4f}  <-- tampak hebat")
print(f"  Precision: {precision_score(y_test, pred_dummy, zero_division=0):.4f}")
print(f"  Recall   : {recall_score(y_test, pred_dummy, zero_division=0):.4f}  <-- NOL")
print(f"  F1       : {f1_score(y_test, pred_dummy, zero_division=0):.4f}")
print("\nModel ini tidak menemukan satu pun transaksi janggal.")
```

> **Inilah alasan mengapa melaporkan akurasi saja pada data tak seimbang dikenai pengurangan nilai di mata kuliah ini.**

### LANGKAH 3: Perhitungan Manual Matriks Konfusi

```python
# =============================================
# LANGKAH 3: Hitung manual, lalu verifikasi
# =============================================
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression

kol_num = ["nominal_rb", "jam_transaksi", "jarak_lokasi_km",
           "frekuensi_harian", "usia_akun_hari"]
kol_kat = ["jenis_perangkat"]

pra = ColumnTransformer([
    ("num", StandardScaler(), kol_num),
    ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), kol_kat),
])

logreg = Pipeline([
    ("pra", pra),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced",
                               random_state=RANDOM_STATE)),
]).fit(X_train, y_train)

pred = logreg.predict(X_test)
cm = confusion_matrix(y_test, pred)
tn, fp, fn, tp = cm.ravel()

print("Matriks konfusi:")
print(pd.DataFrame(cm, index=["Aktual wajar", "Aktual janggal"],
                   columns=["Prediksi wajar", "Prediksi janggal"]))

# --- HITUNG MANUAL ---
akurasi_m   = (tp + tn) / (tp + tn + fp + fn)
precision_m = tp / (tp + fp) if (tp + fp) else 0
recall_m    = tp / (tp + fn) if (tp + fn) else 0
spesif_m    = tn / (tn + fp) if (tn + fp) else 0
f1_m        = 2 * precision_m * recall_m / (precision_m + recall_m) \
              if (precision_m + recall_m) else 0

print(f"\nTN={tn}  FP={fp}  FN={fn}  TP={tp}")
print(f"\nManual — Akurasi    : ({tp}+{tn})/{tp+tn+fp+fn} = {akurasi_m:.4f}")
print(f"Manual — Precision  : {tp}/({tp}+{fp}) = {precision_m:.4f}")
print(f"Manual — Recall     : {tp}/({tp}+{fn}) = {recall_m:.4f}")
print(f"Manual — Spesifisitas: {tn}/({tn}+{fp}) = {spesif_m:.4f}")
print(f"Manual — F1         : {f1_m:.4f}")

print(f"\nVerifikasi sklearn  : akurasi={accuracy_score(y_test, pred):.4f}  "
      f"precision={precision_score(y_test, pred):.4f}  "
      f"recall={recall_score(y_test, pred):.4f}  f1={f1_score(y_test, pred):.4f}")
```

### LANGKAH 4: Tafsir *Odds Ratio*

```python
# =============================================
# LANGKAH 4: Odds ratio
# =============================================
nama_fitur = logreg.named_steps["pra"].get_feature_names_out()
koef = logreg.named_steps["clf"].coef_[0]

odds = pd.DataFrame({
    "Fitur": nama_fitur,
    "Koefisien": koef.round(4),
    "Rasio odds": np.exp(koef).round(4),
}).sort_values("Rasio odds", ascending=False)

print(odds.to_string(index=False))
print("\nTafsir: rasio odds > 1 menaikkan peluang janggal;")
print("        rasio odds < 1 menurunkannya.")
print("Koefisien dihitung pada skala TERSTANDARDISASI, sehingga")
print("tafsirnya adalah 'per satu simpangan baku', bukan per satu satuan asli.")
```

### LANGKAH 5: k-NN sebagai Pembanding

```python
# =============================================
# LANGKAH 5: k-NN — penskalaan WAJIB
# =============================================
from sklearn.neighbors import KNeighborsClassifier

hasil = []
for k in [3, 5, 11, 21]:
    knn = Pipeline([("pra", pra),
                    ("clf", KNeighborsClassifier(n_neighbors=k,
                                                 weights="distance"))]).fit(X_train, y_train)
    p = knn.predict(X_test)
    hasil.append({"Model": f"k-NN (k={k})",
                  "Akurasi": accuracy_score(y_test, p),
                  "Precision": precision_score(y_test, p, zero_division=0),
                  "Recall": recall_score(y_test, p, zero_division=0),
                  "F1": f1_score(y_test, p, zero_division=0)})

hasil.insert(0, {"Model": "Baseline (mayoritas)",
                 "Akurasi": accuracy_score(y_test, pred_dummy),
                 "Precision": 0.0, "Recall": 0.0, "F1": 0.0})
hasil.insert(1, {"Model": "Regresi logistik (balanced)",
                 "Akurasi": accuracy_score(y_test, pred),
                 "Precision": precision_score(y_test, pred),
                 "Recall": recall_score(y_test, pred),
                 "F1": f1_score(y_test, pred)})

print(pd.DataFrame(hasil).round(4).to_string(index=False))
```

### LANGKAH 6: Ambang Keputusan dan Biaya

```python
# =============================================
# LANGKAH 6: Menentukan ambang dari BIAYA
# =============================================
prob = logreg.predict_proba(X_test)[:, 1]

BIAYA_FN = 5_000_000   # transaksi janggal lolos: rata-rata kerugian
BIAYA_FP =    50_000   # pemeriksaan sia-sia: biaya petugas

baris = []
for t in np.arange(0.05, 0.96, 0.05):
    p = (prob >= t).astype(int)
    tn_, fp_, fn_, tp_ = confusion_matrix(y_test, p).ravel()
    baris.append({
        "Ambang": round(t, 2),
        "TP": tp_, "FP": fp_, "FN": fn_,
        "Precision": precision_score(y_test, p, zero_division=0),
        "Recall": recall_score(y_test, p, zero_division=0),
        "F1": f1_score(y_test, p, zero_division=0),
        "Total biaya (Rp)": fn_ * BIAYA_FN + fp_ * BIAYA_FP,
    })

tabel_ambang = pd.DataFrame(baris)
print(tabel_ambang.round(4).to_string(index=False))

terbaik_biaya = tabel_ambang.loc[tabel_ambang["Total biaya (Rp)"].idxmin()]
terbaik_f1    = tabel_ambang.loc[tabel_ambang["F1"].idxmax()]
print(f"\nAmbang dengan biaya terendah : {terbaik_biaya['Ambang']} "
      f"(Rp {terbaik_biaya['Total biaya (Rp)']:,.0f})")
print(f"Ambang dengan F1 tertinggi   : {terbaik_f1['Ambang']} "
      f"(F1 {terbaik_f1['F1']:.4f})")
```

**Tulis kesimpulan:** apakah kedua ambang itu sama? Bila berbeda, mana yang sebaiknya dipakai dan mengapa?

### LANGKAH 7: Kurva ROC dan Precision-Recall

```python
# =============================================
# LANGKAH 7: ROC vs PR pada data tak seimbang
# =============================================
import matplotlib.pyplot as plt
from sklearn.metrics import (RocCurveDisplay, PrecisionRecallDisplay,
                             roc_auc_score, average_precision_score)

fig, ax = plt.subplots(1, 2, figsize=(13, 5))

RocCurveDisplay.from_predictions(y_test, prob, ax=ax[0], name="Regresi logistik")
ax[0].plot([0, 1], [0, 1], "k--", lw=1, label="Acak")
ax[0].set_title(f"Kurva ROC (n={len(y_test)})"); ax[0].legend()

PrecisionRecallDisplay.from_predictions(y_test, prob, ax=ax[1],
                                        name="Regresi logistik")
ax[1].axhline(y_test.mean(), color="k", ls="--", lw=1,
              label=f"Baseline = proporsi positif ({y_test.mean():.3f})")
ax[1].set_title("Kurva Precision-Recall"); ax[1].legend()

plt.tight_layout(); plt.show()

print(f"ROC-AUC: {roc_auc_score(y_test, prob):.4f}")
print(f"PR-AUC : {average_precision_score(y_test, prob):.4f}")
print(f"Proporsi positif (baseline PR): {y_test.mean():.4f}")
```

> **Perhatikan selisih ROC-AUC dan PR-AUC.** Pada data dengan 2% positif, ROC-AUC dapat mencapai 0,90 sementara PR-AUC hanya 0,30 — dan PR-AUC-lah yang lebih jujur menggambarkan kegunaan model.

---

## Tantangan Tambahan

### Tantangan 1 — Pengaruh `class_weight`

Latih regresi logistik dengan dan tanpa `class_weight="balanced"`. Bandingkan *precision*, *recall*, dan ambang optimumnya. Apa yang sebenarnya dilakukan `class_weight`?

### Tantangan 2 — Biaya yang Berbeda

Ubah `BIAYA_FN` menjadi Rp 500.000 (sepersepuluh) dan jalankan ulang analisis ambang. Bagaimana ambang optimum bergeser? Jelaskan hubungannya dengan rasio biaya.

### Tantangan 3 — SMOTE di Dalam `Pipeline`

Pasang `imbalanced-learn`, lalu terapkan SMOTE **di dalam** `imblearn.pipeline.Pipeline`. Bandingkan hasilnya dengan `class_weight="balanced"`. Tunjukkan pula apa yang terjadi bila SMOTE diterapkan **sebelum** pembagian data (kebocoran).

---

## Checklist Penyelesaian

- [ ] *Baseline* mayoritas dibangun dan **akurasi tingginya ditunjukkan sebagai peringatan**
- [ ] **Perhitungan manual** matriks konfusi dan lima metrik, diverifikasi dengan sklearn
- [ ] Rasio odds dihitung dan ditafsirkan dengan benar (per simpangan baku)
- [ ] k-NN dijalankan di dalam `Pipeline` berpenskalaan
- [ ] **Analisis ambang berdasarkan biaya** dijalankan
- [ ] Perbedaan ambang optimum biaya dan F1 dibahas
- [ ] Kurva ROC **dan** PR ditampilkan dengan garis *baseline*
- [ ] Selisih ROC-AUC dan PR-AUC dijelaskan
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 7](../03-modules/week-07-klasifikasi-dan-metriknya.md)
2. [Bab 7 buku ajar](../06-buku-ajar/bab-07-klasifikasi-dan-metriknya.md)
3. Saito, T., & Rehmsmeier, M. (2015). The Precision-Recall Plot Is More Informative than the ROC Plot. *PLoS ONE*, 10(3).
4. Dokumentasi scikit-learn — *Classification metrics*. <https://scikit-learn.org/stable/modules/model_evaluation.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
