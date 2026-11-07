# Lab 14: Audit *Bias* dan *Model Card*

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 14 |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-13 |
| Durasi | 100 menit |
| Prasyarat | Lab 13 selesai; model proyek sudah ada |
| Bobot | 2,0% (Observasi, Sub-CPMK102-1) |

---

## Tujuan Praktikum

1. Mengukur kinerja model terpisah per kelompok, dan membaca angkanya dengan memperhitungkan ukuran sampel.
2. Menghitung empat ukuran *fairness* dan menunjukkan dengan angka ukuran mana yang **secara matematis** tidak dapat dipenuhi bersamaan.
3. Membuktikan bahwa menghapus atribut sensitif tidak menghapus ketimpangan ketika ada **fitur proksi**.
4. Menyusun *model card* yang lengkap dan jujur.

---

## Persiapan

1. Buka notebook baru di Google Colab dan simpan sebagai `NIM_Nama_Lab14.ipynb`.
2. Jalankan **sel pembuka baku** dari [Lab 1, Langkah 1](lab-01-setup-ekosistem-ml.md) (impor pustaka, pencatatan versi, `RANDOM_STATE = 42`). Semua langkah di bawah memakai variabel `RANDOM_STATE` dari sel itu.
3. Siapkan model proyek kelompok Anda; teknik di lab ini akan Anda terapkan padanya pada Langkah 8.

---

## Ketentuan Khusus Lab Ini

> **Audit dilakukan pada model proyek Anda sendiri**, bukan pada contoh. Contoh pada lab ini hanya untuk mempelajari tekniknya. Luaran yang dinilai adalah audit atas model kelompok Anda.

> **Tentang data contoh.** Data pada lab ini **sintetis** (dibangkitkan dengan `numpy`), dirancang meniru dua pola yang lazim pada data kredit UMKM di Indonesia: data terpusat di Jawa, dan akses layanan keuangan yang timpang antarwilayah. Angka-angkanya bukan statistik resmi.

---

## Langkah-langkah

### LANGKAH 1: Data dengan Ketimpangan Representasi dan Fitur Proksi

```python
# =============================================
# LANGKAH 1: Data yang mencerminkan ketimpangan nyata
# =============================================
import numpy as np, pandas as pd
rng = np.random.default_rng(RANDOM_STATE)

# Proporsi wilayah sengaja dibuat sangat timpang —
# mencerminkan keadaan data terbuka Indonesia yang terpusat di Jawa
wilayah_nama = ["Jawa", "Sumatera", "Kalimantan", "Sulawesi", "Papua"]
wilayah_prop = [0.62, 0.20, 0.09, 0.07, 0.02]
n = 10_000
wilayah = rng.choice(wilayah_nama, size=n, p=wilayah_prop)

# Jarak ke kantor layanan keuangan terdekat — median berbeda per wilayah.
# Kolom ini TIDAK menyebut wilayah, tetapi "membawa" informasi wilayah (proksi).
median_jarak = {"Jawa": 3, "Sumatera": 8, "Kalimantan": 20,
                "Sulawesi": 15, "Papua": 45}
jarak = pd.Series(wilayah).map(median_jarak).values * rng.lognormal(0, 0.5, size=n)

df = pd.DataFrame({
    "wilayah":          wilayah,
    "omzet_jt":         rng.gamma(2.0, 20, size=n).round(1),
    "lama_usaha_thn":   rng.gamma(2.0, 2.5, size=n).round(1),
    "rasio_utang":      rng.beta(2, 5, size=n).round(3),
    "riwayat_telat":    rng.poisson(0.8, size=n),
    "jenis_usaha":      rng.choice(["Kuliner", "Retail", "Jasa", "Produksi"], size=n),
    "jarak_layanan_km": jarak.round(1),
})

# Pola hubungan BERBEDA di luar Jawa:
# - riwayat telat bayar kurang informatif (pencatatan kredit belum merata);
# - guncangan musiman (cuaca, logistik) yang TIDAK tercatat lebih berpengaruh.
luar_jawa = (df["wilayah"] != "Jawa").values
guncangan_musiman = rng.normal(0, 1, size=n)          # tidak masuk ke data
efek_wilayah = {"Jawa": 0.0, "Sumatera": 0.4, "Kalimantan": 0.8,
                "Sulawesi": 0.7, "Papua": 1.2}
logit = (-1.6 - 0.025 * df["omzet_jt"] - 0.15 * df["lama_usaha_thn"]
         + 3.0 * df["rasio_utang"]
         + np.where(luar_jawa, 0.25, 0.75) * df["riwayat_telat"]
         + np.where(luar_jawa, 0.9, 0.1) * guncangan_musiman
         + df["wilayah"].map(efek_wilayah))
df["gagal_bayar"] = rng.binomial(1, 1 / (1 + np.exp(-logit)))

print("Sebaran wilayah:")
print(df["wilayah"].value_counts().to_string())
print("\nProporsi gagal bayar (base rate) per wilayah:")
print(df.groupby("wilayah")["gagal_bayar"].mean().round(3).to_string())
print("\nMedian jarak ke layanan keuangan (km) per wilayah:")
print(df.groupby("wilayah")["jarak_layanan_km"].median().round(1).to_string())
```

