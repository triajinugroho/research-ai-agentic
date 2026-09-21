# BAB 13: AI GENERATIF DAN AI YANG BERTANGGUNG JAWAB

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK082-1` | Menjelaskan prinsip kerja model generatif dan LLM pada tingkat gagasan | C2 |
| `DAIML-Sub-CPMK082-1` | Menganalisis sumber *bias* dalam data dan model | C4 |
| `DAIML-Sub-CPMK082-1` | Mengevaluasi dampak sosial penerapan sebuah model | C5 |

---

## 13.1 Model Generatif

### 13.1.1 Diskriminatif vs Generatif

| Aspek | Diskriminatif | Generatif |
|-------|---------------|-----------|
| Yang dipelajari | $P(y\mid x)$ — batas antarkelas | $P(x)$ atau $P(x,y)$ — sebaran data |
| Kemampuan | Membedakan | **Membangkitkan contoh baru** |
| Contoh | Regresi logistik, SVM, *Random Forest* | LLM, model difusi, VAE, GAN |

Seluruh model pada Bab 6–12 bersifat diskriminatif. Bab ini memperkenalkan sisi lainnya, pada tingkat gagasan.

### 13.1.2 Gagasan *Large Language Model*

Pada intinya, LLM dilatih untuk satu tugas yang sangat sederhana: **memperkirakan token berikutnya**.

```
  "Ibu kota Indonesia adalah" ──► model ──► P(token berikutnya)
                                             ├─ "Jakarta"   0,87
                                             ├─ "Nusantara" 0,06
                                             ├─ "kota"      0,02
                                             └─ ...
```

Dari tugas sesederhana ini, dilatih pada data yang sangat besar, muncul kemampuan yang tampak jauh lebih luas. Tiga hal yang perlu dipahami dari sifat ini:

| Sifat | Akibat |
|-------|--------|
| Model memperkirakan **token yang mungkin**, bukan **fakta yang benar** | Keluaran dapat meyakinkan tetapi salah (*halusinasi*) |
| Pengetahuannya berasal dari data latih | Ada batas waktu pengetahuan; kesalahan dalam data ikut terpelajari |
| Tidak ada mekanisme pemeriksaan kebenaran | **Verifikasi adalah tanggung jawab pemakai** |

> Inilah dasar kebijakan AI mata kuliah ini. Pembatasan pada [RPS §K.1](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md) bukan kekhawatiran akan kecurangan, melainkan pengakuan atas sifat teknis alat itu: ia tidak mengetahui konteks data Anda dan tidak memiliki mekanisme untuk memeriksa kebenarannya sendiri.

---

## 13.2 *Bias* dalam Pembelajaran Mesin

### 13.2.1 Enam Sumber

| Sumber | Penjelasan | Contoh Indonesia |
|--------|------------|------------------|
| **Bias historis** | Data mencerminkan ketidakadilan yang sudah ada | Data penerimaan kerja masa lalu yang timpang gender |
| **Bias representasi** | Sebagian kelompok kurang terwakili | Data kesehatan yang terpusat di Jawa |
| **Bias pengukuran** | Variabel proksi tidak mengukur yang dimaksud | "Jumlah kunjungan puskesmas" sebagai proksi kesehatan — padahal mengukur **akses** |
| **Bias agregasi** | Satu model untuk kelompok yang berbeda sifat | Model tunggal untuk perkotaan dan perdesaan |
| **Bias penerapan** | Model dipakai di luar konteks perancangannya | Model perkotaan diterapkan di daerah terpencil |
| **Bias umpan balik** | Keluaran model memengaruhi data berikutnya | Patroli diarahkan ke wilayah yang diprediksi rawan → lebih banyak kasus tercatat di sana |

Baris terakhir adalah yang paling berbahaya karena **memperkuat dirinya sendiri**:

```
  Model memprediksi wilayah A rawan
           ↓
  Patroli ditingkatkan di A
           ↓
  Lebih banyak pelanggaran TERCATAT di A
           ↓
  Data berikutnya "membuktikan" A memang rawan
           ↓
  Model semakin yakin ────────┘
