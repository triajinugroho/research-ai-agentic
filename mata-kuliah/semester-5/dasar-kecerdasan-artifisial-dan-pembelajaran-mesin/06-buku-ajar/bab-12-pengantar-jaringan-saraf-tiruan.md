# BAB 12: PENGANTAR JARINGAN SARAF TIRUAN

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK082-1` | Menjelaskan struktur perseptron dan *multilayer perceptron* | C2 |
| `DAIML-Sub-CPMK082-1` | Menghitung satu langkah maju dan mundur secara manual | C3 |
| `DAIML-Sub-CPMK082-1` | Menganalisis kapan jaringan saraf tidak lebih unggul daripada model klasik | C4 |

---

## Batas Cakupan Bab Ini

Bab ini memberi **pengantar secukupnya** agar pembaca memahami prinsip kerja jaringan saraf dan dapat menilai kapan ia diperlukan. Arsitektur lanjut — CNN, RNN, Transformer, teknik pelatihan *deep learning* — adalah cakupan mata kuliah **Jaringan Syaraf Tiruan dan Pembelajaran Mendalam (IF52510032)**, yang berjalan pada semester yang sama.

Pembagian ini disepakati agar tidak terjadi tumpang tindih, dan agar keluasan alur pembelajaran mesin klasik pada mata kuliah ini tercakup tuntas.

---

## 12.1 Perseptron

### 12.1.1 Struktur

```
    x₁ ──w₁──┐
             │
    x₂ ──w₂──┼──► Σ (z = Σwᵢxᵢ + b) ──► σ(z) ──► keluaran
             │
    x₃ ──w₃──┘
             ▲
             b (bias)
```

$$z=\sum_i w_ix_i+b \qquad \hat{y}=\sigma(z)$$

Bentuk ini **identik dengan regresi logistik** ketika $\sigma$ adalah sigmoid. Satu perseptron = satu regresi logistik. Kekuatan jaringan seluruhnya datang dari penyusunannya berlapis.

### 12.1.2 Batas Perseptron Tunggal

```
  x₂                      XOR:
   ▲                      (0,0) → 0     Tidak ada satu garis lurus
 1 │ ●        ○           (0,1) → 1     yang dapat memisahkan
   │                      (1,0) → 1     ● dari ○
 0 │ ○        ●           (1,1) → 0
   └──────────────► x₁
     0        1
```

Perseptron tunggal hanya dapat memisahkan data yang **terpisahkan secara linear**. Penemuan batas ini (Minsky & Papert, 1969) menjadi salah satu pemicu musim dingin AI pertama.

Jalan keluarnya — menambahkan lapisan tersembunyi — sudah dikenal secara teoretis, tetapi baru menjadi praktis setelah algoritma *backpropagation* dipopulerkan pada 1986.

---

## 12.2 *Multilayer Perceptron*

```
   Masukan      Lapis Tersembunyi     Keluaran
   ┌────┐         ┌────┐
   │ x₁ ├────────►│ h₁ ├──────┐
   └────┘    ╲ ╱  └────┘      │
   ┌────┐     ╳   ┌────┐      ├────► ŷ
   │ x₂ ├────╱ ╲─►│ h₂ ├──────┤
   └────┘    ╲ ╱  └────┘      │
   ┌────┐     ╳   ┌────┐      │
   │ x₃ ├────╱ ╲─►│ h₃ ├──────┘
   └────┘         └────┘
