# Minggu 7: Klasifikasi dan Metriknya

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 7 dari 16 |
| Topik | Regresi logistik, k-NN, matriks konfusi, *precision*/*recall*, ROC-AUC, data tak seimbang |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-07 |
| Bloom | C3 (Menerapkan) → C5 (Mengevaluasi) |
| Durasi | 150 menit |
| Metode | Kuliah · Perhitungan manual · Praktikum |
| Penilaian | Observasi (Lab 7) · **Kuis 2** · **Milestone proyek 1 (P-01)** |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menjelaskan** (C2) cara kerja regresi logistik dan k-NN beserta perbedaannya.
2. **Menghitung** (C3) matriks konfusi, *precision*, *recall*, F1, dan spesifisitas secara manual.
3. **Menganalisis** (C4) mengapa akurasi menyesatkan pada data tak seimbang.
4. **Memilih** (C5) ambang keputusan berdasarkan biaya kesalahan.
5. **Menafsirkan** (C4) kurva ROC dan kurva *precision-recall*.

---

## Materi Pembelajaran

### 7.1 Regresi Logistik

#### 7.1.1 Dari Linear ke Probabilitas

Regresi linear menghasilkan bilangan pada rentang tak terbatas — tidak sesuai untuk probabilitas. Fungsi **sigmoid** memetakannya ke [0, 1]:

$$z = \beta_0 + \beta_1 x_1 + \dots + \beta_p x_p$$
$$P(y=1 \mid x) = \sigma(z) = \frac{1}{1 + e^{-z}}$$

```
   P(y=1)
    1,0 ┤                          ╭──────────────
        │                      ╭───╯
    0,5 ┤ ─ ─ ─ ─ ─ ─ ─ ─╭────╯ ─ ─ ─ ─ ─ ─ ─ ─
        │            ╭───╯
    0,0 ┤────────────╯
        └────────────┬─────────────────────────► z
                     0
```

#### 7.1.2 Menafsirkan Koefisien: *Odds Ratio*

$$\text{odds} = \frac{P}{1-P} \qquad e^{\beta_j} = \text{rasio odds}$$

| $\beta_j$ | $e^{\beta_j}$ | Tafsir |
|-----------|---------------|--------|
| 0,69 | 2,0 | Kenaikan satu satuan $x_j$ **melipatgandakan** odds |
| 0 | 1,0 | Tidak berpengaruh |
| −0,69 | 0,5 | Kenaikan satu satuan **menyetengahkan** odds |

```python
from sklearn.linear_model import LogisticRegression
import numpy as np, pandas as pd

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

rasio_odds = pd.Series(np.exp(model.coef_[0]), index=X_train.columns)
print(rasio_odds.sort_values(ascending=False))
```

> Regresi logistik tetap banyak dipakai pada bidang yang menuntut keterjelasan (perbankan, kesehatan, kebijakan publik) justru karena koefisiennya dapat dijelaskan kepada orang yang akan terkena keputusannya.

---

### 7.2 k-Nearest Neighbors

Tidak ada pelatihan dalam arti biasa: model menyimpan seluruh data latih, lalu memprediksi berdasarkan k tetangga terdekat.

```python
from sklearn.neighbors import KNeighborsClassifier

# PENSKALAAN WAJIB — k-NN berbasis jarak
model = Pipeline([
    ("skala", StandardScaler()),
    ("knn", KNeighborsClassifier(n_neighbors=5, weights="distance")),
])
```

| k | Perilaku | Risiko |
|---|----------|--------|
| 1 | Mengikuti setiap titik | *Overfit*; sangat peka derau |
| 5–15 | Biasanya memadai | — |
| Sangat besar | Mendekati kelas mayoritas | *Underfit* |

| Kelebihan | Kekurangan |
|-----------|------------|
| Sederhana; tanpa asumsi bentuk | Lambat saat prediksi pada data besar |
| Batas keputusan dapat rumit | **Wajib penskalaan** |
| Alami untuk multikelas | Buruk pada dimensi tinggi (kutukan dimensi) |

---

### 7.3 Matriks Konfusi

```
                        PREDIKSI
                  Negatif    Positif
              ┌───────────┬───────────┐
     Negatif  │    TN     │    FP     │
              │ (benar    │ (galat    │
  A           │  negatif) │  Tipe I)  │
  K           ├───────────┼───────────┤
  T  Positif  │    FN     │    TP     │
  U           │ (galat    │ (benar    │
  A           │  Tipe II) │  positif) │
  L           └───────────┴───────────┘
```

| Metrik | Rumus | Menjawab pertanyaan |
|--------|-------|---------------------|
| **Akurasi** | $\frac{TP+TN}{TP+TN+FP+FN}$ | Berapa proporsi prediksi yang benar? |
| **Precision** | $\frac{TP}{TP+FP}$ | Dari yang **diprediksi positif**, berapa yang benar? |
| **Recall** (sensitivitas) | $\frac{TP}{TP+FN}$ | Dari yang **benar-benar positif**, berapa yang tertangkap? |
| **Spesifisitas** | $\frac{TN}{TN+FP}$ | Dari yang benar-benar negatif, berapa yang tertangkap? |
| **F1** | $2 \cdot \frac{P \cdot R}{P + R}$ | Rata-rata harmonik *precision* dan *recall* |

#### 7.3.1 Perhitungan Manual

Deteksi penipuan: 1.000 transaksi, 20 penipuan.

```
                    PREDIKSI
              Wajar      Penipuan
         ┌────────────┬────────────┐
 Wajar   │  TN = 950  │  FP = 30   │   980
         ├────────────┼────────────┤
Penipuan │  FN = 6    │  TP = 14   │    20
         └────────────┴────────────┘
             956          44          1.000
```

$$\text{Akurasi} = \frac{14 + 950}{1000} = 0{,}964$$
$$\text{Precision} = \frac{14}{14+30} = \frac{14}{44} \approx 0{,}318$$
$$\text{Recall} = \frac{14}{14+6} = \frac{14}{20} = 0{,}700$$
$$\text{F1} = 2 \cdot \frac{0{,}318 \cdot 0{,}700}{0{,}318 + 0{,}700} \approx 0{,}437$$

**Pembacaannya:** akurasi 96,4% terdengar sangat baik, tetapi *precision* 0,318 berarti **dua dari tiga peringatan penipuan adalah peringatan palsu** — yang berarti beban kerja besar bagi petugas pemeriksa.

#### 7.3.2 Mengapa Akurasi Menyesatkan

Model yang **selalu** menjawab "wajar" pada kasus di atas:

$$\text{Akurasi} = \frac{980}{1000} = 0{,}98 \qquad \text{Recall} = \frac{0}{20} = 0$$

Akurasinya **lebih tinggi** daripada model yang sebenarnya bekerja. Modelnya sama sekali tidak berguna.

> **Ketentuan mata kuliah ini:** melaporkan akurasi sebagai satu-satunya metrik pada data tak seimbang dikenai pengurangan nilai, baik pada lab maupun proyek.

---

### 7.4 Ambang Keputusan

Model menghasilkan probabilitas; ambang mengubahnya menjadi keputusan.

```python
probabilitas = model.predict_proba(X_test)[:, 1]

# Ambang baku 0,5 — belum tentu tepat
prediksi_baku = (probabilitas >= 0.50).astype(int)

# Ambang lebih rendah: recall naik, precision turun
prediksi_sensitif = (probabilitas >= 0.30).astype(int)

# Ambang lebih tinggi: precision naik, recall turun
prediksi_ketat = (probabilitas >= 0.70).astype(int)
```

| Ambang | Precision | Recall | Kapan dipilih |
|--------|-----------|--------|---------------|
| Rendah (0,2–0,3) | Turun | **Naik** | Melewatkan positif sangat mahal (deteksi penyakit) |
| Baku (0,5) | Seimbang | Seimbang | Biaya kedua kesalahan setara |
| Tinggi (0,7–0,8) | **Naik** | Turun | Positif palsu sangat mahal (penyaring spam) |

#### 7.4.1 Menentukan Ambang dari Biaya

Bila biaya FN dan FP dapat ditaksir:

```python
biaya_fn = 5_000_000   # penipuan lolos: rata-rata kerugian
biaya_fp = 50_000      # pemeriksaan sia-sia: biaya petugas

import numpy as np
hasil = []
for t in np.arange(0.05, 0.96, 0.05):
    pred = (probabilitas >= t).astype(int)
    fn = ((y_test == 1) & (pred == 0)).sum()
    fp = ((y_test == 0) & (pred == 1)).sum()
    hasil.append((t, fn * biaya_fn + fp * biaya_fp))

ambang_terbaik = min(hasil, key=lambda r: r[1])
print(f"Ambang dengan biaya terendah: {ambang_terbaik[0]:.2f}")
```

> Pendekatan ini mengubah pemilihan ambang dari soal selera menjadi soal yang dapat dipertanggungjawabkan. Ia menjadi kriteria penilaian pada proyek.

---

### 7.5 Kurva ROC dan *Precision-Recall*

| Kurva | Sumbu | Ringkasan | Kapan dipakai |
|-------|-------|-----------|---------------|
| **ROC** | FPR vs TPR | AUC | Kelas relatif seimbang |
| **Precision-Recall** | Recall vs Precision | PR-AUC / *Average Precision* | **Kelas sangat tak seimbang** |

```python
from sklearn.metrics import roc_auc_score, average_precision_score, RocCurveDisplay

print("ROC-AUC:", roc_auc_score(y_test, probabilitas))
print("PR-AUC :", average_precision_score(y_test, probabilitas))
```

| ROC-AUC | Tafsir |
|---------|--------|
| 0,5 | Setara menebak acak |
| 0,7–0,8 | Dapat diterima |
| 0,8–0,9 | Baik |
| > 0,9 | Sangat baik — **periksa kebocoran** |

> **Mengapa PR-AUC lebih jujur pada data tak seimbang:** ROC memakai *false positive rate*, yang penyebutnya adalah jumlah negatif. Ketika negatif sangat banyak, penambahan FP hampir tidak menggeser FPR — sehingga ROC-AUC tetap tampak tinggi meski *precision* buruk.

---

### 7.6 Menangani Data Tak Seimbang

| Strategi | Cara | Catatan |
|----------|------|---------|
| **Metrik yang tepat** | F1, PR-AUC, *recall* per kelas | **Selalu dilakukan lebih dahulu** |
| Bobot kelas | `class_weight="balanced"` | Sederhana dan aman |
| *Undersampling* | Kurangi kelas mayoritas | Membuang data |
| *Oversampling* | Gandakan kelas minoritas | Risiko *overfit* |
| SMOTE | Bangkitkan contoh sintetis | **Hanya pada data latih**, di dalam `Pipeline` |
| Penyesuaian ambang | Geser ambang keputusan | Sering paling efektif |

```python
# Cara paling sederhana dan aman
model = LogisticRegression(class_weight="balanced", max_iter=1000, random_state=42)
```

> **Peringatan tentang SMOTE:** menerapkannya sebelum pembagian data adalah kebocoran — contoh sintetis yang dibangun dari data uji masuk ke data latih. SMOTE wajib berada di dalam `Pipeline` (gunakan `imblearn.pipeline.Pipeline`).

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 7 buku ajar](../06-buku-ajar/bab-07-klasifikasi-dan-metriknya.md).
- Menyiapkan Milestone 1 proyek — **dikumpulkan hari ini**.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | **Pengumpulan P-01**; tinjauan |
| **Kuis 2** | 20' | Matriks konfusi dan pemilihan metrik |
| Konsep | 30' | Regresi logistik; *odds ratio*; k-NN |
| Latihan | 25' | **Perhitungan manual** matriks konfusi dan seluruh metrik |
| Konsep | 30' | Ambang keputusan; ROC vs PR; data tak seimbang |
| Praktik | 25' | Mulai Lab 7 |
| Penutup | 10' | Rangkuman; persiapan UTS |

**Demonstrasi yang wajib ditunjukkan:** model yang selalu menjawab kelas mayoritas, dengan akurasi 98% dan *recall* 0. Ditampilkan sebelum metrik lain dibahas, agar persoalannya terasa konkret.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 7](../04-labs/lab-07-klasifikasi-dan-metrik.md).
- Mempersiapkan UTS dengan [kisi-kisi](../05-assessments/kisi-kisi-uts.md).

---

## Penugasan

**T-07 — Model Klasifikasi dan Metriknya**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook Colab |
| Isi | (a) **Perhitungan manual** matriks konfusi dan metrik, diverifikasi dengan `scikit-learn`; (b) Regresi logistik dan k-NN dalam `Pipeline`; (c) Tafsir *odds ratio*; (d) Kurva ROC dan PR; (e) **Analisis ambang berdasarkan biaya kesalahan**; (f) Perbandingan dengan *baseline* |
| Tenggat | Awal pertemuan Minggu 9 |
| Bobot | 1,9% (Observasi) |

---

## Rangkuman

1. **Sigmoid** mengubah keluaran linear menjadi probabilitas; $e^{\beta}$ adalah **rasio odds**.
2. **k-NN wajib diskalakan** dan buruk pada dimensi tinggi.
3. **Matriks konfusi adalah dasar seluruh metrik klasifikasi.**
4. *Precision*: dari yang diprediksi positif, berapa yang benar. *Recall*: dari yang benar positif, berapa tertangkap.
5. **Akurasi menyesatkan pada data tak seimbang** — model yang selalu menjawab mayoritas dapat berakurasi tinggi dan tak berguna.
6. **Ambang keputusan adalah pilihan**, dan sebaiknya ditentukan dari biaya kesalahan.
7. **PR-AUC lebih jujur daripada ROC-AUC** ketika kelas sangat tak seimbang.
8. ROC-AUC > 0,9 adalah alasan untuk **memeriksa kebocoran**, bukan untuk merayakan.
9. Penanganan ketidakseimbangan dimulai dari **metrik yang tepat**, bukan dari penyeimbangan data.
10. **SMOTE hanya di dalam `Pipeline`** — di luar itu ia kebocoran.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 3. O'Reilly.
2. James, G., et al. (2023). *An Introduction to Statistical Learning with Python*, Bab 4. Springer.
3. Saito, T., & Rehmsmeier, M. (2015). The Precision-Recall Plot Is More Informative than the ROC Plot. *PLoS ONE*, 10(3).
4. He, H., & Garcia, E. A. (2009). Learning from Imbalanced Data. *IEEE TKDE*, 21(9), 1263–1284.
5. Dokumentasi scikit-learn — *Classification metrics*. <https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
