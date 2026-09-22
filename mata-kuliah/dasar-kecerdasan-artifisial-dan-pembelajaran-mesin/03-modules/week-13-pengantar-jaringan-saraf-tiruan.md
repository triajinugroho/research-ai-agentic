# Minggu 13: Pengantar Jaringan Saraf Tiruan

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 13 dari 16 |
| Topik | Perseptron, MLP, fungsi aktivasi, *loss*, *gradient descent*, *backpropagation* |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-12 |
| Bloom | C2 (Memahami) → C4 (Menganalisis) |
| Durasi | 150 menit |
| Metode | Kuliah · Perhitungan manual · Praktikum |
| Penilaian | Observasi (Lab 13) · **Kuis 4** |

---

## Batas Cakupan

Pertemuan ini memberi **pengantar secukupnya** agar mahasiswa memahami prinsip kerja jaringan saraf dan dapat menilai kapan ia diperlukan. Arsitektur lanjut — CNN, RNN, Transformer, teknik pelatihan *deep learning* — adalah cakupan mata kuliah **Jaringan Syaraf Tiruan dan Pembelajaran Mendalam (IF52510032)**, yang berjalan pada semester yang sama.

Pembagian ini disepakati agar tidak terjadi tumpang tindih dan agar keluasan alur ML klasik pada mata kuliah ini tercakup tuntas.

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menjelaskan** (C2) struktur perseptron dan *multilayer perceptron*.
2. **Menghitung** (C3) satu langkah maju dan satu langkah mundur secara manual pada jaringan kecil.
3. **Menjelaskan** (C2) peran fungsi aktivasi, fungsi *loss*, dan *gradient descent*.
4. **Menerapkan** (C3) `MLPClassifier` pada data tabular.
5. **Menganalisis** (C4) kapan jaringan saraf **tidak** lebih unggul daripada model klasik.

---

## Materi Pembelajaran

### 13.1 Perseptron

#### 13.1.1 Struktur

```
    x₁ ──w₁──┐
             │
    x₂ ──w₂──┼──► Σ (z = Σwᵢxᵢ + b) ──► σ(z) ──► keluaran
             │
    x₃ ──w₃──┘
             ▲
             b (bias)
```

$$z = \sum_{i} w_i x_i + b \qquad \hat{y} = \sigma(z)$$

Bentuk ini identik dengan regresi logistik ketika $\sigma$ adalah sigmoid. **Satu perseptron = satu regresi logistik.** Kekuatan jaringan datang dari penyusunannya berlapis.

#### 13.1.2 Batas Perseptron Tunggal

Perseptron tunggal hanya dapat memisahkan data yang **terpisahkan secara linear**. Ia tidak dapat mempelajari fungsi XOR:

```
  x₂                      XOR:
   ▲                      (0,0) → 0     Tidak ada satu garis lurus
 1 │ ●        ○           (0,1) → 1     yang dapat memisahkan
   │                      (1,0) → 1     ● dari ○
 0 │ ○        ●           (1,1) → 0
   └──────────────► x₁
     0        1
```

Penemuan batas ini (Minsky & Papert, 1969) menjadi salah satu pemicu musim dingin AI pertama. Jalan keluarnya — menambahkan lapisan tersembunyi — baru menjadi praktis setelah algoritma *backpropagation* dipopulerkan pada 1986.

---

### 13.2 *Multilayer Perceptron*

```
   Masukan      Lapis Tersembunyi     Keluaran
   ┌────┐         ┌────┐
   │ x₁ ├────────►│ h₁ ├──────┐
   └────┘    ╲ ╱  └────┘      │
   ┌────┐     ╳   ┌────┐      ├────►│ ŷ │
   │ x₂ ├────╱ ╲─►│ h₂ ├──────┤
   └────┘    ╲ ╱  └────┘      │
   ┌────┐     ╳   ┌────┐      │
   │ x₃ ├────╱ ╲─►│ h₃ ├──────┘
   └────┘         └────┘
```

**Teorema hampiran universal:** jaringan dengan satu lapis tersembunyi yang cukup lebar dapat menghampiri fungsi kontinu apa pun dengan ketelitian sembarang.

> Teorema ini sering disalahpahami sebagai janji bahwa jaringan saraf selalu unggul. Ia hanya menyatakan bahwa fungsi itu **dapat dihampiri** — bukan bahwa ia **akan ditemukan** dari data yang tersedia, dalam waktu yang wajar, tanpa *overfitting*.

---

### 13.3 Fungsi Aktivasi

| Fungsi | Rumus | Rentang | Catatan |
|--------|-------|---------|---------|
| **Sigmoid** | $\frac{1}{1+e^{-z}}$ | (0, 1) | Keluaran biner; gradien menghilang pada nilai ekstrem |
| **Tanh** | $\frac{e^z - e^{-z}}{e^z + e^{-z}}$ | (−1, 1) | Berpusat nol; tetap ada gradien menghilang |
| **ReLU** | $\max(0, z)$ | [0, ∞) | **Baku untuk lapis tersembunyi**; cepat |
| **Leaky ReLU** | $\max(\alpha z, z)$ | (−∞, ∞) | Mengatasi "ReLU mati" |
| **Softmax** | $\frac{e^{z_i}}{\sum_j e^{z_j}}$ | (0,1), jumlah 1 | **Lapis keluaran multikelas** |

