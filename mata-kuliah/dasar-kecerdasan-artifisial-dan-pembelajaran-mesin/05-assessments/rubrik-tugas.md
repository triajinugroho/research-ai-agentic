# Rubrik Penilaian Tugas Praktikum

## Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — IF52510031

**Teknik:** Observasi (Praktek/Tugas) · **Bobot total:** 25%
**Sub-CPMK:** `DAIML-Sub-CPMK082-1` (15%) · `DAIML-Sub-CPMK102-1` (10%)

---

## 1. Ketentuan Umum

| Aspek | Ketentuan |
|-------|-----------|
| Jumlah praktikum | 13 (Minggu 1–7, 9–14) |
| Bobot per praktikum | 25% ÷ 13 ≈ **1,9%** |
| Bentuk | Notebook Google Colab (`.ipynb`) |
| Pengumpulan | Tautan Colab + berkas `.ipynb` |
| Penamaan | `NIM_Nama_LabNN.ipynb` |
| Tenggat | Awal pertemuan minggu berikutnya |
| Pengerjaan | **Perorangan** (diskusi diperbolehkan) |

---

## 2. Rubrik Umum (berlaku untuk seluruh praktikum)

| Aspek | Bobot | 4 — Sangat Baik | 3 — Baik | 2 — Cukup | 1 — Kurang |
|-------|-------|-----------------|----------|-----------|------------|
| **Kebenaran teknis** | 40% | Seluruh langkah benar; tidak ada kebocoran; hasil dapat dipertanggungjawabkan | Benar dengan kekeliruan kecil yang tidak mengubah kesimpulan | Ada kekeliruan yang memengaruhi hasil | Langkah pokok salah atau ada kebocoran |
| **Kesesuaian metode dan metrik** | 25% | Tepat untuk jenis data dan masalah; **alasan tertulis** | Tepat, alasan kurang tajam | Dapat diterima tetapi bukan pilihan yang optimal | Tidak sesuai jenis data |
| **Kualitas interpretasi** | 25% | Tajam; sebatas yang didukung data; keterbatasan dinyatakan | Tepat; keterbatasan kurang dibahas | Ada klaim yang melampaui data | Tidak ada kalimat interpretasi |
| **Reproduksibilitas dan kerapian** | 10% | Berjalan ulang mulus; versi tercatat; `random_state` ditetapkan; terstruktur | Berjalan dengan penyesuaian kecil | Perlu perbaikan agar berjalan | Tidak dapat dijalankan |

### Konversi

$$\text{Nilai praktikum} = \left(\sum_{\text{aspek}} \frac{\text{skor}}{4} \times \text{bobot aspek}\right) \times 1{,}9\%$$

---

## 3. Kriteria Khusus per Praktikum

Selain rubrik umum, tiap praktikum memiliki satu kriteria khusus yang menjadi penekanan. Kriteria ini masuk dalam aspek **Kebenaran teknis**.

| Lab | Mg | Sub-CPMK | Kriteria khusus |
|-----|----|----------|-----------------|
| [01](../04-labs/lab-01-setup-ekosistem-ml.md) | 1 | 082-1 | Ketepatan penentuan jenis *task*; **alasan tertulis mengapa ML diperlukan atau tidak** |
| [02](../04-labs/lab-02-formulasi-masalah-baseline.md) | 2 | 082-1 | Metrik dipilih dari **dampak kesalahan**; *baseline* dilaporkan dan ditafsirkan |
| [03](../04-labs/lab-03-pipeline-prapemrosesan.md) | 3 | 102-1 | **Seluruh transformasi di dalam `Pipeline`**; ordinal disandikan dengan urutan yang ditentukan |
| [04](../04-labs/lab-04-validasi-silang-deteksi-kebocoran.md) | 4 | 102-1 | Jumlah kebocoran yang ditemukan; **ketepatan penjelasan mekanismenya** |
| [05](../04-labs/lab-05-rekayasa-fitur.md) | 5 | 102-1 | Model tetap terkunci; peningkatan diukur pada **validasi**; **catatan fitur yang gagal** |
| [06](../04-labs/lab-06-model-regresi-dan-metrik.md) | 6 | 082-1 | Perhitungan manual benar; α ditentukan lewat CV; penjelasan mengapa metrik berbeda kesimpulan |
| [07](../04-labs/lab-07-klasifikasi-dan-metrik.md) | 7 | 082-1 | Matriks konfusi dihitung manual dengan benar; **ambang ditentukan dari biaya kesalahan** |
| [09](../04-labs/lab-09-pohon-keputusan-dan-ensemble.md) | 9 | 082-1 | *Entropy* dan *information gain* manual benar; bias kepentingan fitur ditunjukkan |
| [10](../04-labs/lab-10-svm-naive-bayes-penyetelan.md) | 10 | 082-1 | Penyetelan **tidak menyentuh data uji**; perbandingan memakai lipatan yang sama |
| [11](../04-labs/lab-11-clustering-dan-metriknya.md) | 11 | 082-1 | **Penafsiran klaster substantif** — nama, ciri, dan usulan tindakan |
| [12](../04-labs/lab-12-pca-dan-visualisasi-model.md) | 12 | 102-1 | **Diagnosis tertulis** dari kurva pembelajaran; analisis pola kesalahan |
| [13](../04-labs/lab-13-jaringan-saraf-tiruan.md) | 13 | 082-1 | Langkah maju-mundur manual benar; **kesimpulan jujur** pada perbandingan MLP vs RF |
| [14](../04-labs/lab-14-audit-bias-dan-model-card.md) | 14 | 102-1 | Audit pada **model sendiri**; *model card* memuat keterbatasan yang jujur |

