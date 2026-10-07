# BAB 7: KLASIFIKASI DAN METRIKNYA

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK082-1` | Membangun model klasifikasi dengan regresi logistik dan k-NN | C3 |
| `DAIML-Sub-CPMK082-1` | Menghitung dan menafsirkan seluruh metrik dari matriks konfusi | C3–C4 |
| `DAIML-Sub-CPMK082-1` | Menentukan ambang keputusan berdasarkan biaya kesalahan | C5 |

---

## 7.1 Regresi Logistik

### 7.1.1 Dari Linear ke Probabilitas

Regresi linear menghasilkan bilangan pada rentang tak terbatas — tidak sesuai untuk probabilitas. Fungsi **sigmoid** memetakannya ke [0, 1]:

$$z=\beta_0+\beta_1x_1+\dots+\beta_px_p \qquad P(y=1\mid x)=\sigma(z)=\frac{1}{1+e^{-z}}$$

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

### 7.1.2 *Odds Ratio*

$$\text{odds}=\frac{P}{1-P} \qquad e^{\beta_j}=\text{rasio odds}$$

| $\beta_j$ | $e^{\beta_j}$ | Tafsir |
|-----------|---------------|--------|
| 0,69 | 2,0 | Kenaikan satu satuan **melipatgandakan** odds |
| 0 | 1,0 | Tidak berpengaruh |
| −0,69 | 0,5 | Kenaikan satu satuan **menyetengahkan** odds |

```python
import numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression

model.fit(X_train, y_train)
rasio_odds = pd.Series(np.exp(model.named_steps["clf"].coef_[0]),
                       index=nama_fitur).sort_values(ascending=False)
print(rasio_odds.round(3))
```

> **Perhatikan:** bila fitur sudah diskalakan (`StandardScaler`), tafsirnya menjadi "per satu simpangan baku", bukan "per satu satuan asli". Ini sering luput dan membuat interpretasi keliru.

Regresi logistik tetap banyak dipakai pada bidang yang menuntut keterjelasan — perbankan, kesehatan, kebijakan publik — justru karena koefisiennya dapat dijelaskan kepada orang yang akan terkena keputusannya.

---

## 7.2 k-Nearest Neighbors

Tidak ada pelatihan dalam arti biasa: model menyimpan seluruh data latih, lalu memprediksi dari k tetangga terdekat.

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

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
| Alami untuk multikelas | Buruk pada dimensi tinggi |

---

## 7.3 Matriks Konfusi

```
                        PREDIKSI
                  Negatif    Positif
              ┌───────────┬───────────┐
     Negatif  │    TN     │    FP     │
  A           │           │ (Tipe I)  │
  K           ├───────────┼───────────┤
  T  Positif  │    FN     │    TP     │
  U           │ (Tipe II) │           │
  A           └───────────┴───────────┘
  L
