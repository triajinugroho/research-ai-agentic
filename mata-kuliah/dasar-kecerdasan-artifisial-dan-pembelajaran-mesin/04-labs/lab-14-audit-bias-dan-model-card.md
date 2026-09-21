# Lab 14: Audit *Bias* dan *Model Card*

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 14 |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-13 |
| Durasi | 100 menit |
| Prasyarat | Lab 13 selesai; model proyek sudah ada |
| Bobot | 1,9% (Observasi) |

---

## Tujuan Praktikum

1. Mengukur kinerja model terpisah per kelompok.
2. Menghitung ukuran *fairness* dan menunjukkan pertentangannya.
3. Membuktikan bahwa menghapus atribut sensitif tidak menghapus *bias*.
4. Menyusun *model card* yang lengkap dan jujur.

---

## Ketentuan Khusus Lab Ini

> **Audit dilakukan pada model proyek Anda sendiri**, bukan pada contoh. Contoh pada lab ini hanya untuk mempelajari tekniknya. Luaran yang dinilai adalah audit atas model kelompok Anda.

---

## Langkah-langkah

### LANGKAH 1: Data dengan Ketimpangan Representasi

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

df = pd.DataFrame({
    "wilayah":        wilayah,
    "omzet_jt":       rng.gamma(2.0, 20, size=n).round(1),
    "lama_usaha_thn": rng.gamma(2.0, 2.5, size=n).round(1),
    "rasio_utang":    rng.beta(2, 5, size=n).round(3),
    "riwayat_telat":  rng.poisson(0.8, size=n),
    "jenis_usaha":    rng.choice(["Kuliner","Retail","Jasa","Produksi"], size=n),
})

# Pola hubungan BERBEDA antar wilayah — model tunggal akan kesulitan
# pada wilayah yang datanya sedikit
efek_wilayah = {"Jawa": 0.0, "Sumatera": 0.2, "Kalimantan": 0.4,
                "Sulawesi": 0.5, "Papua": 0.9}
logit = (-1.8 - 0.021 * df["omzet_jt"] - 0.15 * df["lama_usaha_thn"]
         + 2.7 * df["rasio_utang"] + 0.40 * df["riwayat_telat"]
         + df["wilayah"].map(efek_wilayah))
df["gagal_bayar"] = rng.binomial(1, 1 / (1 + np.exp(-logit)))

print("Sebaran wilayah:")
print(df["wilayah"].value_counts().to_string())
print("\nProporsi gagal bayar per wilayah:")
print(df.groupby("wilayah")["gagal_bayar"].mean().round(3).to_string())
```

> **Perhatikan:** angka kejadian dasar (*base rate*) berbeda antarwilayah. Inilah kondisi yang membuat ukuran-ukuran *fairness* saling bertentangan (Kleinberg et al., 2016).

### LANGKAH 2: Melatih Model

```python
# =============================================
# LANGKAH 2: Model — dengan atribut wilayah sebagai fitur
# =============================================
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score

X = df.drop(columns=["gagal_bayar"]); y = df["gagal_bayar"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=RANDOM_STATE)

kol_kat = ["wilayah", "jenis_usaha"]
kol_num = [c for c in X.columns if c not in kol_kat]

pra = ColumnTransformer([
    ("num", "passthrough", kol_num),
    ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), kol_kat),
])

model = Pipeline([
    ("pra", pra),
    ("clf", HistGradientBoostingClassifier(max_iter=300, early_stopping=True,
                                           random_state=RANDOM_STATE)),
]).fit(X_train, y_train)

pred = model.predict(X_test)
prob = model.predict_proba(X_test)[:, 1]
print(f"ROC-AUC keseluruhan: {roc_auc_score(y_test, prob):.4f}")
```

### LANGKAH 3: Audit per Kelompok — Inti Lab Ini

```python
# =============================================
# LANGKAH 3: Fungsi audit
# =============================================
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score, confusion_matrix)