> **Perhatikan tiga hal:** (1) jumlah data per wilayah sangat timpang; (2) *base rate* berbeda antarwilayah; (3) jarak ke layanan keuangan hampir "menyebutkan" wilayahnya. Ketiganya akan muncul kembali dalam audit.

### LANGKAH 2: Melatih Model

```python
# =============================================
# LANGKAH 2: Model — dengan atribut wilayah sebagai fitur
# =============================================
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score, recall_score

X = df.drop(columns=["gagal_bayar"]); y = df["gagal_bayar"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=RANDOM_STATE)

kol_kat = ["wilayah", "jenis_usaha"]
kol_num = [c for c in X.columns if c not in kol_kat]

def buat_model(kolom_kategorik):
    # Pipeline yang sama dipakai untuk model dengan dan tanpa wilayah
    pra = ColumnTransformer([
        ("num", "passthrough", kol_num),
        ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False),
         kolom_kategorik),
    ])
    # class_weight="balanced": kelas gagal bayar (±18%) diberi bobot lebih besar.
    # Tanpa ini, model nyaris tidak pernah memprediksi "gagal bayar"
    # dan recall-nya hanya beberapa persen.
    return Pipeline([
        ("pra", pra),
        ("clf", HistGradientBoostingClassifier(
            max_iter=300, early_stopping=True, class_weight="balanced",
            random_state=RANDOM_STATE)),
    ])

model = buat_model(kol_kat).fit(X_train, y_train)
pred = model.predict(X_test)
prob = model.predict_proba(X_test)[:, 1]
print(f"ROC-AUC keseluruhan: {roc_auc_score(y_test, prob):.4f}")
print(f"Recall keseluruhan : {recall_score(y_test, pred):.4f}")
```

### LANGKAH 3: Audit per Kelompok — Inti Lab Ini

```python
# =============================================
# LANGKAH 3: Fungsi audit
# =============================================
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, confusion_matrix)

def audit_kelompok(y_true, y_pred, y_prob, kelompok, nama_kelompok="Kelompok"):
    # Menghitung metrik terpisah per kelompok
    y_true, y_pred, y_prob = map(np.asarray, (y_true, y_pred, y_prob))
    kelompok = np.asarray(kelompok)
    baris = []
    for k in pd.unique(kelompok):
        m = kelompok == k
        yt, yp = y_true[m], y_pred[m]
        tn, fp, fn, tp = confusion_matrix(yt, yp, labels=[0, 1]).ravel()
        baris.append({
            nama_kelompok: k,
            "n": int(m.sum()),
            "n positif": int(yt.sum()),
            "Base rate": yt.mean(),
            "Akurasi": accuracy_score(yt, yp),
            "Precision": precision_score(yt, yp, zero_division=0),
            "Recall": recall_score(yt, yp, zero_division=0),
            "FPR": fp / (fp + tn) if (fp + tn) else 0.0,
            "Prop. prediksi positif": yp.mean(),
            "ROC-AUC": (roc_auc_score(yt, y_prob[m])
                        if len(np.unique(yt)) > 1 else np.nan),
        })
    return pd.DataFrame(baris).sort_values("n", ascending=False)

tabel = audit_kelompok(y_test, pred, prob, X_test["wilayah"], "Wilayah")
print("Audit kinerja per wilayah:")
print(tabel.round(3).to_string(index=False))

# Pembanding yang lebih stabil: Jawa vs gabungan luar Jawa
jawa_vs_luar = np.where(X_test["wilayah"] == "Jawa", "Jawa", "Luar Jawa")
tabel_jl = audit_kelompok(y_test, pred, prob, jawa_vs_luar, "Kelompok")
print("\nJawa vs luar Jawa (gabungan):")
print(tabel_jl.round(3).to_string(index=False))

print(f"\nKinerja KESELURUHAN — akurasi {accuracy_score(y_test, pred):.3f}, "
      f"recall {recall_score(y_test, pred):.3f}")
```