```

| Metrik | Rumus | Menjawab pertanyaan |
|--------|-------|---------------------|
| **Akurasi** | $\frac{TP+TN}{TP+TN+FP+FN}$ | Berapa proporsi prediksi yang benar? |
| **Precision** | $\frac{TP}{TP+FP}$ | Dari yang **diprediksi positif**, berapa yang benar? |
| **Recall** | $\frac{TP}{TP+FN}$ | Dari yang **benar-benar positif**, berapa yang tertangkap? |
| **Spesifisitas** | $\frac{TN}{TN+FP}$ | Dari yang benar negatif, berapa yang tertangkap? |
| **F1** | $2\cdot\frac{P\cdot R}{P+R}$ | Rata-rata harmonik *precision* dan *recall* |

### 7.3.1 Perhitungan Manual

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

$$\text{Akurasi}=\frac{14+950}{1000}=0{,}964 \qquad \text{Precision}=\frac{14}{44}\approx 0{,}318$$
$$\text{Recall}=\frac{14}{20}=0{,}700 \qquad \text{F1}=2\cdot\frac{0{,}318\cdot 0{,}700}{0{,}318+0{,}700}\approx 0{,}437$$

**Pembacaannya:** akurasi 96,4% terdengar sangat baik, tetapi *precision* 0,318 berarti **dua dari tiga peringatan adalah peringatan palsu** — beban kerja besar bagi petugas pemeriksa yang harus menindaklanjutinya.

### 7.3.2 Mengapa Akurasi Menyesatkan

Model yang **selalu** menjawab "wajar" pada kasus di atas:

$$\text{Akurasi}=\frac{980}{1000}=0{,}98 \qquad \text{Recall}=\frac{0}{20}=0$$

Akurasinya **lebih tinggi** daripada model yang sebenarnya bekerja, dan modelnya sama sekali tidak berguna.

> **Ketentuan mata kuliah ini:** melaporkan akurasi sebagai satu-satunya metrik pada data tak seimbang dikenai pengurangan nilai.

---

## 7.4 Ambang Keputusan

Model menghasilkan probabilitas; **ambang mengubahnya menjadi keputusan**, dan ambang adalah pilihan yang harus dipertanggungjawabkan.

| Ambang | Precision | Recall | Kapan dipilih |
|--------|-----------|--------|---------------|
| Rendah (0,2–0,3) | Turun | **Naik** | Melewatkan positif sangat mahal |
| Baku (0,5) | Seimbang | Seimbang | Biaya kedua kesalahan setara |
| Tinggi (0,7–0,8) | **Naik** | Turun | Positif palsu sangat mahal |

### 7.4.1 Menentukan Ambang dari Biaya

Bila biaya FN dan FP dapat ditaksir, pemilihan ambang berhenti menjadi soal selera:

```python
import numpy as np
from sklearn.metrics import confusion_matrix

prob = model.predict_proba(X_test)[:, 1]
BIAYA_FN = 5_000_000     # penipuan lolos
BIAYA_FP =    50_000     # pemeriksaan sia-sia

hasil = []
for t in np.arange(0.05, 0.96, 0.05):
    pred = (prob >= t).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()
    hasil.append((round(t, 2), fn * BIAYA_FN + fp * BIAYA_FP))

ambang_terbaik = min(hasil, key=lambda r: r[1])
print(f"Ambang dengan biaya terendah: {ambang_terbaik[0]} "
      f"(Rp {ambang_terbaik[1]:,.0f})")
