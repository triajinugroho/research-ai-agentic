# Lab 13: Jaringan Saraf Tiruan

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 13 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-12 |
| Durasi | 100 menit |
| Prasyarat | Lab 12 selesai |
| Bobot | 1,9% (Observasi) |

---

## Tujuan Praktikum

1. Menghitung satu langkah maju dan satu langkah mundur secara manual.
2. Melatih `MLPClassifier` dan membaca kurva *loss*-nya.
3. Menguji pengaruh laju pembelajaran.
4. **Membandingkan MLP dengan *Random Forest*** pada data tabular yang sama dan melaporkan hasilnya dengan jujur.

---

## Langkah-langkah

### LANGKAH 1: Perhitungan Manual — Langkah Maju

```python
# =============================================
# LANGKAH 1: Langkah maju jaringan 2-2-1 (MANUAL)
# =============================================
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Bobot awal
w11, w12 = 0.5, 0.3      # dari x1 ke h1, h2
w21, w22 = 0.2, 0.4      # dari x2 ke h1, h2
b1, b2   = 0.0, 0.0      # bias lapis tersembunyi
v1, v2   = 0.6, 0.7      # dari h1, h2 ke keluaran
c        = 0.0           # bias keluaran

# Satu contoh
x1, x2 = 1.0, 0.0
y_target = 1.0

# Lapis tersembunyi
z1 = w11*x1 + w21*x2 + b1
z2 = w12*x1 + w22*x2 + b2
h1, h2 = sigmoid(z1), sigmoid(z2)

# Lapis keluaran
z_out = v1*h1 + v2*h2 + c
y_hat = sigmoid(z_out)

print(f"z1 = {w11}·{x1} + {w21}·{x2} + {b1} = {z1:.4f}  ->  h1 = σ(z1) = {h1:.4f}")
print(f"z2 = {w12}·{x1} + {w22}·{x2} + {b2} = {z2:.4f}  ->  h2 = σ(z2) = {h2:.4f}")
print(f"z_out = {v1}·{h1:.4f} + {v2}·{h2:.4f} + {c} = {z_out:.4f}")
print(f"ŷ = σ(z_out) = {y_hat:.4f}")

loss = (y_target - y_hat) ** 2
print(f"\nLoss (MSE) = ({y_target} - {y_hat:.4f})² = {loss:.4f}")
```

### LANGKAH 2: Perhitungan Manual — Langkah Mundur

```python
# =============================================
# LANGKAH 2: Backpropagation (MANUAL)
# =============================================
eta = 0.1     # laju pembelajaran

# Gradien di lapis keluaran
dL_dyhat   = -2 * (y_target - y_hat)
dsig_zout  = y_hat * (1 - y_hat)
delta_out  = dL_dyhat * dsig_zout

print(f"∂L/∂ŷ        = -2({y_target} - {y_hat:.4f}) = {dL_dyhat:.4f}")
print(f"σ'(z_out)    = ŷ(1-ŷ) = {y_hat:.4f}·{1-y_hat:.4f} = {dsig_zout:.4f}")
print(f"δ_out        = {dL_dyhat:.4f} × {dsig_zout:.4f} = {delta_out:.4f}")

# Gradien bobot lapis keluaran
dL_dv1 = delta_out * h1
dL_dv2 = delta_out * h2
print(f"\n∂L/∂v1 = δ_out·h1 = {delta_out:.4f}·{h1:.4f} = {dL_dv1:.4f}")
print(f"∂L/∂v2 = δ_out·h2 = {delta_out:.4f}·{h2:.4f} = {dL_dv2:.4f}")

# Gradien merambat ke lapis tersembunyi
delta_h1 = delta_out * v1 * h1 * (1 - h1)
delta_h2 = delta_out * v2 * h2 * (1 - h2)
print(f"\nδ_h1 = δ_out·v1·h1(1-h1) = {delta_h1:.5f}")
print(f"δ_h2 = δ_out·v2·h2(1-h2) = {delta_h2:.5f}")

# Pembaruan bobot
v1_baru = v1 - eta * dL_dv1
v2_baru = v2 - eta * dL_dv2
w11_baru = w11 - eta * delta_h1 * x1
print(f"\nv1: {v1} -> {v1_baru:.4f}   (naik, karena prediksi masih di bawah target)")
print(f"v2: {v2} -> {v2_baru:.4f}")
print(f"w11: {w11} -> {w11_baru:.4f}")

# Verifikasi: apakah loss turun setelah pembaruan?
z_out_baru = v1_baru*h1 + v2_baru*h2 + c
y_hat_baru = sigmoid(z_out_baru)
loss_baru = (y_target - y_hat_baru) ** 2
print(f"\nSebelum: ŷ={y_hat:.4f}, loss={loss:.4f}")
print(f"Sesudah: ŷ={y_hat_baru:.4f}, loss={loss_baru:.4f}")
print("Loss turun:", loss_baru < loss)
```

