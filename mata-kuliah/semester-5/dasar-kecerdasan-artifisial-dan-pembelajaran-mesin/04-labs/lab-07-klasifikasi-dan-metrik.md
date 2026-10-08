# Lab 07: Model Klasifikasi dan Metriknya

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 7 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-07 |
| Durasi | 100 menit |
| Prasyarat | Lab 6 selesai |
| Bobot | 1,875% (Observasi, Sub-CPMK082-1) |
| Diuji pada | scikit-learn 1.6 dan 1.9, pandas 2.2 dan 3.0 (Oktober 2026) |

---

## Tujuan Praktikum

1. Menghitung matriks konfusi dan seluruh metrik turunannya secara manual.
2. Menunjukkan mengapa akurasi menyesatkan pada data tak seimbang.
3. Menentukan ambang keputusan berdasarkan biaya kesalahan.
4. Menafsirkan kurva ROC dan *precision-recall*.

---

## Persiapan

1. Buat notebook baru bernama `NIM_Nama_Lab07.ipynb`.
2. Jalankan **sel pembuka baku** di [Lampiran D](../06-buku-ajar/lampiran.md#lampiran-d-sel-pembuka-baku) — mengimpor pustaka, mencatat versi, dan menetapkan `RANDOM_STATE = 42`. Seluruh langkah di bawah mengandaikan sel itu sudah dijalankan.
3. **Data:** data transaksi lab ini adalah **data sintetis (simulasi)** yang meniru pola transaksi pembayaran digital (dompet digital) di Indonesia; **bukan data resmi BPS/lembaga** mana pun (termasuk bank, Bank Indonesia, atau OJK). Data dibangkitkan pada Langkah 1: 12.000 transaksi dengan ≈ 6% berlabel janggal, sehingga data uji (20%) memuat 145 transaksi janggal — cukup banyak agar *precision*, *recall*, dan analisis ambang tidak ditentukan oleh segelintir kasus. Aturan pembangkit label (nominal besar, lokasi jauh, transaksi dini hari, akun baru → lebih berisiko) adalah **asumsi ilustratif**, bukan temuan empiris tentang penipuan; `frekuensi_harian` dan `jenis_perangkat` sengaja **tidak** ikut menentukan label.

---

## Langkah-langkah

### LANGKAH 1: Data Tak Seimbang

> **Data sintetis (simulasi)** yang meniru pola transaksi pembayaran digital di Indonesia; bukan data resmi BPS/lembaga. Peluang janggal dibangkitkan dari nominal, jarak lokasi, transaksi dini hari (pukul 00.00–04.59), dan usia akun, ditambah keacakan; sekitar 6% transaksi berakhir berlabel janggal.

```python
# =============================================
# LANGKAH 1: Data SINTETIS — deteksi transaksi janggal (≈ 6% positif)
# (simulasi, bukan data resmi BPS/lembaga)
# =============================================
import numpy as np, pandas as pd
rng = np.random.default_rng(RANDOM_STATE)
n = 12_000

df = pd.DataFrame({
    "nominal_rb":      rng.gamma(2.0, 180, size=n).round(0),
    "jam_transaksi":   rng.integers(0, 24, size=n),
    "jarak_lokasi_km": rng.gamma(1.5, 12, size=n).round(1),
    "frekuensi_harian":rng.poisson(3, size=n) + 1,
    "usia_akun_hari":  rng.gamma(3.0, 200, size=n).round(0),
    "jenis_perangkat": rng.choice(["Android", "iOS", "Web"], size=n,
                                  p=[0.55, 0.30, 0.15]),
})

# Aturan pembangkit label (asumsi ilustratif): nominal besar, lokasi jauh,
# transaksi dini hari (00.00–04.59), dan akun baru menaikkan peluang janggal.
# frekuensi_harian dan jenis_perangkat TIDAK ikut menentukan label.
dini_hari = df["jam_transaksi"].isin([0, 1, 2, 3, 4]).astype(float)
logit = (-3.8 + 0.004 * df["nominal_rb"]
         + 0.03 * df["jarak_lokasi_km"]
         + 1.5 * dini_hari
         - 0.004 * df["usia_akun_hari"])
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
akurasi_dummy = accuracy_score(y_test, pred_dummy)
recall_dummy  = recall_score(y_test, pred_dummy, zero_division=0)

print(f"Data uji: {len(y_test)} transaksi, {y_test.sum()} janggal ({y_test.mean():.2%})")
print("\nModel yang SELALU menjawab 'wajar':")
print(f"  Akurasi  : {akurasi_dummy:.4f}  <-- tampak hebat")
print(f"  Precision: {precision_score(y_test, pred_dummy, zero_division=0):.4f}")
print(f"  Recall   : {recall_dummy:.4f}  <-- perhatikan")
print(f"  F1       : {f1_score(y_test, pred_dummy, zero_division=0):.4f}")

# Kesimpulan dihitung dari hasil, bukan teks tetap
if recall_dummy == 0:
    print(f"\nAkurasi {akurasi_dummy:.1%} hanya mencerminkan porsi kelas 'wajar' — "
          f"model ini tidak menemukan satu pun dari {y_test.sum()} transaksi janggal.")
else:
    print(f"\nModel ini menemukan {recall_dummy:.1%} transaksi janggal.")
```

> **Inilah alasan mengapa melaporkan akurasi saja pada data tak seimbang dikenai pengurangan nilai di mata kuliah ini.**

**Pemeriksaan otomatis.** Sel berikut harus lulus tanpa `AssertionError`; bila gagal, pesannya menunjukkan apa yang perlu diperiksa.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 1 dan 2
# =============================================
n_pos_uji = int(y_test.sum())
assert n_pos_uji >= 100, (
    f"Data uji hanya memuat {n_pos_uji} transaksi janggal (< 100) — metrik kelas positif "
    f"akan ditentukan oleh segelintir kasus; periksa n dan intersep logit di Langkah 1")
assert 0.03 <= y_test.mean() <= 0.12, (
    f"Proporsi janggal {y_test.mean():.2%} di luar rentang tak seimbang yang dimaksud (3–12%)")
assert akurasi_dummy >= 0.90 and recall_dummy == 0, (
    f"Baseline mayoritas seharusnya berakurasi tinggi (≥ 0,90) tetapi recall-nya 0 "
    f"(sekarang akurasi {akurasi_dummy:.4f}, recall {recall_dummy:.4f})")
print("Pemeriksaan otomatis lulus.")
```

Pada data lab ini, data uji berisi 2.400 transaksi dengan 145 transaksi janggal (6,0%). *Baseline* mayoritas meraih akurasi ≈ 0,94 — tanpa menemukan satu pun transaksi janggal (*recall* 0).

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

# Rasio odds hanya bermakna bila hubungannya (pada skala logit) kira-kira linear
or_jam = odds.set_index("Fitur").loc["num__jam_transaksi", "Rasio odds"]
if or_jam < 1:
    print(f"\nAwas: rasio odds jam_transaksi = {or_jam:.2f} (< 1) seolah berarti "
          "'makin larut makin aman'.")
    print("Padahal risiko pada data ini naik hanya pada dini hari (00.00–04.59) —")
    print("pola tak linear yang tidak dapat diwakili satu koefisien linear untuk jam 0–23.")
else:
    print(f"\nRasio odds jam_transaksi = {or_jam:.2f}; ingat, risiko pada data ini "
          "hanya naik pada dini hari (00.00–04.59) — hubungan yang tidak linear.")
```

**Yang harus ditulis di sel Markdown:**
- Fitur numerik mana yang efeknya paling kuat? Bandingkan **|koefisien|**, yaitu jarak rasio odds dari 1 pada skala log — bukan selisih biasa: rasio odds 0,25 sama kuatnya dengan 4 ke arah sebaliknya, karena |ln 0,25| = |ln 4|. Cocokkan dengan aturan pembangkit di Langkah 1 **setelah** koefisien pembangkitnya dikalikan simpangan baku fitur (`X_train[kol_num].std()`): koefisien pembangkit berlaku per satu satuan asli, sedangkan koefisien model per satu simpangan baku.
- Mengapa rasio odds `jam_transaksi` tidak menggambarkan risiko dini hari, dan fitur apa yang akan Anda rancang untuk menangkapnya (bandingkan dengan Lab 5)?
- Untuk `jenis_perangkat`, bandingkan rasio odds **antarkategori**, bukan terhadap 1: ketiga kolom *one-hot* selalu berjumlah 1 — sama persis dengan kolom intersep (kolinearitas sempurna) — sehingga sebuah konstanta dapat berpindah antara intersep dan ketiga koefisien tanpa mengubah prediksi. Karena itu tingkat absolut rasio odds-nya (misalnya semuanya < 1) tidak bermakna; hanya selisih antarkategori yang bermakna. Apakah selisihnya besar?

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
                 "Akurasi": akurasi_dummy,
                 "Precision": precision_score(y_test, pred_dummy, zero_division=0),
                 "Recall": recall_dummy,
                 "F1": f1_score(y_test, pred_dummy, zero_division=0)})
