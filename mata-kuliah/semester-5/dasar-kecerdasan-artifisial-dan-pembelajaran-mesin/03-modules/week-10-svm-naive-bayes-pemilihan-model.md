# Minggu 10: SVM, Naive Bayes, dan Pemilihan Model

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 10 dari 16 |
| Topik | SVM dan *kernel*, Naive Bayes, penyetelan hiperparameter, perbandingan model yang adil |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-09 |
| Bloom | C3 (Menerapkan) → C5 (Mengevaluasi) |
| Durasi | 150 menit |
| Metode | Kuliah · Praktikum · Diskusi hasil |
| Penilaian | Observasi (Lab 10) · **Kuis 3** |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menjelaskan** (C2) gagasan margin maksimum pada SVM dan peran *kernel*.
2. **Menerapkan** (C3) Naive Bayes dan menjelaskan asumsi kebebasannya.
3. **Menerapkan** (C3) penyetelan hiperparameter dengan `GridSearchCV` dan `RandomizedSearchCV`.
4. **Merancang** (C6) protokol perbandingan model yang adil.
5. **Mengevaluasi** (C5) hasil perbandingan dengan memperhatikan ketidakpastiannya.

---

## Materi Pembelajaran

### 10.1 Support Vector Machine

#### 10.1.1 Margin Maksimum

```
        ×  ×            │      ○
     ×     ×      ┊     │    ┊    ○   ○
        ×      ┊        │       ┊   ○
    ×       ┊           │          ┊    ○
          ┊             │             ┊
      ─────┴────────────┴──────────────┴─────
        margin    hiperbidang    margin
        bawah      pemisah        atas

    × dan ○ yang MENYENTUH garis putus-putus
    adalah support vector — hanya mereka yang
    menentukan posisi hiperbidang.
```

SVM tidak sekadar mencari pemisah; ia mencari pemisah dengan **jarak terbesar** ke titik terdekat dari kedua kelas. Gagasan ini memberi ketahanan: pemisah yang berjarak lebar lebih mungkin bertahan pada data baru.

#### 10.1.2 *Kernel*

Ketika data tidak terpisahkan secara linear, *kernel* memetakannya ke ruang berdimensi lebih tinggi tempat pemisahan linear menjadi mungkin — tanpa menghitung pemetaan itu secara eksplisit (*kernel trick*).

| Kernel | Bentuk | Kapan dipakai |
|--------|--------|---------------|
| `linear` | $x_i^\top x_j$ | Data berdimensi tinggi; teks |
| `rbf` | $\exp(-\gamma\|x_i-x_j\|^2)$ | **Baku; paling serbaguna** |
| `poly` | $(\gamma x_i^\top x_j + r)^d$ | Hubungan polinomial |

```python
from sklearn.svm import SVC

# PENSKALAAN WAJIB — SVM berbasis jarak
model = Pipeline([
    ("skala", StandardScaler()),
    ("svm", SVC(kernel="rbf", C=1.0, gamma="scale", probability=True, random_state=42)),
])
```

| Hiperparameter | Pengaruh |
|----------------|----------|
| `C` kecil | Margin lebar, lebih banyak kesalahan ditoleransi → lebih sederhana |
| `C` besar | Margin sempit, kesalahan ditekan → risiko *overfit* |
| `gamma` kecil | Pengaruh tiap titik meluas → batas keputusan halus |
| `gamma` besar | Pengaruh tiap titik sempit → batas keputusan berliku, risiko *overfit* |

> **Keterbatasan penting:** SVM berskala buruk pada data besar (kompleksitas antara $O(n^2)$ dan $O(n^3)$). Pada data di atas puluhan ribu baris, `LinearSVC` atau model lain lebih sesuai.

---

### 10.2 Naive Bayes

#### 10.2.1 Dari Teorema Bayes

$$P(y \mid x_1,\dots,x_p) \propto P(y) \prod_{j=1}^{p} P(x_j \mid y)$$

