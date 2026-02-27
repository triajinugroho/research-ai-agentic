# Panduan Proyek Akhir

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — UAI — Semester Genap 2025/2026
### Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.

---

## 1. Deskripsi Proyek

Proyek akhir merupakan kulminasi dari seluruh pembelajaran selama semester. Kelompok mahasiswa (2-3 orang) melakukan **analisis data end-to-end** pada dataset riil Indonesia, menggunakan metode statistik yang telah dipelajari, dengan **AI sebagai co-analyst yang didokumentasikan**.

Proyek ini menguji kemampuan mahasiswa untuk:
- Merumuskan pertanyaan penelitian yang bermakna
- Memilih dan mengaplikasikan metode statistik yang tepat
- Menggunakan Python untuk analisis dan visualisasi
- Menginterpretasi hasil secara kritis
- Berkolaborasi dengan AI secara bertanggung jawab
- Mengkomunikasikan temuan secara efektif

**Bobot:** 25% dari nilai akhir

---

## 2. Timeline Proyek

| Minggu | Milestone | Deliverable |
|--------|-----------|-------------|
| 9 | Kickoff: pengumuman, pembentukan kelompok, brainstorm topik | — |
| 10 | Proposal disetujui | Proposal (1 halaman) via LMS |
| 11 | Exploratory Data Analysis selesai | Progress check di kelas |
| 12 | Analisis statistik utama selesai | — |
| 13 | Draft notebook dan laporan | Draft untuk review dosen |
| 14 | Finalisasi + persiapan presentasi | — |
| 15 | **Presentasi + Peer Review** | Semua deliverables dikumpulkan |

---

## 3. Deliverables

### 3.1 Jupyter Notebook (40% dari nilai proyek)

**Format:** File `.ipynb` yang sudah dijalankan semua cell-nya

**Struktur wajib:**
```
1. Judul & Anggota Kelompok
2. Latar Belakang & Pertanyaan Penelitian
3. Deskripsi Dataset
4. Exploratory Data Analysis (EDA)
   - Statistik deskriptif
   - Visualisasi data (minimal 5 chart)
   - Identifikasi missing values & outliers
5. Analisis Statistik
   - Minimal 2 metode berbeda (misal: uji hipotesis + regresi)
   - Justifikasi pemilihan metode
   - Cek asumsi
6. Hasil & Interpretasi
7. Kesimpulan & Limitasi
8. Dokumentasi Penggunaan AI (wajib)
9. Referensi
```

**Kriteria kode:**
- Kode berjalan tanpa error dari awal sampai akhir
- Well-commented (setiap blok kode ada penjelasan)
- Menggunakan library yang dipelajari: pandas, numpy, matplotlib, seaborn, scipy, sklearn
- Markdown cells menjelaskan setiap langkah

### 3.2 Laporan Tertulis (30% dari nilai proyek)

**Format:** PDF, 3-5 halaman (tidak termasuk referensi)

**Struktur:**
1. **Pendahuluan** (0.5 halaman) — Latar belakang, motivasi, pertanyaan penelitian
2. **Data & Metodologi** (1 halaman) — Deskripsi dataset, metode yang digunakan, justifikasi
3. **Hasil** (1-1.5 halaman) — Temuan utama dengan visualisasi kunci (pilih 3-4 chart terbaik)
4. **Diskusi** (0.5-1 halaman) — Interpretasi, implikasi, limitasi, saran
5. **Kesimpulan** (0.5 halaman) — Ringkasan temuan, jawaban pertanyaan penelitian
6. **Referensi** — Format APA

**Catatan:** Laporan ditulis dalam Bahasa Indonesia. Istilah teknis boleh dalam Bahasa Inggris.

### 3.3 Presentasi (20% dari nilai proyek)

**Format:** Slide deck (Google Slides/PowerPoint), 10 menit presentasi + 5 menit Q&A

**Struktur slide yang direkomendasikan:**
| No | Slide | Konten |
|----|-------|--------|
| 1 | Judul | Judul proyek, nama kelompok, tanggal |
| 2 | Masalah | Pertanyaan penelitian & mengapa penting |
| 3 | Data | Sumber, ukuran, variabel utama |
| 4 | Metodologi | Metode yang digunakan (diagram/flowchart) |
| 5-7 | Hasil | Visualisasi kunci + temuan utama |
| 8 | Diskusi | Interpretasi, limitasi |
| 9 | Kesimpulan | Jawaban pertanyaan penelitian, rekomendasi |
| 10 | Q&A | Terima kasih, siap menerima pertanyaan |

**Tips presentasi:**
- Jangan baca slide — gunakan slide sebagai visual aid
- Setiap anggota kelompok harus mempresentasikan bagiannya
- Latihan sebelumnya — 10 menit cepat berlalu
- Fokus pada insight, bukan pada kode

### 3.4 AI Usage Log (10% dari nilai proyek)