```

> Pendekatan ini menjadi kriteria penilaian pada proyek. Melaporkan "kami memakai ambang 0,5" tanpa alasan menunjukkan bahwa pilihan itu tidak dipikirkan.

---

## 7.5 Kurva ROC dan *Precision-Recall*

| Kurva | Sumbu | Ringkasan | Kapan dipakai |
|-------|-------|-----------|---------------|
| **ROC** | FPR vs TPR | AUC | Kelas relatif seimbang |
| **Precision-Recall** | Recall vs Precision | PR-AUC | **Kelas sangat tak seimbang** |

| ROC-AUC | Tafsir |
|---------|--------|
| 0,5 | Setara menebak acak |
| 0,7–0,8 | Dapat diterima |
| 0,8–0,9 | Baik |
| > 0,9 | Sangat baik — **periksa kebocoran** |

### 7.5.1 Mengapa PR-AUC Lebih Jujur pada Data Tak Seimbang

ROC memakai *false positive rate*, yang penyebutnya adalah jumlah negatif. Ketika negatif sangat banyak, penambahan FP hampir tidak menggeser FPR:

$$\text{FPR}=\frac{FP}{FP+TN} = \frac{30}{30+950} \approx 0{,}031$$

Menambah 30 FP lagi hanya menggeser FPR ke 0,061 — nyaris tak terlihat pada kurva. Sementara *precision* anjlok dari 0,318 ke 0,189.

Karena itu, pada data dengan 2% kelas positif, ROC-AUC dapat mencapai 0,90 sementara PR-AUC hanya 0,30 — dan PR-AUC-lah yang menggambarkan kegunaan model yang sebenarnya.

---

## 7.6 Data Tak Seimbang

| Strategi | Cara | Catatan |
|----------|------|---------|
| **Metrik yang tepat** | F1, PR-AUC, *recall* per kelas | **Selalu dilakukan lebih dahulu** |
| Bobot kelas | `class_weight="balanced"` | Sederhana dan aman |
| *Undersampling* | Kurangi kelas mayoritas | Membuang data |
| *Oversampling* | Gandakan kelas minoritas | Risiko *overfit* |
| SMOTE | Bangkitkan contoh sintetis | **Hanya pada data latih, di dalam `Pipeline`** |
| Penyesuaian ambang | Geser ambang keputusan | Sering paling efektif |

> **Peringatan tentang SMOTE:** menerapkannya sebelum pembagian data adalah kebocoran — contoh sintetis yang dibangun dari data uji masuk ke data latih. Ia wajib berada di dalam `imblearn.pipeline.Pipeline`.

Urutan yang benar: **perbaiki metrik lebih dahulu**, baru pertimbangkan mengubah data. Banyak masalah "ketidakseimbangan" sebenarnya adalah masalah "metrik yang keliru dipilih".

---

## AI Corner — Tahap *Apply*

### Kekeliruan Khas AI pada Metrik Klasifikasi

Empat kekeliruan berikut muncul berulang dan layak dikenali:

| Kekeliruan | Contoh keluaran | Mengapa keliru |
|------------|-----------------|----------------|
| Menyarankan akurasi tanpa memeriksa keseimbangan | "Gunakan `accuracy_score` untuk mengukur kinerja" | Menyesatkan pada data timpang |
| Membalik *precision* dan *recall* | "*Precision* adalah proporsi positif yang berhasil ditemukan" | Itu definisi *recall* |
| Menyarankan SMOTE sebelum pembagian | Kode yang menerapkan SMOTE pada `X` penuh | Kebocoran |
| Menafsirkan koefisien terskala sebagai satuan asli | "Setiap kenaikan 1 juta omzet..." padahal fitur sudah distandardisasi | Tafsir salah besaran |

Ketiga kekeliruan pertama dapat dikenali siapa pun yang memahami bab ini. Yang keempat paling sering lolos, karena angkanya tetap tampak masuk akal.

### Pemakaian yang Wajar

Untuk kode: sepenuhnya boleh.

```
Bagaimana cara menampilkan matriks konfusi ternormalisasi per kelas
aktual dengan ConfusionMatrixDisplay?
```

Untuk keputusan: tidak.

```
Saya memilih recall sebagai metrik utama karena melewatkan kasus
penipuan berbiaya sekitar Rp 5 juta, sementara pemeriksaan sia-sia
berbiaya sekitar Rp 50 ribu — rasio 100:1.

Saya menetapkan ambang 0,25 berdasarkan analisis biaya.