Tanda perkalian itulah asumsi "naif": **seluruh fitur dianggap saling bebas bila kelasnya diketahui**. Asumsi ini hampir selalu salah dalam kenyataan — dan modelnya sering tetap bekerja baik.

#### 10.2.2 Varian

| Varian | Untuk data | Contoh |
|--------|------------|--------|
| `GaussianNB` | Numerik kontinu | Pengukuran sensor |
| `MultinomialNB` | Cacahan | **Klasifikasi teks** |
| `BernoulliNB` | Biner | Ada/tidaknya kata |
| `CategoricalNB` | Kategorik | Data survei |

| Kelebihan | Kekurangan |
|-----------|------------|
| Sangat cepat dilatih | Asumsi kebebasan sering dilanggar |
| Bekerja pada data kecil | Probabilitas keluarannya kurang terkalibrasi |
| Baik sebagai *baseline* teks | Kalah oleh model lain pada data tabular |

> Naive Bayes layak dicoba sebagai **pembanding cepat** sebelum model yang lebih mahal. Bila model kompleks tidak mengungguli Naive Bayes, ada yang perlu diselidiki.

---

### 10.3 Penyetelan Hiperparameter

#### 10.3.1 Parameter vs Hiperparameter

| | Parameter | Hiperparameter |
|---|-----------|----------------|
| Ditentukan oleh | Proses pelatihan | Manusia atau pencarian |
| Contoh | Koefisien regresi, struktur pohon | `C`, `max_depth`, `n_neighbors` |
| Kapan ditetapkan | Saat `fit` | Sebelum `fit` |

#### 10.3.2 *Grid Search* vs *Random Search*

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import loguniform

# Grid search — mencoba seluruh kombinasi
ruang_grid = {
    "svm__C": [0.1, 1, 10, 100],
    "svm__gamma": [0.001, 0.01, 0.1, 1],
    "svm__kernel": ["rbf", "linear"],
}
pencarian = GridSearchCV(model, ruang_grid, cv=5, scoring="f1", n_jobs=-1)

# Random search — mencoba n kombinasi acak; lebih efisien pada ruang besar
ruang_acak = {
    "svm__C": loguniform(1e-2, 1e3),
    "svm__gamma": loguniform(1e-4, 1e1),
}
pencarian = RandomizedSearchCV(model, ruang_acak, n_iter=50, cv=5,
                               scoring="f1", random_state=42, n_jobs=-1)

pencarian.fit(X_train, y_train)          # HANYA data latih
print("Terbaik:", pencarian.best_params_)
print("Skor CV:", pencarian.best_score_)
```

> **Perhatikan penamaan `svm__C`.** Dua garis bawah menghubungkan nama langkah dalam `Pipeline` dengan nama parameternya. Dengan begitu parameter prapemrosesan pun dapat disetel dalam pencarian yang sama.

#### 10.3.3 Kesalahan Paling Umum dalam Penyetelan

| Kesalahan | Akibat |
|-----------|--------|
| Menyetel pada data uji | Skor uji menjadi optimistis; kebocoran pemilihan |
| Melaporkan `best_score_` sebagai kinerja akhir | Skor itu sudah dioptimalkan, sehingga bias ke atas |
| Ruang pencarian terlalu sempit | Nilai optimum berada di tepi ruang — perluas |
| Hanya melaporkan rerata, tanpa memeriksa selisih per lipatan | Perbedaan yang dilaporkan bisa tidak bermakna (§10.4.2) |

**Yang benar:** setel pada data latih dengan validasi silang; laporkan kinerja akhir pada data uji yang disentuh **sekali**.

#### 10.3.4 Validasi Silang Bersarang

Bila penyetelan dan penaksiran kinerja harus dilakukan dari data yang sama:

```python
from sklearn.model_selection import cross_val_score, KFold

