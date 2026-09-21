# BAB 14: PROYEK AKHIR — SOLUSI PEMBELAJARAN MESIN *END-TO-END*

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK082-1` | Merancang dan membangun solusi ML utuh untuk masalah nyata | C6 |
| `DAIML-Sub-CPMK102-1` | Mengevaluasi kinerja model dan mengomunikasikan batasnya | C4–C5 |

---

## Pengantar: Dari Potongan Menjadi Rangkaian

Tiga belas bab sebelumnya mengajarkan **potongan**. Bab ini mengajarkan **rangkaiannya**.

Perbedaannya besar. Pada latihan, seseorang sudah memilihkan datanya, sudah memastikan targetnya jelas, dan sudah memastikan tidak ada kebocoran. Yang tersisa adalah menjalankan metode. Pada persoalan nyata, tidak satu pun dari itu tersedia.

Bab ini adalah peta jalan untuk menghadapi keadaan itu.

> Rincian administratif proyek — tenggat, format, dan rubrik — ada pada [Panduan Proyek](../05-assessments/project-guidelines.md). Bab ini membahas **cara berpikirnya**.

---

## 14.1 Anatomi Sebuah Proyek Pembelajaran Mesin

### 14.1.1 Tujuh Tahap

```
┌─────────────────────────────────────────────────────────────┐
│  1. FORMULASI       Masalah apa, dan apakah ML jawabannya?   │
│         ↓                                                    │
│  2. DATA            Dari mana, seberapa layak dipercaya?     │
│         ↓                                                    │
│  3. PENYIAPAN       Pembersihan, pembagian, fitur —          │
│                     tanpa kebocoran                          │
│         ↓                                                    │
│  4. BASELINE        Apa yang dicapai tanpa model?            │
│         ↓                                                    │
│  5. PEMODELAN       Model mana, disetel bagaimana,           │
│                     dibandingkan dengan protokol apa?        │
│         ↓                                                    │
│  6. EVALUASI        Metrik, analisis kesalahan, audit bias   │
│         ↓                                                    │
│  7. KOMUNIKASI      Apa yang dapat DAN TIDAK DAPAT           │
│                     dilakukan model ini?                     │
└─────────────────────────────────────────────────────────────┘
```

Alur ini **tidak lurus**. Tahap 6 sering memaksa kembali ke tahap 3; tahap 4 kadang memaksa kembali ke tahap 1 karena ternyata masalahnya tidak dapat dipecahkan dengan data yang ada. Bolak-balik semacam itu normal — yang tidak normal adalah menyembunyikannya.

### 14.1.2 Pembagian Waktu yang Realistis

| Tahap | Perkiraan mahasiswa | Kenyataan |
|-------|---------------------|-----------|
| Formulasi | 5% | **15%** |
| Mencari dan memperoleh data | 10% | 15% |
| Penyiapan data | 10% | **30%** |
| *Baseline* | 2% | 3% |
| Pemodelan | **50%** | 12% |
| Evaluasi dan analisis kesalahan | 10% | 15% |
| Komunikasi | 13% | 10% |

Melatih *gradient boosting* memakan lima menit. Memastikan bahwa kolom `provinsi` menuliskan "DI Yogyakarta", "D.I. Yogyakarta", dan "Yogyakarta" sebagai entitas yang sama memakan dua jam. Ini bukan kekurangan mata kuliah; ini memang pekerjaannya.

---

## 14.2 Tahap 1 — Formulasi

Seluruh isinya ada pada Bab 2. Yang perlu ditegaskan di sini adalah **urutannya**: formulasi diselesaikan **sebelum** data dilihat lebih jauh daripada memastikan ia ada.

| Yang harus selesai sebelum melangkah | Rujukan |
|--------------------------------------|---------|
| Tujuh pertanyaan formulasi terjawab | Bab 2 §2.1.1 |
| Target dirumuskan dengan empat unsur | Bab 2 §2.1.2 |
| Metrik dipilih dari dampak kesalahan | Bab 2 §2.3 |
| **Ambang keberhasilan ditetapkan** | Bab 2 |
| Daftar fitur terlarang disusun | Bab 4 §4.5.2 |

> **Menetapkan ambang keberhasilan sebelum melihat hasil** adalah disiplin yang sama dengan menulis hipotesis sebelum melihat data pada Probabilitas dan Statistik. Tanpa itu, ambang akan selalu "kebetulan" berada tepat di bawah hasil yang diperoleh.

---

## 14.3 Tahap 2–3 — Data dan Penyiapan

### 14.3.1 Yang Dicatat pada Saat Mengunduh

| Butir | Mengapa penting |
|-------|-----------------|
| URL lengkap dan **tanggal akses** | Data terbuka sering diperbarui diam-diam |
| Dimensi saat diunduh | Pembanding setelah pembersihan |
| Lisensi | Amanah dalam memakai karya orang lain |
| **Definisi tiap variabel** | Tanpa ini, angka tidak bermakna |
| Cakupan wilayah dan periode | Menentukan batas keberlakuan kesimpulan |

**Simpan salinan data mentah dengan tanggal pada namanya.** Tanpa itu, notebook tidak dapat dijalankan ulang dengan hasil yang sama — dan reproduksibilitas adalah kriteria penilaian.

### 14.3.2 Urutan yang Benar

```
  1. Perbaikan STRUKTURAL      ── kode nilai hilang, tipe data, pembakuan
     (boleh sebelum pembagian,    nama, duplikat
      karena tidak memakai
      statistik data)
         ↓
  2. PEMBAGIAN data            ── strategi sesuai sifat data
         ↓
  3. Prapemrosesan STATISTIK   ── imputasi, penskalaan, penyandian
     (WAJIB di dalam Pipeline)     — di-fit pada latih saja
