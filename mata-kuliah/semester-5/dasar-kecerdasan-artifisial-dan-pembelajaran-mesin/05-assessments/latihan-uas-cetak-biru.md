---
id: uai-if52510031-latihan-uas-cetak-biru
tipe: asesmen
judul: "Latihan UAS — Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — Cetak Biru Butir dan Panduan Varian"
kode_mk: IF52510031
nama_mk: Dasar Kecerdasan Artifisial dan Pembelajaran Mesin
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-09
---

# Cetak Biru Butir dan Panduan Varian — Latihan UAS Dasar Kecerdasan Artifisial dan Pembelajaran Mesin

## Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — IF52510031

> **Latihan UAS — bukan naskah UAS.** Cetak biru ini menyertai simulasi lengkap UAS Dasar Kecerdasan Artifisial dan Pembelajaran Mesin Ganjil 2026/2027 untuk berlatih: komposisi, durasi (120 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UAS. Naskah UAS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> Berkas ini untuk dosen dan penelaah: tabel butir, ringkasan per Sub-CPMK/Bloom/bagian/minggu, model waktu dan uji coba berwaktu, serta [panduan menyusun varian](#6-panduan-menyusun-varian-naskah-uas-sebenarnya). Pasangan berkas: [latihan UAS](latihan-uas.md) dan [pembahasan dan pedoman skor](latihan-uas-pembahasan.md).

| Aspek | Keterangan | Acuan |
|-------|------------|-------|
| Waktu, bentuk | Minggu 16 · tes tulis · 120 menit · *closed book* · kalkulator saja · rumus dan tabel $\log_2$ dicetak pada lembar soal | [Kisi-kisi UAS](kisi-kisi-uas.md) §1, §5 |
| Cakupan | Seluruh semester, penekanan Minggu 9–14 dan `DAIML-Sub-CPMK082-1` | Kisi-kisi §2 |
| Komposisi | A. Konsep 25% (5 soal) · B. Perancangan solusi 45% (2 soal, bentuk §4) · C. Perhitungan 30% (3 soal) | Kisi-kisi §3–§4 |
| Bobot nilai akhir | 15% (Tes Tulis UAS; registri: seluruhnya `DAIML-Sub-CPMK082-1`) | [RPS §H.1](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md#h1-bobot-per-teknik-dan-sub-cpmk); registri 15d |
| Penandaan | Per butir menurut isinya (§1) | KENDALI-EKSEKUSI D-03 |
| Perkiraan waktu | Membaca petunjuk dan lembar rumus ±5 menit · membaca soal + menjawab ±85,8–107,5 menit · memeriksa ≥ 5 menit (§4); belum diuji coba — aturan uji coba berwaktu §4.2 | — |
| Berkas | [Latihan UAS](latihan-uas.md) · [pembahasan dan pedoman skor](latihan-uas-pembahasan.md) · pola: [cetak biru Latihan UTS](latihan-uts-cetak-biru.md) | — |
| Butir kendali | T1-10 (varian naskah UAS + kunci) · T0-15 (aturan telaah sejawat dan uji coba berwaktu, dipakai juga untuk UAS) · T1-16 (lembar skor per butir) · T1-19 (ketercapaian) | [KENDALI-EKSEKUSI](../../../00-meta/KENDALI-EKSEKUSI.md) |
| Penyusun | Tri Aji Nugroho, S.T., M.T. | — |

**Indikator registri** (registri 15d, diterjemahkan pada [RPS §E](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md#e-sub-cpmk)):

| Kode | Indikator |
|------|-----------|
| `082-1/1` | Memformulasikan *task* dan memilih model AI/ML |
| `082-1/2` | Membangun *pipeline* serta melatih model yang dapat direproduksi |
| `102-1/1` | Menyiapkan dan membagi data tanpa kebocoran |
| `102-1/2` | Menganalisis metrik serta memvisualisasikan hasil model secara tepat |

`082-1` = `DAIML-Sub-CPMK082-1` (C4–C6/P4–P5) · `102-1` = `DAIML-Sub-CPMK102-1` (C3–C4/P2–P3).

---

## 1. Prinsip Penandaan

**Penandaan Sub-CPMK per butir menurut isi adalah bawaan sementara D-03(a); bobot Tes Tulis UAS (15%) tetap tercatat pada `DAIML-Sub-CPMK082-1` sesuai alokasi registri dan RPS.**

1. **Sub-CPMK ditetapkan menurut isi butir**, dengan Materi registri 15d sebagai pembeda: formulasi masalah, pemilihan model, pelatihan dan generalisasi (*ensemble*, SVM/Naive Bayes, *clustering*, jaringan saraf), perancangan protokol evaluasi, serta penilaian dampak penerapan → `082-1`; kebocoran dan pembagian data, metrik klasifikasi/regresi/*clustering*, dan visualisasi diagnostik (kurva pembelajaran, PCA, t-SNE) → `102-1`. Akibatnya A4 dan A5 (Minggu 12) ditandai `102-1` sesuai ICM-11. Butir metrik B1(c) (ICM-07), B2(c) (ICM-06), dan metrik *clustering* C3(a)–(c) (ICM-10) ditandai `102-1`, berbeda dari peta ICM-06/07/10 → `082-1` pada [RPS §F](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md#f-indikator-capaian-mingguan); ICM tetap dicantumkan untuk penelusuran. Risiko etis B(f) ditandai `082-1` (dampak sosial; ICM-13; Tujuan Pembelajaran Bab 13), walaupun Materi `102-1` memuat "pengantar *bias*/*fairness*". Protokol B(e) (ICM-04/09) ditandai `082-1` (perancangan protokol evaluasi, C6), walaupun unsur pembagiannya (1,5 poin per soal) adalah materi ICM-04 → `102-1` pada RPS §F.
2. **Level Bloom dijaga dalam rentang Sub-CPMK-nya**: `082-1` pada C4–C6 (T1-10: "≥ C4 untuk 082-1"), `102-1` pada C3–C4. Karena itu **baris hitung prosedural C3** — C1(a)–(c) dan C2(a)–(d), yang materinya (pohon keputusan, jaringan saraf) adalah materi `082-1` — ditandai `102-1` menurut rumusan `102-1` dan CPMK102 "mengolah (C3) … data menggunakan metode statistik, komputasi"; tidak ada indikator registri khusus untuk baris ini (ᵃ pada §2). Baris analisis atas hasil hitungan yang sama — C1(d), C2(e), C3(d) — ditandai `082-1`. Tujuan Pembelajaran Bab 8 dan Bab 12 menandai "menghitung" (C3) sebagai `082-1`, dan Tujuan Pembelajaran Bab 10 menandai penerapan *clustering*, penilaian hasilnya dengan metrik, dan penafsirannya sebagai `082-1` — padahal C3(a)–(c) (7 poin) ditandai `102-1` di sini; perbedaan itu menunggu keputusan dosen (Catatan untuk Dosen no. 1).
3. **Kata kerja perintah mengikuti level yang dicetak** (registri `16-taksonomi-bloom-cap.md`): C3 "hitung"; C4 memuat sekurang-kurangnya satu kata kerja C4 ("analisislah", "bandingkan"), bukan hanya "tentukan"; C5 "pilih … beri argumentasi" dan "nilailah"; C6 "rumuskan" dan "rancang". Tidak ada butir C1–C2 dan tidak ada perintah "sebutkan".
4. **Soal campuran ditandai per sub-soal.** Satu baris lembar skor = satu soal Bagian A (bagian berlabel di dalamnya, mis. A1 (i)/(ii), tidak dipisah) atau satu sub-soal Bagian B/C; setiap baris bertanda satu Sub-CPMK (30 baris).
5. **Latihan dan naskah varian mencetak Bloom dan skor saja** (TD-49). Kisi-kisi UAS, RPS Minggu 16, dan modul Minggu 16 menyatakan bahwa UAS mengukur `DAIML-Sub-CPMK082-1`, dan registri membebankan seluruh bobot UAS ke `082-1`. Tanda per butir dicantumkan pada pembahasan dan cetak biru dengan catatan itu, dan dipakai untuk menghitung ketercapaian (§5) — bukan untuk memindahkan bobot nilai akhir.

---

## 2. Tabel Cetak Biru per Butir

| No | Mg | Indikator butir (yang diukur) | Ind. registri | ICM | Sub-CPMK | Bloom | Skor | Jawab (menit) |
|----|----|-------------------------------|---------------|-----|----------|-------|------|---------------|
| A1 | 9 | Menganalisis dua rencana *ensemble* terhadap diagnosis *underfit*/*overfit*: rata-rata mengurangi varians, bukan bias; pohon berkorelasi (`max_features=None`, fitur dominan) | 082-1/1 | ICM-08 | `082-1` | C4 | 5 | 3,5–4,25 |
| A2 | 10 | Menganalisis perbandingan berpasangan dengan dua syarat aturan praktis (satu terpenuhi, satu tidak) dan model kompleks ≈ Naive Bayes (sumber keterbatasan kinerja); menentukan tindak lanjut | 082-1/1 | ICM-09 | `082-1` | C4 | 5 | 3,75–4,5 |
| A3 | 11 | Menganalisis sekurang-kurangnya dua karakteristik data (bentuk, ukuran, k ditetapkan, pencilan) untuk memilih metode *clustering* | 082-1/1 | ICM-10 | `082-1` | C4 | 5 | 3,25–4 |
| A4 | 12 | Menganalisis dua kurva pembelajaran untuk mendiagnosis kondisi model dengan bukti angka dan memutuskan pembelian data | 102-1/2 | ICM-11 | `102-1` | C4 | 5 | 3–3,75 |
| A5 | 12 | Menganalisis PCA pada model yang wajib menjelaskan keputusan dan dua kekeliruan t-SNE; menentukan perbaikannya | 102-1/2 | ICM-11 | `102-1` | C4 | 5 | 3,25–4 |
| B1a | 2 | Merumuskan target klasifikasi (peristiwa, batas pengamatan), jenis *task*, dan saat prediksi dari alur keputusan | 082-1/1 | ICM-02 | `082-1` | C6 | 2,5 | 2,25–2,75 |
| B1b | 4 | Menganalisis kolom tersedia untuk menemukan dua kolom yang menimbulkan kebocoran temporal/target (kriteria kebocoran dicetak; satu pengecoh masa lalu yang sah) | 102-1/1 | ICM-04 | `102-1` | C4 | 2,5 | 1,5–2 |
| B1c | 7 | Membandingkan dampak FN/FP berbiaya tidak setara; menentukan metrik klasifikasi yang sesuai | 102-1/2 | ICM-07 | `102-1` | C4 | 2,5 | 2,5–3 |
| B1d | 7, 9 | Memilih tiga model kandidat untuk data tabular besar dengan argumentasi dari sifat data dan kebutuhan | 082-1/1 | ICM-07/08 | `082-1` | C5 | 4,5 | 2,75–3,5 |
| B1e | 4, 10 | Merancang protokol: pembagian temporal beserta alasannya, validasi dan penyetelan di data latih, perbandingan berpasangan, *baseline* aturan yang paling bermakna | 082-1/1 | ICM-04/09 | `082-1` | C6 | 5,5 | 3,25–4 |
| B1f | 14 | Menilai dua risiko etis yang konkret (mis. proksi wilayah, label selektif) dan menetapkan penanganannya | 082-1/1 | ICM-13 | `082-1` | C5 | 5 | 3,5–4,5 |
| B2a | 2 | Merumuskan target regresi (besaran, cara ukur) dan saat prediksi dalam minggu sejak tanam | 082-1/1 | ICM-02 | `082-1` | C6 | 2,5 | 1,5–2 |
| B2b | 4 | Menganalisis kolom tersedia: dua kebocoran (target dan kolom mingguan yang belum tersedia; kriteria kebocoran dicetak) | 102-1/1 | ICM-04 | `102-1` | C4 | 2,5 | 1,5–2 |
| B2c | 6 | Membandingkan dampak galat terlalu tinggi/terlalu rendah pada dua pemakaian; menentukan metrik regresi beserta ukuran pelengkap yang memperlihatkan perbedaan dampak (berarah, atau galat dalam ton) | 102-1/2 | ICM-06 | `102-1` | C4 | 2,5 | 2,75–3,5 |
| B2d | 6, 9, 12 | Memilih tiga kandidat untuk data tabular dengan blok fitur berkorelasi (mis. regularisasi, *ensemble*, PCA) | 082-1/1 | ICM-06/08/11 | `082-1` | C5 | 4,5 | 2,5–3,25 |
| B2e | 4, 10 | Merancang protokol per musim beserta alasannya, validasi dan penyetelan, perbandingan berpasangan, *baseline* persistensi yang paling bermakna | 082-1/1 | ICM-04/09 | `082-1` | C6 | 5,5 | 3–3,75 |
| B2f | 14 | Menilai dua risiko etis yang konkret (mis. bias pengukuran/representasi, satu perkiraan per desa untuk petani yang berbeda sifat) dan penanganannya | 082-1/1 | ICM-13 | `082-1` | C5 | 5 | 3–3,75 |
| C1a | 9 | Menghitung *entropy* dan *Gini* simpul akar | —ᵃ | ICM-08 | `102-1` | C3 | 2 | 1,5–2 |
| C1b | 9 | Menghitung *entropy* cabang dan IG kandidat P | —ᵃ | ICM-08 | `102-1` | C3 | 3 | 2–2,5 |
| C1c | 9 | Menghitung IG kandidat R (satu cabang murni) | —ᵃ | ICM-08 | `102-1` | C3 | 2 | 1,5–2 |
| C1d | 9 | Menganalisis percabangan pengenal berdaun kecil yang IG-nya tertinggi; pilihan dengan `min_samples_leaf` beserta alasannya | 082-1/1 | ICM-08 | `082-1` | C4 | 3 | 2,25–2,75 |
| C2a | 13 | Menghitung langkah maju lapis tersembunyi | —ᵃ | ICM-12 | `102-1` | C3 | 2 | 2–2,5 |
| C2b | 13 | Menghitung keluaran dan *loss* | —ᵃ | ICM-12 | `102-1` | C3 | 1,5 | 1,5–1,75 |
| C2c | 13 | Menghitung $\delta_{\text{out}}$, gradien, dan pembaruan bobot keluaran | —ᵃ | ICM-12 | `102-1` | C3 | 3 | 2,5–3 |
| C2d | 13 | Menghitung $\delta$ lapis tersembunyi dan pembaruan $w_{22}$ | —ᵃ | ICM-12 | `102-1` | C3 | 1,5 | 1,25–1,5 |
| C2e | 13 | Menganalisis arah perubahan bobot lewat aturan rantai (tanda $v_2$) | 082-1/2 | ICM-12 | `082-1` | C4 | 2 | 2,25–3 |
| C3a | 11 | Menghitung $a(i)$, $b(i)$ (klaster terdekat dari dua), dan $s(i)$ untuk dua titik | 102-1/2 | ICM-10 | `102-1` | C3 | 4 | 3,5–4,5 |
| C3b | 11 | Menghitung rerata *silhouette* | 102-1/2 | ICM-10 | `102-1` | C3 | 1 | 1–1,25 |
| C3c | 11 | Menganalisis *silhouette* negatif dan tindakan atas titik perbatasan | 102-1/2 | ICM-10 | `102-1` | C4 | 2 | 1,75–2,25 |
| C3d | 11 | Membandingkan k = 2 dan k = 3 dari *silhouette* dan kebermaknaan; menyarankan k | 082-1/1 | ICM-10 | `082-1` | C4 | 3 | 2,25–2,75 |
| **Jumlah** | | **30 baris skor · 10 soal** | | | | | **100** | **72–90,25** |

ᵃ Baris hitung prosedural: diukur menurut rumusan `102-1` "mengolah (C3) data"; tidak ada indikator registri yang khusus (§1 butir 2).

**Jawab** = taksiran waktu mahasiswa semester 5 berpikir, menghitung dengan kalkulator, dan menulis jawaban dengan tangan, **di luar** waktu membaca soal: angka kiri optimistis (penulis cepat), angka kanan realistis — waktu menulis jawaban minimal bernilai penuh pada ±20 kata/menit ditambah waktu berpikir dan menghitung (audit tulis, §4.1–§4.2). Porsi minggu B1e dan B2e dihitung per unsur pedoman skor, sedangkan B1d dan B2d menurut kandidat contoh *Baik* (perkiraan; §3.5).

---

## 3. Ringkasan

### 3.1 Per Sub-CPMK

| Sub-CPMK | Butir (baris skor) | Skor maks | % UAS | Setara nilai akhir (× 15%) |
|----------|--------------------|-----------|-------|----------------------------|
| `DAIML-Sub-CPMK082-1` | A1, A2, A3, B1a, B1d–f, B2a, B2d–f, C1d, C2e, C3d | 58 | **58%** | 8,7 |
| `DAIML-Sub-CPMK102-1` | A4, A5, B1b, B1c, B2b, B2c, C1a–c, C2a–d, C3a–c | 42 | **42%** | 6,3 |
| **Jumlah** | 30 baris | **100** | **100%** | **15,0** |

Bila baris hitung C1(a)–(c) dan C2(a)–(d) ditandai menurut materi asalnya (`082-1`), pembagiannya menjadi 73/27 — tetapi 15 poin C3 berada di bawah rentang Bloom `082-1`; bila C3(a)–(c) juga ditandai menurut Tujuan Pembelajaran Bab 10, 80/20 (20 poin C3 di bawah rentang) (Catatan untuk Dosen no. 1).

### 3.2 Per indikator registri

| Indikator | Skor | % |
|-----------|------|---|
| `082-1/1` Memformulasikan *task* dan memilih model | 56 | 56% |
| `082-1/2` Membangun *pipeline* dan melatih model yang dapat direproduksi | 2 | 2% — C2(e); indikator ini terutama diukur oleh Observasi (lab) dan Unjuk Kerja (proyek) |
| `102-1/1` Menyiapkan dan membagi data tanpa kebocoran | 5 | 5% |
| `102-1/2` Menganalisis metrik dan memvisualisasikan hasil | 22 | 22% |
| Hitung prosedural `102-1` tanpa indikator khusus (ᵃ) | 15 | 15% |

### 3.3 Per level Bloom

| Bloom | Skor | % | Rincian Sub-CPMK |
|-------|------|---|------------------|
| C1–C2 | 0 | 0% | — |
| C3 | 20 | 20% | `102-1` 20 |
| C4 | 45 | 45% | `082-1` 23 · `102-1` 22 |
| C5 | 19 | 19% | `082-1` 19 |
| C6 | 16 | 16% | `082-1` 16 |
| **≥ C3** | **100** | **100%** | Seluruh butir; 80% ≥ C4; seluruh butir `082-1` ≥ C4 |

### 3.4 Per bagian

| Bagian | Skor (kisi-kisi) | `082-1` | `102-1` | Membaca soal (menit) | Menjawab (menit) | Disarankan pada latihan |
|--------|------------------|---------|---------|----------------------|------------------|-------------------------|
| A. Konsep | 25 (25%) | 15 | 10 | 4,6–5,7 | 16,75–20,5 | ±26 menit |
| B. Perancangan solusi | 45 (45%) | 35 | 10 | 4,9–6,2 | 30–38 | ±44 menit |
| C. Perhitungan | 30 (30%) | 8 | 22 | 4,3–5,3 | 25,25–31,75 | ±37 menit |
| **Jumlah** | **100** | **58** | **42** | **13,8–17,2** | **72–90,25** | **±107 menit** |

Waktu membaca per bagian termasuk kepala bagian; jumlahnya dihitung dari total kata (selisih pembulatan ±0,1).

### 3.5 Per minggu — terhadap porsi perkiraan kisi-kisi §2

| Minggu | Topik | Porsi kisi-kisi | Aktual | Selisih | Sumber |
|--------|-------|-----------------|--------|---------|--------|
| 1–7 | Materi UTS sebagai dasar perancangan | 15 | 21 | +6 | B(a) Mg 2: 5 · B(b) dan pembagian B(e) Mg 4: 8 · B2(c) dan Ridge pada B2(d) Mg 6: 4 · B1(c) dan regresi logistik pada B1(d) Mg 7: 4 |
| 9 | Pohon keputusan; *ensemble* | 18 | 19,5 | +1,5 | A1 5 · C1 10 · B1(d) *gradient boosting* dan *Random Forest* 3 · B2(d) *gradient boosting* 1,5 |
| 10 | SVM; Naive Bayes; pemilihan model | 17 | 13 | −4 | A2 5 · B(e) validasi, perbandingan, *baseline* 8 |
| 11 | *Clustering*; deteksi anomali | 15 | 15 | 0 | A3 5 · C3 10 |
| 12 | PCA; kurva diagnostik | 12 | 11,5 | −0,5 | A4 5 · A5 5 · B2(d) PCA 1,5 |
| 13 | Jaringan saraf tiruan | 13 | 10 | −3 | C2 10 |
| 14 | AI generatif; *bias*; *fairness*; tanggung jawab | 10 | 10 | 0 | B1(f) 5 · B2(f) 5 |
| **Jumlah** | | **100** | **100** | | |

Porsi B(d) per minggu adalah **perkiraan**: ditetapkan menurut tiga kandidat contoh *Baik* (1,5 poin per kandidat), padahal Bagian B menerima kandidat lain yang beralasan — mis. Naive Bayes (Minggu 10) atau jaringan saraf (Minggu 13) menggeser porsi itu. Selisih terbesar: Minggu 1–7 +6 dan Minggu 10 −4. Kelebihan Minggu 1–7 berasal dari bentuk Bagian B yang ditetapkan kisi-kisi §4 — formulasi, kolom terlarang, metrik, dan strategi pembagian adalah materi Minggu 2–7 — dan dari model klasik (regresi logistik, Ridge) yang tepat untuk kedua kasus. Minggu 10 terisi lewat A2 dan protokol B(e); Minggu 13 hanya lewat C2, karena usulan jaringan saraf pada B2 adalah pengecoh yang tidak dinilai tersendiri. Deteksi anomali (Minggu 11) dan AI generatif (Minggu 14) tidak diuji tersendiri, sama seperti contoh soal kisi-kisi §6; porsi kedua minggu itu terisi oleh *clustering* serta *bias*, *fairness*, dan tanggung jawab (Catatan untuk Dosen no. 5).

---

## 4. Model Waktu

### 4.1 Cara menaksir

Waktu ujian 120 menit = **±5 menit** membaca petunjuk dan lembar rumus di awal + **waktu kerja** (membaca soal + menjawab) + **≥ 5 menit** memeriksa. Syaratnya: taksiran kerja realistis **≤ 110 menit**.

- **Membaca soal:** jumlah kata soal (judul, stem, tabel, dan sub-soal; tanpa petunjuk dan lembar rumus; angka pada tabel ikut dihitung) dibagi laju baca. 150 kata/menit = optimistis; **120 kata/menit** = laju baca cermat untuk teks padat tabel dan angka (dipakai untuk batas atas).
- **Menjawab:** taksiran per baris skor pada §2. Batas kanan (realistis) disusun dengan **audit tulis**: untuk setiap baris ditulis jawaban minimal bernilai penuh menurut pedoman skor — contoh *Baik* literal pada pembahasan untuk setiap soal A dan B serta setiap sub-soal analisis C, dan langkah minimal untuk sub-soal hitung — lalu katanya dihitung (angka dan simbol pada perhitungan ikut dihitung). Pada laju tulis tangan **±20 kata/menit**, sisa anggaran menjadi waktu berpikir dan menghitung. Syaratnya: setiap baris analisis (C4–C6) menyisakan **≥ 0,5 menit** berpikir, dan baris hitung memuat waktu kalkulator. Batas kiri (optimistis) = penulis cepat (±25 kata/menit) dengan waktu berpikir lebih singkat.
- Petunjuk, kepala naskah, pernyataan amanah, dan lembar rumus (±575 kata, termasuk 36 angka tabel $\log_2$, dan lima baris rumus) terbaca dalam ±4,5–4,8 menit pada 120 kata/menit, sehingga pas dalam jatah 5 menit bila tabel $\log_2$ hanya dipindai; kelebihan kecil diambil dari waktu memeriksa (±7,5 menit pada taksiran realistis). Pernyataan amanah hanya dibaca, tidak disalin.

### 4.2 Hasil per soal

| Soal | Kata soal | Baca (150–120 kpm) | Jawab | Kerja | Jawaban minimal (kata) | Menulis pada 20 kpm | Sisa berpikir/hitung (batas kanan) |
|------|-----------|--------------------|-------|-------|------------------------|---------------------|------------------------------------|
| A1 | 153 | 1,0–1,3 | 3,5–4,25 | 4,5–5,5 | 62 | 3,1 | 1,2 |
| A2 | 193 | 1,3–1,6 | 3,75–4,5 | 5,0–6,1 | 66 | 3,3 | 1,2 |
| A3 | 118 | 0,8–1,0 | 3,25–4 | 4,0–5,0 | 57 | 2,9 | 1,2 |
| A4 | 102 | 0,7–0,9 | 3–3,75 | 3,7–4,6 | 54 | 2,7 | 1,1 |
| A5 | 113 | 0,8–0,9 | 3,25–4 | 4,0–4,9 | 57 | 2,9 | 1,2 |
| B1 | 344 | 2,3–2,9 | 15,75–19,75 | 18,0–22,6 | 229 | 11,5 | 8,3 |
| B2 | 369 | 2,5–3,1 | 14,25–18,25 | 16,7–21,3 | 209 | 10,5 | 7,8 |
| C1 | 172 | 1,1–1,4 | 7,25–9,25 | 8,4–10,7 | 122 | 6,1 | 3,2 |
| C2 | 198 | 1,3–1,7 | 9,5–11,75 | 10,8–13,4 | 153 | 7,7 | 4,1 |
| C3 | 262 | 1,7–2,2 | 8,5–10,75 | 10,2–12,9 | 152 | 7,6 | 3,2 |
| **Jumlah** (termasuk kepala bagian, 41 kata) | **2.065** | **13,8–17,2** | **72–90,25** | **85,8–107,5** | **1.161** | **58,1** | **32,2** |

Per baris B, sisa berpikir pada batas kanan (kata contoh *Baik* per butir, termasuk label butir): B1 (a) 1,2 · (b) 0,8 · (c) 1,3 · (d) 1,75 · (e) 1,65 · (f) 1,6 (jumlah 8,3); B2 (a) 1,05 · (b) 1,1 · (c) 1,2 · (d) 1,45 · (e) 1,5 · (f) 1,5 menit (jumlah 7,8). Baris analisis C: C1(d) 0,7 · C2(e) 0,7 · C3(c) 0,65 · C3(d) 0,9 menit.

**Kesimpulan:** 5 + ±85,8–107,5 + ≥ 5 ≤ 120 menit. Pada taksiran realistis sisa memeriksa ±7,5 menit. Jawaban minimal bernilai penuh (±1.161 kata) memerlukan ±58,1 menit menulis; sisanya ±32,2 menit untuk berpikir dan menghitung — paling sedikit ±0,65 menit pada setiap baris analisis. Batas itu hanya berlaku bila jawaban seringkas contoh *Baik*; karena itu petunjuk Bagian B meminta poin ringkas, bukan esai, dan pembahasan menyatakan bahwa nilai penuh hanya menuntut unsur yang dinilai. Taksiran ini **belum diuji coba**; penentunya uji coba berwaktu berikut.

**Uji coba berwaktu.** Latihan ini diuji coba **sebelum varian disusun**, dan varian diuji coba lagi sebelum difinalkan (T0-15, §6.4 butir 3), dengan aturan yang sama: 2–3 penguji coba (asisten atau mahasiswa senior) yang **belum membaca latihan ini maupun varian** mengerjakannya dalam kondisi "120 menit, *closed book*, tulisan tangan, alat bantu sesuai kisi-kisi (kalkulator saja), tanpa AI", dan mencatat menit per bagian; yang disimpan hanya angka agregat (median dan rentang). Penguji coba yang sudah mengenal soalnya bekerja lebih cepat dan membuat taksiran waktu terlalu rendah. Penguji coba yang menguasai materi bekerja ±1,5× lebih cepat daripada rerata mahasiswa, sehingga batasnya 2/3 dan 3/4 durasi; satu menit penguji coba di atas 80 menit setara ±1,5 menit kerja mahasiswa yang harus dipangkas:

| Median waktu penguji coba | Keputusan |
|---------------------------|-----------|
| ≤ 80 menit (≤ 2/3 durasi) | Lolos |
| > 80 dan ≤ 90 menit (≤ 3/4 durasi) | Lolos bersyarat: terapkan cadangan pemangkasan pertama (§4.3). Cadangan pertama hanya cukup untuk median sampai **±81 menit**; di atasnya dosen juga menetapkan pemangkasan lanjutan (§4.3), lalu uji ulang |
| > 90 menit (> 3/4 durasi) | Dosen menetapkan pemangkasan lanjutan (§4.3), lalu uji ulang |

Pemangkasan diterapkan pada latihan, pembahasan, dan cetak biru sekaligus, lalu pada varian, sehingga cetak biru keduanya tetap sama.

Data pelengkap (bila dosen memintanya): catatan menit per bagian dari mahasiswa yang mengerjakan latihan ini — termasuk waktu tambahan yang dicatat terpisah bila 120 menit tidak cukup (latihan, "Cara memakai latihan ini") — diserahkan tanpa nama; yang dipakai dan dicatat hanya rekap agregat (median dan rentang per bagian). Angka itu hanya data pelengkap; keputusan pemangkasan mengikuti median penguji coba pada tabel di atas.

### 4.3 Cadangan pemangkasan

Dipakai menurut hasil uji coba berwaktu (§4.2). Cadangan pertama perlu disetujui dosen **sebelum** uji coba, lalu diterapkan langsung bila median 80–81 menit. Setiap cadangan menjaga komposisi 5/2/3 soal dan 25/45/30 poin serta Sub-CPMK, level Bloom, dan skor setiap baris; poin hanya dipindahkan di dalam baris yang sama. Angka hemat adalah taksiran model §4 (waktu menjawab; kata soal hampir tidak berubah).

| Cadangan | Pemangkasan | Pembagian poin baru | Hemat (± menit) |
|----------|-------------|---------------------|-----------------|
| **Pertama** (lolos bersyarat; cukup sampai median ±81 menit) | A2(i): baris $d_i$ dicetak pada tabel · C3(a): rerata jarak D2 ke klaster B (6,35) dan C (5,5) dicetak; mahasiswa memilih $b(\text{D2})$ dan menghitung $s(\text{D2})$, sedangkan D5 tetap dihitung penuh | A2: tetap · C3(a): D2 — $a$ 0,5 · memilih klaster terdekat 1,0 · $s$ 0,5; D5 tetap | 1,25–1,5 |
| Lanjutan (keputusan dosen) | Pilihan yang mengurangi cakupan: A2 hanya situasi (i) · C3(a) hanya D5 ($s(\text{D2})$ dicetak) · B1 dan B2 masing-masing satu kolom pengecoh dihapus dari tabel kolom | Ditetapkan dosen bersama pemangkasannya | ±1 · ±1 · ±0,5 |

**Batas cakupan cadangan.** Rentang lolos bersyarat (median 80–90 menit) setara sampai ±15 menit kerja mahasiswa, sedangkan cadangan pertama menghemat ±1,25–1,5 menit kerja mahasiswa (±0,8–1 menit penguji coba). Jadi cadangan pertama **hanya cukup untuk median sampai ±81 menit**. Cadangan pertama dan ketiga pilihan lanjutan bersama-sama (±3,75–4 menit kerja mahasiswa) **hanya cukup sampai ±82,5 menit**. Karena itu:

- median > ±81 dan ≤ ±82,5 menit → cadangan pertama ditambah pilihan lanjutan yang ditetapkan dosen, lalu uji ulang;
- median > ±82,5 menit → dosen menetapkan pemangkasan yang lebih besar daripada seluruh pilihan di tabel (mis. mencetak $h_1$ dan $h_2$ pada C2(a), menghapus satu sub-soal, atau mengurangi butir lewat revisi kisi-kisi), diterapkan pada latihan, pembahasan, dan cetak biru sekaligus, lalu uji ulang.

Pilihan lanjutan sebaiknya ditetapkan dosen **sebelum** uji coba, agar hasil uji coba langsung dapat ditindaklanjuti.

---

## 5. Ketercapaian per Sub-CPMK dari Skor Butir

Lembar skor mencatat **30 baris** (satu baris = satu soal Bagian A atau satu sub-soal Bagian B/C, seperti pada §2). Untuk tiap Sub-CPMK $j$:

$$\text{Ketercapaian}_j = \frac{\sum_{\text{mahasiswa}} \sum_{i \in j} \text{skor}_i}{N \cdot \text{skor maks}_j} \times 100\% \qquad \text{skor maks}_{082\text{-}1}=58,\ \ \text{skor maks}_{102\text{-}1}=42$$

- Yang dicatat di repositori hanya **agregat**: rerata dan sebaran per baris butir dan per Sub-CPMK, serta proporsi mahasiswa ≥ ambang. Skor per mahasiswa tidak dimasukkan ke repositori.
- **Butir yang perlu dicermati setelah ujian** (bahan evaluasi PPEPP, T1-19): rerata < 50% skor maks; baris analisis C4 yang reratanya jauh di bawah baris hitung C3 pada soal yang sama (C1, C2, C3); butir Bagian B dengan banyak jawaban "Cukup" yang seragam (indikasi rumusan soal kurang jelas).
- Bobot nilai akhir UAS tetap 15% pada `082-1` sesuai registri, dan syarat lulus "capaian tiap Sub-CPMK ≥ 50% dari bobotnya" ([RPS §I](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md#i-konversi-nilai)) dihitung dengan alokasi itu. Pemakaian angka ketercapaian di atas untuk alokasi ulang bobot memerlukan keputusan D-03 dan persetujuan prodi.

---

## 6. Panduan Menyusun Varian (Naskah UAS Sebenarnya)

Naskah UAS sebenarnya adalah **varian** latihan ini: struktur, tuntutan berpikir, dan skornya sama; isi permukaannya baru. Mahasiswa yang berlatih dengan sungguh-sungguh mendapat manfaat dari **cara bernalar** yang sama, bukan dari jawaban yang dihafal. Bila dibutuhkan ujian susulan, susun **varian kedua** dengan prosedur yang sama; konteks, data, dan angkanya berbeda dari latihan maupun varian pertama.

### 6.1 Invarian per butir

Yang **tidak boleh berubah** pada setiap butir varian:

| Butir | Sub-CPMK · Bloom · skor | Konsep/keterampilan yang diuji | Jumlah unsur/langkah | Kesulitan | Format jawaban |
|-------|-------------------------|--------------------------------|----------------------|-----------|----------------|
| A1 | `082-1` · C4 · 5 | Dua rencana *ensemble*: satu untuk model *underfit* yang tidak tertolong rata-rata (bias), satu untuk model *overfit* yang tidak tertolong karena pohonnya berkorelasi | 2 bagian × (diagnosis + bukti, mekanisme, perubahan) | Sedang | Uraian singkat |
| A2 | `082-1` · C4 · 5 | Aturan berpasangan dua syarat: satu terpenuhi dan satu tidak, sedangkan rekan hanya memakai yang terpenuhi; model kompleks ≈ model sederhana di atas *baseline* → kemungkinan besar batas pada fitur (sumber keterbatasan diminta eksplisit pada batang soal) | 2 situasi × (pemeriksaan, kesimpulan, tindak lanjut); 5 lipatan | Sedang | Uraian singkat |
| A3 | `082-1` · C4 · 5 | Memilih metode *clustering* dari karakteristik data; dua kebutuhan dengan jawaban terbaik yang berbeda | 2 kebutuhan × (≥ 2 karakteristik — jumlah minimal dicetak pada batang soal —, metode, alasan) | Sedang | Uraian/tabel |
| A4 | `102-1` · C4 · 5 | Dua kurva pembelajaran (empat ukuran data): satu **kurang data** — selisih latih–validasi menyempit, validasi masih menanjak (data membantu; label "*overfit*" yang menyempit juga diterima) — dan satu datar (data tidak membantu); keputusan membeli data | 2 tim × (diagnosis + bukti, keputusan, tindakan) | Sedang | Uraian singkat |
| A5 | `102-1` · C4 · 5 | PCA pada model yang wajib menjelaskan keputusan; dua kekeliruan pemakaian t-SNE | 2 keputusan × (masalah, perbaikan) | Sedang | Uraian singkat |
| B1 | `082-1`/`102-1` · C6, C4, C4, C5, C6, C5 · 2,5 + 2,5 + 2,5 + 4,5 + 5,5 + 5 | Perancangan solusi **klasifikasi**: saat prediksi disimpulkan dari alur keputusan; dua kolom bocor (satu jelas sesudah kejadian, satu halus karena waktunya) dan sekurang-kurangnya satu pengecoh masa lalu yang sah; biaya FN/FP tidak setara; data tabular besar dengan entitas berulang; protokol temporal; dua risiko etis yang konkret. Batang (b) mencetak kriteria kebocoran; batang (e) meminta alasan pembagian dan *baseline* yang paling bermakna | 6 butir (a)–(f) kisi-kisi §4 | Sulit | Poin ringkas per butir |
| B2 | `082-1`/`102-1` · sama dengan B1 | Perancangan solusi **regresi** dengan dua pemakaian yang dirugikan oleh arah galat berbeda; kolom berindeks waktu yang sebagian belum tersedia; blok fitur berkorelasi (PCA/regularisasi relevan); usulan model "canggih" sebagai pengecoh yang tidak dinilai tersendiri; pembagian per periode. Batang (b) dan (e) seperti B1; batang (c) meminta ukuran pelengkap yang memperlihatkan perbedaan dampak | 6 butir (a)–(f) kisi-kisi §4 | Sulit | Poin ringkas per butir |
| C1 | `102-1` (a–c), `082-1` (d) · C3, C3, C3, C4 · 2 + 3 + 2 + 3 | Tiga kandidat percabangan biner; satu kandidat pengenal berdaun murni sangat kecil dengan IG tertinggi; IG satu kandidat diberikan; seluruh proporsi ada pada tabel $\log_2$; `min_samples_leaf` mengubah pilihan (batang (d) meminta alasannya, di antara ketiga kandidat) | *Entropy* + *Gini* akar; 2 IG; 1 analisis | Sedang | Hitung + uraian singkat |
| C2 | `102-1` (a–d), `082-1` (e) · C3, C3, C3, C3, C4 · 2 + 1,5 + 3 + 1,5 + 2 | Jaringan 2-2-1 sigmoid, bias 0, satu bobot keluaran negatif; satu langkah maju-mundur sampai satu bobot lapis tersembunyi (sub-soal $\delta_h$ mencetak "pakai bobot keluaran sebelum diperbarui"); arah perubahan dijelaskan lewat tanda bobot keluaran | 4 nilai maju; $L$; $\delta_{\text{out}}$, 2 gradien, 2 pembaruan; $\delta_h$, 1 gradien, 1 pembaruan; 1 analisis | Sedang | Hitung empat desimal + uraian singkat |
| C3 | `102-1` (a–c), `082-1` (d) · C3, C3, C4, C4 · 4 + 1 + 2 + 3 | *Silhouette* dari tabel jarak (6–8 titik, k = 3; dibulatkan satu desimal dan dinyatakan demikian) hasil K-Means; satu titik bernilai negatif; $b(i)$ menuntut memilih klaster terdekat dari dua; k = 2 vs k = 3 dengan batas kemampuan pemangku kepentingan (perintah meminta juga apa yang tidak diukur *silhouette*) | 2 titik × ($a$, $b$, $s$); 1 rerata; 2 analisis | Sedang | Hitung + uraian singkat |

Rumusan perintah juga invarian sepanjang menyangkut unsur yang dinilai: setiap unsur pedoman skor diminta batang soal — mis. diagnosis dengan bukti angka (A1, A4), sumber keterbatasan kinerja (A2(ii)), sekurang-kurangnya dua karakteristik (A3), kriteria kebocoran (B(b)), ukuran pelengkap (B2(c)), alasan pembagian, pemakaian data uji, dan *baseline* yang paling bermakna (B(e)), alasan pilihan dengan `min_samples_leaf` (C1(d)), bobot keluaran sebelum diperbarui (C2(d)), dan apa yang tidak diukur *silhouette* (C3(d)). Komposisi, durasi, alat bantu, lembar rumus (sama dengan kisi-kisi §5) beserta tabel $\log_2$, pernyataan amanah (rumusan sama dengan latihan; dicetak dan disetujui dengan menuliskan nama dan NIM, tidak disalin), dan model waktu §4 juga invarian.

### 6.2 Yang wajib diubah, dengan contoh arah variasi

Pada **setiap** butir wajib diubah: konteks/kasus, data dan angka, nama entitas (instansi, kota, kolom, dataset), serta **urutan unsur** — analog dengan mengacak letak kunci pilihan ganda (latihan ini tidak memakai pilihan ganda): urutan bagian (i)/(ii) pada A1–A5, letak kolom bocor dan pengecoh pada tabel B1(b) dan B2(b), urutan kandidat P/Q/R pada C1, serta letak titik bernilai negatif pada C3. Lembar soal mencetak skor per soal A (dengan pembagian rata per bagian, mis. "2,5 poin per tim") dan per sub-soal B/C; rincian poin per unsur hanya ada pada kunci.

Tabel berikut **hanya menunjukkan arah variasi**. Dokumen ini publik, sehingga naskah varian **tidak boleh** memakai konteks, nama kolom, atau angka yang tercantum di sini; rancang konteks setara yang tidak tercantum (§6.3 butir 6).

| Butir | Contoh arah variasi (arah saja — konteks, nama, dan angkanya tidak dipakai pada varian) |
|-------|------------------------------------------------------------------|
| A1 | Konteks lain, mis. prediksi keterlambatan pembayaran iuran, kerusakan pompa irigasi, atau penolakan klaim garansi. Bagian *underfit* dapat memakai *bagging* model yang sama terbatasnya; bagian *overfit* dapat memakai `max_features` yang hampir sama dengan jumlah fitur, atau beberapa fitur dominan yang saling berkorelasi |
| A2 | Syarat yang terpenuhi dapat dibalik, mis. arah sama pada 5 dari 5 lipatan tetapi $\lvert\bar d\rvert \le 2\cdot SE$; atau $\lvert\bar d\rvert > 2\cdot SE$ dengan arah 3 dari 5. Model sederhana pembanding, mis. regresi logistik atau Naive Bayes; metrik, mis. F1, ROC-AUC, atau PR-AUC |
| A3 | Pasangan kebutuhan lain dengan jawaban terbaik berbeda, mis. puluhan unit wilayah dengan kebutuhan melihat struktur bertingkat (*hierarchical*), sebaran titik dengan kerapatan dan pencilan (DBSCAN), atau jutaan baris dengan k ditetapkan (K-Means) |
| A4 | Ukuran data dan metrik lain (mis. RMSE untuk regresi, dengan arah "lebih rendah lebih baik"); tim yang tidak perlu membeli data dapat *underfit* atau sudah pas dan mendatar |
| A5 | Keputusan yang wajib dijelaskan, mis. penerimaan pinjaman modal, penetapan tarif, atau seleksi beasiswa; kekeliruan t-SNE lain, mis. ukuran klaster dibaca sebagai jumlah anggota, atau klaster yang muncul pada satu nilai `perplexity` dianggap pasti |
| B1 | Klasifikasi dengan keputusan sebelum langkah operasional berbiaya, mis. memverifikasi pendaftar layanan, memeriksa ulang klaim, atau menjadwalkan kunjungan petugas; hindari domain pengiriman paket (dekat dengan Bab 2 §2.6 dan latihan ini); *base rate* 5–15%; ratusan ribu baris dengan entitas berulang; kolom bocor halus yang tercatat pada tahap proses sesudah saat prediksi |
| B2 | Regresi dengan dua pemakaian, mis. perkiraan kebutuhan air baku, jumlah pengunjung, atau volume panen komoditas lain; kolom berindeks waktu (mingguan/bulanan) yang sebagian belum tersedia saat keputusan; pembagian per musim, per tahun, atau per gelombang |
| C1 | Konteks dan angka lain dengan proporsi pada tabel $\log_2$ (mis. 1/3, 0,1, 0,3, 0,4); pengenal lain, mis. nomor tiket atau kode transaksi; ambang `min_samples_leaf` lain yang tetap menyingkirkan kandidat pengenal |
| C2 | Masukan, target (boleh $y = 0$, sehingga arah perubahan berbalik), $\eta$, dan letak bobot negatif lain (mis. $v_1$); bobot lapis tersembunyi yang ditanyakan berbeda (mis. $w_{11}$ atau $w_{21}$); semua nilai tetap dapat dihitung dengan kalkulator |
| C3 | Jumlah titik 6–8, konteks lain (mis. posyandu, sentra UMKM, atau sekolah); tabel jarak dibulatkan satu desimal dari koordinat terskala, dan pembulatan itu dinyatakan pada soal; kendala pemangku kepentingan lain (mis. hanya tiga tim pendamping) |

### 6.3 Larangan

1. **Menyalin** kalimat, kasus, nama, atau angka latihan, termasuk contoh pada §6.2 (butir 6) — juga parafrasa dekat dan angka yang hanya digeser sedikit. Varian juga tidak boleh mengulang Latihan Soal Bab 8–14 buku ajar, contoh soal kisi-kisi UAS §6, maupun soal Latihan UTS (§7), dan tidak memakai domain studi kasus badan bab yang dekat dengan butirnya (mis. pengiriman paket, Bab 2 §2.6, untuk B1).
2. **Mengubah** level Bloom, skor, Sub-CPMK, jumlah sub-soal, atau format jawaban suatu butir; mengubah komposisi 5/2/3 soal dan 25/45/30 poin, atau keenam butir (a)–(f) Bagian B.
3. **Menambah materi di luar kisi-kisi** atau di luar yang diajarkan pada Bab 1–13, modul, dan lab — mis. arsitektur CNN/RNN, SVR, atau *loss* yang tidak diajarkan — atau menguji hafalan nama fungsi dan nilai bawaan parameter (modul Minggu 16 §16.7).
4. **Menambahkan kembali** unsur yang dipangkas pada §4.3, atau memperpanjang stem sehingga taksiran kerja model §4 melampaui 110 menit.
5. Menyajikan data sebagai data resmi suatu lembaga; seluruh angka tetap ilustrasi (rekaan) dan dinyatakan demikian pada petunjuk.
6. **Memakai contoh arah variasi §6.2 apa adanya** (konteks, nama, nama kolom, atau angka). Dokumen ini publik; contoh itu hanya menunjukkan arah, sehingga varian memakai konteks lain yang setara dan tidak tercantum pada dokumen ini, latihan, kisi-kisi, maupun buku ajar.
7. **Mencetak rincian poin per unsur** di dalam soal A (mis. "1 poin untuk diagnosis") atau poin per kolom pada B(b): rincian itu menunjukkan bentuk jawaban yang diharapkan.

### 6.4 Prosedur mutu varian

1. **Selesaikan ulang setiap butir dengan Python** (Colab): seluruh angka Bagian C, A2, dan A4 — nilai akhir maupun nilai antara berpembulatan per langkah — konsistensi tabel jarak C3 dengan koordinatnya dan hasil K-Means, serta angka pendukung B (mis. *base rate*, minggu keputusan). Simpan skrip bersama kunci varian.
2. **Pastikan satu kunci yang benar** untuk setiap butir hitung dan setiap keputusan tertutup (kolom bocor B(b), kandidat terpilih C1(d), arah bobot C2(e)); untuk butir analisis dan Bagian B, tulis daftar alternatif yang diterima seperti pada pembahasan latihan.
3. **Periksa waktu**: hitung kata varian dan ulangi model §4 termasuk audit tulis — jawaban minimal bernilai penuh per baris, setiap baris analisis menyisakan ≥ 0,5 menit berpikir, kerja ≤ 110 menit; lakukan **uji coba berwaktu** varian menurut aturan §4.2 — 2–3 penguji coba (asisten atau mahasiswa senior) yang belum membaca latihan maupun varian, kondisi "120 menit, *closed book*, tulisan tangan, kalkulator saja, tanpa AI"; median ≤ 80 menit lolos, > 80–90 menit terapkan cadangan pertama §4.3 (cukup hanya sampai median ±81 menit; di atasnya dosen juga menetapkan pemangkasan lanjutan), > 90 menit dosen menetapkan pemangkasan lanjutan lalu uji ulang. Uji coba ini **wajib** sebelum varian difinalkan (T0-15). Bandingkan dengan hasil uji coba latihan ini.
4. **Telaah sejawat** memakai [checklist-verifikasi](../../../00-pedoman-obe/checklist-verifikasi.md#c-lembar-telaah-sejawat) §C, termasuk pemeriksaan orisinalitas terhadap latihan ini.
5. **Simpan varian dan kuncinya di penyimpanan privat** (bukan di repositori). Setelah ujian, yang masuk repositori hanya angka agregat per butir dan per Sub-CPMK (§5).
6. **Varian kedua untuk ujian susulan** disusun dengan langkah 1–5 yang sama; konteks, data, dan angkanya berbeda dari latihan maupun varian pertama.

---

## 7. Pemeriksaan Orisinalitas

Sumber yang dibandingkan (terlarang dipakai ulang atau diparafrasa dekat): Latihan Soal Bab 8–14 buku ajar (tingkat Dasar, Menengah, Mahir), contoh soal kisi-kisi UAS §6 (A1–A5, B1–B2, C1–C3), dan soal [Latihan UTS](latihan-uts.md). Sebagai pembanding tambahan: contoh terhitung di badan bab (Bab 8 §8.1.3, Bab 12 §12.4.2) dan studi kasus Bab 2 §2.6.

| Butir | Sumber terdekat | Pembeda |
|-------|-----------------|---------|
| A1 | Kisi-kisi A1 (mengapa *ensemble* unggul; bias–varians); Latihan Bab 8 no. 3 dan 6(d) | Diagnosis dua rencana dengan angka; *ensemble* pohon dangkal tidak mengatasi *underfit*; `max_features=None` dengan fitur dominan. **Irisan konsep yang disengaja:** dekorelasi pohon (Latihan Bab 8 no. 3) diuji lewat kasus, bukan pertanyaan "mengapa" |
| A2 | Kisi-kisi C3; Latihan Bab 8 no. 8, Bab 9 no. 8, Bab 12 no. 8, Bab 14 no. 8 | Tidak menghitung SE; $\lvert\bar d\rvert > 2\cdot SE$ terpenuhi tetapi arah hanya 3 dari 5 (kombinasi yang tidak ada pada latihan buku); model kompleks ≈ Naive Bayes → batas pada fitur. **Irisan konsep yang disengaja:** aturan berpasangan itu sendiri |
| A3 | Latihan Bab 10 no. 2 dan 4 | Memilih di antara tiga metode untuk dua kebutuhan nyata dari bentuk klaster, ukuran data, dan k yang ditetapkan kebutuhan |
| A4 | Latihan Bab 11 no. 3(b)–(c) dan 6; Latihan Bab 14 no. 10(a) dan (c) ("apakah data tambahan akan membantu? bila tidak, ke mana perhatian dialihkan") | Tabel empat ukuran data untuk dua tim; keputusan membeli data; menyempitnya selisih latih–validasi sebagai bukti angka. Bab 14 no. 10 memakai kurva proyek mahasiswa sendiri dan meminta proposal, bukan membaca dua kurva yang diberikan. **Irisan konsep yang disengaja:** diagnosis "validasi masih menanjak → data tambahan membantu" dan "keduanya rendah dan mendatar → *underfit*" (Latihan Bab 11 no. 3(b)–(c), no. 6) diuji lewat tabel angka dua tim dan keputusan berbiaya, bukan lewat deskripsi pola |
| A5 | Latihan Bab 11 no. 2 dan 4; Latihan Bab 11 no. 10(f) (PCA pada masalah yang menuntut keterjelasan) | Keputusan dalam laporan model yang wajib menjelaskan penolakan; t-SNE dipakai sebagai fitur. Bab 11 no. 10(f) menanyakan titik komponen hasil eksperimen sendiri; A5(i) menilai keputusan dalam laporan dengan hak atas penjelasan |
| B1 | Kisi-kisi B1 (puskesmas; bentuk §4); Bab 2 §2.6 (keterlambatan pengiriman); Latihan Bab 13 no. 7 (umpan balik patroli) | COD yang ditolak; saat prediksi disimpulkan dari telepon sebelum penjemputan; kolom bocor dan pengecoh baru; biaya FN/FP; label selektif. Bentuk enam butir mengikuti kisi-kisi §4 (disengaja) |
| B2 | Kisi-kisi B1 dan B2 | Regresi produktivitas padi per desa; kolom citra mingguan yang sebagian belum tersedia; blok fitur berkorelasi (PCA, Ridge); usulan jaringan saraf sebagai pengecoh; pembagian per musim |
| C1 | Kisi-kisi C1 (200 sampel; fitur lain IG 0,08); Latihan Bab 8 no. 1 dan 5; Latihan Bab 8 no. 7 (kolom pengenal `id_transaksi` pada kepentingan fitur); Bab 8 §8.1.3 | Tiga kandidat; kandidat pengenal berdaun 3 dengan IG tertinggi; `min_samples_leaf` mengubah pilihan. Bab 8 no. 7 membahas pengenal lewat kepentingan bawaan vs permutasi, bukan lewat IG dan ukuran daun |
| C2 | Kisi-kisi C2 = Latihan Bab 12 no. 5 (2-2-1, $x=[1,1]$, $y=0$); Bab 12 §12.4.2 dan Lab 13 ($x=[1,0]$, $y=1$) | Bobot negatif, $x=[2,1]$, $\eta=0{,}5$; gradien dan pembaruan bobot lapis tersembunyi; arah $w_{22}$ dijelaskan lewat tanda $v_2$. **Irisan konsep yang disengaja:** (e) menanyakan arah perubahan bobot seperti kisi-kisi C2(f), tetapi pada bobot lapis tersembunyi dengan $v_2$ negatif |
| C3 | Kisi-kisi A3 (*silhouette* 0,68 → bermakna?); Latihan Bab 10 no. 3 dan 5 | Hitung manual $a$, $b$, $s$ dari tabel jarak dengan tiga klaster; titik negatif hasil K-Means; k dari *silhouette* dan kemampuan program |
| Seluruhnya | Latihan UTS (A1–A6, B1–B4, C1–C3) | Tidak ada butir yang memakai ulang kasus, data, atau bentuk tugas Latihan UTS; konsep Minggu 1–7 muncul hanya sebagai dasar perancangan pada Bagian B |

Seluruh konteks, angka, dan dataset adalah ilustrasi (rekaan); petunjuk latihan menyatakan bahwa data bukan data resmi lembaga mana pun.

---

## 8. Daftar Periksa

| # | Butir | Status |
|---|-------|--------|
| 1 | Komposisi A/B/C = 25/45/30, jumlah soal 5/2/3, total 100, 30 baris skor; Bagian B memuat (a)–(f) kisi-kisi §4 | ☑ dihitung skrip |
| 2 | Taksiran kerja ≤ 110 menit (5 + kerja + ≥ 5 ≤ 120) | ☑ ±85,8–107,5 menit dengan audit tulis memakai contoh *Baik* literal (§4) · ☐ uji coba berwaktu latihan oleh penguji coba yang belum membaca latihan ini, median ≤ 80 menit (§4.2) · ☐ uji coba berwaktu varian, aturan sama (wajib, T0-15) |
| 3 | Setiap baris skor bertanda Sub-CPMK, indikator, Bloom; tidak ada C1–C2; butir `082-1` ≥ C4; kata kerja perintah sesuai Bloom | ☑ |
| 4 | Latihan mencetak Bloom dan skor; pembahasan mencantumkan Sub-CPMK, Bloom, dan skor per butir | ☑ |
| 5 | Lembar rumus latihan = kisi-kisi §5 | ☑ lima baris rumus dan notasi sama persis; isi tabel $\log_2$ ditetapkan latihan karena kisi-kisi §5 hanya menyebut "tabel kecil" (Catatan untuk Dosen no. 3); $L$ dan $\partial L/\partial\hat y$ C2 dicetak pada stem |
| 6 | Angka kunci diverifikasi dengan Python | ☑ 9 Oktober 2026 — NumPy 2.5, scikit-learn 1.6.1 dan 1.9.1 ([pembahasan §5](latihan-uas-pembahasan.md#5-memeriksa-angka-dengan-python)) |
| 7 | Tidak memakai ulang/memparafrasa Latihan Soal Bab 8–14, contoh kisi-kisi UAS, dan Latihan UTS | ☑ (§7) — empat irisan konsep yang disengaja (A1, A2, A4, C2(e)) menunggu persetujuan dosen |
| 8 | Konteks Indonesia; data rekaan; nilai keislaman alami (amanah pada pernyataan amanah; *al-'adl* dan *la darar* pada B(f)) | ☑ |
| 9 | Varian naskah UAS + kunci disusun menurut §6 dan disimpan privat | ☐ T1-10 |
| 10 | Telaah sejawat varian dengan checklist-verifikasi §C | ☐ T0-15 |

---

## Catatan untuk Dosen

1. **Penandaan.** Baris hitung C3 (C1(a)–(c), C2(a)–(d); 15 poin) dan hitung *silhouette* C3(a)–(c) ditandai `102-1`, sehingga `082-1`/`102-1` = 58/42; menurut Tujuan Pembelajaran bab dan peta ICM pada RPS §F menjadi 73/27 sampai 85/15, tetapi ada baris C3 di bawah rentang `082-1` (§1, §3.1). Protokol B(e) ditandai `082-1` walaupun unsur pembagiannya ICM-04 → `102-1` (§1). Keputusan D-03; yang berubah hanya kolom Sub-CPMK §2–§3 dan judul butir pembahasan.
2. ***Silhouette* pada Bagian C.** C3 menghitung *silhouette*, bukan perbandingan berpasangan seperti contoh kisi-kisi §6 C3, agar porsi Minggu 11 sesuai kisi-kisi §2 (§3.5); modul Minggu 16 §16.3, §16.5, dan §16.7 kini menyebutnya. Bab 10 §10.3.2 belum memuat contoh terhitung *silhouette* (usul: tambahkan satu); bila C3 tidak disetujui, ganti dengan soal hitung lain dan jaga porsi Minggu 11 lewat butir lain.
3. **Tabel $\log_2$.** Kisi-kisi §5 hanya menyebut "tabel kecil"; latihan menetapkan 18 nilai $-\log_2 p$. Bila disetujui, tabel itu dapat dicantumkan pada kisi-kisi §5 agar varian memakai tabel yang sama.
4. **Waktu.** Taksiran realistis 5 + 107,5 menit, dengan ±7,5 menit untuk memeriksa; penentunya uji coba berwaktu §4.2 pada latihan ini sebelum varian disusun. Cadangan pertama (§4.3) disetujui dosen sebelum uji coba; cadangan itu hanya cukup sampai median ±81 menit dan seluruh pilihan §4.3 hanya sampai ±82,5 menit.
5. **Cakupan dan irisan konsep.** Porsi Minggu 1–7 = 21 dan Minggu 10 = 13 (kisi-kisi 15 dan 17) karena bentuk Bagian B dan kandidat contoh *Baik* (§3.5); deteksi anomali dan AI generatif tidak diuji tersendiri. Bila dosen menghendakinya, revisi butir **menggantikan** unsur pada minggu yang sama, bukan menambah butir. B(e) menilai juga validasi/penyetelan dan perbandingan kandidat — penjabaran kisi-kisi §4 dan Bab 9 §9.4, di samping pembagian dan *baseline* pada kisi-kisi §8. Empat irisan konsep yang disengaja (§7: A1, A2, A4, C2(e)) dipertahankan karena menguji konsep inti dengan konteks baru.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
