# Lab 13: Jaringan Saraf Tiruan

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 13 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-12 |
| Durasi | 100 menit |
| Prasyarat | Lab 12 selesai |
| Bobot | 1,875% (Observasi, Sub-CPMK082-1) |
| Diuji pada | scikit-learn 1.6 dan 1.9, pandas 2.2 dan 3.0 (Oktober 2026) |

---

## Tujuan Praktikum

1. Menghitung satu langkah maju dan satu langkah mundur secara manual.
2. Melatih `MLPClassifier`, membaca kurva *loss*-nya, dan mengenali kapan `early_stopping` menipu.
3. Menguji pengaruh laju pembelajaran.
4. **Membandingkan MLP dengan *Random Forest*** — serta *gradient boosting* dan *baseline* regresi logistik — pada data tabular yang sama, menilai selisihnya **secara berpasangan per lipatan**, dan melaporkan hasilnya dengan jujur.

---

## Persiapan

1. Buat notebook baru bernama `NIM_Nama_Lab13.ipynb`.
2. Jalankan **sel pembuka baku** di [Lampiran D](../06-buku-ajar/lampiran.md#lampiran-d-sel-pembuka-baku) — mengimpor pustaka, mencatat versi, dan menetapkan `RANDOM_STATE = 42`. Seluruh langkah di bawah mengandaikan sel itu sudah dijalankan.
3. **Data:** data kredit UMKM pada Langkah 3–8 adalah **data sintetis (simulasi)** yang meniru pola pengajuan kredit UMKM di Indonesia; **bukan data resmi BPS/lembaga** mana pun (termasuk bank atau OJK). Data dibangkitkan pada Langkah 3: 5.000 UMKM dengan sekitar 11% berlabel gagal bayar — kelas **tak seimbang**, dan ini penting untuk Langkah 5. Label dibangkitkan dari sebuah **rumus logistik** (omzet kecil, usaha yang masih muda, rasio utang tinggi, dan riwayat telat bayar menaikkan peluang gagal bayar). Rumus itu adalah **asumsi ilustratif**, bukan temuan empiris; `jumlah_pegawai`, `usia_pemilik`, `jenis_usaha`, dan `wilayah` sengaja **tidak** ikut menentukan label.
4. Kerjakan Langkah 1–2 dengan kalkulator lebih dahulu, lalu cocokkan dengan keluaran kode.

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
print(f"\nδ_h1 = δ_out·v1·h1(1-h1) = {delta_h1:.4f}")
print(f"δ_h2 = δ_out·v2·h2(1-h2) = {delta_h2:.4f}")

# Pembaruan bobot
v1_baru = v1 - eta * dL_dv1
v2_baru = v2 - eta * dL_dv2
w11_baru = w11 - eta * delta_h1 * x1

def arah(lama, baru):
    return "naik" if baru > lama else "turun"

print(f"\nv1: {v1} -> {v1_baru:.4f}   ({arah(v1, v1_baru)})")
print(f"v2: {v2} -> {v2_baru:.4f}   ({arah(v2, v2_baru)})")
print(f"w11: {w11} -> {w11_baru:.4f}   ({arah(w11, w11_baru)})")
posisi = "di bawah" if y_hat < y_target else "di atas"
print(f"Prediksi ({y_hat:.4f}) {posisi} target ({y_target}), sehingga pembaruan "
      f"mendorong ŷ {'naik' if y_hat < y_target else 'turun'}.")

# Verifikasi: apakah loss turun setelah pembaruan bobot keluaran (v1, v2)?
z_out_baru = v1_baru*h1 + v2_baru*h2 + c
y_hat_baru = sigmoid(z_out_baru)
loss_baru = (y_target - y_hat_baru) ** 2
print(f"\nSebelum: ŷ={y_hat:.4f}, loss={loss:.4f}")
print(f"Sesudah: ŷ={y_hat_baru:.4f}, loss={loss_baru:.4f}")
print("Loss turun:", loss_baru < loss)
```

> **Bentuk soal ini muncul pada UAS.** Kerjakan dengan kalkulator lebih dahulu; angka dipilih agar dapat dihitung tangan.
>
> **Konvensi pembulatan** (sama di Lab 13, [Bab 12 §12.4.2](../06-buku-ajar/bab-12-pengantar-jaringan-saraf-tiruan.md#1242-backpropagation--perhitungan-manual), dan [Modul Minggu 13](../03-modules/week-13-pengantar-jaringan-saraf-tiruan.md)): setiap nilai dihitung dengan presisi penuh dari nilai sebelumnya, lalu **ditampilkan dalam 4 desimal**. Hasilnya: ŷ = 0,6847; ∂L/∂ŷ = −0,6305; σ′ = 0,2159; δ_out = −0,1361; ∂L/∂v₁ = −0,0847; ∂L/∂v₂ = −0,0782; δ_h1 = −0,0192. Bila Anda membulatkan di setiap langkah, digit keempat dapat bergeser ±0,0001 — misalnya −2 × 0,3153 = −0,6306, sedangkan presisi penuh memberi −0,6305.

**Pemeriksaan otomatis.** Sel berikut harus lulus tanpa `AssertionError`; bila gagal, pesannya menunjukkan apa yang perlu diperiksa. Sel ini juga memperkenalkan **pemeriksaan gradien** (*gradient checking*): gradien hasil *backpropagation* dicocokkan dengan turunan numerik (beda hingga), cara baku untuk memastikan aturan rantai sudah diterapkan dengan benar.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 1 dan 2
# =============================================
def loss_dari(v1_, v2_, w11_):
    # Loss satu contoh sebagai fungsi tiga bobot (bobot lain tetap)
    h1_ = sigmoid(w11_*x1 + w21*x2 + b1)
    y_hat_ = sigmoid(v1_*h1_ + v2_*h2 + c)
    return (y_target - y_hat_) ** 2

eps = 1e-6   # langkah kecil untuk turunan numerik (beda tengah)
num_v1  = (loss_dari(v1 + eps, v2, w11) - loss_dari(v1 - eps, v2, w11)) / (2 * eps)
num_v2  = (loss_dari(v1, v2 + eps, w11) - loss_dari(v1, v2 - eps, w11)) / (2 * eps)
num_w11 = (loss_dari(v1, v2, w11 + eps) - loss_dari(v1, v2, w11 - eps)) / (2 * eps)
print(f"∂L/∂v1 : backprop {dL_dv1:.6f} | numerik {num_v1:.6f}")
print(f"∂L/∂v2 : backprop {dL_dv2:.6f} | numerik {num_v2:.6f}")
print(f"∂L/∂w11: backprop {delta_h1 * x1:.6f} | numerik {num_w11:.6f}")

assert abs(num_v1 - dL_dv1) < 1e-6 and abs(num_v2 - dL_dv2) < 1e-6, (
    "Gradien bobot keluaran tidak cocok dengan turunan numerik — periksa δ_out = ∂L/∂ŷ · ŷ(1-ŷ)")
assert abs(num_w11 - delta_h1 * x1) < 1e-6, (
    "Gradien w11 tidak cocok dengan turunan numerik — periksa δ_h1 = δ_out · v1 · h1(1-h1)")
assert loss_baru < loss, (
    "Loss harus turun setelah satu langkah pembaruan — periksa tanda pada w ← w − η·∂L/∂w")
assert abs(y_hat - 0.6847) < 5e-5 and abs(delta_out - (-0.1361)) < 5e-5, (
    "Angka berbeda dari contoh terhitung Bab 12 §12.4.2 — periksa bobot awal di Langkah 1")
print("Pemeriksaan otomatis lulus.")
```

### LANGKAH 3: Data Sintetis Kredit UMKM dan Lipatan Validasi Silang

> **Data sintetis (simulasi)** yang meniru pola pengajuan kredit UMKM di Indonesia; bukan data resmi BPS/lembaga. Sekitar 11% pengajuan berlabel gagal bayar.

```python
# =============================================
# LANGKAH 3: Data SINTETIS kredit UMKM (≈ 11% gagal bayar)
# (simulasi, bukan data resmi BPS/lembaga)
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

# Aturan pembangkit label (asumsi ilustratif): rumus LOGISTIK yang mulus.
# Omzet kecil, usaha muda, rasio utang tinggi, dan riwayat telat menaikkan peluang
# gagal bayar; jumlah_pegawai, usia_pemilik, jenis_usaha, wilayah TIDAK ikut menentukan.
logit = (-1.8 - 0.021 * df["omzet_jt"] - 0.15 * df["lama_usaha_thn"]
         + 2.7 * df["rasio_utang"] + 0.40 * df["riwayat_telat"])
df["gagal_bayar"] = rng.binomial(1, 1 / (1 + np.exp(-logit)))

X = df.drop(columns=["gagal_bayar"]); y = df["gagal_bayar"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE)

print("Dimensi:", df.shape, "| Proporsi positif:", round(float(y.mean()), 3))
```

Langkah 5, 7, dan 8 membandingkan model dengan validasi silang. Agar adil, semuanya memakai **lipatan yang sama** (`CV`), sehingga skor dua model pada lipatan ke-*i* **berpasangan** — dinilai pada baris uji yang persis sama. Fungsi berikut menghitung selisih berpasangan itu; alasannya dijelaskan di Langkah 8.

```python
# =============================================
# LANGKAH 3 (lanjutan): Lipatan bersama dan alat pembanding berpasangan
# =============================================
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

> Seluruh simpangan baku skor lipatan di lab ini memakai **`ddof=1`** (simpangan baku sampel), sama dengan `pd.Series.std()`.

### LANGKAH 4: MLP dengan scikit-learn

```python
# =============================================
# LANGKAH 4: MLPClassifier — penskalaan WAJIB
# =============================================
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import roc_auc_score
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
        alpha=1.0,               # regularisasi L2 kuat: pengendali overfitting utama di sini
        learning_rate_init=1e-3, max_iter=500,
        early_stopping=False,    # SENGAJA dimatikan — alasannya dibuktikan di Langkah 5
        n_iter_no_change=20,     # berhenti bila loss LATIH tidak turun > tol selama 20 iterasi
        random_state=RANDOM_STATE)),
])