```

**Teorema hampiran universal:** jaringan dengan satu lapis tersembunyi yang cukup lebar dapat menghampiri fungsi kontinu apa pun dengan ketelitian sembarang.

> Teorema ini sering disalahpahami sebagai janji bahwa jaringan saraf selalu unggul. Ia hanya menyatakan bahwa fungsi itu **dapat dihampiri** — bukan bahwa ia **akan ditemukan** dari data yang tersedia, dalam waktu yang wajar, tanpa *overfitting*.

---

## 12.3 Fungsi Aktivasi

| Fungsi | Rumus | Rentang | Catatan |
|--------|-------|---------|---------|
| **Sigmoid** | $\frac{1}{1+e^{-z}}$ | (0, 1) | Keluaran biner; gradien menghilang pada nilai ekstrem |
| **Tanh** | $\frac{e^z-e^{-z}}{e^z+e^{-z}}$ | (−1, 1) | Berpusat nol; tetap ada gradien menghilang |
| **ReLU** | $\max(0,z)$ | [0, ∞) | **Baku untuk lapis tersembunyi**; cepat |
| **Leaky ReLU** | $\max(\alpha z, z)$ | (−∞, ∞) | Mengatasi "ReLU mati" |
| **Softmax** | $\frac{e^{z_i}}{\sum_j e^{z_j}}$ | (0,1), jumlah 1 | **Lapis keluaran multikelas** |

### 12.3.1 Mengapa Aktivasi Harus Non-Linear

Tanpa aktivasi non-linear, penumpukan lapisan menjadi sia-sia:

$$W_2(W_1x+b_1)+b_2=(W_2W_1)x+(W_2b_1+b_2)=W'x+b'$$

Hasilnya tetap sebuah fungsi linear — sama saja dengan satu lapisan. **Non-linearitas adalah alasan lapisan tersembunyi bermakna.**

---

## 12.4 Pelatihan

### 12.4.1 Fungsi *Loss* dan *Gradient Descent*

| Jenis masalah | *Loss* |
|---------------|--------|
| Regresi | MSE: $\frac{1}{n}\sum(y-\hat{y})^2$ |
| Klasifikasi biner | *Binary cross-entropy* |
| Klasifikasi multikelas | *Categorical cross-entropy* |

$$w \leftarrow w - \eta\frac{\partial L}{\partial w}$$

| Laju pembelajaran η | Akibat |
|---------------------|--------|
| Terlalu kecil | Konvergensi sangat lambat |
| Tepat | Turun mantap ke minimum |
| Terlalu besar | Melompati minimum; *loss* naik-turun atau meledak |

### 12.4.2 *Backpropagation* — Perhitungan Manual

Jaringan 2-2-1, aktivasi sigmoid, satu contoh: $x=[1,0]$, target $y=1$, $\eta=0{,}1$.

**Bobot awal:**

| Lapis | Bobot |
|-------|-------|
| Masukan → tersembunyi | $w_{11}=0{,}5$, $w_{12}=0{,}3$, $w_{21}=0{,}2$, $w_{22}=0{,}4$; bias 0 |
| Tersembunyi → keluaran | $v_1=0{,}6$, $v_2=0{,}7$; bias 0 |

**Konvensi pembulatan:** setiap nilai dihitung dengan presisi penuh dari nilai sebelumnya, lalu **ditampilkan dalam 4 desimal** — sama dengan keluaran kode Lab 13 (Langkah 1–2). Bila Anda membulatkan di setiap langkah, digit keempat dapat bergeser ±0,0001.

**Langkah maju:**

$$z_1=0{,}5(1)+0{,}2(0)+0=0{,}5 \qquad h_1=\sigma(0{,}5)=0{,}6225$$
$$z_2=0{,}3(1)+0{,}4(0)+0=0{,}3 \qquad h_2=\sigma(0{,}3)=0{,}5744$$
$$z_{\text{out}}=0{,}6(0{,}6225)+0{,}7(0{,}5744)=0{,}3735+0{,}4021=0{,}7756$$
$$\hat{y}=\sigma(0{,}7756)=0{,}6847$$

**Loss (MSE):** $L=(1-0{,}6847)^2=0{,}0994$

**Langkah mundur:**

$$\frac{\partial L}{\partial\hat{y}}=-2(y-\hat{y})=-2(0{,}3153)=-0{,}6305$$
$$\sigma'(z_{\text{out}})=\hat{y}(1-\hat{y})=0{,}6847(0{,}3153)=0{,}2159$$
$$\delta_{\text{out}}=-0{,}6305\times 0{,}2159=-0{,}1361$$

Pada baris pertama, $-2 \times 0{,}3153$ dari angka yang sudah dibulatkan memberi $-0{,}6306$; nilai presisi penuh $1-\hat{y}=0{,}31527\ldots$ memberi $-0{,}6305$. Inilah contoh pergeseran digit keempat yang dimaksud konvensi di atas.

$$\frac{\partial L}{\partial v_1}=\delta_{\text{out}}\cdot h_1=-0{,}1361\times 0{,}6225=-0{,}0847$$
$$\frac{\partial L}{\partial v_2}=\delta_{\text{out}}\cdot h_2=-0{,}1361\times 0{,}5744=-0{,}0782$$

**Pembaruan bobot:**

$$v_1\leftarrow 0{,}6-0{,}1(-0{,}0847)=0{,}6085 \qquad v_2\leftarrow 0{,}7-0{,}1(-0{,}0782)=0{,}7078$$

Keduanya **naik** — tepat sebagaimana diharapkan, karena prediksi (0,6847) masih di bawah target (1).

**Gradien merambat ke lapis tersembunyi:**

$$\delta_{h_1}=\delta_{\text{out}}\cdot v_1\cdot h_1(1-h_1)=-0{,}1361\times 0{,}6\times 0{,}6225\times 0{,}3775=-0{,}0192$$

Inilah yang dimaksud "*back*propagation": gradien merambat mundur dari keluaran ke masukan melalui aturan rantai.

> Perhitungan semacam ini muncul pada UAS. Yang diuji adalah **pemahaman alurnya**, bukan kecepatan berhitung; angka dipilih agar dapat dikerjakan dengan kalkulator biasa.

---

## 12.5 JST dengan scikit-learn

```python
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# PENSKALAAN WAJIB — JST sangat peka terhadap skala masukan
model = Pipeline([
    ("skala", StandardScaler()),
    ("mlp", MLPClassifier(
        hidden_layer_sizes=(64, 32), activation="relu", solver="adam",
        alpha=1e-4, learning_rate_init=1e-3, max_iter=500,
        # early_stopping memantau AKURASI validasi — pada data tak seimbang, baca 12.5.2
        early_stopping=True, n_iter_no_change=20, random_state=42)),
])
```

| Hiperparameter | Pengaruh |
|----------------|----------|
| `hidden_layer_sizes` | Kapasitas; makin besar makin rawan *overfit* |
| `alpha` | Regularisasi L2; nilai lebih besar meredam *overfitting* |
| `learning_rate_init` | Ukuran langkah |
| `early_stopping` | **Disarankan** bila kelas cukup seimbang — pertahanan terhadap *overfitting*; pada data tak seimbang, periksa dulu (12.5.2) |

### 12.5.1 Membaca Kurva *Loss*

| Pola kurva | Diagnosis |
|------------|-----------|
| Turun mantap lalu mendatar | Normal |
| Naik-turun tajam | Laju pembelajaran terlalu besar |
| Turun sangat lambat | Laju terlalu kecil, atau **data belum diskalakan** |
| Latih terus turun, validasi naik | *Overfitting* — aktifkan `early_stopping` atau perbesar `alpha` |
| Akurasi validasi datar di sekitar proporsi kelas mayoritas | `early_stopping` tidak dapat bekerja — lihat 12.5.2 |

### 12.5.2 Catatan: `early_stopping` pada Data Tak Seimbang

Dengan `early_stopping=True`, `MLPClassifier` menyisihkan sebagian data latih (`validation_fraction`, bawaan 10%) sebagai data validasi dan **memantau akurasinya** — bukan *loss*, bukan ROC-AUC. Pelatihan berhenti bila akurasi validasi tidak membaik lebih dari `tol` selama `n_iter_no_change` iterasi berturut-turut, lalu bobot **dikembalikan ke iterasi dengan akurasi validasi tertinggi**.

Pada data tak seimbang, mekanisme ini mudah tertipu. Bila hanya 11% data positif, model yang selalu menebak kelas mayoritas sudah mencapai akurasi ±89% sejak iterasi pertama. Akurasi validasi lalu datar, sehingga:

- pelatihan berhenti terlalu dini; dan
- bila akurasi tidak pernah melampaui nilai iterasi pertama, bobot yang dipulihkan adalah **bobot iterasi pertama** — model yang hampir belum belajar.

Pada data Lab 13 (11% positif), varian `early_stopping=True` dari konfigurasi Lab 13 Langkah 4 (`alpha=1.0`) menghasilkan ROC-AUC validasi silang ±0,44 — **lebih buruk daripada tebakan acak** di kelima lipatan. Konfigurasi contoh di atas (`alpha=1e-4`) tidak jauh lebih baik: ±0,55, dengan tiga dari lima lipatan di bawah 0,5.

Menaikkan `n_iter_no_change` memberi pelatihan lebih banyak kesempatan, tetapi **tidak menjamin** perbaikan: bila akurasi validasi memang tidak bergerak, kesabaran berapa pun tetap memulihkan bobot iterasi pertama. Pilihan yang lebih aman:

1. Matikan `early_stopping` dan kendalikan *overfitting* dengan regularisasi `alpha` yang lebih kuat serta batas `max_iter` (konfigurasi Langkah 4 Lab 13).
2. Pantau metrik yang tidak bergantung pada ambang — *log-loss* atau ROC-AUC — pada data validasi sendiri, misalnya dengan memilih `alpha` atau `max_iter` melalui validasi silang.

Apa pun pilihannya, **periksa `validation_scores_`**: kurva akurasi validasi yang datar di sekitar proporsi kelas mayoritas adalah tanda bahaya. Dan jangan pernah menyimpulkan bahwa JST "kalah" dari model lain bila ROC-AUC-nya di bawah 0,5 — itu tanda pelatihannya gagal, bukan hasil perbandingan.

---

## 12.6 Kapan JST Tidak Diperlukan

Ini bagian terpenting bab ini.

| Keadaan | Yang lebih sesuai |
|---------|-------------------|
| **Data tabular** dengan fitur bermakna | ***Gradient boosting*** — sering lebih unggul |
| Data sedikit (< beberapa ribu baris) | Model klasik; JST butuh banyak data |
| Keterjelasan dituntut | Regresi logistik; pohon keputusan |
| Waktu komputasi terbatas | Model klasik |
| *Baseline* belum dibangun | **Bangun *baseline* lebih dahulu** |

> **Temuan yang konsisten dalam literatur:** pada data tabular, metode berbasis pohon masih mengungguli jaringan dalam (Grinsztajn et al., 2022). Ini bukan pengetahuan usang — ia tetap berlaku pada 2026.
>
> Jaringan saraf unggul pada data **tak terstruktur**: citra, suara, teks, dan runtun. Ketiganya adalah cakupan mata kuliah lain pada kurikulum ini.

### 12.6.1 Mengapa Penting Mengetahuinya

Memilih jaringan saraf ketika *gradient boosting* lebih sesuai bukan sekadar pemborosan komputasi. Ia berarti:

- Waktu pelatihan berlipat tanpa peningkatan kinerja.
- Hiperparameter yang jauh lebih banyak untuk disetel.
- Model yang jauh lebih sulit dijelaskan kepada pemangku kepentingan.
- Ketergantungan pada pustaka yang lebih berat untuk penerapan.

Seluruhnya adalah biaya nyata, dibayar untuk sesuatu yang tidak memberi imbalan.

### 12.6.2 Membandingkan Dua Model: Skor Berpasangan

Keputusan "JST atau model klasik" diambil dari perbandingan validasi silang. Karena kedua model dinilai pada **lipatan yang sama**, skor keduanya **berpasangan**: pada lipatan ke-$i$, keduanya diuji pada baris yang persis sama. Sebagian variasi skor berasal dari lipatannya sendiri — ada lipatan yang "mudah", ada yang "sulit" — dan dialami kedua model bersama-sama. Selisih per lipatan menghapus variasi bersama itu.

Untuk $k$ lipatan, hitung selisih per lipatan $d_i = \text{skor}_{A,i} - \text{skor}_{B,i}$, lalu laporkan rerata, simpangan baku sampel, dan galat baku rerata selisih:

$$\bar d=\frac{1}{k}\sum_{i=1}^{k} d_i \qquad s_d=\sqrt{\frac{1}{k-1}\sum_{i=1}^{k}\left(d_i-\bar d\right)^2} \qquad SE=\frac{s_d}{\sqrt{k}}$$

**Aturan praktis mata kuliah:** selisih dianggap bermakna bila $|\bar d| > 2\cdot SE$ **dan** arahnya konsisten di sebagian besar lipatan (pada 5 lipatan: minimal 4). Aturan ini penyaring kasar — skor antarlipatan tidak benar-benar saling bebas karena data latihnya tumpang-tindih. Untuk analisis formal, gunakan *corrected resampled t-test* (Nadeau & Bengio, 2003).

```python
import numpy as np