# Lingkar dalam: memilih hiperparameter
# Lingkar luar: menaksir kinerja
lingkar_dalam = KFold(n_splits=5, shuffle=True, random_state=42)
lingkar_luar  = KFold(n_splits=5, shuffle=True, random_state=7)

pencarian = GridSearchCV(model, ruang_grid, cv=lingkar_dalam, scoring="f1")
skor = cross_val_score(pencarian, X, y, cv=lingkar_luar, scoring="f1")

print(f"Taksiran kinerja yang tidak bias: {skor.mean():.3f} ± {skor.std(ddof=1):.3f}")   # ddof=1
```

---

### 10.4 Merancang Perbandingan Model yang Adil

#### 10.4.1 Lima Syarat

| Syarat | Mengapa |
|--------|---------|
| **Lipatan yang sama** untuk seluruh model | Perbedaan lipatan dapat lebih besar daripada perbedaan model |
| **Prapemrosesan yang sesuai** tiap model | Tidak adil membandingkan SVM tanpa penskalaan dengan RF |
| **Anggaran penyetelan yang sebanding** | Model yang disetel 100 kali vs 5 kali bukan perbandingan |
| ***Baseline* disertakan** | Tanpa itu, seluruh angka tidak bermakna |
| **Simpangan dan selisih per lipatan dilaporkan** | Selisih rerata 0,01 baru bermakna bila konsisten antarlipatan — diukur dengan selisih berpasangan (§10.4.2), bukan dengan membandingkannya pada simpangan masing-masing model |

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score
import pandas as pd

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)   # SAMA untuk semua

kandidat = {
    "Baseline":       pipeline_dummy,
    "Regresi Logistik": pipeline_logreg,
    "k-NN":           pipeline_knn,
    "SVM (RBF)":      pipeline_svm,
    "Random Forest":  pipeline_rf,
    "Grad. Boosting": pipeline_gb,
}

baris, skor_lipatan = [], {}
for nama, pipa in kandidat.items():
    skor = cross_val_score(pipa, X_train, y_train, cv=cv, scoring="f1")
    skor_lipatan[nama] = skor                     # disimpan untuk perbandingan berpasangan
    baris.append({"Model": nama, "F1 rerata": skor.mean(),
                  "Simpangan": skor.std(ddof=1),  # simpangan baku SAMPEL (ddof=1)
                  "Min": skor.min(), "Maks": skor.max()})

tabel = (pd.DataFrame(baris).sort_values("F1 rerata", ascending=False)
           .reset_index(drop=True))
print(tabel.round(3).to_string(index=False))
```

#### 10.4.2 Membaca Hasil Perbandingan

