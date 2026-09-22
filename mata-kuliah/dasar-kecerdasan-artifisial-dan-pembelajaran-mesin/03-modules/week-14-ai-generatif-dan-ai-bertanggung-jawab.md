# Minggu 14: AI Generatif dan AI yang Bertanggung Jawab

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 14 dari 16 |
| Topik | Model generatif dan LLM; *bias*, *fairness*, *explainability*, *model card* |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-13 |
| Bloom | C2 (Memahami) → C5 (Mengevaluasi) |
| Durasi | 150 menit |
| Metode | Kuliah · Studi kasus · Audit model |
| Penilaian | Observasi (Lab 14) · **Laporan proyek (P-03)** |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menjelaskan** (C2) prinsip kerja model generatif dan *large language model* pada tingkat gagasan.
2. **Menganalisis** (C4) sumber *bias* dalam data dan model.
3. **Menghitung** (C3) ukuran *fairness* antarkelompok pada model sendiri.
4. **Mengevaluasi** (C5) dampak sosial penerapan sebuah model.
5. **Menyusun** (C6) *model card* yang lengkap dan jujur.

---

## Materi Pembelajaran

### 14.1 Model Generatif

#### 14.1.1 Diskriminatif vs Generatif

| Aspek | Diskriminatif | Generatif |
|-------|---------------|-----------|
| Yang dipelajari | $P(y \mid x)$ — batas antarkelas | $P(x)$ atau $P(x, y)$ — sebaran data itu sendiri |
| Kemampuan | Membedakan | **Membangkitkan contoh baru** |
| Contoh | Regresi logistik, SVM, *Random Forest* | LLM, model difusi, VAE, GAN |

Seluruh model yang dipelajari Minggu 6–13 bersifat diskriminatif. Pertemuan ini memperkenalkan sisi lainnya, pada tingkat gagasan.

#### 14.1.2 Gagasan *Large Language Model*

Pada intinya, LLM dilatih untuk satu tugas yang sangat sederhana: **memperkirakan token berikutnya** dari runtun token sebelumnya.

```
  "Ibu kota Indonesia adalah" ──► model ──► P(token berikutnya)
                                             ├─ "Jakarta"  0,87
                                             ├─ "Nusantara" 0,06
                                             ├─ "kota"      0,02
                                             └─ ...
```

Dari tugas sederhana ini, dilatih pada data yang sangat besar, muncul kemampuan yang tampak jauh lebih luas. Tiga hal yang perlu dipahami dari sifat ini:

| Sifat | Akibat |
|-------|--------|
| Model memperkirakan **token yang mungkin**, bukan **fakta yang benar** | Keluaran dapat meyakinkan tetapi salah (*halusinasi*) |
| Pengetahuannya berasal dari data latih | Ada batas waktu pengetahuan; kesalahan dalam data ikut terpelajari |
| Tidak ada mekanisme pemeriksaan kebenaran | **Verifikasi adalah tanggung jawab pemakai** |

> Inilah dasar kebijakan AI mata kuliah ini. Pembatasan pada [RPS §K.1](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md) bukan kekhawatiran akan kecurangan, melainkan pengakuan atas sifat teknis alat itu: ia tidak mengetahui konteks data Anda dan tidak memiliki mekanisme untuk memeriksa kebenarannya sendiri.

---

### 14.2 *Bias* dalam Pembelajaran Mesin

#### 14.2.1 Enam Sumber *Bias*

| Sumber | Penjelasan | Contoh Indonesia |
|--------|------------|------------------|
| **Bias historis** | Data mencerminkan ketidakadilan yang sudah ada | Data penerimaan kerja masa lalu yang timpang gender |
| **Bias representasi** | Sebagian kelompok kurang terwakili | Data kesehatan yang terpusat di Jawa |
| **Bias pengukuran** | Variabel proksi tidak mengukur yang dimaksud | "Jumlah kunjungan puskesmas" sebagai proksi kesehatan — padahal mengukur akses |
| **Bias agregasi** | Satu model untuk kelompok yang berbeda sifat | Model tunggal untuk perkotaan dan perdesaan |
| **Bias penerapan** | Model dipakai di luar konteks perancangannya | Model perkotaan diterapkan di daerah terpencil |
| **Bias umpan balik** | Keluaran model memengaruhi data berikutnya | Patroli diarahkan ke wilayah yang diprediksi rawan → lebih banyak kasus tercatat di sana |

Baris terakhir adalah yang paling berbahaya karena **memperkuat dirinya sendiri**. Model memprediksi kerawanan di wilayah A → patroli ditingkatkan di A → lebih banyak pelanggaran tercatat di A → data berikutnya "membuktikan" A memang rawan.