```

Lingkaran ini dapat berjalan bertahun-tahun tanpa disadari, dan data yang dihasilkannya tampak seperti bukti yang semakin kuat.

### 13.2.2 Model Akurat yang Tetap Merugikan

| Kelompok | n | Akurasi | Recall |
|----------|---|---------|--------|
| Jawa | 8.400 | 0,89 | 0,86 |
| Sumatera | 3.100 | 0,85 | 0,81 |
| Kalimantan | 1.200 | 0,82 | 0,74 |
| Sulawesi | 900 | 0,79 | 0,68 |
| **Papua** | **300** | **0,71** | **0,52** |
| **Keseluruhan** | **13.900** | **0,86** | **0,82** |

Angka keseluruhan (0,86) tampak baik. Bagi penduduk Papua, model ini **melewatkan hampir separuh kasus** yang seharusnya terdeteksi.

> **Inilah alasan audit terpisah per kelompok wajib dilakukan.** Angka agregat menyembunyikan ketimpangan, dan ketimpangan itu paling sering merugikan kelompok yang paling sedikit terwakili dalam data — yang di Indonesia sering juga kelompok yang paling rentan.
>
> Dalam kerangka nilai yang dipegang program studi ini, persoalan itu bukan sekadar persoalan teknis. **Adil (`al-'adl`)** menuntut bahwa sistem yang memengaruhi hidup orang bekerja setara bagi semua; prinsip **tidak menimbulkan kerusakan (`la darar`)** menuntut bahwa dampak buruk pada kelompok mana pun diketahui dan dipertanggungjawabkan — bukan disembunyikan di balik satu angka rata-rata.

---

## 13.3 Mengukur *Fairness*

### 13.3.1 Tiga Ukuran Pokok

| Ukuran | Definisi | Menuntut |
|--------|----------|----------|
| **Demographic parity** | $P(\hat{y}=1\mid A=a)$ sama untuk semua kelompok | Proporsi prediksi positif setara |
| **Equal opportunity** | *Recall* sama untuk semua kelompok | Yang layak memperoleh peluang setara |
| **Equalized odds** | *Recall* **dan** FPR sama | Kedua jenis kesalahan setara |

### 13.3.2 Ketiganya Tidak Dapat Dipenuhi Sekaligus

Kleinberg, Mullainathan, dan Raghavan (2016) membuktikan bahwa ketika angka kejadian dasar (*base rate*) berbeda antarkelompok, ukuran-ukuran ini **saling bertentangan secara matematis**. Tidak ada model yang dapat memenuhi semuanya — bukan karena kurang canggih, melainkan karena tidak mungkin.

> **Konsekuensinya bagi praktik:** *fairness* bukan kotak centang yang dapat dipenuhi, melainkan **pilihan yang harus dinyatakan dan dipertanggungjawabkan**. Insinyur wajib menyatakan ukuran mana yang dipilih, mengapa, dan **apa yang dikorbankan**.

Menyatakan "model kami adil" tanpa menyebut ukuran yang dipakai adalah pernyataan yang tidak bermakna.

### 13.3.3 Mengukurnya

```python
import pandas as pd
from sklearn.metrics import recall_score, precision_score, confusion_matrix

def audit_kelompok(y_true, y_pred, kelompok):
    # Menghitung metrik terpisah per kelompok
    baris = []
    for k in pd.unique(kelompok):
        m = (kelompok == k).values
        yt, yp = y_true[m], y_pred[m]
        tn, fp, fn, tp = confusion_matrix(yt, yp, labels=[0, 1]).ravel()
        baris.append({
            "Kelompok": k, "n": int(m.sum()), "Base rate": yt.mean(),
            "Precision": precision_score(yt, yp, zero_division=0),
            "Recall": recall_score(yt, yp, zero_division=0),
            "FPR": fp / (fp + tn) if (fp + tn) else 0.0,
            "Prop. prediksi positif": yp.mean(),
        })
    return pd.DataFrame(baris).sort_values("n", ascending=False)

tabel = audit_kelompok(y_test, y_pred, X_test["wilayah"])
print(f"Selisih recall maks-min: {tabel['Recall'].max() - tabel['Recall'].min():.3f}")
```

### 13.3.4 Menghapus Atribut Sensitif Tidak Cukup

Membuang kolom "jenis kelamin" atau "wilayah" dari fitur **tidak** membuat model adil. Atribut itu sering dapat diperkirakan kembali dari fitur lain:

| Atribut dibuang | Proksi yang tersisa |
|-----------------|---------------------|
| Wilayah | Kode pos, jarak ke fasilitas, jenis pekerjaan |
| Jenis kelamin | Riwayat cuti, jenis pekerjaan, pola konsumsi |
| Usia | Lama bekerja, tahun lulus, jenis perangkat |

Pendekatan yang benar adalah **tetap mengukur** kinerja per kelompok — bahkan ketika atributnya tidak dipakai sebagai fitur.

---

## 13.4 *Explainability*

| Pendekatan | Cara | Catatan |
|------------|------|---------|
| Model yang dapat ditafsirkan | Regresi logistik, pohon dangkal | **Paling andal** — penjelasannya adalah modelnya sendiri |
| *Feature importance* | Bawaan atau permutasi | Global; tidak menjelaskan kasus tunggal |
| **SHAP** | Sumbangan tiap fitur pada satu prediksi | Berdasar teori permainan; lebih mahal |
| **LIME** | Hampiran lokal dengan model sederhana | Cepat; kurang stabil |
| *Partial dependence* | Pengaruh rata-rata satu fitur | Menyesatkan bila fitur berkorelasi |

> **Kaidah praktis:** bila keputusan model menyentuh hak atau kesempatan seseorang — kredit, pekerjaan, layanan publik, hukuman — pertimbangkan sungguh-sungguh untuk memakai **model yang dapat ditafsirkan sejak awal**, alih-alih model kompleks yang dijelaskan belakangan dengan alat penghampiran.
>
> Penjelasan dari SHAP atau LIME adalah **hampiran atas perilaku model**, bukan penjelasan atas keputusan itu sendiri. Bagi orang yang pengajuannya ditolak, perbedaan itu bukan perbedaan akademis.

---

## 13.5 *Model Card*

Dokumentasi baku yang diperkenalkan Mitchell et al. (2019), kini menjadi praktik umum dan mulai dituntut regulasi.

```markdown
# Model Card — [Nama Model]

## 1. Rincian Model
Pengembang · tanggal · versi · jenis model · lisensi data

## 2. Penggunaan yang Dimaksudkan
- **Untuk:** ...
- **BUKAN untuk:** ...
- Pengguna yang dituju · Di luar cakupan

## 3. Data
Sumber · periode · dimensi · cakupan kelompok ·
**yang TIDAK tercakup** · prapemrosesan

## 4. Kinerja
Tabel metrik **per kelompok**, bukan hanya keseluruhan · baseline

## 5. Keterbatasan
Kelompok dengan kinerja terendah · kondisi model tidak andal ·
asumsi yang dapat gugur

## 6. Pertimbangan Etis
Siapa dapat dirugikan · **ukuran fairness yang dipilih DAN ALASANNYA** ·
apa yang dikorbankan · pengawasan manusia · cara mengajukan keberatan

## 7. Pemeliharaan
Kapan dilatih ulang · indikator yang dipantau · penanggung jawab
```

> Bagian 5 dan 6 dinilai paling ketat. *Model card* yang menyatakan "tidak ada keterbatasan" atau mengosongkan pertimbangan etis dikembalikan untuk dilengkapi.

---

## 13.6 Tanggung Jawab

### 13.6.1 Enam Pertanyaan Sebelum Menerapkan Model

1. **Siapa yang terdampak** bila model salah, dan seberapa berat dampaknya?
2. **Apakah ada kelompok** yang dirugikan secara tidak sebanding?
3. **Adakah pengawasan manusia** pada keputusan yang berdampak besar?
4. **Dapatkah orang yang terdampak mengetahui** bahwa keputusannya melibatkan model?
5. **Adakah jalan mengajukan keberatan** dan memperoleh peninjauan manusia?
6. **Siapa yang bertanggung jawab** ketika model merugikan seseorang?

Pertanyaan keenam tidak memiliki jawaban teknis. Ia selalu terjawab dengan **nama seseorang** — tidak pernah dengan nama sebuah model.

### 13.6.2 Tanggung Jawab Tidak Dapat Dialihkan

> "Modelnya yang memutuskan" bukan penjelasan yang dapat diterima, sebagaimana "kalkulatornya yang salah hitung" bukan penjelasan yang dapat diterima.
>
> Seseorang memilih data. Seseorang memilih metrik. Seseorang memutuskan model itu cukup baik untuk diterapkan. Seseorang memutuskan untuk memakainya pada keputusan yang menyentuh hidup orang lain. Rangkaian keputusan itu seluruhnya milik manusia, dan pertanggungjawabannya melekat pada manusia.