Tolong periksa: apakah ada pertimbangan yang saya lewatkan dalam
penalaran ini? Jangan ubah keputusan saya.
```

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan perbedaan *precision* dan *recall* dengan satu kalimat masing-masing, lalu berikan satu kasus di mana masing-masing lebih penting.

2. Sebuah matriks konfusi menunjukkan TN=380, FP=45, FN=25, TP=50.
   (a) Hitung akurasi, *precision*, *recall*, spesifisitas, dan F1.
   (b) Berapa proporsi kelas positif?
   (c) Berapa akurasi model yang selalu menjawab negatif?

3. Jelaskan apa yang dilakukan ambang keputusan, dan mengapa 0,5 bukan pilihan yang selalu tepat.

4. Sebuah model memiliki $\beta = 1{,}10$ untuk suatu fitur. Berapa rasio odds-nya, dan apa artinya?

### Tingkat Menengah

5. Sebuah model penyaring lamaran kerja memiliki *recall* 0,92 dan *precision* 0,31.
   (a) Apa arti kedua angka itu bagi pelamar?
   (b) Apa arti keduanya bagi tim rekrutmen?
   (c) Ke arah mana ambang sebaiknya digeser, dan apa yang dikorbankan?
   (d) Pertimbangan etis apa yang harus disertakan dalam keputusan itu?

6. Pada data dengan 1,5% kelas positif, sebuah model memperoleh ROC-AUC 0,91 dan PR-AUC 0,28.
   (a) Mengapa kedua angka ini bisa sangat berbeda?
   (b) Mana yang lebih menggambarkan kegunaan model?
   (c) Hitung *baseline* PR-AUC untuk data ini.
   (d) Apakah PR-AUC 0,28 lebih baik daripada *baseline*? Berapa kali lipat?

7. Sebuah tim menerapkan SMOTE pada seluruh data, lalu membaginya, dan memperoleh F1 0,94.
   (a) Kebocoran jenis apa ini?
   (b) Jelaskan bagaimana informasi berpindah.
   (c) Apa yang akan terjadi pada F1 setelah diperbaiki?
   (d) Tuliskan cara yang benar.

8. Sebuah model klasifikasi memakai fitur yang sudah distandardisasi, dan koefisien untuk `omzet` adalah 0,85.
   (a) Berapa rasio odds-nya?
   (b) Tafsirkan dengan benar.
   (c) Mengapa "setiap kenaikan 1 juta omzet" adalah tafsir yang keliru?
   (d) Bagaimana cara memperoleh tafsir dalam satuan asli?

### Tingkat Mahir

9. Bangun analisis ambang berbasis biaya secara lengkap.
   (a) Pilih masalah klasifikasi dengan kelas tak seimbang.
   (b) Taksir biaya FN dan FP berdasarkan konteks nyata; **tuliskan dasar penaksirannya**.
   (c) Buat tabel ambang 0,05–0,95 dengan TP, FP, FN, *precision*, *recall*, dan total biaya.
   (d) Buat grafik total biaya terhadap ambang.
   (e) Bandingkan ambang optimum biaya dengan ambang optimum F1 — mengapa berbeda?
   (f) Tuliskan rekomendasi ambang beserta alasannya, seolah untuk pemangku kepentingan non-teknis.

10. Selidiki pengaruh `class_weight`.
    (a) Latih regresi logistik dengan dan tanpa `class_weight="balanced"`.
    (b) Bandingkan matriks konfusi keduanya.
    (c) Bandingkan ambang optimum biaya keduanya.
    (d) Jelaskan apa yang sebenarnya dilakukan `class_weight` pada fungsi *loss*.
    (e) Apakah `class_weight` dan penyesuaian ambang menghasilkan hal yang setara? Jelaskan.

11. Tulislah pedoman satu halaman berjudul *"Melaporkan Kinerja Model Klasifikasi kepada Pemangku Kepentingan Non-Teknis"*. Sertakan: metrik mana yang layak disebut dan mana yang tidak, cara menjelaskan *precision* dan *recall* tanpa istilah teknis, cara menyatakan ambang sebagai pilihan yang dapat ditinjau ulang, dan tiga contoh kalimat sebelum-sesudah perbaikan.

---

## Rangkuman

1. **Sigmoid** mengubah keluaran linear menjadi probabilitas; $e^{\beta}$ adalah **rasio odds**.
2. Pada fitur terskala, tafsir rasio odds adalah **"per satu simpangan baku"**, bukan per satuan asli.
3. **k-NN wajib diskalakan** dan buruk pada dimensi tinggi.
4. **Matriks konfusi adalah dasar seluruh metrik klasifikasi.**
5. *Precision*: dari yang diprediksi positif, berapa benar. *Recall*: dari yang benar positif, berapa tertangkap.
6. **Akurasi menyesatkan pada data tak seimbang** — model yang selalu menjawab mayoritas dapat berakurasi tinggi dan tak berguna.
7. **Ambang keputusan adalah pilihan** yang sebaiknya ditentukan dari biaya kesalahan.
8. **PR-AUC lebih jujur daripada ROC-AUC** ketika kelas sangat timpang.
9. ROC-AUC > 0,9 adalah alasan untuk **memeriksa kebocoran**, bukan merayakan.
10. Penanganan ketidakseimbangan dimulai dari **metrik yang tepat**, bukan dari mengubah data.
11. **SMOTE hanya di dalam `Pipeline`** — di luar itu ia kebocoran.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 3. O'Reilly.
2. James, G., et al. (2023). *An Introduction to Statistical Learning with Python*, Bab 4. Springer.
3. Saito, T., & Rehmsmeier, M. (2015). The Precision-Recall Plot Is More Informative than the ROC Plot. *PLoS ONE*, 10(3).
4. He, H., & Garcia, E. A. (2009). Learning from Imbalanced Data. *IEEE TKDE*, 21(9), 1263–1284.
5. Dokumentasi scikit-learn — *Classification metrics*. <https://scikit-learn.org/stable/modules/model_evaluation.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
