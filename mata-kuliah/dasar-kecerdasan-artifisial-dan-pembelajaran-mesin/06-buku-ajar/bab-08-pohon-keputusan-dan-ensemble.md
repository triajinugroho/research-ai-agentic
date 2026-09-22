# BAB 8: POHON KEPUTUSAN DAN *ENSEMBLE*

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK082-1` | Menghitung *entropy*, *information gain*, dan *Gini impurity* | C3 |
| `DAIML-Sub-CPMK082-1` | Menerapkan *Random Forest* dan *gradient boosting* | C3 |
| `DAIML-Sub-CPMK082-1` | Menganalisis mengapa *ensemble* mengungguli pohon tunggal | C4 |

---

## 8.1 Pohon Keputusan

### 8.1.1 Bentuknya

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

Setiap simpul internal adalah pertanyaan atas satu fitur; setiap daun adalah keputusan.

**Inilah model yang paling mudah dijelaskan** kepada orang yang tidak berlatar teknis. Keputusan atas satu nasabah dapat ditelusuri sebagai rangkaian pertanyaan — kelebihan yang bernilai tinggi pada bidang yang menuntut keterjelasan, dan yang hilang begitu kita beralih ke *ensemble*.

### 8.1.2 Memilih Percabangan

$$H(S)=-\sum_{i=1}^{c}p_i\log_2 p_i \qquad IG(S,A)=H(S)-\sum_{v\in A}\frac{|S_v|}{|S|}H(S_v)$$

| Komposisi | Entropy | Makna |
|-----------|---------|-------|
| 50% / 50% | 1,000 | Paling tidak murni |
| 75% / 25% | 0,811 | — |
| 90% / 10% | 0,469 | — |
| 100% / 0% | 0,000 | Murni sempurna |

### 8.1.3 Perhitungan Manual

100 pengajuan kredit: 60 disetujui (+), 40 ditolak (−).

**Entropy induk:**
$$H(S)=-0{,}6\log_2 0{,}6-0{,}4\log_2 0{,}4 = 0{,}6(0{,}737)+0{,}4(1{,}322)=0{,}971$$

**Percabangan pada `omzet ≤ 50jt`:**

| Cabang | n | Setuju | Tolak | Entropy |
|--------|---|--------|-------|---------|
| Ya | 55 | 20 | 35 | $-\frac{20}{55}\log_2\frac{20}{55}-\frac{35}{55}\log_2\frac{35}{55}=0{,}946$ |
| Tidak | 45 | 40 | 5 | $-\frac{40}{45}\log_2\frac{40}{45}-\frac{5}{45}\log_2\frac{5}{45}=0{,}503$ |

$$IG = 0{,}971-\left(\tfrac{55}{100}(0{,}946)+\tfrac{45}{100}(0{,}503)\right)=0{,}971-0{,}747=\mathbf{0{,}224}$$

Pohon memilih fitur dan titik potong dengan **information gain terbesar**, lalu mengulangi proses itu pada tiap cabang.

### 8.1.4 *Gini Impurity*

$$G(S)=1-\sum_i p_i^2 = 1-(0{,}6^2+0{,}4^2)=0{,}48$$

| Aspek | Entropy | Gini |
|-------|---------|------|
| Perhitungan | Logaritma (lebih lambat) | Kuadrat (lebih cepat) |
| Hasil pohon | Hampir selalu sama | Hampir selalu sama |
| Baku scikit-learn | — | **Gini** |

> Perdebatan Gini vs Entropy jarang bermakna dalam praktik. Yang bermakna adalah **kedalaman pohon**.

---

## 8.2 *Overfitting* pada Pohon

Pohon tanpa batas kedalaman tumbuh sampai setiap daun murni — yaitu **menghafal data latih**.

```python
from sklearn.tree import DecisionTreeClassifier

# Tanpa batas — hampir selalu overfit
pohon_bebas = DecisionTreeClassifier(random_state=42)
# Akurasi latih: 1,000  |  Akurasi uji: 0,712

# Dengan pembatasan
pohon_batas = DecisionTreeClassifier(
    max_depth=5, min_samples_split=20, min_samples_leaf=10, random_state=42)