> **Membaca angka per kelompok dengan hati-hati.** Papua hanya memiliki sekitar 50 baris uji dan belasan kasus positif. Satu kasus yang berubah dapat menggeser *recall*-nya sampai 5–10 poin persentase. Karena itu, untuk kelompok kecil, bandingkan juga pada tingkat **gabungan** (Jawa vs luar Jawa), dan jangan menyimpulkan dari selisih *recall* satu wilayah saja.

**Tulis temuan:** pada kelompok mana ROC-AUC lebih rendah? Pada kelompok mana FPR (nasabah yang sebenarnya lancar, tetapi ditandai berisiko) lebih tinggi? Apa artinya bagi pelaku usaha yang tinggal di sana?

### LANGKAH 4: Empat Ukuran *Fairness* dan Pertentangannya

| Ukuran | Menuntut | Kolom pada tabel audit |
|--------|----------|------------------------|
| *Demographic parity* | Proporsi prediksi positif sama | `Prop. prediksi positif` |
| *Equal opportunity* | *Recall* sama | `Recall` |
| *Equalized odds* | *Recall* **dan** FPR sama | `Recall`, `FPR` |
| *Predictive parity* | *Precision* sama | `Precision` |

```python
# =============================================
# LANGKAH 4: Ukuran fairness — gunakan tabel Jawa vs luar Jawa
# =============================================
t = tabel_jl.set_index("Kelompok")
def selisih(kolom):
    return abs(t.loc["Jawa", kolom] - t.loc["Luar Jawa", kolom])

print("Selisih Jawa vs luar Jawa:")
print(f"  Demographic parity (prop. prediksi positif): {selisih('Prop. prediksi positif'):.3f}")
print(f"  Equal opportunity  (recall)                : {selisih('Recall'):.3f}")
print(f"  Equalized odds     (FPR)                   : {selisih('FPR'):.3f}")
print(f"  Predictive parity  (precision)             : {selisih('Precision'):.3f}")
print(f"\nBase rate — Jawa {t.loc['Jawa', 'Base rate']:.3f}, "
      f"luar Jawa {t.loc['Luar Jawa', 'Base rate']:.3f}")

# Identitas Chouldechova (2017): untuk setiap kelompok berlaku
#   FPR = p/(1-p) * (1-PPV)/PPV * recall,  dengan p = base rate, PPV = precision.
# Bila p berbeda dan model tidak sempurna, precision yang sama memaksa
# recall atau FPR berbeda — dan sebaliknya.
for k in ["Jawa", "Luar Jawa"]:
    p, ppv, rec = t.loc[k, ["Base rate", "Precision", "Recall"]]
    print(f"{k:9s}: FPR teramati {t.loc[k, 'FPR']:.3f} | "
          f"FPR dari identitas {p/(1-p) * (1-ppv)/ppv * rec:.3f}")
```