```

Melanggar urutan ini adalah penyebab kebocoran yang paling sering.

### 14.3.3 Catatan Keputusan

Setiap keputusan penyiapan dicatat dengan **tiga unsur**: apa, berapa banyak, mengapa.

```python
n_awal = len(df)

# (1) Kode nilai hilang -> NaN
n = (df["omzet"] == -99).sum()
df.loc[df["omzet"] == -99, "omzet"] = np.nan
print(f"(1) {n} nilai -99 pada kolom omzet diubah menjadi NaN "
      f"(kode nilai hilang menurut dokumentasi BPS)")

# (2) Pencilan DIPERIKSA, tidak otomatis dibuang
q1, q3 = df["omzet"].quantile([0.25, 0.75]); iqr = q3 - q1
pencilan = df[(df["omzet"] > q3 + 1.5*iqr)]
print(f"(2) {len(pencilan)} baris teridentifikasi sebagai pencilan omzet. "
      f"DIPERTAHANKAN — data sah, bukan kesalahan pencatatan. "
      f"Membuangnya akan mengubah populasi yang diwakili.")
```

> **Aturan tegas:** membuang data tanpa alasan substantif — termasuk membuang pencilan agar hasil "lebih rapi" — mengurangi nilai pada aspek kebenarannya. Pencilan hanya dibuang bila **ada bukti bahwa nilainya keliru**.

---

## 14.4 Tahap 4–5 — *Baseline* dan Pemodelan

### 14.4.1 *Baseline* Dibangun Sebelum Model Apa Pun

Tiga jenis *baseline* yang layak dilaporkan:

| Jenis | Apa yang diukurnya |
|-------|--------------------|
| `DummyClassifier`/`DummyRegressor` | Batas bawah mutlak |
| Aturan sederhana (`if-else`) | Apa yang dicapai tanpa pembelajaran |
| **Sistem yang berlaku saat ini** | Apa yang harus dikalahkan agar model berguna |

Baris ketiga yang paling bermakna dan paling sering tidak tersedia. Bila dapat diperoleh, ia mengubah seluruh pembicaraan: pertanyaannya berhenti menjadi "seberapa akurat model ini" dan menjadi "apakah model ini lebih baik daripada yang sekarang".

### 14.4.2 Protokol Perbandingan

Lima syarat pada Bab 9 §9.4.1 berlaku penuh:

- Lipatan yang sama untuk seluruh model.
- Prapemrosesan yang sesuai tiap model.
- Anggaran penyetelan yang sebanding.
- *Baseline* disertakan.
- **Simpangan dilaporkan.**

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score
import pandas as pd, numpy as np

CV = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)   # SAMA untuk semua

baris = []
for nama, pipa in kandidat.items():
    skor = cross_val_score(pipa, X_train, y_train, cv=CV, scoring="f1", n_jobs=-1)
    baris.append({"Model": nama, "F1": skor.mean(), "Simpangan": skor.std(),
                  "Min": skor.min(), "Maks": skor.max()})

t = pd.DataFrame(baris).sort_values("F1", ascending=False).reset_index(drop=True)
selisih = t.loc[0, "F1"] - t.loc[1, "F1"]
gabung = np.sqrt(t.loc[0, "Simpangan"]**2 + t.loc[1, "Simpangan"]**2)
print(t.round(4).to_string(index=False))
print(f"\nSelisih 1-2: {selisih:.4f} | Simpangan gabungan: {gabung:.4f}")
print("Kesimpulan:", "perbedaan kemungkinan nyata" if selisih > gabung
      else "TIDAK DAPAT DISIMPULKAN mana yang lebih baik")
```

