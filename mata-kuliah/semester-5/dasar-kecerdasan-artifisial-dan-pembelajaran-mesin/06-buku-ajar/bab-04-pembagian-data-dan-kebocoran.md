# BAB 4: PEMBAGIAN DATA DAN KEBOCORAN DATA

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK102-1` | Menerapkan strategi pembagian data yang sesuai sifat datanya | C3 |
| `DAIML-Sub-CPMK102-1` | Menganalisis sebuah *pipeline* dan menemukan kebocoran di dalamnya | C4 |
| `DAIML-Sub-CPMK102-1` | Memperbaiki kebocoran dan melaporkan dampaknya terhadap skor | C5 |

---

## 4.1 Satu Bab Penuh untuk Satu Jenis Kesalahan

Kapoor dan Narayanan (2023) menelaah 294 makalah ilmiah dari 17 bidang yang memakai pembelajaran mesin, dan menemukan **kebocoran data pada sebagian besar di antaranya**. Akibatnya: hasil yang dilaporkan tidak dapat diulang, dan sebagian kesimpulan ilmiah yang telah dipublikasikan ternyata keliru.

Ini bukan kesalahan pemula. Ini kesalahan yang terjadi pada peneliti terlatih, berulang kali, karena satu sebab:

> **Kebocoran data adalah satu-satunya jenis kesalahan dalam pembelajaran mesin yang *memberi hadiah* ketika dilakukan.**

Ia tidak menghasilkan pesan galat. Ia tidak membuat kode berhenti. Ia menghasilkan **skor yang bagus** — dan skor yang bagus jarang dipertanyakan.

---

## 4.2 Tiga Peran Data

```
┌────────────────────────────────────────────────────────────┐
│                     SELURUH DATA                           │
├──────────────────────────┬──────────────┬──────────────────┤
│         LATIH            │   VALIDASI   │       UJI        │
│         (60%)            │    (20%)     │      (20%)       │
├──────────────────────────┼──────────────┼──────────────────┤
│ Model belajar dari sini  │ Memilih model│ Menaksir kinerja │
│                          │ & menyetel   │ pada data baru   │
├──────────────────────────┼──────────────┼──────────────────┤
│ Dilihat berkali-kali     │ Berkali-kali │ SEKALI, di akhir │
└──────────────────────────┴──────────────┴──────────────────┘
```

### 4.2.1 Mengapa Data Uji Hanya Sekali

Setiap kali keputusan diambil berdasarkan skor data uji — "model A lebih baik, mari pakai A" — informasi dari data uji masuk ke dalam pilihan. Setelah beberapa kali, skor data uji berhenti menjadi taksiran kinerja pada data baru, dan menjadi skor pada data yang **sudah ikut membentuk model**.

Fenomena ini disebut **kebocoran melalui pemilihan berulang**. Ia halus, tidak menghasilkan galat, dan hampir selalu terjadi bila data uji dipakai lebih dari sekali.

Pemecahannya: pakai data **validasi** untuk seluruh pemilihan dan penyetelan; sentuh data **uji** satu kali, ketika seluruh keputusan sudah selesai.

---

## 4.3 Strategi Pembagian sesuai Sifat Data

| Sifat data | Strategi | Alat |
|------------|----------|------|
| Biasa, kelas seimbang | Acak | `train_test_split` |
| Kelas tak seimbang | **Stratifikasi** | `train_test_split(stratify=y)` |
| Ada urutan waktu | **Temporal** | `TimeSeriesSplit` |
| Ada entitas berulang | **Berkelompok** | `GroupKFold` |
| Data sangat sedikit | Lipatan banyak | `KFold(n_splits=10)` |

### 4.3.1 Pembagian Temporal

Ketika data memiliki urutan waktu, pembagian acak **selalu** menghasilkan kebocoran: model belajar dari masa depan untuk memprediksi masa lalu.

```
  SALAH (acak):
  ───────────────────────────────────────────────►  waktu
  [U][L][L][U][L][U][L][L][U][L]   ← uji tersebar di antara latih
     Model "melihat masa depan"

  BENAR (temporal):
  ───────────────────────────────────────────────►  waktu
  [L][L][L][L][L][L][L][V][V][U][U] ← uji selalu setelah latih
```

```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
for i, (i_tr, i_te) in enumerate(tscv.split(X), 1):
    print(f"Lipatan {i}: latih=[0:{i_tr[-1]+1}]  uji=[{i_te[0]}:{i_te[-1]+1}]")