> **Bentuk soal ini muncul pada UAS.** Kerjakan dengan kalkulator lebih dahulu; angka dipilih agar dapat dihitung tangan.

### LANGKAH 3: Data Tabular

```python
# =============================================
# LANGKAH 3: Data tabular nyata
# =============================================
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold

rng = np.random.default_rng(RANDOM_STATE)
n = 5000

df = pd.DataFrame({
    "omzet_jt":        rng.gamma(2.0, 20, size=n).round(1),
    "lama_usaha_thn":  rng.gamma(2.0, 2.5, size=n).round(1),
    "jumlah_pegawai":  rng.poisson(4, size=n) + 1,
    "rasio_utang":     rng.beta(2, 5, size=n).round(3),
    "riwayat_telat":   rng.poisson(0.8, size=n),
    "usia_pemilik":    rng.integers(21, 66, size=n),
    "jenis_usaha":     rng.choice(["Kuliner","Retail","Jasa","Produksi"], size=n),
    "wilayah":         rng.choice(["Jawa","Sumatera","Kalimantan","Sulawesi"],
                                  size=n, p=[0.5, 0.22, 0.15, 0.13]),
})

logit = (-1.8 - 0.021 * df["omzet_jt"] - 0.15 * df["lama_usaha_thn"]
         + 2.7 * df["rasio_utang"] + 0.40 * df["riwayat_telat"])
df["gagal_bayar"] = rng.binomial(1, 1 / (1 + np.exp(-logit)))

X = df.drop(columns=["gagal_bayar"]); y = df["gagal_bayar"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE)

print("Dimensi:", df.shape, "| Proporsi positif:", y.mean().round(3))
```

### LANGKAH 4: MLP dengan scikit-learn

```python
# =============================================
# LANGKAH 4: MLPClassifier — penskalaan WAJIB
# =============================================
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neural_network import MLPClassifier
import time

kol_kat = ["jenis_usaha", "wilayah"]
kol_num = [c for c in X.columns if c not in kol_kat]

def pra(skala=True):
    return ColumnTransformer([
        ("num", StandardScaler() if skala else "passthrough", kol_num),
        ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), kol_kat),
    ])

mlp = Pipeline([
    ("pra", pra(True)),
    ("clf", MLPClassifier(
        hidden_layer_sizes=(64, 32), activation="relu", solver="adam",
        alpha=1e-4, learning_rate_init=1e-3, max_iter=500,
        early_stopping=True, n_iter_no_change=20,
        validation_fraction=0.15, random_state=RANDOM_STATE)),
])

t0 = time.time()
mlp.fit(X_train, y_train)
waktu_mlp = time.time() - t0

from sklearn.metrics import roc_auc_score, f1_score
prob_mlp = mlp.predict_proba(X_test)[:, 1]
print(f"MLP — waktu latih: {waktu_mlp:.2f} s")
print(f"MLP — ROC-AUC    : {roc_auc_score(y_test, prob_mlp):.4f}")
print(f"MLP — iterasi     : {mlp.named_steps['clf'].n_iter_}")
```

### LANGKAH 5: Membaca Kurva *Loss*