# Akurasi latih: 0,834  |  Akurasi uji: 0,798
```

| Hiperparameter | Pengaruh |
|----------------|----------|
| `max_depth` | Pembatas paling langsung terhadap kompleksitas |
| `min_samples_split` | Mencegah percabangan pada kelompok kecil |
| `min_samples_leaf` | Menjamin tiap daun memuat cukup sampel |
| `ccp_alpha` | *Cost-complexity pruning* — pemangkasan setelah pohon tumbuh |

Perhatikan bahwa model kedua **lebih buruk pada data latih** dan **lebih baik pada data uji**. Ini adalah gambaran tukar-tambah bias–varians dalam bentuknya yang paling konkret.

---

## 8.3 *Ensemble*

### 8.3.1 Mengapa Berhasil

Gagasannya berakar pada statistik: **rata-rata dari banyak penduga yang tidak saling berkorelasi memiliki varians lebih kecil** daripada masing-masing penduga.

$$\text{Var}(\bar{X})=\frac{\sigma^2}{n} \quad \text{bila saling bebas}$$

Karena itu *ensemble* terutama mengurangi **varians** — yaitu memperbaiki *overfitting*, bukan *underfitting*.

### 8.3.2 *Bagging* dan *Random Forest*

```
    Data latih
        │
   ┌────┼────┬────────┬────────┐   bootstrap sampling
   ▼    ▼    ▼        ▼        ▼
  D₁   D₂   D₃  ...  D₉₉     D₁₀₀
   │    │    │        │        │
   ▼    ▼    ▼        ▼        ▼
  T₁   T₂   T₃  ...  T₉₉     T₁₀₀
   │    │    │        │        │
   └────┴────┴────┬───┴────────┘
                  ▼
     Suara terbanyak / rata-rata
```

*Random Forest* menambahkan satu hal pada *bagging*: pada setiap percabangan, hanya **sebagian fitur** yang dipertimbangkan secara acak. Ini membuat pohon-pohonnya **kurang berkorelasi** — dan menurut rumus di atas, itulah yang membuat penggabungannya efektif.

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=300,       # jumlah pohon
    max_depth=None,         # pohon boleh dalam — ensemble mengendalikan varians
    max_features="sqrt",    # akar jumlah fitur per percabangan
    n_jobs=-1, random_state=42,
)
```

### 8.3.3 *Boosting*

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
    max_iter=300, learning_rate=0.1,
    early_stopping=True,    # berhenti bila validasi tidak membaik
    random_state=42,
)
```

### 8.3.4 Perbandingan

| Aspek | Pohon tunggal | *Random Forest* | *Gradient Boosting* |
|-------|---------------|-----------------|---------------------|
| Pelatihan | Cepat | Paralel, cepat | Berurutan, lebih lambat |
| Kinerja khas | Sedang | Baik | **Sering terbaik pada data tabular** |
| Kepekaan hiperparameter | Sedang | **Rendah** | Tinggi |
| Risiko *overfit* | Tinggi | Rendah | Sedang–tinggi bila tidak disetel |
| Keterjelasan | **Sangat tinggi** | Rendah | Rendah |

> **Pada data tabular — yang mendominasi masalah nyata di organisasi Indonesia — *gradient boosting* masih sering mengungguli jaringan saraf dalam** (Grinsztajn et al., 2022). Ini bukan pengetahuan usang; ia tetap berlaku pada 2026, dan menjadi alasan mengapa bab ini memperoleh porsi penuh.

---

## 8.4 Kepentingan Fitur

```python
import pandas as pd
from sklearn.inspection import permutation_importance

# (a) Kepentingan bawaan — cepat, tetapi BIAS
kepentingan = pd.Series(rf.feature_importances_, index=nama_fitur)

# (b) Permutation importance — lebih dapat dipercaya
hasil = permutation_importance(rf, X_test, y_test, n_repeats=10,
                               scoring="roc_auc", random_state=42)
