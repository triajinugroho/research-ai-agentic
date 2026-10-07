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

**Langkah maju:**

$$z_1=0{,}5(1)+0{,}2(0)+0=0{,}5 \qquad h_1=\sigma(0{,}5)=0{,}6225$$
$$z_2=0{,}3(1)+0{,}4(0)+0=0{,}3 \qquad h_2=\sigma(0{,}3)=0{,}5744$$
$$z_{\text{out}}=0{,}6(0{,}6225)+0{,}7(0{,}5744)=0{,}3735+0{,}4021=0{,}7756$$
$$\hat{y}=\sigma(0{,}7756)=0{,}6848$$

**Loss (MSE):** $L=(1-0{,}6848)^2=0{,}0994$

**Langkah mundur:**

$$\frac{\partial L}{\partial\hat{y}}=-2(y-\hat{y})=-2(0{,}3152)=-0{,}6304$$
$$\sigma'(z_{\text{out}})=\hat{y}(1-\hat{y})=0{,}6848(0{,}3152)=0{,}2158$$
$$\delta_{\text{out}}=-0{,}6304\times 0{,}2158=-0{,}1360$$

$$\frac{\partial L}{\partial v_1}=\delta_{\text{out}}\cdot h_1=-0{,}1360\times 0{,}6225=-0{,}0847$$
$$\frac{\partial L}{\partial v_2}=\delta_{\text{out}}\cdot h_2=-0{,}1360\times 0{,}5744=-0{,}0781$$

**Pembaruan bobot:**

$$v_1\leftarrow 0{,}6-0{,}1(-0{,}0847)=0{,}6085 \qquad v_2\leftarrow 0{,}7-0{,}1(-0{,}0781)=0{,}7078$$

Keduanya **naik** — tepat sebagaimana diharapkan, karena prediksi (0,6848) masih di bawah target (1).

**Gradien merambat ke lapis tersembunyi:**

$$\delta_{h_1}=\delta_{\text{out}}\cdot v_1\cdot h_1(1-h_1)=-0{,}1360\times 0{,}6\times 0{,}6225\times 0{,}3775=-0{,}01918$$

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
        early_stopping=True, n_iter_no_change=20, random_state=42)),
])
```

| Hiperparameter | Pengaruh |
|----------------|----------|
| `hidden_layer_sizes` | Kapasitas; makin besar makin rawan *overfit* |
| `alpha` | Regularisasi L2 |
| `learning_rate_init` | Ukuran langkah |
| `early_stopping` | **Sangat disarankan** — pertahanan utama terhadap *overfitting* |

### 12.5.1 Membaca Kurva *Loss*

| Pola kurva | Diagnosis |
|------------|-----------|
| Turun mantap lalu mendatar | Normal |
| Naik-turun tajam | Laju pembelajaran terlalu besar |
| Turun sangat lambat | Laju terlalu kecil, atau **data belum diskalakan** |
| Latih terus turun, validasi naik | *Overfitting* — aktifkan `early_stopping` |

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

---

## AI Corner — Tahap *Apply → Create*

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

8. Pada data tabular, *Random Forest* memperoleh ROC-AUC 0,871 ± 0,019 dan MLP 0,843 ± 0,027.
   (a) Apakah selisihnya bermakna? Hitung simpangan gabungan.
   (b) Apakah hasil ini sesuai dengan literatur?
   (c) Bagaimana Anda melaporkannya dalam laporan proyek?
   (d) Apakah wajar bila hasil Anda berbeda dari literatur? Apa yang harus diperiksa?

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
9. `early_stopping` adalah pertahanan utama terhadap *overfitting*.
10. **Pada data tabular, metode berbasis pohon masih sering mengungguli JST.** JST unggul pada data tak terstruktur.
11. Memilih JST ketika model klasik lebih sesuai membawa **biaya nyata** tanpa imbalan.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 10. O'Reilly.
2. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*, Bab 6. MIT Press.
3. Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning Representations by Back-Propagating Errors. *Nature*, 323, 533–536.
4. Minsky, M., & Papert, S. (1969). *Perceptrons*. MIT Press.
5. Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022). Why Do Tree-Based Models Still Outperform Deep Learning on Tabular Data? *NeurIPS*.
6. Dokumentasi scikit-learn — *Neural network models*. <https://scikit-learn.org/stable/modules/neural_networks_supervised.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