---

## 14.5 Tahap 6 — Evaluasi

### 14.5.1 Tiga Lapis Evaluasi

| Lapis | Pertanyaan | Alat |
|-------|-----------|------|
| **Teknis** | Seberapa baik model bekerja? | Metrik, *baseline*, simpangan |
| **Diagnostik** | Mengapa ia salah pada kasus-kasus itu? | Kurva pembelajaran, analisis kesalahan |
| **Keadilan** | Untuk siapa ia bekerja lebih buruk? | Audit per kelompok |

Laporan yang hanya memuat lapis pertama belum selesai.

### 14.5.2 Analisis Kesalahan

Bagian yang paling sering dilewati dan paling sering mengungkap sesuatu:

```python
salah = model.predict(X_test) != y_test
print(f"Salah: {salah.sum()} dari {len(y_test)} ({salah.mean():.1%})")

# Adakah POLA?
perbandingan = pd.DataFrame({
    "Rata-rata (salah)": X_test[salah].mean(),
    "Rata-rata (benar)": X_test[~salah].mean(),
})
perbandingan["Selisih baku"] = ((perbandingan.iloc[:, 0] - perbandingan.iloc[:, 1])
                                / X_test.std())
print(perbandingan.reindex(perbandingan["Selisih baku"].abs()
                           .nlargest(5).index).round(3))
```

Tiga pertanyaan yang dijawabnya:

1. Apakah kesalahan terpusat pada **satu kelas**?
2. Apakah terpusat pada **rentang nilai tertentu**?
3. Apakah terpusat pada **kelompok tertentu**? → Bila ya, ini temuan *fairness*.

---

## 14.6 Tahap 7 — Mengomunikasikan Batas

### 14.6.1 Tiga Kalimat yang Harus Ada

1. **Apa yang dicapai** — "Model memperoleh F1 0,74 pada data uji, dibandingkan *baseline* 0,52."
2. **Seberapa besar dan seberapa yakin** — "Simpangan antarlipatan 0,03; selisih terhadap model kedua tidak bermakna."
3. **Apa yang tidak dapat dilakukan** — "Model ini tidak dapat diandalkan untuk wilayah di luar lima provinsi yang tercakup data latih, dan *recall*-nya untuk Papua hanya 0,52."

### 14.6.2 Kalimat yang Harus Dihindari

| Hindari | Ganti dengan |
|---------|--------------|
| "Model ini akurat 94%" (tanpa konteks) | "Akurasi 94%, dengan *baseline* 91% dan *recall* kelas positif 0,38" |
| "Fitur X paling memengaruhi hasil" | "Fitur X paling berkontribusi pada kemampuan model membedakan kelas" |
| "Model siap dipakai" | "Model layak diuji terbatas dengan pengawasan manusia pada kondisi A, B, C" |
| "Tidak ada keterbatasan" | Tidak ada gantinya. Kalimat ini selalu keliru. |
| "Model memutuskan" | "Model memberi rekomendasi; keputusan diambil oleh [nama peran]" |

### 14.6.3 Mengapa Hasil yang Sederhana Tetap Bernilai