#### 13.3.1 Mengapa Aktivasi Harus Non-Linear

Tanpa aktivasi non-linear, penumpukan lapisan menjadi sia-sia:

$$W_2(W_1 x + b_1) + b_2 = (W_2 W_1) x + (W_2 b_1 + b_2) = W' x + b'$$

Hasilnya tetap sebuah fungsi linear — sama saja dengan satu lapisan. **Non-linearitas adalah alasan lapisan tersembunyi bermakna.**

---

### 13.4 Pelatihan

#### 13.4.1 Fungsi *Loss*

| Jenis masalah | *Loss* | Rumus |
|---------------|--------|-------|
| Regresi | MSE | $\frac{1}{n}\sum (y - \hat{y})^2$ |
| Klasifikasi biner | *Binary cross-entropy* | $-\frac{1}{n}\sum [y\log\hat{y} + (1-y)\log(1-\hat{y})]$ |
| Klasifikasi multikelas | *Categorical cross-entropy* | $-\frac{1}{n}\sum\sum y_{ij}\log\hat{y}_{ij}$ |

#### 13.4.2 *Gradient Descent*

$$w \leftarrow w - \eta \frac{\partial L}{\partial w}$$

```
   Loss
     ▲
     │╲                                    ╱
     │ ●  ← w awal                        ╱
     │  ╲                               ╱
     │   ●                            ╱
     │    ╲                         ╱
     │     ●                      ╱
     │      ╲___              ___╱
     │          ●────●────●──╱     ← minimum
     └──────────────────────────────► w
```

| Laju pembelajaran η | Akibat |
|---------------------|--------|
| Terlalu kecil | Konvergensi sangat lambat |
| Tepat | Turun mantap ke minimum |
| Terlalu besar | Melompati minimum; *loss* naik-turun atau meledak |

#### 13.4.3 *Backpropagation* — Perhitungan Manual

Jaringan 2-2-1, aktivasi sigmoid, satu contoh: $x = [1, 0]$, target $y = 1$.

**Bobot awal:**

| Lapis | Bobot |
|-------|-------|
| Masukan → tersembunyi | $w_{11}=0{,}5$, $w_{12}=0{,}3$, $w_{21}=0{,}2$, $w_{22}=0{,}4$; bias $b_1 = b_2 = 0$ |
| Tersembunyi → keluaran | $v_1 = 0{,}6$, $v_2 = 0{,}7$; bias $c = 0$ |

**Langkah maju:**

$$z_1 = 0{,}5(1) + 0{,}2(0) + 0 = 0{,}5 \qquad h_1 = \sigma(0{,}5) = 0{,}6225$$
$$z_2 = 0{,}3(1) + 0{,}4(0) + 0 = 0{,}3 \qquad h_2 = \sigma(0{,}3) = 0{,}5744$$
$$z_{\text{out}} = 0{,}6(0{,}6225) + 0{,}7(0{,}5744) = 0{,}3735 + 0{,}4021 = 0{,}7756$$
$$\hat{y} = \sigma(0{,}7756) = 0{,}6848$$

**Loss (MSE):** $L = (1 - 0{,}6848)^2 = 0{,}0994$

**Langkah mundur:**

$$\frac{\partial L}{\partial \hat{y}} = -2(y - \hat{y}) = -2(0{,}3152) = -0{,}6304$$
$$\sigma'(z_{\text{out}}) = \hat{y}(1-\hat{y}) = 0{,}6848(0{,}3152) = 0{,}2158$$
$$\delta_{\text{out}} = -0{,}6304 \times 0{,}2158 = -0{,}1360$$

$$\frac{\partial L}{\partial v_1} = \delta_{\text{out}} \cdot h_1 = -0{,}1360 \times 0{,}6225 = -0{,}0847$$
$$\frac{\partial L}{\partial v_2} = \delta_{\text{out}} \cdot h_2 = -0{,}1360 \times 0{,}5744 = -0{,}0781$$

**Pembaruan bobot ($\eta = 0{,}1$):**

$$v_1 \leftarrow 0{,}6 - 0{,}1(-0{,}0847) = 0{,}6085$$
$$v_2 \leftarrow 0{,}7 - 0{,}1(-0{,}0781) = 0{,}7078$$

Keduanya naik — tepat sebagaimana diharapkan, karena prediksi (0,6848) masih di bawah target (1).

> Perhitungan semacam ini muncul pada UAS. Yang diuji adalah **pemahaman alurnya**, bukan kecepatan berhitung; angka dipilih agar dapat dikerjakan dengan kalkulator biasa.

---

### 13.5 JST dengan scikit-learn