def audit_kelompok(y_true, y_pred, y_prob, kelompok, nama_kelompok="Kelompok"):
    # Menghitung metrik terpisah per kelompok
    baris = []
    for k in pd.unique(kelompok):
        m = (kelompok == k).values if hasattr(kelompok, "values") else (kelompok == k)
        yt, yp = np.asarray(y_true)[m], np.asarray(y_pred)[m]
        cm = confusion_matrix(yt, yp, labels=[0, 1])
        tn, fp, fn, tp = cm.ravel()
        baris.append({
            nama_kelompok: k,
            "n": int(m.sum()),
            "Base rate": yt.mean(),
            "Akurasi": accuracy_score(yt, yp),
            "Precision": precision_score(yt, yp, zero_division=0),
            "Recall": recall_score(yt, yp, zero_division=0),
            "FPR": fp / (fp + tn) if (fp + tn) else 0.0,
            "Prop. prediksi positif": yp.mean(),
            "ROC-AUC": (roc_auc_score(yt, np.asarray(y_prob)[m])
                        if len(np.unique(yt)) > 1 else np.nan),
        })
    return pd.DataFrame(baris).sort_values("n", ascending=False)

tabel = audit_kelompok(y_test, pred, prob, X_test["wilayah"], "Wilayah")
print("Audit kinerja per wilayah:")
print(tabel.round(4).to_string(index=False))

print(f"\nKinerja KESELURUHAN — akurasi {accuracy_score(y_test, pred):.4f}, "
      f"recall {recall_score(y_test, pred):.4f}")
print(f"\nSelisih recall maks-min   : "
      f"{tabel['Recall'].max() - tabel['Recall'].min():.4f}")
print(f"Selisih precision maks-min: "
      f"{tabel['Precision'].max() - tabel['Precision'].min():.4f}")
print(f"Selisih FPR maks-min      : "
      f"{tabel['FPR'].max() - tabel['FPR'].min():.4f}")
```

**Tulis temuan:** wilayah mana yang kinerjanya paling rendah? Apakah berkaitan dengan jumlah datanya? Apa artinya bagi orang yang tinggal di sana?

### LANGKAH 4: Tiga Ukuran *Fairness*

```python
# =============================================
# LANGKAH 4: Ukuran fairness dan pertentangannya
# =============================================
print("Demographic parity — proporsi prediksi positif harus SAMA:")
print(tabel[["Wilayah", "Prop. prediksi positif"]].round(4).to_string(index=False))
print(f"  Selisih maks-min: "
      f"{tabel['Prop. prediksi positif'].max() - tabel['Prop. prediksi positif'].min():.4f}")

print("\nEqual opportunity — recall harus SAMA:")
print(tabel[["Wilayah", "Recall"]].round(4).to_string(index=False))
print(f"  Selisih maks-min: {tabel['Recall'].max() - tabel['Recall'].min():.4f}")

print("\nEqualized odds — recall DAN FPR harus SAMA:")
print(tabel[["Wilayah", "Recall", "FPR"]].round(4).to_string(index=False))

print("\nBase rate per wilayah (angka kejadian sebenarnya):")
print(tabel[["Wilayah", "Base rate"]].round(4).to_string(index=False))
print("\nKarena base rate BERBEDA antarwilayah, ketiga ukuran di atas")
print("TIDAK DAPAT dipenuhi sekaligus (Kleinberg et al., 2016).")
print("Insinyur harus MEMILIH salah satu dan menyatakan alasannya.")
```

### LANGKAH 5: Menghapus Atribut Sensitif Tidak Cukup

```python
# =============================================
# LANGKAH 5: Membuang kolom wilayah — apakah bias hilang?
# =============================================
X2 = X.drop(columns=["wilayah"])
X2_train, X2_test = X2.loc[X_train.index], X2.loc[X_test.index]

pra2 = ColumnTransformer([
    ("num", "passthrough", kol_num),
    ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False),
     ["jenis_usaha"]),
])
model2 = Pipeline([
    ("pra", pra2),
    ("clf", HistGradientBoostingClassifier(max_iter=300, early_stopping=True,
                                           random_state=RANDOM_STATE)),
]).fit(X2_train, y_train)

pred2 = model2.predict(X2_test)
prob2 = model2.predict_proba(X2_test)[:, 1]