> **Kelompok yang modelnya tidak mengungguli *baseline* tidak dirugikan nilainya.**
>
> Yang dinilai adalah ketepatan formulasi, kebenaran prosedur, kesesuaian metrik, dan kejujuran analisis. Melaporkan *"model terbaik kami hanya unggul 0,03 dari baseline, dengan simpangan 0,04 — sehingga kami tidak dapat menyimpulkan bahwa model ini lebih baik; berikut analisis mengapa, dan berikut yang akan kami lakukan dengan data lebih banyak"* dengan prosedur yang benar bernilai **lebih tinggi** daripada melaporkan ROC-AUC 0,99 yang ternyata mengandung kebocoran.
>
> Ini bukan kelonggaran. Di lapangan, seorang insinyur yang melaporkan "pendekatan ini tidak berhasil, dan berikut sebabnya" setelah tiga bulan bekerja menghemat organisasinya jauh lebih banyak daripada yang memaksakan hasil yang tampak baik.

---

## 14.7 Kesalahan yang Paling Sering Terjadi pada Proyek

| Kesalahan | Akibat | Pencegahan |
|-----------|--------|------------|
| Melatih model sebelum formulasi selesai | Model menjawab pertanyaan yang salah | Tujuh pertanyaan Bab 2 |
| Tidak ada *baseline* | Angka kinerja tidak bermakna | `Dummy` sejak milestone pertama |
| Transformasi di luar `Pipeline` | Kebocoran | Ketentuan sejak Bab 3 |
| Data uji dipakai berkali-kali | Kebocoran pemilihan | Data validasi untuk semua pemilihan |
| Anggaran penyetelan tidak setara | Perbandingan tidak sah | Tetapkan anggaran di awal |
| Melaporkan rerata tanpa simpangan | Kesimpulan bisa tidak bermakna | Selalu keduanya |
| Merayakan skor sangat tinggi | Kebocoran tidak terdeteksi | **Curigai lebih dahulu** |
| Tidak ada analisis kesalahan | Kehilangan temuan terpenting | Wajib di milestone 2 |
| Tidak ada audit per kelompok | Ketimpangan tersembunyi | Wajib di laporan akhir |
| Keterbatasan ditulis sebagai formalitas | Menunjukkan analisis tidak dipahami | Lima butir panduan proyek |
| Notebook tidak dapat dijalankan ulang | Melanggar kriteria kurikulum | Jalankan ulang sebelum mengumpulkan |

---

## 14.8 Daftar Periksa Akhir

**Formulasi**
- [ ] Tujuh pertanyaan terjawab dan tertulis
- [ ] Target dirumuskan dengan empat unsur
- [ ] Metrik dipilih dari dampak kesalahan, alasan tertulis
- [ ] Ambang keberhasilan ditetapkan sebelum melihat hasil
- [ ] Daftar fitur terlarang disusun beserta alasannya

**Data**
- [ ] Sumber lengkap dengan tautan dan tanggal akses
- [ ] Salinan data mentah disimpan dengan tanggal
- [ ] Definisi tiap variabel dipahami
- [ ] Setiap keputusan pembersihan dicatat: apa, berapa, mengapa
- [ ] Pencilan diperiksa, keputusannya dijelaskan

**Prosedur**
- [ ] Seluruh transformasi di dalam `Pipeline`
- [ ] Strategi pembagian sesuai sifat data
- [ ] Data uji tidak pernah dipakai untuk memilih atau menyetel
- [ ] Daftar periksa kebocoran (Bab 4 §4.6) dicentang seluruhnya
- [ ] Notebook berjalan ulang dari sel pertama tanpa galat

**Evaluasi**
- [ ] *Baseline* dilaporkan pada metrik yang sama
- [ ] Minimal tiga model dibandingkan dengan protokol yang sama
- [ ] Rerata **dan** simpangan dilaporkan
- [ ] Analisis kesalahan dengan pencarian pola
- [ ] **Audit kinerja per kelompok**

**Komunikasi**
- [ ] Ketiga kalimat §14.6.1 ada
- [ ] Tidak ada klaim sebab-akibat dari kepentingan fitur
- [ ] Keterbatasan membahas minimal empat butir
- [ ] *Model card* lengkap, termasuk bagian Etis
- [ ] Setiap grafik punya judul, label dengan satuan, dan n