#### 14.2.2 Model Akurat yang Tetap Merugikan

Sebuah model dapat memiliki akurasi keseluruhan tinggi dan tetap bekerja **jauh lebih buruk** untuk kelompok tertentu:

| Kelompok | n | Akurasi | Recall |
|----------|---|---------|--------|
| Jawa | 8.400 | 0,89 | 0,86 |
| Sumatera | 3.100 | 0,85 | 0,81 |
| Kalimantan | 1.200 | 0,82 | 0,74 |
| Sulawesi | 900 | 0,79 | 0,68 |
| **Papua** | **300** | **0,71** | **0,52** |
| **Keseluruhan** | **13.900** | **0,86** | **0,82** |

Angka keseluruhan (0,86) tampak baik. Bagi penduduk Papua, model ini melewatkan hampir separuh kasus yang seharusnya terdeteksi.

> **Inilah alasan audit terpisah per kelompok wajib dilakukan.** Angka agregat menyembunyikan ketimpangan, dan ketimpangan itu justru paling sering merugikan kelompok yang paling sedikit terwakili dalam data.
>
> Dalam kerangka nilai yang dipegang program studi ini, persoalan tersebut bukan sekadar persoalan teknis. **Adil (`al-'adl`)** menuntut bahwa sistem yang memengaruhi hidup orang bekerja setara bagi semua, dan prinsip **tidak menimbulkan kerusakan (`la darar`)** menuntut bahwa dampak buruk pada kelompok mana pun diketahui dan dipertanggungjawabkan — bukan disembunyikan di balik satu angka rata-rata.

---

### 14.3 Mengukur *Fairness*

#### 14.3.1 Tiga Ukuran Pokok

| Ukuran | Definisi | Menuntut |
|--------|----------|----------|
| **Demographic parity** | $P(\hat{y}=1 \mid A=a)$ sama untuk semua kelompok | Proporsi prediksi positif setara |
| **Equal opportunity** | *Recall* sama untuk semua kelompok | Yang layak memperoleh peluang setara |
| **Equalized odds** | *Recall* **dan** FPR sama | Kedua jenis kesalahan setara |

#### 14.3.2 Ketiganya Tidak Dapat Dipenuhi Sekaligus

Kleinberg et al. (2016) membuktikan bahwa ketika angka kejadian dasar (*base rate*) berbeda antarkelompok, ukuran-ukuran *fairness* tersebut **saling bertentangan secara matematis**. Tidak ada model yang dapat memenuhi semuanya.

> **Konsekuensinya bagi praktik:** *fairness* bukan kotak centang yang dapat dipenuhi, melainkan **pilihan yang harus dinyatakan dan dipertanggungjawabkan**. Insinyur wajib menyatakan ukuran mana yang dipilih dan mengapa — dan mengakui apa yang dikorbankan.

#### 14.3.3 Mengukurnya

```python
import pandas as pd
from sklearn.metrics import recall_score, precision_score, accuracy_score

def audit_kelompok(y_true, y_pred, kelompok):
    # Menghitung metrik terpisah per kelompok
    baris = []
    for k in sorted(pd.unique(kelompok)):
        m = kelompok == k
        baris.append({
            "Kelompok": k,
            "n": int(m.sum()),
            "Akurasi": accuracy_score(y_true[m], y_pred[m]),
            "Precision": precision_score(y_true[m], y_pred[m], zero_division=0),
            "Recall": recall_score(y_true[m], y_pred[m], zero_division=0),
            "Proporsi positif": y_pred[m].mean(),
        })
    tabel = pd.DataFrame(baris)

    # Selisih terbesar antarkelompok — inilah angka yang dilaporkan
    print("Selisih recall maks-min   :",
          round(tabel["Recall"].max() - tabel["Recall"].min(), 3))
    print("Selisih precision maks-min:",
          round(tabel["Precision"].max() - tabel["Precision"].min(), 3))
    return tabel.round(3)

print(audit_kelompok(y_test, y_pred, X_test["wilayah"]))
```

#### 14.3.4 Menghapus Atribut Sensitif Tidak Cukup

Membuang kolom "jenis kelamin" atau "wilayah" dari fitur **tidak** membuat model adil. Atribut itu sering dapat diperkirakan kembali dari fitur lain:

| Atribut dibuang | Proksi yang tersisa |
|-----------------|---------------------|
| Wilayah | Kode pos, jarak ke fasilitas, jenis pekerjaan |
| Jenis kelamin | Riwayat cuti, jenis pekerjaan, pola konsumsi |
| Usia | Lama bekerja, tahun lulus, jenis perangkat |

