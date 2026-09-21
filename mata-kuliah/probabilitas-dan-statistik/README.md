# Probabilitas dan Statistik — IF52510033

> **Mata Kuliah:** Probabilitas dan Statistik (3 SKS)
> **Semester:** Ganjil 2026/2027 (Tingkat 1, Semester 1)
> **Kelas:** IF26A, IF26H
> **Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.
> **Kurikulum:** Informatika 2025 — Revisi 2026

Materi kuliah lengkap untuk mata kuliah **Probabilitas dan Statistik** Program Studi Informatika, Universitas Al Azhar Indonesia. Seluruh dokumen disusun mengikuti [referensi Kurikulum Informatika 2025 Revisi 2026](../00-kurikulum-if-2025-revisi-2026/) — kode mata kuliah, CPL, CPMK, Sub-CPMK, dan bobot penilaiannya diambil langsung dari sana.

---

## Tentang Mata Kuliah

| Atribut | Detail |
|---------|--------|
| **Kode** | IF52510033 |
| **SKS** | 3 |
| **Semester** | 1 (Ganjil) |
| **Kelompok MK** | MKP — Mata Kuliah Inti Prodi (Wajib) |
| **Rumpun Keilmuan** | Matematika & Fondasi Komputasi (R02) |
| **Bahan Kajian** | BK08 — *Mathematical and Statistical Foundations* |
| **Prasyarat** | — |
| **CPL** | CPL08, CPL10 |
| **CPMK** | CPMK081, CPMK102 |
| **Sub-CPMK** | `PS-Sub-CPMK081-1` (45%), `PS-Sub-CPMK102-1` (55%) |
| **Tahap AI** | F (Foundation) · Mode K (Kontekstual) · Pilar DS–AI |

### Mengapa mata kuliah ini penting

Sepuluh mata kuliah di semester berikutnya bergantung pada fondasi yang dibangun di sini — dari Analisis Data Statistik (Sem 2) sampai Tugas Akhir (Sem 8). Pada AI Curriculum Infusion Matrix, perannya dinyatakan tegas: *fondasi uncertainty, inference dan ML*, dengan prinsip **mahasiswa tidak boleh menjadi sekadar pengguna model/API**.

---

## Capaian Pembelajaran

### Sub-CPMK 1 — `PS-Sub-CPMK081-1` (CPL08 / CPMK081, Bloom C3–C4, bobot 45%)

> Mampu menerapkan (C3) dan menganalisis (C4) konsep probabilitas, peubah acak, distribusi, estimasi, dan inferensi sebagai fondasi perancangan metode komputasi dan pembelajaran mesin.

### Sub-CPMK 2 — `PS-Sub-CPMK102-1` (CPL10 / CPMK102, Bloom C3–C4/P2–P3, bobot 55%)

> Mampu mengolah (C3/P2), menganalisis (C4), dan memvisualisasikan (C3/P3) data menggunakan statistika deskriptif dan inferensial untuk menghasilkan kesimpulan yang valid.

---

## Struktur Repositori

```
probabilitas-dan-statistik/
├── README.md                       # Berkas ini
├── 00-strategic-analysis/          # Analisis SWOT, Porter, tren statistika era AI
├── 01-rps/                         # Rencana Pembelajaran Semester
├── 02-rtm/                         # Rencana Tugas Mahasiswa
├── 03-modules/                     # 16 modul mingguan
├── 04-labs/                        # 13 lab hands-on Python
├── 05-assessments/                 # Kerangka asesmen, kisi-kisi, rubrik, panduan proyek
├── 06-buku-ajar/                   # Buku ajar 14 bab + pendukung
└── datasets/                       # Panduan dataset dan sumber data Indonesia
```

---

## Peta Materi 16 Minggu

### Fase 1 — Membaca Data: *Describe What Happened* (Minggu 1–3)