```

### 4.3.2 Pembagian Berkelompok

Bila satu entitas (pasien, nasabah, mahasiswa) muncul dalam beberapa baris, pembagian acak membuat entitas yang sama hadir di latih **dan** uji. Model dapat "mengenali" entitas itu alih-alih mempelajari polanya.

```python
from sklearn.model_selection import GroupKFold

gkf = GroupKFold(n_splits=5)
for i_tr, i_te in gkf.split(X, y, groups=id_nasabah):
    ...   # seluruh baris satu nasabah berada di lipatan yang sama
```

Semakin banyak baris per entitas, semakin besar kebocorannya.

---

## 4.4 Validasi Silang

```
  ┌────┬────┬────┬────┬────┐
  │ V  │ L  │ L  │ L  │ L  │  → skor 1
  ├────┼────┼────┼────┼────┤
  │ L  │ V  │ L  │ L  │ L  │  → skor 2
  ├────┼────┼────┼────┼────┤
  │ L  │ L  │ V  │ L  │ L  │  → skor 3
  ├────┼────┼────┼────┼────┤
  │ L  │ L  │ L  │ V  │ L  │  → skor 4
  ├────┼────┼────┼────┼────┤
  │ L  │ L  │ L  │ L  │ V  │  → skor 5
  └────┴────┴────┴────┴────┘
       Kinerja = rerata ± simpangan
```

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold
import numpy as np

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# PENTING: yang divalidasi-silang adalah PIPELINE, bukan model saja.
skor = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring="f1")
print(f"F1 = {skor.mean():.3f} ± {skor.std():.3f}")
print("Per lipatan:", np.round(skor, 3))
```

### 4.4.1 Membaca Simpangan Antarlipatan

| Keadaan | Tafsir | Tindakan |
|---------|--------|----------|
| Simpangan < 0,02 | Kinerja stabil | Dapat dipercaya |
| 0,02–0,05 | Wajar pada data terbatas | Laporkan rerata **dan** simpangan |
| > 0,10 | Data sedikit, atau ada lipatan yang sangat berbeda | Selidiki lipatan yang menyimpang |
| Satu lipatan jauh lebih rendah | Ada kelompok atau periode yang berbeda sifat | Periksa apakah strategi pembagian sudah tepat |

> **Melaporkan rerata tanpa simpangan menyembunyikan informasi penting.** Rerata 0,80 dari {0,79; 0,80; 0,81} sangat berbeda artinya dari rerata 0,80 dari {0,60; 0,80; 1,00}.

---

## 4.5 Enam Jenis Kebocoran

### 4.5.1 Kebocoran Prapemrosesan

Transformasi di-*fit* pada seluruh data sebelum pembagian. Dicegah dengan `Pipeline` (Bab 3).

### 4.5.2 Kebocoran Temporal

Fitur memuat informasi yang belum tersedia saat prediksi dibutuhkan.

| Kasus | Fitur yang bocor |
|-------|------------------|
| Prediksi gagal bayar saat pengajuan | Riwayat pembayaran setelah pencairan |
| Prediksi keterlambatan saat paket masuk gudang | Status perjalanan berikutnya |
| Prediksi putus kuliah pada semester 3 | IPK semester 5 |

**Pencegahnya** adalah menjawab jujur pertanyaan 3 dan 4 pada formulasi Bab 2: *kapan prediksi dibutuhkan, dan apa yang tersedia saat itu?*

### 4.5.3 Kebocoran Duplikat

Baris yang sama (atau nyaris sama) muncul di latih dan uji.

```python
print("Duplikat penuh:", df.duplicated().sum())
print("Duplikat tanpa kolom id:", df.drop(columns=["id"]).duplicated().sum())
```

### 4.5.4 Kebocoran Kelompok

Satu entitas tersebar di latih dan uji. Diatasi dengan `GroupKFold`.

### 4.5.5 Kebocoran Target

Fitur yang sebenarnya merupakan turunan dari target.

| Fitur mencurigakan | Mengapa bocor |
|--------------------|---------------|
| `jumlah_tagihan_tertunggak` untuk memprediksi gagal bayar | Ia **adalah** gagal bayar |
| `lama_dirawat` untuk memprediksi keparahan penyakit | Akibat, bukan sebab |
| `nomor_invoice` untuk memprediksi pembelian | Hanya ada bila pembelian terjadi |

**Tanda pengenalnya:** korelasi terhadap target mendekati sempurna, atau kinerja model jauh di atas yang masuk akal.