t0 = time.time()
mlp.fit(X_train, y_train)
waktu_mlp = time.time() - t0

clf = mlp.named_steps["clf"]
prob_mlp = mlp.predict_proba(X_test)[:, 1]
auc_mlp = roc_auc_score(y_test, prob_mlp)
print(f"MLP — waktu latih: {waktu_mlp:.2f} s")
print(f"MLP — ROC-AUC uji: {auc_mlp:.4f}")
print(f"MLP — iterasi    : {clf.n_iter_} dari batas {clf.max_iter}",
      "(berhenti sendiri: loss latih tidak lagi turun)" if clf.n_iter_ < clf.max_iter
      else "(batas iterasi tercapai)")
```

**Konfigurasi Langkah 4** inilah yang dipakai lagi melalui `clone` di Langkah 5 (sebagai pembanding varian `early_stopping=True`), Langkah 7 (sama persis, hanya tanpa penskalaan), dan Langkah 8 (sama persis). Dua pilihannya berbeda dari contoh umum:

- `alpha=1.0` (bawaan scikit-learn `1e-4`): regularisasi L2 yang lebih kuat menjadi pengendali *overfitting* utama pada data berderau ini.
- `early_stopping=False`: pada data dengan 11% positif, `early_stopping` bawaan scikit-learn **tidak dapat diandalkan** — Langkah 5 membuktikannya. Pelatihan tetap berhenti sendiri: `n_iter_no_change=20` menghentikannya bila *loss* latih tidak lagi turun.

Pada data lab ini, MLP berhenti sendiri setelah ±136 iterasi dengan ROC-AUC uji ≈ 0,735 (waktu latih bergantung pada mesin).

### LANGKAH 5: Membaca Kurva *Loss* — dan Jebakan `early_stopping`

Dengan `early_stopping=True`, `MLPClassifier` menyisihkan sebagian data latih (`validation_fraction`) sebagai data validasi, **memantau akurasinya** — bukan *loss*, bukan ROC-AUC — lalu di akhir pelatihan **memulihkan bobot dari iterasi dengan akurasi validasi tertinggi**. Sel berikut menjalankan varian Langkah 4 dengan `early_stopping=True` pada kelima lipatan `CV` dan membandingkannya dengan konfigurasi Langkah 4.

```python
# =============================================
# LANGKAH 5: Kurva loss dan jebakan early_stopping pada data tak seimbang
# =============================================
import matplotlib.pyplot as plt
from sklearn.base import clone
from sklearn.model_selection import cross_val_score, cross_validate