```python
# =============================================
# LANGKAH 5: Kurva loss dan diagnosisnya
# =============================================
import matplotlib.pyplot as plt

clf = mlp.named_steps["clf"]
fig, ax = plt.subplots(1, 2, figsize=(13, 4.5))

ax[0].plot(clf.loss_curve_)
ax[0].set_xlabel("Iterasi"); ax[0].set_ylabel("Loss latih")
ax[0].set_title("Kurva loss")

if hasattr(clf, "validation_scores_") and clf.validation_scores_ is not None:
    ax[1].plot(clf.validation_scores_, color="tab:orange")
    ax[1].set_xlabel("Iterasi"); ax[1].set_ylabel("Skor validasi")
    ax[1].set_title(f"Skor validasi (early stopping pada iterasi {clf.n_iter_})")

plt.tight_layout(); plt.show()
```

| Pola kurva | Diagnosis |
|------------|-----------|
| Turun mantap lalu mendatar | Normal |
| Naik-turun tajam | Laju pembelajaran terlalu besar |
| Turun sangat lambat | Laju terlalu kecil, atau data belum diskalakan |
| Latih terus turun, validasi naik | *Overfitting* |

### LANGKAH 6: Pengaruh Laju Pembelajaran

```python
# =============================================
# LANGKAH 6: Tiga laju pembelajaran
# =============================================
fig, ax = plt.subplots(figsize=(9, 5))
baris = []

for lr, warna in [(1e-4, "tab:blue"), (1e-3, "tab:green"), (1e-1, "tab:red")]:
    m = Pipeline([
        ("pra", pra(True)),
        ("clf", MLPClassifier(hidden_layer_sizes=(64, 32), solver="adam",
                              learning_rate_init=lr, max_iter=200,
                              early_stopping=False, random_state=RANDOM_STATE)),
    ]).fit(X_train, y_train)
    kurva = m.named_steps["clf"].loss_curve_
    ax.plot(kurva, label=f"lr = {lr}", color=warna)
    baris.append({"Laju": lr, "Loss akhir": kurva[-1],
                  "ROC-AUC uji": roc_auc_score(y_test, m.predict_proba(X_test)[:, 1])})

ax.set_xlabel("Iterasi"); ax.set_ylabel("Loss latih")
ax.set_title("Pengaruh laju pembelajaran terhadap konvergensi")
ax.legend(); plt.tight_layout(); plt.show()

print(pd.DataFrame(baris).round(4).to_string(index=False))
```

**Tulis pembahasan:** laju mana yang terlalu besar? Bagaimana terlihat pada kurvanya?

### LANGKAH 7: Membuktikan Penskalaan Wajib

```python
# =============================================
# LANGKAH 7: MLP tanpa penskalaan
# =============================================
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    mlp_tanpa = Pipeline([
        ("pra", pra(False)),
        ("clf", MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=300,
                              random_state=RANDOM_STATE)),
    ]).fit(X_train, y_train)

auc_tanpa = roc_auc_score(y_test, mlp_tanpa.predict_proba(X_test)[:, 1])
print(f"MLP DENGAN penskalaan: {roc_auc_score(y_test, prob_mlp):.4f}")
print(f"MLP TANPA penskalaan : {auc_tanpa:.4f}")
print(f"Selisih              : {roc_auc_score(y_test, prob_mlp) - auc_tanpa:+.4f}")
```

### LANGKAH 8: MLP vs *Random Forest* — Bagian Utama Lab Ini

