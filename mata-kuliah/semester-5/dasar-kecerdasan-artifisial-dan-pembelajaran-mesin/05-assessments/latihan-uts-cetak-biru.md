---
id: uai-if52510031-latihan-uts-cetak-biru
tipe: asesmen
judul: "Latihan UTS — Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — Cetak Biru Butir dan Panduan Varian"
kode_mk: IF52510031
nama_mk: Dasar Kecerdasan Artifisial dan Pembelajaran Mesin
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-08
---

# Cetak Biru Butir dan Panduan Varian — Latihan UTS Dasar Kecerdasan Artifisial dan Pembelajaran Mesin

## Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — IF52510031

> **Latihan UTS — bukan naskah UTS.** Cetak biru ini menyertai simulasi lengkap UTS Dasar Kecerdasan Artifisial dan Pembelajaran Mesin Ganjil 2026/2027 untuk berlatih: komposisi, durasi (120 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UTS. Naskah UTS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> Berkas ini untuk dosen dan penelaah: tabel butir, ringkasan per Sub-CPMK/Bloom/bagian, model waktu dan uji coba berwaktu, serta [panduan menyusun varian](#6-panduan-menyusun-varian-naskah-uts-sebenarnya). Pasangan berkas: [latihan UTS](latihan-uts.md) dan [pembahasan dan pedoman skor](latihan-uts-pembahasan.md).

| Aspek | Keterangan | Acuan |
|-------|------------|-------|
| Waktu, bentuk | Minggu 8 · tes tulis · 120 menit · *closed book* · kalkulator saja · rumus dicetak pada lembar soal | [Kisi-kisi UTS](kisi-kisi-uts.md) §1, §5 |
| Cakupan | Minggu 1–7 | Kisi-kisi §2 |
| Komposisi | A. Konsep 30% (6 soal) · B. Analisis kasus 40% (4 soal) · C. Perhitungan 30% (3 soal) | Kisi-kisi §3 |
| Bobot nilai akhir | 20% (Tes Tulis UTS; registri: seluruhnya `DAIML-Sub-CPMK102-1`) | [RPS §H.1](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md#h1-bobot-per-teknik-dan-sub-cpmk); registri 15d |
| Penandaan | Per butir menurut isinya (§1) | KENDALI-EKSEKUSI D-03 |
| Perkiraan waktu | Membaca petunjuk dan lembar rumus ±5 menit · membaca soal + menjawab ±92–109,1 menit · memeriksa ≥ 5 menit (§4); belum diuji coba — aturan uji coba berwaktu §4.2 | — |
| Berkas | [Latihan UTS](latihan-uts.md) · [pembahasan dan pedoman skor](latihan-uts-pembahasan.md) | — |
| Butir kendali | T0-01 (varian naskah + kunci) · T0-15 (telaah sejawat dan uji coba berwaktu) · T1-16 (lembar skor per butir) | [KENDALI-EKSEKUSI](../../../00-meta/KENDALI-EKSEKUSI.md) |
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

**Penandaan Sub-CPMK per butir menurut isi adalah bawaan sementara D-03(a).**

1. **Sub-CPMK ditetapkan menurut isi butir**, dengan Materi registri 15d sebagai pembeda: formulasi masalah, kelayakan ML, *baseline*, dan pemilihan/generalisasi model → `082-1`; prapemrosesan, pembagian data, rekayasa fitur, kebocoran, serta metrik klasifikasi/regresi → `102-1`. Akibatnya butir metrik Minggu 6–7 (C1, C2, B2(b)–(c), B4(d)) ditandai `102-1`, berbeda dari peta ICM-06/07 → `082-1` pada [RPS §F](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md#f-indikator-capaian-mingguan); ICM tetap dicantumkan untuk penelusuran.
2. Level Bloom butir `102-1` dijaga dalam rentang Sub-CPMK-nya (C3–C4); butir `082-1` pada C4–C6. Tidak ada butir C1–C2 dan tidak ada perintah "sebutkan". Kata kerja perintah mengikuti level yang dicetak (registri `16-taksonomi-bloom-cap.md`): butir C4 tidak memakai kata kerja C5 seperti "nilailah" atau "putuskan" dan memuat sekurang-kurangnya satu kata kerja C4 (mis. "analisislah", "bandingkan", "hubungkan"), bukan hanya "tuliskan" atau "tentukan"; butir C3 tidak dibuka dengan "analisislah". "Pilih" dipakai pada A6(b), B1(b), B4(a) (C4) dan B2(d) (C5) karena registri mencantumkannya pada kedua level.
3. Soal campuran ditandai **per sub-soal**. Satu baris lembar skor = satu soal Bagian A (bagian berlabel di dalamnya, mis. A1 (i)/(ii) atau A6 (a)/(b), tidak dipisah) atau satu sub-soal Bagian B/C; setiap baris bertanda satu Sub-CPMK (33 baris).
4. **Latihan dan naskah varian mencetak Bloom dan skor saja.** Kisi-kisi UTS dan modul Minggu 8 menyatakan bahwa UTS mengukur `DAIML-Sub-CPMK102-1`, dan registri membebankan seluruh bobot UTS ke `102-1`. Tanda per butir dicantumkan pada pembahasan dan cetak biru dengan catatan itu, dan dipakai untuk menghitung ketercapaian (§5) — bukan untuk memindahkan bobot nilai akhir. Butir C5–C6 bertanda `082-1` (8 poin) berada di luar pernyataan cakupan kisi-kisi dan modul Minggu 8 (Catatan untuk Dosen no. 1).

---

## 2. Tabel Cetak Biru per Butir

| No | Mg | Indikator butir (yang diukur) | Ind. registri | ICM | Sub-CPMK | Bloom | Skor | Jawab (menit) |
|----|----|-------------------------------|---------------|-----|----------|-------|------|---------------|
| A1 | 1 | Menganalisis kelayakan ML pada dua usulan (satu layak, satu pertanyaan kausal dengan seleksi non-acak) dan menetapkan pendekatannya, termasuk pembanding yang harus dikalahkan bila layak | 082-1/1 | ICM-01 | `082-1` | C4 | 5 | 3,5–3,75 |
| A2 | 2 | Menganalisis bukti kinerja (*drift*; model ≈ *baseline*) untuk menentukan tahap daur hidup yang harus diulang dan tindakan bagi manajemen | 082-1/1 | ICM-02 | `082-1` | C4 | 5 | 3,5 |
| A3 | 3 | Menganalisis keluaran pemeriksaan kualitas data: kode nilai hilang, nilai 0 yang wajar (pengecoh), korelasi mencurigakan | 102-1/1 | ICM-03 | `102-1` | C4 | 5 | 3–3,75 |
| A4 | 3 | Menganalisis keputusan penyandian dan penskalaan untuk k-NN (ordinal di-*one-hot*, pencilan, satu keputusan tepat) | 102-1/1 | ICM-03 | `102-1` | C4 | 5 | 3,75 |
| A5 | 5 | Menganalisis tiga calon fitur (interaksi, ketersediaan saat prediksi, agregat masa lalu) dan menentukan pertahankan/ubah/buang | 102-1/1 | ICM-05 | `102-1` | C4 | 5 | 3–3,75 |
| A6 | 6 | Menganalisis galat latih–validasi untuk mendiagnosis kondisi model dan memilih α | 082-1/1 | ICM-06 | `082-1` | C4 | 5 | 3–3,75 |
| B1a | 4 | Menganalisis kode untuk menemukan tiga kebocoran dan menamai jenisnya (satu pengecoh) | 102-1/1 | ICM-04 | `102-1` | C4 | 3 | 2,5–3 |
| B1b | 4 | Menganalisis arah bias skor, kebocoran terbesar pada data itu, dan mekanismenya | 102-1/1 | ICM-04 | `102-1` | C4 | 4 | 2,5–3 |
| B1c | 4 | Menerapkan perbaikan alur sebagai langkah/pseudokode: pembagian berkelompok, imputasi di `Pipeline`, CV berkelompok untuk `k`, uji sekali | 102-1/1 | ICM-04 | `102-1` | C3 | 3 | 3,5–4 |
| B2a | 2 | Merumuskan target empat unsur selaras saat keputusan; jenis *task* | 082-1/1 | ICM-02 | `082-1` | C6 | 2 | 3 |
| B2b | 7 | Menghitung batas *recall* akibat kapasitas dan menganalisis artinya | 102-1/2 | ICM-07 | `102-1` | C4 | 2 | 2 |
| B2c | 7 | Menganalisis akurasi = *baseline*; ambang dari kapasitas; metrik 40 teratas | 102-1/2 | ICM-07 | `102-1` | C4 | 3 | 2,5–3 |
| B2d | 2 | Memilih *baseline* bermakna beserta argumentasinya | 082-1/1 | ICM-02 | `082-1` | C5 | 3 | 1,75–2,25 |
| B3a | 3, 4, 5 | Menganalisis tiga kekeliruan penyiapan data (agregat target bocor, fitur rasio dari target, nominal diberi nomor) | 102-1/1 | ICM-03/04/05 | `102-1` | C4 | 3 | 3 |
| B3b | 3 | Menganalisis pola nilai hilang (MAR), akibat `dropna` pada saran harga; usul penanganan | 102-1/1 | ICM-03 | `102-1` | C4 | 3 | 3–3,5 |
| B3c | 5 | Menerapkan penyandian bulan yang menangkap musim tahun ajaran | 102-1/1 | ICM-05 | `102-1` | C3 | 2 | 2 |
| B3d | 5 | Menerapkan fitur agregat kecamatan pada baris latih (*cross-fitting*) dan kecamatan dengan sedikit iklan (penghalusan) | 102-1/1 | ICM-05 | `102-1` | C3 | 2 | 1,75–2,5 |
| B4a | 1 | Menganalisis usulan dengan satu pertanyaan uji kelayakan yang paling bermasalah dan mengaitkannya dengan batas kemampuan AI | 082-1/1 | ICM-01 | `082-1` | C4 | 3 | 1,75–2,25 |
| B4b | 3 | Menganalisis arah bias imputasi median (MNAR) dan kecukupan imputasi per pekerjaan | 102-1/1 | ICM-03 | `102-1` | C4 | 2 | 2–2,75 |
| B4c | 2 | Merancang ulang peran model, label, dan pengawasan | 082-1/1 | ICM-02 | `082-1` | C6 | 3 | 2,5–3 |
| B4d | 2 | Membandingkan dampak dua jenis kesalahan; menentukan metrik pengganti akurasi | 102-1/2 | ICM-02/07 | `102-1` | C4 | 2 | 1,5–2 |
| C1a | 7 | Menghitung *precision*, *recall*, dan F1 Model A dari matriks konfusi (akurasinya dan metrik Model B diberikan) | 102-1/2 | ICM-07 | `102-1` | C3 | 4 | 2,5–3 |
| C1b | 7 | Menghitung akurasi kebijakan tanpa kunjungan (= *baseline* kelas terbanyak) | 102-1/2 | ICM-07 | `102-1` | C3 | 1 | 1 |
| C1c | 7 | Menghitung total biaya kesalahan dua model | 102-1/2 | ICM-07 | `102-1` | C3 | 3 | 1,5–1,75 |
| C1d | 7 | Menganalisis pertentangan peringkat akurasi/F1 dengan biaya; memilih model | 102-1/2 | ICM-07 | `102-1` | C4 | 2 | 1,25–1,75 |
| C2a | 6 | Menghitung MAE dan RMSE Model P (Model Q diberikan) | 102-1/2 | ICM-06 | `102-1` | C3 | 4 | 4–4,5 |
| C2b | 6 | Menghitung R² Model P ($\bar{y}$ dan $SS_{tot}$ diberikan) | 102-1/2 | ICM-06 | `102-1` | C3 | 1 | 0,5 |
| C2c | 6 | Menganalisis rasio RMSE/MAE dan pengamatan penyebabnya | 102-1/2 | ICM-06 | `102-1` | C4 | 2 | 1–1,5 |
| C2d | 6 | Membandingkan dua model dengan ukuran yang membedakan perkiraan terlalu rendah dari terlalu tinggi (ditetapkan dan dihitung sendiri); memilih model | 102-1/2 | ICM-06 | `102-1` | C4 | 3 | 2–2,75 |
| C3a | 4 | Menghitung simpangan baku sampel skor lipatan berkelompok (rerata dan skema acak diberikan) | 102-1/2 | ICM-04 | `102-1` | C3 | 4 | 3,5–4 |
| C3b | 4 | Menganalisis optimisme skema acak (kebocoran kelompok); memilih taksiran | 102-1/1 | ICM-04 | `102-1` | C4 | 2 | 1–2 |
| C3c | 4 | Menganalisis lipatan menyimpang dan pemeriksaan per kelompok | 102-1/2 | ICM-04 | `102-1` | C4 | 2 | 2 |
| C3d | 4 | Menghubungkan hasil (a)–(c) menjadi laporan kinerja yang jujur beserta ketidakpastiannya (satu kalimat) | 102-1/2 | ICM-04 | `102-1` | C4 | 2 | 1,5–1,75 |
| **Jumlah** | | **33 baris skor · 13 soal** | | | | | **100** | **76,75–90** |

**Jawab** = taksiran waktu mahasiswa semester 5 berpikir, menghitung dengan kalkulator, dan menulis jawaban dengan tangan, **di luar** waktu membaca soal: angka kiri optimistis (penulis cepat), angka kanan realistis — waktu menulis jawaban minimal bernilai penuh pada ±20 kata/menit ditambah waktu berpikir dan menghitung (audit tulis, §4.1–§4.2). Waktu membaca dihitung terpisah (§4). Porsi minggu B3a dihitung per baris kode (baris 3 → Mg 5, baris 4 → Mg 4, baris 5 → Mg 3).

---

## 3. Ringkasan

### 3.1 Per Sub-CPMK

| Sub-CPMK | Butir (baris skor) | Skor maks | % UTS | Setara nilai akhir (× 20%) |
|----------|--------------------|-----------|-------|----------------------------|
| `DAIML-Sub-CPMK082-1` | A1, A2, A6, B2a, B2d, B4a, B4c | 26 | **26%** | 5,2 |
| `DAIML-Sub-CPMK102-1` | A3, A4, A5, B1a–c, B2b, B2c, B3a–d, B4b, B4d, C1a–d, C2a–d, C3a–d | 74 | **74%** | 14,8 |
| **Jumlah** | 33 baris | **100** | **100%** | **20,0** |

### 3.2 Per indikator registri

| Indikator | Skor | % |
|-----------|------|---|
| `082-1/1` Memformulasikan *task* dan memilih model | 26 | 26% |
| `082-1/2` Membangun *pipeline* dan melatih model yang dapat direproduksi | 0 | 0% — diukur oleh Observasi (lab) dan Unjuk Kerja (proyek), bukan tes tulis |
| `102-1/1` Menyiapkan dan membagi data tanpa kebocoran | 39 | 39% |
| `102-1/2` Menganalisis metrik dan memvisualisasikan hasil | 35 | 35% |

### 3.3 Per level Bloom

| Bloom | Skor | % | Rincian Sub-CPMK |
|-------|------|---|------------------|
| C1–C2 | 0 | 0% | — |
| C3 | 24 | 24% | `102-1` 24 |
| C4 | 68 | 68% | `082-1` 18 · `102-1` 50 |
| C5 | 3 | 3% | `082-1` 3 |
| C6 | 5 | 5% | `082-1` 5 |
| **≥ C3** | **100** | **100%** | Seluruh butir; 76% ≥ C4 |

### 3.4 Per bagian

| Bagian | Skor (kisi-kisi) | `082-1` | `102-1` | Membaca soal (menit) | Menjawab (menit) | Disarankan pada latihan |
|--------|------------------|---------|---------|----------------------|------------------|-------------------------|
| A. Konsep | 30 (30%) | 15 | 15 | 4,4–5,5 | 19,75–22,25 | ±28 menit |
| B. Analisis kasus | 40 (40%) | 11 | 29 | 6,9–8,6 | 35,25–41,25 | ±50 menit |
| C. Perhitungan | 30 (30%) | 0 | 30 | 4,0–5,0 | 21,75–26,5 | ±32 menit |
| **Jumlah** | **100** | **26** | **74** | **15,3–19,1** | **76,75–90** | **±110 menit** |

### 3.5 Per minggu — terhadap porsi perkiraan kisi-kisi §2

| Minggu | Topik | Porsi kisi-kisi | Aktual | Selisih |
|--------|-------|-----------------|--------|---------|
| 1 | Lanskap AI; kapan ML tidak dipakai | 8 | 8 | 0 |
| 2 | Formulasi *task*; metrik; *baseline* | 15 | 15 | 0 |
| 3 | Kualitas data; prapemrosesan; `Pipeline` | 18 | 16 | −2 |
| 4 | Pembagian data; enam jenis kebocoran | 22 | 21 | −1 |
| 5 | Rekayasa fitur; pemilihan fitur | 12 | 10 | −2 |
| 6 | Regresi; regularisasi; metrik regresi | 12 | 15 | +3 |
| 7 | Klasifikasi; matriks konfusi; metrik | 13 | 15 | +2 |
| **Jumlah** | | **100** | **100** | |

Seluruh selisih ≤ 3 poin. Kelebihan Minggu 6–7 berasal dari Bagian C yang menurut kisi-kisi memang berfokus pada metrik regresi dan klasifikasi.

---

## 4. Model Waktu

### 4.1 Cara menaksir

Waktu ujian 120 menit = **±5 menit** membaca petunjuk dan lembar rumus di awal + **waktu kerja** (membaca soal + menjawab) + **≥ 5 menit** memeriksa. Syaratnya: taksiran kerja realistis **≤ 110 menit**.

- **Membaca soal:** jumlah kata soal (judul, stem, tabel, kode, dan sub-soal; tanpa petunjuk dan lembar rumus) dibagi laju baca. 150 kata/menit = optimistis; **120 kata/menit** = laju baca cermat untuk teks padat kode, tabel, dan angka (dipakai untuk batas atas).
- **Menjawab:** taksiran per baris skor pada §2. Batas kanan (realistis) disusun dengan **audit tulis**: untuk setiap baris ditulis jawaban minimal bernilai penuh menurut pedoman skor — hanya unsur yang dinilai, seringkas contoh *Baik* pada pembahasan — lalu katanya dihitung (angka dan simbol pada perhitungan ikut dihitung). Pada laju tulis tangan **±20 kata/menit**, sisa anggaran menjadi waktu berpikir dan menghitung. Syaratnya: setiap baris analisis (C4–C6) menyisakan **≥ 0,5 menit** berpikir, dan baris hitung memuat waktu kalkulator. Batas kiri (optimistis) = penulis cepat (±25 kata/menit) dengan waktu berpikir lebih singkat.
- Petunjuk, kepala naskah, pernyataan amanah, dan lembar rumus (±380 kata dan lima baris rumus) terbaca dalam ±4 menit pada 120 kata/menit, sehingga cukup dalam jatah 5 menit. Pernyataan amanah hanya dibaca, tidak disalin: menuliskan nama dan NIM pada lembar jawaban berarti menyetujuinya.

### 4.2 Hasil per soal

| Soal | Kata soal | Baca (150–120 kpm) | Jawab | Kerja | Jawaban minimal (kata) | Menulis pada 20 kpm | Sisa berpikir/hitung (batas kanan) |
|------|-----------|--------------------|-------|-------|------------------------|---------------------|------------------------------------|
| A1 | 121 | 0,8–1,0 | 3,5–3,75 | 4,3–4,8 | 51 | 2,6 | 1,2 |
| A2 | 125 | 0,8–1,0 | 3,5 | 4,3–4,5 | 50 | 2,5 | 1,0 |
| A3 | 106 | 0,7–0,9 | 3–3,75 | 3,7–4,6 | 53 | 2,7 | 1,1 |
| A4 | 97 | 0,6–0,8 | 3,75 | 4,4–4,6 | 58 | 2,9 | 0,9 |
| A5 | 103 | 0,7–0,9 | 3–3,75 | 3,7–4,6 | 48 | 2,4 | 1,4 |
| A6 | 98 | 0,7–0,8 | 3–3,75 | 3,7–4,6 | 53 | 2,7 | 1,1 |
| B1 | 291 | 1,9–2,4 | 8,5–10 | 10,4–12,4 | 101 | 5,1 | 5,0 |
| B2 | 213 | 1,4–1,8 | 9,25–10,25 | 10,7–12,0 | 112 | 5,6 | 4,7 |
| B3 | 285 | 1,9–2,4 | 9,75–11 | 11,7–13,4 | 139 | 7,0 | 4,1 |
| B4 | 237 | 1,6–2,0 | 7,75–10 | 9,3–12,0 | 137 | 6,9 | 3,2 |
| C1 | 186 | 1,2–1,6 | 6,25–7,5 | 7,5–9,1 | 67 | 3,4 | 4,2 |
| C2 | 199 | 1,3–1,7 | 7,5–9,25 | 8,8–10,9 | 89 | 4,5 | 4,8 |
| C3 | 210 | 1,4–1,8 | 8–9,75 | 9,4–11,5 | 85 | 4,3 | 5,5 |
| **Jumlah** (termasuk kepala bagian, 25 kata) | **2.296** | **15,3–19,1** | **76,75–90** | **92,1–109,1** | **1.043** | **52,2** | **37,9** |

**Kesimpulan:** 5 + ±92–109,1 + ≥ 5 ≤ 120 menit. Pada taksiran realistis sisa memeriksa ±5,9 menit, dan petunjuk biasanya terbaca dalam ±4 dari 5 menit. Jawaban minimal bernilai penuh (±1.040 kata; kolom ini = contoh *Baik* literal pada pembahasan, dan langkah minimal untuk sub-soal hitung) memerlukan ±52 menit menulis; sisanya ±38 menit untuk berpikir dan menghitung — rata-rata ±1,1 menit per soal Bagian A dan ±1,1 menit per sub-soal Bagian B, paling sedikit ±0,5 menit (B2(d) dan B3(d)). Batas itu hanya berlaku bila jawaban seringkas contoh *Baik*; karena itu pembahasan menyatakan bahwa nilai penuh hanya menuntut unsur yang dinilai. Taksiran ini **belum diuji coba**; penentunya uji coba berwaktu berikut.

**Uji coba berwaktu.** Latihan ini diuji coba **sebelum varian disusun**, dan varian diuji coba lagi sebelum difinalkan (T0-15, §6.4 butir 3), dengan aturan yang sama: 2–3 asisten atau mahasiswa senior yang belum melihat pembahasan maupun varian mengerjakannya dalam kondisi ujian — 120 menit, *closed book*, tulisan tangan, alat bantu sesuai kisi-kisi (kalkulator saja), tanpa AI — dan mencatat menit per bagian; yang disimpan hanya angka agregat (median dan rentang). Untuk uji coba latihan ini, penguji coba juga **belum membaca atau mengerjakan latihan ini** (latihan publik sejak 8 Oktober 2026), karena penguji coba yang sudah mengenal soalnya bekerja lebih cepat dan membuat taksiran waktu terlalu rendah. Penguji coba yang menguasai materi bekerja ±1,5× lebih cepat daripada rerata mahasiswa, sehingga batasnya 2/3 dan 3/4 durasi; satu menit penguji coba di atas 80 menit setara ±1,5 menit kerja mahasiswa yang harus dipangkas:

| Median waktu penguji coba | Keputusan |
|---------------------------|-----------|
| ≤ 80 menit (≤ 2/3 durasi) | Lolos |
| > 80 dan ≤ 90 menit (≤ 3/4 durasi) | Lolos bersyarat: terapkan cadangan pemangkasan pertama (§4.4). Cadangan pertama hanya cukup untuk median sampai **±81 menit**; di atasnya dosen juga menetapkan pemangkasan lanjutan (§4.4), lalu uji ulang |
| > 90 menit (> 3/4 durasi) | Dosen menetapkan pemangkasan lanjutan (§4.4), lalu uji ulang |

Pemangkasan diterapkan pada latihan, pembahasan, dan cetak biru sekaligus, lalu pada varian, sehingga cetak biru keduanya tetap sama.

Data pelengkap (bila dosen memintanya): catatan menit per bagian dari mahasiswa yang mengerjakan latihan ini — termasuk waktu tambahan yang dicatat terpisah bila 120 menit tidak cukup (latihan, "Cara memakai latihan ini") — diserahkan tanpa nama; yang dipakai dan dicatat hanya rekap agregat (median dan rentang per bagian). Angka itu hanya data pelengkap; keputusan pemangkasan mengikuti median penguji coba pada tabel di atas.

### 4.3 Pemangkasan dari rancangan awal

Rancangan awal butir (sebelum diterbitkan sebagai latihan), dengan model yang sama tetapi sebelum audit tulis, memerlukan ±111–128,5 menit kerja (2.582 kata soal) — total ±116–133,5 menit bila petunjuk (±5 menit) ikut dihitung — sehingga batas 120 menit tidak terjamin. Pemangkasan berikut menghemat ±18,6 menit pada batas atas (±16,5 menit menjawab dan ±2,1 menit membaca) dan diterapkan tanpa mengubah komposisi 6/4/3 soal dan 30/40/30 poin, Sub-CPMK, maupun level Bloom per baris. **Penyusun varian tidak menambahkan kembali unsur yang dipangkas.**

| Butir | Dipangkas (termasuk pemadatan stem) | Hemat (± menit) | Catatan |
|-------|-------------------------------------|-----------------|---------|
| A1 | Tiga usulan → dua (usulan aturan tetap/zakat dibuang); 2,5 poin per usulan | 1,5 | Nilai amanah tetap hadir pada B4(d) dan pernyataan amanah |
| A2 | Tiga situasi → dua (label tidak konsisten dibuang; formulasi target sudah diuji B2(a) dan B4(c)) | 1,8 | — |
| A3 | Empat temuan → tiga (format "Rp" pada kolom biaya dibuang) | 1,4 | — |
| A4 | Empat baris → tiga (nilai bawaan `handle_unknown` dibuang) | 1,3 | Kisi-kisi §4: nilai baku hiperparameter tidak diuji |
| A5 | Empat fitur → tiga (kardinalitas tinggi dibuang; konsepnya diuji B3(d)) | 1,3 | — |
| A6 | Sub-soal "RMSE ≈ simpangan baku target" dibuang; (a) dan (b) masing-masing 2,5 poin | 1,6 | Gagasan *baseline* tetap diuji C1(b) dan B2(c) |
| B1 | Mekanisme dua kebocoran (2 poin) dan arah + kebocoran terbesar (2 poin) digabung menjadi satu sub-soal 4 poin | 1,6 | Baris skor 34 → 33 |
| B2 | F1 pada ambang 0,5 dibuang dari stem dan (c); ukuran dampak dibuang dari (d) | 2,0 | Ukuran dampak menjadi nilai tambah |
| B3 | (d): tiga keadaan → dua (kecamatan baru menjadi nilai tambah) | 0,8 | — |
| B4 | (d): cukup membandingkan dua kesalahan dan menentukan metrik pengganti | 0,6 | Alasan "akurasi meniru label bias" menjadi nilai tambah |
| C1 | (c) tanpa biaya kebijakan tanpa kunjungan; (d) tanpa syarat operasional | 1,8 | Keduanya menjadi catatan/nilai tambah pada pembahasan |
| C2 | $\bar{y}$ dan $SS_{tot}$ dicetak; (a) 4 poin, (b) 1 poin; rasio Model Q diberikan pada (c) | 2,0 | Lembar rumus tetap sama dengan kisi-kisi §5; stem C2 justru bertambah 27 kata |
| C3 | (d): dua kalimat → satu kalimat | 0,8 | — |
| **Jumlah** | | **±18,6** | Termasuk ±0,1 menit dari kepala bagian |

**Pemangkasan kedua dan audit tulis (8 Oktober 2026).** Telaah anggaran sesudah pemangkasan di atas (kerja ±95–109,9 menit) menunjukkan bahwa waktu menulis belum diperhitungkan: beberapa contoh jawaban *Baik* tidak dapat ditulis dalam anggaran barisnya, dan B2(d), B3(d), B4(b), serta B4(d) hampir tidak menyisakan waktu berpikir. Karena itu cadangan pertama yang semula direncanakan langsung diterapkan, dan anggaran per baris disusun ulang dengan audit tulis (§4.1):

| Perubahan | Rincian | Batas kanan menjawab (± menit) |
|-----------|---------|--------------------------------|
| Cadangan pertama lama diterapkan | C1(a): akurasi Model A dicetak pada stem — *precision* 1,25 · *recall* 1,25 · F1 1,5 · C3(a): rerata skema berkelompok dicetak — simpangan dan kuadratnya 2 · $s$ 2 · B4(a): cukup **satu** pertanyaan uji kelayakan — pertanyaan 1 · bukti 1 · batas AI 1 | −2,25 |
| Anggaran dinaikkan (sisa berpikir < 0,5 menit, atau contoh *Baik* lebih panjang daripada anggaran) | B2(d) +0,5 · B3(d) +0,5 · B4(b) +0,75 · B4(d) +0,5 · C1(c) +0,25 · C1(d) +0,25 · C2(c) +0,25 · C2(d) +0,25 | +3,25 |
| Anggaran diturunkan (baris analisis dengan sisa berpikir ≥ 2 menit di luar menulis) | B1(a) −0,5 · B1(c) −0,5 · B4(c) −0,5 | −1,5 |
| **Bersih** | Menjawab 90,5 → 90 menit; kata soal 2.329 → 2.335; kerja 109,9 → 109,5 menit | **−0,5** |

Pemangkasan kedua tidak menghapus konsep yang diuji: angka antara C1(a) dan C3(a) bukan keterampilan baru, dan B4(a) tetap menguji uji kelayakan dan batas kemampuan AI.

**Telaah sebelum terbit (8 Oktober 2026).** Stem A1 kini meminta pembanding (*baseline*) yang harus dikalahkan secara eksplisit, karena pedoman skornya memberi 0,5 untuk itu. A3–A5 hanya mencetak skor total, karena rincian per baris menandai baris yang "tepat", "bukan masalah", atau "pertahankan" (§6.2). A6(a) memakai kata kerja C4 ("analisislah"). Pernyataan amanah tidak lagi disalin mahasiswa (§4.1). Audit tulis kini memakai contoh *Baik* literal pada pembahasan, yang ditulis untuk setiap soal Bagian A dan B serta setiap sub-soal analisis Bagian C; contoh B3(d) dan B4(b) dipersingkat agar setiap baris menyisakan ≥ 0,5 menit berpikir. Anggaran jawab per baris tidak berubah. Hasil: kata soal 2.335 → 2.296 (termasuk koreksi hitung: baris penutup naskah dan *tagline* tidak lagi terhitung sebagai kata soal C3); kerja realistis 109,5 → 109,1 menit; jawaban minimal 964 → 1.043 kata.

### 4.4 Cadangan pemangkasan

Dipakai menurut hasil uji coba berwaktu (§4.2). Cadangan pertama yang semula direncanakan sudah diterapkan (§4.3); cadangan pertama di bawah adalah penggantinya. Cadangan pertama perlu disetujui dosen **sebelum** uji coba, lalu diterapkan langsung bila median 80–81 menit. Setiap cadangan menjaga komposisi 6/4/3 soal dan 30/40/30 poin serta Sub-CPMK, level Bloom, dan skor setiap baris; poin hanya dipindahkan di dalam baris yang sama. Angka hemat adalah taksiran model §4 (waktu menjawab; kata soal hampir tidak berubah).

| Cadangan | Pemangkasan | Pembagian poin baru | Hemat (± menit) |
|----------|-------------|---------------------|-----------------|
| **Pertama** (lolos bersyarat; cukup sampai median ±81 menit) | C1(c): total biaya Model B dicetak pada stem; mahasiswa menghitung biaya Model A saja · C2(a): kolom galat $e = y - \hat{y}$ Model P dicetak pada tabel | C1(c): biaya FN 1 · biaya FP 1 · total 1 · C2(a): tetap (MAE: nilai mutlak dan jumlahnya 0,75 + hasil 0,75 · RMSE: kuadrat dan jumlahnya 1,25 + hasil 1,25) | 1–1,25 |
| Lanjutan (keputusan dosen) | Pilihan yang mengurangi cakupan indikator: A3 dua temuan (T1 dan T2; kebocoran target tetap diuji A5 dan B3(a)) · B3(d) hanya keadaan (i) · B1(c) satu langkah perbaikan per kebocoran | Ditetapkan dosen bersama pemangkasannya | ±1 per pilihan |

Cadangan pertama tidak menghapus konsep yang diuji: biaya kesalahan tetap dihitung untuk satu model (seperti metrik pada C1(a)), dan MAE serta RMSE tetap dihitung dari galat.

**Batas cakupan cadangan.** Rentang lolos bersyarat (median 80–90 menit) setara sampai ±15 menit kerja mahasiswa, sedangkan cadangan pertama menghemat ±1–1,25 menit kerja mahasiswa (±0,7–0,8 menit penguji coba). Jadi cadangan pertama **hanya cukup untuk median sampai ±81 menit**. Cadangan pertama dan ketiga pilihan lanjutan bersama-sama (±4–4,25 menit kerja mahasiswa) **hanya cukup sampai ±83 menit**. Karena itu:

- median > ±81 dan ≤ ±83 menit → cadangan pertama ditambah pilihan lanjutan dari tabel di atas yang ditetapkan dosen, lalu uji ulang;
- median > ±83 menit → dosen menetapkan pemangkasan yang lebih besar daripada seluruh pilihan di tabel (mis. mencetak hasil antara pada butir hitung lain, menghapus satu sub-soal, atau mengurangi butir lewat revisi kisi-kisi), diterapkan pada latihan, pembahasan, dan cetak biru sekaligus, lalu uji ulang.

Pilihan lanjutan sebaiknya ditetapkan dosen **sebelum** uji coba, agar hasil uji coba langsung dapat ditindaklanjuti.

---

## 5. Ketercapaian per Sub-CPMK dari Skor Butir

Lembar skor mencatat **33 baris** (satu baris = satu soal Bagian A atau satu sub-soal Bagian B/C, seperti pada §2). Untuk tiap Sub-CPMK $j$:

$$\text{Ketercapaian}_j = \frac{\sum_{\text{mahasiswa}} \sum_{i \in j} \text{skor}_i}{N \cdot \text{skor maks}_j} \times 100\% \qquad \text{skor maks}_{082\text{-}1}=26,\ \ \text{skor maks}_{102\text{-}1}=74$$

- Yang dicatat di repositori hanya **agregat**: rerata dan sebaran per baris butir dan per Sub-CPMK, serta proporsi mahasiswa ≥ ambang. Skor per mahasiswa tidak dimasukkan ke repositori.
- **Butir yang perlu dicermati setelah ujian** (sinyal pengendalian pasca-UTS, T1-18): rerata < 50% skor maks; butir C4 dengan rerata jauh di bawah butir C3 se-Sub-CPMK; butir dengan banyak jawaban "Cukup" yang seragam (indikasi rumusan soal kurang jelas).
- Bobot nilai akhir UTS tetap 20% pada `102-1` sesuai registri; pemakaian angka ketercapaian di atas untuk alokasi ulang bobot memerlukan keputusan D-03 dan persetujuan prodi.

---

## 6. Panduan Menyusun Varian (Naskah UTS Sebenarnya)

Naskah UTS sebenarnya adalah **varian** latihan ini: struktur, tuntutan berpikir, dan skornya sama; isi permukaannya baru. Mahasiswa yang berlatih dengan sungguh-sungguh mendapat manfaat dari **cara bernalar** yang sama, bukan dari jawaban yang dihafal. Bila dibutuhkan ujian susulan, susun **varian kedua** dengan prosedur yang sama; konteks, data, dan angkanya berbeda dari latihan maupun varian pertama.

### 6.1 Invarian per butir

Yang **tidak boleh berubah** pada setiap butir varian:

| Butir | Sub-CPMK · Bloom · skor | Konsep/keterampilan yang diuji | Jumlah unsur/langkah | Kesulitan | Format jawaban |
|-------|-------------------------|--------------------------------|----------------------|-----------|----------------|
| A1 | `082-1` · C4 · 5 | Uji kelayakan ML: satu kasus layak (pola + data + kesalahan dapat ditoleransi + *baseline*), satu kasus kausal dengan seleksi non-acak | 2 usulan × (kesimpulan, alasan, pendekatan); untuk kasus layak, stem meminta pembanding yang harus dikalahkan | Sedang | Uraian singkat |
| A2 | `082-1` · C4 · 5 | Tahap daur hidup dari bukti: *drift* setelah perubahan dunia nyata; model ≈ *baseline* + tindakan bagi manajemen | 2 situasi × (tahap, alasan, tindakan) | Sedang | Uraian singkat |
| A3 | `102-1` · C4 · 5 | Membaca keluaran pemeriksaan data: kode nilai hilang; nilai ekstrem yang **sah** dengan bukti pemutus di kolom lain; korelasi mencurigakan karena informasi masa depan | 3 temuan (1 bukan masalah) | Sedang | Uraian/tabel; naskah mencetak skor total saja |
| A4 | `102-1` · C4 · 5 | Keputusan prapemrosesan untuk model berbasis jarak: ordinal diperlakukan nominal; penskalaan pada data menceng; satu keputusan tepat | 3 baris (1 tepat) | Sedang | Uraian/tabel; naskah mencetak skor total saja |
| A5 | `102-1` · C4 · 5 | Fitur untuk regresi linear pada saat prediksi tertentu: interaksi; fitur yang belum tersedia saat prediksi; agregat masa lalu yang sah | 3 fitur (ubah/buang/pertahankan) | Sedang | Uraian/tabel; naskah mencetak skor total saja |
| A6 | `082-1` · C4 · 5 | Diagnosis *overfit*/*underfit* dari tabel galat latih–validasi lima nilai regularisasi; memilih dengan validasi, bukan latih | 2 sub-soal | Sedang | Uraian singkat |
| B1 | `102-1` · C4, C4, C3 · 3 + 4 + 3 | Kode ±16 baris dengan tiga kebocoran dari enam jenis (salah satunya dominan karena struktur data) dan satu pengecoh yang sudah benar; arah bias; perbaikan sebagai langkah | 3 sub-soal; perbaikan 4 langkah | Sulit | Baris + jenis; uraian; langkah bernomor |
| B2 | `082-1`/`102-1` · C6, C4, C4, C5 · 2 + 2 + 3 + 3 | Keputusan berkapasitas tetap: target empat unsur selaras saat keputusan; batas *recall* = kapasitas/kejadian < 1; akurasi = *baseline*; ambang dari kapasitas, metrik k teratas; *baseline* bermakna | 4 sub-soal; 1 perhitungan dua langkah | Sulit | Uraian + hitung singkat |
| B3 | `102-1` · C4, C4, C3, C3 · 3 + 3 + 2 + 2 | Kode regresi ±11 baris dengan agregat target bocor, fitur turunan target, nominal diberi nomor; `dropna` pada pola MAR; penyandian musiman; agregat kategori dengan *cross-fitting* dan penghalusan | 4 sub-soal | Sulit | Uraian; langkah atau kode ringkas |
| B4 | `082-1`/`102-1` · C4, C4, C6, C4 · 3 + 2 + 3 + 2 | Keputusan publik otomatis berisiko tinggi: uji kelayakan (satu pertanyaan paling bermasalah) + batas AI; imputasi median pada pola MNAR; rancang ulang (peran, label, pengawasan); kesalahan eksklusi vs inklusi | 4 sub-soal | Sulit | Uraian |
| C1 | `102-1` · C3, C3, C3, C4 · 4 + 1 + 3 + 2 | Dua matriks konfusi; *precision*, *recall*, dan F1 dihitung untuk satu model (akurasinya dan metrik model lain diberikan); akurasi *baseline*; biaya asimetris yang membalik peringkat akurasi/F1 | 3 metrik + 1 akurasi *baseline* + 2 biaya + 1 analisis | Sedang | Hitung + uraian singkat |
| C2 | `102-1` · C3, C3, C4, C4 · 4 + 1 + 2 + 3 | Lima pengamatan, dua model; MAE dan RMSE satu model; R² dengan $\bar{y}$ dan $SS_{tot}$ diberikan; rasio RMSE/MAE; ukuran kerugian berarah | 5 baris galat; 1 rasio; 1 ukuran untuk 2 model | Sedang | Tabel hitung + uraian |
| C3 | `102-1` · C3, C4, C4, C4 · 4 + 2 + 2 + 2 | CV acak vs berkelompok; $s$ (pembagi $n-1$) lima skor dua desimal dengan rerata dicetak; lipatan menyimpang yang dijelaskan subkelompok; laporan jujur satu kalimat | 5 simpangan; 3 analisis | Sedang | Hitung + uraian singkat |

Komposisi, durasi, alat bantu, lembar rumus (sama dengan kisi-kisi §5), pernyataan amanah (rumusan sama dengan latihan; dicetak pada naskah dan disetujui dengan menuliskan nama dan NIM, tidak disalin), dan model waktu §4 juga invarian.

### 6.2 Yang wajib diubah, dengan contoh arah variasi

Pada **setiap** butir wajib diubah: konteks/kasus, data dan angka, nama entitas (instansi, kota, kolom, dataset), serta **urutan unsur** — analog dengan mengacak letak kunci pilihan ganda (latihan ini tidak memakai pilihan ganda): letak baris yang "tepat" pada A4, letak temuan yang "bukan masalah" pada A3, urutan keputusan ubah/buang/pertahankan pada A5, letak pengecoh dan urutan kebocoran pada B1, serta urutan baris kekeliruan pada B3 diacak ulang. Karena letaknya diacak, **rincian poin per baris yang dicetak pada naskah tidak boleh membedakan** baris "tepat" (A4), "bukan masalah" (A3), atau "pertahankan" (A5): naskah mencetak skor total butir saja, dan rincian per baris hanya ada pada kunci.

Tabel berikut **hanya menunjukkan arah variasi**. Dokumen ini publik, sehingga naskah varian **tidak boleh** memakai konteks, nama kolom, atau angka yang tercantum di sini; rancang konteks setara yang tidak tercantum (§6.3 butir 6).

| Butir | Contoh arah variasi (arah saja — konteks, nama, dan angkanya tidak dipakai pada varian) |
|-------|------------------------------------------------------------------|
| A1 | Kasus layak, mis. perkiraan kebutuhan kantong darah harian di UTD PMI atau perkiraan penumpang KRL per jam. Kasus kausal, mis. "apakah pelatihan digital **menyebabkan** omzet UMKM naik" dengan peserta yang mendaftar sendiri; "apakah aplikasi antrean menyebabkan waktu tunggu puskesmas turun" dengan puskesmas percontohan yang dipilih dinas. Urutan kedua kasus boleh dibalik |
| A2 | *Drift*, mis. model permintaan ojek daring di sekitar stasiun yang MAE-nya naik sejak LRT beroperasi, atau model penjualan toko yang memburuk sejak pesaing baru dibuka. Model ≈ *baseline*, mis. model penunggakan cicilan koperasi yang F1-nya sama dengan aturan "terlambat bayar ≥ 2 bulan", atau model keluhan pelanggan yang setara aturan sederhana berbasis riwayat |
| A3 | Kode hilang, mis. `tekanan_sistolik` = 999 atau `jumlah_anak` = −1. Nilai ekstrem yang sah, mis. `jam_kerja_per_minggu` = 0 pada responden berusia ≥ 60 yang berstatus pensiun, atau `jumlah_tanggungan` = 0 pada mahasiswa. Korelasi mencurigakan, mis. fitur yang memuat informasi sesudah saat prediksi — `total_klaim_tahun_ini` terhadap klaim bulan depan, atau status yang baru tercatat sesudah kejadian target |
| A4 | Model berbasis jarak dalam cakupan Minggu 1–7 (mis. k-NN) dengan kasus baru (mis. prediksi pembatalan pesanan katering). Ordinal di-*one-hot*, mis. tingkat kepuasan 1–5 atau jenjang pendidikan. Data menceng, mis. jumlah transaksi per bulan atau luas lahan. Keputusan tepat, mis. `OneHotEncoder(handle_unknown="ignore")` pada provinsi, atau `StandardScaler` pada usia yang hampir simetris |
| A5 | Konteks, mis. waktu tunggu servis bengkel atau durasi bongkar muat di pelabuhan. Interaksi, mis. jumlah kendaraan × hari Sabtu. Belum tersedia saat prediksi, mis. durasi pengerjaan aktual. Agregat masa lalu yang sah, mis. rata-rata durasi petugas itu pada periode sebelum saat prediksi |
| A6 | Lasso atau Ridge pada harga mobil bekas atau konsumsi BBM armada; lima nilai α dengan titik terbaik **di tengah** (bukan di tepi rentang), angka baru, pola *overfit* di α kecil dan *underfit* di α besar tetap |
| B1 | Entitas berulang lain: sesi belajar per mahasiswa di LMS, transaksi per pelanggan koperasi, pemeriksaan per ibu hamil di posyandu. Rotasi jenis kebocoran: mis. penskala di-*fit* sebelum pembagian (pengecoh berganti menjadi imputer yang sudah di dalam `Pipeline`), pemilihan fitur atau ambang pada data uji. Satu kebocoran tetap dominan karena struktur data dan dapat dijelaskan mekanismenya |
| B2 | Inspeksi 50 dari 1.500 kapal ikan per minggu; pemeriksaan 30 dari 900 SPBU per bulan; kunjungan 25 dari 500 posyandu. Prevalensi dan kapasitas baru dengan batas *recall* < 1 yang bersih; saat keputusan lain |
| B3 | Harga mobil bekas, tarif sewa ruko, atau harga lahan per kavling. Pola MAR baru (mis. kolom kosong pada iklan yang dipasang lewat aplikasi seluler, yang harganya berbeda); puncak musiman lain yang tetap pada bulan kalender (mis. Desember–Januari untuk sewa vila); agregat kategori lain (merek, kelurahan) |
| B4 | Penetapan otomatis penerima beasiswa daerah, subsidi pupuk, atau bantuan rumah tidak layak huni. Label lama dari keputusan panitia/kepala desa yang terbukti bias; data lama; kolom yang hilang pada pekerja informal (mis. slip gaji atau luas lahan garapan); target akurasi terhadap label lama |
| C1 | Deteksi kerusakan mesin di pabrik, penyakit tanaman di kebun, atau kendaraan tidak laik jalan saat uji KIR. Matriks konfusi baru dengan angka bulat; rasio biaya FN:FP baru (bukan 8× seperti latihan) yang **tetap** membalik peringkat akurasi/F1 terhadap biaya |
| C2 | Kebutuhan listrik harian menjelang hari raya, pengunjung kebun binatang pada libur sekolah, pesanan katering pada akhir pekan. Lima pengamatan dengan galat bulat; model yang unggul MAE harus kalah pada ukuran berarah karena meleset jauh terlalu rendah pada hari puncak; cetak $\bar{y}$ dan $SS_{tot}$; tetapkan ulang titik seri kerugian linear asimetris dan perbarui tabel ukuran yang diterima |
| C3 | Pasien per rumah sakit, toko per kota, atau petani per desa; subkelompok penyebab lipatan menyimpang yang baru (rumah sakit tipe D, toko di daerah 3T). Skor dua desimal; rerata skema berkelompok dicetak dan $s$ dapat dihitung manual |

### 6.3 Larangan

1. **Menyalin** kalimat, kasus, nama, atau angka latihan, termasuk contoh pada §6.2 (butir 6) — juga parafrasa dekat dan angka yang hanya digeser sedikit. Varian juga tidak boleh mengulang contoh soal kisi-kisi §6 maupun Latihan Soal Bab 1–7 buku ajar (§7).
2. **Mengubah** level Bloom, skor, Sub-CPMK, jumlah sub-soal, atau format jawaban suatu butir; mengubah komposisi 6/4/3 dan 30/40/30.
3. **Menambah materi di luar kisi-kisi** (Minggu 1–7) — mis. pohon keputusan, SVM, *clustering*, atau jaringan saraf — atau menguji hafalan nama fungsi dan nilai bawaan parameter (kisi-kisi §4).
4. **Menambahkan kembali** unsur yang dipangkas pada §4.3 atau §4.4, atau memperpanjang stem sehingga taksiran kerja model §4 melampaui 110 menit.
5. Menyajikan data sebagai data resmi suatu lembaga; seluruh angka tetap ilustrasi dan dinyatakan demikian pada petunjuk.
6. **Memakai contoh arah variasi §6.2 apa adanya** (konteks, nama, nama kolom, atau angka). Dokumen ini publik; contoh itu hanya menunjukkan arah, sehingga varian memakai konteks lain yang setara dan tidak tercantum pada dokumen ini, latihan, kisi-kisi, maupun buku ajar.
7. **Mencetak rincian poin per baris** pada A3–A5 (atau pada butir lain yang barisnya berbobot berbeda menurut jenis jawabannya): bobot baris akan menunjukkan baris yang "tepat", "bukan masalah", atau "pertahankan" (§6.2).

### 6.4 Prosedur mutu varian

1. **Selesaikan ulang setiap butir dengan Python** (Colab): seluruh angka Bagian C dan B2(b), perilaku setiap potongan kode (jalankan pada data sintetis), arah bias kebocoran pada B1, dan tabel ukuran yang diterima pada C2(d). Simpan skrip bersama kunci varian.
2. **Pastikan satu kunci yang benar** untuk setiap butir hitung dan setiap keputusan "tepat/tidak tepat"; untuk butir analisis, tulis daftar alternatif yang diterima seperti pada pembahasan latihan.
3. **Periksa waktu**: hitung kata varian dan ulangi model §4 termasuk audit tulis — jawaban minimal bernilai penuh per baris, setiap baris analisis menyisakan ≥ 0,5 menit berpikir, kerja ≤ 110 menit; lakukan **uji coba berwaktu** varian menurut aturan §4.2 — 2–3 penguji coba yang belum melihat varian maupun kuncinya; median ≤ 80 menit lolos, > 80–90 menit terapkan cadangan pertama §4.4 (cukup hanya sampai median ±81 menit; di atasnya dosen juga menetapkan pemangkasan lanjutan, dan di atas ±83 menit pemangkasan yang lebih besar daripada pilihan §4.4), > 90 menit dosen menetapkan pemangkasan lanjutan lalu uji ulang. Bandingkan dengan hasil uji coba latihan ini.
4. **Telaah sejawat** memakai [checklist-verifikasi](../../../00-pedoman-obe/checklist-verifikasi.md#c-lembar-telaah-sejawat) §C (KENDALI T0-15), termasuk pemeriksaan orisinalitas terhadap latihan ini.
5. **Simpan varian dan kuncinya di penyimpanan privat** (bukan di repositori). Setelah ujian, yang masuk repositori hanya angka agregat per butir dan per Sub-CPMK (§5).

---

## 7. Pemeriksaan Orisinalitas

Sumber yang dibandingkan: Latihan Soal Bab 1–7 buku ajar (tingkat Dasar, Menengah, Mahir), contoh soal kisi-kisi UTS §6 (A1–A6, B1–B4, C1–C3), dan contoh terhitung di badan bab (Bab 6 §6.4.2, Bab 7 §7.3.1).

| Butir | Sumber terdekat | Pembeda |
|-------|-----------------|---------|
| A1 | Latihan Bab 1 no. 5; kisi-kisi A1 ("sebutkan tiga keadaan") | Dua usulan baru; keputusan per kasus; seleksi non-acak pada pertanyaan kausal |
| A2 | Latihan Bab 2 no. 7 (F1 model vs *baseline*) | Situasi daur hidup (*drift*, model = aturan) dan tindakan bagi manajemen |
| A3 | Latihan Bab 3 no. 9(b); tabel tanda bahaya Bab 3 §3.2.2 | Membaca keluaran yang diberikan; pengecoh usia 0 di poli KIA dengan berat badan bayi sebagai pemutus |
| A4 | Latihan Bab 3 no. 2–3; kisi-kisi A3, A5 | Menganalisis keputusan yang sudah diambil; satu keputusan tepat |
| A5 | Latihan Bab 5 no. 1–3 | Interaksi, ketersediaan saat prediksi, agregat masa lalu; tanpa fitur siklik/rasio |
| A6 | Latihan Bab 6 no. 2 dan 8; kisi-kisi A6 (Ridge vs Lasso) | Tabel lima α; diagnosis dua ujung |
| B1 | Kisi-kisi B1 (= Latihan Bab 4 no. 5); Latihan Bab 4 no. 7 | Kode baru; tiga jenis kebocoran lain dan satu pengecoh; kebocoran terbesar dijelaskan dari struktur data (±6 baris/pasien, ciri tetap, k-NN) |
| B2 | Kisi-kisi B2, B3; Latihan Bab 7 no. 6 | Kapasitas tetap → batas *recall*, ambang dari kapasitas, metrik k teratas, *baseline* aturan |
| B3 | Latihan Bab 5 no. 5, Bab 3 no. 5 dan 6 | Iklan kos; kebocoran target lewat fitur rasio; nominal (bukan ordinal); musim tahun ajaran; *cross-fitting* dan penghalusan. **Irisan konsep yang disengaja:** baris 3 pada (a) (1 poin) menanyakan jenis kebocoran agregat target seperti Latihan Bab 5 no. 5(a) |
| B4 | Latihan Bab 1 no. 6 dan 8; Latihan Bab 3 no. 5 | Bantuan sosial; label bias; MNAR yang tidak terselesaikan oleh imputasi per pekerjaan; metrik eksklusi |
| C1 | Kisi-kisi C1; Latihan Bab 7 no. 2; Bab 7 §7.3.1 | Dua **model** dengan biaya asimetris; angka baru; metrik dihitung untuk satu model |
| C2 | Kisi-kisi C2 (= Bab 6 §6.4.2); Latihan Bab 6 no. 5 | Peringkat MAE dan RMSE berlawanan; ukuran berarah, bukan "metrik mana bila galat besar merugikan". **Irisan konsep yang disengaja:** (c) menanyakan pengamatan penyebab RMSE ≫ MAE seperti kisi-kisi C2(d) |
| C3 | Kisi-kisi C3; Latihan Bab 4 no. 8 | Satu model, dua skema CV; lipatan menyimpang yang dijelaskan subkelompok |

Seluruh konteks, angka, dan dataset adalah ilustrasi; petunjuk latihan menyatakan bahwa data bukan data resmi lembaga mana pun.

---

## 8. Daftar Periksa

| # | Butir | Status |
|---|-------|--------|
| 1 | Komposisi A/B/C = 30/40/30, jumlah soal 6/4/3, total 100, 33 baris skor | ☑ dihitung skrip |
| 2 | Taksiran kerja ≤ 110 menit (5 + kerja + ≥ 5 ≤ 120) | ☑ ±92–109,1 menit dengan audit tulis memakai contoh *Baik* literal (§4) · ☐ uji coba berwaktu latihan oleh penguji coba yang belum membaca latihan ini, median ≤ 80 menit (§4.2) · ☐ uji coba berwaktu varian, aturan sama (wajib, T0-15) |
| 3 | Setiap baris skor bertanda Sub-CPMK, indikator, Bloom; tidak ada C1–C2; kata kerja perintah sesuai Bloom | ☑ |
| 4 | Latihan mencetak Bloom dan skor; pembahasan mencantumkan Sub-CPMK, Bloom, dan skor per butir | ☑ — A3–A5 mencetak skor total saja (§6.2) |
| 5 | Lembar rumus latihan = kisi-kisi §5 | ☑ sama persis; $\bar{y}$ dan $SS_{tot}$ C2 dicetak pada stem |
| 6 | Angka kunci dan perilaku kode diverifikasi dengan Python | ☑ 8 Oktober 2026 — NumPy 2.5, pandas 2.2 dan 3.0, scikit-learn 1.6.1 dan 1.9.1 ([pembahasan §5](latihan-uts-pembahasan.md#5-memeriksa-angka-dengan-python)) |
| 7 | Tidak memakai ulang/memparafrasa Latihan Soal Bab 1–7 dan contoh kisi-kisi | ☑ (§7) — dua irisan konsep yang disengaja menunggu persetujuan dosen |
| 8 | Konteks Indonesia; nilai keislaman alami (amanah pada B4(d) dan pernyataan amanah) | ☑ |
| 9 | Varian naskah UTS + kunci disusun menurut §6 dan disimpan privat | ☐ T0-01 |
| 10 | Telaah sejawat varian dengan checklist-verifikasi §C | ☐ T0-15 |

---

## Catatan untuk Dosen

1. **Penandaan dan cakupan.** Penandaan Sub-CPMK per butir mengikuti bawaan sementara D-03(a); bila D-03 diputuskan lain, hanya kolom Sub-CPMK pada §2–§3 dan judul butir pembahasan yang diubah. Butir C5–C6 bertanda `082-1` (B2(a), B2(d), B4(c); 8 poin) berada di luar pernyataan kisi-kisi/RPS (UTS mengukur `102-1`, C3–C4) dan modul Minggu 8 (C2–C4); penyelarasannya menunggu D-03 (T0-19).
2. **Waktu.** Pemangkasan §4.3 — termasuk cadangan pertama yang semula direncanakan (C1(a), C3(a), B4(a)) — sudah diterapkan, dan anggaran per baris disusun ulang dengan audit tulis: taksiran realistis 5 + 109,1 menit, dengan ±5,9 menit untuk memeriksa. Penentunya uji coba berwaktu §4.2 pada latihan ini sebelum varian disusun. Cadangan pertama pengganti (§4.4: C1(c), C2(a)) disetujui dosen sebelum uji coba, lalu diterapkan langsung bila median 80–81 menit. Cadangan itu hanya cukup sampai ±81 menit dan seluruh pilihan §4.4 hanya sampai ±83 menit, sehingga pilihan lanjutan sebaiknya ditetapkan sebelum uji coba.
3. **Irisan konsep.** Dua irisan yang disengaja (§7: B3(a) baris 3 dan C2(c), ±2 poin) dipertahankan karena menguji konsep inti kisi-kisi dengan konteks baru.
4. **Lembar rumus** sama persis dengan kisi-kisi §5. $\bar{y}$, $SS_{tot}$, dan definisi $SS_{res}$ untuk C2 dicetak pada stem soal, bukan pada lembar rumus.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