# Varian Langkah 4 yang hanya berbeda pada early_stopping
mlp_es = clone(mlp).set_params(clf__early_stopping=True, clf__validation_fraction=0.15)
hasil_es = cross_validate(mlp_es, X_train, y_train, cv=CV, scoring="roc_auc",
                          return_estimator=True, n_jobs=-1)
skor_mlp_cv = cross_val_score(mlp, X_train, y_train, cv=CV,
                              scoring="roc_auc", n_jobs=-1)   # konfigurasi Langkah 4

proporsi_mayoritas = 1 - y_train.mean()   # akurasi bila selalu menebak "lancar"

fig, ax = plt.subplots(1, 2, figsize=(13, 4.5))
ax[0].plot(clf.loss_curve_)
ax[0].set_xlabel("Iterasi"); ax[0].set_ylabel("Loss latih (termasuk penalti L2)")
ax[0].set_title(f"Kurva loss MLP Langkah 4 ({clf.n_iter_} iterasi)")

rekap = []
for i, (est, auc_es, auc_l4) in enumerate(
        zip(hasil_es["estimator"], hasil_es["test_score"], skor_mlp_cv), start=1):
    akurasi_val = np.asarray(est.named_steps["clf"].validation_scores_)
    ax[1].plot(akurasi_val, label=f"Lipatan {i}")
    rekap.append({"Lipatan": i,
                  "Iterasi": len(akurasi_val),
                  "Bobot dari iterasi": int(akurasi_val.argmax()) + 1,
                  "Akurasi val. maks": akurasi_val.max(),
                  "Rentang akurasi val.": akurasi_val.max() - akurasi_val.min(),
                  "ROC-AUC early_stopping": auc_es,
                  "ROC-AUC Langkah 4": auc_l4})
ax[1].axhline(proporsi_mayoritas, color="black", ls="--",
              label="Selalu menebak 'lancar'")
ax[1].set_xlabel("Iterasi"); ax[1].set_ylabel("Akurasi validasi")
ax[1].set_title("early_stopping=True: akurasi validasi per lipatan")
ax[1].legend(fontsize=8)
plt.tight_layout(); plt.show()

rekap = pd.DataFrame(rekap)
print(rekap.round(4).to_string(index=False))