**Format:** Section terakhir di Jupyter Notebook ATAU dokumen terpisah

**Template:**
```markdown
## Dokumentasi Penggunaan AI dalam Proyek

### Ringkasan
- Total interaksi AI: [jumlah]
- AI tools yang digunakan: [list]
- Persentase estimasi kontribusi AI: [X%]

### Log Interaksi

#### Interaksi 1
- **Tahap:** [EDA / Analisis / Interpretasi / Kode / Lainnya]
- **Prompt:** [copy-paste prompt yang digunakan]
- **Output AI:** [ringkasan output]
- **Keputusan:** [diterima / dimodifikasi / ditolak]
- **Alasan:** [mengapa menerima/memodifikasi/menolak]

#### Interaksi 2
[...dst]

### Refleksi
1. Pada tahap mana AI paling membantu?
2. Pada tahap mana AI kurang membantu atau menyesatkan?
3. Apa yang dipelajari dari berkolaborasi dengan AI?
4. Apakah hasil analisis akan berbeda tanpa AI? Mengapa?
```

---

## 4. Contoh Topik Proyek

### Topik dengan Dataset Publik Indonesia

| No | Topik | Dataset | Metode yang Mungkin |
|----|-------|---------|---------------------|
| 1 | Faktor-faktor yang mempengaruhi IPM per provinsi | BPS - IPM | Regresi berganda, korelasi |
| 2 | Analisis kesenjangan pendidikan antar wilayah | BPS - Pendidikan | ANOVA, visualisasi, deskriptif |
| 3 | Prediksi tingkat pengangguran berdasarkan indikator ekonomi | BPS - Ketenagakerjaan | Regresi, ML klasifikasi |
| 4 | Pola pengeluaran rumah tangga Indonesia | Susenas/BPS | Clustering, deskriptif, ANOVA |
| 5 | Analisis tren kualitas udara Jakarta | Open data Jakarta | Time series deskriptif, korelasi |
| 6 | Faktor yang mempengaruhi kelulusan tepat waktu mahasiswa | Data internal (anonim) | Logistic regression, chi-square |
| 7 | Perbandingan indikator kesehatan antar provinsi | BPS - Kesehatan | ANOVA, non-parametrik |
| 8 | Analisis sentimen review aplikasi e-commerce | Google Play scraping | Chi-square, deskriptif (jika simplified) |
| 9 | Hubungan akses internet dan pencapaian akademik | BPS + Kemendikbud | Korelasi, regresi, chi-square |
| 10 | Prediksi curah hujan berdasarkan data historis | BMKG open data | Regresi, distribusi, CLT |

### Panduan Memilih Topik

- **Relevansi:** Pilih topik yang menarik bagi kelompok dan relevan dengan Indonesia
- **Ketersediaan data:** Pastikan dataset accessible dan cukup besar (minimal 100 observasi)
- **Feasibility:** Pastikan bisa diselesaikan dalam 7 minggu dengan tools yang dipelajari
- **Kedalaman:** Harus bisa menerapkan minimal 2 metode statistik berbeda
- **Originalitas:** Hindari duplikasi topik antar kelompok

---

## 5. Rubrik Penilaian Proyek Akhir

### 5.1 Jupyter Notebook (40%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **EDA** (10%) | EDA komprehensif: deskriptif + 5+ visualisasi + outlier handling + insight bermakna | EDA solid dengan beberapa visualisasi | EDA dasar, visualisasi minimal | EDA tidak ada atau sangat minim |
| **Metode statistik** (10%) | 2+ metode tepat, asumsi dicek, justifikasi kuat | 2 metode, beberapa asumsi dicek | 1 metode, tanpa cek asumsi | Metode salah atau tidak ada |
| **Interpretasi** (10%) | Interpretasi mendalam, kontekstual, limitasi didiskusikan | Interpretasi benar, beberapa konteks | Interpretasi superfisial | Tidak ada atau salah |
| **Kualitas kode** (10%) | Kode clean, efficient, well-documented, reproducible | Kode berjalan, beberapa comment | Kode berjalan tapi berantakan | Kode error, tidak lengkap |

### 5.2 Laporan Tertulis (30%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Struktur & writing** (10%) | Terstruktur rapi, bahasa akademik, flow logis | Cukup terstruktur, bahasa baik | Kurang terstruktur | Tidak terstruktur |
| **Metodologi** (10%) | Metode dijelaskan dan dijustifikasi dengan baik | Metode dijelaskan | Metode disebutkan tanpa justifikasi | Metode tidak jelas |
| **Temuan & insight** (10%) | Temuan bermakna, didukung data, implikasi jelas | Temuan ada, didukung data | Temuan superfisial | Tidak ada temuan jelas |