> **Apa yang sebenarnya terbukti secara matematis.** Chouldechova (2017) menunjukkan identitas di atas: bila *base rate* berbeda antarkelompok dan model tidak sempurna, **predictive parity** (*precision* sama) dan **equalized odds** (*recall* dan FPR sama) **tidak dapat dipenuhi bersamaan**. Kleinberg, Mullainathan, dan Raghavan (2016) membuktikan hal serupa untuk **kalibrasi per kelompok** versus keseimbangan galat kedua kelas.
>
> Hati-hati: *demographic parity*, *equal opportunity*, dan *equalized odds* **dapat** dipenuhi bersamaan — misalnya oleh model yang memprediksi semua orang "lancar". Model seperti itu adil menurut ketiga ukuran, tetapi tidak berguna. Jadi pertentangannya adalah antara ukuran *fairness* yang saling bertentangan **dan** antara *fairness* dengan kegunaan. Insinyur harus **memilih**, menyatakan alasannya, dan mengakui apa yang dikorbankan.

### LANGKAH 5: Menghapus Atribut Sensitif Tidak Cukup

```python
# =============================================
# LANGKAH 5: Membuang kolom wilayah — apakah ketimpangan hilang?
# =============================================
X2_train = X_train.drop(columns=["wilayah"])
X2_test  = X_test.drop(columns=["wilayah"])

model2 = buat_model(["jenis_usaha"]).fit(X2_train, y_train)
pred2 = model2.predict(X2_test)
prob2 = model2.predict_proba(X2_test)[:, 1]

# Audit TETAP dilakukan per wilayah, meski wilayah bukan lagi fitur
tabel2 = audit_kelompok(y_test, pred2, prob2, X_test["wilayah"], "Wilayah")
tabel2_jl = audit_kelompok(y_test, pred2, prob2, jawa_vs_luar, "Kelompok").set_index("Kelompok")
print("Audit setelah kolom wilayah DIBUANG:")
print(tabel2.round(3).to_string(index=False))

def gap_fpr(tb):
    return tb.loc["Luar Jawa", "FPR"] - tb.loc["Jawa", "FPR"]

g1, g2 = gap_fpr(t), gap_fpr(tabel2_jl)
print(f"\nSelisih FPR (luar Jawa − Jawa) — dengan wilayah : {g1:+.3f}")
print(f"Selisih FPR (luar Jawa − Jawa) — tanpa wilayah  : {g2:+.3f}")

# Seberapa kuat jarak menjadi proksi wilayah?
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
akurasi_proksi = cross_val_score(
    DecisionTreeClassifier(max_depth=3, random_state=RANDOM_STATE),
    X[["jarak_layanan_km"]], (X["wilayah"] == "Jawa"), cv=5).mean()
print(f"Jawa/luar Jawa dapat ditebak dari jarak saja dengan akurasi {akurasi_proksi:.3f}")

# Kesimpulan DIHITUNG dari angka, bukan ditulis tetap
if g2 > 0.5 * g1 and g2 > 0.02:
    print("\nKESIMPULAN: ketimpangan FPR TIDAK hilang setelah wilayah dibuang "
          f"(semula {g1:+.3f}, kini {g2:+.3f}). Jarak bertindak sebagai proksi.")
else:
    print("\nKESIMPULAN: ketimpangan FPR mengecil tajam setelah wilayah dibuang. "
          "Periksa apakah ada fitur proksi lain pada data Anda.")
```

> **Kesimpulan yang harus ditulis:** ketimpangan bersumber dari **pola yang berbeda antarkelompok, jumlah data yang timpang, dan fitur proksi** — bukan semata dari hadirnya kolom wilayah sebagai fitur. Karena itu pengukuran per kelompok tetap wajib, **bahkan ketika atributnya tidak dipakai sebagai fitur**. Untuk itu atribut sensitif tetap perlu **disimpan untuk keperluan audit**, meskipun tidak dipakai untuk memprediksi.

### LANGKAH 6: Visualisasi Ketimpangan