# --- Kesimpulan dihitung dari hasil ---
n_iter1 = int((rekap["Bobot dari iterasi"] == 1).sum())
n_bawah = int((rekap["ROC-AUC early_stopping"] < 0.5).sum())
print(f"\nAkurasi bila selalu menebak 'lancar': {proporsi_mayoritas:.4f}")
print(f"early_stopping=True : ROC-AUC CV {rekap['ROC-AUC early_stopping'].mean():.4f}; "
      f"{n_bawah} dari {len(rekap)} lipatan di bawah 0,5; "
      f"bobot iterasi 1 dipulihkan pada {n_iter1} lipatan")
print(f"Konfigurasi Langkah 4: ROC-AUC CV {skor_mlp_cv.mean():.4f} "
      f"(lipatan terendah {skor_mlp_cv.min():.4f})")
if n_iter1 > 0:
    print("Kesimpulan: akurasi validasi (nyaris) datar di sekitar proporsi kelas mayoritas, "
          "sehingga early_stopping tidak dapat membedakan model yang belajar dari yang "
          f"tidak; pada {n_iter1} dari {len(rekap)} lipatan yang dipulihkan adalah bobot "
          "iterasi PERTAMA.")
else:
    print("Kesimpulan: tidak ada lipatan yang memulihkan bobot iterasi pertama; tetap "
          "bandingkan ROC-AUC kedua konfigurasi sebelum memilih.")
```

| Pola kurva | Diagnosis |
|------------|-----------|
| Turun mantap lalu mendatar | Normal |
| Naik-turun tajam | Laju pembelajaran terlalu besar |
| Turun sangat lambat | Laju terlalu kecil, atau data belum diskalakan |
| Latih terus turun, validasi naik | *Overfitting* |
| Akurasi validasi datar di sekitar proporsi kelas mayoritas | `early_stopping` "buta" — matikan dan andalkan regularisasi `alpha`, atau pantau metrik lain (*log-loss*, ROC-AUC) |

> **Yang terjadi pada data lab ini** (hasil sama pada scikit-learn 1.6 dan 1.9): pada **kelima** lipatan, akurasi validasi benar-benar datar di 0,8875 sejak iterasi pertama — persis akurasi menebak "lancar" untuk semua pengajuan. Karena akurasi itu tidak pernah melampaui nilai iterasi pertama, pelatihan berhenti setelah 22 iterasi dan bobot yang dipulihkan adalah **bobot iterasi 1** — model yang hampir belum belajar. ROC-AUC kelima lipatan **di bawah 0,5** (rerata ≈ 0,443, lebih buruk daripada tebakan acak), sedangkan konfigurasi Langkah 4 memperoleh ≈ 0,680. Menaikkan `n_iter_no_change` tidak menolong: sampai 100 pun hasilnya sama, karena akurasinya memang tidak pernah bergerak. Dengan regularisasi lemah (`alpha=1e-4`) akurasi validasi sesekali naik sedikit, tetapi tetap tidak dapat diandalkan: dengan `n_iter_no_change=20`, tiga dari lima lipatan masih di bawah 0,5; dengan 50 atau 100, dua dari lima.

**Tulis pembahasan:** (a) mengapa akurasi validasi hampir tidak bergerak pada data 11% positif? (b) Mengapa ROC-AUC tetap dapat membedakan model yang belajar dari yang tidak, sedangkan akurasi tidak?

### LANGKAH 6: Pengaruh Laju Pembelajaran

Langkah ini **sengaja** memakai regularisasi lemah (`alpha` bawaan `1e-4`), batas 200 iterasi, dan tanpa `early_stopping`, agar pengaruh laju pembelajaran terhadap *loss* latih terlihat jelas. Peringatan `ConvergenceWarning` untuk dua laju terkecil wajar di sini: batas 200 iterasi tercapai sebelum *loss* berhenti turun.

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
    kurva = np.asarray(m.named_steps["clf"].loss_curve_)
    ax.plot(kurva, label=f"lr = {lr}", color=warna)
    baris.append({"Laju": lr, "Iterasi": len(kurva),
                  "Loss iter. 20": kurva[19], "Loss akhir": kurva[-1],
                  "Kenaikan > 0,005": int((np.diff(kurva) > 0.005).sum()),
                  "ROC-AUC uji": roc_auc_score(y_test, m.predict_proba(X_test)[:, 1])})

ax.set_xlabel("Iterasi"); ax.set_ylabel("Loss latih")
ax.set_title("Pengaruh laju pembelajaran terhadap konvergensi")
ax.legend(); plt.tight_layout(); plt.show()

hasil_lr = pd.DataFrame(baris).set_index("Laju")
print(hasil_lr.round(4).to_string())

# --- Kesimpulan dihitung dari hasil ---
lr_goyang   = hasil_lr["Kenaikan > 0,005"].idxmax()
lr_lambat   = hasil_lr["Loss iter. 20"].idxmax()
lr_loss_min = hasil_lr["Loss akhir"].idxmin()
lr_auc_maks = hasil_lr["ROC-AUC uji"].idxmax()
print(f"\nPaling sering naik-turun : lr = {lr_goyang} "
      f"({hasil_lr.loc[lr_goyang, 'Kenaikan > 0,005']} kenaikan > 0,005) -> terlalu besar")
print(f"Paling lambat turun      : lr = {lr_lambat} "
      f"(loss iterasi 20 = {hasil_lr.loc[lr_lambat, 'Loss iter. 20']:.4f}) -> terlalu kecil")
print(f"Loss latih akhir terendah: lr = {lr_loss_min} | ROC-AUC uji tertinggi: lr = {lr_auc_maks}")
if lr_loss_min != lr_auc_maks:
    print("Loss latih terendah TIDAK memberi kinerja uji terbaik: dengan regularisasi lemah "
          "dan tanpa early stopping, model itu ikut menghafal derau data latih (overfitting).")
else:
    print("Pada data ini, laju dengan loss latih terendah juga terbaik pada data uji.")
```

