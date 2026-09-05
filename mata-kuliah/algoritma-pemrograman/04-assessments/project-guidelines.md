---
id: uai-inf101-asesmen-proyek
tipe: asesmen
judul: Panduan Proyek Akhir — Algoritma dan Pemrograman
kode_mk: INF-101
nama_mk: Algoritma dan Pemrograman
prodi: Informatika
asesmen_id: ASM-PRJ
mengukur_cpmk: [CPMK-5, CPMK-6, CPMK-7]
mengukur_sub_cpmk: [Sub-CPMK-5.7, Sub-CPMK-6.4, Sub-CPMK-6.8, Sub-CPMK-7.4, Sub-CPMK-7.6, Sub-CPMK-7.8, Sub-CPMK-7.9, Sub-CPMK-7.10, Sub-CPMK-7.11, Sub-CPMK-7.12]
bobot_persen: 0
ai_diizinkan: true
versi: 1.0
status: draft
diperbarui: 2026-09-05
---

# Panduan Proyek Akhir — Algoritma dan Pemrograman

> **Kedudukan.** Berkas ini memuat rincian yang sebelumnya berada di RPS §K. Pemindahan dilakukan agar RPS tetap ramping (Pedoman §H.1), tanpa memutus keterlacakan — RPS §L menaut ke sini.
>
> **Penilaian angka proyek dilakukan di INF-102** (bobot 35% pada peta evaluasi praktikum). Pada INF-101, proyek diukur melalui presentasi Minggu 15 yang berkontribusi pada `ASM-PAR`.

## A. Deskripsi Umum

Proyek akhir merupakan kulminasi seluruh capaian pembelajaran. Mahasiswa — individu atau kelompok maksimal 3 orang — merancang dan membangun program Python yang menyelesaikan permasalahan nyata dengan mengintegrasikan konsep yang telah dipelajari.

## B. Persyaratan Teknis

| No | Komponen | Persyaratan | Sub-CPMK terkait |
|:-:|---|---|---|
| 1 | **Bahasa & platform** | Python 3.x, dikerjakan di Google Colab | Sub-CPMK-1.4 |
| 2 | **Struktur kontrol** | Minimal seleksi (`if`/`elif`/`else`) dan perulangan (`for`/`while`) | Sub-CPMK-3.2, 3.5 |
| 3 | **Fungsi** | Minimal 5 fungsi modular dengan *docstring* | Sub-CPMK-4.1, 4.4 |
| 4 | **Struktur data** | Minimal 3 jenis berbeda (*list*, *tuple*, *dict*, *set*) dengan justifikasi pemilihan | Sub-CPMK-5.7 |
| 5 | **Algoritma** | Minimal 1 algoritma pencarian dan/atau pengurutan | Sub-CPMK-6.2, 6.6 |
| 6 | **Analisis efisiensi** | Analisis Big-O atas algoritma inti yang digunakan | Sub-CPMK-7.3, 7.4 |
| 7 | **Clean code** | Penamaan sesuai PEP 8, komentar informatif, kode terstruktur | Sub-CPMK-7.7 |
| 8 | **Testing** | Minimal 5 *assertion test* atau *unit test* sederhana | Sub-CPMK-7.7 |
| 9 | **AI Usage Log** | Dokumentasi lengkap penggunaan AI selama pengembangan | Sub-CPMK-7.6, 7.8 |
| 10 | **Dokumentasi** | README: deskripsi, cara penggunaan, desain algoritma, refleksi | Sub-CPMK-7.10 |

## C. Tahapan

| Minggu | Tahapan | Luaran |
|:-:|---|---|
| 13 | Proposal | Judul, deskripsi masalah, rencana solusi, pembagian tugas |
| 13–14 | Pengembangan | Proses *coding*, *testing*, dan dokumentasi |
| 15 | Presentasi | Presentasi 10–15 menit + *live demo* + tanya jawab + pengumpulan *notebook* dan AI Usage Log |

## D. Kriteria Penilaian

| No | Aspek | Bobot | Deskripsi | Sub-CPMK |
|:-:|---|:-:|---|---|
| 1 | **Fungsionalitas** | 30% | Program berjalan benar dan menyelesaikan masalah yang dideskripsikan | 7.10 |
| 2 | **Desain algoritma & struktur data** | 25% | Ketepatan dan efisiensi pemilihan serta implementasi | 5.7, 6.4, 7.4 |
| 3 | **Kualitas kode** | 20% | *Clean code*, modularitas, dokumentasi, *testing* | 7.7 |
| 4 | **Presentasi & komunikasi** | 15% | Kejelasan, demonstrasi, kemampuan mempertahankan keputusan desain | 7.9, 7.11 |
| 5 | **AI Usage Log & refleksi** | 10% | Kelengkapan, kejujuran, dan kedalaman refleksi | 7.6, 7.8 |
| | **TOTAL** | **100%** | | |

Setiap mahasiswa juga melakukan **telaah sejawat** atas proyek kelompok lain menggunakan rubrik yang disediakan (Sub-CPMK-7.12).

## E. Contoh Tema Proyek

Tema **bebas dipilih**, namun didorong menjawab kebutuhan nyata — ini menjadi bahan bukti kriteria **Relevansi PkM** (LAM-INFOKOM 2.0 kriteria 4) dan kebijakan *Diktisaintek Berdampak*.

| Kategori | Contoh |
|---|---|
| **Berdampak sosial** (dianjurkan) | Sistem pencatatan bank sampah RT/RW; penjadwalan relawan kegiatan sosial; kalkulator zakat dan pembagian waris; pemantauan stok posyandu |
| Sistem informasi | Manajemen perpustakaan dengan pencarian dan pengurutan; manajemen keuangan pribadi |
| Analisis data | Analisis dan visualisasi data statistik sederhana — integrasi dengan Analisis Data Statistik |
| Keamanan | Enkripsi/dekripsi pesan dengan berbagai metode *cipher* |
| Rekomendasi | Sistem rekomendasi sederhana berbasis *similarity scoring* |
| Permainan | Permainan berbasis teks: petualangan, kuis, atau teka-teki kata |

**Penandaan tema berdampak.** Kelompok yang memilih tema pada kategori *Berdampak sosial* mencantumkan penanda `#berdampak` beserta identifikasi penerima manfaat pada README proyek. Penandaan ini menjadi bukti terhimpun untuk `mutu/01-peta-mutu-mk.md` §3–§4.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