Pendekatan yang benar adalah **tetap mengukur** kinerja per kelompok — bahkan ketika atributnya tidak dipakai sebagai fitur.

---

### 14.4 *Explainability*

| Pendekatan | Cara | Catatan |
|------------|------|---------|
| Model yang dapat ditafsirkan | Regresi logistik, pohon dangkal | **Paling andal** — penjelasannya adalah modelnya sendiri |
| *Feature importance* | Kepentingan bawaan atau permutasi | Global; tidak menjelaskan kasus tunggal |
| **SHAP** | Sumbangan tiap fitur pada satu prediksi | Berdasar teori permainan; lebih mahal |
| **LIME** | Hampiran lokal dengan model sederhana | Cepat; kurang stabil |
| *Partial dependence* | Pengaruh rata-rata satu fitur | Menyesatkan bila fitur berkorelasi |

```python
from sklearn.inspection import PartialDependenceDisplay, permutation_importance

hasil = permutation_importance(model, X_test, y_test, n_repeats=10, random_state=42)
PartialDependenceDisplay.from_estimator(model, X_test, features=["omzet", "lama_usaha"])
```

> **Kaidah praktis:** bila keputusan model menyentuh hak atau kesempatan seseorang — kredit, pekerjaan, layanan publik, hukuman — pertimbangkan sungguh-sungguh untuk memakai model yang dapat ditafsirkan sejak awal, alih-alih model kompleks yang dijelaskan belakangan dengan alat penghampiran.

---

### 14.5 *Model Card*

Dokumentasi baku yang diperkenalkan Mitchell et al. (2019), kini menjadi praktik umum dan mulai dituntut regulasi.

```markdown
# Model Card — Penilaian Kelayakan Kredit UMKM

## 1. Rincian Model
- Dikembangkan oleh: Kelompok 4, IF52510031, Prodi Informatika UAI
- Tanggal: November 2026
- Versi: 1.0
- Jenis: Gradient Boosting (HistGradientBoostingClassifier)
- Lisensi data: Terbuka, sumber [nama portal]

## 2. Penggunaan yang Dimaksudkan
- **Untuk:** membantu penilai manusia memprioritaskan berkas pengajuan
- **BUKAN untuk:** mengambil keputusan penolakan secara otomatis
- Pengguna: petugas analis kredit koperasi
- Di luar cakupan: kredit konsumtif, kredit korporasi, wilayah di luar data latih

## 3. Data
- Sumber, periode, jumlah baris dan kolom
- Cakupan wilayah: [sebutkan provinsi yang tercakup]
- **Yang TIDAK tercakup:** [sebutkan dengan jelas]
- Praproses: [ringkas]

## 4. Kinerja
| Kelompok | n | Precision | Recall | F1 |
|----------|---|-----------|--------|-----|
| Keseluruhan | | | | |
| Per wilayah | | | | |
| Per skala usaha | | | | |

Baseline: [skor DummyClassifier]

## 5. Keterbatasan
- Kelompok yang kinerjanya lebih rendah dan besarnya selisih
- Kondisi ketika model tidak dapat diandalkan
- Asumsi yang dapat gugur seiring waktu

## 6. Pertimbangan Etis
- Siapa yang dapat dirugikan bila model salah
- Ukuran fairness yang dipilih DAN ALASANNYA
- Mekanisme pengawasan manusia
- Cara mengajukan keberatan atas keputusan

## 7. Pemeliharaan
- Kapan model harus dilatih ulang
- Indikator yang dipantau untuk mendeteksi penurunan kinerja
- Penanggung jawab
```

> ***Model card* wajib disertakan pada laporan proyek (P-03).** Bagian 5 dan 6 dinilai paling ketat: *model card* yang menyatakan "tidak ada keterbatasan" atau mengosongkan pertimbangan etis dikembalikan.

---

### 14.6 Tanggung Jawab

#### 14.6.1 Pertanyaan yang Wajib Dijawab Sebelum Menerapkan Model

1. **Siapa yang terdampak** bila model salah, dan seberapa berat dampaknya?
2. **Apakah ada kelompok** yang dirugikan secara tidak sebanding?
3. **Adakah pengawasan manusia** pada keputusan yang berdampak besar?
4. **Dapatkah orang yang terdampak mengetahui** bahwa keputusannya melibatkan model?
5. **Adakah jalan untuk mengajukan keberatan** dan memperoleh peninjauan manusia?
6. **Siapa yang bertanggung jawab** ketika model merugikan seseorang?

Pertanyaan keenam tidak memiliki jawaban teknis. Ia selalu terjawab dengan nama seseorang — tidak pernah dengan nama sebuah model.