> **Pada data lab ini** (hasil sama pada scikit-learn 1.6 dan 1.9): `lr = 0.1` naik-turun paling sering (6 kenaikan > 0,005) dan berhenti pada iterasi 59 di *loss* ≈ 0,29, karena *loss*-nya tidak lagi membaik selama 10 iterasi berturut-turut (`n_iter_no_change` bawaan). `lr = 0.0001` turun mulus tetapi paling lambat (*loss* ≈ 0,35 pada iterasi 20 dan masih ≈ 0,31 setelah 200 iterasi). `lr = 0.001` mencapai *loss* latih **terendah** (≈ 0,18) — tetapi ROC-AUC ujinya justru **terendah** (≈ 0,63, dibandingkan ≈ 0,65 untuk `lr = 0.1` dan ≈ 0,71 untuk `lr = 0.0001`). *Loss* latih yang rendah bukan tujuan; yang dinilai adalah kinerja pada data yang belum pernah dilihat.

**Tulis pembahasan:** laju mana yang terlalu besar, dan bagaimana terlihat pada kurvanya? Mengapa laju dengan *loss* latih terendah tidak menghasilkan ROC-AUC uji tertinggi? Apa yang akan Anda ubah agar laju itu tidak *overfit* (petunjuk: Langkah 4)?

### LANGKAH 7: Membuktikan Penskalaan Wajib

```python
# =============================================
# LANGKAH 7: MLP tanpa penskalaan — konfigurasi lain PERSIS sama dengan Langkah 4
# =============================================
mlp_tanpa = Pipeline([("pra", pra(False)), ("clf", clone(clf))])
mlp_tanpa.fit(X_train, y_train)
auc_tanpa = roc_auc_score(y_test, mlp_tanpa.predict_proba(X_test)[:, 1])

print(f"Iterasi    : DENGAN penskalaan {clf.n_iter_} | TANPA "
      f"{mlp_tanpa.named_steps['clf'].n_iter_}")
print(f"ROC-AUC uji: DENGAN {auc_mlp:.4f} | TANPA {auc_tanpa:.4f} | "
      f"selisih {auc_mlp - auc_tanpa:+.4f}")

# Satu pembagian uji belum cukup sebagai bukti — bandingkan per lipatan (berpasangan)
skor_tanpa_cv = cross_val_score(mlp_tanpa, X_train, y_train, cv=CV,
                                scoring="roc_auc", n_jobs=-1)
b_skala = banding_berpasangan(skor_mlp_cv, skor_tanpa_cv)
print(f"\nSelisih per lipatan (dengan − tanpa): {np.round(b_skala['d'], 4)}")
print(f"d̄ = {b_skala['d_bar']:+.4f} | s_d = {b_skala['s_d']:.4f} | "
      f"SE = {b_skala['SE']:.4f} | searah {b_skala['searah']}/{b_skala['k']}")
if b_skala["bermakna"] and b_skala["d_bar"] > 0:
    print("Kesimpulan: penskalaan menaikkan ROC-AUC secara bermakna "
          "(|d̄| > 2·SE dan searah di sebagian besar lipatan).")
elif b_skala["bermakna"]:
    print("Kesimpulan: tanpa penskalaan justru lebih baik secara bermakna — periksa pra().")
else:
    print("Kesimpulan: selisih belum bermakna menurut aturan |d̄| > 2·SE.")
```

> **Pada data lab ini** (hasil sama pada scikit-learn 1.6 dan 1.9): tanpa penskalaan, MLP butuh ±404 iterasi (dengan penskalaan ±136) dan ROC-AUC-nya lebih rendah di **kelima** lipatan (d̄ ≈ +0,024; SE ≈ 0,004). Selisih itu tidak dramatis, tetapi konsisten — dan dibayar dengan pelatihan tiga kali lebih lama.

**Pemeriksaan otomatis.** Sel berikut mengunci pelajaran Langkah 5–7.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 5 sampai 7
# =============================================
assert skor_mlp_cv.mean() > 0.60 and skor_mlp_cv.min() > 0.55, (
    f"ROC-AUC CV MLP Langkah 4 ({skor_mlp_cv.mean():.3f}, lipatan terendah "
    f"{skor_mlp_cv.min():.3f}) harus jelas di atas 0,5 (tebakan acak) — "
    f"periksa alpha dan early_stopping di Langkah 4")
