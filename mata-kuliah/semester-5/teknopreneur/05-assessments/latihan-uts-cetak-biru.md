---
id: uai-st52510002-latihan-uts-cetak-biru
tipe: asesmen
judul: "Latihan UTS — Teknopreneur — Cetak Biru Butir dan Panduan Varian"
kode_mk: ST52510002
nama_mk: Teknopreneur
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-08
---

# Cetak Biru Butir dan Panduan Varian — Latihan UTS Teknopreneur

## Teknopreneur — ST52510002

> **Latihan UTS — bukan naskah UTS.** Cetak biru ini menyertai simulasi lengkap UTS Teknopreneur Ganjil 2026/2027 untuk berlatih: komposisi, durasi (90 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UTS. Naskah UTS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> Berkas ini untuk dosen dan penelaah: tabel butir, ringkasan per Sub-CPMK/Bloom/bagian, model waktu dan uji coba berwaktu, serta [panduan menyusun varian](#panduan-menyusun-varian-naskah-uts-sebenarnya). Pasangan berkas: [latihan UTS](latihan-uts.md) dan [pembahasan dan pedoman skor](latihan-uts-pembahasan.md).

---

## Identitas dan Dasar Penyusunan

| Komponen | Isi |
|----------|-----|
| Mata kuliah | Teknopreneur (`ST52510002`), semester 5 |
| Asesmen | Latihan UTS (simulasi) untuk UTS Semester Ganjil 2026/2027, Minggu 8 — tes tulis *closed book*, 90 menit, skor 100; UTS berbobot 10% nilai akhir |
| Penyusun | Tri Aji Nugroho, S.T., M.T. |
| Butir kendali | [KENDALI-EKSEKUSI §2](../../../00-meta/KENDALI-EKSEKUSI.md#2-tahap-0--darurat-sebelum-uts-mg-58): `T0-03` (naskah UTS + kunci = varian privat dari latihan ini), `T0-15` (telaah sejawat dan uji coba berwaktu); `T1-16` (lembar per butir `mutu/02`) |
| Acuan | [Kisi-kisi UTS](kisi-kisi-uts.md) §1–§4 dan §7 (durasi 90 menit; *closed book*; kalkulator saja, rumus dicetak; komposisi A 30% · B 50% · C 20%; porsi topik; "tidak diuji: hafalan nama kerangka kerja"; kaidah penilaian) · [RPS Minggu 8](../01-rps/rps-teknopreneur.md#minggu-8--ujian-tengah-semester) dan [§G.1](../01-rps/rps-teknopreneur.md#g1-bobot-per-teknik-dan-sub-cpmk) · [RTM §I](../02-rtm/rtm-teknopreneur.md#i-ujian) · registri [`15d`](../../../00-kurikulum-if-2025-revisi-2026/15d-subcpmk-tingkat-3-semester-5-6.md) (bagian Teknopreneur) · Bab 1–7 buku ajar dan Modul 1–8 |

### Aturan penandaan Sub-CPMK

**Penandaan Sub-CPMK per butir menurut isi adalah bawaan sementara D-03(a)** ([KENDALI §1](../../../00-meta/KENDALI-EKSEKUSI.md#1-keputusan-yang-dibutuhkan-d), TD-48). Kisi-kisi, RPS §G.1, Modul 8 §8.5, dan registri `15d` membebankan seluruh UTS (10% nilai akhir) pada `TEKNO-Sub-CPMK091-1`; nilai akhir tetap dihitung sebagai skor UTS × 10%, sedangkan penandaan per butir dipakai untuk ketercapaian (`mutu/02`). Bila D-03 diputuskan lain, cukup kolom Sub-CPMK di tabel-tabel berkas ini dan judul butir pembahasan yang diubah — isi soal tidak berubah.

| Topik (label kisi-kisi §2) | Sub-CPMK menurut RPS §F | Butir menurut topik | Tag |
|----------------------------|-------------------------|---------------------|-----|
| Mg 1 — Ranah vs solusi; penyebab kegagalan usaha teknologi | `TEKNO-Sub-CPMKUAI32-1` | A1 | A1 → `UAI32-1` |
| Mg 2–4 — *The Mom Test*, struktur wawancara, kesalahan khas; persona berbasis bukti, JTBD, konteks penggunaan; kebutuhan vs keinginan vs solusi, *constraint*, keterlacakan | `TEKNO-Sub-CPMK091-1` | A2, A3, A4, B1, B2, B3, C1 | seluruhnya → `091-1` |
| Mg 5–7 — Pasar, kelayakan, *unit economics* (dasar) | `TEKNO-Sub-CPMKUAI21-1` | A5, B4 | A5, B4(a–b) → `UAI21-1`; **B4(c) → `UAI32-1`** |

B4(c) adalah satu-satunya sub-butir yang topik dan Sub-CPMK-nya berasal dari baris berbeda. Isinya — menyebut asumsi tim yang terbantah lalu memutuskan lanjut/ubah/hentikan dari angka *unit economics* — adalah bahan Mg 5–7 (Bab 7 §7.3.2–§7.3.3), sehingga porsi topiknya dihitung pada Mg 5–7. Tag Sub-CPMK-nya mengikuti **indikator**, bukan minggu: "merevisi asumsi bisnis setelah bukti pasar" adalah indikator 2 `UAI32-1`, dengan kriteria "bukti adaptasi keputusan".

Teks indikator registri yang dirujuk pada tabel butir (verbatim, `15d`):

| Kode ringkas | Teks registri |
|--------------|---------------|
| **091-I1** | Mendokumentasikan persona dan jobs-to-be-done pelanggan |
| **091-I2** | memetakan kebutuhan serta constraint menjadi persyaratan produk |
| **091-K** | Kriteria: Validitas bukti pelanggan; ketepatan sintesis kebutuhan; keterlacakan requirement |
| **091-M** | Materi: Customer discovery; persona; problem interview; context of use; product requirements |
| **21-I1** | Menganalisis pasar, kompetitor, biaya dan risiko |
| **21-I2** | membandingkan alternatif usaha menggunakan asumsi transparan |
| **21-K** | Kriteria: Ketepatan perhitungan dan data; kelengkapan kelayakan; kualitas evaluasi risiko |
| **32-I2** | merevisi asumsi bisnis setelah bukti pasar |
| **32-K** | Kriteria: Kejelasan pembelajaran; relevansi tren; bukti adaptasi keputusan |
| **32-M** | Materi: Technology entrepreneurship; innovation strategy; learning agility; trend scanning |

---

## Tabel Cetak Biru

### Per sub-butir

Kolom **Menjawab** = waktu menulis jawaban minimal + baris hitung + waktu berpikir menurut level Bloom, pada skenario tengah (lihat [model waktu](#komposisi-dan-waktu)); waktu membaca dihitung per butir pada tabel berikutnya. Angka per sub-butir dibulatkan, sehingga jumlahnya dapat berbeda 0,1 dari total.

| No. | Butir | Topik | Indikator butir (operasional) | Indikator / kriteria registri | Sub-CPMK | Bloom | Skor | Menjawab (menit) |
|:--:|------|:-----:|-------------------------------|-------------------------------|----------|:-----:|:----:|:----:|
| 1 | A1(a) | Mg 1 | Memilah ranah dan solusi dari empat pernyataan dengan uji yang dinyatakan | 32-M | UAI32-1 | C4 | 3 | 1,8 |
| 2 | A1(b) | Mg 1 | Menilai klaim "teknologi matang = risiko kecil" dan mengaitkannya dengan penyebab kegagalan usaha teknologi tersering | 32-M, 32-I2 | UAI32-1 | C5 | 3 | 3,3 |
| 3 | A1(c) | Mg 1 | Merumuskan ulang pernyataan solusi menjadi ranah (pelaku, kesulitan, bebas solusi) | 32-M | UAI32-1 | C3 | 3 | 1,2 |
| 4 | A2(a) | Mg 3 | Menganalisis persona rata-rata (gabungan segmen) melalui keputusan produk yang tak terputuskan | 091-I1, 091-K | 091-1 | C4 | 3 | 2,6 |
| 5 | A2(b) | Mg 3 | Menetapkan jumlah persona dan dasar pemisahannya dengan rujukan kode | 091-I1, 091-K | 091-1 | C4 | 3 | 2,8 |
| 6 | A3(a) | Mg 3 | Mengidentifikasi dimensi konteks penggunaan yang dilanggar beserta bukti pengamatan | 091-M (*context of use*) | 091-1 | C4 | 3 | 2,2 |
| 7 | A3(b) | Mg 3 | Mengusulkan perubahan konsep — bukan fitur — yang menghormati kendala konteks | 091-M, 091-I2 | 091-1 | C5 | 3 | 2,5 |
| 8 | A4 | Mg 4 | Mengklasifikasi jenis *constraint* dan sifat keras/lunak/belum pasti dari kutipan, dengan alasan | 091-I2 | 091-1 | C4 | 6 | 3,1 |
| 9 | A5 | Mg 6 | Mengurutkan ketergantungan pihak ketiga menurut dampak dan kekuatan bukti; alasan untuk butir teratas | 21-I1, 21-K | UAI21-1 | C5 | 3 | 2,5 |
| 10 | B1(a) | Mg 2 | Menganalisis tiga kesalahan pewawancara per giliran dan dampaknya pada mutu data | 091-M (*problem interview*), 091-K | 091-1 | C4 | 3 | 2,1 |
| 11 | B1(b) | Mg 2 | Mengenali solusi tempelan dalam transkrip dan menafsirkan artinya bagi tim | 091-M, 091-K | 091-1 | C4 | 3 | 2,6 |
| 12 | B1(c) | Mg 4 | Menerjemahkan keinginan menjadi kebutuhan bebas solusi dan persyaratan terukur lima unsur yang menghormati *constraint* | 091-I2, 091-K | 091-1 | C4 | 7 | 4,0 |
| 13 | B2(a) | Mg 3 | Memverifikasi empat pernyataan persona terhadap kutipan (didukung/berlebihan/salah rujuk/tanpa bukti) | 091-I1, 091-K | 091-1 | C5 | 5 | 4,0 |
| 14 | B2(b) | Mg 3 | Menguji pernyataan *job* dengan tiga ujian dan merumuskannya ulang secara tertelusur, termasuk lapis emosional/sosial | 091-I1 | 091-1 | C4 | 4 | 3,9 |
| 15 | B2(c) | Mg 3 | Menilai penetapan titik nyeri terbesar dengan dua kriteria (frekuensi, usaha mengatasi) yang dapat berlawanan arah, lalu menimbangnya | 091-I1, 091-K | 091-1 | C5 | 4 | 3,4 |
| 16 | B3(a) | Mg 4 | Menelusuri induk setiap persyaratan, atau kutipan yang menunjukkan persyaratan itu tidak dibutuhkan atau ditolak | 091-I2, 091-K (keterlacakan) | 091-1 | C4 | 5 | 1,7 |
| 17 | B3(b) | Mg 4 | Menilai persyaratan dengan model Kano (kategori diberikan) dan memutuskan prioritas beserta alasannya | 091-I2, 091-K | 091-1 | C5 | 7 | 2,9 |
| 18 | B4(a) | Mg 5 | Menghitung ulang SOM dari kapasitas dan perilaku membayar; menilai pengali, termasuk sumber "asisten AI tanpa rujukan" | 21-I1, 21-K | UAI21-1 | C4 | 4 | 4,1 |
| 19 | B4(b) | Mg 7 | Menghitung ulang CAC, margin, LTV, dan rasio (10 bulan), lalu menafsirkannya termasuk pengaruh masa bertahan nyata (D5) | 21-I1, 21-K | UAI21-1 | C4 | 5 | 5,3 |
| 20 | B4(c) | Mg 7\* | Merevisi asumsi setelah bukti (angka lama → baru) dan menetapkan keputusan lanjut/ubah/hentikan beserta alasannya | 32-I2, 32-K | UAI32-1 | C5 | 3 | 2,7 |
| 21 | C1(a) | Mg 2 | Menentukan narasumber yang dapat membantah dugaan dan cara menjangkaunya | 091-M (*customer discovery*), 091-K | 091-1 | C5 | 5 | 3,3 |
| 22 | C1(b) | Mg 2 | Menyusun pertanyaan perilaku masa lalu yang mencakup penerima dan jalur, konteks penggunaan, pencatatan, dan peristiwa terakhir | 091-M (*problem interview*; *context of use*), 091-K | 091-1 | C6 | 9 | 4,6 |
| 23 | C1(c) | Mg 2 | Membedakan jawaban yang mendukung dan yang melemahkan dugaan, untuk satu pertanyaan | 091-K (validitas bukti) | 091-1 | C4 | 6 | 2,6 |
| | | | | | | **Jumlah** | **100** | **69,1** |

Kode Sub-CPMK disingkat; kode lengkap: `TEKNO-Sub-CPMK091-1`, `TEKNO-Sub-CPMKUAI21-1`, `TEKNO-Sub-CPMKUAI32-1`.
\* B4(c): topik Mg 5–7, dihitung pada Mg 5–7 dalam rekap porsi topik; tag `UAI32-1` mengikuti indikator 2 (lihat [aturan penandaan](#aturan-penandaan-sub-cpmk)). Aspek konteks penggunaan pada C1(b) (Mg 3) dihitung pada Mg 2 bersama seluruh C1.

### Per butir — skor, beban, dan perkiraan waktu

| Butir | Sub-CPMK | Bloom dominan | Skor | Kata baca | Kata jawab minimal | Baris hitung | Berpikir (menit) | Waktu, skenario tengah (menit) | Konteks kasus |
|:-----:|----------|:-------------:|:----:|:---------:|:------------------:|:------------:|:----------------:|:-------------:|---------------|
| A1 | `UAI32-1` | C5 | 9 | 137 | 80 | — | 1,75 | 7,1 | Pernyataan P-00: katering pabrik Cikarang, songket Palembang, *chatbot* umrah, bengkel las Tangerang |
| A2 | `091-1` | C4 | 6 | 140 | 77 | — | 1,0 | 6,2 | Toko bahan bangunan, Kabupaten Bogor |
| A3 | `091-1` | C5 | 6 | 174 | 56 | — | 1,5 | 5,7 | Petugas baca meter air, Pontianak |
| A4 | `091-1` | C4 | 6 | 93 | 45 | — | 0,5 | 3,6 | Usaha fotokopi dekat kampus, Ciputat |
| A5 | `UAI21-1` | C5 | 3 | 115 | 26 | — | 1,0 | 3,1 | Informasi jadwal kapal, Kepulauan Seribu |
| B1 | `091-1` | C4 | 13 | 326 | 126 | — | 1,5 | 10,5 | Laundry kiloan rumahan, Depok |
| B2 | `091-1` | C5 | 13 | 382 | 153 | — | 2,5 | 13,4 | Bendahara masjid kecil, Kota Bandung |
| B3 | `091-1` | C5 | 12 | 312 | 55 | — | 1,5 | 6,4 | Penyewaan perlengkapan hajatan, Kabupaten Klaten |
| B4 | `UAI21-1` (a–b, 9) · `UAI32-1` (c, 3) | C4 | 12 | 444\*\* | 88 | 10 | 2,0 | 14,5 | Langganan perawatan motor ojek daring, Kota Medan |
| C1 | `091-1` | C6 | 20 | 257 | 132 | — | 3,0 | 12,0 | Wawancara lanjutan, homestay rumahan desa wisata, Kabupaten Sleman |
| *Umum* | — | — | — | 412 | — | — | — | 3,3 | Identitas, petunjuk, judul bagian; menulis nama/NIM |
| **Jumlah** | | | **100** | **2.792** | **838** | **10** | **16,25** | **85,6** (sisa **4,4**) | |

\*\* Termasuk Lembar Rumus (83 kata), yang dibaca saat mengerjakan B4.
**Bloom dominan** = level dengan skor terbesar di butir itu; bila seri, level yang lebih tinggi. **Kata baca** dihitung dari [latihan UTS](latihan-uts.md) — termasuk tanda skor dan level Bloom yang juga dicetak pada lembar UTS (TD-49), tanpa spanduk latihan dan tanpa bagian "Sesudah Waktu Habis". **Kata jawab minimal** = jumlah kata jawaban yang memuat setiap unsur pedoman skor untuk skor penuh tanpa unsur tambahan, ditulis sebagai kalimat atau butir ringkas (bukan gaya telegram) — **diukur dengan menulis jawaban seperti itu untuk setiap sub-butir**, bukan ditaksir; setara contoh "Baik" yang dipadatkan, dan bukan panjang yang dituntut. **Baris hitung** = satu baris operasi beserta hasilnya pada jawaban minimal B4: (a) 3 baris (kapasitas, pelanggan, SOM), (b) 7 baris (nilai waktu, total biaya, CAC, dukungan, margin, LTV, rasio). Kunci di pembahasan menjabarkannya menjadi ±14 baris agar mudah diikuti; baris tambahan itu tidak dituntut. **Berpikir** = jumlah waktu berpikir sub-butir menurut level Bloom-nya. Angka per butir dibulatkan; jumlahnya dapat berbeda 0,1–0,2 dari total.

---

## Rekap

### Komposisi dan waktu

| Bagian | Bentuk | Jumlah butir | Sub-butir | Skor | Kisi-kisi | Perkiraan (skenario tengah) | Saran pada Petunjuk 4 |
|--------|--------|:------------:|:---------:|:----:|:---------:|:---------------------------:|:---------------------:|
| A. Konsep | Uraian singkat | 5 | 9 | 30 | 30% · 5 soal ✓ | 25,6 menit | ±26 menit |
| B. Analisis kasus | Menilai bahan yang diberikan | 4 | 11 | 50 | 50% · 4 soal ✓ | 44,7 menit | ±45 menit |
| C. Perancangan | Menyusun naskah wawancara | 1 | 3 | 20 | 20% · 1 soal ✓ | 12,0 menit | ±12 menit |
| Umum | Petunjuk dan identitas | — | — | — | — | 3,3 menit | ±3 menit |
| Memeriksa jawaban | — | — | — | — | — | — | sisanya ±4 menit |
| **Jumlah** | | **10** | **23** | **100** | | **85,6 menit** — sisa **4,4** | 90 menit |

A4 dan A5 tidak bersub-butir; masing-masing dihitung satu sub-butir.

**Model waktu** (asumsi perencanaan, **belum diuji**; dihitung ulang 8 Oktober 2026 dengan kata jawab minimal yang diukur, bukan ditaksir, dan sesudah [cadangan (i) dan (ii)](#5-cadangan-pemangkasan-waktu) diterapkan):
waktu butir = kata baca ÷ kecepatan baca + kata jawab minimal ÷ kecepatan menulis tangan + baris hitung × menit per baris **+ Σ waktu berpikir sub-butir (menurut level Bloom) × faktor skenario**; ditambah waktu membaca bagian umum dan 1 menit menulis identitas. Waktu berpikir diperlukan karena kecepatan tulis 17,5 kata/menit hampir sama dengan kecepatan menyalin, sehingga tanpa itu model tidak menyisakan waktu untuk menimbang jawaban dan mencari rujukan (G…, M…, S…, D…). Waktu berpikir sengaja tidak dikurangi untuk sub-butir yang dipangkas (B2(c), B4(c)).

| Level Bloom sub-butir | Menit berpikir (skenario tengah) | Jumlah sub-butir | Subtotal |
|-----------------------|:--------------------------------:|:----------------:|:--------:|
| C3 | 0,25 | 1 (A1(c)) | 0,25 |
| C4 | 0,5 | 13 | 6,5 |
| C5 | 1,0 | 8 | 8,0 |
| C6 | 1,5 | 1 (C1(b)) | 1,5 |
| **Jumlah** | | **23** | **16,25 menit** |

| Skenario | Baca (kata/menit) | Tulis (kata/menit) | Menit per baris hitung | Faktor berpikir | Tanpa waktu berpikir | **Total** | Sisa dari 90 menit |
|----------|:-----------------:|:------------------:|:----------------------:|:---------------:|:--------------------:|:---------:|:--------:|
| Cepat | 215 | 20 | 0,4 | 0,75 | 59,9 menit | **72,1 menit** | 17,9 menit |
| **Tengah** | **180** | **17,5** | **0,5** | **1,00** | **69,4 menit** | **85,6 menit** | **4,4 menit** |
| Lambat | 160 | 15 | 0,6 | 1,25 | 80,3 menit | **100,6 menit** | −10,6 menit |

**Hasilnya:** skenario tengah muat dengan sisa **±4 menit** untuk memeriksa; **skenario lambat melewati 90 menit ±10,6 menit**. Sebelum cadangan (i) dan (ii) diterapkan, dengan kata jawab yang sama-sama diukur, angkanya 73,6 / 87,4 / 102,7 menit — skenario tengah hanya menyisakan ±2,6 menit; karena itu kedua cadangan diterapkan pada latihan ini, dan varian mengikutinya. Ukuran kata jawab sebelumnya (±748 kata, ditaksir) terlalu rendah; yang diukur ±868 kata sebelum pemangkasan dan **838 kata** sesudahnya. Asumsi waktu berpikir (0,5 menit per sub-butir C4, 1,0 per C5) dan kecepatan tulis tangan masih mungkin optimistis: bila waktu berpikir 1,5× asumsi, skenario tengah menjadi **±93,8 menit**, dan bila 2×, **±101,9 menit**. Model ini **belum membuktikan** latihan muat 90 menit untuk sebagian besar peserta; penentunya uji coba berwaktu pada latihan ini sebelum varian disusun ([prosedur mutu varian](#4-prosedur-mutu-varian) butir 4).

### Skor per Sub-CPMK (sementara)

| Sub-CPMK | Butir / sub-butir | Skor maks | % dari total UTS | Setara nilai akhir |
|----------|-------------------|:---------:|:----------------:|:------------------:|
| `TEKNO-Sub-CPMK091-1` | A2, A3, A4, B1, B2, B3, C1 | 76 | **76%** | ±7,6% |
| `TEKNO-Sub-CPMKUAI21-1` | A5, B4(a), B4(b) | 12 | **12%** | ±1,2% |
| `TEKNO-Sub-CPMKUAI32-1` | A1, B4(c) | 12 | **12%** | ±1,2% |
| **Jumlah** | | **100** | **100%** | 10% |

Kolom "setara nilai akhir" hanya bahan usulan revisi alokasi teknik ke tim kurikulum (`T2-08`); nilai akhir tetap skor UTS × 10% pada `TEKNO-Sub-CPMK091-1`. Bila D-03 memutuskan seluruh UTS untuk 091-1, baris UAI21-1 dan UAI32-1 digabung ke 091-1 (100%).

### Level Bloom

| Level | Skor sub-butir | % | Butir (level dominan) | Skor butir |
|-------|:--------------:|:-:|-----------------------|:----------:|
| C1 | 0 | 0% | — | 0 |
| C2 | 0 | 0% | — | 0 |
| C3 | 3 | 3% | — | 0 |
| C4 | 55 | 55% | A2, A4, B1, B4 | 37 |
| C5 | 33 | 33% | A1, A3, A5, B2, B3 | 43 |
| C6 | 9 | 9% | C1 | 20 |
| **Jumlah** | **100** | **100%** | 10 butir | **100** |

- **Mayoritas ≥ C3:** 10 dari 10 butir (level dominan); 100 dari 100 poin; 97 poin pada C4–C6.
- **Tanpa C1 murni ("sebutkan"):** A1(b) menuntut pengetahuan Bab 1 (penyebab kegagalan tersering), tetapi poinnya untuk **mengaitkan** penyebab itu dengan klaim tim. Kategori Kano dicetak pada B3(b); A3(a) dan A4 menerima "nama atau uraian singkat", dan pedoman skor memberi poin label yang sama untuk uraian setara (pembahasan §1.3 butir 4).
- **Terhadap rentang registri (penandaan sementara):**

| Sub-CPMK | Rentang registri | Di bawah | Di dalam | Di atas |
|----------|:----------------:|:--------:|:--------:|:-------:|
| `TEKNO-Sub-CPMK091-1` | C2–C4 | 0 | 43 | 33 (C5 = 24; C6 = 9) |
| `TEKNO-Sub-CPMKUAI21-1` | C4–C5 | 0 | 12 | 0 |
| `TEKNO-Sub-CPMKUAI32-1` | C6 | 12 | 0 | 0 |

### Porsi topik terhadap kisi-kisi

Label topik disalin dari kisi-kisi §2; setiap sub-butir dihitung pada topik **isinya**.

| Topik (kisi-kisi §2) | Kisi-kisi | Latihan | Selisih | Butir |
|----------------------|:---------:|:-------:|:-------:|-------|
| Mg 1 — Ranah vs solusi; penyebab kegagalan usaha teknologi | 10 | 9 | −1 | A1 |
| Mg 2 — *The Mom Test*; struktur wawancara; kesalahan khas | 25 | 26 | +1 | B1(a,b), C1 |
| Mg 3 — Persona berbasis bukti; JTBD; konteks penggunaan | 25 | 25 | 0 | A2, A3, B2 |
| Mg 4 — Kebutuhan vs keinginan vs solusi; *constraint*; keterlacakan | 25 | 25 | 0 | A4, B1(c), B3 |
| Mg 5–7 — Pasar, kelayakan, *unit economics* (dasar) | 15 | 15 | 0 | A5, B4 |
| **Jumlah** | **100** | **100** | | |

Contoh soal kisi-kisi §5 tidak memuat butir Mg 5–7; latihan ini mengikuti **tabel porsi** kisi-kisi §2, bukan sebaran contohnya.

---

## Pemeriksaan Ketentuan

| Ketentuan | Hasil |
|-----------|-------|
| Komposisi 5/4/1; bobot bagian 30/50/20; total 100 (kisi-kisi §3) | ✓ A1 9 · A2 6 · A3 6 · A4 6 · A5 3; B1 13 · B2 13 · B3 12 · B4 12; C1 20 |
| Durasi 90 menit | ✓ skenario tengah sesudah cadangan (i) dan (ii) diterapkan (85,6 menit, sisa 4,4 — ketat); ✗ skenario lambat (100,6). **Belum diuji** — uji coba berwaktu pada latihan ini sebelum Mg 7 dan sebelum varian disusun ([prosedur mutu](#4-prosedur-mutu-varian) butir 4) |
| Alat bantu (kisi-kisi §1, RTM §I, Modul 8 §8.5): kalkulator saja; rumus dicetak | ✓ Lembar Rumus pada latihan; tidak memuat kategori tafsir rasio atau komponen CAC (keduanya diuji) |
| Tidak menguji hafalan nama kerangka kerja (kisi-kisi §4) | ✓ Kategori Kano dicetak; uraian setara mendapat poin label (A3(a), A4, B3(b)) |
| Lembar soal tidak bertentangan dengan kisi-kisi | ✓ Lembar soal memuat skor dan level Bloom saja; Sub-CPMK per butir hanya di pembahasan dan cetak biru (TD-49) |
| Porsi topik kisi-kisi §2 | ✓ Selisih tiap topik ≤ 1 poin |
| Mayoritas butir ≥ C3; tidak ada C1 murni | ✓ 10/10 butir; 0 poin C1–C2 |
| Soal terbuka punya rubrik analitik dan kaidah "berbeda tetapi konsisten" (kisi-kisi §7) | ✓ Pembahasan §1.1–§1.2 (K1–K4) dan rubrik per butir; C1 dengan rubrik analitik penuh/sebagian/rendah |
| Rubrik hanya menilai yang diminta batang soal | ✓ A1(b) meminta kaitan dengan penyebab kegagalan; B1(c) menyebut lima unsur persyaratan dan aturan asumsi; B3(b) meminta alasan prioritas; B4(c) meminta angka lama → baru; besaran pada B2(c) dan uji berikutnya pada B4(c) tidak diminta sehingga tidak dinilai |
| Petunjuk tidak memberi isyarat jawaban | ✓ Petunjuk 6 menyebut jenis rujukan secara umum (nomor giliran, kode kutipan, nomor baris/pengamatan/data) tanpa bentuk kode; contoh P1/P5 pada B2(a) bukan baris yang dinilai |
| Kunci lengkap dengan langkah; angka diverifikasi Python | ✓ Pembahasan §6 (kode Colab dengan `assert`) |
| Contoh jawaban kurang/cukup/baik dan kesalahan umum untuk setiap butir | ✓ A1–A5, B1–B4, C1 |

### Orisinalitas

Sumber yang tidak boleh dipakai ulang — Latihan Soal Bab 1–7 (termasuk Latihan Reflektif Bab 1) dan contoh soal A1–C1 kisi-kisi — telah dibaca seluruhnya. Varian wajib lolos pemeriksaan yang sama, ditambah latihan ini dan contoh arah variasi pada [panduan varian](#2-yang-wajib-diubah-per-butir) sebagai sumber terlarang.

| Butir | Sumber terdekat | Perbedaan |
|-------|-----------------|-----------|
| A1 | Kisi-kisi A1, A2; Bab 1 Latihan 3, 6 | Kisi-kisi meminta definisi + contoh dan menyebut sebab kegagalan; A1 memilah empat pernyataan baru, **mengaitkan** penyebab kegagalan tersering dengan klaim tim, dan merumuskan ulang satu solusi menjadi ranah |
| A2 | Bab 3 Latihan 1, 6, 10; kisi-kisi B2 | Ketiganya menguji persona tanpa bukti secara umum; A2 menguji **persona rata-rata** dari dua segmen, keputusan yang tak terputuskan, dan jumlah persona |
| A3 | Kisi-kisi A5 | A5 meminta definisi; A3 menerapkan pada kasus baru dengan bukti pengamatan dan menuntut perubahan konsep |
| A4 | Kisi-kisi B3(e) | B3(e) meminta menyebut *constraint* tersirat; A4 menguji jenis dan sifat keras/lunak/belum pasti dengan alasan; nominal biaya sengaja berbeda dari contoh Modul 4 §4.2 |
| A5 | Bab 6 Latihan 4, 8, 12 | L4 meminta menyebut dua sumbu; L8 dan L12 merancang uji untuk proyek sendiri. A5 menerapkan kedua sumbu untuk **mengurutkan empat ketergantungan pihak ketiga yang diberikan** |
| B1 | Kisi-kisi B1, B3; Bab 2 Latihan 1, 2, 5, 6, 7 | Kisi-kisi B1 menilai daftar pertanyaan lepas; B1 menilai **transkrip berjalan** per giliran, mengenali solusi tempelan, lalu menurunkan kebutuhan dan persyaratan yang menghormati *constraint* |
| B2 | Kisi-kisi B2; Bab 3 Latihan 5, 6, 7, 8, 9 | B2 **mencocokkan klaim persona dengan kutipan yang disediakan** (salah rujuk vs tanpa bukti), menguji *job* dengan tiga ujian, dan menilai titik nyeri dengan dua kriteria yang berlawanan arah pada kasus baru |
| B3 | Kisi-kisi B4; Bab 4 Latihan 2, 5, 6, 7, 10 | B3 menelusuri induk dari kutipan + daftar persyaratan (dengan kutipan penunjuk untuk yang tanpa induk) dan menerapkan Kano dengan **kategori yang diberikan** |
| B4 | Bab 5 Latihan 2, 7, 12; Bab 7 Latihan 6, 7, 8 | Bab 7 L6/L7 menghitung CAC/LTV dari data bersih; B4 menuntut menemukan kesalahan model tim (sumber AI, kapasitas, "mau" ≠ membayar, voucer dan dukungan tak dihitung, masa bertahan) dan merevisi keputusan |
| C1 | Kisi-kisi C1; Bab 2 Latihan 8; Bab 3 Latihan 9 | Bentuk tetap menyusun naskah wawancara (komposisi Bagian C), tetapi sebagai **wawancara lanjutan untuk menguji dugaan tertulis tanpa mengungkapkannya**; yang sejajar contoh kisi-kisi C1 hanya prinsip "pertanyaan perilaku masa lalu, tanpa solusi" |

**Keadilan konteks.** Konteks kasus dipilih di luar daftar ranah yang disarankan [RTM §C.3](../02-rtm/rtm-teknopreneur.md#c3-ranah-yang-disarankan) (kuliner, organisasi mahasiswa, posyandu/puskesmas, pembelajaran sekolah, logistik UMKM daring, sampah/bank sampah, pertanian), agar tidak ada kelompok yang diuntungkan karena ranah proyeknya sama dengan kasus ujian — **kecuali** pernyataan pendek A1(1) tentang katering (kuliner), yang hanya diklasifikasi sebagai solusi. Varian tidak memakai ranah RTM §C.3 sama sekali, termasuk pada pernyataan pendek A1.

---

## Panduan Menyusun Varian (Naskah UTS Sebenarnya)

Naskah UTS sebenarnya adalah **varian** dari latihan ini: setiap butir menguji hal yang sama dengan bobot dan level yang sama, tetapi dengan kasus, data, dan angka baru. Mahasiswa yang berlatih dengan sungguh-sungguh memperoleh keuntungan dari **cara bernalar**, bukan dari hafalan jawaban. Bila dibutuhkan ujian susulan, susun **varian kedua** dengan prosedur yang sama; konteks, data, dan angkanya berbeda dari latihan maupun varian pertama.

> **Berkas ini publik.** Contoh pada tabel arah variasi hanya menggambarkan **jenis** perubahan; unsur yang disebut di berkas ini — konteks, solusi tempelan, *constraint*, fitur pengecoh, alasan penolakan, peran, teknologi, pasangan sebab — **tidak dipakai apa adanya** pada varian, agar kasus UTS tidak dapat ditebak. Tabel invarian hanya memuat tingkat keterampilan, bahan, jumlah langkah, kesulitan (label dan jumlah jebakan, tanpa jenisnya), dan format jawaban. **Sebaran kunci varian tidak dicantumkan di sini** — lihat catatan di bawah tabel invarian. Untuk varian, pilih konteks yang **tidak** disebut di berkas ini maupun di latihan.

### 1. Invarian per butir

Yang **tidak boleh berubah** dari latihan ke varian tercantum pada tabel di bawah.

**Kesulitan** (taksiran penyusun, per butir): **Sulit** bila butir memadukan beberapa bahan berkode (kutipan, giliran, data) menjadi penilaian, keputusan, atau rancangan **dan** memuat ≥ 2 jebakan khas; selain itu **Sedang**. *Jebakan khas* adalah unsur bahan yang sengaja memancing miskonsepsi yang dikenal. Varian mempertahankan label kesulitan, **jumlah** jebakan khas, dan bahan tempat jebakan itu berada (kolom Kesulitan); **jenis** dan letak persis setiap jebakan varian ditetapkan dari data varian dan dicatat pada lembar invarian privat. Tabel ini sengaja tidak menyatakan apakah jenisnya sama dengan latihan, karena jenis jebakan menentukan sebagian kunci (jebakan latihan diuraikan pada bagian *Kesalahan umum* setiap butir di pembahasan). Panjangnya dijaga dengan kata baca dan kata jawab minimal per butir dalam ±10% dari latihan ([prosedur mutu](#4-prosedur-mutu-varian) butir 4). Sebaran skor: Sedang 30 (Bagian A) · Sulit 70 (Bagian B dan C). Label ini taksiran; bila tersedia, kalibrasikan dengan capaian rata-rata per butir (agregat) dari latihan dan UTS.

| Butir | Sub-CPMK · Bloom · skor per sub-butir | Konsep/keterampilan yang diuji | Bahan dan jumlah langkah | Kesulitan | Format jawaban |
|:-----:|---------------------------------------|--------------------------------|--------------------------|-----------|----------------|
| A1 | UAI32-1 · (a) C4 3 · (b) C5 3 · (c) C3 3 | Ranah vs solusi dengan uji eksplisit; klaim kelayakan teknis vs risiko pasar; penyebab kegagalan tersering; merumuskan ulang ranah | Empat pernyataan P-00 untuk dipilah menjadi ranah atau solusi; satu klaim tim tentang kelayakan teknis. Tiga langkah: memilah + menyatakan uji; mengkritik klaim dan mengaitkannya dengan penyebab kegagalan; merumuskan ulang satu pernyataan solusi menjadi ranah | Sedang — 1 jebakan, pada pernyataan P-00 (unsur kalimat yang menyesatkan pemilahan) | Klasifikasi nomor + uji; 1–3 kalimat; satu rumusan ranah |
| A2 | 091-1 · (a) C4 3 · (b) C4 3 | Persona rata-rata (gabungan segmen); keputusan produk yang tak terputuskan; jumlah persona berbasis data | Ringkasan temuan 10–14 narasumber berkode dengan ciri yang dapat dibandingkan (cara membayar/bekerja, jumlah orang yang terlibat, keluhan utama, atau setara); persona susunan tim yang diuji terhadap ringkasan. Dua langkah: keputusan tak terputuskan + sebab; jumlah persona + dasar + kode | Sedang — 1 jebakan, pada persona tim (masalah pokoknya tampak seperti sekadar kurang detail) | Satu keputusan + sebab berkode; jumlah persona + dasar + kode |
| A3 | 091-1 · (a) C4 3 · (b) C5 3 | Dimensi konteks penggunaan (waktu, fisik, sosial, perangkat/infrastruktur); perubahan konsep vs fitur | Rancangan yang lolos uji laboratorium tetapi ditinggalkan di lapangan; lima pengamatan O1–O5 yang mencakup ≥ 4 dimensi; satu contoh fitur dikecualikan di batang soal. Dua langkah: tiga dimensi + bukti; satu perubahan konsep + dua pengamatan | Sedang — 1 jebakan, pada pengamatan (menyesatkan penamaan atau penghitungan dimensi) | Tiga dimensi + nomor pengamatan; satu usulan + dua pengamatan |
| A4 | 091-1 · C4 6 | Jenis *constraint* dan sifat keras/lunak/belum pasti | Tiga kutipan satu narasumber, masing-masing satu jenis *constraint* utama (boleh beririsan, seperti F1 waktu/fisik pada latihan; kunci mencantumkan jenis alternatif yang sah); sifatnya harus ditentukan dari isi kutipan, bukan dari nada bicara. Satu langkah per kutipan: jenis + sifat + alasan | Sedang — 2 jebakan, pada kutipan (kata atau nada yang menyesatkan penentuan jenis atau sifat); setiap kutipan dinilai sendiri, tidak dipadukan | Tabel tiga baris: jenis, sifat, alasan |
| A5 | UAI21-1 · C5 3 | Mengurutkan asumsi menurut dampak bila salah × kekuatan bukti | Empat ketergantungan pihak ketiga, masing-masing dengan keadaan saat ini; dampak dan kekuatan buktinya berbeda-beda. Dua langkah: mengurutkan; alasan dua sumbu untuk butir teratas | Sedang — 1 jebakan, pada daftar ketergantungan (kesan risiko yang tidak sejalan dengan dampak dan kekuatan bukti) | Urutan + alasan dua sumbu untuk butir teratas |
| B1 | 091-1 · (a) C4 3 · (b) C4 3 · (c) C4 7 | Kesalahan pewawancara; solusi tempelan; keinginan → kebutuhan → persyaratan lima unsur | Transkrip ±11 giliran dengan ≥ 6 jenis kesalahan pewawancara yang berbeda (agar ada pilihan); dua cara buatan sendiri untuk dua persoalan pada giliran berbeda (dinyatakan di batang soal); satu *constraint* yang dapat diperiksa; satu ukuran yang ada di transkrip. Tiga langkah: tiga kesalahan + akibat; dua cara + arti; kebutuhan + persyaratan | Sulit — 3 jebakan: satu pada giliran pewawancara, satu pada cara buatan sendiri, satu pada keinginan narasumber | Tabel tiga kesalahan; dua cara + arti; kebutuhan + persyaratan bertanda sumber/asumsi |
| B2 | 091-1 · (a) C5 5 · (b) C4 4 · (c) C5 4 | Verifikasi persona terhadap kutipan; tiga ujian *job*; titik nyeri terbesar dengan dua kriteria (frekuensi, usaha mengatasi) | Enam kutipan berkode dari 5–6 narasumber; draf persona enam baris (dua dicetak sebagai contoh yang sudah dinilai, empat dinilai) dengan kategori yang beragam; pernyataan *job* tim yang gagal ≥ 2 ujian (dinyatakan di batang soal); satu titik nyeri pilihan tim. Tiga langkah: menilai empat baris + alasan; ujian *job* + rumusan ulang berkode; dua kriteria pada kedua titik nyeri + kesimpulan | Sulit — 2 jebakan: satu pada kolom sumber draf persona, satu pada penerapan dua kriteria titik nyeri | Penilaian empat baris + alasan; ujian gagal + *job* baru berkode; dua kriteria + kesimpulan |
| B3 | 091-1 · (a) C4 5 · (b) C5 7 | Keterlacakan persyaratan; persyaratan tanpa induk; Kano dan keputusan prioritas | Enam kutipan; lima persyaratan campuran berinduk dan tanpa induk, setiap "tanpa induk" punya sekurang-kurangnya satu kutipan penunjuk yang jelas — penunjuk alternatif yang sah dicantumkan eksplisit di kunci (seperti S05-2/S07-2 untuk R4 pada latihan); dua persyaratan dinilai dengan Kano, kategori Kano dicetak. Dua langkah: induk atau "tidak ada" + kutipan penunjuk; jenis Kano + alasan + tindakan prioritas | Sulit — 2 jebakan: satu pada penelusuran induk, satu pada penggolongan Kano | Kode induk atau "tidak ada" + kutipan penunjuk; jenis Kano + alasan + tindakan |
| B4 | UAI21-1 · (a) C4 4 · (b) C4 5 · UAI32-1 · (c) C5 3 | SOM dari bawah; CAC jujur (waktu tim, biaya promosi); margin dengan dukungan manual; LTV/CAC; masa bertahan; revisi asumsi dan keputusan; kritik sumber AI tanpa rujukan | Tabel SOM tim lima pengali dengan sumber yang beragam mutunya (satu dari asisten AI tanpa rujukan); D1 kapasitas lapangan; D2 perilaku membayar k dari n; D3 biaya uang + jam tim × upah pembanding; D4 biaya langsung + menit dukungan; D5 masa bertahan asumsi vs tersirat; D6 kesimpulan tim. ±10 baris hitung pada jawaban minimal (±3 SOM, ±7 CAC–LTV) — dasar model waktu dan tabel per butir; kunci menjabarkannya menjadi ±14 baris; satu keputusan beralasan | Sulit — 4 jebakan yang melekat pada struktur bahan di kolom sebelah (bukan petunjuk kunci tambahan): sumber AI tanpa rujukan; "mau" ≠ membayar; komponen CAC dan margin yang tidak dihitung; menit → jam | Langkah hitung; pengali yang diganti + alasan, satu pengali lain yang bermasalah; arti; ≥ 2 asumsi terbantah (lama → baru) + keputusan beralasan |
| C1 | 091-1 · (a) C5 5 · (b) C6 9 · (c) C4 6 | Narasumber pembanding yang dapat membantah dugaan; pertanyaan peristiwa masa lalu bercakupan; bukti pendukung vs pelemah | Ranah baru; tiga temuan awal berkode; dugaan sebab tertulis berbentuk "X, bukan Y" yang tidak boleh diungkapkan; empat aspek cakupan pertanyaan di batang soal, salah satunya "di mana dan sedang apa" (konteks penggunaan). Tiga langkah: profil narasumber + alasan + cara; empat pertanyaan; satu pasang jawaban | Sulit — 2 jebakan (pada rancangan, bukan kunci): narasumber yang hanya membenarkan; temuan yang membaurkan kedua sebab | Profil narasumber + alasan + cara; empat pertanyaan; satu pasang jawaban |

Bagian umum juga invarian: petunjuk pengerjaan (termasuk saran waktu per bagian), aturan alat bantu, Lembar Rumus (isi dan urutan barisnya), serta penandaan skor dan level Bloom pada lembar soal — **kecuali rujukan khas latihan**, yang disesuaikan untuk naskah UTS: spanduk dan "Cara memakai", kata "latihan" pada baris identitas (Asesmen, Skor, Tidak diperkenankan) dan pada Petunjuk 3 dan 9, kalimat amanah tentang pembahasan, dan bagian "Sesudah Waktu Habis". Petunjuk 6 sudah umum (tanpa bentuk kode), sehingga cocok untuk kode apa pun pada varian.

**Sebaran kunci varian** — misalnya berapa pernyataan yang ranah, baris mana yang menjadi pengecoh, kategori apa yang muncul, butir mana yang teratas, dan arah keputusan B4 — ditetapkan dari data varian dan dicatat pada **lembar invarian privat** yang disimpan bersama varian ([prosedur mutu](#4-prosedur-mutu-varian) butir 1). Berkas publik ini sengaja tidak menyatakan apakah sebaran itu sama dengan latihan.

### 2. Yang wajib diubah per butir

Untuk **setiap** butir: konteks/kasus dan wilayah, data dan angka, nama orang/usaha/kode narasumber, serta urutan baris atau pilihan. Latihan ini tidak memuat pilihan ganda; padanannya adalah butir klasifikasi dan pengurutan (A1, A4, A5, B2(a), B3(a)) — **letak jawaban benarnya ditetapkan ulang secara acak** (boleh kebetulan sama dengan latihan) dan dicatat pada lembar invarian privat, sehingga pola jawaban latihan tidak dapat dipakai untuk menebak kunci varian.

| Butir | Arah variasi yang konkret |
|:-----:|---------------------------|
| A1 | Empat pernyataan dari sektor dan kota lain, di luar ranah RTM §C.3; letak ranah dan solusi diacak ulang (lembar invarian); teknologi pada pernyataan solusi diganti (mis. sensor IoT, *marketplace*, pengenalan gambar); klaim tim diganti klaim kelayakan teknis lain (mis. "API-nya sudah tersedia", "model sumber terbuka sudah akurat") |
| A2 | Jenis usaha dan kabupaten lain; jumlah narasumber, pengelompokannya, dan ciri pembedanya baru (mis. cara memesan, jam buka, sumber modal); nama dan ciri persona tim baru; kode narasumber tidak mengikuti pola latihan |
| A3 | Pekerja lapangan lain dengan rancangan gagal lain (mis. formulir panjang, foto kuitansi, verifikasi kode SMS); pengamatan dengan kendala lain (hujan, bising, sambil mengemudi, listrik padam); fitur pengecoh di batang soal diganti (mis. perintah suara) |
| A4 | Usaha lain; tiga kutipan baru — jenis dan sifat *constraint*-nya ditetapkan pada lembar invarian (boleh sama atau berbeda dengan latihan) dan urutannya diacak; angka pada kutipan tidak sama dengan latihan maupun contoh Modul 4 §4.2 (bukan "seratus ribu", bukan "lima puluh ribu"); pihak yang disebut dalam kutipan diganti (mis. pengelola gedung, asosiasi, dinas, pemasok) |
| A5 | Layanan informasi dan wilayah lain; letak ketergantungan paling berisiko diacak ulang (lembar invarian); pihak ketiga lain (mis. operator, koperasi, pengurus kawasan) |
| B1 | Usaha jasa lain; nomor giliran kesalahan dan urutannya diacak; dua solusi tempelan lain (mis. papan tulis, karet gelang warna, buku tempo); *constraint* lain yang dapat diperiksa (mis. tangan berminyak, tidak ada sinyal di los, ponsel dipakai berjualan siang hari); angka keluhan baru |
| B2 | Peran pengelola dana lain (mis. bendahara iuran warga, pengurus koperasi karyawan, pengelola dana sosial); kategori setiap baris persona ditetapkan ulang (lembar invarian); kutipan penanda dan pernyataan *job* baru (ujian yang gagal tetap ≥ 2 sesuai batang soal, kombinasinya boleh berbeda); titik nyeri pilihan tim berbeda jenisnya |
| B3 | Usaha penyewaan atau jasa lain dan kabupaten lain; urutan persyaratan berinduk/tanpa induk diacak; alasan penolakan pelanggan diganti (mis. enggan tanda tangan di layar, pembayaran lewat pengurus); letak dua persyaratan yang dinilai dengan Kano diacak ulang, kategorinya ditetapkan pada lembar invarian |
| B4 | Produk langganan dan kota lain; **seluruh angka baru** — harga, angka "dari asisten AI", persentase, parameter kapasitas, k/n, komponen biaya, jam tim, upah pembanding, menit dukungan, masa bertahan. Hasil antara bulat dalam rupiah; syarat angka lainnya (rentang rasio, komponen yang menentukan koreksi) ditetapkan pada lembar invarian |
| C1 | Ranah lain dengan dugaan sebab lain berbentuk "X, bukan Y" dan **pasangan sebab yang berbeda dari latihan** — bukan lagi jumlah penerima vs jumlah jalur (mis. "stok bahan habis karena pencatatan ditunda, bukan karena pemasok terlambat"); tiga temuan awal baru (pola buktinya pada lembar invarian); empat aspek cakupan disesuaikan dengan ranah baru |

### 3. Larangan

1. **Menyalin** kalimat, kutipan, nama, kode, atau angka dari latihan ini, dari contoh arah variasi pada berkas ini, juga dari Latihan Soal Bab 1–7 dan contoh soal kisi-kisi. "Kode" di sini berarti kode narasumber dan kutipan (mis. W01, M01-1, S01-2, H01) — buat pola baru. Label struktur (D1…, O1…, F1…, G1…, P1…, R1…, KP, P-00) boleh dipertahankan karena tidak mengungkap isi.
2. **Mengubah level Bloom** sub-butir mana pun, skor sub-butir, atau komposisi bagian (A 30 · B 50 · C 20). [Cadangan pemangkasan](#5-cadangan-pemangkasan-waktu) tidak melanggar larangan ini karena poinnya dipindahkan di dalam sub-butir yang sama.
3. **Menambah materi di luar kisi-kisi** — mis. *business model canvas*, MVP, *go-to-market*, *pitching* (Minggu 9 ke atas), atau rumus yang tidak ada pada Lembar Rumus.
4. Memakai ranah yang disarankan RTM §C.3 sebagai konteks kasus, termasuk pada pernyataan pendek A1.
5. Mencetak tag Sub-CPMK pada lembar soal (lembar soal memuat skor dan level Bloom saja, TD-49).
6. Menyimpan varian, kuncinya, lembar invariannya, atau skrip verifikasinya di repositori publik ini.

### 4. Prosedur mutu varian

1. **Isi lembar invarian (privat).** Untuk setiap butir varian, cocokkan dengan tabel invarian (Sub-CPMK, Bloom, skor, bahan dan jumlah langkah, kesulitan dan jumlah jebakan, format jawaban), lalu catat jenis dan letak setiap jebakan serta sebaran kuncinya. Lembar ini disimpan bersama varian, tidak di repositori.
2. **Selesaikan ulang setiap butir.** B4 dihitung ulang dengan Python — pakai kode pembahasan §6 sebagai templat, ganti angkanya, dan tambahkan `assert` untuk syarat angka pada lembar invarian (mis. hasil antara bulat, rentang rasio yang ditetapkan). Butir uraian diselesaikan dengan menulis jawaban "Baik" lengkap.
3. **Satu jawaban benar.** Untuk setiap butir klasifikasi dan pengurutan, pastikan hanya ada satu kunci — atau alternatif yang dapat dipertahankan dicantumkan eksplisit di kunci (seperti P2/P4 pada B2(a) dan R1 acuh/terbalik pada B3(b) latihan); setiap "tidak ada" pada B3(a) memiliki sekurang-kurangnya satu kutipan penunjuk yang jelas, dan penunjuk alternatif yang sah dicantumkan eksplisit di kunci (seperti S05-2/S07-2 untuk R4 pada latihan).
4. **Cek waktu — uji coba berwaktu** (KENDALI `T0-15`, TD-49).
   - **Latihan ini — sekarang, sebelum varian disusun; usulan jadwal: selesai sebelum Mg 7.** Penguji coba: 2–3 asisten atau mahasiswa senior yang belum melihat pembahasan maupun varian — untuk uji coba latihan ini, juga **belum membaca atau mengerjakan latihan ini** (latihan publik sejak 8 Oktober 2026) — dalam kondisi ujian (90 menit, *closed book*, tulisan tangan, kalkulator saja, tanpa AI); catat menit per bagian. Keputusan menurut **median** waktu penguji coba: **≤ 60 menit** (≤ 2/3 durasi) → lolos; **> 60 dan ≤ 67,5 menit** (≤ 3/4 durasi) → bersyarat: terapkan [cadangan pemangkasan pertama](#5-cadangan-pemangkasan-waktu), yaitu (iii) A4 dua kutipan, yang cukup untuk median sampai ±60,6 menit; di atasnya dosen juga memilih kandidat lanjutan (iv)–(vii), dan (viii) paling akhir; lalu uji ulang; **> 67,5 menit** → dosen menetapkan [pemangkasan lanjutan](#5-cadangan-pemangkasan-waktu), lalu uji ulang. **Dasar ambang:** penguji coba yang menguasai materi bekerja ±1,5× lebih cepat daripada rerata mahasiswa, sehingga 60 menit penguji coba setara ±90 menit rerata mahasiswa. Pemangkasan diterapkan pada latihan dan varian **sekaligus**. Catatan menit mahasiswa (latihan, "Sesudah Waktu Habis" butir 3) menjadi data pelengkap; yang dicatat hanya rekap agregat (median dan rentang per bagian).
   - **Varian:** hitung kata baca dengan aturan yang sama; total varian sebaiknya dalam ±5% dari 2.792 kata dan setiap butir dalam ±10% dari tabel per butir. Tulis jawaban minimal varian untuk setiap sub-butir (aturan pada catatan tabel per butir) dan hitung katanya; totalnya sebaiknya dalam ±5% dari 838 kata dan setiap butir dalam ±10% dari kolom "Kata jawab minimal". Bila tersedia, satu atau lebih penguji coba yang belum melihat varian mengerjakannya dengan aturan dan ambang yang sama.
5. **Telaah sejawat** dengan [checklist-verifikasi §C](../../../00-pedoman-obe/checklist-verifikasi.md#c-lembar-telaah-sejawat) (KENDALI `T0-15`), termasuk pemeriksaan orisinalitas terhadap latihan ini dan contoh arah variasi pada berkas ini.
6. **Simpan** varian, kunci dan pedoman skornya, lembar invarian, serta skrip verifikasinya di **penyimpanan privat** — tidak di repositori. Ke repositori hanya masuk angka agregat hasil UTS (`mutu/02`).
7. **Saat menilai UTS:** pakai pedoman skor varian dengan kaidah yang sama dengan pembahasan §1 (K1–K4, kesalahan bawaan, label tidak dihafal). Penelaah sejawat memeriksa ulang sekurang-kurangnya 10% lembar jawaban (acak, mencakup nilai tinggi, tengah, rendah); selisih > 2 poin pada satu butir dibahas dan diputuskan bersama, lalu dicatat sebagai tambahan pedoman. Kesamaan jawaban uraian yang mencolok antar-mahasiswa ditangani sesuai ketentuan universitas, bukan dengan pengurangan sepihak oleh pemeriksa.

### 5. Cadangan pemangkasan waktu

Setiap pemangkasan memindahkan poin di dalam sub-butir yang sama, sehingga skor sub-butir, skor butir, level Bloom, dan total 100 tidak berubah; yang berubah hanya batang soal dan pedoman skor — pada latihan dan varian sekaligus.

| Urutan | Pemangkasan | Pemindahan poin (skor sub-butir tetap) | Status · hemat tengah / lambat (menit) |
|:------:|-------------|----------------------------------------|:-----------------------------:|
| (i) | B2(c): dua kriteria saja — frekuensi dan usaha mengatasi | Per kriteria 1 → 1,5; kesimpulan tetap 1 (B2(c) tetap 4) | **Diterapkan** pada latihan (8 Oktober 2026) |
| (ii) | B4(c): tanpa "uji berikutnya beserta kriteria keberhasilan" | Asumsi terbantah 1 → 1,5; keputusan dengan alasan 1 → 1,5 (B4(c) tetap 3). Indikator 2 `UAI32-1` ("merevisi asumsi bisnis setelah bukti pasar") tetap terukur | **Diterapkan** pada latihan (8 Oktober 2026) |
| (iii) | A4: dua kutipan, bukan tiga (kutipan yang dibuang dipilih dosen; hemat = rerata ketiga pilihan) | Per kutipan: jenis 1 → 1,5; sifat dengan alasan 1 → 1,5 (alasan umum tetap 0,5); A4 tetap 6 | **Cadangan pemangkasan pertama** · ±1,0 / ±1,1 → total ±84,7 / ±99,5 |

Cadangan (i) dan (ii) diterapkan karena model waktu yang dihitung ulang (kata jawab diukur) menunjukkan skenario tengah tanpa keduanya hanya menyisakan ±2,6 menit. Cadangan (iii) adalah **cadangan pemangkasan pertama** yang diterapkan bila hasil uji coba berwaktu bersyarat ([prosedur mutu](#4-prosedur-mutu-varian) butir 4): hematnya terbesar di antara semua kandidat, dan ia tidak menyentuh literasi AI. Angka hemat adalah perkiraan model waktu yang sama (bacaan dan tulisan saja; waktu berpikir tidak dikurangi). Dengan (iii) pun **skenario lambat masih melewati 90 menit**. Bila median uji coba berwaktu > 67,5 menit — atau bersyarat, tetapi (iii) tidak cukup (lihat di bawah) — pemangkasan lanjutan diperlukan dan menjadi keputusan dosen.

**Kandidat pemangkasan lanjutan** (dipilih dosen; berlaku pada latihan dan varian sekaligus). Usulan urutan penyusun: sesuai nomor, dengan (viii) **paling akhir** karena menghapus satu-satunya butir literasi AI di UTS; sebaiknya dosen menetapkan urutannya **sebelum** uji coba. Aturannya sama: poin hanya dipindahkan di dalam sub-butir sendiri. Angka hemat dihitung dengan model waktu yang sama; waktu berpikir tidak dikurangi, sehingga perkiraannya konservatif.

| Kandidat | Pemangkasan | Pemindahan poin (skor sub-butir tetap) | Hemat tengah / lambat (menit) |
|:--------:|-------------|----------------------------------------|:-----------------------------:|
| (iv) | B2(a): tiga baris yang dinilai, bukan empat (mis. tanpa P2, yang kategorinya bercabang) | Konversi baris benar → skor: 3 = 5; 2,5 = 4; 2 = 3,5; 1,5 = 2,5; 1 = 1,5; 0,5 = 1; B2(a) tetap 5 | ±0,9 / ±1,0 |
| (v) | C1(b): tiga pertanyaan inti untuk tiga aspek — tanpa aspek pencatatan dan penerusan, yang sebagian sudah terbuka lewat pertanyaan penerima dan jalur | Per pertanyaan 1,5 → 2 (peristiwa dan terbuka 1,5; tidak memimpin 0,5; kebiasaan umum atau ya/tidak 1 + 0,5; menyiratkan pemesanan ganda 1,5 + 0); cakupan 3 aspek = 3, 2 = 1,5, 1 = 0,5; C1(b) tetap 9 | ±0,9 / ±1,1 |
| (vi) | B1(a): dua kesalahan pewawancara, bukan tiga | Per kesalahan: giliran + jenis 0,5; kerusakan pada data 0,5 → 1; B1(a) tetap 3 | ±0,6 / ±0,7 |
| (vii) | B3(a): empat persyaratan — tanpa R3 dan kutipan penunjuknya (S07-2) | R2, R5 tetap 1; R1, R4 "tidak ada" + kutipan penunjuk 1 → 1,5 ("tidak ada" tanpa penunjuk tetap 0,5); B3(a) tetap 5 | ±0,4 / ±0,5 |
| (viii) | B4(a): tanpa "satu pengali lain yang bermasalah" — **paling akhir**, karena menghapus satu-satunya butir literasi AI di UTS (kritik atas angka asisten AI tanpa rujukan) | Alasan dua pengali yang diganti 0,5 → 1 masing-masing (B4(a) tetap 4) | ±0,7 / ±0,8 |

**Cukupkah?** Kandidat (iv)–(vii) bersama-sama menghemat ±2,8 / ±3,2 menit; ditambah (iii) ±3,7 / ±4,3 (model ±81,9 / ±96,3 menit), dan dengan (viii) juga ±4,4 / ±5,1 (±81,2 / ±95,5 menit) — skenario lambat **masih** di atas 90 menit. Menurut [dasar ambang uji coba](#4-prosedur-mutu-varian) (butir 4), (iii) saja menutup median sampai ±60,6 menit, (iii)–(vii) sampai ±62,5 menit, dan seluruh cadangan termasuk (viii) sampai ±63 menit. Karena itu, pada Teknopreneur hasil **bersyarat** (median > 60 dan ≤ 67,5 menit) di atas ±60,6 menit memerlukan, selain (iii), satu atau lebih kandidat (iv)–(vii) pilihan dosen; (viii) baru diperlukan bila median di atas ±62,5 menit. Median di atas ±63 menit tidak dapat ditutup dengan pemindahan poin di dalam sub-butir; yang diperlukan adalah pengurangan butir atau sub-butir lewat revisi kisi-kisi (keputusan dosen).

---

## Templat Lembar per Butir untuk `mutu/02` (diisi setelah UTS — agregat saja)

| Butir | Sub-CPMK (sementara) | Bloom | Skor maks | Rata-rata kelas | % capaian (rata-rata ÷ maks) | Catatan butir (mis. daya beda, kesalahan umum) |
|:-----:|----------|:-----:|:---------:|:---------------:|:----------------------------:|-----------------------------------------------|
| A1 | UAI32-1 | C5 | 9 | | | |
| A2 | 091-1 | C4 | 6 | | | |
| A3 | 091-1 | C5 | 6 | | | |
| A4 | 091-1 | C4 | 6 | | | |
| A5 | UAI21-1 | C5 | 3 | | | |
| B1 | 091-1 | C4 | 13 | | | |
| B2 | 091-1 | C5 | 13 | | | |
| B3 | 091-1 | C5 | 12 | | | |
| B4(a–b) | UAI21-1 | C4 | 9 | | | |
| B4(c) | UAI32-1 | C5 | 3 | | | |
| C1 | 091-1 | C6 | 20 | | | |

| Sub-CPMK | Skor maks | n | Rata-rata capaian (%) | % mahasiswa ≥ ambang\* | Status |
|----------|:---------:|:-:|:---------------------:|:----------------------:|:------:|
| `TEKNO-Sub-CPMK091-1` | 76 | | | | ⏳ |
| `TEKNO-Sub-CPMKUAI21-1` | 12 | | | | ⏳ |
| `TEKNO-Sub-CPMKUAI32-1` | 12 | | | | ⏳ |

\* Ambang usulan 70 — **status usulan**, menunggu `T1-17` dan SK (`F-03`). Skor per mahasiswa tidak masuk repositori; hanya baris agregat. Bila D-03 tidak memilih opsi (a), tabel kedua menjadi satu baris (`TEKNO-Sub-CPMK091-1`, skor maks 100). Kolom Bloom berisi level dominan butir.

---

## Catatan untuk Dosen

1. **Penandaan Sub-CPMK** mengikuti bawaan sementara D-03(a) (76/12/12). Bila D-03 diputuskan lain, ubah kolom Sub-CPMK saja.
2. **Level di atas rentang registri.** 33 poin bertanda 091-1 berada di C5–C6 (registri C2–C4), terutama Bagian B (16 poin: B2(a), B2(c), B3(b)) dan Bagian C (14 poin: C1(a), C1(b)), ditambah A3(b) 3 poin; UAI32-1 (registri C6) hanya diukur pada C3–C5 di UTS, sedangkan C6-nya pada UAS. Bahan laporan `T2-08`. Baris Bloom "C2–C4" pada tabel Informasi Modul 8 belum diubah; pembahasan §1.4 menjelaskannya kepada mahasiswa.
3. **Bentuk C1.** Wawancara lanjutan untuk menguji dugaan, bukan wawancara pertama lima bagian seperti contoh kisi-kisi C1; tetap "menyusun naskah wawancara" (kisi-kisi §3).
4. **Waktu.** Model (belum diuji) memberi 72,1 / 85,6 / 100,6 menit (cepat / tengah / lambat), sesudah cadangan (i)–(ii) diterapkan; bila waktu berpikir 1,5× asumsi, skenario tengah ±93,8 menit. Penentunya uji coba berwaktu ([prosedur mutu](#4-prosedur-mutu-varian) butir 4): median ≤ 60 menit lolos; > 60 dan ≤ 67,5 menit bersyarat (cadangan pertama (iii), A4 dua kutipan); > 67,5 menit pemangkasan lanjutan oleh dosen. Cadangan (iii) hanya menghemat ±1,0 menit, sehingga hasil bersyarat di atas ±60,6 menit juga memerlukan kandidat (iv)–(vii) ([§5](#5-cadangan-pemangkasan-waktu)); bersama (viii) — paling akhir karena menghapus satu-satunya butir literasi AI — seluruh cadangan menutup median sampai ±63 menit, dan di atasnya diperlukan pengurangan butir lewat revisi kisi-kisi. Urutan cadangan ini usulan penyusun; sebaiknya dosen menetapkannya **sebelum** uji coba, agar hasilnya dapat langsung diterapkan.
5. **Perbedaan bahan ajar** yang sudah ditangani pedoman skor: pembuka wawancara Bab 2 §2.2.1 vs §2.2.2 (dipakai §2.2.2); rumus LTV Bab 7 vs Modul 7 (setara, keduanya di Lembar Rumus); "tingkat keyakinan" Bab 6 §6.3.1 vs "kekuatan bukti" A5 (setara). Modul 8 §8.6 menggambarkan Bagian B tanpa *unit economics*; B4 mengikuti tabel porsi kisi-kisi §2.
6. **Rujukan ayat.** Latihan merujuk QS An-Nisa' (4): 58 dengan parafrase pesannya, tanpa kutipan terjemahan, karena teks terjemahan resmi Kemenag belum terverifikasi. Bila varian mengutip terjemahannya, salin dari laman resmi quran.kemenag.go.id atau mushaf terbitan Kemenag.
7. **Sebaran kunci varian** (mis. jumlah ranah/solusi, kategori Kano, arah keputusan B4) dicatat pada lembar invarian privat, tidak di berkas publik ini.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