```python
# =============================================
# LANGKAH 6: Menampilkan ketimpangan secara visual
# =============================================
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 3, figsize=(16, 4.5))
urut = tabel.sort_values("n", ascending=False)

ax[0].barh(urut["Wilayah"][::-1], urut["n"][::-1])
ax[0].set_xlabel("Jumlah data uji"); ax[0].set_title("1. Representasi dalam data")

ax[1].barh(urut["Wilayah"][::-1], urut["FPR"][::-1], color="tab:orange")
fpr_total = ((pred == 1) & (y_test.values == 0)).sum() / (y_test.values == 0).sum()
ax[1].axvline(fpr_total, color="red", ls="--", label=f"Keseluruhan ({fpr_total:.3f})")
ax[1].set_xlabel("FPR (lancar, tetapi ditandai berisiko)")
ax[1].set_title("2. FPR per wilayah"); ax[1].legend()

ax[2].scatter(urut["n"], urut["ROC-AUC"], s=110)
for _, r in urut.iterrows():
    ax[2].annotate(r["Wilayah"], (r["n"], r["ROC-AUC"]),
                   xytext=(5, 5), textcoords="offset points", fontsize=8)
ax[2].set_xscale("log")
ax[2].set_xlabel("Jumlah data uji (skala log)"); ax[2].set_ylabel("ROC-AUC")
ax[2].set_title("3. Jumlah data dan kemampuan membedakan")

plt.tight_layout(); plt.show()
```

**Tulis pembahasan:** apakah grafik ketiga menunjukkan bahwa wilayah dengan data lebih sedikit dilayani lebih buruk? Apa implikasinya bagi pengumpulan data di masa depan?

### LANGKAH 7: Satu Model vs Model per Kelompok

```python
# =============================================
# LANGKAH 7: Apakah model terpisah membantu?
# =============================================
baris = []
for w in wilayah_nama:
    m_tr = (X_train["wilayah"] == w).values
    m_te = (X_test["wilayah"] == w).values
    auc_tunggal = tabel.loc[tabel["Wilayah"] == w, "ROC-AUC"].iloc[0]
    if m_tr.sum() < 300:
        baris.append({"Wilayah": w, "n latih": int(m_tr.sum()),
                      "AUC (model tunggal)": auc_tunggal,
                      "AUC (model terpisah)": np.nan,
                      "Catatan": "data terlalu sedikit untuk model sendiri"})
        continue
    m_khusus = buat_model(["jenis_usaha"]).fit(X2_train[m_tr], y_train[m_tr])
    auc_khusus = roc_auc_score(y_test[m_te], m_khusus.predict_proba(X2_test[m_te])[:, 1])
    baris.append({"Wilayah": w, "n latih": int(m_tr.sum()),
                  "AUC (model tunggal)": auc_tunggal,
                  "AUC (model terpisah)": auc_khusus, "Catatan": ""})

print(pd.DataFrame(baris).round(3).to_string(index=False))
```

> **Perhatikan baris "data terlalu sedikit".** Kelompok yang paling membutuhkan model khusus justru yang paling tidak mungkin memperolehnya, karena datanya paling sedikit. Ini bentuk ketimpangan yang tidak dapat diselesaikan secara teknis semata — jalan keluarnya ada pada **pengumpulan data**, bukan pada algoritma.

### LANGKAH 8: Menyusun *Model Card*

```python
# =============================================
# LANGKAH 8: Model card — luaran wajib
# =============================================
# Buat berkas TERPISAH bernama model_card.md berisi format berikut,
# diisi dari hasil audit di atas.
```

```markdown
# Model Card — [Judul Model Proyek Anda]

## 1. Rincian Model
- Dikembangkan oleh: Kelompok __, IF52510031, Prodi Informatika UAI
- Tanggal: ______  ·  Versi: 1.0
- Jenis model: ______
- Sumber dan lisensi data: ______

## 2. Penggunaan yang Dimaksudkan
- **Untuk:** ______
- **BUKAN untuk:** ______
- Pengguna yang dituju: ______
- Di luar cakupan: ______

## 3. Data
- Sumber, periode, jumlah baris dan kolom: ______
- Cakupan kelompok (wilayah/kategori): ______
- **Yang TIDAK tercakup:** ______
- Prapemrosesan: ______

## 4. Kinerja
| Kelompok | n | Base rate | Precision | Recall | FPR |
|----------|---|-----------|-----------|--------|-----|
| Keseluruhan | | | | | |
| ... | | | | | |

- Baseline (DummyClassifier): ______
- Metrik utama dan alasan pemilihannya: ______

## 5. Keterbatasan
- Kelompok dengan kinerja terendah dan besarnya selisih: ______
- Kondisi ketika model tidak dapat diandalkan: ______
- Asumsi yang dapat gugur seiring waktu: ______

## 6. Pertimbangan Etis
- Siapa yang dapat dirugikan bila model salah: ______
- **Ukuran fairness yang dipilih DAN ALASANNYA:** ______
- Apa yang dikorbankan dengan pilihan itu: ______
- Mekanisme pengawasan manusia: ______
- Cara mengajukan keberatan atas keputusan: ______

## 7. Pemeliharaan
- Kapan model harus dilatih ulang: ______
- Indikator yang dipantau: ______
- Penanggung jawab: ______
```