hasil.insert(1, {"Model": "Regresi logistik (balanced)",
                 "Akurasi": accuracy_score(y_test, pred),
                 "Precision": precision_score(y_test, pred),
                 "Recall": recall_score(y_test, pred),
                 "F1": f1_score(y_test, pred)})

tabel_model = pd.DataFrame(hasil)
print(tabel_model.round(4).to_string(index=False))

# Kesimpulan dihitung dari hasil
baris_knn = tabel_model[tabel_model["Model"].str.startswith("k-NN")]
knn_terbaik = baris_knn.loc[baris_knn["F1"].idxmax()]
baris_lr = tabel_model.iloc[1]
if knn_terbaik["F1"] < baris_lr["F1"]:
    print(f"\nk-NN terbaik ({knn_terbaik['Model']}, F1 {knn_terbaik['F1']:.3f}) masih di bawah "
          f"regresi logistik balanced (F1 {baris_lr['F1']:.3f}).")
    print(f"Recall k-NN hanya {knn_terbaik['Recall']:.2f} vs {baris_lr['Recall']:.2f}: "
          "KNeighborsClassifier tidak punya class_weight, sehingga tetangga")
    print("terdekat sebuah transaksi janggal pun sering didominasi transaksi wajar.")
else:
    print(f"\nk-NN terbaik ({knn_terbaik['Model']}, F1 {knn_terbaik['F1']:.3f}) menyamai atau "
          f"melampaui regresi logistik balanced (F1 {baris_lr['F1']:.3f}).")