Dalam kerangka nilai yang dipegang program studi ini, inilah wujud **amanah** pada bidang kecerdasan artifisial: kesediaan memikul tanggung jawab atas sesuatu yang dibangun, **termasuk atas akibat yang tidak diinginkan dan tidak terlihat oleh orang lain**.

Kesediaan itu diuji pada saat yang paling sunyi: ketika seorang insinyur menemukan bahwa modelnya bekerja jauh lebih buruk untuk suatu kelompok, tidak ada yang mengetahuinya, dan melaporkannya akan memperlambat peluncuran.

---

## AI Corner — Tahap *Create*

### Bab Ini Adalah Tempat AI Paling Sedikit Dapat Membantu

Enam pertanyaan §13.6.1 seluruhnya menuntut pengetahuan tentang konteks penerapan: siapa penggunanya, apa konsekuensi nyata sebuah kesalahan, mekanisme apa yang tersedia untuk keberatan, siapa yang memikul tanggung jawab dalam struktur organisasi itu.

Tidak satu pun ada dalam prompt. Dan jawaban yang dihasilkan tanpa mengetahuinya akan terdengar meyakinkan sambil tidak mengatakan apa-apa.

| Pertanyaan | Jawaban khas AI | Mengapa tidak memadai |
|------------|-----------------|-----------------------|
| Siapa yang dirugikan? | "Kelompok minoritas dan pengguna yang kurang terwakili" | Benar secara umum, kosong secara khusus |
| Apa mekanisme keberatan? | "Sediakan saluran pengaduan" | Tidak menyebut siapa yang menanganinya dan dengan wewenang apa |
| Siapa bertanggung jawab? | "Tim pengembang dan organisasi" | Bukan nama; tidak dapat dimintai pertanggungjawaban |

### Menulis *Model Card*: Yang Boleh dan Yang Tidak

| Boleh dibantu AI | Tidak boleh |
|------------------|-------------|
| Format dan struktur *model card* | Isi bagian Keterbatasan |
| Penyuntingan bahasa | Isi bagian Pertimbangan Etis |
| Menyusun tabel dari angka yang sudah ada | Menentukan ukuran *fairness* yang dipilih |
| Memeriksa apakah ada bagian yang kosong | Menilai apakah model layak diterapkan |

Alasannya sama sepanjang buku ini, dan di sini paling tajam: **yang dituntut bukan kalimat yang baik, melainkan penilaian yang dapat dipertanggungjawabkan oleh orang yang menandatanganinya.**

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan perbedaan model diskriminatif dan generatif, dengan satu contoh masing-masing.

2. Jelaskan mengapa LLM dapat menghasilkan keluaran yang meyakinkan tetapi salah.

3. Sebutkan enam sumber *bias* dan berikan satu contoh berkonteks Indonesia untuk tiga di antaranya.

4. Jelaskan mengapa menghapus kolom "jenis kelamin" tidak membuat model adil.

### Tingkat Menengah

5. Sebuah model penilaian kredit memiliki kinerja berikut:

   | Kelompok | n | Base rate | Recall | FPR |
   |----------|---|-----------|--------|-----|
   | A | 6.000 | 0,12 | 0,84 | 0,09 |
   | B | 800 | 0,21 | 0,61 | 0,18 |

   (a) Hitung selisih *recall* dan FPR antarkelompok.
   (b) Ukuran *fairness* mana yang dilanggar?
   (c) Apa dugaan penyebabnya?
   (d) Apa yang harus ditulis dalam *model card*?

6. Sebuah tim menaikkan *recall* kelompok B dengan menurunkan ambang khusus untuk kelompok itu.
   (a) Ukuran *fairness* mana yang kini terpenuhi?
   (b) Apa yang terjadi pada *precision* kelompok B?
   (c) Apakah pendekatan ini adil? Bahas dari dua sisi.
   (d) Apa yang harus dinyatakan bila pendekatan ini dipakai?