---

## 4. Yang Menggugurkan Nilai Penuh

Hal-hal berikut membatasi skor aspek **Kebenaran teknis** pada maksimal 2, berapa pun baiknya bagian lain:

| Temuan | Alasan |
|--------|--------|
| **Kebocoran data** | Melanggar kriteria kurikulum *"correctness preprocessing dan split"* |
| Transformasi di luar `Pipeline` | Sumber kebocoran struktural |
| Data uji dipakai untuk memilih atau menyetel | Kebocoran pemilihan |
| Notebook tidak dapat dijalankan ulang | Melanggar kriteria *"reproduksibilitas eksperimen"* |
| Hasil dilaporkan tanpa *baseline* | Angka tanpa pembanding tidak bermakna |
| Akurasi dilaporkan sendirian pada data tak seimbang | Kesimpulan menyesatkan |

---

## 5. Yang Tidak Mengurangi Nilai

Agar tidak salah paham, berikut hal-hal yang **tidak** mengurangi nilai:

| Hal | Alasan |
|-----|--------|
| Model berkinerja rendah | Yang dinilai adalah prosedur, bukan angka kinerja |
| Model tidak mengungguli *baseline* | Temuan yang sah, bila dilaporkan jujur dengan analisisnya |
| Fitur yang dicoba ternyata tidak membantu | **Justru bernilai** bila dicatat beserta dugaan sebabnya |
| Hasil berbeda dari dugaan awal | Yang dinilai adalah kejujuran pelaporannya |
| Memakai AI untuk menulis kode rutin | Diperbolehkan, asalkan dicatat pada AI Usage Log |

---

## 6. AI Usage Log — Wajib

Setiap notebook wajib memuat AI Usage Log pada sel terakhir. Log yang mencantumkan AI pada salah satu dari **empat baris berikut dikembalikan**:

1. Formulasi masalah menjadi *task* ML
2. Pemilihan model dan hiperparameter
3. Pemilihan dan penafsiran metrik
4. Analisis kesalahan dan keterbatasan

Format lengkap ada pada [RTM §I](../02-rtm/rtm-dasar-kecerdasan-artifisial-pembelajaran-mesin.md).

---

## 7. Keterlambatan

| Keterlambatan | Pengurangan |
|---------------|-------------|
| ≤ 24 jam | −10% |
| 24–72 jam | −25% |
| > 72 jam | Tidak dinilai |

Kecuali dengan alasan yang dapat diterima dan disampaikan **sebelum** tenggat.

---

## 8. Umpan Balik

| Aspek | Ketentuan |
|-------|-----------|
| Waktu pengembalian | Paling lambat 1 minggu setelah tenggat |
| Bentuk | Skor per aspek + catatan tertulis pada bagian yang perlu diperbaiki |
| Kesempatan perbaikan | Praktikum yang dikembalikan karena kebocoran atau AI Log dapat diperbaiki dalam 3 hari, dinilai sebagai terlambat ≤ 24 jam |

---

## 9. Contoh Perhitungan

Seorang mahasiswa mengumpulkan Lab 07 dengan penilaian:

| Aspek | Bobot | Skor | Perhitungan | Nilai |
|-------|-------|------|-------------|-------|
| Kebenaran teknis | 40% | 4 | 4/4 × 40% | 40,0% |
| Kesesuaian metode dan metrik | 25% | 3 | 3/4 × 25% | 18,75% |
| Kualitas interpretasi | 25% | 4 | 4/4 × 25% | 25,0% |
| Reproduksibilitas | 10% | 3 | 3/4 × 10% | 7,5% |
| **Jumlah** | | | | **91,25%** |

Nilai terhadap total mata kuliah: 91,25% × 1,9% = **1,73%** dari 100%.

---

## 10. Dokumen Terkait

| Dokumen | Isi |
|---------|-----|
| [Kerangka asesmen](assessment-framework.md) | Bobot resmi dan kriteria kurikulum |
| [RTM](../02-rtm/rtm-dasar-kecerdasan-artifisial-pembelajaran-mesin.md) | Rincian tiap tugas dan format AI Usage Log |
| [Panduan proyek](project-guidelines.md) | Rubrik proyek |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