# Audit TETAP dilakukan per wilayah, meski wilayah bukan lagi fitur
tabel2 = audit_kelompok(y_test, pred2, prob2, X_test["wilayah"], "Wilayah")
print("Audit setelah kolom wilayah DIBUANG:")
print(tabel2.round(4).to_string(index=False))

print(f"\nSelisih recall — dengan wilayah : "
      f"{tabel['Recall'].max() - tabel['Recall'].min():.4f}")
print(f"Selisih recall — tanpa wilayah  : "
      f"{tabel2['Recall'].max() - tabel2['Recall'].min():.4f}")
print("\nKetimpangan TIDAK hilang hanya dengan membuang atributnya.")
```

> **Kesimpulan yang harus ditulis:** ketimpangan bersumber dari **jumlah data dan pola yang berbeda antarkelompok**, bukan semata dari hadirnya kolom itu sebagai fitur. Karena itu pengukuran per kelompok tetap wajib, **bahkan ketika atributnya tidak dipakai**.

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

ax[1].barh(urut["Wilayah"][::-1], urut["Recall"][::-1], color="tab:orange")
ax[1].axvline(recall_score(y_test, pred), color="red", ls="--",
              label=f"Keseluruhan ({recall_score(y_test, pred):.3f})")
ax[1].set_xlabel("Recall"); ax[1].set_title("2. Recall per wilayah"); ax[1].legend()

ax[2].scatter(urut["n"], urut["Recall"], s=110)
for _, r in urut.iterrows():
    ax[2].annotate(r["Wilayah"], (r["n"], r["Recall"]),
                   xytext=(5, 5), textcoords="offset points", fontsize=8)
ax[2].set_xlabel("Jumlah data"); ax[2].set_ylabel("Recall")
ax[2].set_title("3. Hubungan jumlah data dan kinerja")

plt.tight_layout(); plt.show()
```

**Tulis pembahasan:** apakah grafik ketiga menunjukkan hubungan? Apa implikasinya bagi pengumpulan data di masa depan?

### LANGKAH 7: Satu Model vs Model per Kelompok

```python
# =============================================
# LANGKAH 7: Apakah model terpisah membantu?
# =============================================
baris = []
for w in wilayah_nama:
    m_tr = (X_train["wilayah"] == w).values
    m_te = (X_test["wilayah"] == w).values
    if m_tr.sum() < 100 or len(np.unique(y_test[m_te])) < 2:
        baris.append({"Wilayah": w, "n latih": int(m_tr.sum()),
                      "Recall (model tunggal)": tabel.loc[tabel["Wilayah"]==w,
                                                          "Recall"].iloc[0],
                      "Recall (model terpisah)": np.nan,
                      "Catatan": "data terlalu sedikit"})
        continue
    m_khusus = Pipeline([
        ("pra", pra2),
        ("clf", HistGradientBoostingClassifier(max_iter=200, early_stopping=True,
                                               random_state=RANDOM_STATE)),
    ]).fit(X2_train[m_tr], y_train[m_tr])
    r = recall_score(y_test[m_te], m_khusus.predict(X2_test[m_te]), zero_division=0)
    baris.append({"Wilayah": w, "n latih": int(m_tr.sum()),
                  "Recall (model tunggal)": tabel.loc[tabel["Wilayah"]==w,
                                                      "Recall"].iloc[0],
                  "Recall (model terpisah)": r, "Catatan": ""})

print(pd.DataFrame(baris).round(4).to_string(index=False))
```

> **Perhatikan baris "data terlalu sedikit".** Kelompok yang paling membutuhkan model khusus justru yang paling tidak mungkin memperolehnya, karena datanya paling sedikit. Ini adalah bentuk ketimpangan yang tidak dapat diselesaikan secara teknis semata.

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
- [ ] Ketiga ukuran *fairness* dihitung
- [ ] **Pertentangan antarukuran ditunjukkan** dengan bukti *base rate* berbeda
- [ ] Dibuktikan bahwa membuang atribut sensitif **tidak** menghapus ketimpangan
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
6. Suresh, H., & Guttag, J. (2021). A Framework for Understanding Sources of Harm throughout the ML Life Cycle. *EAAMO '21*.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