7. Sebuah sistem prediksi kerawanan dipakai untuk mengarahkan patroli.
   (a) Jenis *bias* apa yang paling mungkin muncul seiring waktu?
   (b) Gambarkan lingkaran umpan baliknya.
   (c) Bagaimana cara mendeteksinya?
   (d) Apa rancangan yang dapat mencegahnya?

8. Sebuah model dipakai untuk menyaring lamaran kerja, dengan pengawasan manusia hanya pada kandidat yang lolos saringan.
   (a) Masalah apa yang timbul dari rancangan pengawasan ini?
   (b) Siapa yang tidak pernah dilihat manusia?
   (c) Bagaimana rancangan pengawasan yang lebih baik?
   (d) Jawab keenam pertanyaan §13.6.1 untuk kasus ini.

### Tingkat Mahir

9. Lakukan audit *fairness* lengkap pada model Anda sendiri.
   (a) Latih model pada data nyata dengan kelompok yang timpang representasinya.
   (b) Ukur kinerja terpisah per kelompok.
   (c) Hitung ketiga ukuran *fairness*.
   (d) Tunjukkan bahwa ketiganya tidak dapat dipenuhi sekaligus, dengan angka dari data Anda.
   (e) Pilih satu ukuran, nyatakan alasannya, dan sebutkan apa yang dikorbankan.
   (f) Susun *model card* lengkap.

10. Simulasikan bias umpan balik.
    (a) Latih model pada data awal.
    (b) Pakai prediksinya untuk menentukan kasus mana yang "diperiksa".
    (c) Hanya kasus yang diperiksa masuk ke data latih berikutnya.
    (d) Latih ulang; ulangi lima siklus.
    (e) Catat bagaimana sebaran kelompok dalam data latih berubah tiap siklus.
    (f) Tuliskan pelajarannya dan rancangan yang dapat memutus lingkaran itu.

11. Tulislah esai satu halaman berjudul *"Siapa yang Bertanggung Jawab"*. Ambil satu kasus nyata sistem AI yang merugikan orang. Uraikan: rangkaian keputusan manusia yang mengarah ke sana, pada titik mana kerugian itu dapat dicegah, siapa yang berada pada posisi untuk mencegahnya, dan mengapa ia tidak melakukannya. Tutup dengan apa yang akan Anda lakukan pada posisi itu.

---

## Rangkuman

1. Model **diskriminatif** mempelajari batas antarkelas; model **generatif** mempelajari sebaran data.
2. LLM memperkirakan **token yang mungkin**, bukan fakta yang benar — verifikasi adalah tanggung jawab pemakai.
3. **Enam sumber *bias***; yang paling berbahaya adalah **bias umpan balik** karena memperkuat dirinya sendiri.
4. **Akurasi keseluruhan tinggi dapat menyembunyikan kinerja buruk pada kelompok tertentu.**
5. Audit terpisah per kelompok **wajib**, bukan pilihan.
6. **Ukuran-ukuran *fairness* saling bertentangan secara matematis** ketika *base rate* berbeda — *fairness* adalah pilihan yang harus dinyatakan beserta pengorbanannya.
7. **Menghapus atribut sensitif tidak membuat model adil** — proksi tetap ada.
8. Bila keputusan menyentuh hak seseorang, pertimbangkan **model yang dapat ditafsirkan sejak awal**.
9. ***Model card*** mendokumentasikan penggunaan, kinerja per kelompok, keterbatasan, dan pertimbangan etis.
10. **Tanggung jawab tidak dapat dialihkan kepada model.** Ia selalu melekat pada manusia yang memutuskan.

---

## Referensi

1. Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and Machine Learning*. MIT Press. <https://fairmlbook.org>
2. Mitchell, M., et al. (2019). Model Cards for Model Reporting. *FAT* '19*, 220–229.
3. Kleinberg, J., Mullainathan, S., & Raghavan, M. (2016). Inherent Trade-Offs in the Fair Determination of Risk Scores. *arXiv:1609.05807*.
4. Angwin, J., et al. (2016). Machine Bias. *ProPublica*.
5. Suresh, H., & Guttag, J. (2021). A Framework for Understanding Sources of Harm throughout the ML Life Cycle. *EAAMO '21*.
6. Lundberg, S. M., & Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. *NeurIPS*.
7. UNESCO (2024). *AI Competency Framework for Students*.
8. Tim Kurikulum Informatika UAI (2026). *AI Curriculum Infusion Matrix*.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
