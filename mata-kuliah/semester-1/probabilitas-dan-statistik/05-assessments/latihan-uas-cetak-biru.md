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
| Penandaan | Penandaan Sub-CPMK per butir menurut isi adalah bawaan sementara D-03(a); bobot nilai akhir UAS tetap tercatat sesuai alokasi registri dan RPS (UAS 25% → `PS-Sub-CPMK081-1`). Satu pengecualian: D4 ditandai menurut konvensi butir utuh kisi-kisi §3 (lihat *Aturan penandaan* di bawah). |

**Aturan penandaan.** Mengikuti indikator mingguan [RPS §F](../01-rps/rps-probabilitas-dan-statistik.md#f-indikator-capaian-mingguan): butir tentang Minggu 1–3 (data, deskriptif, visualisasi) dan Minggu 12–14 (uji dua sampel, ANOVA, chi-square, korelasi–regresi) → `PS-Sub-CPMK102-1`; butir tentang Minggu 4–7 dan 9–11 (probabilitas, Bayes, distribusi, sampling, estimasi, uji satu sampel) → `PS-Sub-CPMK081-1`. Sub-butir D dan C ditandai sendiri-sendiri. Satu pengecualian: D4 ditandai menurut konvensi butir utuh kisi-kisi §3 (Minggu 9 → `PS-Sub-CPMK081-1`), padahal menurut isi 2,5 dari 4 poinnya termasuk Minggu 12 (`PS-Sub-CPMK102-1`); pembagi alternatifnya ada di [Cara menghitung ketercapaian](#cara-menghitung-ketercapaian-agregat). Lembar latihan hanya mencantumkan level Bloom dan skor; Sub-CPMK per butir tercantum di pembahasan dan di berkas ini.

---

## Kesesuaian dengan Kisi-Kisi

### Komposisi, skor, dan waktu

| Bagian | Bentuk | Butir (kisi-kisi → latihan) | Skor (kisi-kisi → latihan) | Bloom kisi-kisi | Bloom latihan | Waktu saran kisi-kisi | Model waktu kerja (135 kpm) |
|---|---|---|---|---|---|---|---|
| A | Pilihan ganda | 15 → 15 | 15 → 15 | C2–C3 | 8 butir C2, 7 butir C3 | 15 menit | 16 menit |
| B | Isian / hitungan pendek | 10 → 10 | 20 → 20 | C3 | 10 butir C3 | 25 menit | 22 menit |
| C | Uraian terstruktur | 5 → 5 | 40 → 40 | C3–C4 | C1, C2, C3, C5: C3–C4; C4: C3 (sub-butir C3: 29,5 poin; C4: 10,5 poin) | 50 menit | 46 menit |
| D | Studi kasus terpadu | 1 → 1 | 25 → 25 | C4 | 1 butir C4 (sub-butir C3: 9 poin; C4: 16 poin) | 25 menit | 22,5 menit |
| **Total** | | **31 → 31** | **100 → 100** | | | **115 menit** | **106,5 menit** |

Bentuk Bagian D mengikuti [kisi-kisi §5](kisi-kisi-uas.md#5-bentuk-soal-studi-kasus-terpadu-bagian-d--25) butir demi butir: D1–D8 = butir 1–8, dengan skor sama dengan bobotnya (2/3/4/4/4/3/3/2). Aturan alat bantu sama dengan kisi-kisi §1, RPS Minggu 16, dan RTM §F.2: *closed book*; kalkulator ilmiah *non-programmable* dan alat tulis; tabel Normal baku, t, chi-square, dan F dibagikan pengawas; rumus tidak disediakan (tanpa lembar rumus); AI dilarang. Butir yang memerlukan tabel Normal: B5(b), B7(a), C4(b)–(d); tabel-t: B8, D5, D6; tabel F: A14. Tabel chi-square dibagikan tetapi tidak diperlukan (A15 hanya memeriksa syarat). Nilai t untuk derajat bebas 48 (A12) tidak ada di tabel sehingga dicetak di soal. Untuk berlatih mandiri, Lampiran A.1–A.5 buku ajar memuat semua nilai tabel yang diperlukan; tabel korelasi A.6 tidak dibagikan saat UAS dan tidak dipakai. Nilai antara yang dicetak di soal untuk menghemat waktu: MS_antar dan MS_dalam (A14), frekuensi harapan baris Ponsel (A15), keandalan alternatif web (B3(b)), galat baku proporsi (B9), P(ditandai) (C1(b)), PPV kebijakan (C1(c)), P(X = 4) dan P(X = 5) (C3), Σx, Σ(x − x̄)², dan data yang sudah terurut (C4), serta t Welch (D2). Tabel isian dicetak pada C3(b) dan D1; tabel itu hanya mengatur tempat menulis jawaban.

### Model waktu

Model per butir (taksiran penyusun): **kata soal ÷ 120–150 kata per menit** (membaca saat mengerjakan) **+ kata jawaban minimal bernilai penuh ÷ ±20 kata per menit** (menulis tangan) **+ waktu berpikir** (membaca tabel dan grafik, menghitung dengan kalkulator, memilih metode). Kata dihitung sebagai token yang memuat huruf atau angka, jadi satu ungkapan hitungan tanpa spasi (mis. "1,96√(0,25/600)") dihitung satu kata; dampak aturan ini diperiksa di bawah (*hitungan ketat*). Grafik ASCII tidak dihitung sebagai kata — waktu membacanya masuk kolom *Berpikir* C5(a) dan C5(c). Jawaban minimal bernilai penuh diukur dari contoh *Baik* di pembahasan (Bagian C dan D) dan dari jawaban minimal Bagian B di tabel kedua di bawah; Bagian A hanya membaca dan berpikir. **Waktu berpikir** setingkat taksiran independen: PG 0,25 menit (pengenalan satu langkah), 0,5 menit (konsep), atau 0,75 menit (hitungan atau tabel); butir B 0,5–1 menit; sub-butir C dan D 0,5–0,75 menit untuk hitungan ringan atau analisis singkat, dan 1–1,25 menit untuk hitungan berlangkah banyak, pembacaan grafik, atau analisis yang memadukan beberapa hasil. Jumlahnya A 8, B 7,5, C 14,25, dan D 6 menit. Waktu berpikir Bagian C turun 1,75 menit dari versi sebelumnya (16 menit) karena pemangkasan no. 6–7 di [Cadangan pemangkasan waktu](#cadangan-pemangkasan-waktu): C1(c) tanpa hitungan PPV (−0,25), C2 dengan tiga sub-butir (−0,75), C3(b) dengan tabel isian (−0,25), C4(a) dengan data terurut (−0,25), dan C4(d) tanpa analisis pernyataan teknisi (−0,25).

| Bagian | Kata soal | Membaca (150–120 kpm) | Kata jawaban | Menulis (20 kpm) | Berpikir | Waktu kerja |
|---|---|---|---|---|---|---|
| A | 1.089 | 7,26–9,07 menit | — | — | 8 menit | 15,26–17,07 menit |
| B | 651 | 4,34–5,42 menit | 194 | 9,7 menit | 7,5 menit | 21,54–22,62 menit |
| C | 1.084 | 7,23–9,03 menit | 472 | 23,6 menit | 14,25 menit | 45,08–46,88 menit |
| D | 539 | 3,59–4,49 menit | 252 | 12,6 menit | 6 menit | 22,19–23,09 menit |
| **Total** | **3.363** | **22,42–28,02 menit** | **918** | **45,9 menit** | **35,75 menit** | **±104,1–109,7 menit** |

Jawaban minimal Bagian B yang dihitung model (satu baris per butir; kata dihitung dengan aturan yang sama):

| Butir | Jawaban minimal bernilai penuh | Kata |
|---|---|---|
| B1 | (a) Permutasi karena karakter berbeda dan urutan bermakna: P(16,4) = 16·15·14·13 = 43.680. (b) P(10,4) = 5.040; 5.040/43.680 = 0,1154 | 16 |
| B2 | (a) P(K∩R) = 0,12 × 0,5 = 0,06; P(K∪R) = 0,18 + 0,12 − 0,06 = 0,24. (b) P(R\|K) = 0,06/0,18 = 0,3333; berbeda karena penyebutnya repositori yang memuat kunci API, bukan repositori tanpa README | 27 |
| B3 | (a) web 1 − 0,05² = 0,9975; basis data 1 − 0,1² = 0,99; R = 0,9875. (b) basis data: 0,9975 × 0,999 = 0,9965 > 0,9899 → basis data | 21 |
| B4 | (a) X ~ Binomial(2.500; 0,0008); n besar, p kecil → Poisson, λ = np = 2. (b) P(X ≤ 1) = e^−2(1 + 2) = 0,4060 | 18 |
| B5 | (a) 36 dan 60 = μ ± 2σ → ±95%. (b) z = (63 − 48)/6 = 2,5; 1 − 0,9938 = 0,0062 | 15 |
| B6 | (a) 200/800 = 0,25; 120/800 = 0,15. (b) rata-rata 400 ms; j/800 = 0,9 → j = 720 ms | 14 |
| B7 | (a) SE = 18/6 = 3; z = (45 − 40)/3 = 1,67; P = 1 − 0,9525 = 0,0475. (b) n = 4 × 36 = 144 | 17 |
| B8 | (a) σ tidak diketahui dan n kecil, jadi harus t, bukan z. (b) df = 15, t = 2,131; SE = 2/4 = 0,5; margin 1,07; [5,43 ; 7,57] menit | 25 |
| B9 | (a) np̂ = 40 ≥ 10, n(1 − p̂) = 210 ≥ 10. (b) 0,16 ± 1,96 × 0,0232 = [0,1145 ; 0,2055]; batas bawah > 0,10, klaim tidak didukung; p̂ saja mengandung galat sampling, interval memperhitungkannya | 27 |
| B10 | (a) E = 1,96√(0,25/600) = 0,04; subkelompok 1,96√(0,25/150) = 0,08. (b) n = 1,96²·0,25/0,05² = 384,16 → 385; tambahan 235 | 14 |
| | **Total** | **194** |

Ditambah **5 menit membaca** seluruh soal di awal dan **sedikitnya 5 menit memeriksa** di akhir, total **±114,1–119,7 menit** (tengah, pada 135 kpm: ±106,6 → ±116,6 menit). Jadi model ini kini **muat dalam 120 menit pada seluruh rentang kecepatan baca**, tetapi sisanya tipis: pada kecepatan baca terendah hanya ±0,3 menit. Per bagian, Bagian B, C, dan D muat dalam waktu sarannya (B ±21,5–22,6 vs 25 menit; C ±45,1–46,9 vs 50 menit; D ±22,2–23,1 vs 25 menit), sedangkan Bagian A (±15,3–17,1 menit) dapat melampaui 15 menit sampai ±2 menit pada kecepatan baca terendah; selisih itu tertutup oleh Bagian B–D. Waktu saran kisi-kisi §2 sendiri berjumlah 115 menit, sehingga waktu membaca dan memeriksa (sedikitnya 10 menit) diambil dari sisa 5 menit dan dari bagian yang selesai lebih cepat (Petunjuk 5).

**Kepekaan: hitungan ketat.** Bila setiap angka di dalam ungkapan hitungan dihitung sebagai kata tersendiri (tanda =, +, −, ×, /, √, ±, tanda kurung, dan sejenisnya menjadi pemisah), kata jawaban minimal bertambah ±73 (918 → 991) dan kata soal ±37 (3.363 → 3.400), sehingga waktu kerja menjadi ±108–113,6 menit dan total **±118–123,6 menit** (tengah ±120,5). Pada hitungan ketat, latihan ini hanya muat pada kecepatan baca tinggi. Model mana yang lebih dekat dengan kenyataan hanya dapat diputuskan oleh **uji coba berwaktu**; karena itu uji coba tetap **wajib** sebelum varian disusun ([prosedur mutu varian](#4-prosedur-mutu-varian) no. 3), dan [cadangan pemangkasan](#cadangan-pemangkasan-waktu) disiapkan untuk hasil yang bersyarat atau tidak lolos.

Model ini sudah memperhitungkan semua pemangkasan yang diterapkan, termasuk tiga pemangkasan lanjutan yang mengubah peta skor, peta aspek, atau level Bloom sub-butir **milik latihan ini** (no. 7 di [Cadangan pemangkasan waktu](#cadangan-pemangkasan-waktu)); komposisi, bobot, dan sebaran kisi-kisi serta total aspek Bagian C tidak berubah. Pemangkasan itu diterapkan sama pada ketiga berkas latihan **sebelum** uji coba, sehingga uji coba menguji bentuk yang akan diwarisi varian; invarian varian per butir baru dibekukan sesudah uji coba ([Invarian per butir](#1-invarian-per-butir); [prosedur mutu varian](#4-prosedur-mutu-varian) no. 3). Latihan tetap menyatakan secara terbuka bahwa panjangnya masih dikalibrasi (Petunjuk 5).

### Cadangan pemangkasan waktu

**Sudah diterapkan** pada latihan ini. Pemangkasan no. 1–6 tidak mengubah Sub-CPMK, level Bloom, atau skor setiap baris [Tabel Butir](#tabel-butir), dan tidak mengubah total aspek Bagian C (poin hanya dipindahkan di dalam baris yang sama). Pemangkasan no. 7 mengubah peta skor, peta aspek, atau level Bloom sub-butir milik latihan ini, tetapi tidak mengubah kisi-kisi:

1. Nilai antara dicetak: P(ditandai) pada C1(b), P(X = 4) pada C3, Σ(x − x̄)² dan Σx pada C4.
2. Batas kalimat D3 dan D4 diturunkan dari 4 menjadi 3.
3. Lima pemangkasan yang semula disiapkan sebagai cadangan pertama: t Welch pembanding (1,42) dicetak pada D2 (hitung 0,75 pindah ke analisis, interpretasi 1,75); prevalensi lampiran yang dipindai (0,0170) dicetak pada C1(c) (kemudian diganti PPV kebijakan, no. 7(b)); frekuensi harapan baris Ponsel dicetak pada A15; keandalan alternatif web (0,9899) dicetak pada B3(b); batas kalimat C1(c), C3(c), C5(a), dan C5(d) diturunkan dari 3 menjadi 2.
4. Pemangkasan lanjutan yang tetap menjaga Sub-CPMK, Bloom, skor baris, dan peta aspek: D1 menggabungkan penentuan skala dengan penilaian tiap ringkasan (skala tidak lagi ditulis terpisah); C3(b) memeriksa kapasitas 5 dan 6 (tanpa mencari kapasitas terkecil dari awal); C4(a) memeriksa kesimetrisan dari rata-rata dan median; serta perumusan ulang yang lebih ringkas pada sebagian kalimat soal.
5. Tiga pemangkasan lagi dari cadangan pertama (9 Oktober 2026, sesudah telaah waktu): P(X = 5) = 0,1008 dicetak pada C3 (mahasiswa tetap menjumlahkan PMF, menghitung P(6), dan memutuskan; hemat ±0,25); MS_antar = 150 dan MS_dalam = 40 dicetak pada A14 (mahasiswa tetap menghitung F, membaca tabel F, dan menghitung η²; hemat ±0,25); galat baku proporsi 0,0232 dicetak pada B9 — baris "p̂ dan SE" (0,5) diganti unsur baru pada butir yang sama, yaitu alasan mengapa p̂ saja belum cukup untuk menilai klaim, sehingga hemat bersihnya ±0 tetapi B9 lebih jauh dari Bab 9 L4 ([Kemiripan](#kemiripan-dengan-sumber-terbuka)).
6. Sisa cadangan pertama (9 Oktober 2026, sesudah telaah model waktu): batas kalimat D2, D3, D4, dan D7 diturunkan dari 3 menjadi 2; D1 dijawab pada tabel isian (ringkasan · skala · sah atau tidak · pengganti); C3(b) memakai tabel isian untuk kapasitas 5 dan 6; data C4 dicetak sudah terurut.
7. Tiga pemangkasan lanjutan (9 Oktober 2026) untuk menutup kelebihan model, yang sebelumnya ±119,4–125 menit:
   - **(a)** C4(d) tanpa pernyataan teknisi: 0,5 poin interpretasinya menjadi tafsir peluang rak bagi pengelola pusat data, sehingga C4(d) menjadi C3 — butir C4 menjadi butir C3, dan skor C4 total 27 → 26,5.
   - **(b)** PPV kebijakan C1(c) (0,4510) dicetak; rumus dan hitung PPV itu (0,25 + 0,25) dipindahkan ke porsi *malware* tak terpindai P(S₁ \| M) pada sub-butir yang sama, sehingga peta aspek C1 tetap. Usulan semula — mencetak porsi tak terpindai (0,1207) dan memindahkan poinnya ke analisis — tidak dipakai, karena menggeser peta aspek C1 (interpretasi menjadi 31%, di luar selisih 5 poin persen) dan total aspek Bagian C.
   - **(c)** C2 menjadi tiga sub-butir: sub-butir lama (c) ("X pertama atau Y terakhir") dihapus; pemeriksaan "dapat terjadi bersamaan" beserta aturan penjumlahannya dipindah ke (b), yang kini menghitung "sesi sama" sebagai gabungan "keduanya pagi" dan "keduanya siang"; skor (a) dan (b) menjadi 3. Peta aspek, minggu, dan level Bloom C2 tetap; aturan penjumlahan umum (dengan irisan) tetap diuji di B2.

   Selain itu, sebagian kalimat soal dan contoh jawaban *Baik* dirumuskan lebih ringkas tanpa mengubah unsur yang dinilai.

**Cadangan pertama (sisa)** — diterapkan bila hasil uji coba **bersyarat**; perlu disetujui dosen **sebelum** uji coba. Aturannya sama: Sub-CPMK, level Bloom, skor baris, dan total aspek Bagian C tetap. Angka hemat adalah taksiran penyusun dalam menit kerja mahasiswa.

| No | Pemangkasan | Pemindahan poin (skor baris tetap) | Hemat |
|---|---|---|---|
| 1 | D5–D6: nilai t untuk db = 35 (t₀,₁₀ sampai t₀,₀₀₅) dicetak, sehingga tabel-t hanya diperlukan B8 | Tidak berubah | 0,25–0,5 |
| 2 | B10: √(0,25/600) dan √(0,25/150) dicetak | Tidak berubah | 0,25 |
| | **Total** | | **±0,5–0,75** |

Dengan dasar penguji coba ±1,5× lebih cepat daripada rerata mahasiswa, hemat ini setara ±0,3–0,5 menit penguji coba, sehingga cadangan pertama hanya cukup untuk median uji coba sampai **±80,5 menit**. Di atasnya dosen juga menetapkan pemangkasan lanjutan, lalu uji ulang.

**Pemangkasan lanjutan (sisa)** — mengubah peta skor, peta aspek, atau Bloom sub-butir, atau komposisi kisi-kisi; ditetapkan dosen, diterapkan sama pada ketiga berkas latihan (Petunjuk 5), lalu uji ulang — semuanya **sebelum** varian disusun. Dipakai bila median > 90 menit, atau bila hasil bersyarat melampaui cakupan cadangan pertama. Pilihannya (hemat dalam menit kerja mahasiswa):

| No | Pemangkasan lanjutan | Akibat pada peta | Hemat |
|---|---|---|---|
| a | C5(c) dengan satu plot residual (plot P); 0,25 poin plot Q menjadi dampak pelanggaran pada inferensi | Unsur "memilah plot tanpa pelanggaran" hilang; peta aspek tetap | 0,5–0,75 |
| b | C3(a) digabung ke C3(b)–(c): P(X = 0) dihapus, dua asumsi Poisson ditanyakan di (c); skor (a) dipindah ke (b) dan (c) | Peta skor dan Bloom C3 berubah (porsi C4 naik) | 1–1,5 |
| c | Revisi kisi-kisi §2: Bagian B menjadi 8 butir bernilai 2,5 | Komposisi kisi-kisi; sebaran §3 disesuaikan | 4–4,5 |

Untuk menutup selisih hitungan ketat (±3,6 menit pada kecepatan baca terendah) dan menyisakan waktu bagi kerja yang lebih lambat, diperlukan c, atau a + b bersama cadangan pertama (±2–3 menit) ditambah satu pemangkasan lain yang ditetapkan dosen.

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
| 4.1 Probabilitas dasar | penjumlahan/perkalian/komplemen, termasuk penjumlahan kejadian saling lepas dan pemeriksaan apakah dapat terjadi bersamaan (A2, B2, C2b); bersyarat dan arahnya (A1, B2, C1c); permutasi dan kombinasi (B1, C2a); perkalian tanpa pengembalian, termasuk rangkaian "pertama kali ditemukan pada pemeriksaan ke-3" (A2, C2b) | — |
| 4.2 Bayes dan kebebasan | probabilitas total pada partisi tiga keadaan beserta syarat partisinya, dan empat komponen Bayes (C1a); *base rate fallacy*, PPV, NPV (C1b); porsi *malware* yang tak pernah dipindai sebagai P(S₁ \| M) dan kebijakan penyaringan, dengan PPV subkelompok yang dicetak (C1c); spesifisitas pada prevalensi rendah (A4); saling lepas vs bebas (A3, C2b, C2c); keandalan seri–paralel (B3) | risiko asumsi kebebasan yang keliru pada keandalan (sudah diuji Latihan UTS C4) |
| 4.3 Distribusi diskret | BINS (A5); E dan Var Binomial (A6); Poisson dan hampirannya (B4, C3a); memilih distribusi (A5, B4); kapasitas berbasis kuantil dari target layanan (C3b) | Geometrik (sudah diuji Latihan UTS B6); tanda *overdispersion* varians ≫ mean (sudah diuji Latihan UTS D3; jawaban C3(c) hanya menyinggungnya dalam catatan yang tidak dinilai) |
| 4.4 Kontinu dan Normal | P(X = x) = 0 (A7); Eksponensial dan tanpa memori (C3d); skor-z dan tabel (B5, C4b); aturan empiris (B5a); x dari persentil (C4c); kenormalan dari Q-Q plot/kemencengan (A8), dan kesimetrisan dari rata-rata–median sebagai dasar model Normal (C4a–b) | — |
| 4.5 Sampling dan CLT | sebaran data vs x̄, galat baku vs simpangan baku (A9, B7); hukum akar n (B7b); isi dan batas TLP, kecukupan n (A10, B7a, D4); simpangan baku jumlah (C4d) | — |
| 4.6 Estimasi | sifat estimator (A13); IK rata-rata dengan t, termasuk mengenali kekeliruan memakai z bila σ tidak diketahui (B8, D6); IK proporsi dan syaratnya, memakai IK untuk menilai klaim, dan mengapa estimasi titik saja belum cukup (B9); tafsir 95% (A11, D6); margin galat, termasuk margin subkelompok, dan ukuran sampel (B10); lebar vs tingkat kepercayaan (A12) | IK dengan z bila σ diketahui |
| 4.7 Uji hipotesis | H₀/H₁ dan arah, arah sebelum data, galat Tipe I/II (D3); menghitung uji-t berpasangan (D5); menganalisis kesesuaian t Welch yang dicetak (D2); asumsi dan cara memeriksanya (D4); bebas vs berpasangan (D2); tafsir *p-value* (D5); signifikansi statistik vs praktis dan Cohen's d (D7) | uji-t satu sampel atas data mentah (uji berpasangan adalah uji-t satu sampel atas selisih); **menghitung** uji-t dua sampel bebas (t Welch dicetak di D2 dan hanya dianalisis); **kuasa uji** (hanya dianjurkan di penjelasan D2, tidak dinilai) |
| 4.8 ANOVA, chi-square, korelasi–regresi | tabel ANOVA, F, η², "bukan setiap pasangan berbeda" (A14); syarat frekuensi harapan (A15); koefisien regresi dan R² tanpa sebab-akibat (C5b–d); asumsi LINE dari plot residual, termasuk mengenali plot tanpa pelanggaran (C5c); ekstrapolasi (C5d) | menghitung inflasi galat Tipe I; mengapa uji lanjut hanya dilakukan setelah ANOVA signifikan (A14 hanya menguji bahwa ANOVA tidak menunjuk pasangan); menghitung statistik χ²; Pearson vs Spearman (hanya catatan tidak dinilai di pembahasan C5) |

Indikator yang tidak diuji tidak dirotasi ke varian — varian memakai cetak biru yang sama. Rotasi dilakukan bila latihan berikutnya disusun ulang.

### Sepuluh konsep inti (kisi-kisi §7)

| No | Konsep inti §7 | Butir yang menguji |
|---|---|---|
| 1 | Probabilitas bersyarat dan P(A\|B) ≠ P(B\|A) | A1, B2, C1(c) |
| 2 | Teorema Bayes dan *base rate fallacy* | A4, C1(a)–(b) |
| 3 | Pemilihan distribusi beserta asumsinya (BINS) | A5, B4, C3(a), C3(c) |
| 4 | Distribusi Normal, skor-z, membaca tabel | B5, B7(a), C4(b)–(d) |
| 5 | Galat baku σ/√n dan Teorema Limit Pusat | A9, A10, B7, C4(d), D4 |
| 6 | Interval kepercayaan dan tafsirnya yang benar | A11, A12, B8, B9, D6 |
| 7 | H₀/H₁, galat Tipe I/II, kuasa uji | D3 (H₀/H₁, galat Tipe I/II); **kuasa uji tidak diuji** — hanya dianjurkan, tidak disyaratkan, di penjelasan D2 |
| 8 | Tafsir *p-value* yang benar | D5 |
| 9 | Memilih uji dua sampel: bebas vs berpasangan | D2 |
| 10 | Korelasi bukan sebab-akibat; asumsi LINE | C5(c)–(d) |

Sembilan konsep teruji penuh; konsep 7 teruji sebagian. Kuasa uji tidak dijadikan unsur bernilai karena kerangka D (kisi-kisi §5) tidak memuat tugas tentang kuasa uji dan model waktu tidak menyisakan ruang untuk unsur baru ([Catatan untuk Dosen](#catatan-untuk-dosen) no. 7).

---

## Tabel Butir

Kolom *Indikator* merujuk subbagian kisi-kisi §4 (4.1–4.8) dan kerangka D di §5. Waktu dalam menit (model waktu pada 135 kata per menit; pembulatan per butir ke 0,25 menit mengikuti total per bagian).

| No | Indikator (kisi-kisi) | Mg | Sub-CPMK | Bloom | Skor | Waktu |
|---|---|---|---|---|---|---|
| A1 | 4.1 Membedakan arah persyaratan pada klaim laporan | 4 | PS-Sub-CPMK081-1 | C2 | 1 | 1 |
| A2 | 4.1 Aturan perkalian tanpa pengembalian pada rangkaian tiga pemeriksaan (pertama kali ditemukan pada pemeriksaan ke-3) | 4 | PS-Sub-CPMK081-1 | C3 | 1 | 1 |
| A3 | 4.2 Saling lepas vs saling bebas | 5 | PS-Sub-CPMK081-1 | C2 | 1 | 1,25 |
| A4 | 4.2 Mengapa spesifisitas lebih berpengaruh pada prevalensi rendah | 5 | PS-Sub-CPMK081-1 | C2 | 1 | 1,25 |
| A5 | 4.3 Memeriksa BINS; memilih distribusi | 6 | PS-Sub-CPMK081-1 | C3 | 1 | 1 |
| A6 | 4.3 E[X] dan SD Binomial | 6 | PS-Sub-CPMK081-1 | C3 | 1 | 0,75 |
| A7 | 4.4 P(X = x) = 0 dan cara membaca PDF | 7 | PS-Sub-CPMK081-1 | C2 | 1 | 0,75 |
| A8 | 4.4 Menilai kenormalan dari Q-Q plot dan kemencengan | 7 | PS-Sub-CPMK081-1 | C2 | 1 | 0,75 |
| A9 | 4.5 Galat baku vs simpangan baku | 9 | PS-Sub-CPMK081-1 | C3 | 1 | 1 |
| A10 | 4.5 Batas keberlakuan TLP; n memadai untuk bentuk populasi | 9 | PS-Sub-CPMK081-1 | C2 | 1 | 1 |
| A11 | 4.6 Tafsir "95% kepercayaan" | 10 | PS-Sub-CPMK081-1 | C2 | 1 | 1 |
| A12 | 4.6 Interval lebih lebar bila tingkat kepercayaan naik (hitung IK 99% dari IK 95%) | 10 | PS-Sub-CPMK081-1 | C3 | 1 | 1,25 |
| A13 | 4.6 Sifat estimator (tak bias) | 10 | PS-Sub-CPMK081-1 | C2 | 1 | 1 |
| A14 | 4.8 Membaca tabel ANOVA (MS dicetak); F, η²; ANOVA tidak menunjuk pasangan | 13 | PS-Sub-CPMK102-1 | C3 | 1 | 1,5 |
| A15 | 4.8 Syarat frekuensi harapan ≥ 5 | 13 | PS-Sub-CPMK102-1 | C3 | 1 | 1,5 |
| B1 | 4.1 Permutasi dengan alasan; peluang dari pencacahan | 4 | PS-Sub-CPMK081-1 | C3 | 2 | 2 |
| B2 | 4.1 Aturan perkalian, penjumlahan umum, dan arah persyaratan | 4 | PS-Sub-CPMK081-1 | C3 | 2 | 2,5 |
| B3 | 4.2 Keandalan seri–paralel; satu alternatif dihitung dan keputusan penempatan replika | 5 | PS-Sub-CPMK081-1 | C3 | 2 | 2,5 |
| B4 | 4.3 Hampiran Poisson untuk Binomial | 6 | PS-Sub-CPMK081-1 | C3 | 2 | 2 |
| B5 | 4.4 Aturan empiris; skor-z dan tabel Normal | 7 | PS-Sub-CPMK081-1 | C3 | 2 | 1,75 |
| B6 | 4.4 Membaca PDF sebagai luas (Uniform kontinu) | 7 | PS-Sub-CPMK081-1 | C3 | 2 | 1,5 |
| B7 | 4.5 Galat baku, TLP untuk P(x̄ > a), hukum akar n | 9 | PS-Sub-CPMK081-1 | C3 | 2 | 2,25 |
| B8 | 4.6 IK rata-rata: mengenali kekeliruan memakai z, lalu IK dengan t | 10 | PS-Sub-CPMK081-1 | C3 | 2 | 2,5 |
| B9 | 4.6 IK proporsi dan syaratnya (SE dicetak); memakai IK untuk menilai klaim dan mengapa p̂ saja belum cukup | 10 | PS-Sub-CPMK081-1 | C3 | 2 | 2,75 |
| B10 | 4.6 Margin galat proporsi dari n, termasuk margin subkelompok; ukuran sampel untuk margin tertentu (pembulatan ke atas) | 10 | PS-Sub-CPMK081-1 | C3 | 2 | 2,25 |
| C1a | 4.2 Bayes dengan empat komponen; *evidence* dengan probabilitas total (tiga keadaan) dan syarat partisinya; perbandingan posterior–prior (diminta) | 5 | PS-Sub-CPMK081-1 | C3 | 3 | 4 |
| C1b | 4.2 *Base rate fallacy*; PPV dan NPV; asumsi sensitivitas/spesifisitas (diminta) | 5 | PS-Sub-CPMK081-1 | C3 | 2,5 | 2,5 |
| C1c | 4.2 Porsi *malware* tak terpindai sebagai probabilitas bersyarat P(S₁ \| M) (arah persyaratan); analisis kebijakan penyaringan dengan angka, memakai PPV subkelompok yang dicetak (≤ 2 kalimat) | 5 | PS-Sub-CPMK081-1 | C4 | 2,5 | 2,5 |
| C2a | 4.1 Permutasi vs kombinasi: menunjukkan peran urutan pada setiap hitungan | 4 | PS-Sub-CPMK081-1 | C3 | 3 | 2 |
| C2b | 4.1 Peluang dari aturan perkalian bersyarat/pencacahan ("keduanya pagi"); aturan penjumlahan kejadian saling lepas ("sesi sama") dengan pemeriksaan apakah dapat terjadi bersamaan (diminta); asumsi undian (diminta) | 4 | PS-Sub-CPMK081-1 | C3 | 3 | 2,75 |
| C2c | 4.2 Analisis kebebasan dengan definisi formal (≤ 2 kalimat) | 5 | PS-Sub-CPMK081-1 | C4 | 2 | 2 |
| C3a | 4.3 Poisson: parameter, asumsi (diminta), PMF | 6 | PS-Sub-CPMK081-1 | C3 | 2 | 1,75 |
| C3b | 4.3 Kapasitas berbasis kuantil dari target layanan dalam satuan waktu (P(X = 4) dan P(X = 5) dicetak); memeriksa dua kapasitas pada tabel isian; keputusan untuk keduanya (diminta) | 6 | PS-Sub-CPMK081-1 | C3 | 2 | 2,75 |
| C3c | 4.3 Analisis kapasitas = rata-rata; kondisi nyata, asumsi Poisson yang dilanggarnya, dan dampaknya (diminta; ≤ 2 kalimat) | 6 | PS-Sub-CPMK081-1 | C4 | 2 | 2,5 |
| C3d | 4.4 Eksponensial; peluang bersyarat dengan sifat tanpa memori dan maknanya (diminta) | 7 | PS-Sub-CPMK081-1 | C3 | 2 | 2,5 |
| C4a | Deskriptif dalam kasus: x̄, median (data dicetak terurut), s; kesimetrisan dari rata-rata dan median (diminta) | 2 | PS-Sub-CPMK102-1 | C3 | 2 | 2 |
| C4b | 4.4 Ekor kanan Normal dan tafsirnya; asumsi kenormalan dan sejauh mana (a) mendukungnya (diminta) | 7 | PS-Sub-CPMK081-1 | C3 | 2 | 2,25 |
| C4c | 4.4 x dari persentil; tafsir (diminta) | 7 | PS-Sub-CPMK081-1 | C3 | 2 | 2 |
| C4d | 4.5 Distribusi jumlah/rata-rata n server (SE); asumsi (diminta); tafsir peluang bagi pengelola (diminta) | 9 | PS-Sub-CPMK081-1 | C3 | 2 | 2,75 |
| C5a | Visualisasi dalam kasus: membaca diagram pencar, titik berpengaruh, alasan dan syarat memisahkannya (≤ 2 kalimat) | 3 | PS-Sub-CPMK102-1 | C3 | 2 | 3,5 |
| C5b | 4.8 Koefisien regresi dari ringkasan; prediksi | 14 | PS-Sub-CPMK102-1 | C3 | 2 | 1,75 |
| C5c | 4.8 R² dan tafsirnya; analisis dua plot residual — memilah yang melanggar asumsi LINE dari yang tidak | 14 | PS-Sub-CPMK102-1 | C4 | 2 | 3 |
| C5d | 4.8 Korelasi bukan sebab-akibat; ekstrapolasi dengan prediksi di luar rentang; pernyataan atas klaim; tafsir kemiringan asosiatif (≤ 2 kalimat) | 14 | PS-Sub-CPMK102-1 | C4 | 2 | 3,5 |
| D1 | §5 butir 1 — menerapkan konsep skala pada tiap ringkasan; mengenali ringkasan yang tidak sah dan menggantinya (tabel isian) | 1–2 | PS-Sub-CPMK102-1 | C3 | 2 | 3,25 |
| D2 | §5 butir 2 — berpasangan atau bebas, dengan alasan; analisis kesesuaian t Welch yang dicetak lewat variasi di penyebutnya, tanpa menyebut rancangan di batang soal (≤ 2 kalimat) | 12 | PS-Sub-CPMK102-1 | C4 | 3 | 3 |
| D3 | §5 butir 3 — H₀/H₁ dalam notasi parameter yang sesuai rancangan, analisis arah, α dari konsekuensi galat (≤ 2 kalimat) | 11 | PS-Sub-CPMK081-1 | C4 | 4 | 3,5 |
| D4 | §5 butir 4 — asumsi dan cara memeriksanya; kecukupan n menurut TLP (≤ 2 kalimat) | 9 | PS-Sub-CPMK081-1 | C4 | 4 | 3,25 |
| D5 | §5 butir 5 — statistik uji sesuai rancangan dan derajat bebasnya, batas *p-value*, keputusan, tafsir | 12 | PS-Sub-CPMK102-1 | C3 | 4 | 3 |
| D6 | §5 butir 6 — IK 95% selisih dan tafsirnya | 10 | PS-Sub-CPMK081-1 | C3 | 3 | 1,75 |
| D7 | §5 butir 7 — Cohen's d; kebermaknaan praktis dengan IK (≤ 2 kalimat) | 11 | PS-Sub-CPMK081-1 | C4 | 3 | 2,25 |
| D8 | §5 butir 8 — analisis klaim yang melampaui rancangan studi dan rumusan yang didukung data (≤ 2 kalimat) | 1 | PS-Sub-CPMK102-1 | C4 | 2 | 2,5 |
| | **Total** | | | | **100** | **106,5** |

Level Bloom butir utuh: A dan B sesuai baris; C1, C2, C3, dan C5 = C3–C4; C4 = C3 (sesudah pemangkasan no. 7(a)); D = C4. Tidak ada butir C1 murni ("sebutkan"); kedelapan butir C2 berada di Bagian A, sesuai rentang C2–C3 kisi-kisi. Kata kerja perintah mengikuti taksonomi repositori ([`16-taksonomi-bloom-cap.md`](../../../00-kurikulum-if-2025-revisi-2026/16-taksonomi-bloom-cap.md), [`taksonomi-cap.md`](../../../00-pedoman-obe/taksonomi-cap.md)). **C3:** setiap butir B dan setiap sub-butir C3 di Bagian C dan D **memuat** sedikitnya satu perintah penerapan — "hitung" atau pertanyaan "berapa …" yang menuntut hitungan (KKO C3 "menghitung"), "tunjukkan" pada C5(a) ("menunjukkan" ada di daftar lengkap KKO C3 registri), atau "terapkan" pada D1 (KKO C3 "menerapkan": "Terapkan konsep skala pengukuran pada setiap ringkasan: tentukan …"). Perintah itu tidak selalu membuka sub-butir: C3(a) dibuka dengan "tuliskan parameter … lalu hitung", dan beberapa sub-butir B dibuka dengan perintah pendukung ("tuliskan" B4(a), "perkirakan" B5(a), "jelaskan" B8(a), "periksa" B9(a)) yang perintah penerapannya ada pada sub-butir pasangannya di butir yang sama. D6 memakai "hitung interval kepercayaan", bukan "susun" (KKO C6 di registri). **C4:** setiap sub-butir C4 memuat perintah "analisis" (KKO C4 "menganalisis"); perintah itu membuka C2(c), C3(c), dan D8, sedangkan pada C1(c), C5(c), C5(d), D2, D3, D4, dan D7 ia didahului langkah hitung, pertanyaan, atau pernyataan yang menjadi bahan analisisnya. C5(c) juga memuat "pilah" (KKO C4 "memilah"). "Menilai" (C5) tidak dipakai — butir 7 kisi-kisi §5 ("menilai kebermaknaan praktisnya") dirumuskan sebagai "analisis" di D7 — dan butir 3 kisi-kisi §5 ("merumuskan H₀ dan H₁"; "merumuskan" adalah KKO C6 di tabel utama registri) dirumuskan di D3 sebagai "nyatakan H₀ dan H₁ … analisis arah uji … tetapkan α dengan menghubungkannya …". Kata kerja pendukung seperti "sebutkan", "tuliskan", "nyatakan" (KKO C1), "tentukan", "deskripsikan", atau "tetapkan" hanya muncul sebagai langkah di dalam butir atau sub-butir yang level utamanya lebih tinggi (mis. "sebutkan asumsi" di C1(b) dan D4, "deskripsikan arah, bentuk, dan kekuatan" di C5(a), "tetapkan α dengan menghubungkannya pada konsekuensi galat" di D3); "memilih" (KKO C5 di tabel utama registri) tidak dipakai sebagai kata kerja perintah. Varian mempertahankan bentuk perintah ini.

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
| C3 | 51,5 | 14 | 65,5 | 65,5% |
| C4 | 17,5 | 9 | 26,5 | 26,5% |
| **Total** | **77** | **23** | **100** | **100%** |

### Skor per bagian dan level Bloom

| Bagian | C2 | C3 | C4 | Total |
|---|---|---|---|---|
| A | 8 | 7 | – | 15 |
| B | – | 20 | – | 20 |
| C | – | 29,5 | 10,5 | 40 |
| D | – | 9 | 16 | 25 |
| **Total** | **8** | **65,5** | **26,5** | **100** |

- Butir utuh ≥ C3: **23 dari 31 (74%)**; skor ≥ C3: **92%**.
- Rentang Bloom kedua Sub-CPMK (C3–C4) terwakili: skor C4 untuk `PS-Sub-CPMK081-1` = 17,5 dari 77 (23%), untuk `PS-Sub-CPMK102-1` = 9 dari 23 (39%). Dibanding Latihan UTS (C4 = 22%), porsi C4 naik menjadi 26,5%.

### Cara menghitung ketercapaian (agregat)

Untuk setiap mahasiswa: ketercapaian 081-1 (%) = (Σ skor butir bertanda 081-1)/77 × 100; ketercapaian 102-1 (%) = (Σ skor butir bertanda 102-1)/23 × 100. Pembagi 77/23 berlaku untuk **konvensi butir utuh** di Tabel Butir, yang mengikuti hitungan kisi-kisi §3. Menurut isi, 2,5 dari 4 poin D4 menguji asumsi uji-t berpasangan (indikator §4.7; [RPS §F](../01-rps/rps-probabilitas-dan-statistik.md#f-indikator-capaian-mingguan) Minggu 12 → `PS-Sub-CPMK102-1`) dan hanya 1,5 poin menguji Teorema Limit Pusat (Minggu 9 → `PS-Sub-CPMK081-1`). Sampai dosen memutuskan §3 vs §5 ([Catatan untuk Dosen](#catatan-untuk-dosen) no. 2), sediakan juga hitungan **menurut isi**: D4 dibagi — baris asumsi kebebasan dan asumsi kenormalan selisih (1,25 + 1,25 = 2,5 poin) ke 102-1, baris analisis TLP (1,5 poin) ke 081-1 — sehingga pembaginya **74,5/25,5**. Laporkan kedua angka dengan menyebut konvensinya; penandaan D8 (Minggu 1, dihitung pada baris deskriptif Minggu 1–3) sama pada kedua konvensi. Untuk `mutu/02` dan laporan PPEPP, yang dicatat di repositori hanya **angka agregat per kelas**: rata-rata dan median ketercapaian per Sub-CPMK, persentase mahasiswa di atas ambang, rata-rata skor per butir (tingkat kesukaran), dan daya beda per butir. Ambang ketercapaian belum ditetapkan (menunggu `T1-17` dan dokumen `F-03`). Skor per mahasiswa tidak dicatat di repositori.

Registri mengalokasikan seluruh UAS (25% nilai akhir) ke `PS-Sub-CPMK081-1`, sedangkan menurut penandaan butir (konvensi butir utuh untuk D4) 23% skor mengukur `PS-Sub-CPMK102-1` (Minggu 1–3 dan 12–14) — 25,5% bila D4 dibagi menurut isi. Dengan penandaan per butir, nilai akhir tetap memakai bobot registri, tetapi UAS menyumbang bukti ketercapaian untuk **kedua** Sub-CPMK; usulan revisi alokasi dicatat untuk tim kurikulum (`T2-08`).

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

Pemeriksaan orisinalitas terhadap tiga **sumber terlarang** — Latihan Soal Bab 1–14 buku ajar (tingkat Dasar, Menengah, Mahir), contoh soal kisi-kisi UAS (kerangka §5 dan contoh §11), dan [Latihan UTS](latihan-uts.md) — serta contoh di dalam bab dan modul Minggu 1–14. Tidak ada butir yang menyalin kalimat soal atau data sumber tersebut; pencocokan rangkaian lima kata hanya menemukan rumusan petunjuk, pertanyaan, dan istilah baku (mis. "jawab dalam paling banyak 2 kalimat", "interval kepercayaan 95% untuk rata-rata", "galat Tipe I dan Tipe II", serta "apakah rancangan ini berpasangan atau …" dari tugas kisi-kisi §5 butir 2). Beberapa butir menguji indikator yang sama dengan sumber terdekat, termasuk Latihan UTS yang menguji Minggu 1–7; untuk indikator yang langkah hitungnya baku (mis. probabilitas total lalu posterior di C1(a), interval-t di B8), langkahnya memang sama, sehingga butir itu dibedakan dari sumber terdekat oleh **bentuk pertanyaannya** — tugas, unsur yang diminta, dan kalimat perintahnya — bukan hanya konteks dan angkanya (kolom *Pembeda*). Varian wajib menjaga jarak yang sama dari sumber ini **dan** dari latihan ini.

| Butir | Sumber terdekat | Pembeda |
|---|---|---|
| A1 | Bab 4 L9 (contoh P(A\|B) ≠ P(B\|A) buatan sendiri); Latihan UTS C2(c) (laju vs porsi) | Klaim laporan keamanan tanpa tabel; PG dengan pengecoh komplemen |
| A2 | Bab 4 L8 (3 tiket dari 20 tanpa pengembalian: ketiganya kritis, tidak ada yang kritis, sedikitnya satu, dibandingkan dengan pengembalian); Bab 4 §4.4.3 (contoh: 2 tiket dari 20); Latihan UTS B6 (Geometrik: percobaan saling bebas sampai berhasil) | Bentuk pertanyaan lain: rangkaian pemeriksaan tanpa pengembalian yang **berhenti** pada temuan pertama — P(pertama kali ditemukan pada pemeriksaan ke-3) — yang tidak ada di Bab 4 L8 maupun contoh §4.4.3; pengecoh rumus Geometrik (seolah-olah dengan pengembalian, kontras dengan Latihan UTS B6), dua pemeriksaan pertama saja, dan peluang bersyarat pemeriksaan ketiga saja |
| A3 | Bab 5 L4, L8; Bab 5 §5.4.2 (materi: HTTP 200/404); Latihan UTS C4(a) (saling lepas dan saling bebas dua server dari data log) | Dua kategori pada satu tiket; PG yang memadukan saling lepas, bebas, dan P(T ∪ R), tanpa data frekuensi |
| A4 | Bab 5 §5.3.3 (materi: prevalensi 0,4%, 98%/97%); Bab 5 L10(c) | PG memilih tuas perbaikan PPV di antara empat tindakan |
| A5 | Bab 6 L2 (contoh pelanggaran BINS); Latihan UTS C4(c)–(d) | PG memilih model untuk *build* CI dengan *cache* bersama; pengecoh Poisson dan Geometrik |
| A6 | Bab 6 L3 (Binomial(15; 0,2)) | PG dengan pengecoh varians, Bernoulli, dan Var = mean |
| A7 | Bab 7 L1–L2 (jelaskan P(X = x) = 0; PDF > 1) | PG empat pernyataan tentang waktu unggah |
| A8 | Bab 7 L8 (n = 3.000, kemencengan 2,8, Shapiro) | PG membaca Q-Q plot dan kemencengan; pengecoh "n besar → Normal" |
| A9 | Bab 8 AI Corner (100 pengukuran, SD 35 ms) dan L2–L3; kisi-kisi §11 contoh B ("Dari sampel 64 permintaan API diperoleh x̄ = 218 ms dan s = 40 ms": hitung IK) | PG galat baku vs simpangan baku dengan pengecoh ±2 SE untuk data individual; n = 81 dan kalimat data dirumuskan lain dari contoh §11 B, yang tugasnya pun berbeda (IK, bukan galat baku) |
| A10 | Bab 8 §8.4.3 (materi: tabel n cukup besar); Bab 8 L9 | PG kecukupan n untuk populasi sangat menceng, n = 20 |
| A11 | Bab 9 L5–L6 (tafsir IK [205, 223] ms); kisi-kisi §11 contoh A (tafsir *p-value*) | PG tafsir IK waktu tempuh; pengecoh "rata-rata sampel baru" |
| A12 | Bab 9 L3 (IK 90/95/99% dari n = 36) | Menurunkan IK 99% dari IK 95% yang diketahui (margin dan rasio t); kalimat soal tidak memakai templat "Dari … diperoleh …" kisi-kisi §11 contoh B |
| A13 | Bab 9 L1 (sebutkan tiga sifat estimator); Bab 2 L11 (jelaskan intuisi penyebut n − 1 dan simulasikan biasnya); Latihan UTS B2 (memilih penyebut N atau n − 1 untuk data seluruh server) | PG alasan penyebut n − 1 dengan pengecoh efisiensi, konsistensi, dan syarat Normal; tidak meminta intuisi atau simulasi (Bab 2 L11) dan tidak menanyakan populasi vs sampel (Latihan UTS B2) |
| A14 | Bab 12 L3 (tabel ANOVA k = 4, N = 44, SS 240/600), L6 | PG keputusan dengan tabel F dan η²; pengecoh "setiap pasangan berbeda" |
| A15 | Bab 12 L8 (sel harapan 2,3 dan 3,8) | Tabel 2 × 3 lengkap; satu baris frekuensi harapan dicetak, baris lain dihitung; pengecoh frekuensi teramati |
| B1 | Bab 4 L6(b) (PIN 6 digit tanpa pengulangan: urutan bermakna, digit tak berulang); Bab 4 L5 (P(8,3), C(8,3)); Latihan UTS B3 (P(9,3) · C(7,2) dengan alasan permutasi atau kombinasi) | Pencacahan permutasi dari 16 karakter heksadesimal (bukan 10 digit) dengan alasan aturannya, diikuti **peluang** subhimpunan (token hanya angka) — Bab 4 L6 hanya mencacah, tanpa peluang; perintah alasan dirumuskan lain dari Latihan UTS B3 |
| B2 | Bab 4 L3–L4 (1.000 sesi: dari cacah ke gabungan, komplemen, bersyarat); Latihan UTS C2(a) (P(gagal \| COD), P(COD \| gagal), dan gabungan dari tabel kontingensi) | Tanpa tabel: dari P(K \| R) yang diketahui ke irisan (aturan perkalian), gabungan, lalu P(R \| K) beserta alasan perbedaannya |
| B3 | Bab 5 L5 (3 server paralel vs seri); Latihan UTS C4(b) (*load balancer* + 3 replika) | Dua tingkat seri, masing-masing 2 replika; satu alternatif penempatan dicetak, alternatif lain dihitung untuk keputusan |
| B4 | Bab 6 §6.4.3 (materi); Bab 6 L6(e) (5.000 pengguna, 0,06%: pilih distribusi) | Menghitung P(X ≤ 1) dengan hampiran dan menyebut alasannya |
| B5 | Bab 7 L3, L6; Latihan UTS B8(b) (aturan empiris di ekor) | Persentase tengah ±2σ tanpa tabel; ekor z = 2,5 dengan tabel |
| B6 | Bab 7 §7.2 (materi: *jitter* 0–500 ms) | Selang tengah, ekor kanan, rata-rata, dan persentil 90 |
| B7 | Bab 8 L3 (σ = 20, SE untuk berbagai n), L7 | P(x̄ > a) dengan TLP; hukum akar n |
| B8 | Bab 9 L2 ("Dari sampel n = 36 diperoleh x̄ = 120 dan s = 18. Hitung interval kepercayaan 95% untuk μ."); kisi-kisi §11 contoh B ("Dari sampel 64 permintaan API diperoleh x̄ = 218 ms dan s = 40 ms. Hitung interval kepercayaan 95% … Gunakan tabel-t."); Bab 9 §9.2.2 (materi) | Laporan analis yang keliru memakai z diberikan; mahasiswa mengenali kekeliruannya lalu menghitung ulang interval itu dengan t. Kalimat data ("Rekaman 16 sesi …: durasi rata-rata 6,5 menit, simpangan baku 2,0 menit") tidak memakai templat "Dari … diperoleh x̄ = … dan s = …" kedua sumber, dan perintah (b) ("Hitung ulang interval itu dengan prosedur yang benar …") dirumuskan lain dari "Hitung interval kepercayaan 95% …". Langkah hitung interval-t tetap sama dengan kedua sumber, karena itu varian **wajib** menjaga bentuk "kenali kekeliruan, lalu perbaiki" ([Larangan](#3-larangan) no. 4) |
| B9 | Bab 9 L4 (85 dari 500: periksa syarat, hitung IK proporsi); Bab 9 L12 (panduan pelaporan: mengapa estimasi titik saja tidak cukup) | Galat baku dicetak, sehingga bagian yang sama dengan Bab 9 L4 (syarat dan interval) tinggal 1 dari 2 poin; 1 poin lainnya untuk menilai klaim pengembang "paling banyak 10%" dengan interval dan menjelaskan mengapa p̂ saja belum cukup untuk menilainya — keduanya tidak diminta Bab 9 L4 |
| B10 | Bab 8 L8(a) (margin untuk 1.200 dan 40 responden dengan p̂ = 0,5); Bab 9 L8(a)–(c) (n untuk ±2 poin persen tanpa dan dengan dugaan p, lalu penghematannya); Bab 9 §9.5 (contoh kode: survei kepuasan, p = 0,50) | Langkah hitungnya sama dengan Bab 8 L8(a) dan Bab 9 L8(a), karena itu varian **wajib** memakai bentuk pertanyaan lain ([Larangan](#3-larangan) no. 4). Unsur baru pada latihan: margin **subkelompok** dari survei yang sama (memakai n subkelompok, bukan n total), lalu ukuran subkelompok untuk margin tertentu dengan pembulatan ke atas (384,16 → 385) dan tambahannya. Tidak ada perbandingan dua survei terpisah (Bab 8 L8) maupun dua dugaan p (Bab 9 L8(b)–(c)) |
| C1 | Bab 5 L2–L3 (laporan bug dari tiga sumber 60/30/10: probabilitas total, lalu posterior satu sumber), L6(d)–(e) (PPV pada kelompok bergejala berprevalensi 15%), L7 (pemindai 96%/92%, 1,5%); §5.3.4 (materi); Latihan UTS C3(a)–(b) (prior dari audit, detektor dengan sensitivitas/spesifisitas, notasi prior/*likelihood*/*evidence*, asumsi tentang prior, NPV dari tabel frekuensi) dan C3(d) (usulan kebijakan pimpinan untuk dianalisis) | Partisi **tiga** sumber berprevalensi berbeda (Latihan UTS C3: dua keadaan). (a) menanyakan posterior satu sumber dengan empat komponen Bayes, **syarat partisi** hukum probabilitas total (bukan asumsi tentang angka audit atau prior), dan perbandingan posterior–prior; (b) PPV dan NPV dari P(ditandai) yang dicetak, dengan asumsi kinerja pemindai antarsumber; (c) kebijakan yang dianalisis adalah penyaringan sebagian sumber — porsi *malware* yang tak pernah dipindai, P(S₁ \| M), dengan PPV subkelompok yang dicetak — bukan sanksi atas hasil detektor seperti Latihan UTS C3(d) |
| C2 | Bab 4 L7 (3 penelaah dari 12; dua anggota terpilih bersama); Latihan UTS B3 (alasan permutasi atau kombinasi) dan C4(a) (uji kebebasan dengan definisi formal; saling lepas) | Undian urutan presentasi: susunan vs himpunan dari satu undian; "sesi sama" sebagai gabungan dua kejadian saling lepas ("keduanya pagi", "keduanya siang") dengan pemeriksaan apakah keduanya dapat terjadi bersamaan; kebebasan dua penempatan **akibat undian tanpa pengembalian** (Latihan UTS C4(a): kebebasan dari frekuensi log). Langkah "keduanya pagi" di (b) sama dengan Bab 4 L7(c) (dua anggota tertentu terpilih bersama), tetapi di sini hanya satu langkah antara menuju "sesi sama" dan menjadi P(A ∩ B) di (c); varian **wajib** memakai bentuk pertanyaan lain dari L7(c) ([Larangan](#3-larangan) no. 4). Kalimat perintah (a) dan (c) dirumuskan berbeda dari Latihan UTS |
| C3 | Bab 6 §6.4.2 (materi λ = 8), L4, L7 (λ = 25: kapasitas minimum untuk tingkat layanan 95–99,9% dan rasionya terhadap rata-rata); Bab 7 L4; Latihan UTS B6(c) (Geometrik tanpa memori), D3–D4 (galat per jam; Eksponensial "tidak ada galat selama 45 menit") | (b) target dinyatakan dalam menit per jam yang harus diterjemahkan menjadi peluang, lalu menilai dua kapasitas (tanpa rasio terhadap rata-rata); (c) kritik "kapasitas = rata-rata"; (d) peluang bersyarat ekor kiri "tiba dalam 10 detik berikutnya" dengan konversi satuan |
| C4 | Bab 7 L6 (N(45, 8): "waktu yang hanya dilampaui 5% kompilasi"); Bab 8 §8.1.2 (materi: SD total tumbuh √n), L6; Latihan UTS B2 (varians dan simpangan baku dengan alasan penyebut) dan C1(a) (mean, median, simpangan baku, kuartil, pencilan) | (a) tidak menanyakan pilihan penyebut (Latihan UTS B2) — "simpangan baku sampel" disebut di soal dan Σx serta Σ(x − x̄)² dicetak; tugasnya memeriksa kesimetrisan dari rata-rata dan median sebagai dasar model Normal di (b), bukan kuartil dan pencilan (Latihan UTS C1(a)); ambang pada persentil ke-90; total satu rak dengan tafsir peluangnya bagi pengelola |
| C5 | Bab 13 L3, L6, L7, L8 (pola corong: asumsi mana, dampak pada IK koefisien, cara mengatasi, tafsir log); §13.3.3 (materi: ekstrapolasi rumah 3.000 m²); Bab 14 L9 (kalimat AI yang menafsirkan r jam belajar–IPK sebagai kenaikan kausal) | Titik viral dan alasan serta syarat memisahkannya; β dari ringkasan; (c) memilah dua plot residual — satu melanggar, satu tidak; (d) klaim pemilik usaha yang menggabungkan sebab-akibat dengan prediksi di luar rentang, yang harus dihitung lalu dianalisis (Bab 14 L9 meminta mengoreksi kalimat tafsir r, tanpa ekstrapolasi) |
| D | Kisi-kisi §5 (kerangka: optimasi basis data SIAKAD, 40 permintaan), §11 contoh C (12 *endpoint caching*, d̄ = 34, s_d = 18); Bab 10 AI Corner, Bab 11 §11.3.2 dan L6 (waktu muat halaman pada 15 perangkat sebelum–sesudah optimasi gambar: berpasangan atau bebas, uji yang tepat, akibat uji bebas, asumsi pada selisih); Latihan UTS D1 (skala tiga variabel dan satu ukuran pemusatan) dan D6 (tuliskan satu kesimpulan yang tidak dapat ditarik); Bab 1 L7–L8 (rata-rata kode ordinal; suhu "dua kali lebih panas") | Katalog perpustakaan, 36 kueri pada dua indeks; ringkasan kedua kelompok **dan** selisih; t Welch dicetak untuk dianalisis kesesuaiannya (Bab 11 L6(c) menanyakan akibat uji bebas secara umum); kriteria praktis 50 ms. D1 meminta mengenali ringkasan tidak sah dalam draf laporan dan menggantinya (simpangan baku ordinal, koefisien variasi rasio, median nominal — bukan contoh di Bab 1 maupun Latihan UTS). D8 memberikan klaim pimpinan untuk dianalisis dan dirumuskan ulang, bukan meminta mahasiswa menuliskan sendiri satu kesimpulan yang tidak dapat ditarik. D3–D7 mengikuti tugas §5 butir 3–7 dengan data dan pertanyaan baru. Domain "waktu respons setelah perubahan sistem" sama dengan kerangka §5, contoh §11 C, dan Bab 11 L6; pembedanya cukup untuk latihan, tetapi varian **wajib** memakai domain lain ([Larangan](#3-larangan) no. 4) |

---

## Panduan Menyusun Varian (Naskah UAS Sebenarnya)

Naskah UAS sebenarnya adalah **varian** dari latihan ini. Mahasiswa sudah melihat latihan beserta pembahasannya, jadi varian harus menguji keterampilan yang sama dengan tingkat kesulitan yang sama, tetapi tidak dapat dijawab dengan mengingat jawaban latihan. Susun **dua** varian dengan prosedur yang sama: satu untuk UAS dan satu untuk ujian susulan ([kerangka asesmen §8.2](assessment-framework.md#82-susulan): soal susulan berbeda).

### 1. Invarian per butir

Untuk **setiap** butir dan sub-butir berikut ini tetap sama dengan [Tabel Butir](#tabel-butir) dan tabel di bawah: Sub-CPMK, level Bloom, skor, indikator kisi-kisi, taksiran waktu (±0,5 menit), dan tingkat kesulitan (kolom *Kesulitan*). Selain itu tetap sama: peta aspek tiap butir C ([pembahasan §0.1](latihan-uas-pembahasan.md#01-aturan-dari-kisi-kisi-uas-6-soal-uraian-dalam-latihan-ini-juga-diterapkan-pada-bagian-b-dan-d-petunjuk-6): C1 2,25/2/2/1,75; C2 2,5/2,25/2/1,25; C3 dan C4 2,5/2/2/1,5; C5 2,25/1,75/2/2) dengan total Bagian C rumus 12 · hitung 10 · asumsi 10 · interpretasi 8, struktur pedoman skor parsial, aturan pembulatan di Petunjuk Umum, **batas kalimat** pada perintah uraian, nilai antara yang dicetak (A14, A15, B3(b), B9, C1(b), C1(c), C3, C4, D2), tabel isian (C3(b), D1), jenis tabel yang diperlukan (Normal, t, F; nilai di luar tabel dicetak di soal), serta keseimbangan PG (sebaran huruf kunci 3–4 per huruf; kunci bukan opsi terpanjang di lebih dari 2–3 butir).

Invarian di bawah sengaja dirumuskan sebagai **syarat bentuk dan tingkat kesulitan**, bukan sebagai hasil: keputusan, kunci, dan arah kesimpulan butir varian boleh berbeda dari latihan, dan dicatat hanya di catatan privat penyusun varian.

**Kapan invarian dibekukan.** Model waktu latihan ini kini muat dalam 120 menit hanya dengan sisa tipis, dan pada hitungan ketat melampauinya ([Model waktu](#model-waktu)), sehingga uji coba berwaktu dapat berujung pada pemangkasan lanjutan yang mengubah peta skor, peta aspek, atau Bloom sub-butir. Karena itu invarian per butir — skor, peta aspek, level Bloom, dan taksiran waktu — baru **dibekukan sesudah** uji coba berwaktu latihan ini dan keputusan dosen tentang pemangkasan ([Catatan untuk Dosen](#catatan-untuk-dosen) no. 6), dan varian baru disusun sesudah itu. Pemangkasan yang mengubah peta diterapkan lebih dulu pada ketiga berkas latihan (Petunjuk 5), sehingga latihan tetap menjadi simulasi yang setia bagi varian; tabel di bawah dan [Tabel Butir](#tabel-butir) diperbarui bersamaan.

**Nilai antara yang dicetak** tidak boleh mempersingkat jawaban sub-butir sebelumnya. Pada latihan ini, P(ditandai) di C1(b) memungkinkan P(M) di C1(a) dihitung mundur, dan P(X = 4) di C3 memuat e^(−3) dari C3(a); dampaknya kecil (masing-masing 0,5 poin hitung, dan hitungan mundurnya tidak lebih singkat daripada hitungan langsung), tetapi pada varian pilih nilai cetak yang tidak membuka jalan itu — mis. nilai yang hanya dipakai sub-butir sesudahnya, atau nilai yang tidak memuat jawaban sub-butir sebelumnya.

**Tingkat kesulitan** (taksiran penyusun) ditetapkan per satuan jawaban — butir A; butir B menurut sub-butirnya yang tersulit; sub-butir C dan D — dengan aturan berurutan yang sama dengan Latihan UTS: **Sulit** bila jalur jawaban memuat dua atau lebih jebakan khas atau keputusan konsep, atau analisis yang memadukan beberapa hasil menjadi keputusan; **Sedang** bila memerlukan hitungan atau jawaban yang disusun sendiri dengan paling banyak satu jebakan khas, atau PG tanpa hitungan yang ciri penentunya harus disimpulkan dari skenario; **Mudah** bila PG tanpa hitungan yang ciri penentunya disebut langsung di stem dan cukup satu langkah pengenalan (≤ 1 menit).

Sebaran skor menurut kesulitan: mudah 5 · sedang 60 · sulit 35 (A 5/9/1; B 0/16/4; C 0/24/16; D 0/11/14). Label ini taksiran; bila tersedia, kalibrasikan dengan proporsi jawaban benar per butir (angka agregat) dari latihan dan UAS.

| Butir | Sub-CPMK · Bloom · skor | Konsep/keterampilan yang diuji | Langkah dan format | Kesulitan |
|---|---|---|---|---|
| A1 | 081-1 · C2 · 1 | Arah persyaratan pada klaim | PG tanpa hitungan; kutipan laporan "x% dari yang mengalami E punya ciri F" dan kesimpulan yang membalik arah; pengecoh komplemen | Sedang (ii) — jebakan: angka sama dianggap makna sama |
| A2 | 081-1 · C3 · 1 | Perkalian tanpa pengembalian | PG angka; rangkaian dua atau tiga pengambilan tanpa pengembalian dengan kejadian yang **bukan** bentuk Bab 4 L8 (semuanya, tidak ada, atau sedikitnya satu); pengecoh memuat hitungan dengan pengembalian dan satu kesalahan perangkaian lain (mis. faktor yang terlewat atau peluang bersyarat satu tahap saja) | Sedang |
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
| A14 | 102-1 · C3 · 1 | Tabel ANOVA: F, η², keputusan dengan tabel F, tafsir | PG; k, N, SS_antar, SS_dalam, serta MS_antar dan MS_dalam dicetak; df₂ ada di tabel F | Sulit |
| A15 | 102-1 · C3 · 1 | Syarat frekuensi harapan | PG; tabel 2 × 3 lengkap; frekuensi harapan satu baris dicetak, baris lain dihitung; sedikitnya satu sel teramati < 5 sebagai pengecoh, sehingga keputusan hanya dapat diambil dengan menghitung frekuensi harapan | Sedang |
| B1 | 081-1 · C3 · 2 | Permutasi dengan alasan; peluang dari pencacahan | (a) 1 + (b) 1 | Sedang |
| B2 | 081-1 · C3 · 2 | Perkalian, penjumlahan umum, arah persyaratan | (a) 1 + (b) 1; diberikan dua peluang marginal dan satu peluang bersyarat | Sedang |
| B3 | 081-1 · C3 · 2 | Keandalan seri–paralel; keputusan | (a) 1 + (b) 1; dua tingkat, keandalan tingkat berbeda; satu alternatif penempatan dicetak di (b), alternatif lain dihitung | Sulit |
| B4 | 081-1 · C3 · 2 | Hampiran Poisson | (a) 1 + (b) 1; np bulat kecil (1–4) | Sedang |
| B5 | 081-1 · C3 · 2 | Aturan empiris; ekor Normal | (a) 1 + (b) 1; batas tepat μ ± kσ; z dua desimal di tabel | Sedang |
| B6 | 081-1 · C3 · 2 | PDF sebagai luas (Uniform) | (a) 1 + (b) 1 | Sedang |
| B7 | 081-1 · C3 · 2 | SE, TLP, hukum akar n | (a) 1,5 + (b) 0,5; n kuadrat sempurna ≥ 30; sebaran agak menceng | Sulit |
| B8 | 081-1 · C3 · 2 | IK rata-rata dengan t; mengenali kekeliruan prosedur | (a) 0,5 + (b) 1,5; laporan analis memuat tepat satu kekeliruan prosedur; σ tidak diketahui; df ada di tabel; SE bulat | Sedang |
| B9 | 081-1 · C3 · 2 | IK proporsi dan syaratnya; menilai klaim dengan IK; mengapa estimasi titik saja belum cukup | (a) 0,5 + (b) 1,5; galat baku dicetak; syarat diperiksa dengan angka (hasilnya, dan kesesuaian (b) dengan hasil itu, dicatat di catatan privat penyusun varian); klaim berupa batas proporsi; (b) memuat interval (0,5), penilaian klaim dengan interval (0,5), dan alasan mengapa p̂ saja belum cukup (0,5) | Sedang |
| B10 | 081-1 · C3 · 2 | Margin dari n, termasuk margin subkelompok; ukuran sampel untuk margin | (a) 1 + (b) 1; tanpa dugaan awal; margin untuk seluruh responden dan satu subkelompok; ukuran subkelompok untuk margin tertentu yang hasil hitungnya pecahan (pembulatan ke atas) | Sedang |
| C1 | 081-1 · C3–C4 · 8 | Probabilitas total (3 keadaan); Bayes; PPV/NPV; kebijakan penyaringan pada subkelompok | (a) 3 C3, (b) 2,5 C3, (c) 2,5 C4; (a) meminta empat komponen Bayes, syarat partisi, dan perbandingan posterior–prior; (c) ≤ 2 kalimat; prevalensi gabungan < 2%; posterior keadaan yang ditanya berbeda nyata dari prior-nya (naik atau turun); P(ditandai) dicetak di (b); PPV subkelompok dicetak di (c), sedangkan porsi *malware* tak terpindai, P(S₁ \| M), dihitung dari tabel | (a) Sedang · (b) Sulit · (c) Sulit |
| C2 | 081-1 · C3–C4 · 8 | Permutasi/kombinasi; peluang tanpa pengembalian; penjumlahan kejadian saling lepas; uji kebebasan | (a) 3 C3, (b) 3 C3, (c) 2 C4; (c) ≤ 2 kalimat; undian 6–10 unit dibagi dua sesi/kelompok; (b) menghitung peluang dua unit berada di satu kelompok tertentu, lalu di kelompok yang sama sebagai gabungan kejadian saling lepas, dengan pemeriksaan apakah kejadian-kejadian itu dapat terjadi bersamaan; (c) dapat memakai hasil (b) | (a) Sedang · (b) Sulit · (c) Sulit |
| C3 | 081-1 · C3–C4 · 8 | Poisson: asumsi, kapasitas dari target layanan, kritik kapasitas = rata-rata; Eksponensial tanpa memori | (a), (b), (d) 2 C3; (c) 2 C4; (c) ≤ 2 kalimat; λ bulat 2–4; P(X ≤ λ) dan dua nilai PMF berikutnya dicetak; target (b) dinyatakan dalam satuan waktu yang harus diterjemahkan menjadi peluang, dan (b) menilai dua kapasitas yang disebut soal pada tabel isian; (d) peluang bersyarat dengan konversi satuan | (a) Sedang · (b) Sedang · (c) Sulit · (d) Sulit |
| C4 | 102-1: (a) · 081-1: (b)–(d) · C3 · 8 | Deskriptif dari data mentah; Normal; persentil; distribusi jumlah | (a)–(d) 2 C3; delapan data bulat, dicetak terurut, dengan x̄, median, dan s mudah dihitung; Σx dan Σ(x − x̄)² dicetak; (d) meminta tafsir peluang total bagi pengelola; (a) memeriksa kesimetrisan dari rata-rata dan median, (b) menjelaskan sejauh mana hasil itu mendukung model Normal (hasil keduanya dicatat di catatan privat); z untuk (b) dan (d) ada di tabel | (a) Sedang · (b) Sedang · (c) Sedang · (d) Sedang |
| C5 | 102-1 · C3–C4 · 8 | Diagram pencar dan titik berpengaruh; regresi dari ringkasan; R² dan LINE; sebab-akibat dan ekstrapolasi | (a), (b) 2 C3; (c), (d) 2 C4; (a) dan (d) ≤ 2 kalimat; sembilan titik bulat + satu titik berpengaruh dengan alasan substantif; dua plot residual yang harus dipilah — sedikitnya satu memperlihatkan pelanggaran LINE; (d) memuat prediksi di luar rentang data | (a) Sedang · (b) Sedang · (c) Sedang · (d) Sulit |
| D | 102-1: D1, D2, D5, D8 · 081-1: D3, D4, D6, D7 · C4 · 25 | Delapan keputusan kisi-kisi §5 dalam satu kasus perbandingan dua kondisi | D1 2 C3, D2 3 C4, D3 4 C4, D4 4 C4, D5 4 C3, D6 3 C3, D7 3 C4, D8 2 C4; rancangan harus dinalar dari cara data dikumpulkan, bukan dari judul atau bentuk tabel, dan batang soal D3–D8 tidak menyebut rancangan (tidak memakai kata seperti "berpasangan" atau "selisih berpasangan", dan tidak meminta notasi yang hanya cocok untuk satu rancangan — notasi diminta "sesuai rancangan pada D2"); ringkasan data boleh memuat baris yang diperlukan untuk hitungan; ringkasan yang dicetak cukup untuk D2–D7 dengan rumus daftar kisi-kisi, dan hitungan pembanding D2 dicetak — pilihan rancangan, pola ringkasan, dan kunci D2 dicatat **hanya** di catatan privat penyusun varian; df ada di tabel-t; keputusan D5 dan letak kriteria praktis terhadap IK (di atas, di dalam, atau di bawah) boleh berbeda dari latihan, asalkan analisis D7 dapat dinalar dari IK; bentuk sebaran selisih dan n dipilih sehingga analisis TLP di D4 bermuatan (kesimpulannya boleh layak atau tidak layak); D1 memuat tiga ringkasan pada tiga skala berbeda, campuran sah dan tidak sah, dijawab pada tabel isian; D8 memuat klaim yang melampaui rancangan studi | D1 Sedang · D2 Sulit · D3 Sulit · D4 Sulit · D5 Sedang · D6 Sedang · D7 Sulit · D8 Sedang |

### 2. Yang wajib diubah per butir

Pada setiap butir: **konteks/kasus**, **data dan angka**, **urutan dan isi pilihan ganda** (letak kunci diacak ulang), dan **nama entitas** (lembaga, sistem, kolom, kota). Karena panduan ini publik, contoh di kolom kanan hanya menggambarkan **jenis** perubahan — naskah sebenarnya memakai konteks dan angka pilihan dosen sendiri, bukan contoh ini secara harfiah — dan tidak menetapkan kunci atau kesimpulan varian.

| Butir | Arah variasi (contoh ilustratif) |
|---|---|
| A1 | Klaim lain dengan arah persyaratan tertukar (mis. porsi pengguna ponsel lama di antara akun yang mengalami *crash*, atau porsi transaksi malam di antara transaksi yang dibatalkan) |
| A2 | Benda dan jumlah lain (mis. kartu RFID rusak di antara 10–12 kartu, atau berkas rusak di antara 9 cadangan); kejadian yang bukan bentuk Bab 4 L8 (mis. temuan pertama pada pengambilan ke-2 atau ke-4, atau hanya pengambilan kedua yang rusak) |
| A3 | Dua kategori lain dari satu objek (mis. status pesanan "dibatalkan" vs "selesai"; kelas jaringan satu perangkat) |
| A4 | Penyaring lain berprevalensi ≤ 1% (mis. deteksi transaksi janggal, deteksi akun ganda) dengan tindakan perbaikan lain; kunci ditentukan dari perhitungan PPV keempat opsi |
| A5 | Proses berulang lain yang melanggar satu syarat BINS (mis. percobaan tidak saling bebas, peluang berubah antarpercobaan, atau banyaknya percobaan tidak tetap) |
| A6 | Proporsi dan n lain (mis. n = 200 dengan p = 0,05, atau n = 400 dengan p = 0,02) dengan np bulat dan √(np(1 − p)) dua desimal yang rapi |
| A7 | Peubah kontinu lain (mis. suhu ruang server, panjang antrean waktu); urutan pernyataan diacak |
| A8 | Data lain; arah kemencengan boleh dibalik (mis. menceng kiri pada skor tugas yang mudah) |
| A9 | n kuadrat sempurna lain (mis. 36, 49, atau 100) dan s baru; kalimat data tidak meniru templat kisi-kisi §11 contoh B ("Dari sampel n … diperoleh x̄ = … dan s = …") |
| A10 | Bentuk populasi lain (mis. simetris tanpa pencilan dengan n = 12, atau agak menceng dengan n = 25) dengan kunci yang menyesuaikan tabel Bab 8 |
| A11 | Konteks dan interval baru (mis. waktu tunggu layanan akademik, atau proporsi pengguna aktif sebagai IK proporsi); boleh ditanyakan pernyataan yang keliru |
| A12 | Arah boleh sama atau dibalik (mis. dari IK 95% ke IK 99%, dari IK 99% ke IK 90%, atau dari IK 90% ke IK 95%) dengan rasio t yang memberi hasil bulat; nilai t dicetak bila df tidak ada di tabel |
| A13 | Sifat yang sama atau lain dalam konteks lain (mis. tak bias, efisien, atau konsisten), dengan pengecoh yang mencampur ketiga sifat itu |
| A14 | k, N, dan SS baru (mis. k = 3 atau 4, N antara 24 dan 44) dengan df₂ yang ada di tabel F; keputusan boleh menolak atau gagal menolak, dengan η² tetap ditafsirkan |
| A15 | Tabel 2 × 3 atau 3 × 2 lain (mis. jenis peramban × status unggahan); syarat boleh terpenuhi (≤ 20% sel < 5, minimum ≥ 1) atau tidak, asalkan tetap ada sel teramati < 5 sebagai pengecoh |
| B1 | Pencacahan lain dengan urutan bermakna (mis. kode kupon, susunan juri) dan peluang subhimpunan |
| B2 | Konteks lain (mis. laporan *bug* tanpa langkah reproduksi, atau akun tanpa foto profil); yang diketahui boleh, mis., P(B \| A) alih-alih P(A \| B) |
| B3 | Dua atau tiga tingkat seri dengan banyak replika berbeda (mis. 2 dan 3 replika); tingkat terlemah boleh tingkat mana pun; alternatif yang dicetak boleh yang lebih baik atau yang lebih buruk |
| B4 | Kejadian langka lain (mis. galat sinkronisasi per hari) dengan np = 1, 3, atau 4; boleh P(X ≥ 2) |
| B5 | Batas μ ± kσ lain (mis. k = 1, 2, atau 3) dan ekor lain (mis. ekor kiri atau kanan) |
| B6 | Selang lain (mis. 200–1.000 ms); persentil lain |
| B7 | μ, σ, n baru (mis. n = 36, 49, atau 64); ekor kiri atau kanan; perubahan galat baku lain (mis. separuh atau sepertiga) |
| B8 | Laporan lain dengan satu kekeliruan prosedur (mis. z padahal σ tidak diketahui, penyebut n alih-alih √n, atau df keliru); n kuadrat sempurna dengan df di tabel (mis. 16, 25, atau 36); kalimat data tidak meniru templat kisi-kisi §11 contoh B atau Bab 9 L2 ("Dari sampel n … diperoleh x̄ = … dan s = …"), dan perintahnya tetap meminta memperbaiki laporan, bukan "hitung interval kepercayaan 95% …" |
| B9 | Proporsi dan klaim lain (mis. klaim batas bawah "sedikitnya x%"); klaim boleh berada di dalam atau di luar interval |
| B10 | Anggaran, subkelompok, dan margin lain (mis. 400 atau 900 responden; subkelompok sepertiga atau seperempat responden; margin ±4 atau ±6 poin persen) dengan ukuran subkelompok hasil hitung yang pecahan |
| C1 | Penyaring lain dengan partisi tiga keadaan (mis. permintaan API dari tiga wilayah, berkas unggahan dari tiga jenis pengguna); prevalensi, sensitivitas, dan spesifisitas baru; kebijakan penyaringan pada subkelompok lain (mis. satu keadaan saja, atau dua dari tiga keadaan), dengan PPV subkelompok dicetak |
| C2 | Undian lain (mis. pembagian 10 asisten ke dua laboratorium, urutan 6 tim *hackathon*); "sama kelompok" sebagai gabungan kejadian saling lepas dengan langkah antara yang bukan bentuk Bab 4 L7(c) (mis. kelompok dengan ukuran berbeda, atau tiga unit di kelompok yang sama), dan uji kebebasan dua penempatan |
| C3 | Kedatangan lain (mis. pengunjung loket layanan, permintaan cetak di laboratorium) dengan λ bulat 2–4; target dalam satuan waktu lain (mis. paling banyak 2 menit per jam, atau 1 dari 20 menit); peluang bersyarat lain dengan konversi satuan (mis. "dalam 15 detik berikutnya" atau "tidak ada selama 20 detik berikutnya") |
| C4 | Besaran fisik lain (mis. suhu CPU, tegangan catu daya); delapan data bulat; persentil lain (mis. ke-80 atau ke-95); total n unit dengan tafsir peluangnya bagi pengelola |
| C5 | Pasangan peubah lain (mis. banyaknya ulasan produk dan penjualan bulanan toko daring, atau frekuensi pembaruan aplikasi dan banyaknya unduhan); titik berpengaruh dengan alasan substantif; pelanggaran LINE yang sama atau lain pada salah satu plot (mis. pola corong, pola melengkung, atau residual yang tidak saling bebas menurut urutan waktu), plot lain boleh tanpa pelanggaran atau dengan pelanggaran berbeda; prediksi di luar rentang pada nilai lain |
| D | Kasus perbandingan dua kondisi lain **di luar waktu respons atau waktu muat** (mis. konsumsi memori proses sebelum–sesudah *patch*, skor uji kegunaan dua rancangan antarmuka, atau akurasi dua model pada kumpulan uji yang sama); semua hitungan D5–D7 harus dapat dikerjakan dengan rumus daftar kisi-kisi ([Larangan](#3-larangan) no. 3); n dengan db di tabel-t dan galat baku yang mudah dihitung (mis. n kuadrat sempurna seperti 16, 25, atau 36; bila db tidak ada di tabel, nilai t dicetak); kriteria praktis boleh di atas, di dalam, atau di bawah IK (analisis D7 menyesuaikan); ringkasan D1 baru pada tiga skala (mis. ordinal, interval, nominal); klaim D8 baru yang melampaui rancangan (mis. generalisasi ke perangkat, waktu, atau pengguna lain) |

### 3. Larangan

1. Menyalin kalimat, data, atau angka latihan ini — termasuk pengecoh PG, atau kalimat soal yang hanya diganti angkanya.
2. Mengubah level Bloom, skor, atau Sub-CPMK butir dan sub-butir, atau peta aspek butir C.
3. Menambah materi di luar kisi-kisi (Minggu 1–15, indikator §4–§5), atau menuntut rumus di luar daftar kisi-kisi UTS §7 dan UAS §8 yang tidak dapat diturunkan dari rumus di daftar.
4. Memakai teks atau angka Latihan Soal Bab 1–14, contoh soal kisi-kisi UAS (§5 dan §11), Latihan UTS, atau contoh ilustratif tabel di atas secara harfiah, atau memparafrasakan soalnya dengan hanya mengganti konteks dan angka. Untuk Bagian D secara khusus: kerangka kisi-kisi §5, contoh §11 C (waktu respons 12 *endpoint* sebelum–sesudah *caching*), Bab 11 L6 (waktu muat halaman 15 perangkat sebelum–sesudah optimasi gambar), dan latihan ini sudah memakai domain waktu respons atau waktu muat — varian memakai domain lain. Untuk A2, B8, B9, B10, dan C2(b) secara khusus, langkah hitungnya sama dengan Bab 4 L8 (perkalian tanpa pengembalian), Bab 9 L2 dan kisi-kisi §11 contoh B (interval-t dari x̄ dan s), Bab 9 L4 (syarat dan IK proporsi), Bab 8 L8 dan Bab 9 L8 (margin galat dan ukuran sampel tanpa dugaan awal), serta Bab 4 L7(c) (dua anggota tertentu berada di kelompok terpilih) — varian **wajib** memakai bentuk pertanyaan yang berbeda dari soal-soal itu, bukan hanya konteks dan angka yang berbeda (mis. A2 tidak menanyakan "semuanya", "tidak ada", atau "sedikitnya satu"; B8 tetap memuat laporan keliru yang diperbaiki dan tidak memakai templat "Dari … diperoleh x̄ = … dan s = …"; B9 tetap memuat penilaian klaim; B10 tetap memuat margin subkelompok; C2(b) tetap menjumlahkan kejadian saling lepas).
5. Butir yang memerlukan nilai tabel di luar tabel yang dibagikan, tanpa nilai itu dicetak di soal; butir yang memerlukan tabel korelasi.
6. Menyimpan varian, kuncinya, skrip verifikasinya, atau catatan privat penyusun varian di repositori publik.

### 4. Prosedur mutu varian

1. **Selesaikan ulang setiap butir dengan Python** (pola blok kode di [pembahasan §5](latihan-uas-pembahasan.md#5-memeriksa-angka-dengan-python)) dan cocokkan dengan kunci varian. Periksa dengan `assert`: setiap angka kunci; skor per bagian 15/20/40/25; sebaran per pokok bahasan 8/12/14/10/12/10/12/14/8; Sub-CPMK 77/23; Bloom C2/C3/C4 = 8/65,5/26,5; aspek Bagian C 12/10/10/8; df dan nilai z yang dipakai ada di tabel. Pemeriksaan sifat yang menentukan kunci atau kesimpulan varian (mis. rancangan D dan pola ringkasannya, keputusan uji di D5, letak kriteria praktis terhadap IK di D7, kapasitas yang memenuhi target di C3, hasil pemeriksaan syarat di B9) dicatat di catatan privat penyusun varian, bukan di dokumen publik ini.
2. **Pilihan ganda:** penelaah menjawab tanpa kunci untuk memastikan **tepat satu** jawaban benar per butir; letak kunci diacak ulang (sebaran huruf seimbang dan berbeda dari urutan kunci latihan); panjang opsi diperiksa agar kunci tidak menonjol.
3. **Cek waktu — uji coba berwaktu** (KENDALI `T1-10`, pola `T0-15`). Penguji coba: 2–3 asisten atau mahasiswa senior yang **belum membaca latihan maupun varian** (latihan ini publik sejak 9 Oktober 2026), dalam kondisi ujian: **120 menit, *closed book*, tulisan tangan, alat bantu sesuai kisi-kisi (kalkulator ilmiah *non-programmable*; tabel Normal, t, chi-square, dan F), tanpa AI**; catat waktu per bagian. Uji coba pada latihan ini **wajib** dan dilakukan **sebelum varian disusun**: hasilnya menentukan pemangkasan yang diterapkan, dan sesudah itu barulah invarian per butir dibekukan ([Invarian per butir](#1-invarian-per-butir)). Uji coba juga **wajib** pada varian sebelum difinalkan, oleh 2–3 penguji coba yang belum melihat varian maupun kuncinya, dengan ambang yang sama. Keputusan menurut **median** waktu penguji coba: **≤ 80 menit** (≤ 2/3 durasi) → lolos; **> 80 dan ≤ 90 menit** (≤ 3/4 durasi) → bersyarat: terapkan [cadangan pemangkasan pertama (sisa)](#cadangan-pemangkasan-waktu), yang hanya cukup untuk median sampai **±80,5 menit**; di atasnya dosen juga menetapkan [pemangkasan lanjutan](#cadangan-pemangkasan-waktu), lalu uji ulang; **> 90 menit** → dosen menetapkan pemangkasan lanjutan, lalu uji ulang. Dasar ambang: penguji coba yang menguasai materi bekerja ±1,5× lebih cepat daripada rerata mahasiswa, sehingga 2/3 durasi bagi penguji coba setara dengan seluruh durasi bagi rerata mahasiswa. Data pelengkap (bila dosen memintanya): catatan waktu per bagian dari mahasiswa yang mengerjakan latihan ini, diserahkan tanpa nama; yang dipakai dan dicatat hanya rekap agregat (median dan sebaran waktu per bagian).
4. **Telaah sejawat** memakai [checklist-verifikasi §C](../../../00-pedoman-obe/checklist-verifikasi.md#c-lembar-telaah-sejawat).
5. **Simpan** varian, kunci, skrip verifikasinya, dan catatan privat penyusun varian di penyimpanan privat, tidak di repositori. Untuk `mutu/02`, catat hanya angka agregat.

---

## Catatan untuk Dosen

1. **Penandaan.** Sub-CPMK per butir menurut penandaan butir (D-03(a); konvensi butir utuh untuk D4): 77% skor ke `PS-Sub-CPMK081-1`, 23% ke `PS-Sub-CPMK102-1` — atau 74,5/25,5 bila D4 dibagi menurut isi (no. 2); nilai akhir tetap memakai alokasi registri (UAS → 081-1). Usulan revisi alokasi masuk `T2-08`.
2. **Kisi-kisi §3 vs §5.** Kerangka D (§5) adalah satu kasus uji dua sampel; bila semua butirnya dihitung sebagai uji hipotesis, porsinya ±20 poin, melebihi bobot §3 (14%). Latihan menjaga total §3 menurut konvensi penandaan butir utuh dengan menandai D4, D6, D8 ke Minggu 9, 10, 1 dan tidak memuat butir Minggu 11–12 di A–C. D4 sendiri juga menguji indikator §4.7 (memeriksa asumsi uji); menurut isi, porsi uji hipotesis ±16,5 poin, dan pembagi ketercapaian menjadi 74,5/25,5 alih-alih 77/23 ([Cara menghitung ketercapaian](#cara-menghitung-ketercapaian-agregat)). Selain itu kisi-kisi §1 menyebut "penekanan Minggu 9–14", sedangkan bobot §3 untuk Minggu 9–14 hanya 44%. Perlu diputuskan: pertahankan §3, atau sesuaikan bobotnya.
3. **Modul Minggu 16.** §2.4 modul memuat kerangka D yang berbeda dari kisi-kisi §5 (memodelkan distribusi, menghitung probabilitas, dst.); latihan mengikuti kisi-kisi §5. "Strategi Mengerjakan" modul membagi 115 menit ditambah 5 menit memeriksa tanpa waktu membaca, sedangkan model waktu latihan memakai 5 menit membaca dan sedikitnya 5 menit memeriksa.
4. **Ketentuan skor (usulan).** Penerapan aturan kisi-kisi §6 pada Bagian B dan D; bobot aspek 30/25/25/20 yang dipenuhi tepat pada total Bagian C dan per butir dengan selisih paling besar 5 poin persen; tafsir "kehilangan maksimal 30%" sebagai 30% skor butir; aturan "asumsi yang diminta" per baris pedoman skor; pengurangan −50% interpretasi sebagai batas atas sekali per butir (agar kalimat yang sama tidak dihukum dua kali); serta kesalahan berantai, toleransi pembulatan, kelipatan 0,25, dan jawaban alternatif sahih ([pembahasan §0](latihan-uas-pembahasan.md#0-ketentuan-umum-penskoran)) — termasuk H₀: μ_d ≤ 50 di D3 sebagai rumusan alternatif yang dinilai penuh, dengan D5 mengikuti jalurnya. Penerapan kisi-kisi §9 no. 2 ("memakai uji bebas pada data berpasangan → kehilangan aspek rumus") juga perlu dikonfirmasi: latihan menafsirkannya sebagai baris R D2, D5 (SE dan df), dan D6 (rumus interval) bernilai 0, sedangkan baris H dan I D5–D7 dinilai berantai (pembahasan §0.1) — kecuali baris t D5, yang bernilai 0 karena t Welch sudah dicetak di D2 dan nilai yang dicetak tidak diberi skor (pembahasan §0.3); jadi kesalahan ini dikecualikan dari aturan berantai §0.2 no. 1.
5. **Rumus di luar daftar hafalan** — Uniform, ekor dan CDF Eksponensial, Cohen's d berpasangan, SD jumlah n peubah bebas, R² = r², margin galat proporsi dari n — diterima lewat jalur penurunan (pembahasan §0.3); pertimbangkan menambahkannya ke kisi-kisi §8.
6. **Waktu — putuskan sebelum uji coba.** Untuk menutup kelebihan model (sebelumnya ±119,4–125 menit), penyusun sudah menerapkan sisa cadangan pertama dan tiga pemangkasan yang mengubah peta skor, peta aspek, atau Bloom sub-butir **milik latihan ini** tanpa mengubah kisi-kisi: C4(d) tanpa pernyataan teknisi (C4(d) dan butir C4 menjadi C3; skor C4 total 27 → 26,5), PPV kebijakan C1(c) dicetak (peta aspek C1 tetap), dan C2 menjadi tiga sub-butir (skor (a) dan (b) menjadi 3; peta aspek, minggu, dan Bloom C2 tetap) ([Cadangan pemangkasan waktu](#cadangan-pemangkasan-waktu) no. 6–7). Model kini ±104,1–109,7 menit kerja + 10 menit membaca dan memeriksa = **±114,1–119,7 menit** — muat dalam 120 menit, tetapi pada kecepatan baca terendah sisanya hanya ±0,3 menit, dan pada hitungan ketat (setiap angka dalam ungkapan hitungan dihitung satu kata) totalnya ±118–123,6 menit ([Model waktu](#model-waktu)). Yang perlu diputuskan **sebelum** uji coba: (a) mengesahkan ketiga pemangkasan yang mengubah peta itu, atau mengembalikannya; (b) menyetujui cadangan pertama (sisa); (c) bila menghendaki sisa waktu yang lebih lebar, memilih pemangkasan lanjutan (sisa) atau revisi kisi-kisi §2. Uji coba berwaktu **wajib** sebelum varian disusun, dan invarian per butir baru dibekukan sesudahnya ([Invarian per butir](#1-invarian-per-butir)).
7. **Indikator yang tidak diuji** (Geometrik, tanda *overdispersion*, Pearson vs Spearman, menghitung χ² dan inflasi galat Tipe I, alasan uji lanjut hanya setelah ANOVA signifikan, uji-t satu sampel atas data mentah, menghitung uji-t dua sampel bebas (t Welch dicetak di D2 sesudah pemangkasan dan hanya dianalisis), IK-z) — akibat porsi §3; sebagian sudah diuji di Latihan UTS. Dari sepuluh konsep inti kisi-kisi §7, **kuasa uji** (bagian konsep 7) tidak diuji sebagai unsur bernilai — hanya dianjurkan di penjelasan D2 ([pemetaan §7](#sepuluh-konsep-inti-kisi-kisi-7)). Bila dosen ingin salah satunya masuk UAS, cetak biru diubah lebih dulu, lalu latihan diperbarui.
8. **Level Bloom UAS.** RPS Minggu 16 menulis UAS C3–C4, sedangkan kisi-kisi §2 menetapkan Bagian A C2–C3 dan latihan memuat 8 poin C2 (Bagian A). Perlu diselaraskan: RPS Minggu 16 dengan kisi-kisi §2 dan cetak biru ini (masalah sejenis untuk UTS tercatat di KENDALI `T0-19`).
9. **Data rekaan.** Seluruh angka rekaan; tidak ada merek atau lembaga nyata. Data C5 sembilan UMKM bilangan bulat dengan x̄ = 12, s_x = 5, ȳ = 30, s_y = 8, r = 0,80 tepat; ringkasan D konsisten (korelasi implisit waktu lama–baru ±0,87). Diagram pencar C5 dibulatkan ke kelipatan 2 juta (dinyatakan di soal); kedua plot residual C5(c) digambar tangan untuk data rekaan dua kota lain dengan prediksi 15–50 juta, sesuai rentang pengikut 2–25 ribu yang dinyatakan di soal.
10. **Nilai Islam** hadir secara ringan: kotak *Amanah berlatih* di lembar soal dan catatan kejujuran berdagang (tidak dinilai) di pembahasan C5(d); tidak ada butir bernilai yang bergantung pada rujukan dalil.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
