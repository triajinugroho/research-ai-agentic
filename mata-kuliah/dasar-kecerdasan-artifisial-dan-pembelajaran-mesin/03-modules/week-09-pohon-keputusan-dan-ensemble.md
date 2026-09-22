# Minggu 9: Pohon Keputusan dan *Ensemble*

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 9 dari 16 |
| Topik | Pohon keputusan, *entropy*, *Gini*, *pruning*, *bagging*, *Random Forest*, *boosting* |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-08 |
| Bloom | C3 (Menerapkan) → C4 (Menganalisis) |
| Durasi | 150 menit |
| Metode | Kuliah · Perhitungan manual · Praktikum |
| Penilaian | Observasi (Lab 9) |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menjelaskan** (C2) cara pohon keputusan memilih percabangan.
2. **Menghitung** (C3) *entropy*, *information gain*, dan *Gini impurity* secara manual.
3. **Menerapkan** (C3) *Random Forest* dan *gradient boosting*.
4. **Menganalisis** (C4) mengapa *ensemble* umumnya mengungguli pohon tunggal.
5. **Menafsirkan** (C4) kepentingan fitur beserta keterbatasannya.

---

## Materi Pembelajaran

### 9.1 Pohon Keputusan

#### 9.1.1 Bentuknya

```
                    ┌──────────────────────┐
                    │ omzet_bulanan ≤ 50jt?│
                    └──────────┬───────────┘
                    Ya ────────┴──────── Tidak
                    │                     │
          ┌─────────▼─────────┐  ┌────────▼─────────┐
          │ lama_usaha ≤ 2 th?│  │ rasio_utang≤0,4? │
          └─────────┬─────────┘  └────────┬─────────┘
             Ya ────┴──── Tidak     Ya ───┴─── Tidak
             │            │         │          │
         ┌───▼───┐   ┌────▼───┐ ┌───▼───┐  ┌───▼────┐
         │TOLAK  │   │ TINJAU │ │SETUJU │  │ TINJAU │
         │n=120  │   │ n=85   │ │n=210  │  │ n=45   │
         └───────┘   └────────┘ └───────┘  └────────┘
```

Setiap simpul internal adalah pertanyaan atas satu fitur; setiap daun adalah keputusan. Inilah model yang **paling mudah dijelaskan** kepada orang yang tidak berlatar teknis — kelebihan yang bernilai tinggi pada bidang yang menuntut keterjelasan.

#### 9.1.2 Memilih Percabangan: *Entropy*

$$H(S) = -\sum_{i=1}^{c} p_i \log_2 p_i$$

| Komposisi | Entropy | Makna |
|-----------|---------|-------|
| 50% / 50% | 1,00 | Paling tidak murni |
| 75% / 25% | 0,811 | — |
| 90% / 10% | 0,469 | — |
| 100% / 0% | 0,00 | Murni sempurna |

**Information Gain** — pengurangan entropy setelah percabangan:

$$IG(S, A) = H(S) - \sum_{v \in A} \frac{|S_v|}{|S|} H(S_v)$$

#### 9.1.3 Perhitungan Manual

Data: 100 pengajuan kredit, 60 disetujui (+) dan 40 ditolak (−).

**Entropy induk:**
$$H(S) = -0{,}6\log_2 0{,}6 - 0{,}4\log_2 0{,}4 = 0{,}6(0{,}737) + 0{,}4(1{,}322) = 0{,}971$$

**Percabangan pada `omzet ≤ 50jt`:**

| Cabang | n | Setuju | Tolak | Entropy |
|--------|---|--------|-------|---------|
| Ya | 55 | 20 | 35 | $-\frac{20}{55}\log_2\frac{20}{55} - \frac{35}{55}\log_2\frac{35}{55} = 0{,}946$ |
| Tidak | 45 | 40 | 5 | $-\frac{40}{45}\log_2\frac{40}{45} - \frac{5}{45}\log_2\frac{5}{45} = 0{,}503$ |

$$IG = 0{,}971 - \left(\frac{55}{100}(0{,}946) + \frac{45}{100}(0{,}503)\right) = 0{,}971 - 0{,}747 = \mathbf{0{,}224}$$

Pohon memilih fitur dan titik potong yang memberi **information gain terbesar**, lalu mengulangi proses itu pada tiap cabang.

#### 9.1.4 *Gini Impurity*

$$G(S) = 1 - \sum_{i=1}^{c} p_i^2$$

Untuk data di atas: $G(S) = 1 - (0{,}6^2 + 0{,}4^2) = 1 - 0{,}52 = 0{,}48$.

| Aspek | Entropy | Gini |
|-------|---------|------|
| Perhitungan | Logaritma (lebih lambat) | Kuadrat (lebih cepat) |
| Hasil pohon | Hampir selalu sama | Hampir selalu sama |
| Baku scikit-learn | — | **Gini** |