Karena seluruh model dinilai pada **lipatan yang sama**, skor dua model **berpasangan**: pada lipatan ke-$i$, keduanya diuji pada baris yang persis sama. Sebagian variasi skor berasal dari lipatannya sendiri — ada lipatan yang "mudah" dan ada yang "sulit" — dan dialami semua model bersama-sama. Selisih per lipatan menghapus variasi bersama itu. Untuk $k$ lipatan, hitung selisih per lipatan $d_i = \text{skor}_{A,i} - \text{skor}_{B,i}$, reratanya $\bar d$, simpangan baku sampelnya $s_d$ (`ddof=1`), dan galat baku $SE = s_d/\sqrt{k}$ (rumus lengkap: [Bab 9 §9.4.2](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md#942-membaca-hasil-perbandingan) dan [Lampiran A.10](../06-buku-ajar/lampiran.md#a10-perbandingan-model)).

```python
import numpy as np

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

# Peringkat 1 dibandingkan dengan peringkat 2 dari tabel §10.4.1 (lipatan cv yang SAMA)
juara, kedua = tabel.loc[0, "Model"], tabel.loc[1, "Model"]
b12 = banding_berpasangan(skor_lipatan[juara], skor_lipatan[kedua])
print(f"{juara} − {kedua}, per lipatan:", np.round(b12["d"], 4))
print(f"d̄ = {b12['d_bar']:+.4f} | s_d = {b12['s_d']:.4f} | SE = {b12['SE']:.4f} "
      f"| batas 2·SE = {2 * b12['SE']:.4f} | searah {b12['searah']}/{b12['k']}")
if b12["bermakna"]:
    print(f"Kesimpulan: {juara} lebih baik daripada {kedua} secara bermakna.")
else:
    print(f"Kesimpulan: TIDAK DAPAT DISIMPULKAN bahwa {juara} lebih baik daripada {kedua}.")
```

| Hasil | Tafsir |
|-------|--------|
| $\lvert\bar d\rvert > 2\cdot SE$ **dan** arah selisih konsisten di sebagian besar lipatan (pada 5 lipatan: minimal 4) | Perbedaan kemungkinan nyata |
| $\lvert\bar d\rvert \le 2\cdot SE$, atau arah selisih berganti-ganti antarlipatan | **Tidak dapat disimpulkan mana yang lebih baik** |
| Seluruh model ≈ *baseline* | Fitur tidak memuat sinyal untuk target ini |
| Model sederhana ≈ model kompleks | **Pilih yang sederhana** — lebih mudah dipelihara dan dijelaskan |

Aturan $|\bar d| > 2\cdot SE$ adalah **aturan praktis mata kuliah** — penyaring kasar, karena skor antarlipatan tidak benar-benar saling bebas (data latihnya tumpang-tindih). Untuk analisis formal, gunakan *corrected resampled t-test* (Nadeau & Bengio, 2003).

> **Jangan bandingkan selisih rerata dengan simpangan masing-masing model, dan jangan pakai "simpangan gabungan" $\sqrt{s_1^2+s_2^2}$.** Keduanya memperlakukan skor dua model seolah-olah tidak berpasangan dan memakai simpangan baku (SD) alih-alih galat baku (SE) rerata selisih. Akibatnya, selisih yang konsisten di semua lipatan dapat dinyatakan "tidak bermakna" hanya karena kedua model sama-sama naik-turun dari lipatan ke lipatan. Simpangan baku skor lipatan selalu dihitung dengan **`ddof=1`** — `np.std(x, ddof=1)` atau `pd.Series.std()`; `skor.std()` pada larik NumPy tanpa argumen memakai `ddof=0`.

> Baris terakhir tabel di atas — *model sederhana ≈ model kompleks* — adalah kaidah yang sering diabaikan. Model yang lebih rumit hanya sepadan bila peningkatannya nyata dan bermakna secara praktis, bukan sekadar lebih besar pada angka desimal ketiga.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 9 buku ajar](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md).
- Meninjau kembali Teorema Bayes dari Probabilitas dan Statistik (Bab 5).

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Tinjauan; pembahasan T-09 |
| **Kuis 3** | 20' | Protokol eksperimen dan penyetelan |
| Konsep | 30' | SVM dan margin; *kernel*; Naive Bayes |
| Konsep | 25' | Penyetelan hiperparameter; kesalahan umum; CV bersarang |
| Demonstrasi | 40' | **Kegiatan inti:** membangun tabel perbandingan enam model dengan protokol yang adil |
| Penutup | 25' | Membaca hasil; kapan memilih model sederhana; penugasan |

**Diskusi yang wajib muncul:** pada tabel perbandingan, tunjukkan kasus ketika model terbaik hanya unggul $\bar d = 0{,}004$ dari model kedua, dengan selisih per lipatan yang berganti tanda (misalnya unggul di 3 lipatan dan kalah di 2) sehingga $|\bar d| \le 2\cdot SE$. Tanyakan: model mana yang sebaiknya dipakai, dan mengapa? Jawaban yang diharapkan menyatakan bahwa keduanya tidak dapat dibedakan, lalu mempertimbangkan kemudahan pemeliharaan dan keterjelasan, bukan hanya angka. Bandingkan dengan kasus selisih kecil yang searah di kelima lipatan **dan** lolos aturan $|\bar d| > 2\cdot SE$ (searah 5/5 saja belum cukup — lihat tahap *+ domain* di [Lab 5 Langkah 8](../04-labs/lab-05-rekayasa-fitur.md#langkah-8-ringkasan-dan-analisis): naik di kelima lipatan, tetapi $|\bar d| \approx 1{,}9 \cdot SE$): apakah selisih yang bermakna menurut aturan itu otomatis bermakna secara praktis?

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 10](../04-labs/lab-10-svm-naive-bayes-penyetelan.md).
- Menyelesaikan Milestone 2 proyek (jatuh tempo Minggu 11).

---

## Penugasan

**T-10 — SVM, Naive Bayes, dan Penyetelan**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook Colab |
| Isi | (a) SVM dengan tiga *kernel*, dalam `Pipeline` berpenskalaan; (b) Naive Bayes sebagai pembanding cepat; (c) `GridSearchCV` **pada data latih saja**; (d) Tabel perbandingan lima model dengan lipatan yang sama, memuat rerata, simpangan baku sampel (`ddof=1`), min, dan maks; (e) **Kesimpulan berdasarkan selisih berpasangan per lipatan** terhadap model terbaik ($\bar d$, $s_d$, $SE = s_d/\sqrt{k}$), bukan hanya rerata |
| Tenggat | Awal pertemuan Minggu 11 |
| Bobot | 1,875% (Observasi, Sub-CPMK082-1) |

---

## Rangkuman

1. SVM mencari pemisah dengan **margin terbesar**; hanya *support vector* yang menentukannya.
2. ***Kernel*** memungkinkan pemisahan non-linear tanpa menghitung pemetaannya secara eksplisit.
3. **SVM wajib diskalakan** dan berskala buruk pada data besar.
4. Naive Bayes mengandaikan **kebebasan antarfitur** — hampir selalu salah, sering tetap berguna.
5. **Hiperparameter disetel sebelum `fit`**; penyetelan dilakukan **hanya pada data latih**.
6. `best_score_` **bukan** kinerja akhir — ia sudah dioptimalkan.
7. Nilai optimum di tepi ruang pencarian berarti ruangnya perlu diperluas.
8. **Validasi silang bersarang** memberi taksiran kinerja yang tidak bias.
9. Perbandingan yang adil menuntut **lipatan sama, anggaran setara, *baseline*, dan pelaporan simpangan (`ddof=1`) serta selisih per lipatan**.
10. **Dua model dibandingkan secara berpasangan:** selisih per lipatan $d_i$, rerata $\bar d$, dan $SE = s_d/\sqrt{k}$. Selisih baru dianggap bermakna bila $|\bar d| > 2\cdot SE$ dan arahnya konsisten di sebagian besar lipatan; bila tidak, keduanya tidak dapat dibedakan — pilih yang sederhana.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 5. O'Reilly.
2. James, G., et al. (2023). *An Introduction to Statistical Learning with Python*, Bab 9. Springer.
3. Cortes, C., & Vapnik, V. (1995). Support-Vector Networks. *Machine Learning*, 20(3), 273–297.
4. Bergstra, J., & Bengio, Y. (2012). Random Search for Hyper-Parameter Optimization. *JMLR*, 13, 281–305.
5. Cawley, G. C., & Talbot, N. L. C. (2010). On Over-fitting in Model Selection and Subsequent Selection Bias. *JMLR*, 11, 2079–2107.
6. Nadeau, C., & Bengio, Y. (2003). Inference for the Generalization Error. *Machine Learning*, 52(3), 239–281.
7. Dokumentasi scikit-learn — *Tuning the hyper-parameters*. <https://scikit-learn.org/stable/modules/grid_search.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