### LANGKAH 9: Enam Pertanyaan Tanggung Jawab

```python
# =============================================
# LANGKAH 9: Jawab di sel Markdown
# =============================================
# 1. Siapa yang terdampak bila model salah, dan seberapa berat?
# 2. Adakah kelompok yang dirugikan secara tidak sebanding?
# 3. Adakah pengawasan manusia pada keputusan berdampak besar?
# 4. Dapatkah orang yang terdampak mengetahui bahwa keputusannya
#    melibatkan model?
# 5. Adakah jalan mengajukan keberatan dan memperoleh peninjauan manusia?
# 6. SIAPA yang bertanggung jawab ketika model merugikan seseorang?
#
# Pertanyaan keenam tidak memiliki jawaban teknis. Ia selalu terjawab
# dengan NAMA SESEORANG — tidak pernah dengan nama sebuah model.
```

---

## Tantangan Tambahan

### Tantangan 1 — Ambang per Kelompok

Tetapkan ambang keputusan yang **berbeda** untuk tiap wilayah sehingga *recall*-nya menjadi setara. Apa yang terjadi pada *precision* masing-masing? Apakah pendekatan ini adil? Bahas dari dua sisi.

### Tantangan 2 — Bobot Sampel

Latih ulang model dengan `sample_weight` yang menaikkan bobot kelompok kecil. Apakah ketimpangan berkurang? Berapa biayanya pada kinerja keseluruhan?

### Tantangan 3 — Bias Umpan Balik

Simulasikan bias umpan balik: (a) latih model, (b) pakai prediksinya untuk memutuskan siapa yang "diperiksa", (c) hanya data yang diperiksa masuk ke data latih berikutnya, (d) latih ulang. Ulangi lima siklus. Bagaimana sebaran wilayah dalam data latih berubah? Apa pelajarannya?

---

## Checklist Penyelesaian

- [ ] Audit kinerja **model proyek sendiri**, terpisah per minimal dua kelompok
- [ ] Selisih *recall*, *precision*, dan FPR antarkelompok dilaporkan
- [ ] Keempat ukuran *fairness* dihitung
- [ ] **Pertentangan *predictive parity* vs *equalized odds* ditunjukkan** dengan bukti *base rate* berbeda
- [ ] Fitur proksi atribut sensitif pada data sendiri diidentifikasi
- [ ] Diperiksa dengan angka apakah membuang atribut sensitif menghapus ketimpangan
- [ ] Hubungan jumlah data dan kinerja divisualisasikan
- [ ] **Ukuran *fairness* yang dipilih dinyatakan beserta alasan dan pengorbanannya**
- [ ] *Model card* lengkap sebagai berkas terpisah
- [ ] Bagian Keterbatasan dan Pertimbangan Etis **terisi jujur**
- [ ] Enam pertanyaan tanggung jawab dijawab
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 14](../03-modules/week-14-ai-generatif-dan-ai-bertanggung-jawab.md)
2. [Bab 13 buku ajar](../06-buku-ajar/bab-13-ai-generatif-dan-ai-bertanggung-jawab.md)
3. Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and Machine Learning*. MIT Press. <https://fairmlbook.org>
4. Mitchell, M., et al. (2019). Model Cards for Model Reporting. *FAT* '19*, 220–229.
5. Kleinberg, J., Mullainathan, S., & Raghavan, M. (2016). Inherent Trade-Offs in the Fair Determination of Risk Scores. *arXiv:1609.05807*.
6. Chouldechova, A. (2017). Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments. *Big Data*, 5(2), 153–163.
7. Suresh, H., & Guttag, J. (2021). A Framework for Understanding Sources of Harm throughout the ML Life Cycle. *EAAMO '21*.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