> Perdebatan Gini vs Entropy jarang bermakna dalam praktik — keduanya menghasilkan pohon yang hampir identik. Yang bermakna adalah **kedalaman pohon**, yang dibahas berikutnya.

---

### 9.2 *Overfitting* pada Pohon

Pohon tanpa batas kedalaman akan tumbuh sampai setiap daun murni — yaitu **menghafal data latih**.

```python
from sklearn.tree import DecisionTreeClassifier

# Tanpa batas — hampir selalu overfit
pohon_bebas = DecisionTreeClassifier(random_state=42)
# Akurasi latih: 1,000  |  Akurasi uji: 0,712

# Dengan pembatasan
pohon_batas = DecisionTreeClassifier(
    max_depth=5,               # kedalaman maksimum
    min_samples_split=20,      # minimum sampel untuk bercabang
    min_samples_leaf=10,       # minimum sampel per daun
    random_state=42,
)
# Akurasi latih: 0,834  |  Akurasi uji: 0,798
```

| Hiperparameter | Pengaruh |
|----------------|----------|
| `max_depth` | Pembatas paling langsung terhadap kompleksitas |
| `min_samples_split` | Mencegah percabangan pada kelompok kecil |
| `min_samples_leaf` | Menjamin tiap daun memuat cukup sampel |
| `ccp_alpha` | *Cost-complexity pruning* — pemangkasan setelah pohon tumbuh |

---

### 9.3 *Ensemble*: Menggabungkan Banyak Model

#### 9.3.1 Mengapa Berhasil

Gagasannya berakar pada statistik: **rata-rata dari banyak penduga yang tidak saling berkorelasi memiliki varians lebih kecil daripada masing-masing penduga**.

$$\text{Var}(\bar{X}) = \frac{\sigma^2}{n} \quad \text{bila saling bebas}$$

Karena itu *ensemble* terutama mengurangi **varians** — yaitu memperbaiki *overfitting*.

#### 9.3.2 *Bagging* dan *Random Forest*

```
    Data latih
        │
   ┌────┼────┬────────┬────────┐   bootstrap sampling
   ▼    ▼    ▼        ▼        ▼
  D₁   D₂   D₃  ...  D₉₉     D₁₀₀
   │    │    │        │        │
   ▼    ▼    ▼        ▼        ▼
  T₁   T₂   T₃  ...  T₉₉     T₁₀₀   pohon dilatih terpisah
   │    │    │        │        │
   └────┴────┴────┬───┴────────┘
                  ▼
         Suara terbanyak (klasifikasi)
         atau rata-rata (regresi)
```

*Random Forest* menambahkan satu hal pada *bagging*: pada setiap percabangan, hanya **sebagian fitur** yang dipertimbangkan secara acak. Ini membuat pohon-pohonnya kurang berkorelasi, sehingga penggabungannya lebih efektif.

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=300,          # jumlah pohon
    max_depth=None,            # pohon boleh dalam — ensemble mengendalikan varians
    max_features="sqrt",       # akar dari jumlah fitur per percabangan
    n_jobs=-1,
    random_state=42,
)
```

#### 9.3.3 *Boosting*

Berbeda dari *bagging* yang melatih pohon secara paralel dan bebas, *boosting* melatihnya **berurutan** — setiap pohon memperbaiki kesalahan pohon sebelumnya.

```
  T₁ ──► residual₁ ──► T₂ ──► residual₂ ──► T₃ ──► ... ──► Tₙ
   │                    │                    │              │
   └────────────────────┴────────────────────┴──────────────┘
                    Jumlah berbobot
```

```python
from sklearn.ensemble import HistGradientBoostingClassifier

gb = HistGradientBoostingClassifier(
    max_iter=300,
    learning_rate=0.1,         # semakin kecil, semakin banyak iterasi dibutuhkan
    max_depth=None,
    early_stopping=True,       # berhenti bila validasi tidak membaik
    random_state=42,
)
```

#### 9.3.4 Perbandingan

| Aspek | Pohon tunggal | *Random Forest* | *Gradient Boosting* |
|-------|---------------|-----------------|---------------------|
| Pelatihan | Cepat | Paralel, cepat | Berurutan, lebih lambat |
| Kinerja khas | Sedang | Baik | **Sering terbaik pada data tabular** |
| Kepekaan hiperparameter | Sedang | **Rendah** | Tinggi |
| Risiko *overfit* | Tinggi | Rendah | Sedang–tinggi bila tidak disetel |
| Keterjelasan | **Sangat tinggi** | Rendah | Rendah |

> **Pada data tabular — yang mendominasi masalah nyata di organisasi Indonesia — *gradient boosting* masih sering mengungguli jaringan saraf dalam.** Ini bukan pengetahuan usang; ia tetap berlaku pada 2026 dan menjadi alasan mengapa Minggu 9–10 memperoleh porsi penuh.

---

### 9.4 Kepentingan Fitur dan Keterbatasannya

```python
import pandas as pd