**Integritas**
- [ ] AI Usage Log lengkap dan ditandatangani
- [ ] Empat baris yang wajib "dikerjakan sendiri" terisi demikian
- [ ] Pembagian peran tiap anggota dicatat

---

## AI Corner — Tahap *Create*

### Proyek Adalah Tempat Kebijakan AI Diuji

Sepanjang buku ini, pembatasan pemakaian AI dinyatakan berulang kali. Pada proyek, pembatasan itu menjadi nyata — karena di sinilah godaan terbesarnya.

| Boleh | Tidak boleh |
|-------|-------------|
| Menulis kode `scikit-learn` rutin | Memformulasikan masalah menjadi *task* ML |
| Memperbaiki galat; menjelaskan dokumentasi | Memilih model dan hiperparameter |
| Menyarankan jenis visualisasi | Memilih dan menafsirkan metrik |
| Menyunting bahasa laporan | Menganalisis kesalahan dan keterbatasan |
| Memeriksa apakah ada bagian laporan yang kosong | Menulis *model card* dan bagian etis |

### Mengapa Empat Hal di Kolom Kanan

Bukan karena sulit, dan bukan karena terlarang secara prinsip. Melainkan karena **keempatnya adalah Sub-CPMK mata kuliah ini**, dan karena keempatnya menuntut pengetahuan yang tidak ada dalam prompt:

| Keputusan | Pengetahuan yang dibutuhkan |
|-----------|----------------------------|
| Formulasi | Kapan data setiap kolom tersedia; apa yang akan dilakukan dengan keluarannya |
| Pemilihan model | Batas komputasi, kebutuhan keterjelasan, siapa yang akan memeliharanya |
| Pemilihan metrik | Berapa biaya nyata tiap jenis kesalahan |
| Analisis dan keterbatasan | Bagaimana data dikumpulkan; siapa yang tidak tercakup |

### AI Usage Log

Setiap tahap proyek wajib melampirkan catatan pemakaian AI, dengan **empat baris yang wajib ditulis "dikerjakan sendiri"** sebagaimana daftar di atas.

> Mencatat pemakaian AI **tidak mengurangi nilai**. Tidak mencatatnya, padahal memakainya, adalah pelanggaran integritas akademik — dan inilah **amanah** dalam bentuknya yang paling sehari-hari: menyatakan apa adanya tentang bagaimana sebuah pekerjaan dikerjakan, ketika tidak ada yang akan mengetahuinya bila disembunyikan.

Pada sesi tanya jawab akan ada satu pertanyaan tentang ini: *"Bagian mana yang dibantu AI? Jelaskan salah satu baris kodenya."* Mahasiswa yang memakai AI sesuai pembagian di atas akan menjawabnya dengan mudah.

---

## Latihan Soal

### Tingkat Dasar

1. Urutkan tujuh tahap proyek ML dan jelaskan satu kalimat untuk masing-masing.

2. Jelaskan urutan yang benar antara perbaikan struktural, pembagian data, dan prapemrosesan statistik. Mengapa urutan itu penting?

3. Sebutkan tiga jenis *baseline* dan jelaskan mana yang paling bermakna.

4. Sebutkan tiga lapis evaluasi dan pertanyaan yang dijawab masing-masing.

### Tingkat Menengah

5. Sebuah kelompok memperoleh F1 0,96 pada milestone pertama, jauh di atas *baseline* 0,58.
   (a) Apa reaksi pertama yang tepat?
   (b) Sebutkan lima hal yang harus diperiksa.
   (c) Bila ternyata tidak ada kebocoran, apa yang harus dilaporkan?
   (d) Bila ternyata ada, apa yang harus dilakukan?

6. Analisis kesalahan menunjukkan bahwa 62% kesalahan berasal dari satu kategori yang menyumbang 9% data.
   (a) Apa dua kemungkinan penyebabnya?
   (b) Bagaimana cara membedakan keduanya?
   (c) Apa yang harus masuk ke *model card*?
   (d) Tindakan apa yang dapat dipertimbangkan, dan apa biayanya masing-masing?