| Minggu | Topik | Modul | Lab |
|--------|-------|-------|-----|
| 1 | Pengantar statistika, data, dan ketidakpastian dalam computing | [week-01](03-modules/week-01-pengantar-statistika-data-ketidakpastian.md) | [lab-01](04-labs/lab-01-setup-colab-eksplorasi-data.md) |
| 2 | Statistika deskriptif — pemusatan, penyebaran, posisi | [week-02](03-modules/week-02-statistika-deskriptif.md) | [lab-02](04-labs/lab-02-statistika-deskriptif-pandas.md) |
| 3 | Visualisasi data statistik | [week-03](03-modules/week-03-visualisasi-data-statistik.md) | [lab-03](04-labs/lab-03-studio-visualisasi-statistik.md) |

### Fase 2 — Mengukur Peluang: *Reason About Uncertainty* (Minggu 4–7)

| Minggu | Topik | Modul | Lab |
|--------|-------|-------|-----|
| 4 | Dasar probabilitas | [week-04](03-modules/week-04-dasar-probabilitas.md) | [lab-04](04-labs/lab-04-simulasi-probabilitas-monte-carlo.md) |
| 5 | Teorema Bayes dan kebebasan | [week-05](03-modules/week-05-teorema-bayes-kebebasan.md) | [lab-05](04-labs/lab-05-bayes-penyaring-spam.md) |
| 6 | Peubah acak diskret dan distribusinya | [week-06](03-modules/week-06-peubah-acak-diskret.md) | [lab-06](04-labs/lab-06-distribusi-diskret-scipy.md) |
| 7 | Peubah acak kontinu dan distribusi normal | [week-07](03-modules/week-07-peubah-acak-kontinu-normal.md) | [lab-07](04-labs/lab-07-distribusi-kontinu-uji-kenormalan.md) |
| 8 | **Ujian Tengah Semester** | [week-08](03-modules/week-08-uts-review-dan-ujian.md) | — |

### Fase 3 — Menarik Kesimpulan: *Infer Beyond the Sample* (Minggu 9–13)

| Minggu | Topik | Modul | Lab |
|--------|-------|-------|-----|
| 9 | Ekspektasi, varians, dan distribusi sampling | [week-09](03-modules/week-09-ekspektasi-varians-distribusi-sampling.md) | [lab-09](04-labs/lab-09-simulasi-teorema-limit-pusat.md) |
| 10 | Estimasi titik dan interval kepercayaan | [week-10](03-modules/week-10-estimasi-interval-kepercayaan.md) | [lab-10](04-labs/lab-10-interval-kepercayaan-cakupan.md) |
| 11 | Uji hipotesis satu sampel | [week-11](03-modules/week-11-uji-hipotesis-satu-sampel.md) | [lab-11](04-labs/lab-11-uji-hipotesis-satu-sampel.md) |
| 12 | Uji hipotesis dua sampel dan uji proporsi | [week-12](03-modules/week-12-uji-hipotesis-dua-sampel.md) | [lab-12](04-labs/lab-12-ab-testing-dua-sampel.md) |
| 13 | ANOVA satu arah dan uji chi-square | [week-13](03-modules/week-13-anova-chi-square.md) | [lab-13](04-labs/lab-13-anova-chi-square.md) |

### Fase 4 — Menghubungkan: *Model the Relationship* (Minggu 14–16)

| Minggu | Topik | Modul | Lab |
|--------|-------|-------|-----|
| 14 | Korelasi dan pengantar regresi linear | [week-14](03-modules/week-14-korelasi-regresi-linear.md) | [lab-14](04-labs/lab-14-korelasi-regresi-linear.md) |
| 15 | Presentasi proyek analisis data | [week-15](03-modules/week-15-presentasi-proyek.md) | — |
| 16 | **Ujian Akhir Semester** | [week-16](03-modules/week-16-uas-review-dan-ujian.md) | — |

---

## Buku Ajar