# (a) Kepentingan bawaan — cepat, tetapi BIAS terhadap fitur
#     berkardinalitas tinggi
kepentingan = pd.Series(rf.feature_importances_, index=X_train.columns)

# (b) Permutation importance — lebih dapat dipercaya
from sklearn.inspection import permutation_importance
hasil = permutation_importance(rf, X_test, y_test, n_repeats=10, random_state=42)
kepentingan_perm = pd.Series(hasil.importances_mean, index=X_test.columns)
```

| Metode | Kelebihan | Kelemahan |
|--------|-----------|-----------|
| Bawaan (`feature_importances_`) | Gratis, langsung tersedia | **Bias ke fitur berkardinalitas tinggi**; dihitung pada data latih |
| *Permutation importance* | Dihitung pada data uji; bebas model | Lebih lambat; terganggu bila fitur berkorelasi kuat |

#### 9.4.1 Tiga Kekeliruan Menafsirkan Kepentingan Fitur

| Kekeliruan | Yang sebenarnya |
|------------|-----------------|
| "Fitur penting berarti menyebabkan target" | Kepentingan adalah **hubungan prediktif**, bukan sebab-akibat |
| "Fitur dengan kepentingan nol tidak berguna" | Bisa jadi ia berkorelasi kuat dengan fitur lain yang sudah dipakai |
| "Urutan kepentingan itu pasti" | Ia berubah antar-*seed* dan antar-lipatan; laporkan sebarannya |

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 8 buku ajar](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md).
- Meninjau hasil UTS bila sudah dibagikan.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 15' | Pembahasan UTS; kesalahan yang paling sering |
| Konsep | 30' | Pohon keputusan; *entropy* dan *Gini* |
| Latihan | 25' | **Perhitungan manual** *entropy* dan *information gain* satu percabangan |
| Konsep | 30' | *Overfitting* pada pohon; *bagging*; *Random Forest*; *boosting* |
| Demonstrasi | 30' | Membandingkan pohon tunggal vs RF vs GB; menampilkan struktur pohon |
| Penutup | 20' | Kepentingan fitur dan keterbatasannya; penugasan |

**Demonstrasi yang wajib:** menampilkan pohon tunggal dengan `plot_tree` pada kedalaman 3, lalu menanyakan kepada mahasiswa apa keputusan yang diambil untuk satu contoh tertentu. Keterjelasan ini menjadi pembanding ketika membahas model yang tidak transparan pada Minggu 13–14.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 9](../04-labs/lab-09-pohon-keputusan-dan-ensemble.md).
- Melanjutkan proyek; Milestone 2 jatuh tempo Minggu 11.

---

## Penugasan

**T-09 — Pohon Keputusan dan *Ensemble***

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook Colab + perhitungan manual |
| Isi | (a) **Perhitungan manual** *entropy* dan *information gain* satu percabangan, diverifikasi dengan `scikit-learn`; (b) Pohon tunggal tanpa dan dengan pembatasan, dengan skor latih dan uji; (c) *Random Forest* dan *gradient boosting*; (d) Perbandingan keempatnya dengan protokol sama; (e) Kepentingan fitur bawaan **dan** permutasi, beserta pembahasan selisihnya |
| Tenggat | Awal pertemuan Minggu 10 |
| Bobot | 1,9% (Observasi) |

---

## Rangkuman

1. Pohon memilih percabangan yang memberi **information gain terbesar** (atau penurunan Gini terbesar).
2. **Entropy dan Gini** hampir selalu menghasilkan pohon yang sama; yang menentukan adalah **kedalaman**.
3. Pohon tanpa batas **menghafal data latih**; pembatasan kedalaman wajib.
4. *Ensemble* bekerja karena **rata-rata penduga tak berkorelasi memiliki varians lebih kecil**.
5. *Random Forest* = *bagging* + pemilihan fitur acak per percabangan.
6. *Boosting* melatih pohon **berurutan**, masing-masing memperbaiki kesalahan sebelumnya.
7. Pada **data tabular**, *gradient boosting* masih sering terbaik — termasuk terhadap jaringan dalam.
8. Pohon tunggal **paling mudah dijelaskan**; *ensemble* mengorbankan keterjelasan demi kinerja.
9. Kepentingan bawaan **bias terhadap kardinalitas tinggi**; gunakan *permutation importance*.
10. Kepentingan fitur adalah **hubungan prediktif**, bukan sebab-akibat.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 6–7. O'Reilly.
2. James, G., et al. (2023). *An Introduction to Statistical Learning with Python*, Bab 8. Springer.
3. Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5–32.
4. Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022). Why Do Tree-Based Models Still Outperform Deep Learning on Tabular Data? *NeurIPS*.
5. Strobl, C., et al. (2007). Bias in Random Forest Variable Importance Measures. *BMC Bioinformatics*, 8(25).
6. Dokumentasi scikit-learn — *Ensemble methods*. <https://scikit-learn.org/stable/modules/ensemble.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