#### 14.6.2 Tanggung Jawab Tidak Dapat Dialihkan ke Alat

> "Modelnya yang memutuskan" bukan penjelasan yang dapat diterima, sebagaimana "kalkulatornya yang salah hitung" bukan penjelasan yang dapat diterima.
>
> Seseorang memilih data, seseorang memilih metrik, seseorang memutuskan model itu cukup baik untuk diterapkan, dan seseorang memutuskan untuk memakainya pada keputusan yang menyentuh hidup orang lain. Rangkaian keputusan itu seluruhnya milik manusia, dan pertanggungjawabannya melekat pada manusia.

Dalam kerangka nilai yang dipegang program studi ini, inilah wujud **amanah** pada bidang kecerdasan artifisial: kesediaan memikul tanggung jawab atas sesuatu yang dibangun, termasuk atas akibat yang tidak diinginkan dan tidak terlihat oleh orang lain.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 13 buku ajar](../06-buku-ajar/bab-13-ai-generatif-dan-ai-bertanggung-jawab.md).
- **Menyelesaikan laporan akhir proyek** — dikumpulkan hari ini.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | **Pengumpulan P-03** (laporan + notebook + *model card*) |
| Konsep | 30' | Model generatif; gagasan LLM; mengapa halusinasi terjadi |
| Konsep | 30' | Enam sumber *bias*; model akurat yang tetap merugikan |
| **Audit** | 40' | **Kegiatan inti:** mahasiswa mengaudit model proyeknya sendiri per kelompok |
| Diskusi | 25' | Studi kasus: sistem penilaian yang merugikan kelompok tertentu |
| Penutup | 15' | *Model card*; enam pertanyaan tanggung jawab; persiapan presentasi |

**Kegiatan inti — audit model sendiri:** setiap kelompok menjalankan fungsi `audit_kelompok` §14.3.3 pada modelnya, lalu melaporkan selisih *recall* terbesar antarkelompok. Kelompok dengan selisih besar diminta menjelaskan dugaan penyebabnya — hampir selalu berkaitan dengan jumlah data per kelompok.

**Studi kasus untuk diskusi:** sistem penilaian risiko yang dipakai pengadilan di Amerika Serikat, yang ditemukan memiliki tingkat positif palsu berbeda antar-kelompok ras (ProPublica, 2016), beserta bantahan pengembangnya bahwa sistem itu terkalibrasi setara. **Keduanya benar secara teknis** — dan itulah demonstrasi paling konkret dari ketidakmungkinan §14.3.2.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 14](../04-labs/lab-14-audit-bias-dan-model-card.md).
- Menyiapkan presentasi proyek (Minggu 15).

---

## Penugasan

**T-14 — Audit *Bias* dan *Model Card***

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook audit + berkas *model card* (Markdown) |
| Isi | (a) Audit kinerja **model sendiri** terpisah per sekurang-kurangnya dua kelompok; (b) Selisih *recall* dan *precision* antarkelompok; (c) Pembahasan dugaan penyebab ketimpangan; (d) Ukuran *fairness* yang dipilih **beserta alasannya**; (e) *Model card* lengkap sesuai format §14.5; (f) Jawaban atas enam pertanyaan tanggung jawab §14.6.1 |
| Ketentuan khusus | Audit dilakukan pada model proyek sendiri, bukan pada contoh |
| Tenggat | Awal pertemuan Minggu 15 |
| Bobot | 1,9% (Observasi) |

---

## Rangkuman

1. Model **diskriminatif** mempelajari batas antarkelas; model **generatif** mempelajari sebaran data.
2. LLM memperkirakan **token yang mungkin**, bukan fakta yang benar — karena itu verifikasi adalah tanggung jawab pemakai.
3. **Enam sumber *bias***; yang paling berbahaya adalah **bias umpan balik** karena memperkuat dirinya sendiri.
4. **Akurasi keseluruhan tinggi dapat menyembunyikan kinerja buruk pada kelompok tertentu.**
5. Audit terpisah per kelompok **wajib**, bukan pilihan.
6. **Ukuran-ukuran *fairness* saling bertentangan secara matematis** ketika *base rate* berbeda — *fairness* adalah pilihan yang harus dinyatakan.
7. **Menghapus atribut sensitif tidak membuat model adil** — proksi tetap ada.
8. Bila keputusan menyentuh hak seseorang, pertimbangkan **model yang dapat ditafsirkan sejak awal**.
9. ***Model card*** mendokumentasikan penggunaan yang dimaksudkan, kinerja per kelompok, keterbatasan, dan pertimbangan etis.
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