7. Sebuah kelompok menemukan pada Minggu 13 bahwa salah satu fiturnya bocor.
   (a) Apa yang harus dilakukan?
   (b) Apakah temuan ini harus dilaporkan? Mengapa?
   (c) Bagaimana pengaruhnya pada nilai, menurut rubrik?
   (d) Bandingkan dengan kelompok yang menyembunyikannya dan ketahuan saat tanya jawab.

8. Hasil akhir: model terbaik F1 0,71 ± 0,05; *baseline* 0,68.
   (a) Apakah model ini berguna?
   (b) Bagaimana Anda menuliskannya dalam kesimpulan laporan?
   (c) Apa yang akan Anda rekomendasikan kepada organisasi yang memesan model ini?
   (d) Apa yang akan Anda usulkan sebagai langkah berikutnya?

### Tingkat Mahir

9. Lakukan audit terhadap proyek ML orang lain.
   (a) Pilih satu proyek ML publik (*notebook*, repositori, atau makalah).
   (b) Terapkan daftar periksa §14.8 seluruhnya.
   (c) Untuk setiap butir yang tidak terpenuhi, taksir dampaknya terhadap keandalan hasil.
   (d) Identifikasi satu temuan yang paling mengkhawatirkan.
   (e) Tuliskan lima pertanyaan yang akan Anda ajukan kepada penulisnya, disusun agar tidak menuduh.

10. Rancang ulang proyek Anda sendiri dengan data dua kali lipat.
    (a) Berdasarkan kurva pembelajaran proyek Anda, apakah data tambahan akan membantu?
    (b) Bila ya, berapa banyak yang dibutuhkan untuk peningkatan yang bermakna?
    (c) Bila tidak, ke mana perhatian sebaiknya dialihkan?
    (d) Susun proposal satu halaman untuk tahap berikutnya, lengkap dengan taksiran biaya dan manfaat.

11. Tulislah refleksi satu halaman berjudul *"Yang Saya Pelajari dari Kegagalan pada Proyek Ini"*. Uraikan: satu keputusan yang ternyata keliru, kapan Anda menyadarinya, apa yang akan Anda lakukan berbeda, dan apa yang membuat kekeliruan itu sulit dikenali pada saat itu. Refleksi yang menyatakan tidak ada kegagalan dikembalikan.

---

## Rangkuman

1. Proyek ML terdiri atas **tujuh tahap**, dan alurnya **tidak lurus**.
2. **Penyiapan data memakan porsi waktu terbesar**, bukan pemodelan.
3. **Formulasi diselesaikan sebelum data dilihat lebih jauh**; ambang keberhasilan ditetapkan lebih dahulu.
4. Urutan yang benar: **perbaikan struktural → pembagian → prapemrosesan statistik dalam `Pipeline`**.
5. Setiap keputusan penyiapan dicatat dengan **apa, berapa banyak, mengapa**.
6. **Pencilan hanya dibuang bila terbukti keliru** — bukan agar hasil lebih rapi.
7. ***Baseline* dibangun sebelum model apa pun**; yang paling bermakna adalah sistem yang berlaku saat ini.
8. Perbandingan menuntut **lipatan sama, anggaran setara, dan pelaporan simpangan**.
9. Evaluasi berjalan **tiga lapis**: teknis, diagnostik, dan keadilan.
10. Laporan wajib menyatakan **apa yang tidak dapat dilakukan model**.
11. **Hasil yang sederhana tetap bernilai** bila prosedurnya benar dan pelaporannya jujur.
12. **Tanggung jawab atas setiap angka dan setiap kalimat tetap pada penulisnya**, bukan pada alatnya.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 2. O'Reilly.
2. Huyen, C. (2022). *Designing Machine Learning Systems*. O'Reilly.
3. Kapoor, S., & Narayanan, A. (2023). Leakage and the Reproducibility Crisis in ML-based Science. *Patterns*, 4(9).
4. Mitchell, M., et al. (2019). Model Cards for Model Reporting. *FAT* '19*.
5. Sculley, D., et al. (2015). Hidden Technical Debt in Machine Learning Systems. *NeurIPS*.
6. Badan Pusat Statistik. *Sistem Informasi Rujukan Statistik*. <https://sirusa.bps.go.id>
7. Tim Kurikulum Informatika UAI (2026). *AI Curriculum Infusion Matrix*.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