```python
from sklearn.neural_network import MLPClassifier

# PENSKALAAN WAJIB — JST sangat peka terhadap skala masukan
model = Pipeline([
    ("skala", StandardScaler()),
    ("mlp", MLPClassifier(
        hidden_layer_sizes=(64, 32),   # dua lapis tersembunyi
        activation="relu",
        solver="adam",
        alpha=1e-4,                    # regularisasi L2
        learning_rate_init=1e-3,
        max_iter=500,
        early_stopping=True,           # berhenti bila validasi tidak membaik
        n_iter_no_change=20,
        random_state=42,
    )),
])
```

| Hiperparameter | Pengaruh |
|----------------|----------|
| `hidden_layer_sizes` | Kapasitas model; makin besar makin rawan *overfit* |
| `alpha` | Regularisasi L2 |
| `learning_rate_init` | Ukuran langkah; terlalu besar membuat *loss* tidak stabil |
| `early_stopping` | **Sangat disarankan** — mencegah *overfitting* |

#### 13.5.1 Memeriksa Kurva *Loss*

```python
import matplotlib.pyplot as plt

mlp = model.named_steps["mlp"]
plt.plot(mlp.loss_curve_, label="Loss latih")
if hasattr(mlp, "validation_scores_"):
    plt.plot(mlp.validation_scores_, label="Skor validasi")
plt.xlabel("Iterasi"); plt.legend()
```

| Pola kurva | Diagnosis |
|------------|-----------|
| Turun mantap lalu mendatar | Normal |
| Naik-turun tajam | Laju pembelajaran terlalu besar |
| Turun sangat lambat | Laju terlalu kecil, atau data belum diskalakan |
| Latih terus turun, validasi naik | *Overfitting* — aktifkan `early_stopping` |

---

### 13.6 Kapan JST Tidak Diperlukan

Ini bagian terpenting pertemuan ini.

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

Karena itu Lab 13 secara khusus meminta mahasiswa membandingkan MLP dengan *Random Forest* pada data tabular yang sama — dan melaporkan hasilnya dengan jujur, apa pun hasilnya.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 12 buku ajar](../06-buku-ajar/bab-12-pengantar-jaringan-saraf-tiruan.md).
- Meninjau kembali regresi logistik (Minggu 7) — perseptron adalah bentuk yang sama.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Tinjauan; pembahasan T-12 |
| **Kuis 4** | 20' | Diagnosis dari kurva; metrik *clustering*; evaluasi model |
| Konsep | 30' | Perseptron; batas XOR; MLP; fungsi aktivasi |
| Latihan | 30' | **Perhitungan manual** satu langkah maju-mundur jaringan 2-2-1 |
| Demonstrasi | 35' | `MLPClassifier`; membaca kurva *loss*; **membandingkan dengan Random Forest** |
| Penutup | 25' | Kapan JST tidak diperlukan; kaitan dengan IF52510032; penugasan |

**Demonstrasi yang wajib:** pada data tabular yang sama, tampilkan hasil *Random Forest* dan MLP berdampingan, lengkap dengan waktu pelatihan. Bila RF menang — yang sering terjadi — itulah pelajarannya, bukan kegagalan demonstrasi.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 13](../04-labs/lab-13-jaringan-saraf-tiruan.md).
- **Menyelesaikan laporan akhir proyek** (jatuh tempo Minggu 14).

---

## Penugasan

**T-13 — Jaringan Saraf Tiruan**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook Colab + perhitungan manual |
| Isi | (a) **Perhitungan manual** satu langkah maju dan mundur jaringan 2-2-1, diverifikasi dengan kode; (b) `MLPClassifier` dengan `early_stopping`; (c) Kurva *loss* beserta diagnosisnya; (d) Pengaruh tiga nilai laju pembelajaran yang berbeda; (e) **Perbandingan MLP dan *Random Forest*** pada data yang sama, dengan waktu pelatihan; (f) Kesimpulan jujur tentang model mana yang lebih sesuai untuk data itu |
| Tenggat | Awal pertemuan Minggu 14 |
| Bobot | 1,9% (Observasi) |

---

## Rangkuman

1. **Satu perseptron setara dengan satu regresi logistik.**
2. Perseptron tunggal **tidak dapat mempelajari XOR** — ia hanya memisahkan secara linear.
3. **Non-linearitas adalah alasan lapisan tersembunyi bermakna**; tanpa itu, penumpukan lapisan sia-sia.
4. **ReLU** baku untuk lapis tersembunyi; **softmax** untuk keluaran multikelas.
5. Teorema hampiran universal menyatakan fungsi **dapat** dihampiri — bukan bahwa ia **akan** ditemukan.
6. *Backpropagation* menyebarkan gradien mundur dengan aturan rantai.
7. **Laju pembelajaran terlalu besar** membuat *loss* naik-turun; terlalu kecil membuatnya sangat lambat.
8. **JST wajib diskalakan** dan sangat peka terhadapnya.
9. `early_stopping` adalah pertahanan utama terhadap *overfitting*.
10. **Pada data tabular, metode berbasis pohon masih sering mengungguli JST.** JST unggul pada data tak terstruktur — cakupan mata kuliah lain.

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