```

**Pemeriksaan otomatis.**

```python
# =============================================
# Pemeriksaan otomatis — Langkah 3 dan 5
# =============================================
assert np.isclose(precision_m, precision_score(y_test, pred)) and \
       np.isclose(recall_m, recall_score(y_test, pred)) and \
       np.isclose(f1_m, f1_score(y_test, pred)), (
    "Perhitungan manual Langkah 3 tidak cocok dengan sklearn — periksa urutan tn, fp, fn, tp")
for _, b in baris_knn.iterrows():
    assert b["F1"] > 0, (
        f"{b['Model']} tidak menemukan satu pun transaksi janggal (F1 = 0) — "
        f"periksa data Langkah 1 dan Pipeline berpenskalaan")
print("Pemeriksaan otomatis lulus.")
```

Pada data lab ini, F1 k-NN berkisar ≈ 0,19 (k = 21) s.d. ≈ 0,27 (k = 3) dengan *recall* hanya 0,11–0,20, sedangkan regresi logistik *balanced* pada ambang 0,5 mencapai F1 ≈ 0,32 dengan *recall* ≈ 0,86 (tetapi *precision* hanya ≈ 0,20). Makin besar k, makin kuat suara mayoritas — *recall* k-NN turun.

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
n_tandai_f1   = int(terbaik_f1["TP"] + terbaik_f1["FP"])
def rp(x):
    """Format rupiah dengan titik ribuan, mis. Rp 72.900.000."""
    return f"Rp {x:,.0f}".replace(",", ".")

print(f"\nAmbang dengan biaya terendah : {terbaik_biaya['Ambang']:.2f} "
      f"({rp(terbaik_biaya['Total biaya (Rp)'])}; FN {terbaik_biaya['FN']:.0f}, "
      f"FP {terbaik_biaya['FP']:.0f})")
print(f"Ambang dengan F1 tertinggi   : {terbaik_f1['Ambang']:.2f} "
      f"(F1 {terbaik_f1['F1']:.4f}; {n_tandai_f1} transaksi ditandai; "
      f"{rp(terbaik_f1['Total biaya (Rp)'])})")

# Kesimpulan dihitung dari hasil
rasio_biaya = BIAYA_FN / BIAYA_FP
if terbaik_biaya["Ambang"] < terbaik_f1["Ambang"]:
    print(f"\nKedua ambang BERBEDA. Satu FN semahal {rasio_biaya:.0f} FP, sehingga ambang "
          "biaya lebih RENDAH: lebih banyak transaksi diperiksa demi")
    print(f"menangkap {terbaik_biaya['Recall']:.0%} transaksi janggal (ambang F1 hanya "
          f"{terbaik_f1['Recall']:.0%}). F1 menimbang FP dan FN setara dan tidak mengenal rupiah.")
elif terbaik_biaya["Ambang"] > terbaik_f1["Ambang"]:
    print("\nKedua ambang BERBEDA: ambang biaya lebih TINGGI daripada ambang F1 — "
          "periksa kembali BIAYA_FN dan BIAYA_FP.")
else:
    print("\nKedua ambang SAMA pada grid ini.")
```