kepentingan_perm = pd.Series(hasil.importances_mean, index=X_test.columns)
```

| Metode | Kelebihan | Kelemahan |
|--------|-----------|-----------|
| Bawaan | Gratis, langsung tersedia | **Bias ke fitur berkardinalitas tinggi**; dihitung pada data latih |
| Permutasi | Dihitung pada data uji; bebas model | Lebih lambat; terganggu bila fitur berkorelasi kuat |

### 8.4.1 Demonstrasi Biasnya

Tambahkan kolom `kode_cabang` berisi 120 nilai acak yang **sama sekali tidak berhubungan** dengan target. Kepentingan bawaan sering memberinya nilai tinggi — karena kardinalitasnya tinggi, ia menawarkan banyak titik potong dan sering terpilih secara kebetulan. Kepentingan permutasi mendekati nol, sebagaimana seharusnya.

Inilah bias yang diperingatkan Strobl et al. (2007), dan alasan mengapa kepentingan bawaan tidak boleh dilaporkan sendirian.

### 8.4.2 Tiga Kekeliruan Menafsirkan

| Kekeliruan | Yang sebenarnya |
|------------|-----------------|
| "Fitur penting berarti menyebabkan target" | Kepentingan adalah **hubungan prediktif**, bukan sebab-akibat |
| "Fitur dengan kepentingan nol tidak berguna" | Bisa jadi ia berkorelasi kuat dengan fitur lain yang sudah dipakai |
| "Urutan kepentingan itu pasti" | Ia berubah antar-*seed* dan antar-lipatan; **laporkan sebarannya** |

---

## AI Corner — Tahap *Apply → Create*

### Memverifikasi Keluaran AI tentang *Ensemble*

Pada bab ini muncul satu kekeliruan AI yang khas dan layak dikenali: **menyarankan *deep learning* untuk data tabular**.

Diminta merekomendasikan model untuk data tabular berukuran sedang, model bahasa cukup sering menyarankan jaringan saraf — karena teks yang melatihnya sarat dengan pembahasan *deep learning*. Saran itu bertentangan dengan temuan empiris yang konsisten: pada data tabular, metode berbasis pohon masih unggul.

Cara memeriksanya sederhana dan merupakan bagian dari pekerjaan: **jalankan keduanya dan bandingkan** dengan protokol yang sama. Lab 13 secara khusus meminta perbandingan itu.

### Kekeliruan Kedua: Kepentingan Fitur sebagai Sebab

Diberi tabel kepentingan fitur, model bahasa sangat mungkin menuliskan kalimat seperti *"rasio utang adalah faktor yang paling memengaruhi gagal bayar"*. Kata "memengaruhi" adalah klaim sebab-akibat yang **tidak didukung** oleh apa pun dalam perhitungan kepentingan fitur.

Tafsir yang benar: *"rasio utang adalah fitur yang paling berkontribusi pada kemampuan model membedakan kelas"*. Perbedaannya bukan sekadar kehati-hatian bahasa — ia menentukan apakah temuan itu dapat dijadikan dasar kebijakan.

---

## Latihan Soal

### Tingkat Dasar

1. Hitung entropy untuk komposisi berikut:
   (a) 30 positif, 70 negatif.
   (b) 50 positif, 50 negatif.
   (c) 95 positif, 5 negatif.

2. Jelaskan perbedaan *bagging* dan *boosting* dalam cara melatih pohon-pohonnya.

3. Mengapa *Random Forest* memilih sebagian fitur secara acak pada tiap percabangan? Kaitkan dengan rumus varians rata-rata.

4. Sebutkan dua kelebihan pohon tunggal yang hilang pada *ensemble*.

### Tingkat Menengah

5. Sebuah simpul memuat 240 sampel: 150 kelas A, 90 kelas B. Percabangan menghasilkan cabang kiri (140 sampel: 120 A, 20 B) dan cabang kanan (100 sampel: 30 A, 70 B).
   (a) Hitung entropy induk.
   (b) Hitung entropy kedua cabang.
   (c) Hitung *information gain*.
   (d) Hitung Gini induk dan bandingkan kesimpulannya.

6. Sebuah pohon tanpa batas kedalaman memperoleh akurasi latih 1,000 dan akurasi uji 0,68.
   (a) Kondisi apa ini?
   (b) Berapa kira-kira jumlah daunnya dibandingkan jumlah baris data latih?
   (c) Sebutkan tiga cara menanganinya.
   (d) Mengapa *Random Forest* dapat memakai pohon dalam tanpa masalah yang sama?

7. Pada tabel kepentingan fitur, kolom `id_transaksi` menempati peringkat ketiga menurut kepentingan bawaan tetapi mendekati nol menurut permutasi.
   (a) Jelaskan penyebabnya.
   (b) Kepentingan mana yang harus dipercaya?
   (c) Apa yang harus dilakukan terhadap kolom itu?
   (d) Bagaimana kekeliruan ini dapat memengaruhi keputusan yang diambil dari model?

8. Sebuah perbandingan menghasilkan: pohon tunggal ROC-AUC 0,78 ± 0,04; *Random Forest* 0,86 ± 0,02; *gradient boosting* 0,87 ± 0,03.
   (a) Apakah *gradient boosting* jelas lebih baik daripada *Random Forest*?
   (b) Hitung simpangan gabungan antara keduanya.
   (c) Faktor apa selain skor yang layak dipertimbangkan?
   (d) Model mana yang Anda rekomendasikan, dan mengapa?

### Tingkat Mahir

9. Bangun pohon keputusan dari nol secara manual.
   (a) Ambil dataset kecil (20–30 baris) dengan 3 fitur.
   (b) Hitung *information gain* untuk setiap kemungkinan percabangan pada akar.
   (c) Pilih percabangan terbaik dan ulangi untuk kedua cabangnya.
   (d) Gambarkan pohon hasilnya sampai kedalaman 3.
   (e) Bandingkan dengan keluaran `DecisionTreeClassifier(criterion="entropy")`.
   (f) Jelaskan perbedaannya bila ada.

10. Selidiki stabilitas kepentingan fitur.
    (a) Latih *Random Forest* dengan lima *seed* berbeda.
    (b) Catat peringkat kepentingan setiap fitur pada masing-masing.
    (c) Hitung rentang peringkat tiap fitur.
    (d) Fitur mana yang paling stabil dan mana yang paling berubah-ubah?
    (e) Apa implikasinya bagi cara melaporkan kepentingan fitur dalam laporan?

11. Bandingkan pohon, *Random Forest*, *gradient boosting*, dan MLP pada data tabular nyata.
    (a) Pakai protokol yang sama untuk seluruhnya: lipatan sama, anggaran penyetelan sebanding.
    (b) Laporkan rerata, simpangan, dan waktu latih.
    (c) Tentukan apakah selisih peringkat 1 dan 2 lebih besar daripada simpangan gabungan.
    (d) Buat rekomendasi yang mempertimbangkan kinerja, waktu, dan keterjelasan.
    (e) Bandingkan kesimpulan Anda dengan temuan Grinsztajn et al. (2022).

---

## Rangkuman

1. Pohon memilih percabangan dengan **information gain terbesar** (atau penurunan Gini terbesar).
2. **Entropy dan Gini** hampir selalu menghasilkan pohon yang sama; yang menentukan adalah **kedalaman**.
3. Pohon tanpa batas **menghafal data latih**; pembatasan kedalaman wajib.
4. *Ensemble* bekerja karena **rata-rata penduga tak berkorelasi memiliki varians lebih kecil** — karena itu ia memperbaiki *overfitting*, bukan *underfitting*.
5. *Random Forest* = *bagging* + pemilihan fitur acak per percabangan.
6. *Boosting* melatih pohon **berurutan**, masing-masing memperbaiki kesalahan sebelumnya.
7. Pada **data tabular**, *gradient boosting* masih sering terbaik — termasuk terhadap jaringan dalam.
8. Pohon tunggal **paling mudah dijelaskan**; *ensemble* mengorbankan keterjelasan demi kinerja.
9. Kepentingan bawaan **bias terhadap kardinalitas tinggi**; gunakan *permutation importance*.
10. **Kepentingan fitur adalah hubungan prediktif, bukan sebab-akibat**, dan urutannya tidak stabil.

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