| Bab | Judul |
|-----|-------|
| — | [Halaman depan dan daftar isi](06-buku-ajar/00-halaman-depan.md) |
| — | [Mengapa buku ini ditulis](06-buku-ajar/mengapa-buku-ini.md) |
| 1 | [Pengantar Statistika dan Ketidakpastian dalam Computing](06-buku-ajar/bab-01-pengantar-statistika-ketidakpastian.md) |
| 2 | [Statistika Deskriptif](06-buku-ajar/bab-02-statistika-deskriptif.md) |
| 3 | [Visualisasi Data Statistik](06-buku-ajar/bab-03-visualisasi-data-statistik.md) |
| 4 | [Dasar Probabilitas](06-buku-ajar/bab-04-dasar-probabilitas.md) |
| 5 | [Probabilitas Bersyarat dan Teorema Bayes](06-buku-ajar/bab-05-probabilitas-bersyarat-bayes.md) |
| 6 | [Peubah Acak dan Distribusi Diskret](06-buku-ajar/bab-06-peubah-acak-distribusi-diskret.md) |
| 7 | [Distribusi Kontinu dan Distribusi Normal](06-buku-ajar/bab-07-distribusi-kontinu-normal.md) |
| 8 | [Ekspektasi, Varians, dan Distribusi Sampling](06-buku-ajar/bab-08-ekspektasi-varians-sampling.md) |
| 9 | [Estimasi dan Interval Kepercayaan](06-buku-ajar/bab-09-estimasi-interval-kepercayaan.md) |
| 10 | [Uji Hipotesis Satu Sampel](06-buku-ajar/bab-10-uji-hipotesis-satu-sampel.md) |
| 11 | [Uji Hipotesis Dua Sampel dan Proporsi](06-buku-ajar/bab-11-uji-hipotesis-dua-sampel.md) |
| 12 | [ANOVA dan Uji Chi-Square](06-buku-ajar/bab-12-anova-chi-square.md) |
| 13 | [Statistika dengan Bantuan AI: Batas dan Tanggung Jawab](06-buku-ajar/bab-13-statistika-dengan-bantuan-ai.md) |
| 14 | [Proyek Akhir: Analisis Data Statistik End-to-End](06-buku-ajar/bab-14-proyek-akhir.md) |
| — | [Lampiran](06-buku-ajar/lampiran.md) · [Penutup](06-buku-ajar/penutup.md) |

---

## Bobot Penilaian

Bobot melekat pada Sub-CPMK sesuai penetapan Kurikulum 2025 Revisi 2026.

| Teknik Penilaian | PS-Sub-CPMK081-1 | PS-Sub-CPMK102-1 | Total |
|------------------|------------------|------------------|-------|
| Kuis (4×) | 15% | – | **15%** |
| Observasi — laporan lab (13×) | – | 25% | **25%** |
| Unjuk Kerja — proyek + presentasi | 5% | 5% | **10%** |
| Tes Tulis — UTS | – | 25% | **25%** |
| Tes Tulis — UAS | 25% | – | **25%** |
| **Total** | **45%** | **55%** | **100%** |

Tidak ada komponen Partisipasi pada mata kuliah ini.

---

## Kebijakan AI

Mata kuliah ini berstatus **tahap F (Foundation), mode K (Kontekstual)** — **tidak ada Sub-CPMK AI tersendiri**.

| Kegiatan | AI |
|----------|-----|
| Memahami konsep, mencari penjelasan alternatif | Diizinkan |
| Memeriksa ulang hitungan yang sudah dikerjakan sendiri | Diizinkan |
| Membantu menulis kode visualisasi | Diizinkan, wajib dicatat di AI Usage Log |
| Mengerjakan soal latihan atau kuis | **Tidak diizinkan** |
| UTS dan UAS | **Tidak diizinkan** |
| Menentukan uji statistik dan menafsirkan hasil proyek | **Tidak diizinkan sebagai penentu** |

**AI Usage Log wajib** pada setiap laporan lab dan laporan proyek. Formatnya ada di [RTM Bagian I](02-rtm/rtm-probabilitas-dan-statistik.md).

---

## Tools

| Tool | Fungsi |
|------|--------|
| Python 3.x | Bahasa komputasi |
| Google Colab | Lingkungan kerja (tanpa instalasi) |
| NumPy | Komputasi numerik |
| pandas | Manipulasi data |
| matplotlib, seaborn | Visualisasi statistik |
| `scipy.stats` | Distribusi dan uji statistik |
| statsmodels | Regresi dan ANOVA |

---

## Sumber Data

Seluruh contoh dan proyek memakai data berkonteks Indonesia. Panduan lengkap ada di [datasets/README.md](datasets/README.md).

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