### 4.5.6 Kebocoran melalui Pemilihan Berulang

Data uji dipakai berkali-kali untuk memilih. Diatasi dengan disiplin §4.2.1.

---

## 4.6 Daftar Periksa Kebocoran

Wajib dijalankan sebelum mengumpulkan pekerjaan apa pun:

- [ ] Seluruh transformasi berada di dalam `Pipeline`
- [ ] `fit` hanya pernah dipanggil pada data latih
- [ ] Data uji tidak dipakai untuk memilih model, fitur, atau hiperparameter
- [ ] Bila ada urutan waktu: pembagian temporal, bukan acak
- [ ] Bila ada entitas berulang: `GroupKFold`
- [ ] Duplikat diperiksa sebelum pembagian
- [ ] Setiap fitur lolos pertanyaan: *"tersedia saat prediksi dibutuhkan?"*
- [ ] Tidak ada fitur yang merupakan turunan target
- [ ] **Skor yang mencurigakan tinggi sudah diselidiki, bukan dirayakan**

> **Kaidah praktis:** bila kinerja model jauh melampaui yang masuk akal untuk masalah itu, kemungkinan terbesarnya bukan bahwa modelnya hebat — melainkan bahwa ada kebocoran yang belum ditemukan.

---

## AI Corner — Tahap *Understand → Apply*

### Kebocoran Adalah Kesalahan yang Tidak Dapat Dideteksi Alat

Tidak ada pustaka yang dapat memeriksa apakah sebuah fitur "tersedia saat prediksi dibutuhkan". Pertanyaan itu menuntut pengetahuan tentang **proses bisnis** yang menghasilkan data — kapan setiap kolom terisi, oleh siapa, dan dalam urutan apa.

Model bahasa dapat mengenali pola kebocoran yang **tampak dari kode** — misalnya `fit_transform` sebelum `train_test_split`. Ia **tidak** dapat mengenali kebocoran yang tersembunyi dalam **makna kolom**, karena ia tidak tahu apa arti kolom itu pada organisasi yang menerbitkannya.

| Dapat dideteksi dari kode | Hanya dapat dikenali dari pemahaman domain |
|---------------------------|--------------------------------------------|
| `fit` di luar `Pipeline` | Kolom `lama_dirawat` adalah akibat, bukan sebab |
| Pembagian acak pada data bertanggal | Kolom `nomor_invoice` hanya ada bila transaksi terjadi |
| Pemilihan fitur sebelum pembagian | Kolom `status_verifikasi` diisi setelah keputusan dibuat |

### Pemakaian yang Wajar

```
Ini daftar 18 fitur saya untuk memprediksi gagal bayar kredit,
yang diprediksi SAAT PENGAJUAN diterima:
[daftar fitur dengan penjelasan singkat tiap kolom]

Saya sudah menandai 3 fitur sebagai berisiko bocor: [sebutkan].

Tolong periksa daftar ini terhadap pertanyaan "apakah nilai ini
sudah ada pada saat pengajuan diterima?" — dan sebutkan bila ada
yang saya lewatkan. Jangan ubah daftar saya; cukup tunjukkan
yang perlu saya periksa ulang.
```

Prompt ini berhasil karena memberikan konteks yang tidak dimiliki AI (arti tiap kolom dan kapan prediksi dibutuhkan), sekaligus membatasi perannya pada pemeriksaan.

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan peran berbeda data latih, validasi, dan uji. Mengapa data uji hanya boleh dipakai sekali?

2. Tentukan strategi pembagian yang tepat untuk masing-masing:
   (a) Data 50.000 transaksi dengan 1,2% penipuan.
   (b) Data penjualan harian selama tiga tahun.
   (c) Data 8.000 kunjungan dari 900 pasien.
   (d) Data 400 provinsi-tahun tanpa urutan yang bermakna.

3. Sebutkan enam jenis kebocoran data dan berikan satu contoh singkat untuk masing-masing.

4. Sebuah laporan menyebutkan "F1 = 0,84". Informasi apa yang hilang, dan mengapa ia penting?

### Tingkat Menengah

5. Perhatikan kode berikut:
   ```python
   X_scaled = StandardScaler().fit_transform(X)
   pemilih = SelectKBest(f_classif, k=10).fit(X_scaled, y)
   X_sel = pemilih.transform(X_scaled)
   X_tr, X_te, y_tr, y_te = train_test_split(X_sel, y, test_size=0.2)
   ```
   (a) Temukan dua kebocoran.
   (b) Jelaskan mekanisme masing-masing.
   (c) Tuliskan versi yang benar dengan `Pipeline`.
   (d) Kebocoran mana yang dampaknya lebih besar? Jelaskan.