assert skor_mlp_cv.mean() - rekap["ROC-AUC early_stopping"].mean() > 0.05, (
    "Konfigurasi Langkah 4 seharusnya jelas lebih baik daripada varian early_stopping=True "
    "pada data tak seimbang ini — periksa set_params pada mlp_es")
assert lr_goyang == 0.1 and hasil_lr.loc[0.1, "Kenaikan > 0,005"] >= 3, (
    "Laju 0,1 seharusnya paling sering naik-turun — periksa learning_rate_init di Langkah 6")
assert lr_lambat == 1e-4, (
    "Laju 0,0001 seharusnya paling lambat menurunkan loss — periksa Langkah 6")
assert hasil_lr.loc[1e-4, "ROC-AUC uji"] - hasil_lr.loc[1e-3, "ROC-AUC uji"] > 0.03, (
    "Pada Langkah 6, laju 0,001 (loss latih terendah) seharusnya overfit sehingga ROC-AUC "
    "ujinya lebih rendah daripada laju 0,0001 — periksa alpha dan max_iter")
assert b_skala["bermakna"] and b_skala["d_bar"] > 0.01, (
    f"Penskalaan seharusnya menaikkan ROC-AUC secara bermakna; sekarang d̄ = "
    f"{b_skala['d_bar']:+.4f}, SE = {b_skala['SE']:.4f} — periksa pra(True)/pra(False)")
print("Pemeriksaan otomatis lulus.")
```

### LANGKAH 8: MLP vs *Random Forest* — Bagian Utama Lab Ini

```python
# =============================================
# LANGKAH 8: Perbandingan yang jujur pada data tabular
# =============================================
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

kandidat = {
    "MLP (64, 32)": clone(mlp),                    # konfigurasi Langkah 4, persis sama
    "Random Forest": Pipeline([
        ("pra", pra(False)),
        ("clf", RandomForestClassifier(n_estimators=300,
                                       random_state=RANDOM_STATE, n_jobs=-1))]),
    "Gradient Boosting": Pipeline([
        ("pra", pra(False)),
        ("clf", HistGradientBoostingClassifier(max_iter=300, early_stopping=True,
                                               random_state=RANDOM_STATE))]),
    "Regresi logistik (baseline)": Pipeline([
        ("pra", pra(True)),
        ("clf", LogisticRegression(max_iter=1000))]),
}

skor_lipatan, baris = {}, []
for nama, pipa in kandidat.items():
    t0 = time.time()
    skor = cross_val_score(pipa, X_train, y_train, cv=CV,
                           scoring="roc_auc", n_jobs=-1)
    skor_lipatan[nama] = skor                                  # untuk uji berpasangan
    baris.append({"Model": nama, "ROC-AUC": skor.mean(),
                  "Simpangan": skor.std(ddof=1), "Waktu (s)": time.time() - t0})

tabel = pd.DataFrame(baris).sort_values("ROC-AUC", ascending=False).reset_index(drop=True)
print(tabel.round(4).to_string(index=False))

# --- Selisih berpasangan: model peringkat 1 dikurangi tiap model lain ---
juara = tabel.loc[0, "Model"]
banding = []
for nama in tabel["Model"][1:]:
    b = banding_berpasangan(skor_lipatan[juara], skor_lipatan[nama])
    banding.append({"Dibandingkan dengan": nama, "d̄": b["d_bar"], "s_d": b["s_d"],
                    "SE": b["SE"], "Searah": f"{b['searah']}/{b['k']}",
                    "Bermakna": "ya" if b["bermakna"] else "tidak"})
print(f"\nSelisih berpasangan: '{juara}' dikurangi model lain (per lipatan)")
print(pd.DataFrame(banding).round(4).to_string(index=False))

kedua = tabel.loc[1, "Model"]
b12 = banding_berpasangan(skor_lipatan[juara], skor_lipatan[kedua])
print(f"\nPeringkat 1-2: d̄ = {b12['d_bar']:+.4f} | batas 2·SE = {2 * b12['SE']:.4f} "
      f"| searah {b12['searah']}/{b12['k']}")
print("Kesimpulan peringkat 1-2:",
      f"'{juara}' lebih baik secara bermakna daripada '{kedua}'" if b12["bermakna"]
      else "TIDAK DAPAT DISIMPULKAN mana yang lebih baik")

# --- Kesimpulan tentang MLP, dihitung dari hasil ---
w = tabel.set_index("Model")["Waktu (s)"]
pohon = max(["Random Forest", "Gradient Boosting"], key=lambda m: skor_lipatan[m].mean())
b_pohon = banding_berpasangan(skor_lipatan["MLP (64, 32)"], skor_lipatan[pohon])
b_base = banding_berpasangan(skor_lipatan["MLP (64, 32)"],
                             skor_lipatan["Regresi logistik (baseline)"])
