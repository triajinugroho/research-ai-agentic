---
id: uai-if52510033-latihan-uas-cetak-biru
tipe: asesmen
judul: "Latihan UAS — Probabilitas dan Statistik — Cetak Biru Butir dan Panduan Varian"
kode_mk: IF52510033
nama_mk: Probabilitas dan Statistik
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-09
---

# Cetak Biru Butir dan Panduan Varian — Latihan UAS Probabilitas dan Statistik

## Probabilitas dan Statistik — IF52510033

> **Latihan UAS — bukan naskah UAS.** Cetak biru ini menyertai simulasi lengkap UAS Probabilitas dan Statistik Ganjil 2026/2027 untuk berlatih: komposisi, durasi (120 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UAS. Naskah UAS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> Berkas ini untuk dosen dan penelaah: tabel butir, ringkasan per Sub-CPMK/Bloom/bagian/minggu, model waktu dan uji coba berwaktu, pemeriksaan orisinalitas, serta [panduan menyusun varian](#panduan-menyusun-varian-naskah-uas-sebenarnya). Pasangan berkas: [latihan UAS](latihan-uas.md) dan [pembahasan dan pedoman skor](latihan-uas-pembahasan.md).

---

## Identitas dan Dasar Penyusunan

| Komponen | Isi |
|---|---|
| Mata kuliah | Probabilitas dan Statistik (IF52510033), semester 1 |
| Asesmen | Latihan UAS (simulasi) untuk UAS Semester Ganjil 2026/2027, Minggu 16 — UAS berbobot 25% nilai akhir |
| Penyusun | Tri Aji Nugroho, S.T., M.T. |
| Butir kendali | [KENDALI-EKSEKUSI](../../../00-meta/KENDALI-EKSEKUSI.md): `T1-10` (naskah UAS + kunci = varian privat dari latihan ini, termasuk uji coba berwaktu); telaah sejawat dan uji coba berwaktu mengikuti pola `T0-15`; ketentuan skor tambahan berstatus usulan seperti `T0-18` |
| Acuan | [Kisi-kisi UAS](kisi-kisi-uas.md) §1–§8, [RPS Minggu 16](../01-rps/rps-probabilitas-dan-statistik.md#minggu-16-ujian-akhir-semester-uas), [RTM §F.2](../02-rtm/rtm-probabilitas-dan-statistik.md#f2-ujian-akhir-semester-u-02), registri [`15b-subcpmk-tingkat-1-semester-1-2.md`](../../../00-kurikulum-if-2025-revisi-2026/15b-subcpmk-tingkat-1-semester-1-2.md) |
| Sub-CPMK registri | `PS-Sub-CPMK081-1` (CPL08/CPMK081, C3–C4): probabilitas, peubah acak, distribusi, estimasi, inferensi. `PS-Sub-CPMK102-1` (CPL10/CPMK102, C3–C4/P2–P3): statistika deskriptif dan inferensial, visualisasi |
| Penandaan | Penandaan Sub-CPMK per butir menurut isi adalah bawaan sementara D-03(a); bobot nilai akhir UAS tetap tercatat sesuai alokasi registri dan RPS (UAS 25% → `PS-Sub-CPMK081-1`). |

**Aturan penandaan.** Mengikuti indikator mingguan [RPS §F](../01-rps/rps-probabilitas-dan-statistik.md#f-indikator-capaian-mingguan): butir tentang Minggu 1–3 (data, deskriptif, visualisasi) dan Minggu 12–14 (uji dua sampel, ANOVA, chi-square, korelasi–regresi) → `PS-Sub-CPMK102-1`; butir tentang Minggu 4–7 dan 9–11 (probabilitas, Bayes, distribusi, sampling, estimasi, uji satu sampel) → `PS-Sub-CPMK081-1`. Sub-butir D dan C ditandai sendiri-sendiri. Lembar latihan hanya mencantumkan level Bloom dan skor; Sub-CPMK per butir tercantum di pembahasan dan di berkas ini.

---

## Kesesuaian dengan Kisi-Kisi

### Komposisi, skor, dan waktu

| Bagian | Bentuk | Butir (kisi-kisi → latihan) | Skor (kisi-kisi → latihan) | Bloom kisi-kisi | Bloom latihan | Waktu saran kisi-kisi | Model waktu (135 kpm) |
|---|---|---|---|---|---|---|---|
| A | Pilihan ganda | 15 → 15 | 15 → 15 | C2–C3 | 8 butir C2, 7 butir C3 | 15 menit | 15,25 menit |
| B | Isian / hitungan pendek | 10 → 10 | 20 → 20 | C3 | 10 butir C3 | 25 menit | 20,5 menit |
| C | Uraian terstruktur | 5 → 5 | 40 → 40 | C3–C4 | 5 butir C3–C4 (sub-butir C3: 29 poin; C4: 11 poin) | 50 menit | 46,75 menit |
| D | Studi kasus terpadu | 1 → 1 | 25 → 25 | C4 | 1 butir C4 (sub-butir C3: 9 poin; C4: 16 poin) | 25 menit | 24,5 menit |
| **Total** | | **31 → 31** | **100 → 100** | | | **115 menit** | **107 menit** |

Bentuk Bagian D mengikuti [kisi-kisi §5](kisi-kisi-uas.md#5-bentuk-soal-studi-kasus-terpadu-bagian-d--25) butir demi butir: D1–D8 = butir 1–8, dengan skor sama dengan bobotnya (2/3/4/4/4/3/3/2). Aturan alat bantu sama dengan kisi-kisi §1, RPS Minggu 16, dan RTM §F.2: *closed book*; kalkulator ilmiah *non-programmable* dan alat tulis; tabel Normal baku, t, chi-square, dan F dibagikan pengawas; rumus tidak disediakan (tanpa lembar rumus); AI dilarang. Butir yang memerlukan tabel Normal: B5(b), B7(a), C4(b)–(d); tabel-t: B8, D5, D6; tabel F: A14. Tabel chi-square dibagikan tetapi tidak diperlukan (A15 hanya memeriksa syarat). Nilai t untuk derajat bebas 48 (A12) tidak ada di tabel sehingga dicetak di soal. Untuk berlatih mandiri, Lampiran A.1–A.5 buku ajar memuat semua nilai tabel yang diperlukan; tabel korelasi A.6 tidak dibagikan saat UAS dan tidak dipakai. Nilai antara yang dicetak di soal untuk menghemat waktu: Σ(x − x̄)² pada C4, P(X = 4) pada C3, dan P(ditandai) pada C1(b).

### Model waktu

Model per butir (taksiran penyusun): **kata soal ÷ 120–150 kata per menit** (membaca saat mengerjakan) **+ kata jawaban minimal bernilai penuh ÷ ±20 kata per menit** (menulis tangan, termasuk angka dan notasi) **+ waktu berpikir** (membaca tabel dan grafik, menghitung dengan kalkulator, memilih metode). Kata dihitung sebagai token yang memuat huruf atau angka; grafik ASCII tidak dihitung sebagai kata — waktu membacanya masuk kolom *Berpikir* C5(a) dan C5(c). Jawaban minimal bernilai penuh diukur dari contoh *Baik* di pembahasan (Bagian C dan D) dan dari jawaban ringkas berlangkah (Bagian B); Bagian A hanya membaca dan berpikir. Waktu berpikir: PG 0,25–1 menit (1 menit untuk A14 dan A15, yang memerlukan hitungan dan tabel); hitungan ringan atau analisis 0,5 menit; hitungan kalkulator berlangkah banyak 0,75–1 menit per butir B atau sub-butir C/D.

| Bagian | Kata soal | Membaca (120–150 kpm) | Kata jawaban | Menulis (20 kpm) | Berpikir | Waktu kerja |
|---|---|---|---|---|---|---|
| A | 1.099 | 7,3–9,2 menit | — | — | 7 menit | 14,3–16,2 menit |
| B | 613 | 4,1–5,1 menit | 189 | 9,5 menit | 6,5 menit | 20–21,1 menit |
| C | 1.038 | 6,9–8,7 menit | 520 | 26 menit | 13 menit | 45,9–47,7 menit |
| D | 503 | 3,4–4,2 menit | 322 | 16,1 menit | 4,75 menit | 24,2–25 menit |
| **Total** | **3.253** | **21,7–27,1 menit** | **1.031** | **51,6 menit** | **31,25 menit** | **±104,5–110 menit** |

Ditambah **5 menit membaca** seluruh soal di awal dan **sedikitnya 5 menit memeriksa** di akhir, total **±114,5–120 menit**: muat dalam 120 menit, tetapi **tanpa margin** pada kecepatan baca terendah. Setiap bagian muat dalam waktu saran kisi-kisi §2, kecuali Bagian A pada kecepatan baca terendah (16,2 vs 15 menit); selisihnya tertutup oleh Bagian B yang lebih cepat dari waktu sarannya. Taksiran penyusun cenderung lebih rendah daripada waktu mahasiswa — pada Latihan UTS, taksiran independen ±10% lebih tinggi; dengan koreksi itu waktu kerja menjadi ±115–121 menit, sehingga bersama membaca dan memeriksa, 120 menit bisa tidak cukup. Karena itu latihan menyatakan secara terbuka bahwa panjangnya masih dikalibrasi (Petunjuk 5), dan panjang naskah UAS diputuskan dari **uji coba berwaktu** sebelum varian ditetapkan ([prosedur mutu varian](#4-prosedur-mutu-varian) no. 3), dengan [cadangan pemangkasan](#cadangan-pemangkasan-waktu) yang sudah disiapkan.

### Cadangan pemangkasan waktu

Empat pemangkasan sudah diterapkan pada latihan ini tanpa mengubah Sub-CPMK, level Bloom, atau skor setiap baris: Σ(x − x̄)² dicetak pada C4(a), P(X = 4) dicetak pada C3, P(ditandai) dicetak pada C1(b), dan batas kalimat D3 dan D4 diturunkan dari 4 menjadi 3. Cadangan di bawah dipakai menurut hasil uji coba berwaktu; pemangkasan yang dipakai diterapkan sama pada latihan, pembahasan, dan cetak biru (kunci, Tabel Butir, peta aspek), lalu pada varian.

**Cadangan pertama** — diterapkan bila hasil uji coba **bersyarat**; perlu disetujui dosen **sebelum** uji coba. Setiap pemangkasan menjaga Sub-CPMK, level Bloom, dan skor setiap baris [Tabel Butir](#tabel-butir); poin hanya dipindahkan di dalam baris yang sama, dan total aspek Bagian C tidak berubah. Angka hemat adalah taksiran penyusun dalam menit kerja mahasiswa.

| No | Pemangkasan | Pemindahan poin (skor baris tetap) | Hemat |
|---|---|---|---|
| 1 | D2: t Welch pembanding (1,42) dicetak; mahasiswa memilih rancangan, memberi alasan, dan menjelaskan mengapa t Welch kecil | Hitung 0,75 pindah ke penjelasan (interpretasi 1,75) | 0,5–0,75 |
| 2 | C1(c): prevalensi lampiran yang dipindai (0,0170) dicetak; mahasiswa tetap menghitung PPV dan porsi tak terpindai | Rumus prevalensi 0,25 pindah ke rumus porsi tak terpindai (0,5) | 0,5–0,75 |
| 3 | A15: frekuensi harapan baris Ponsel dicetak | — | 0,25–0,5 |
| 4 | B3(b): keandalan bila replika ditambah di tingkat web (0,9899) dicetak; mahasiswa menghitung alternatif basis data dan memutuskan | Tidak berubah | 0,25–0,5 |
| 5 | Batas kalimat C1(c), C3(c), C5(a), dan C5(d) diturunkan dari 3 menjadi 2 kalimat | Tidak berubah | 1–1,5 |
| | **Total** | | **±2,5–4** |

Dengan dasar penguji coba ±1,5× lebih cepat daripada rerata mahasiswa, hemat ini setara ±1,7–2,7 menit penguji coba, sehingga cadangan pertama hanya cukup untuk median uji coba sampai **±82 menit**. Di atasnya dosen juga menetapkan pemangkasan lanjutan, lalu uji ulang.

**Pemangkasan lanjutan** — bila median > 90 menit, atau bila hasil bersyarat melampaui cakupan cadangan pertama; ditetapkan dosen, lalu uji ulang. Pilihannya mengubah peta skor atau Bloom sub-butir dan diterapkan sama pada ketiga berkas, mis.: C4(d) tanpa pernyataan teknisi (0,5 poin C4 dipindah ke analisis pada C4(c) atau C4(b)); C1(c) dengan porsi malware tak terpindai dicetak; satu sub-butir C dihapus dan skornya dipindah ke sub-butir lain pada butir yang sama; atau pengurangan butir lewat revisi kisi-kisi §2 (mis. Bagian B menjadi 8 butir bernilai 2,5).

### Sebaran materi (kisi-kisi §3)

| Pokok bahasan | Minggu | Target | A | B | C | D | Total latihan |
|---|---|---|---|---|---|---|---|
| Statistika deskriptif dan visualisasi | 2–3 (D1 dan D8 juga memuat Mg 1) | 8 | – | – | 4 | 4 | **8** |
| Probabilitas dasar dan pencacahan | 4 | 12 | 2 | 4 | 6 | – | **12** |
| Teorema Bayes dan kebebasan | 5 | 14 | 2 | 2 | 10 | – | **14** |
| Distribusi diskret | 6 | 10 | 2 | 2 | 6 | – | **10** |
| Distribusi kontinu dan Normal | 7 | 12 | 2 | 4 | 6 | – | **12** |
| Distribusi sampling dan CLT | 9 | 10 | 2 | 2 | 2 | 4 | **10** |
| Estimasi dan interval kepercayaan | 10 | 12 | 3 | 6 | – | 3 | **12** |
| Uji hipotesis satu dan dua sampel | 11–12 | 14 | – | – | – | 14 | **14** |
| ANOVA, chi-square, korelasi–regresi | 13–14 | 8 | 2 | – | 6 | – | **8** |
| **Total** | | **100** | **15** | **20** | **40** | **25** | **100** |

Total per pokok bahasan sama dengan §3 **menurut konvensi penandaan butir utuh**: setiap butir atau sub-butir ditandai satu minggu menurut indikator utamanya. Catatan §3 untuk deskriptif ("diuji sebagai bagian dari kasus, bukan soal tersendiri") dipatuhi: poinnya ada pada C4(a), C5(a), D1, dan D8. Kerangka D di §5 adalah satu kasus uji dua sampel, sehingga butir 2, 3, 5, dan 7 (14 poin) sudah menghabiskan bobot uji hipotesis §3; karena itu A–C tidak memuat butir Minggu 11–12, sedangkan D4 (asumsi dan kecukupan n menurut Teorema Limit Pusat), D6 (interval kepercayaan), dan D8 (batas inferensi dari rancangan studi) ditandai Minggu 9, 10, dan 1. **Menurut isi**, D4 memuat 1,5 poin Teorema Limit Pusat (Minggu 9) dan 2,5 poin asumsi uji-t berpasangan (indikator §4.7, Minggu 11–12); bila D4 dibagi menurut isi, porsi uji hipotesis menjadi ±16,5 poin dan Minggu 9 ±7,5 poin. Ketegangan §3–§5 ini dicatat untuk dosen ([Catatan untuk Dosen](#catatan-untuk-dosen) no. 2).

### Cakupan indikator kisi-kisi §4

| Subbagian | Indikator yang diuji (butir) | Indikator yang tidak diuji di latihan ini |
|---|---|---|
| 4.1 Probabilitas dasar | penjumlahan/perkalian/komplemen (A2, B2, C2c); bersyarat dan arahnya (A1, B2, C1c); permutasi dan kombinasi (B1, C2a); perkalian tanpa pengembalian (A2, C2b) | — |
| 4.2 Bayes dan kebebasan | probabilitas total pada partisi tiga keadaan dan empat komponen Bayes (C1a); *base rate fallacy*, PPV, NPV (C1b); prevalensi subkelompok dan kebijakan penyaringan (C1c); spesifisitas pada prevalensi rendah (A4); saling lepas vs bebas (A3, C2d); keandalan seri–paralel (B3) | risiko asumsi kebebasan yang keliru pada keandalan (sudah diuji Latihan UTS C4) |
| 4.3 Distribusi diskret | BINS (A5); E dan Var Binomial (A6); Poisson dan hampirannya (B4, C3a); memilih distribusi (A5, B4); kapasitas berbasis kuantil dari target layanan (C3b) | Geometrik (sudah diuji Latihan UTS B6); tanda *overdispersion* varians ≫ mean (sudah diuji Latihan UTS D3; jawaban C3(c) hanya menyinggungnya dalam catatan yang tidak dinilai) |
| 4.4 Kontinu dan Normal | P(X = x) = 0 (A7); Eksponensial dan tanpa memori (C3d); skor-z dan tabel (B5, C4b); aturan empiris (B5a); x dari persentil (C4c); kenormalan dari Q-Q plot/kemencengan (A8, C4b) | — |
| 4.5 Sampling dan CLT | sebaran data vs x̄, galat baku vs simpangan baku (A9, B7); hukum akar n (B7b); isi dan batas TLP, kecukupan n (A10, B7a, D4); simpangan baku jumlah (C4d) | — |
| 4.6 Estimasi | sifat estimator (A13); IK rata-rata dengan t, termasuk mengenali kekeliruan memakai z bila σ tidak diketahui (B8, D6); IK proporsi dan syaratnya, serta memakai IK untuk menilai klaim (B9); tafsir 95% (A11, D6); margin dan ukuran sampel (B10); lebar vs tingkat kepercayaan (A12) | IK dengan z bila σ diketahui |
| 4.7 Uji hipotesis | H₀/H₁ dan arah, arah sebelum data, galat Tipe I/II (D3); uji-t berpasangan dan Welch (D2, D5); asumsi dan cara memeriksanya (D4); bebas vs berpasangan (D2); tafsir *p-value* (D5); signifikansi statistik vs praktis dan Cohen's d (D7) | uji-t satu sampel atas data mentah (uji berpasangan adalah uji-t satu sampel atas selisih) |
| 4.8 ANOVA, chi-square, korelasi–regresi | tabel ANOVA, F, η², "bukan setiap pasangan berbeda" (A14); syarat frekuensi harapan (A15); koefisien regresi dan R² tanpa sebab-akibat (C5b–d); asumsi LINE dari plot residual, termasuk mengenali plot tanpa pelanggaran (C5c); ekstrapolasi (C5d) | menghitung inflasi galat Tipe I; mengapa uji lanjut hanya dilakukan setelah ANOVA signifikan (A14 hanya menguji bahwa ANOVA tidak menunjuk pasangan); menghitung statistik χ²; Pearson vs Spearman (hanya catatan tidak dinilai di pembahasan C5) |

Indikator yang tidak diuji tidak dirotasi ke varian — varian memakai cetak biru yang sama. Rotasi dilakukan bila latihan berikutnya disusun ulang.

---

## Tabel Butir

Kolom *Indikator* merujuk subbagian kisi-kisi §4 (4.1–4.8) dan kerangka D di §5. Waktu dalam menit (model waktu pada 135 kata per menit; pembulatan per butir ke 0,25 menit mengikuti total per bagian).

| No | Indikator (kisi-kisi) | Mg | Sub-CPMK | Bloom | Skor | Waktu |
|---|---|---|---|---|---|---|
| A1 | 4.1 Membedakan arah persyaratan pada klaim laporan | 4 | PS-Sub-CPMK081-1 | C2 | 1 | 1 |
| A2 | 4.1 Aturan perkalian tanpa pengembalian | 4 | PS-Sub-CPMK081-1 | C3 | 1 | 0,75 |
| A3 | 4.2 Saling lepas vs saling bebas | 5 | PS-Sub-CPMK081-1 | C2 | 1 | 1,25 |
| A4 | 4.2 Mengapa spesifisitas lebih berpengaruh pada prevalensi rendah | 5 | PS-Sub-CPMK081-1 | C2 | 1 | 1 |
| A5 | 4.3 Memeriksa BINS; memilih distribusi | 6 | PS-Sub-CPMK081-1 | C3 | 1 | 0,75 |
| A6 | 4.3 E[X] dan SD Binomial | 6 | PS-Sub-CPMK081-1 | C3 | 1 | 0,75 |
| A7 | 4.4 P(X = x) = 0 dan cara membaca PDF | 7 | PS-Sub-CPMK081-1 | C2 | 1 | 0,75 |
| A8 | 4.4 Menilai kenormalan dari Q-Q plot dan kemencengan | 7 | PS-Sub-CPMK081-1 | C2 | 1 | 0,75 |
| A9 | 4.5 Galat baku vs simpangan baku | 9 | PS-Sub-CPMK081-1 | C3 | 1 | 1 |
| A10 | 4.5 Batas keberlakuan TLP; n memadai untuk bentuk populasi | 9 | PS-Sub-CPMK081-1 | C2 | 1 | 1 |
| A11 | 4.6 Tafsir "95% kepercayaan" | 10 | PS-Sub-CPMK081-1 | C2 | 1 | 0,75 |
| A12 | 4.6 Interval lebih lebar bila tingkat kepercayaan naik (hitung IK 99% dari IK 95%) | 10 | PS-Sub-CPMK081-1 | C3 | 1 | 1,25 |
| A13 | 4.6 Sifat estimator (tak bias) | 10 | PS-Sub-CPMK081-1 | C2 | 1 | 0,75 |
| A14 | 4.8 Membaca tabel ANOVA; F, η²; ANOVA tidak menunjuk pasangan | 13 | PS-Sub-CPMK102-1 | C3 | 1 | 1,75 |
| A15 | 4.8 Syarat frekuensi harapan ≥ 5 | 13 | PS-Sub-CPMK102-1 | C3 | 1 | 1,75 |
| B1 | 4.1 Permutasi dengan alasan; peluang dari pencacahan | 4 | PS-Sub-CPMK081-1 | C3 | 2 | 1,75 |
| B2 | 4.1 Aturan perkalian, penjumlahan umum, dan arah persyaratan | 4 | PS-Sub-CPMK081-1 | C3 | 2 | 2,5 |
| B3 | 4.2 Keandalan seri–paralel; keputusan penempatan replika | 5 | PS-Sub-CPMK081-1 | C3 | 2 | 2,5 |
| B4 | 4.3 Hampiran Poisson untuk Binomial | 6 | PS-Sub-CPMK081-1 | C3 | 2 | 1,75 |
| B5 | 4.4 Aturan empiris; skor-z dan tabel Normal | 7 | PS-Sub-CPMK081-1 | C3 | 2 | 1,75 |
| B6 | 4.4 Membaca PDF sebagai luas (Uniform kontinu) | 7 | PS-Sub-CPMK081-1 | C3 | 2 | 1,5 |
| B7 | 4.5 Galat baku, TLP untuk P(x̄ > a), hukum akar n | 9 | PS-Sub-CPMK081-1 | C3 | 2 | 2 |
| B8 | 4.6 IK rata-rata: mengenali kekeliruan memakai z, lalu IK dengan t | 10 | PS-Sub-CPMK081-1 | C3 | 2 | 2,5 |
| B9 | 4.6 IK proporsi dan syaratnya; memakai IK untuk menilai klaim | 10 | PS-Sub-CPMK081-1 | C3 | 2 | 2,25 |
| B10 | 4.6 Margin galat proporsi dari n; ukuran sampel untuk margin tertentu | 10 | PS-Sub-CPMK081-1 | C3 | 2 | 2 |
| C1a | 4.2 Probabilitas total (tiga keadaan); Bayes dengan empat komponen; asumsi dan tafsir (diminta) | 5 | PS-Sub-CPMK081-1 | C3 | 3 | 3,25 |
| C1b | 4.2 *Base rate fallacy*; PPV dan NPV; asumsi sensitivitas/spesifisitas (diminta) | 5 | PS-Sub-CPMK081-1 | C3 | 2,5 | 2,5 |
| C1c | 4.2 Prevalensi subkelompok (probabilitas bersyarat) dan kebijakan penyaringan; analisis dengan angka (≤ 3 kalimat) | 5 | PS-Sub-CPMK081-1 | C4 | 2,5 | 3,75 |
| C2a | 4.1 Permutasi vs kombinasi dengan alasan | 4 | PS-Sub-CPMK081-1 | C3 | 2 | 2 |
| C2b | 4.1 Peluang dari pencacahan/aturan perkalian bersyarat; asumsi undian (diminta) | 4 | PS-Sub-CPMK081-1 | C3 | 2 | 2,5 |
| C2c | 4.1 Aturan penjumlahan umum; memeriksa saling lepas (diminta) | 4 | PS-Sub-CPMK081-1 | C3 | 2 | 1,5 |
| C2d | 4.2 Uji kebebasan dengan definisi formal (≤ 2 kalimat) | 5 | PS-Sub-CPMK081-1 | C4 | 2 | 2 |
| C3a | 4.3 Poisson: parameter, asumsi (diminta), PMF | 6 | PS-Sub-CPMK081-1 | C3 | 2 | 1,75 |
| C3b | 4.3 Kapasitas berbasis kuantil dari target layanan dalam satuan waktu; keputusan (diminta) | 6 | PS-Sub-CPMK081-1 | C3 | 2 | 2,75 |
| C3c | 4.3 Analisis kapasitas = rata-rata; asumsi Poisson yang dilanggar (≤ 3 kalimat) | 6 | PS-Sub-CPMK081-1 | C4 | 2 | 2,5 |
| C3d | 4.4 Eksponensial; peluang bersyarat dengan sifat tanpa memori dan maknanya (diminta) | 7 | PS-Sub-CPMK081-1 | C3 | 2 | 2,25 |
| C4a | Deskriptif dalam kasus: x̄, s, alasan penyebut (diminta) | 2 | PS-Sub-CPMK102-1 | C3 | 2 | 2 |
| C4b | 4.4 Ekor kanan Normal dan tafsirnya; asumsi kenormalan diperiksa dengan data (diminta) | 7 | PS-Sub-CPMK081-1 | C3 | 2 | 2,25 |
| C4c | 4.4 x dari persentil; tafsir (diminta) | 7 | PS-Sub-CPMK081-1 | C3 | 2 | 1,75 |
| C4d | 4.5 Distribusi jumlah/rata-rata n server (SE); asumsi (diminta) — C3, 1,5 poin; analisis klaim "16 × batas" (≤ 2 kalimat) — C4, 0,5 poin | 9 | PS-Sub-CPMK081-1 | C3–C4 | 2 | 3 |
| C5a | Visualisasi dalam kasus: membaca diagram pencar, titik berpengaruh, syarat memisahkannya (≤ 3 kalimat) | 3 | PS-Sub-CPMK102-1 | C3 | 2 | 3,5 |
| C5b | 4.8 Koefisien regresi dari ringkasan; prediksi | 14 | PS-Sub-CPMK102-1 | C3 | 2 | 1,5 |
| C5c | 4.8 R² dan tafsirnya; asumsi LINE dari dua plot residual (satu melanggar, satu tidak) | 14 | PS-Sub-CPMK102-1 | C4 | 2 | 2,75 |
| C5d | 4.8 Korelasi bukan sebab-akibat; ekstrapolasi dengan prediksi di luar rentang; tafsir kemiringan asosiatif (≤ 3 kalimat) | 14 | PS-Sub-CPMK102-1 | C4 | 2 | 3,25 |
| D1 | §5 butir 1 — skala variabel; mengenali ringkasan yang tidak sah dan menggantinya | 1–2 | PS-Sub-CPMK102-1 | C3 | 2 | 3,75 |
| D2 | §5 butir 2 — berpasangan atau bebas; t Welch pembanding (≤ 3 kalimat) | 12 | PS-Sub-CPMK102-1 | C4 | 3 | 3 |
| D3 | §5 butir 3 — H₀/H₁, analisis arah, α dari konsekuensi galat (≤ 3 kalimat) | 11 | PS-Sub-CPMK081-1 | C4 | 4 | 4 |
| D4 | §5 butir 4 — asumsi dan cara memeriksanya; kecukupan n menurut TLP (≤ 3 kalimat) | 9 | PS-Sub-CPMK081-1 | C4 | 4 | 3,5 |
| D5 | §5 butir 5 — statistik uji-t berpasangan, batas *p-value*, keputusan, tafsir | 12 | PS-Sub-CPMK102-1 | C3 | 4 | 2,75 |
| D6 | §5 butir 6 — IK 95% selisih dan tafsirnya | 10 | PS-Sub-CPMK081-1 | C3 | 3 | 2 |
| D7 | §5 butir 7 — Cohen's d; kebermaknaan praktis dengan IK (≤ 3 kalimat) | 11 | PS-Sub-CPMK081-1 | C4 | 3 | 2,75 |
| D8 | §5 butir 8 — analisis klaim yang melampaui rancangan studi dan rumusan yang didukung data (≤ 2 kalimat) | 1 | PS-Sub-CPMK102-1 | C4 | 2 | 2,75 |
| | **Total** | | | | **100** | **107** |

Level Bloom butir utuh: A dan B sesuai baris; C1–C5 = C3–C4; D = C4. Tidak ada butir C1 murni ("sebutkan"); kedelapan butir C2 berada di Bagian A, sesuai rentang C2–C3 kisi-kisi. Kata kerja **utama** setiap perintah mengikuti taksonomi repositori ([`16-taksonomi-bloom-cap.md`](../../../00-kurikulum-if-2025-revisi-2026/16-taksonomi-bloom-cap.md), [`taksonomi-cap.md`](../../../00-pedoman-obe/taksonomi-cap.md)): butir dan sub-butir C3 menuntut penerapan — perintahnya dipimpin "hitung" (KKO C3) atau pertanyaan "berapa …" yang menuntut hitungan, dan D6 memakai "hitung interval kepercayaan", bukan "susun" (KKO C6 di registri). "Menilai" (C5) tidak dipakai — butir 7 kisi-kisi §5 ("menilai kebermaknaan praktisnya") dirumuskan sebagai "analisis" di D7 — dan butir 3 kisi-kisi §5 ("merumuskan H₀ dan H₁"; "merumuskan" adalah KKO C6 di tabel utama registri) dirumuskan di D3 sebagai "nyatakan H₀ dan H₁ … analisis arah uji … pilih α dengan menghubungkannya …". Sub-butir C4 dipimpin "analisis" (C1(c), C3(c), C4(d), C5(d), D3, D4, D7, D8), "uji" (C2(d)), atau pertanyaan analitis yang menuntut penguraian hubungan: C5(c) memilah plot residual yang melanggar asumsi LINE dari yang tidak, D2 rancangan dan akibat uji yang keliru. Kata kerja pendukung seperti "sebutkan", "tuliskan", atau "nyatakan" (KKO C1) hanya muncul sebagai langkah di dalam perintah yang level utamanya lebih tinggi (mis. "tuliskan parameter … lalu hitung" di C3(a), "sebutkan asumsi" di C1(a) dan D4). Varian mempertahankan bentuk perintah ini.

---

## Ringkasan per Sub-CPMK, Bloom, dan Bagian

### Skor per Sub-CPMK

| Sub-CPMK | A | B | C | D | **Total skor** | **% skor UAS** | Butir |
|---|---|---|---|---|---|---|---|
| `PS-Sub-CPMK081-1` | 13 | 20 | 30 | 14 | **77** | **77%** | A1–A13, B1–B10, C1, C2, C3, C4(b)–(d), D3, D4, D6, D7 |
| `PS-Sub-CPMK102-1` | 2 | – | 10 | 11 | **23** | **23%** | A14, A15, C4(a), C5, D1, D2, D5, D8 |
| **Total** | 15 | 20 | 40 | 25 | **100** | **100%** | |

### Skor per level Bloom

| Bloom | `PS-Sub-CPMK081-1` | `PS-Sub-CPMK102-1` | Total skor | % |
|---|---|---|---|---|
| C2 | 8 | – | 8 | 8% |
| C3 | 51 | 14 | 65 | 65% |
| C4 | 18 | 9 | 27 | 27% |
| **Total** | **77** | **23** | **100** | **100%** |

### Skor per bagian dan level Bloom

| Bagian | C2 | C3 | C4 | Total |
|---|---|---|---|---|
| A | 8 | 7 | – | 15 |
| B | – | 20 | – | 20 |
| C | – | 29 | 11 | 40 |
| D | – | 9 | 16 | 25 |
| **Total** | **8** | **65** | **27** | **100** |

- Butir utuh ≥ C3: **23 dari 31 (74%)**; skor ≥ C3: **92%**.
- Rentang Bloom kedua Sub-CPMK (C3–C4) terwakili: skor C4 untuk `PS-Sub-CPMK081-1` = 18 dari 77 (23%), untuk `PS-Sub-CPMK102-1` = 9 dari 23 (39%). Dibanding Latihan UTS (C4 = 22%), porsi C4 naik menjadi 27%.

### Cara menghitung ketercapaian (agregat)

Untuk setiap mahasiswa: ketercapaian 081-1 (%) = (Σ skor butir bertanda 081-1)/77 × 100; ketercapaian 102-1 (%) = (Σ skor butir bertanda 102-1)/23 × 100. Untuk `mutu/02` dan laporan PPEPP, yang dicatat di repositori hanya **angka agregat per kelas**: rata-rata dan median ketercapaian per Sub-CPMK, persentase mahasiswa di atas ambang, rata-rata skor per butir (tingkat kesukaran), dan daya beda per butir. Ambang ketercapaian belum ditetapkan (menunggu `T1-17` dan dokumen `F-03`). Skor per mahasiswa tidak dicatat di repositori.

Registri mengalokasikan seluruh UAS (25% nilai akhir) ke `PS-Sub-CPMK081-1`, sedangkan menurut isi butir 23% skor mengukur `PS-Sub-CPMK102-1` (Minggu 1–3 dan 12–14). Dengan penandaan per butir, nilai akhir tetap memakai bobot registri, tetapi UAS menyumbang bukti ketercapaian untuk **kedua** Sub-CPMK; usulan revisi alokasi dicatat untuk tim kurikulum (`T2-08`).

---

## Matriks Sub-CPMK × Minggu × Bagian (skor)

| Minggu | Sub-CPMK | A | B | C | D | Total |
|---|---|---|---|---|---|---|
| 1–3 | 102-1 | – | – | 4 | 4 | 8 |
| 4 | 081-1 | 2 | 4 | 6 | – | 12 |
| 5 | 081-1 | 2 | 2 | 10 | – | 14 |
| 6 | 081-1 | 2 | 2 | 6 | – | 10 |
| 7 | 081-1 | 2 | 4 | 6 | – | 12 |
| 9 | 081-1 | 2 | 2 | 2 | 4 | 10 |
| 10 | 081-1 | 3 | 6 | – | 3 | 12 |
| 11 | 081-1 | – | – | – | 7 | 7 |
| 12 | 102-1 | – | – | – | 7 | 7 |
| 13 | 102-1 | 2 | – | – | – | 2 |
| 14 | 102-1 | – | – | 6 | – | 6 |
| **Total** | | **15** | **20** | **40** | **25** | **100** |

---

## Kemiripan dengan Sumber Terbuka

Pemeriksaan orisinalitas terhadap tiga **sumber terlarang** — Latihan Soal Bab 1–14 buku ajar (tingkat Dasar, Menengah, Mahir), contoh soal kisi-kisi UAS (kerangka §5 dan contoh §11), dan [Latihan UTS](latihan-uts.md) — serta contoh di dalam bab dan modul Minggu 1–14. Tidak ada butir yang memakai ulang teks atau angka sumber tersebut. Beberapa butir menguji indikator yang sama dengan sumber terdekat; untuk indikator yang langkah hitungnya baku (mis. probabilitas total lalu posterior di C1(a), interval-t di B8), langkahnya memang sama, sehingga butir itu dibedakan dari sumber terdekat oleh **bentuk pertanyaannya**, bukan hanya konteks dan angkanya (kolom *Pembeda*). Varian wajib menjaga jarak yang sama dari sumber ini **dan** dari latihan ini.

| Butir | Sumber terdekat | Pembeda |
|---|---|---|
| A1 | Bab 4 L9 (contoh P(A\|B) ≠ P(B\|A) buatan sendiri); Latihan UTS C2(c) (laju vs porsi) | Klaim laporan keamanan tanpa tabel; PG dengan pengecoh komplemen |
| A2 | Bab 4 L8 (3 tiket dari 20 tanpa pengembalian, dibandingkan dengan pengembalian) | PG 2 dari 8 *flashdisk* dengan pengecoh "dengan pengembalian" dan "penyebut tidak dikurangi" |
| A3 | Bab 5 L4, L8; Bab 5 §5.4.2 (materi: HTTP 200/404) | Prioritas tiket; PG yang memadukan saling lepas, bebas, dan P(T ∪ R) |
| A4 | Bab 5 §5.3.3 (materi: prevalensi 0,4%, 98%/97%); Bab 5 L10(c) | PG memilih tuas perbaikan PPV di antara empat tindakan |
| A5 | Bab 6 L2 (contoh pelanggaran BINS); Latihan UTS C4(c)–(d) | PG memilih model untuk *build* CI dengan *cache* bersama; pengecoh Poisson dan Geometrik |
| A6 | Bab 6 L3 (Binomial(15; 0,2)) | PG dengan pengecoh varians, Bernoulli, dan Var = mean |
| A7 | Bab 7 L1–L2 (jelaskan P(X = x) = 0; PDF > 1) | PG empat pernyataan tentang waktu unggah |
| A8 | Bab 7 L8 (n = 3.000, kemencengan 2,8, Shapiro) | PG membaca Q-Q plot dan kemencengan; pengecoh "n besar → Normal" |
| A9 | Bab 8 AI Corner (100 pengukuran, SD 35 ms) dan L2–L3 | PG dengan pengecoh ±2 SE untuk data individual |
| A10 | Bab 8 §8.4.3 (materi: tabel n cukup besar); Bab 8 L9 | PG kecukupan n untuk populasi sangat menceng, n = 20 |
| A11 | Bab 9 L5–L6 (tafsir IK [205, 223] ms); kisi-kisi §11 contoh A (tafsir *p-value*) | PG tafsir IK waktu tempuh; pengecoh "rata-rata sampel baru" |
| A12 | Bab 9 L3 (IK 90/95/99% dari n = 36) | Menurunkan IK 99% dari IK 95% yang diketahui (margin dan rasio t) |
| A13 | Bab 9 L1 (sebutkan tiga sifat estimator) | PG alasan penyebut n − 1 |
| A14 | Bab 12 L3 (tabel ANOVA k = 4, N = 44, SS 240/600), L6 | PG keputusan dengan tabel F dan η²; pengecoh "setiap pasangan berbeda" |
| A15 | Bab 12 L8 (sel harapan 2,3 dan 3,8) | Tabel 2 × 3 lengkap; harus menghitung E; pengecoh frekuensi teramati |
| B1 | Bab 4 L5 (P(8,3), C(8,3)); Latihan UTS B3 (P(9,3) · C(7,2)) | Pencacahan diikuti peluang token hanya angka |
| B2 | Bab 4 L3–L4 (1.000 sesi: dari cacah ke gabungan, komplemen, bersyarat) | Alur dibalik: dari P(K \| R) ke irisan (aturan perkalian), gabungan, lalu P(R \| K) |
| B3 | Bab 5 L5 (3 server paralel vs seri); Latihan UTS C4(b) (*load balancer* + 3 replika) | Dua tingkat seri, masing-masing 2 replika; keputusan penempatan replika tambahan |
| B4 | Bab 6 §6.4.3 (materi); Bab 6 L6(e) (5.000 pengguna, 0,06%: pilih distribusi) | Menghitung P(X ≤ 1) dengan hampiran dan menyebut alasannya |
| B5 | Bab 7 L3, L6; Latihan UTS B8(b) (aturan empiris di ekor) | Persentase tengah ±2σ tanpa tabel; ekor z = 2,5 dengan tabel |
| B6 | Bab 7 §7.2 (materi: *jitter* 0–500 ms) | Selang tengah, ekor kanan, rata-rata, dan persentil 90 |
| B7 | Bab 8 L3 (σ = 20, SE untuk berbagai n), L7 | P(x̄ > a) dengan TLP; hukum akar n |
| B8 | Bab 9 L2 (n = 36, x̄ = 120, s = 18: hitung IK); kisi-kisi §11 contoh B (n = 64, 218 ms, s = 40: hitung IK); Bab 9 §9.2.2 (materi) | Laporan analis yang keliru memakai z diberikan; mahasiswa mengenali kekeliruannya lalu menghitung interval-t |
| B9 | Bab 9 L4 (85 dari 500: periksa syarat, hitung IK proporsi) | Klaim pengembang "paling banyak 10%" dinilai dengan interval |
| B10 | Bab 9 L8 (±2 poin persen; dengan dan tanpa dugaan p ≈ 0,15); Bab 9 §9.5 (contoh kode: survei kepuasan, margin ±3%, p = 0,50) | Arah dibalik: margin terbesar dari anggaran n = 600, lalu n untuk ±3,5 poin persen dan tambahan responden; konteks pengelola kata sandi |
| C1 | Bab 5 L2–L3 (laporan bug dari tiga sumber 60/30/10: probabilitas total, lalu posterior satu sumber), L6(d)–(e) (PPV pada kelompok bergejala berprevalensi 15%), L7 (pemindai 96%/92%, 1,5%); §5.3.4 (materi) | Porsi 70/22/8. (a) memakai langkah L2–L3 (indikator §4.2 menuntutnya), dengan notasi empat komponen, asumsi, dan tafsir yang diminta; (b) PPV dan NPV; (c) prevalensi subkelompok gabungan dua sumber harus dihitung sebagai probabilitas bersyarat (di L6(d) prevalensi diberikan), lalu porsi malware yang tak pernah dipindai dan asumsi perilaku penyerang |
| C2 | Bab 4 L7 (3 penelaah dari 12; dua anggota terpilih bersama) | Undian urutan presentasi; sesi sama, "pertama atau terakhir", dan uji kebebasan akibat tanpa pengembalian |
| C3 | Bab 6 §6.4.2 (materi λ = 8), L4, L7 (λ = 25: kapasitas minimum untuk tingkat layanan 95–99,9% dan rasionya terhadap rata-rata); Bab 7 L4; Latihan UTS B6(c) (Geometrik tanpa memori), D3–D4 (galat per jam; Eksponensial "tidak ada galat selama 45 menit") | (b) target dinyatakan dalam menit per jam yang harus diterjemahkan menjadi peluang, menilai kapasitas usulan lalu mencari kapasitas terkecil (tanpa rasio terhadap rata-rata); (c) kritik "kapasitas = rata-rata"; (d) peluang bersyarat ekor kiri "tiba dalam 10 detik berikutnya" dengan konversi satuan |
| C4 | Bab 7 L6 (N(45, 8): "waktu yang hanya dilampaui 5% kompilasi"); Bab 8 §8.1.2 (materi: SD total tumbuh √n), L6 | Daya server dari 8 data; ambang pada persentil ke-90; total satu rak dan kritik "16 × batas" |
| C5 | Bab 13 L3, L6, L7, L8 (pola corong: asumsi mana, dampak pada IK koefisien, cara mengatasi, tafsir log); §13.3.3 (materi: ekstrapolasi rumah 3.000 m²) | Titik viral dan syarat memisahkannya; β dari ringkasan; (c) memilah dua plot residual — satu melanggar, satu tidak; (d) menghitung prediksi di luar rentang lalu menganalisis klaim membeli pengikut |
| D | Kisi-kisi §5 (kerangka: optimasi basis data SIAKAD, 40 permintaan), §11 contoh C (12 *endpoint caching*, d̄ = 34, s_d = 18); Bab 10 AI Corner, Bab 11 §11.3.2 dan L6; Latihan UTS D1 (skala tiga variabel dan satu ukuran pemusatan) dan D6 (tuliskan satu kesimpulan yang tidak dapat ditarik); Bab 1 L7–L8 (rata-rata kode ordinal; suhu "dua kali lebih panas") | Katalog perpustakaan, 36 kueri pada dua indeks; ringkasan kedua kelompok **dan** selisih (pengecoh Welch); kriteria praktis 50 ms. D1 meminta mengenali ringkasan tidak sah dalam draf laporan dan menggantinya (simpangan baku ordinal, koefisien variasi rasio, median nominal — bukan contoh di Bab 1 maupun Latihan UTS). D8 memberikan klaim pimpinan untuk dianalisis dan dirumuskan ulang, bukan meminta mahasiswa menuliskan sendiri satu kesimpulan yang tidak dapat ditarik. D2–D7 mengikuti tugas §5 butir 2–7 dengan data dan pertanyaan baru |

---

## Panduan Menyusun Varian (Naskah UAS Sebenarnya)

Naskah UAS sebenarnya adalah **varian** dari latihan ini. Mahasiswa sudah melihat latihan beserta pembahasannya, jadi varian harus menguji keterampilan yang sama dengan tingkat kesulitan yang sama, tetapi tidak dapat dijawab dengan mengingat jawaban latihan. Susun **dua** varian dengan prosedur yang sama: satu untuk UAS dan satu untuk ujian susulan ([kerangka asesmen §8.2](assessment-framework.md#82-susulan): soal susulan berbeda).

### 1. Invarian per butir

Untuk **setiap** butir dan sub-butir berikut ini tetap sama dengan [Tabel Butir](#tabel-butir) dan tabel di bawah: Sub-CPMK, level Bloom, skor, indikator kisi-kisi, taksiran waktu (±0,5 menit), dan tingkat kesulitan (kolom *Kesulitan*). Selain itu tetap sama: peta aspek tiap butir C ([pembahasan §0.1](latihan-uas-pembahasan.md#01-aturan-dari-kisi-kisi-uas-6-soal-uraian-dalam-latihan-ini-juga-diterapkan-pada-bagian-b-dan-d-petunjuk-6): C1 2,25/2/2/1,75; C2 2,5/2,25/2/1,25; C3 dan C4 2,5/2/2/1,5; C5 2,25/1,75/2/2) dengan total Bagian C rumus 12 · hitung 10 · asumsi 10 · interpretasi 8, struktur pedoman skor parsial, aturan pembulatan di Petunjuk Umum, **batas kalimat** pada perintah uraian, nilai antara yang dicetak (C1(b), C3, C4(a)), jenis tabel yang diperlukan (Normal, t, F; nilai di luar tabel dicetak di soal), serta keseimbangan PG (sebaran huruf kunci 3–4 per huruf; kunci bukan opsi terpanjang di lebih dari 2–3 butir).

Invarian di bawah sengaja dirumuskan sebagai **syarat bentuk dan tingkat kesulitan**, bukan sebagai hasil: keputusan, kunci, dan arah kesimpulan butir varian boleh berbeda dari latihan, dan dicatat hanya di catatan privat penyusun varian.

**Tingkat kesulitan** (taksiran penyusun) ditetapkan per satuan jawaban — butir A; butir B menurut sub-butirnya yang tersulit; sub-butir C dan D — dengan aturan berurutan yang sama dengan Latihan UTS: **Sulit** bila jalur jawaban memuat dua atau lebih jebakan khas atau keputusan konsep, atau analisis yang memadukan beberapa hasil menjadi keputusan; **Sedang** bila memerlukan hitungan atau jawaban yang disusun sendiri dengan paling banyak satu jebakan khas, atau PG tanpa hitungan yang ciri penentunya harus disimpulkan dari skenario; **Mudah** bila PG tanpa hitungan yang ciri penentunya disebut langsung di stem dan cukup satu langkah pengenalan (≤ 1 menit).

Sebaran skor menurut kesulitan: mudah 5 · sedang 59 · sulit 36 (A 5/9/1; B 0/16/4; C 0/23/17; D 0/11/14). Label ini taksiran; bila tersedia, kalibrasikan dengan proporsi jawaban benar per butir (angka agregat) dari latihan dan UAS.

| Butir | Sub-CPMK · Bloom · skor | Konsep/keterampilan yang diuji | Langkah dan format | Kesulitan |
|---|---|---|---|---|
| A1 | 081-1 · C2 · 1 | Arah persyaratan pada klaim | PG tanpa hitungan; kutipan laporan "x% dari yang mengalami E punya ciri F" dan kesimpulan yang membalik arah; pengecoh komplemen | Sedang (ii) — jebakan: angka sama dianggap makna sama |
| A2 | 081-1 · C3 · 1 | Perkalian tanpa pengembalian | PG angka; dua pengambilan; pengecoh dengan pengembalian dan penyebut tidak dikurangi | Sedang |
| A3 | 081-1 · C2 · 1 | Saling lepas vs bebas | PG; dua kategori dari satu objek dengan peluang tak nol; satu opsi memuat P(A ∪ B) | Sedang (ii) — jebakan: "tidak saling memengaruhi" |
| A4 | 081-1 · C2 · 1 | Pengaruh spesifisitas pada prevalensi rendah | PG; prevalensi ≤ 1%; empat tindakan perbaikan yang dampaknya pada PPV dapat dibandingkan dengan angka | Sedang (ii) — jebakan: tindakan yang tampak intuitif |
| A5 | 081-1 · C3 · 1 | BINS; memilih distribusi | PG; proses berulang yang melanggar tepat satu syarat BINS; pengecoh memuat distribusi lain | Sedang (ii) — jebakan: syarat yang terpenuhi dianggap cukup |
| A6 | 081-1 · C3 · 1 | E dan SD Binomial | PG angka; pengecoh varians, Bernoulli, Var = mean | Sedang |
| A7 | 081-1 · C2 · 1 | P(X = x) = 0; PDF bukan peluang | PG tanpa hitungan | Mudah |
| A8 | 081-1 · C2 · 1 | Kenormalan dari Q-Q plot dan kemencengan | PG; n dan kemencengan disebut | Mudah |
| A9 | 081-1 · C3 · 1 | Galat baku vs simpangan baku | PG; n kuadrat sempurna; pengecoh s, s/n, ±2 SE untuk data | Sedang |
| A10 | 081-1 · C2 · 1 | Batas TLP; n memadai | PG; bentuk populasi dan n disebut | Mudah |
| A11 | 081-1 · C2 · 1 | Tafsir IK | PG; empat pernyataan tafsir, campuran tafsir yang benar dan salah tafsir khas (mis. probabilitas μ, data individual, rata-rata sampel baru); boleh ditanyakan pernyataan yang keliru | Mudah |
| A12 | 081-1 · C3 · 1 | Lebar IK vs tingkat kepercayaan | PG angka; IK dan dua nilai t dicetak; hasil bulat | Sedang |
| A13 | 081-1 · C2 · 1 | Sifat estimator | PG tanpa hitungan | Mudah |
| A14 | 102-1 · C3 · 1 | Tabel ANOVA: F, η², keputusan dengan tabel F, tafsir | PG; k, N, SS_antar, SS_dalam; df₂ ada di tabel F | Sulit |
| A15 | 102-1 · C3 · 1 | Syarat frekuensi harapan | PG; tabel 2 × 3 lengkap; sedikitnya satu sel teramati < 5 sebagai pengecoh, sehingga keputusan hanya dapat diambil dengan menghitung frekuensi harapan | Sedang |
| B1 | 081-1 · C3 · 2 | Permutasi dengan alasan; peluang dari pencacahan | (a) 1 + (b) 1 | Sedang |
| B2 | 081-1 · C3 · 2 | Perkalian, penjumlahan umum, arah persyaratan | (a) 1 + (b) 1; diberikan dua peluang marginal dan satu peluang bersyarat | Sedang |
| B3 | 081-1 · C3 · 2 | Keandalan seri–paralel; keputusan | (a) 1 + (b) 1; dua tingkat, keandalan tingkat berbeda | Sulit |
| B4 | 081-1 · C3 · 2 | Hampiran Poisson | (a) 1 + (b) 1; np bulat kecil (1–4) | Sedang |
| B5 | 081-1 · C3 · 2 | Aturan empiris; ekor Normal | (a) 1 + (b) 1; batas tepat μ ± kσ; z dua desimal di tabel | Sedang |
| B6 | 081-1 · C3 · 2 | PDF sebagai luas (Uniform) | (a) 1 + (b) 1 | Sedang |
| B7 | 081-1 · C3 · 2 | SE, TLP, hukum akar n | (a) 1,5 + (b) 0,5; n kuadrat sempurna ≥ 30; sebaran agak menceng | Sulit |
| B8 | 081-1 · C3 · 2 | IK rata-rata dengan t; mengenali kekeliruan prosedur | (a) 0,5 + (b) 1,5; laporan analis memuat tepat satu kekeliruan prosedur; σ tidak diketahui; df ada di tabel; SE bulat | Sedang |
| B9 | 081-1 · C3 · 2 | IK proporsi dan syaratnya; menilai klaim dengan IK | (a) 0,5 + (b) 1,5; syarat terpenuhi; klaim berupa batas proporsi | Sedang |
| B10 | 081-1 · C3 · 2 | Margin dari n; ukuran sampel untuk margin | (a) 1 + (b) 1; tanpa dugaan awal | Sedang |
| C1 | 081-1 · C3–C4 · 8 | Probabilitas total (3 keadaan); Bayes; PPV/NPV; kebijakan penyaringan pada subkelompok | (a) 3 C3, (b) 2,5 C3, (c) 2,5 C4; (c) ≤ 3 kalimat; prevalensi gabungan < 2%; posterior keadaan yang ditanya berbeda nyata dari prior-nya (naik atau turun); P(ditandai) dicetak di (b); prevalensi subkelompok di (c) harus dihitung dari tabel | (a) Sedang · (b) Sulit · (c) Sulit |
| C2 | 081-1 · C3–C4 · 8 | Permutasi/kombinasi; peluang tanpa pengembalian; penjumlahan umum; uji kebebasan | (a)–(c) 2 C3, (d) 2 C4; (d) ≤ 2 kalimat; undian 6–10 unit dibagi dua sesi/kelompok | (a) Sedang · (b) Sulit · (c) Sedang · (d) Sulit |
| C3 | 081-1 · C3–C4 · 8 | Poisson: asumsi, kapasitas dari target layanan, kritik kapasitas = rata-rata; Eksponensial tanpa memori | (a), (b), (d) 2 C3; (c) 2 C4; (c) ≤ 3 kalimat; λ bulat 2–4; P(X ≤ λ) dan satu nilai PMF dicetak; target (b) dinyatakan dalam satuan waktu yang harus diterjemahkan menjadi peluang; (d) peluang bersyarat dengan konversi satuan | (a) Sedang · (b) Sedang · (c) Sulit · (d) Sulit |
| C4 | 102-1: (a) · 081-1: (b)–(d) · C3–C4 · 8 | Deskriptif dari data mentah; Normal; persentil; distribusi jumlah | (a)–(c) 2 C3, (d) 1,5 C3 + 0,5 C4; delapan data bulat dengan x̄ dan s bulat dan Σ(x − x̄)² dicetak; kelayakan model Normal dapat diperiksa dari mean–median dan simpangan; z untuk (b) dan (d) ada di tabel | (a) Sedang · (b) Sedang · (c) Sedang · (d) Sulit |
| C5 | 102-1 · C3–C4 · 8 | Diagram pencar dan titik berpengaruh; regresi dari ringkasan; R² dan LINE; sebab-akibat dan ekstrapolasi | (a), (b) 2 C3; (c), (d) 2 C4; (a) dan (d) ≤ 3 kalimat; sembilan titik bulat + satu titik berpengaruh dengan alasan substantif; dua plot residual yang harus dipilah — sedikitnya satu memperlihatkan pelanggaran LINE; (d) memuat prediksi di luar rentang data | (a) Sedang · (b) Sedang · (c) Sedang · (d) Sulit |
| D | 102-1: D1, D2, D5, D8 · 081-1: D3, D4, D6, D7 · C4 · 25 | Delapan keputusan kisi-kisi §5 dalam satu kasus sebelum–sesudah | D1 2 C3, D2 3 C4, D3 4 C4, D4 4 C4, D5 4 C3, D6 3 C3, D7 3 C4, D8 2 C4; ringkasan kedua kelompok **dan** selisih dicetak, dengan s kelompok jauh lebih besar daripada s_d sehingga t Welch dan t berpasangan berbeda nyata besarnya; df ada di tabel-t; keputusan D5 dan letak kriteria praktis terhadap IK (di atas, di dalam, atau di bawah) boleh berbeda dari latihan, asalkan analisis D7 dapat dinalar dari IK; bentuk sebaran selisih dan n dipilih sehingga analisis TLP di D4 bermuatan (kesimpulannya boleh layak atau tidak layak); D1 memuat tiga ringkasan pada tiga skala berbeda, campuran sah dan tidak sah; D8 memuat klaim yang melampaui rancangan studi | D1 Sedang · D2 Sulit · D3 Sulit · D4 Sulit · D5 Sedang · D6 Sedang · D7 Sulit · D8 Sedang |

### 2. Yang wajib diubah per butir

Pada setiap butir: **konteks/kasus**, **data dan angka**, **urutan dan isi pilihan ganda** (letak kunci diacak ulang), dan **nama entitas** (lembaga, sistem, kolom, kota). Karena panduan ini publik, contoh di kolom kanan hanya menggambarkan **jenis** perubahan — naskah sebenarnya memakai konteks dan angka pilihan dosen sendiri, bukan contoh ini secara harfiah — dan tidak menetapkan kunci atau kesimpulan varian.

| Butir | Arah variasi (contoh ilustratif) |
|---|---|
| A1 | Klaim lain dengan arah persyaratan tertukar (mis. porsi pengguna ponsel lama di antara akun yang mengalami *crash*, atau porsi transaksi malam di antara transaksi yang dibatalkan) |
| A2 | Benda dan jumlah lain (mis. kartu RFID rusak di antara 10–12 kartu); boleh "keduanya baik" alih-alih "keduanya rusak" |
| A3 | Dua kategori lain dari satu objek (mis. status pesanan "dibatalkan" vs "selesai"; kelas jaringan satu perangkat) |
| A4 | Penyaring lain berprevalensi ≤ 1% (mis. deteksi transaksi janggal, deteksi akun ganda) dengan tindakan perbaikan lain; kunci ditentukan dari perhitungan PPV keempat opsi |
| A5 | Proses berulang lain yang melanggar satu syarat BINS (mis. percobaan tidak saling bebas, peluang berubah antarpercobaan, atau banyaknya percobaan tidak tetap) |
| A6 | Proporsi dan n lain dengan np bulat dan √(np(1 − p)) dua desimal "rapi" |
| A7 | Peubah kontinu lain (mis. suhu ruang server, panjang antrean waktu); urutan pernyataan diacak |
| A8 | Data lain; arah kemencengan boleh dibalik (mis. menceng kiri pada skor tugas yang mudah) |
| A9 | n kuadrat sempurna lain (mis. 49, 81, 100) dan s baru |
| A10 | Bentuk populasi lain (mis. simetris tanpa pencilan dengan n = 12, atau agak menceng dengan n = 25) dengan kunci yang menyesuaikan tabel Bab 8 |
| A11 | Konteks dan interval baru; boleh IK proporsi; boleh ditanyakan pernyataan yang keliru |
| A12 | Arah dibalik (mis. dari IK 99% ke IK 90%) dengan rasio t yang memberi hasil bulat; nilai t dicetak bila df tidak ada di tabel |
| A13 | Sifat lain (mis. konsisten: mengapa x̄ makin dekat ke μ bila n membesar) |
| A14 | k, N, dan SS baru dengan df₂ yang ada di tabel F; keputusan boleh gagal menolak dengan η² tetap ditafsirkan |
| A15 | Tabel 2 × 3 atau 3 × 2 lain; syarat boleh terpenuhi (≤ 20% sel < 5, minimum ≥ 1) asalkan tetap ada sel teramati < 5 sebagai pengecoh |
| B1 | Pencacahan lain dengan urutan bermakna (mis. kode kupon, susunan juri) dan peluang subhimpunan |
| B2 | Konteks lain; yang diketahui boleh P(B \| A) alih-alih P(A \| B) |
| B3 | Dua atau tiga tingkat seri dengan banyak replika berbeda; tingkat terlemah tidak harus tingkat kedua |
| B4 | Kejadian langka lain (mis. galat sinkronisasi per hari) dengan np = 1, 3, atau 4; boleh P(X ≥ 2) |
| B5 | Batas μ ± 1σ atau ± 3σ; ekor kiri |
| B6 | Selang lain (mis. 200–1.000 ms); persentil lain |
| B7 | μ, σ, n baru (n ≥ 30, kuadrat sempurna); ekor kiri; galat baku sepertiga (n × 9) |
| B8 | Laporan lain dengan satu kekeliruan prosedur (mis. z padahal σ tidak diketahui, penyebut n alih-alih √n, atau df keliru); n dengan df di tabel (mis. 10, 21, 25) |
| B9 | Proporsi dan klaim lain (mis. klaim batas bawah "sedikitnya x%"); klaim boleh berada di dalam atau di luar interval |
| B10 | Anggaran dan margin lain (mis. 400 atau 900 responden; margin ±3 atau ±4,5 poin persen) |
| C1 | Penyaring lain dengan partisi tiga keadaan (mis. permintaan API dari tiga wilayah, berkas unggahan dari tiga jenis pengguna); prevalensi, sensitivitas, dan spesifisitas baru; kebijakan penyaringan pada subkelompok lain (mis. satu keadaan saja, bila prevalensinya tetap harus dihitung, atau dua dari tiga keadaan) |
| C2 | Undian lain (mis. pembagian 10 asisten ke dua laboratorium, urutan 6 tim *hackathon*); "sama kelompok", "pertama atau terakhir", dan uji kebebasan dua penempatan |
| C3 | Kedatangan lain (mis. pengunjung loket layanan, permintaan cetak di laboratorium) dengan λ bulat 2–4; target dalam satuan waktu lain (mis. paling banyak 2 menit per jam, atau 1 dari 20 menit); peluang bersyarat lain dengan konversi satuan (mis. "dalam 15 detik berikutnya" atau "tidak ada selama 20 detik berikutnya") |
| C4 | Besaran fisik lain yang wajar Normal (mis. suhu CPU, tegangan catu daya); delapan data bulat; persentil lain (mis. ke-80 atau ke-95); total n unit dengan pernyataan keliru "n × batas" |
| C5 | Pasangan peubah lain (mis. jam belajar di LMS dan nilai proyek; jumlah ulasan dan penjualan); titik berpengaruh dengan alasan substantif; pelanggaran LINE lain pada salah satu plot (mis. pola melengkung → L), plot lain boleh tanpa pelanggaran atau dengan pelanggaran berbeda; prediksi di luar rentang pada nilai lain |
| D | Kasus sebelum–sesudah lain pada unit yang sama (mis. waktu kompilasi modul sebelum–sesudah ganti *compiler*, waktu muat halaman sebelum–sesudah kompresi aset); n dengan df di tabel-t (mis. 30–49); kriteria praktis boleh di atas, di dalam, atau di bawah IK (analisis D7 menyesuaikan); ringkasan D1 baru pada tiga skala (mis. ordinal, interval, nominal); klaim D8 baru yang melampaui rancangan (mis. generalisasi ke perangkat, waktu, atau pengguna lain) |

### 3. Larangan

1. Menyalin kalimat, data, atau angka latihan ini — termasuk pengecoh PG, atau kalimat soal yang hanya diganti angkanya.
2. Mengubah level Bloom, skor, atau Sub-CPMK butir dan sub-butir, atau peta aspek butir C.
3. Menambah materi di luar kisi-kisi (Minggu 1–15, indikator §4–§5), atau menuntut rumus di luar daftar kisi-kisi UTS §7 dan UAS §8 yang tidak dapat diturunkan dari rumus di daftar.
4. Memakai teks atau angka Latihan Soal Bab 1–14, contoh soal kisi-kisi UAS (§5 dan §11), Latihan UTS, atau contoh ilustratif tabel di atas secara harfiah, atau memparafrasakan soalnya dengan hanya mengganti konteks dan angka.
5. Butir yang memerlukan nilai tabel di luar tabel yang dibagikan, tanpa nilai itu dicetak di soal; butir yang memerlukan tabel korelasi.
6. Menyimpan varian, kuncinya, skrip verifikasinya, atau catatan privat penyusun varian di repositori publik.

### 4. Prosedur mutu varian

1. **Selesaikan ulang setiap butir dengan Python** (pola blok kode di [pembahasan §5](latihan-uas-pembahasan.md#5-memeriksa-angka-dengan-python)) dan cocokkan dengan kunci varian. Periksa dengan `assert`: setiap angka kunci; skor per bagian 15/20/40/25; sebaran per pokok bahasan 8/12/14/10/12/10/12/14/8; Sub-CPMK 77/23; Bloom C2/C3/C4 = 8/65/27; aspek Bagian C 12/10/10/8; df dan nilai z yang dipakai ada di tabel. Pemeriksaan sifat yang menentukan kunci atau kesimpulan varian (mis. keputusan uji di D5, letak kriteria praktis terhadap IK di D7, kapasitas terkecil di C3) dicatat di catatan privat penyusun varian, bukan di dokumen publik ini.
2. **Pilihan ganda:** penelaah menjawab tanpa kunci untuk memastikan **tepat satu** jawaban benar per butir; letak kunci diacak ulang (sebaran huruf seimbang dan berbeda dari urutan kunci latihan); panjang opsi diperiksa agar kunci tidak menonjol.
3. **Cek waktu — uji coba berwaktu** (KENDALI `T1-10`, pola `T0-15`). Penguji coba: 2–3 asisten atau mahasiswa senior yang **belum membaca latihan maupun varian** (latihan ini publik sejak 9 Oktober 2026), dalam kondisi ujian: **120 menit, *closed book*, tulisan tangan, alat bantu sesuai kisi-kisi (kalkulator ilmiah *non-programmable*; tabel Normal, t, chi-square, dan F), tanpa AI**; catat waktu per bagian. Uji coba dilakukan pada latihan ini sebelum varian ditetapkan, **dan wajib** pada varian sebelum difinalkan oleh 2–3 penguji coba yang belum melihat varian maupun kuncinya, dengan ambang yang sama. Keputusan menurut **median** waktu penguji coba: **≤ 80 menit** (≤ 2/3 durasi) → lolos; **> 80 dan ≤ 90 menit** (≤ 3/4 durasi) → bersyarat: terapkan [cadangan pemangkasan pertama](#cadangan-pemangkasan-waktu), yang hanya cukup untuk median sampai **±82 menit**; di atasnya dosen juga menetapkan [pemangkasan lanjutan](#cadangan-pemangkasan-waktu), lalu uji ulang; **> 90 menit** → dosen menetapkan pemangkasan lanjutan, lalu uji ulang. Dasar ambang: penguji coba yang menguasai materi bekerja ±1,5× lebih cepat daripada rerata mahasiswa, sehingga 2/3 durasi bagi penguji coba setara dengan seluruh durasi bagi rerata mahasiswa. Data kalibrasi tambahan (bila dosen memintanya): catatan waktu per bagian dari mahasiswa yang mengerjakan latihan ini, diserahkan tanpa nama; yang dipakai dan dicatat hanya rekap agregat (median dan sebaran waktu per bagian).
4. **Telaah sejawat** memakai [checklist-verifikasi §C](../../../00-pedoman-obe/checklist-verifikasi.md#c-lembar-telaah-sejawat).
5. **Simpan** varian, kunci, skrip verifikasinya, dan catatan privat penyusun varian di penyimpanan privat, tidak di repositori. Untuk `mutu/02`, catat hanya angka agregat.

---

## Catatan untuk Dosen

1. **Penandaan.** Sub-CPMK per butir menurut isi (D-03(a)): 77% skor ke `PS-Sub-CPMK081-1`, 23% ke `PS-Sub-CPMK102-1`; nilai akhir tetap memakai alokasi registri (UAS → 081-1). Usulan revisi alokasi masuk `T2-08`.
2. **Kisi-kisi §3 vs §5.** Kerangka D (§5) adalah satu kasus uji dua sampel; bila semua butirnya dihitung sebagai uji hipotesis, porsinya ±20 poin, melebihi bobot §3 (14%). Latihan menjaga total §3 menurut konvensi penandaan butir utuh dengan menandai D4, D6, D8 ke Minggu 9, 10, 1 dan tidak memuat butir Minggu 11–12 di A–C. D4 sendiri juga menguji indikator §4.7 (memeriksa asumsi uji); menurut isi, porsi uji hipotesis ±16,5 poin. Selain itu kisi-kisi §1 menyebut "penekanan Minggu 9–14", sedangkan bobot §3 untuk Minggu 9–14 hanya 44%. Perlu diputuskan: pertahankan §3, atau sesuaikan bobotnya.
3. **Modul Minggu 16.** §2.4 modul memuat kerangka D yang berbeda dari kisi-kisi §5 (memodelkan distribusi, menghitung probabilitas, dst.); latihan mengikuti kisi-kisi §5. "Strategi Mengerjakan" modul membagi 115 menit ditambah 5 menit memeriksa tanpa waktu membaca, sedangkan model waktu latihan memakai 5 menit membaca dan sedikitnya 5 menit memeriksa.
4. **Ketentuan skor (usulan).** Penerapan aturan kisi-kisi §6 pada Bagian B dan D; bobot aspek 30/25/25/20 yang dipenuhi tepat pada total Bagian C dan per butir dengan selisih paling besar 5 poin persen; tafsir "kehilangan maksimal 30%" sebagai 30% skor butir; aturan "asumsi yang diminta" per baris pedoman skor; pengurangan −50% interpretasi sebagai batas atas sekali per butir (agar kalimat yang sama tidak dihukum dua kali); serta kesalahan berantai, toleransi pembulatan, kelipatan 0,25, dan jawaban alternatif sahih ([pembahasan §0](latihan-uas-pembahasan.md#0-ketentuan-umum-penskoran)).
5. **Rumus di luar daftar hafalan** — Uniform, ekor dan CDF Eksponensial, Cohen's d berpasangan, SD jumlah n peubah bebas, R² = r², margin galat proporsi dari n — diterima lewat jalur penurunan (pembahasan §0.3); pertimbangkan menambahkannya ke kisi-kisi §8.
6. **Waktu — putuskan sebelum uji coba.** Model ±104,5–110 menit kerja + 10 menit membaca dan memeriksa = ±114,5–120 menit: muat tanpa margin, dan dengan koreksi +10% seperti Latihan UTS 120 menit bisa tidak cukup. Empat pemangkasan sudah diterapkan (nilai antara dicetak pada C1(b), C3, C4(a); batas 3 kalimat pada D3 dan D4). Cadangan pertama (lima pemangkasan, ±2,5–4 menit) perlu disetujui sebelum uji coba; pilihan pemangkasan lanjutan sebaiknya disiapkan sekarang.
7. **Indikator yang tidak diuji** (Geometrik, tanda *overdispersion*, Pearson vs Spearman, menghitung χ² dan inflasi galat Tipe I, alasan uji lanjut hanya setelah ANOVA signifikan, uji-t satu sampel atas data mentah, IK-z) — akibat porsi §3; sebagian sudah diuji di Latihan UTS. Bila dosen ingin salah satunya masuk UAS, cetak biru diubah lebih dulu, lalu latihan diperbarui.
8. **Level Bloom UAS.** RPS Minggu 16 menulis UAS C3–C4, sedangkan kisi-kisi §2 menetapkan Bagian A C2–C3 dan latihan memuat 8 poin C2 (Bagian A). Perlu diselaraskan: RPS Minggu 16 dengan kisi-kisi §2 dan cetak biru ini (masalah sejenis untuk UTS tercatat di KENDALI `T0-19`).
9. **Data rekaan.** Seluruh angka rekaan; tidak ada merek atau lembaga nyata. Data C5 sembilan UMKM bilangan bulat dengan x̄ = 12, s_x = 5, ȳ = 30, s_y = 8, r = 0,80 tepat; ringkasan D konsisten (korelasi implisit waktu lama–baru ±0,87). Diagram pencar C5 dibulatkan ke kelipatan 2 juta (dinyatakan di soal); kedua plot residual C5(c) digambar tangan untuk data rekaan dua kota lain dengan prediksi 15–50 juta, sesuai rentang pengikut 2–25 ribu yang dinyatakan di soal.
10. **Nilai Islam** hadir secara ringan: kotak *Amanah berlatih* di lembar soal dan catatan kejujuran berdagang (tidak dinilai) di pembahasan C5(d); tidak ada butir bernilai yang bergantung pada rujukan dalil.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