6. Sebuah tim memprediksi keterlambatan pengiriman dan memperoleh ROC-AUC 0,997.
   (a) Apa reaksi pertama Anda?
   (b) Sebutkan tiga fitur yang paling mungkin menjadi penyebabnya.
   (c) Bagaimana cara memastikan dugaan itu?
   (d) Apa yang akan terjadi pada skornya setelah fitur itu dibuang?

7. Sebuah data memuat 12.000 baris dari 1.500 nasabah (rata-rata 8 baris per nasabah).
   (a) Kebocoran jenis apa yang terjadi bila dibagi secara acak?
   (b) Jelaskan mengapa model dapat "mengenali" nasabah.
   (c) Tuliskan kode pembagian yang benar.
   (d) Apakah selisih skornya akan besar atau kecil? Faktor apa yang menentukannya?

8. Validasi silang 5 lipatan menghasilkan skor: 0,62; 0,89; 0,58; 0,91; 0,70.
   (a) Hitung rerata dan simpangan bakunya.
   (b) Apa yang ditunjukkan sebaran ini?
   (c) Sebutkan tiga kemungkinan penyebabnya.
   (d) Apa yang akan Anda periksa lebih dahulu?

### Tingkat Mahir

9. Bangun demonstrasi kebocoran yang dapat diajarkan.
   (a) Ambil dataset nyata dengan urutan waktu.
   (b) Bangun notebook yang mengandung **empat** jenis kebocoran berbeda.
   (c) Catat skornya.
   (d) Perbaiki satu per satu, catat skor setelah tiap perbaikan.
   (e) Buat grafik penurunan skor terhadap tahap perbaikan.
   (f) Tuliskan penjelasan mengapa tiap perbaikan menurunkan skor.

10. Audit sebuah proyek pembelajaran mesin publik.
    (a) Pilih satu *notebook* atau makalah yang tersedia terbuka.
    (b) Terapkan daftar periksa §4.6.
    (c) Untuk setiap butir yang tidak terpenuhi, jelaskan risikonya.
    (d) Perkirakan arah dan besar biasnya.
    (e) Tuliskan tiga pertanyaan yang akan Anda ajukan kepada penulisnya.

11. Tulislah pedoman satu halaman berjudul *"Memeriksa Kebocoran pada Data yang Anda Terima dari Orang Lain"*. Sertakan: pertanyaan yang harus diajukan kepada penyedia data, tanda-tanda yang dapat dikenali dari data itu sendiri, dan cara menyatakan temuan kepada pihak yang memberi data tanpa menuduh.

---

## Rangkuman

1. **Kebocoran data memberi hadiah ketika dilakukan** — itulah yang membuatnya berbahaya.
2. Data uji **dipakai satu kali, di paling akhir**; pemakaian berulang merusak kejujurannya.
3. Strategi pembagian mengikuti **sifat data**: stratifikasi, temporal, atau berkelompok.
4. **Pembagian acak pada data berurutan waktu selalu menghasilkan kebocoran.**
5. Yang divalidasi-silang adalah **`Pipeline`**, bukan model saja.
6. Laporkan **rerata dan simpangan** antarlipatan; rerata saja menyembunyikan informasi.
7. **Enam jenis kebocoran:** prapemrosesan, temporal, duplikat, kelompok, target, pemilihan berulang.
8. **Skor yang terlalu bagus adalah tanda bahaya**, bukan tanda keberhasilan.
9. Kebocoran yang tersembunyi dalam **makna kolom** tidak dapat dideteksi alat mana pun — ia menuntut pemahaman domain.
10. Daftar periksa §4.6 dijalankan sebelum setiap pengumpulan.

---

## Referensi

1. Kapoor, S., & Narayanan, A. (2023). Leakage and the Reproducibility Crisis in ML-based Science. *Patterns*, 4(9), 100804.
2. Kaufman, S., Rosset, S., & Perlich, C. (2012). Leakage in Data Mining. *ACM TKDD*, 6(4), 1–21.
3. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 2. O'Reilly.
4. Müller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*, Bab 5. O'Reilly.
5. Dokumentasi scikit-learn — *Cross-validation*. <https://scikit-learn.org/stable/modules/cross_validation.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