if not b_pohon["bermakna"]:
    print(f"MLP vs {pohon}: selisih tidak bermakna (d̄ = {b_pohon['d_bar']:+.4f}).")
elif b_pohon["d_bar"] > 0:
    print(f"MLP vs {pohon}: MLP lebih baik secara bermakna (d̄ = {b_pohon['d_bar']:+.4f}).")
else:
    print(f"MLP vs {pohon}: {pohon} lebih baik secara bermakna (d̄ = {b_pohon['d_bar']:+.4f}).")
rasio = w["MLP (64, 32)"] / w["Regresi logistik (baseline)"]
if not b_base["bermakna"]:
    print(f"MLP vs baseline: selisih tidak bermakna (d̄ = {b_base['d_bar']:+.4f}), padahal "
          f"waktu MLP ±{rasio:.0f}× lebih lama -> JST tidak diperlukan pada data ini.")
elif b_base["d_bar"] > 0:
    print(f"MLP vs baseline: MLP lebih baik secara bermakna (d̄ = {b_base['d_bar']:+.4f}) "
          f"-> kapasitas non-linear MLP terpakai; nilai apakah sepadan dengan waktunya.")
else:
    print(f"MLP vs baseline: regresi logistik lebih baik secara bermakna "
          f"(d̄ = {b_base['d_bar']:+.4f}) -> pilih baseline.")
```

> **Mengapa berpasangan, dan mengapa SE?** Karena semua model dinilai pada lipatan yang **sama**, sebagian variasi skor berasal dari lipatannya sendiri (ada lipatan yang "mudah", ada yang "sulit") dan dialami semua model bersama-sama. Selisih per lipatan $d_i = \text{skor}_{A,i} - \text{skor}_{B,i}$ menghapus variasi bersama itu. Laporkan rerata $\bar d$, simpangan baku sampel $s_d$ (`ddof=1`), dan galat baku $SE = s_d/\sqrt{k}$ — ketidakpastian **rerata** selisih diukur oleh $SE$, bukan oleh simpangan baku skor masing-masing model. Rumus "simpangan gabungan" $\sqrt{s_1^2+s_2^2}$ **tidak dipakai**: rumus itu memperlakukan skor kedua model seolah-olah tidak berpasangan dan memakai simpangan baku (SD) alih-alih galat baku (SE).
>
> **Aturan praktis mata kuliah:** selisih dianggap bermakna bila $|\bar d| > 2 \cdot SE$ **dan** arahnya konsisten di sebagian besar lipatan (di lab ini: minimal 4 dari 5). Aturan ini hanya penyaring kasar: skor antarlipatan tidak benar-benar saling bebas (data latihnya tumpang-tindih), sehingga $SE$ cenderung terlalu kecil. Untuk analisis formal, gunakan *corrected resampled t-test* (Nadeau & Bengio, 2003).

> **Tulis kesimpulan yang jujur.** Kesimpulan yang dicetak di atas dihitung dari skor per lipatan; tuliskan apa adanya — bukan memaksa MLP menang, dan bukan pula memaksanya kalah. **Pada data lab ini** (scikit-learn 1.6 dan 1.9): regresi logistik dan MLP sama-sama memperoleh ROC-AUC CV ≈ 0,68 dengan selisih yang tidak bermakna, sedangkan *gradient boosting* (≈ 0,63) dan *Random Forest* (≈ 0,63) lebih rendah secara bermakna.
>
> Hasil ini **tidak bertentangan** dengan literatur. Grinsztajn et al. (2022) menemukan bahwa model berbasis pohon unggul pada data tabular **tipikal**, antara lain karena fungsi targetnya sering tidak mulus (*irregular*), sedangkan jaringan saraf cenderung menghasilkan fungsi yang terlalu mulus; selisihnya menyempit ketika fungsi target makin mulus. Label data sintetis Langkah 3 justru dibangkitkan dari rumus logistik yang **mulus** — keadaan yang menguntungkan regresi logistik dan MLP teregularisasi. Pada data nyata yang polanya tidak diketahui, hasilnya bisa berbalik; karena itulah perbandingan harus selalu dijalankan, bukan diandaikan.
>
> Pelajaran utamanya sama dengan [Bab 12 §12.6](../06-buku-ajar/bab-12-pengantar-jaringan-saraf-tiruan.md#126-kapan-jst-tidak-diperlukan): **bangun *baseline* lebih dahulu.** Di sini MLP tidak memberi apa pun di atas regresi logistik, padahal waktu latihnya jauh lebih lama dan hiperparameternya jauh lebih banyak.

**Pemeriksaan otomatis.**

```python
# =============================================
# Pemeriksaan otomatis — Langkah 8
# =============================================
assert (kandidat["MLP (64, 32)"].named_steps["clf"].get_params()
        == clf.get_params()), (
    "MLP di Langkah 8 harus memakai konfigurasi Langkah 4 yang persis sama (clone(mlp))")