### 5.3 Presentasi (20%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Delivery** (7%) | Percaya diri, semua anggota presentasi, engaging | Cukup baik, sebagian besar lancar | Kurang percaya diri, monoton | Membaca slide, tidak jelas |
| **Visual & slide** (6%) | Slide clean, visualisasi jelas, tidak terlalu banyak teks | Slide cukup baik | Slide terlalu penuh teks | Slide buruk |
| **Q&A handling** (7%) | Menjawab dengan tepat dan percaya diri | Menjawab dengan benar | Menjawab sebagian | Tidak bisa menjawab |

### 5.4 AI Usage Log (10%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Kelengkapan dokumentasi** (5%) | Semua interaksi AI terdokumentasi dengan detail | Sebagian besar terdokumentasi | Dokumentasi minim | Tidak ada dokumentasi |
| **Refleksi kritis** (5%) | Refleksi mendalam tentang kapan AI membantu/tidak, lessons learned | Refleksi ada tapi kurang mendalam | Refleksi sangat singkat | Tidak ada refleksi |

---

## 6. Panduan Peer Review

Setiap mahasiswa akan me-review **2 kelompok lain** menggunakan form berikut:

### Form Peer Review

```
Kelompok yang di-review: _______________
Reviewer: _______________

Beri skor 1-4 untuk setiap kriteria:

1. Kejelasan pertanyaan penelitian:        [ ] 1  [ ] 2  [ ] 3  [ ] 4
2. Kesesuaian metode dengan pertanyaan:    [ ] 1  [ ] 2  [ ] 3  [ ] 4
3. Kualitas visualisasi:                   [ ] 1  [ ] 2  [ ] 3  [ ] 4
4. Kedalaman interpretasi:                 [ ] 1  [ ] 2  [ ] 3  [ ] 4
5. Kualitas presentasi:                    [ ] 1  [ ] 2  [ ] 3  [ ] 4
6. Dokumentasi penggunaan AI:              [ ] 1  [ ] 2  [ ] 3  [ ] 4

Komentar konstruktif (wajib, minimal 3 kalimat):
_____________________________________________

Hal terbaik dari proyek ini:
_____________________________________________

Saran perbaikan:
_____________________________________________
```

**Nilai peer review berkontribusi 5% dari nilai presentasi** (bagian dari 20% presentasi).

---

## 7. Panduan Submission

### Apa yang Dikumpulkan (Minggu 15, sebelum presentasi)

1. **Jupyter Notebook:** `ProyekAkhir_Kelompok[X]_[TopikSingkat].ipynb`
2. **Laporan PDF:** `Laporan_Kelompok[X]_[TopikSingkat].pdf`
3. **Slide presentasi:** `Presentasi_Kelompok[X]_[TopikSingkat].pptx` atau link Google Slides
4. **Dataset** (jika kecil) atau **link ke dataset** (jika besar)

### Dimana Mengumpulkan

- **LMS UAI** — Upload semua file (wajib)
- **GitHub** — Push notebook ke repository kelompok (disarankan, bonus portfolio)

### Checklist Sebelum Submit

- [ ] Notebook berjalan dari awal sampai akhir tanpa error (Restart & Run All)
- [ ] Semua visualisasi terlihat di notebook
- [ ] Dokumentasi AI Usage lengkap
- [ ] Laporan PDF formatted rapi, 3-5 halaman
- [ ] Slide presentasi ready
- [ ] Semua anggota tahu bagian presentasinya

---

## 8. FAQ

**Q: Bolehkah menggunakan dataset dari Kaggle?**
A: Boleh, asalkan ada relevansi dengan Indonesia atau mahasiswa bisa menjelaskan konteksnya. Prioritaskan dataset Indonesia.

**Q: Berapa banyak metode statistik yang harus digunakan?**
A: Minimal 2 metode berbeda (misal: uji hipotesis + regresi, atau ANOVA + chi-square).

**Q: Bagaimana jika data yang ditemukan tidak sesuai asumsi?**
A: Justru ini menarik! Dokumentasikan bahwa asumsi tidak terpenuhi dan pilih alternatif (misal: non-parametrik). Proses pemikiran ini dinilai.

**Q: Apakah semua anggota kelompok mendapat nilai yang sama?**
A: Pada prinsipnya ya, kecuali ada bukti kontribusi yang sangat tidak merata. Setiap kelompok akan mengisi peer evaluation internal.

**Q: Bolehkah menggunakan metode yang belum diajarkan?**
A: Boleh sebagai bonus, tapi pastikan metode yang diajarkan tetap ada. Penggunaan metode advance tanpa pemahaman justru akan mengurangi nilai.

**Q: Seberapa banyak AI boleh digunakan?**
A: Tidak ada batas, ASALKAN didokumentasikan dan mahasiswa memahami setiap langkah. Jika ditanya saat presentasi dan tidak bisa menjelaskan, itu masalah.

---

*Dokumen ini merupakan bagian dari RPS mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia.*