```python
# =============================================
# LANGKAH 8: Perbandingan yang jujur pada data tabular
# =============================================
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.model_selection import cross_val_score

CV = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

kandidat = {
    "MLP (64, 32)": Pipeline([
        ("pra", pra(True)),
        ("clf", MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500,
                              early_stopping=True, random_state=RANDOM_STATE))]),
    "Random Forest": Pipeline([
        ("pra", pra(False)),
        ("clf", RandomForestClassifier(n_estimators=300,
                                       random_state=RANDOM_STATE, n_jobs=-1))]),
    "Gradient Boosting": Pipeline([
        ("pra", pra(False)),
        ("clf", HistGradientBoostingClassifier(max_iter=300, early_stopping=True,
                                               random_state=RANDOM_STATE))]),
}

baris = []
for nama, pipa in kandidat.items():
    t0 = time.time()
    skor = cross_val_score(pipa, X_train, y_train, cv=CV,
                           scoring="roc_auc", n_jobs=-1)
    baris.append({"Model": nama, "ROC-AUC": skor.mean(),
                  "Simpangan": skor.std(), "Waktu (s)": time.time() - t0})

tabel = pd.DataFrame(baris).sort_values("ROC-AUC", ascending=False)
print(tabel.round(4).to_string(index=False))

t = tabel.reset_index(drop=True)
selisih = t.loc[0, "ROC-AUC"] - t.loc[1, "ROC-AUC"]
simp = np.sqrt(t.loc[0, "Simpangan"]**2 + t.loc[1, "Simpangan"]**2)
print(f"\nSelisih peringkat 1-2: {selisih:.4f} | Simpangan gabungan: {simp:.4f}")
print("Kesimpulan:", "perbedaan kemungkinan nyata" if selisih > simp
      else "TIDAK DAPAT DISIMPULKAN mana yang lebih baik")
```

> **Tulis kesimpulan yang jujur.** Bila *Random Forest* atau *gradient boosting* mengungguli MLP pada data tabular ini — yang sering terjadi — itulah temuannya, dan itu **sesuai dengan literatur** (Grinsztajn et al., 2022). Melaporkannya apa adanya adalah yang dinilai, bukan memaksa MLP menang.

---

## Tantangan Tambahan

### Tantangan 1 — Ukuran Jaringan

Bandingkan `hidden_layer_sizes` sebesar `(8,)`, `(64,)`, `(64, 32)`, dan `(256, 128, 64)`. Buat grafik ROC-AUC dan waktu latih terhadap jumlah parameter. Pada titik berapa penambahan kapasitas berhenti membantu?

### Tantangan 2 — Implementasi dari Nol

Implementasikan perseptron satu lapis dengan NumPy saja (tanpa `scikit-learn`) untuk mempelajari fungsi AND dan OR. Lalu coba XOR — tunjukkan bahwa perseptron tunggal **gagal**, dan bahwa MLP dengan satu lapis tersembunyi berhasil.

### Tantangan 3 — Kapan JST Menang

Buat data dengan hubungan non-linear yang rumit (misalnya `make_moons` atau `make_circles` dengan derau). Bandingkan MLP dan *Random Forest* di sana. Pada jenis data apa MLP unggul, dan mengapa berbeda dari data tabular Langkah 8?

---

## Checklist Penyelesaian

- [ ] **Perhitungan manual** langkah maju, diverifikasi dengan kode
- [ ] **Perhitungan manual** langkah mundur dan pembaruan bobot
- [ ] Dibuktikan bahwa *loss* turun setelah satu langkah pembaruan
- [ ] `MLPClassifier` dijalankan dengan `early_stopping`
- [ ] Kurva *loss* ditampilkan dan **didiagnosis**
- [ ] Tiga laju pembelajaran dibandingkan dan perbedaannya dijelaskan
- [ ] Dampak tidak adanya penskalaan ditunjukkan dengan angka
- [ ] **MLP dibandingkan dengan *Random Forest*** dengan lipatan yang sama
- [ ] Waktu latih dilaporkan untuk tiap model
- [ ] **Kesimpulan jujur** tentang model mana yang lebih sesuai untuk data tabular
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 13](../03-modules/week-13-pengantar-jaringan-saraf-tiruan.md)
2. [Bab 12 buku ajar](../06-buku-ajar/bab-12-pengantar-jaringan-saraf-tiruan.md)
3. Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022). Why Do Tree-Based Models Still Outperform Deep Learning on Tabular Data? *NeurIPS*.
4. Dokumentasi scikit-learn — *Neural network models*. <https://scikit-learn.org/stable/modules/neural_networks_supervised.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