s_mlp = skor_lipatan["MLP (64, 32)"]
assert s_mlp.mean() > 0.60 and s_mlp.min() > 0.55, (
    f"ROC-AUC CV MLP ({s_mlp.mean():.3f}, lipatan terendah {s_mlp.min():.3f}) harus jelas "
    f"di atas 0,5 — MLP yang lebih buruk daripada tebakan acak berarti pelatihannya gagal "
    f"(periksa early_stopping dan alpha di Langkah 4), bukan bahwa JST 'kalah'")
assert np.isclose(b12["SE"], pd.Series(b12["d"]).std() / np.sqrt(b12["k"])), (
    "SE harus = s_d/√k dengan s_d simpangan baku SAMPEL (ddof=1) dari selisih per lipatan")
print("Pemeriksaan otomatis lulus.")
```

---

## Tantangan Tambahan

### Tantangan 1 — Ukuran Jaringan

Bandingkan `hidden_layer_sizes` sebesar `(8,)`, `(64,)`, `(64, 32)`, dan `(256, 128, 64)`. Buat grafik ROC-AUC dan waktu latih terhadap jumlah parameter. Pada titik berapa penambahan kapasitas berhenti membantu?

### Tantangan 2 — Implementasi dari Nol

Implementasikan perseptron satu lapis dengan NumPy saja (tanpa `scikit-learn`) untuk mempelajari fungsi AND dan OR. Lalu coba XOR — tunjukkan bahwa perseptron tunggal **gagal**, dan bahwa MLP dengan satu lapis tersembunyi berhasil.

### Tantangan 3 — Kapan JST Menang

Buat data dengan hubungan non-linear yang rumit (misalnya `make_moons` atau `make_circles` dengan derau). Bandingkan MLP, regresi logistik, dan *Random Forest* di sana dengan `banding_berpasangan`. Pada jenis data apa MLP unggul, dan mengapa peringkatnya berbeda dari data tabular Langkah 8?

### Tantangan 4 — Fungsi Target yang Tidak Mulus

Ganti rumus `logit` Langkah 3 dengan aturan berambang, misalnya peluang gagal bayar tinggi hanya bila `rasio_utang > 0.45` **dan** `riwayat_telat >= 2`, atau bila `omzet_jt < 10`. Jalankan ulang Langkah 8. Apakah peringkat model berubah? Kaitkan dengan temuan Grinsztajn et al. (2022). Pada percobaan ini pemeriksaan otomatis dapat gagal karena datanya berubah; kembalikan rumus semula setelah selesai.

### Tantangan 5 — Laju Pembelajaran dengan Regularisasi Kuat

Ulangi Langkah 6 dengan `alpha=1.0` (seperti Langkah 4). Apakah perbedaan ROC-AUC uji antarlaju masih sebesar sebelumnya? Jelaskan peran regularisasi terhadap kepekaan model pada pilihan laju pembelajaran.

---

## Checklist Penyelesaian

- [ ] **Perhitungan manual** langkah maju, diverifikasi dengan kode
- [ ] **Perhitungan manual** langkah mundur dan pembaruan bobot, dengan konvensi pembulatan 4 desimal
- [ ] Dibuktikan bahwa *loss* turun setelah satu langkah pembaruan, dan gradien lolos pemeriksaan numerik
- [ ] Konfigurasi `MLPClassifier` Langkah 4 dijelaskan (`alpha`, `early_stopping`, `n_iter_no_change`)
- [ ] Kurva *loss* ditampilkan dan **didiagnosis**
- [ ] **Jebakan `early_stopping`** pada data tak seimbang ditunjukkan dan dijelaskan (akurasi validasi datar, bobot iterasi pertama)
- [ ] Tiga laju pembelajaran dibandingkan, termasuk mengapa *loss* latih terendah tidak memberi ROC-AUC uji tertinggi
- [ ] Dampak tidak adanya penskalaan ditunjukkan dengan angka (selisih berpasangan per lipatan)
- [ ] **MLP dibandingkan dengan *Random Forest*, *gradient boosting*, dan *baseline*** dengan lipatan yang sama
- [ ] **Kesimpulan memakai selisih berpasangan per lipatan** ($\bar d$, $s_d$ dengan `ddof=1`, $SE = s_d/\sqrt{k}$), bukan hanya rerata
- [ ] Waktu latih dilaporkan untuk tiap model
- [ ] **Kesimpulan jujur** tentang model mana yang lebih sesuai untuk data tabular ini
- [ ] Semua sel **Pemeriksaan otomatis** lulus
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 13](../03-modules/week-13-pengantar-jaringan-saraf-tiruan.md)
2. [Bab 12 buku ajar](../06-buku-ajar/bab-12-pengantar-jaringan-saraf-tiruan.md)
3. Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022). Why Do Tree-Based Models Still Outperform Deep Learning on Typical Tabular Data? *NeurIPS 2022 (Datasets and Benchmarks Track)*.
4. Nadeau, C., & Bengio, Y. (2003). Inference for the Generalization Error. *Machine Learning*, 52(3), 239–281.
5. Dokumentasi scikit-learn — *Neural network models*. <https://scikit-learn.org/stable/modules/neural_networks_supervised.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