# skor_a, skor_b: skor per lipatan dari cross_val_score dengan objek CV yang SAMA
d = np.asarray(skor_a) - np.asarray(skor_b)
k = len(d)
d_bar = d.mean()
s_d = d.std(ddof=1)        # simpangan baku SAMPEL (ddof=1), sama dengan pd.Series.std()
se = s_d / np.sqrt(k)
searah = int((np.sign(d) == np.sign(d_bar)).sum())
bermakna = abs(d_bar) > 2 * se and searah >= 0.8 * k
```

> **Jangan pakai "simpangan gabungan" $\sqrt{s_1^2+s_2^2}$.** Rumus itu memperlakukan skor kedua model seolah-olah tidak berpasangan dan memakai simpangan baku (SD) skor masing-masing model, padahal ketidakpastian **rerata selisih** diukur oleh galat baku (SE) dari selisih per lipatan. Akibatnya, selisih yang konsisten di semua lipatan dapat dinyatakan "tidak bermakna" hanya karena kedua model sama-sama naik-turun dari lipatan ke lipatan.
>
> Seragamkan pula cara menghitung simpangan baku skor lipatan: selalu **`ddof=1`** — `np.std(x, ddof=1)` atau `pd.Series.std()`. `np.std(x)` tanpa argumen memakai `ddof=0`.

---

## AI Corner — Tahap *Create*

### Kekeliruan AI yang Paling Konsisten di Bab Ini

Diminta merekomendasikan model untuk data tabular berukuran sedang, model bahasa cukup sering menyarankan jaringan saraf. Penyebabnya dapat diperkirakan: teks yang melatihnya sarat dengan pembahasan *deep learning*, yang mendominasi publikasi satu dekade terakhir.

Saran itu bertentangan dengan temuan empiris yang konsisten. Dan ia **dapat diperiksa dengan mudah**: jalankan keduanya pada data yang sama dengan protokol yang sama, dan bandingkan.

Inilah contoh paling jelas dari prinsip yang berjalan sepanjang buku ini: **keluaran AI adalah dugaan yang harus diuji, bukan jawaban yang diterima**. Pengujiannya di sini memakan waktu lima menit.

### Bahaya Kedua: Arsitektur yang Terlalu Besar

Diminta menuliskan MLP, AI sering menghasilkan arsitektur seperti `(512, 256, 128, 64)` — arsitektur yang wajar untuk data citra berukuran besar, dan berlebihan untuk data tabular 3.000 baris dengan 15 fitur.

Kaidah sederhana: mulai dari yang kecil (`(32,)` atau `(64, 32)`), tambah hanya bila kurva pembelajaran menunjukkan *underfit*. Arsitektur besar pada data kecil menghasilkan *overfitting*, bukan kinerja.

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan mengapa satu perseptron setara dengan satu regresi logistik.

2. Jelaskan mengapa perseptron tunggal tidak dapat mempelajari XOR, dengan bantuan gambar.

3. Buktikan secara aljabar bahwa dua lapisan linear tanpa aktivasi non-linear setara dengan satu lapisan linear.

4. Sebutkan empat fungsi aktivasi dan kapan masing-masing dipakai.

### Tingkat Menengah

5. Sebuah jaringan 2-2-1 dengan sigmoid memiliki $w_{11}=0{,}4$, $w_{12}=0{,}6$, $w_{21}=0{,}3$, $w_{22}=0{,}2$, $v_1=0{,}5$, $v_2=0{,}8$, seluruh bias 0. Masukan $x=[1,1]$, target $y=0$.
   (a) Hitung $z_1$, $z_2$, $h_1$, $h_2$.
   (b) Hitung $z_{\text{out}}$ dan $\hat{y}$.
   (c) Hitung *loss* dengan MSE.
   (d) Hitung $\delta_{\text{out}}$ dan perbarui $v_1$, $v_2$ dengan $\eta=0{,}2$.
   (e) Apakah kedua bobot naik atau turun? Mengapa arah itu masuk akal?

6. Kurva *loss* sebuah MLP naik-turun tajam dan tidak pernah mendatar.
   (a) Apa diagnosisnya?
   (b) Apa yang harus diperiksa lebih dahulu?
   (c) Sebutkan dua tindakan yang tepat.
   (d) Bagaimana cara memastikan tindakan itu berhasil?

7. Sebuah MLP dengan arsitektur `(512, 256, 128)` dilatih pada 800 baris data tabular dengan 12 fitur.
   (a) Berapa kira-kira jumlah parameter yang harus dipelajari?
   (b) Bandingkan dengan jumlah data yang tersedia.
   (c) Apa yang paling mungkin terjadi?
   (d) Apa arsitektur yang lebih masuk akal?

8. Pada data tabular, *Random Forest* dan MLP dinilai dengan validasi silang 5 lipatan yang **sama**. ROC-AUC per lipatan:

   | Lipatan | 1 | 2 | 3 | 4 | 5 |
   |---|---|---|---|---|---|
   | *Random Forest* | 0,862 | 0,888 | 0,852 | 0,894 | 0,859 |
   | MLP | 0,832 | 0,866 | 0,817 | 0,875 | 0,825 |

   (a) Hitung rerata dan simpangan baku (`ddof=1`) skor masing-masing model.
   (b) Hitung selisih per lipatan $d_i$, lalu $\bar d$, $s_d$, dan $SE$. Apakah selisihnya bermakna menurut aturan praktis mata kuliah (12.6.2)?
   (c) Seorang rekan membandingkan selisih rerata dengan "simpangan gabungan" $\sqrt{s_1^2+s_2^2}$. Hitung, lalu jelaskan mengapa cara itu keliru untuk skor validasi silang.
   (d) Apakah hasil ini sesuai dengan literatur? Bagaimana Anda melaporkannya dalam laporan proyek?
   (e) Apakah wajar bila hasil Anda berbeda dari literatur? Apa yang harus diperiksa lebih dahulu (petunjuk: 12.5.2)?

### Tingkat Mahir

9. Implementasikan perseptron dan MLP dari nol dengan NumPy.
   (a) Implementasikan perseptron satu lapis untuk AND dan OR; tunjukkan keduanya berhasil.
   (b) Coba pada XOR; tunjukkan bahwa ia gagal, dan jelaskan mengapa dari batas keputusannya.
   (c) Implementasikan MLP dengan satu lapis tersembunyi berisi 2 neuron.
   (d) Latih pada XOR sampai konvergen.
   (e) Gambarkan batas keputusan yang dihasilkannya.
   (f) Bandingkan dengan `MLPClassifier`.

10. Bandingkan MLP dengan model berbasis pohon pada dua jenis data.
    (a) Data tabular nyata (misalnya indikator BPS atau data transaksi).
    (b) Data dengan pola non-linear rumit (`make_moons` atau `make_circles` dengan derau).
    (c) Pakai protokol yang sama untuk keduanya.
    (d) Laporkan kinerja dan waktu latih.
    (e) Jelaskan mengapa peringkat model berbeda antara kedua jenis data itu.

11. Selidiki pengaruh laju pembelajaran secara sistematis.
    (a) Latih MLP dengan tujuh nilai laju dari $10^{-5}$ sampai $10^{-1}$.
    (b) Gambarkan kurva *loss* seluruhnya pada satu grafik.
    (c) Catat jumlah iterasi sampai konvergen dan kinerja akhir masing-masing.
    (d) Tandai rentang yang terlalu kecil, tepat, dan terlalu besar.
    (e) Jelaskan bentuk kurva pada masing-masing rentang.
    (f) Bandingkan dengan pengaruh `alpha` (regularisasi) — apa bedanya?

---

## Rangkuman

1. **Satu perseptron setara dengan satu regresi logistik.**
2. Perseptron tunggal **tidak dapat mempelajari XOR** — ia hanya memisahkan secara linear.
3. **Non-linearitas adalah alasan lapisan tersembunyi bermakna**; tanpa itu, penumpukan lapisan sia-sia.
4. **ReLU** baku untuk lapis tersembunyi; **softmax** untuk keluaran multikelas.
5. Teorema hampiran universal menyatakan fungsi **dapat** dihampiri — bukan bahwa ia **akan** ditemukan.
6. *Backpropagation* menyebarkan gradien mundur dengan aturan rantai.
7. **Laju terlalu besar** membuat *loss* naik-turun; terlalu kecil membuatnya sangat lambat.
8. **JST wajib diskalakan** dan sangat peka terhadapnya.
9. `early_stopping` dan regularisasi `alpha` adalah pertahanan utama terhadap *overfitting*. `early_stopping` bawaan memantau **akurasi** validasi, sehingga pada data tak seimbang ia dapat berhenti terlalu dini dan memulihkan bobot iterasi pertama — periksa `validation_scores_`.
10. **Pada data tabular, metode berbasis pohon masih sering mengungguli JST.** JST unggul pada data tak terstruktur.
11. Memilih JST ketika model klasik lebih sesuai membawa **biaya nyata** tanpa imbalan.
12. Dua model yang dinilai pada lipatan yang sama dibandingkan dengan **selisih berpasangan per lipatan**: $\bar d$, $s_d$ (`ddof=1`), dan $SE=s_d/\sqrt{k}$ — bukan dengan "simpangan gabungan" $\sqrt{s_1^2+s_2^2}$.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 10. O'Reilly.
2. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*, Bab 6. MIT Press.
3. Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning Representations by Back-Propagating Errors. *Nature*, 323, 533–536.
4. Minsky, M., & Papert, S. (1969). *Perceptrons*. MIT Press.
5. Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022). Why Do Tree-Based Models Still Outperform Deep Learning on Typical Tabular Data? *NeurIPS 2022 (Datasets and Benchmarks Track)*.
6. Dokumentasi scikit-learn — *Neural network models*. <https://scikit-learn.org/stable/modules/neural_networks_supervised.html>
7. Nadeau, C., & Bengio, Y. (2003). Inference for the Generalization Error. *Machine Learning*, 52(3), 239–281.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