**Tulis kesimpulan:** apakah kedua ambang itu sama? Bila berbeda, mana yang sebaiknya dipakai dan mengapa?

Pada data lab ini, ambang biaya terendah adalah 0,30 (5 FN dan 958 FP, total Rp 72,9 juta; *recall* ≈ 0,97), sedangkan F1 tertinggi (≈ 0,44) dicapai pada ambang 0,75 dengan 224 transaksi ditandai — tetapi dengan 63 transaksi janggal lolos (*recall* ≈ 0,57), total biayanya Rp 322,1 juta. Perhatikan pula bahwa kurva F1 cukup datar di sekitar 0,65–0,85 (F1 ≈ 0,42–0,44): memilih ambang hanya dari F1 tertinggi rentan terhadap selisih kecil.

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

roc_auc = roc_auc_score(y_test, prob)
pr_auc  = average_precision_score(y_test, prob)
print(f"ROC-AUC: {roc_auc:.4f}")
print(f"PR-AUC : {pr_auc:.4f}")
print(f"Proporsi positif (baseline PR): {y_test.mean():.4f}")
print(f"PR-AUC = {pr_auc / y_test.mean():.1f} × baseline; "
      f"selisih ROC-AUC − PR-AUC = {roc_auc - pr_auc:.2f}")
```

**Pemeriksaan otomatis.**

```python
# =============================================
# Pemeriksaan otomatis — Langkah 6 dan 7
# =============================================
assert n_tandai_f1 >= 30, (
    f"Ambang F1 tertinggi hanya menandai {n_tandai_f1} transaksi — terlalu sedikit untuk "
    f"disimpulkan; periksa data Langkah 1")
assert terbaik_biaya["Ambang"] < terbaik_f1["Ambang"], (
    f"Dengan FN {rasio_biaya:.0f}× lebih mahal daripada FP, ambang biaya terendah seharusnya "
    f"lebih rendah daripada ambang F1 tertinggi — periksa BIAYA_FN dan BIAYA_FP")
assert pr_auc > 2 * y_test.mean(), (
    "PR-AUC seharusnya jauh di atas baseline proporsi positif — periksa model Langkah 3")
assert roc_auc - pr_auc > 0.2, (
    f"Pada data tak seimbang ini ROC-AUC seharusnya jauh lebih tinggi daripada PR-AUC "
    f"(sekarang selisihnya {roc_auc - pr_auc:.2f})")
print("Pemeriksaan otomatis lulus.")
```

> **Perhatikan selisih ROC-AUC dan PR-AUC.** Pada data lab ini (6,0% positif), ROC-AUC ≈ 0,90 — tampak sangat baik — sementara PR-AUC hanya ≈ 0,48, walaupun itu sudah ≈ 8 kali *baseline*-nya (0,06). PR-AUC-lah yang lebih jujur menggambarkan kegunaan model: pada ambang 0,5, dari setiap lima transaksi yang ditandai, hanya sekitar satu yang benar-benar janggal (*precision* ≈ 0,20).

---

## Tantangan Tambahan

### Tantangan 1 — Pengaruh `class_weight`

Latih regresi logistik dengan dan tanpa `class_weight="balanced"`. Bandingkan *precision*, *recall*, dan ambang optimumnya. Apa yang sebenarnya dilakukan `class_weight`? Tanpa `class_weight`, probabilitas prediksi bergeser ke bawah, sehingga ambang biaya terendah bisa jatuh tepat di tepi grid (0,05); bila demikian, perluas grid ke bawah (mis. `np.arange(0.01, 0.96, 0.01)`) sebelum menyebutnya "optimum".

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
- [ ] Ketiga sel **Pemeriksaan otomatis** lulus
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 7](../03-modules/week-07-klasifikasi-dan-metriknya.md)
2. [Bab 7 buku ajar](../06-buku-ajar/bab-07-klasifikasi-dan-metriknya.md)
3. Saito, T., & Rehmsmeier, M. (2015). The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets. *PLoS ONE*, 10(3), e0118432. <https://doi.org/10.1371/journal.pone.0118432>
4. Dokumentasi scikit-learn — *Classification metrics*. <https://scikit-learn.org/stable/modules/model_evaluation.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
