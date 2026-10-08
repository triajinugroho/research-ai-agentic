---
id: uai-if52510033-latihan-uts-cetak-biru
tipe: asesmen
judul: "Latihan UTS — Probabilitas dan Statistik — Cetak Biru Butir dan Panduan Varian"
kode_mk: IF52510033
nama_mk: Probabilitas dan Statistik
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-08
---

# Cetak Biru Butir dan Panduan Varian — Latihan UTS Probabilitas dan Statistik

## Probabilitas dan Statistik — IF52510033

> **Latihan UTS — bukan naskah UTS.** Cetak biru ini menyertai simulasi lengkap UTS Probabilitas dan Statistik Ganjil 2026/2027 untuk berlatih: komposisi, durasi (100 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UTS. Naskah UTS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> Berkas ini untuk dosen dan penelaah: tabel butir, ringkasan per Sub-CPMK/Bloom/bagian, dan [panduan menyusun varian](#panduan-menyusun-varian-naskah-uts-sebenarnya). Pasangan berkas: [latihan UTS](latihan-uts.md) dan [pembahasan dan pedoman skor](latihan-uts-pembahasan.md).

---

## Identitas dan Dasar Penyusunan

| Komponen | Isi |
|---|---|
| Mata kuliah | Probabilitas dan Statistik (IF52510033), semester 1 |
| Asesmen | Latihan UTS (simulasi) untuk UTS Semester Ganjil 2026/2027, Minggu 8 — UTS berbobot 25% nilai akhir |
| Penyusun | Tri Aji Nugroho, S.T., M.T. |
| Butir kendali | [KENDALI-EKSEKUSI](../../../00-meta/KENDALI-EKSEKUSI.md): `T0-02` (naskah UTS + kunci = varian privat dari latihan ini), `T0-15` (telaah sejawat dan uji coba berwaktu), `T0-18` (penyempurnaan kisi-kisi) |
| Acuan | [Kisi-kisi UTS](kisi-kisi-uts.md) §1–§7, [RPS Minggu 8](../01-rps/rps-probabilitas-dan-statistik.md#minggu-8-ujian-tengah-semester-uts), [RTM §F.1](../02-rtm/rtm-probabilitas-dan-statistik.md#f1-ujian-tengah-semester-u-01), registri [`15b-subcpmk-tingkat-1-semester-1-2.md`](../../../00-kurikulum-if-2025-revisi-2026/15b-subcpmk-tingkat-1-semester-1-2.md) |
| Sub-CPMK registri | `PS-Sub-CPMK081-1` (CPL08/CPMK081, C3–C4): konsep probabilitas, peubah acak, distribusi. `PS-Sub-CPMK102-1` (CPL10/CPMK102, C3–C4/P2–P3): statistika deskriptif dan visualisasi |
| Penandaan | Penandaan Sub-CPMK per butir menurut isi adalah bawaan sementara D-03(a); bobot nilai akhir tetap mengikuti registri (UTS 25% → `PS-Sub-CPMK102-1`). |

**Aturan penandaan.** Butir tentang Minggu 1–3 (data, deskriptif, visualisasi) dan butir D tentang skala, ringkasan, serta batas inferensi → `PS-Sub-CPMK102-1`. Butir tentang Minggu 4–7 (probabilitas, Bayes, distribusi diskret dan kontinu) → `PS-Sub-CPMK081-1`. Pembagian ini mengikuti indikator mingguan RPS (Minggu 1–3 → 102-1; Minggu 4–7 → 081-1). Lembar latihan hanya mencantumkan level Bloom dan skor; Sub-CPMK per butir tercantum di pembahasan dan di berkas ini.

---

## Kesesuaian dengan Kisi-Kisi

### Komposisi, skor, dan waktu

| Bagian | Bentuk | Butir (kisi-kisi → latihan) | Skor (kisi-kisi → latihan) | Bloom kisi-kisi | Bloom latihan | Waktu saran kisi-kisi | Taksiran penyusun |
|---|---|---|---|---|---|---|---|
| A | Pilihan ganda | 15 → 15 | 20 → 20 | C2–C3 | 5 butir C2, 10 butir C3 | 20 menit | 18 menit |
| B | Isian / hitungan pendek | 8 → 8 | 25 → 25 | C3 | 8 butir C3 | 25 menit | 21,5 menit |
| C | Uraian terstruktur | 4 → 4 | 40 → 40 | C3–C4 | 4 butir C3–C4 (sub-butir C3: 25 poin; C4: 15 poin) | 40 menit | 33 menit |
| D | Studi kasus terpadu | 1 → 1 | 15 → 15 | C4 | 1 butir C4 (sub-butir C3: 8 poin; C4: 7 poin) | 15 menit | 12,5 menit |
| **Total** | | **28 → 28** | **100 → 100** | | | **100 menit** | **85 menit** |

**Taksiran waktu — belum ada margin; panjang masih dikalibrasi.** Taksiran penyusun: ±85 menit kerja untuk ±52 unit jawaban (15 PG, 16 sub-butir B, 15 sub-butir C, 6 sub-butir D), termasuk membaca skenario dan menulis ±16 jawaban berupa kalimat (alasan singkat, tafsiran, atau paragraf analisis). Sepuluh jawaban kalimat terpanjang diberi **batas kalimat** — C1(b), C1(d), C2(c), C4(d), dan D2 paling banyak 3 kalimat; C3(d) dan D3 paling banyak 4; bagian asumsi C3(c), tafsiran C4(a), dan D6 paling banyak 2; hitungan tidak termasuk batas. Batas ini tidak mengubah Sub-CPMK, Bloom, skor, atau cakupan indikator, dan memangkas taksiran penyusun dari ±88 menjadi ±85 menit (C1(b), C2(c), C3(d), C4(a), D2, dan D3 masing-masing −0,5 menit). Waktu membaca seluruh soal (5 menit) dan memeriksa ulang harus diambil dari 100 menit yang sama:

| Taksiran waktu kerja | + membaca 5 menit + memeriksa 7 menit | + membaca 5 menit + memeriksa 10 menit ([modul Minggu 8](../03-modules/week-08-uts-review-dan-ujian.md#strategi-mengerjakan-ujian): "Sisakan 10 menit") |
|---|---|---|
| Penyusun, dengan batas kalimat: ±85 menit (A 18, B 21,5, C 33, D 12,5) | 97 menit | **100 menit — tanpa margin** |
| Tiga taksiran lain, dibuat sebelum batas kalimat: independen ±92–95, telaah sebelum terbit ±96, telaah kedua ±95–100 menit; dikurangi penghematan batas kalimat ±3–5 menit (taksiran): ±87–97 menit | ±99–109 menit | **±102–112 menit** |

Jadi latihan ini **belum terbukti muat dalam 100 menit**: dengan batas kalimat hanya taksiran penyusun yang muat, tanpa margin; latihan menyatakan hal ini terus terang kepada mahasiswa (Petunjuk 5). Karena varian memakai cetak biru yang sama, panjangnya diputuskan **sebelum varian ditetapkan**: dosen mengonfirmasi batas kalimat, lalu **uji coba berwaktu** yang wajib menentukan apakah [cadangan pemangkasan](#cadangan-pemangkasan-waktu) diterapkan ([prosedur mutu varian](#4-prosedur-mutu-varian) no. 3).

### Cadangan pemangkasan waktu

Dipakai menurut hasil uji coba berwaktu ([prosedur mutu varian](#4-prosedur-mutu-varian) no. 3). Pemangkasan yang dipakai diterapkan sama pada latihan, pembahasan, dan cetak biru (kunci, Tabel Butir, peta aspek), lalu pada varian.

**Cadangan pertama** — diterapkan bila hasil uji coba **bersyarat**; perlu disetujui dosen **sebelum** uji coba agar dapat langsung diterapkan. Setiap pemangkasan menjaga Sub-CPMK, level Bloom, dan skor setiap baris [Tabel Butir](#tabel-butir) serta peta aspek butir C; poin hanya dipindahkan di dalam baris yang sama. Urutannya dari yang paling sedikit mengurangi cakupan; no. 8 dan 9 masing-masing melepas satu indikator kisi-kisi. Angka hemat adalah taksiran penyusun.

| No | Pemangkasan | Pemindahan poin (skor baris tetap) | Hemat (± menit kerja mahasiswa) |
|---|---|---|---|
| 1 | C2(b): nilai C(96,3) = 142.880 dicetak di soal; penjelasan aturan pencacahan tetap diminta | Prosedur "rumus C(n,r)" beralih ke C(36,2) (0,5); hitung: 37.800 (0,5) dan 0,2646 (0,5) | 0,5 |
| 2 | C3(b): baris "Ditulis AI tanpa diungkapkan" pada kerangka tabel dicetak terisi (90 · 10 · 100) | Prosedur (1): baris "Ditulis sendiri" dan baris total terisi lengkap dan konsisten; hitung: 57, 1.843, 147, 1.853 (0,5) dan 0,9946 (0,5) | 0,25–0,5 |
| 3 | C1(a): jawaban ditulis pada tabel isian ukuran (mean, median, s, Q1, Q3, IQR, pagar, pencilan) | Tidak berubah | 0,25–0,5 |
| 4 | B2: μ = 33 detik dicetak di soal | Langkah "μ = 33 dan Σ(x − μ)² = 30" menjadi "Σ(x − μ)² = 30" (0,5) | 0,25 |
| 5 | A1: tiap opsi memuat dua pasangan, bukan tiga; tiap pengecoh tetap memuat satu pelanggaran khas | — | 0,25–0,5 |
| 6 | D1: dua variabel (`rating_kepuasan` dan `jam_daftar`); skala rasio tetap diuji di A1 | 0,75 per skala + 0,5 ukuran pemusatan | 0,25–0,5 |
| 7 | D3: cukup **satu** asumsi (laju konstan) yang diperiksa dengan tabel | Distribusi + parameter 0,75 · asumsi 0,5 · pemeriksaan dengan tabel 1 · keputusan 0,75 | 0,25–0,5 |
| 8 | C4(a): tanpa pertanyaan saling lepas — melepas indikator "membedakan saling lepas dan saling bebas" (kisi-kisi §4.5) | Interpretasi: tidak bebas 0,5 + penyebab bersama 0,5 | 0,25–0,5 |
| 9 | D4: tanpa (iii) — melepas indikator "hubungan Poisson–Eksponensial" (kisi-kisi §4.7) | (i) 1,5 · (ii) 1,5 | 0,25–0,5 |
| | **Total** | | **±2,5–4,25** |

Hemat cadangan pertama lebih kecil daripada lebar rentang bersyarat (setara sampai ±12 menit kerja mahasiswa), sehingga pilihan pemangkasan lanjutan sebaiknya ditetapkan dosen sebelum uji coba.

**Pemangkasan lanjutan** — bila median > 75 menit; ditetapkan dosen, lalu uji ulang. Pilihannya: pemangkasan yang mengubah peta skor atau Bloom sub-butir — mis. C3(c) cukup analisis asumsi dengan posterior berantai tercetak (1,5 poin C3 dipindah ke C3(a) dan C3(b); hemat ±1,5–2 menit), mencetak hasil antara lain pada butir hitung B/C, atau menghapus satu sub-butir — yang diterapkan sama pada latihan, pembahasan, dan cetak biru; atau pengurangan butir lewat revisi kisi-kisi (`T0-18`).

### Sebaran materi (kisi-kisi §3)

| Minggu | Pokok bahasan | Target | A | B | C | D | Total latihan |
|---|---|---|---|---|---|---|---|
| 1 | Jenis data, skala, populasi–sampel | 8 | 3 | 2 | – | 3 | **8** |
| 2 | Pemusatan, penyebaran, posisi, pencilan | 20 | 9 | 2 | 6 | 3 | **20** |
| 3 | Visualisasi dan pemilihan grafik | 12 | 8 | – | 4 | – | **12** |
| 4 | Aksioma, penjumlahan/perkalian, bersyarat, pencacahan | 20 | – | 10 | 10 | – | **20** |
| 5 | Probabilitas total, Bayes, kebebasan | 18 | – | – | 15 | 3 | **18** |
| 6 | Distribusi diskret | 12 | – | 4 | 5 | 3 | **12** |
| 7 | Distribusi kontinu | 10 | – | 7 | – | 3 | **10** |
| | **Total** | **100** | **20** | **25** | **40** | **15** | **100** |

Kolom "Bagian" kisi-kisi §3 dipatuhi untuk A, B, dan C. Untuk D, kisi-kisi §3 mengaitkan D hanya dengan Minggu 5 dan 7, sedangkan kerangka D di §5 menuntut skala (Minggu 1), ukuran ringkasan (Minggu 2), dan distribusi jumlah galat per jam (Minggu 6). Latihan mengikuti §5 butir demi butir sambil menjaga total per minggu tepat sama dengan §3.

### Aturan alat bantu

Sama dengan kisi-kisi §1, RPS Minggu 8, dan RTM §F.1: *closed book*; kalkulator ilmiah *non-programmable* dan alat tulis; tabel Normal baku dan tabel-t dibagikan pengawas; rumus tidak disediakan (tanpa lembar rumus); AI dilarang. Butir yang memerlukan tabel Normal: B7, B8(a). Butir yang memerlukan fungsi eksponensial kalkulator: D4. Tidak ada butir yang memerlukan tabel-t. Dua rumus ekor yang tidak ada di daftar rumus kisi-kisi §7 (Geometrik P(X > k), dipakai B6; Eksponensial P(T > t), dipakai D4) dapat diturunkan dari rumus di daftar; pembahasan menunjukkan jalurnya.

---

## Tabel Butir

Kolom *Indikator* merujuk subbagian kisi-kisi §4 (4.1–4.7) dan kerangka D di §5. Waktu dalam menit (taksiran penyusun).

| No | Indikator (kisi-kisi) | Mg | Sub-CPMK | Bloom | Skor | Waktu |
|---|---|---|---|---|---|---|
| A1 | 4.1 Menentukan operasi statistik yang sah untuk sebuah skala; tipe data ≠ skala | 1 | PS-Sub-CPMK102-1 | C3 | 1,5 | 2 |
| A2 | 4.1 Mengenali bias sampel (kenyamanan) dan mengapa memperbesar n tidak memperbaikinya | 1 | PS-Sub-CPMK102-1 | C3 | 1,5 | 1 |
| A3 | 4.2 Menafsirkan arah kemencengan dari hubungan mean–median | 2 | PS-Sub-CPMK102-1 | C2 | 1 | 1 |
| A4 | 4.2 Menjelaskan mengapa laporan kinerja sistem memakai p95/p99, bukan rata-rata | 2 | PS-Sub-CPMK102-1 | C2 | 1 | 1 |
| A5 | 4.2 Menentukan ukuran yang tepat berdasarkan bentuk sebaran (ketahanan terhadap pencilan) | 2 | PS-Sub-CPMK102-1 | C2 | 1 | 1 |
| A6 | 4.2 Menghitung koefisien variasi untuk membandingkan dua kelompok berskala berbeda | 2 | PS-Sub-CPMK102-1 | C3 | 1,5 | 1,5 |
| A7 | 4.2 Menerapkan makna kuartil sebagai ukuran posisi (±25% data antara median dan Q3) | 2 | PS-Sub-CPMK102-1 | C3 | 1,5 | 1 |
| A8 | 4.2 Menghitung median dan modus secara manual (tabel frekuensi) | 2 | PS-Sub-CPMK102-1 | C3 | 1,5 | 1,5 |
| A9 | 4.2 Menghitung mean secara manual (rata-rata gabungan) | 2 | PS-Sub-CPMK102-1 | C3 | 1,5 | 1,5 |
| A10 | 4.3 Memilih jenis grafik berdasarkan jenis data dan pertanyaan analisis | 3 | PS-Sub-CPMK102-1 | C3 | 1,5 | 1 |
| A11 | 4.3 Mengenali empat teknik penyajian menyesatkan — pemotongan rentang data (Bab 3 §3.6.1(c)) | 3 | PS-Sub-CPMK102-1 | C3 | 1,5 | 1 |
| A12 | 4.3 Menjelaskan dampak lebar bin histogram terhadap kesan pembaca | 3 | PS-Sub-CPMK102-1 | C2 | 1 | 1 |
| A13 | 4.3 Membaca boxplot (lima angka ringkasan dan pencilan) | 3 | PS-Sub-CPMK102-1 | C3 | 1,5 | 1,5 |
| A14 | 4.3 Unsur wajib grafik yang jujur — menjelaskan dampak unsur yang hilang (C2, bukan sekadar menyebutkan) | 3 | PS-Sub-CPMK102-1 | C2 | 1 | 1 |
| A15 | 4.3 Memilih jenis grafik (perbandingan proporsi yang berdekatan) | 3 | PS-Sub-CPMK102-1 | C3 | 1,5 | 1 |
| B1 | 4.1 Tipe data komputer ≠ skala; operasi yang sah | 1 | PS-Sub-CPMK102-1 | C3 | 2 | 2 |
| B2 | 4.2 Varians dan simpangan baku populasi (penyebut N) beserta alasan pemilihan penyebut (n vs n − 1) | 2 | PS-Sub-CPMK102-1 | C3 | 2 | 2,5 |
| B3 | 4.4 Menghitung P(n,r) dan C(n,r); memilih antara keduanya | 4 | PS-Sub-CPMK081-1 | C3 | 3 | 2,5 |
| B4 | 4.4 Menerapkan aksioma Kolmogorov, aturan komplemen dan penjumlahan | 4 | PS-Sub-CPMK081-1 | C3 | 3 | 2 |
| B5 | 4.4 Menerapkan aturan perkalian berantai dan komplemen; menghitung probabilitas bersyarat | 4 | PS-Sub-CPMK081-1 | C3 | 4 | 2,5 |
| B6 | 4.6 Menerapkan Geometrik, E[X], CDF (batas k), dan sifat tanpa memori | 6 | PS-Sub-CPMK081-1 | C3 | 4 | 3,5 |
| B7 | 4.7 Membaca tabel Normal baku untuk P(X < a) dan P(a < X < b) | 7 | PS-Sub-CPMK081-1 | C3 | 3 | 3 |
| B8 | 4.7 Mencari nilai x dari persentil; aturan empiris 68–95–99,7 | 7 | PS-Sub-CPMK081-1 | C3 | 4 | 3,5 |
| C1a | 4.2 Mean, median, s (n − 1; Σ(x − x̄)² tercetak), kuartil, IQR, batas pencilan | 2 | PS-Sub-CPMK102-1 | C3 | 4 | 3,5 |
| C1b | 4.2 Ukuran pemusatan/penyebaran yang tepat berdasarkan bentuk sebaran (memakai hasil (a) dan ringkasan B, tanpa hitungan baru; ≤ 3 kalimat) | 2 | PS-Sub-CPMK102-1 | C4 | 2 | 1,5 |
| C1c | 4.3 Boxplot (lima angka ringkasan dan pencilan); boxplot B tercetak, mahasiswa menggambar A | 3 | PS-Sub-CPMK102-1 | C3 | 2 | 1,5 |
| C1d | 4.3 Keterbatasan boxplot dalam menampilkan bimodalitas (8 dari 9 tiket B dalam dua jenis; median diwakili 1 tiket; ≤ 3 kalimat) | 3 | PS-Sub-CPMK102-1 | C4 | 2 | 1,5 |
| C2a | 4.4 Menghitung P(A\|B) dan P(B\|A); aturan penjumlahan umum | 4 | PS-Sub-CPMK081-1 | C3 | 3,5 | 2,5 |
| C2b | 4.4 Kombinasi, aturan perkalian pencacahan, dan probabilitas tanpa pengembalian (penjelasan aturan diminta) | 4 | PS-Sub-CPMK081-1 | C3 | 4 | 2,5 |
| C2c | 4.4 Membedakan P(A\|B) dan P(B\|A) (laju vs porsi) dalam pengambilan keputusan (≤ 3 kalimat) | 4 | PS-Sub-CPMK081-1 | C4 | 2,5 | 2 |
| C3a | 4.5 Probabilitas total; Teorema Bayes; prior, *likelihood*, *evidence*, posterior; asumsi prior (diminta) | 5 | PS-Sub-CPMK081-1 | C3 | 3 | 3 |
| C3b | 4.5 *Base rate fallacy* dengan frekuensi harapan (kerangka tabel tercetak); P(ditulis sendiri \| tidak ditandai) | 5 | PS-Sub-CPMK081-1 | C3 | 2 | 1,5 |
| C3c | 4.5 Teorema Bayes berantai (posterior sebagai prior baru) — C3, 1,5 poin; analisis asumsi bebas bersyarat (diminta; ≤ 2 kalimat) — C4, 1 poin | 5 | PS-Sub-CPMK081-1 | C3–C4 | 2,5 | 2,5 |
| C3d | 4.5 Mengapa tes akurat menghasilkan banyak alarm palsu — tafsiran angka (a)–(c), implikasi keputusan, satu langkah prosedur; keterbatasan angka uji (diminta); ≤ 4 kalimat | 5 | PS-Sub-CPMK081-1 | C4 | 2,5 | 2,5 |
| C4a | 4.5 Saling lepas vs saling bebas; uji kebebasan dengan definisi formal (tafsiran ≤ 2 kalimat) | 5 | PS-Sub-CPMK081-1 | C4 | 3 | 2,5 |
| C4b | 4.5 Keandalan sistem gabungan seri–paralel (*load balancer* + replika); batas keandalan dan titik kegagalan tunggal | 5 | PS-Sub-CPMK081-1 | C3 | 2 | 1,5 |
| C4c | 4.6 Memeriksa BINS; P(X ≥ k) dan E[X] Binomial (kuorum mayoritas ≥ 3 dari 4 server) | 6 | PS-Sub-CPMK081-1 | C3 | 3 | 3 |
| C4d | 4.6 Memeriksa BINS — dampak pelanggaran kebebasan (stem dibatasi pada temuan uji kebebasan di (a); ≤ 3 kalimat) | 6 | PS-Sub-CPMK081-1 | C4 | 2 | 1,5 |
| D1 | §5 butir 1 — jenis dan skala variabel (4.1) | 1 | PS-Sub-CPMK102-1 | C3 | 2 | 2,5 |
| D2 | §5 butir 2 — memilih dan menghitung ukuran ringkasan dengan alasan (4.2; ≤ 3 kalimat di luar hitungan) | 2 | PS-Sub-CPMK102-1 | C4 | 3 | 2,5 |
| D3 | §5 butir 3 — memilih distribusi jumlah galat per jam beserta asumsinya (4.6; ≤ 4 kalimat di luar hitungan) | 6 | PS-Sub-CPMK081-1 | C4 | 3 | 2,5 |
| D4 | §5 butir 4 — menghitung probabilitas dari distribusi itu; hubungan Poisson–Eksponensial dijelaskan tanpa hitung ulang (4.7) | 7 | PS-Sub-CPMK081-1 | C3 | 3 | 2 |
| D5 | §5 butir 5 — Teorema Bayes pada informasi tambahan; keputusan dan probabilitas keputusan keliru (4.5) | 5 | PS-Sub-CPMK081-1 | C3 | 3 | 2 |
| D6 | §5 butir 6 — apa yang **tidak** dapat disimpulkan (batas inferensi, 4.1; ≤ 2 kalimat) | 1 | PS-Sub-CPMK102-1 | C4 | 1 | 1 |
| | **Total** | | | | **100** | **85** |

Level Bloom butir utuh: A dan B sesuai baris; C1–C4 = C3–C4; D = C4. Tidak ada butir C1 murni ("sebutkan"); kelima butir C2 berada di Bagian A, sesuai rentang C2–C3 kisi-kisi. Sub-butir C3(c) memuat tugas C3 (hitung) dan C4 (analisis asumsi), sehingga skornya dibagi 1,5 (C3) + 1 (C4). Kata kerja perintah mengikuti taksonomi repositori ([`16-taksonomi-bloom-cap.md`](../../../00-kurikulum-if-2025-revisi-2026/16-taksonomi-bloom-cap.md), [`taksonomi-cap.md`](../../../00-pedoman-obe/taksonomi-cap.md)): "menilai" (C5) tidak dipakai. Sub-butir C4 memakai "analisis" (C1(b), C2(c), C3(c), C3(d), D2), "uji" (C4(a); *menguji* termasuk C4 di taksonomi repositori), atau pertanyaan analitis yang menuntut penguraian hubungan: C1(d) apa yang tidak tampak pada boxplot, C4(d) syarat yang dilanggar dan arah dampaknya, D3 keputusan pemodelan dari pemeriksaan tabel, D6 kesimpulan yang tidak dapat ditarik. Varian mempertahankan bentuk perintah ini.

---

## Ringkasan per Sub-CPMK, Bloom, dan Bagian

### Skor per Sub-CPMK

| Sub-CPMK | A | B | C | D | **Total skor** | **% skor UTS** | Butir |
|---|---|---|---|---|---|---|---|
| `PS-Sub-CPMK102-1` | 20 | 4 | 10 | 6 | **40** | **40%** | A1–A15, B1, B2, C1, D1, D2, D6 |
| `PS-Sub-CPMK081-1` | – | 21 | 30 | 9 | **60** | **60%** | B3–B8, C2, C3, C4, D3, D4, D5 |
| **Total** | 20 | 25 | 40 | 15 | **100** | **100%** | |

### Skor per level Bloom

| Bloom | `PS-Sub-CPMK102-1` | `PS-Sub-CPMK081-1` | Total skor | % |
|---|---|---|---|---|
| C2 | 5 | – | 5 | 5% |
| C3 | 27 | 46 | 73 | 73% |
| C4 | 8 | 14 | 22 | 22% |
| **Total** | **40** | **60** | **100** | **100%** |

### Skor per bagian dan level Bloom

| Bagian | C2 | C3 | C4 | Total |
|---|---|---|---|---|
| A | 5 | 15 | – | 20 |
| B | – | 25 | – | 25 |
| C | – | 25 | 15 | 40 |
| D | – | 8 | 7 | 15 |
| **Total** | **5** | **73** | **22** | **100** |

- Butir utuh ≥ C3: **23 dari 28 (82%)**; sub-butir ≥ C3: 39 dari 44 baris tabel butir (89%); skor ≥ C3: **95%**.
- Rentang Bloom kedua Sub-CPMK (C3–C4) terwakili: skor C4 untuk `PS-Sub-CPMK081-1` = 14 dari 60 (23%), untuk `PS-Sub-CPMK102-1` = 8 dari 40 (20%).

### Cara menghitung ketercapaian (agregat)

Untuk setiap mahasiswa: ketercapaian 102-1 (%) = (Σ skor butir bertanda 102-1)/40 × 100; ketercapaian 081-1 (%) = (Σ skor butir bertanda 081-1)/60 × 100. Untuk `mutu/02` dan laporan PPEPP, yang dicatat di repositori hanya **angka agregat per kelas**: rata-rata dan median ketercapaian per Sub-CPMK, persentase mahasiswa di atas ambang, rata-rata skor per butir (tingkat kesukaran), dan daya beda per butir. Ambang ketercapaian belum ditetapkan (menunggu `T1-17` dan dokumen `F-03`). Skor per mahasiswa tidak dicatat di repositori.

Registri mengalokasikan seluruh UTS (25% nilai akhir) ke `PS-Sub-CPMK102-1`, sedangkan menurut isi butir 60% skor mengukur `PS-Sub-CPMK081-1`. Dengan penandaan per butir, nilai akhir tetap memakai bobot registri, tetapi UTS menyumbang bukti ketercapaian untuk **kedua** Sub-CPMK; usulan revisi alokasi dicatat untuk tim kurikulum (`T2-08`).

---

## Matriks Sub-CPMK × Minggu × Bagian (skor)

| Minggu | Sub-CPMK | A | B | C | D | Total |
|---|---|---|---|---|---|---|
| 1 | 102-1 | 3 | 2 | – | 3 | 8 |
| 2 | 102-1 | 9 | 2 | 6 | 3 | 20 |
| 3 | 102-1 | 8 | – | 4 | – | 12 |
| 4 | 081-1 | – | 10 | 10 | – | 20 |
| 5 | 081-1 | – | – | 15 | 3 | 18 |
| 6 | 081-1 | – | 4 | 5 | 3 | 12 |
| 7 | 081-1 | – | 7 | – | 3 | 10 |
| **Total** | | **20** | **25** | **40** | **15** | **100** |

---

## Kemiripan dengan Sumber Terbuka

Sumber yang diperiksa: Latihan Soal Bab 1–7 buku ajar (tingkat Dasar, Menengah, Mahir), contoh di Bab 3 §3.6.1, contoh soal kisi-kisi UTS (§4, §5, §10), modul Minggu 2–6, serta Lab 05–06. Tidak ada butir yang memakai ulang **teks atau angka** sumber tersebut; beberapa butir memakai **konteks** yang mirip. Tabel berikut mencatat sumber terdekat dan pembedanya. Varian wajib menjaga jarak yang sama dari sumber ini **dan** dari latihan ini.

| Butir | Sumber terdekat | Pembeda |
|---|---|---|
| A1 | Bab 1 L2 (klasifikasi 8 variabel); kisi-kisi §10-A (prioritas bug) | Konteks dompet digital; menilai pasangan variabel → ringkasan untuk lima kolom sekaligus |
| A2 | Bab 1 L6 (formulir sukarela), L9 (survei bias 78%) | Sampel kenyamanan menurut lokasi dan jam; angka 74% |
| A3 | Bab 2 L5 (mean 72, median 85 → bentuk) | Arah dibalik: dari deskripsi sebaran ke hubungan mean–median |
| A4 | Bab 2 L9 (klaim SLA p50/p95/p99) | Dua versi dengan mean sama dan p95 berbeda; tanpa klaim SLA |
| A6 | Bab 2 L8 (CV tiga layanan) | Harga pangan di dua pasar; PG |
| A7 | Bab 2 §2.4.1 dan modul Minggu 2 (tabel makna kuartil — materi, bukan latihan) | Menghitung banyaknya hari dari makna kuartil |
| A11 | Bab 3 §3.6.1(c) dan modul Minggu 3 §6.1(c) (materi, bukan latihan: tren tiga bulan naik, setahun turun); Bab 3 L9 (sumbu-y terpotong) | Lima bulan ditampilkan; stem memuat angka pembanding Januari (72 ribu) dan tren Januari–Agustus; angka sendiri; PG dengan pengecoh "sumbu dari nol, angka benar" |
| A12 | Bab 3 L6 (5 vs 30 bin) | Hanya risiko bin terlalu lebar; tanpa aturan Freedman–Diaconis |
| A13 | Bab 3 L3 (jelaskan boxplot) | Membaca boxplot berangka dan menguji pagar pencilan |
| A14 | Bab 3 L2 ("sebutkan lima unsur wajib") | Menjelaskan dampak unsur yang hilang |
| B1 | Bab 1 L2a (NIM), L7 (rata-rata prioritas ordinal) | Kode pos; menghitung ringkasan yang sah |
| B3 | Bab 4 L5 (P(8,3), C(8,3)), L7 (3 penelaah dari 12) | P(9,3) dan C(7,2) digabung dengan aturan perkalian |
| B4 | Bab 4 L2 (tuliskan aksioma) | Menerapkan aksioma pada keluaran model klasifikasi |
| B6 | Bab 6 L5 (Geometrik p = 0,25), L9 (bukti tanpa memori); modul Minggu 6 (*retry* p = 0,3) | p = 0,7; batas k dari CDF; tanpa memori sebagai perhitungan |
| B7, B8 | Bab 7 L3 (N(100,15)), L6 (N(45,8)); kisi-kisi §4.7 (N(52,9), 2,5%) | Parameter dan konteks baru; persentil 3% ekor kiri |
| C1 | Bab 2 L1, L6; Bab 3 L7 (boxplot menyembunyikan bimodalitas); kisi-kisi §4.2 (9 nilai) | Dua gedung; klaim "rata-rata sama = setara"; bimodalitas dari konteks. Format 9 data mentah memang diumumkan kisi-kisi §4.2 |
| C2 | Bab 4 L3–L4 (1.000 sesi), L8 (3 dari 20 tiket); kisi-kisi §4.4 (600 sesi) | Tabel 3 × 2 metode bayar; laju vs porsi; "tepat 2 dari 3" tanpa pengembalian |
| C3 | Bab 5 L6 (99%/99%), L7 (96%/92%); kisi-kisi §4.5 (96%/92%/1,5%), §10-C (94%/91%/0,8%); Lab 05 | Detektor teks-AI 90%/97%/5%; Bayes berantai dan asumsi bebas bersyarat; NPV; *tabayyun* |
| C4 | Bab 5 L4, L5, L8, L9 dan §5.4.3; Bab 4 L1 dan modul Minggu 4 ("sedikitnya 2 dari 3 server"); modul Minggu 6 dan Lab 06 (20 server); Bab 6 L10 | Uji kebebasan dari log; *load balancer* seri dengan replika paralel dan batas keandalan; kuorum ≥ 3 dari 4 dengan BINS; arah dampak pelanggaran kebebasan |
| D | Kisi-kisi §5 (API SIAKAD) | Sistem antrean rumah sakit; sub-butir mengikuti §5 dengan data dan pertanyaan baru |

Konteks yang terlalu dekat dengan Latihan Dasar yang wajib dikerjakan menurut kisi-kisi §9.2 — tiga server seri vs paralel (Bab 5 L5) dan "sedikitnya 2 dari 3 server" (Bab 4 L1) — sudah dihindari; varian tidak boleh kembali ke konteks itu.

---

## Panduan Menyusun Varian (Naskah UTS Sebenarnya)

Naskah UTS sebenarnya adalah **varian** dari latihan ini. Mahasiswa sudah melihat latihan beserta pembahasannya, jadi varian harus menguji keterampilan yang sama dengan tingkat kesulitan yang sama, tetapi tidak dapat dijawab dengan mengingat jawaban latihan. Susun **dua** varian dengan prosedur yang sama: satu untuk UTS dan satu untuk ujian susulan ([kerangka asesmen §8.2](assessment-framework.md#82-susulan): soal susulan berbeda).

### 1. Invarian per butir

Untuk **setiap** butir dan sub-butir berikut ini tetap sama dengan [Tabel Butir](#tabel-butir) dan tabel di bawah: Sub-CPMK, level Bloom, skor, indikator kisi-kisi, taksiran waktu (±0,5 menit), dan tingkat kesulitan (kolom *Kesulitan*). Selain itu tetap sama: peta aspek tiap butir C (prosedur 3,5 · hitung 2,5 · asumsi 2 · interpretasi 2), struktur pedoman skor parsial, aturan pembulatan dan konvensi kuartil di Petunjuk Umum, **batas kalimat** pada sepuluh perintah uraian (kolom *Langkah dan format*), serta keseimbangan PG (sebaran huruf kunci 3–4 per huruf; kunci bukan opsi terpanjang di lebih dari 2–3 butir).

**Tingkat kesulitan** (taksiran penyusun) ditetapkan per satuan jawaban — butir A; butir B menurut sub-butirnya yang tersulit; sub-butir C dan D — dengan aturan berurutan: aturan pertama yang cocok yang berlaku, sehingga setiap satuan jawaban hanya mendapat satu label.

1. **Sulit** — jalur jawaban memuat **dua atau lebih** jebakan khas atau keputusan konsep (mis. permutasi vs kombinasi **dan** dikalikan vs dijumlahkan; ekor kiri **dan** pencarian terbalik di tabel), atau analisis yang memadukan beberapa hasil sebelumnya menjadi keputusan atau kesimpulan.
2. **Sedang** — tidak memenuhi aturan 1, dan memenuhi salah satu: (i) memerlukan hitungan, atau jawaban yang disusun sendiri (bukan dipilih) dengan penalaran rutin — berapa pun banyak langkahnya, dengan paling banyak **satu** jebakan khas; (ii) PG tanpa hitungan yang ciri penentu jawabannya **tidak** disebut di stem, sehingga harus disimpulkan dari skenario, dengan **satu** jebakan khas.
3. **Mudah** — PG tanpa hitungan yang ciri penentu jawabannya **disebut langsung** di stem (mis. p95 di A4, ekor panggilan panjang di A3, "nilai sangat besar" di A5, "bin sangat lebar" di A12, unsur yang hilang di A14, "mengurutkan" proporsi berdekatan di A15), sehingga satu langkah pengenalan cukup; taksiran waktu ≤ 1 menit.

**Jebakan khas** adalah isyarat di stem atau tugas yang sengaja memancing satu miskonsepsi yang dikenal, mis. n besar dianggap menjamin keterwakilan (A2); s lebih kecil tetapi CV lebih besar (A6); selisih nilai vs banyaknya data (A7); opsi yang hanya menjawab sebagian pertanyaan majemuk (A10); grafik yang lolos satu cek kejujuran tetapi tetap menyesatkan (A11); simetri tabel Normal; penyebut N vs n − 1; satuan menit → jam. Pengecoh biasa yang ada pada setiap PG bukan jebakan khas. Butir Sedang menurut (ii) mencantumkan jebakannya di kolom *Kesulitan*.

Sebaran skor menurut kesulitan: mudah 6,5 · sedang 50,5 · sulit 43 (A 6,5/12/1,5; B 0/10/15; C 0/19,5/20,5; D 0/9/6). Varian mempertahankan label setiap satuan jawaban. Label ini taksiran; bila tersedia, kalibrasikan dengan proporsi jawaban benar per butir (angka agregat) dari latihan dan UTS.

| Butir | Sub-CPMK · Bloom · skor | Konsep/keterampilan yang diuji | Langkah dan format | Kesulitan |
|---|---|---|---|---|
| A1 | 102-1 · C3 · 1,5 | Operasi/ringkasan yang sah per skala; tipe data ≠ skala | PG 4 opsi, tiap opsi tiga pasangan "variabel → ringkasan/pernyataan"; dataset lima kolom mencakup nominal (satu bertipe bilangan), ordinal, interval, rasio; tepat satu opsi seluruhnya sah; tiap pengecoh memuat satu pelanggaran khas | Sulit |
| A2 | 102-1 · C3 · 1,5 | Bias sampel; n besar tidak memperbaiki bias | PG; stem memuat n besar dan persentase hasil; jenis sampel tidak disebut; pengecoh: mitos n besar, "sensus", ganti ukuran ringkasan | Sedang (ii) — jebakan: n besar dianggap representatif |
| A3 | 102-1 · C2 · 1 | Arah kemencengan ↔ mean–median | PG tanpa hitungan; deskripsi verbal sebaran dengan ekor jelas | Mudah |
| A4 | 102-1 · C2 · 1 | Persentil ekor vs rata-rata untuk kinerja sistem | PG; dua sistem dengan pemusatan sama, ekor berbeda | Mudah |
| A5 | 102-1 · C2 · 1 | Ketahanan ukuran terhadap nilai ekstrem | PG; empat pasangan ukuran, tepat satu pasangan *robust* | Mudah |
| A6 | 102-1 · C3 · 1,5 | Koefisien variasi dua kelompok | PG; stem memuat isyarat perbandingan relatif ("dengan memperhitungkan perbedaan tingkat harga"); opsi tanpa angka CV; jebakan: s lebih kecil tetapi CV lebih besar | Sedang |
| A7 | 102-1 · C3 · 1,5 | Makna kuartil (proporsi data antarposisi) | PG; satu perkalian; pengecoh: selisih nilai, IQR, 50% data | Sedang |
| A8 | 102-1 · C3 · 1,5 | Median dan modus dari tabel frekuensi | PG; n genap, dua data tengah di kategori berbeda; mean sebagai pengecoh | Sedang |
| A9 | 102-1 · C3 · 1,5 | Rata-rata gabungan berbobot | PG; n kelompok berbeda; pengecoh rata-rata tanpa bobot | Sedang |
| A10 | 102-1 · C3 · 1,5 | Memilih grafik menurut jenis data dan pertanyaan | PG; pertanyaan majemuk (hubungan dua variabel kuantitatif **dan** beda kelompok); empat grafik wajar, hanya satu menjawab kedua bagian | Sedang (ii) — jebakan: opsi yang hanya menjawab sebagian pertanyaan |
| A11 | 102-1 · C3 · 1,5 | Satu dari empat teknik penyajian menyesatkan Bab 3 §3.6.1 dan kesan salahnya | PG; grafik berangka beserta data pembanding di stem; teknik tidak disebut; satu hitungan perbandingan; pengecoh: "jujur" karena lolos satu cek, alasan keliru tentang jenis grafik, cek kelengkapan yang tidak memperbaiki | Sedang — jebakan: grafik lolos satu cek kejujuran (sumbu dari nol, angka benar) |
| A12 | 102-1 · C2 · 1 | Dampak lebar bin histogram | PG tanpa hitungan | Mudah |
| A13 | 102-1 · C3 · 1,5 | Membaca boxplot berangka; pagar 1,5×IQR | PG; sketsa ASCII lima angka + satu titik terpisah; satu hitungan pagar; pengecoh: median dibaca mean, kumis dibaca kuartil, arah kemencengan | Sedang |
| A14 | 102-1 · C2 · 1 | Dampak unsur wajib grafik yang hilang | PG tanpa hitungan | Mudah |
| A15 | 102-1 · C3 · 1,5 | Grafik untuk membandingkan proporsi berdekatan | PG; 5–8 kategori dengan persentase berdekatan | Mudah |
| B1 | 102-1 · C3 · 2 | Tipe data ≠ skala; ringkasan sah untuk nominal | (a) 1 + (b) 1; lima data; satu "rata-rata" keliru dikutip | Sedang |
| B2 | 102-1 · C3 · 2 | Varians dan simpangan baku populasi; alasan penyebut | Lima data bulat, mean dan Σ(x − μ)² bulat; empat langkah | Sedang |
| B3 | 081-1 · C3 · 3 | Permutasi vs kombinasi + aturan perkalian | Satu bagian berurutan, satu tidak; tiga langkah | Sulit |
| B4 | 081-1 · C3 · 3 | Aksioma Kolmogorov; komplemen; penjumlahan saling lepas | (a) 1 + (b) 1 + (c) 1; empat kategori saling lepas dan lengkap, jumlah ≠ 1 | Sedang |
| B5 | 081-1 · C3 · 4 | Perkalian berantai; bersyarat pada komplemen | (a) 2 + (b) 2; tiga tahap berurutan; kejadian di (b) adalah bagian dari komplemen | Sulit |
| B6 | 081-1 · C3 · 4 | Geometrik: E[X], batas k dari CDF, tanpa memori | (a) 1 + (b) 1,5 + (c) 1,5; k dapat dicari dengan coba-coba dalam ≤ 6 langkah | Sulit |
| B7 | 081-1 · C3 · 3 | Tabel Normal: P(X < a), P(a < X < b) | (a) 1,5 + (b) 1,5; z dua desimal yang ada di tabel; satu batas di bawah μ (perlu simetri) | Sedang |
| B8 | 081-1 · C3 · 4 | x dari persentil; aturan empiris | (a) 2,5 + (b) 1,5; persentil di ekor (perlu z negatif atau simetri); (b) tanpa tabel | Sulit |
| C1 | 102-1 · C3–C4 · 10 | Deskriptif lengkap dan pencilan; memilih ukuran; boxplot; keterbatasan boxplot | (a) 4 C3, (b) 2 C4, (c) 2 C3, (d) 2 C4; (b) dan (d) paling banyak 3 kalimat; kelompok A sembilan data mentah dengan satu pencilan atas dan Σ(x − x̄)² tercetak; kelompok B ringkasan + boxplot tercetak, mean sama dengan A, bimodal tersembunyi | (a) Sedang · (b) Sulit · (c) Sedang · (d) Sulit |
| C2 | 081-1 · C3–C4 · 10 | Bersyarat dua arah; penjumlahan umum; kombinasi tanpa pengembalian; laju vs porsi | (a) 3,5 C3, (b) 4 C3, (c) 2,5 C4; (c) paling banyak 3 kalimat; tabel kontingensi 3 × 2; kategori dengan laju tertinggi bukan penyumbang mayoritas | (a) Sedang · (b) Sulit · (c) Sulit |
| C3 | 081-1 · C3–C4 · 10 | Probabilitas total; Bayes; tabel frekuensi; Bayes berantai; bebas bersyarat; nilai Islam dalam keputusan | (a) 3 C3, (b) 2 C3, (c) 2,5 C3–C4, (d) 2,5 C4; analisis asumsi (c) paling banyak 2 kalimat, (d) paling banyak 4 kalimat; kerangka tabel tercetak; prior rendah sehingga posterior pertama ±50–70% | (a) Sedang · (b) Sedang · (c) Sulit · (d) Sulit |
| C4 | 081-1 · C3–C4 · 10 | Uji kebebasan dan saling lepas; keandalan seri–paralel dan batasnya; Binomial kuorum + BINS; dampak pelanggaran kebebasan | (a) 3 C4, (b) 2 C3, (c) 3 C3, (d) 2 C4; tafsiran (a) paling banyak 2 kalimat, (d) paling banyak 3 kalimat; (c) Binomial dengan dua suku | (a) Sulit · (b) Sedang · (c) Sedang · (d) Sulit |
| D | 102-1: D1, D2, D6 · 081-1: D3, D4, D5 · C4 · 15 | Enam keputusan kisi-kisi §5 dalam satu skenario log sistem | D1 2 C3, D2 3 C4, D3 3 C4, D4 3 C3, D5 3 C3, D6 1 C4; tabel variabel, ringkasan menceng kanan dengan p95 > pagar, tabel galat per jam (seluruh/jam sibuk/lainnya) dengan rasio varians/mean gabungan di dalam atau tepat di batas atas 0,8–1,25 dan rasio varians/mean per periode (jam sibuk dan jam lain, dari angka tabel yang dibulatkan) masing-masing di dalam 0,8–1,25, dua sumber galat; D2 paling banyak 3 dan D3 paling banyak 4 kalimat di luar hitungan, D6 paling banyak 2 kalimat | D1 Sedang · D2 Sulit · D3 Sulit · D4 Sedang · D5 Sedang · D6 Sedang |

### 2. Yang wajib diubah per butir

Pada setiap butir: **konteks/kasus**, **data dan angka**, **urutan dan isi pilihan ganda** (letak kunci diacak ulang), dan **nama entitas** (lembaga, sistem, kolom, kota). Karena panduan ini publik, contoh di kolom kanan hanya menggambarkan **jenis** perubahan — naskah sebenarnya memakai konteks dan angka pilihan dosen sendiri, bukan contoh ini secara harfiah.

| Butir | Arah variasi (contoh ilustratif) |
|---|---|
| A1 | Dataset lain dari sistem informasi (mis. data pasien klinik kampus: nomor rekam medis acak, golongan darah, tingkat nyeri ringan < sedang < berat, suhu tubuh °C sebagai interval, berat badan kg); pelanggaran dalam pengecoh dipindah ke kolom lain |
| A2 | Mekanisme bias lain atau lokasi/jam lain (mis. polling sukarela di grup media sosial angkatan; responden yang sedang antre di loket pada jam sibuk); n dan persentase baru |
| A3 | Konteks lain; arah boleh dibalik menjadi menceng kiri (mis. nilai kuis yang mudah: sebagian besar 80–95, beberapa sangat rendah → mean < median) |
| A4 | Dua layanan/versi lain dengan pemusatan sama dan p99 (atau p95) berbeda (mis. API pembayaran dua penyedia) |
| A5 | Nilai ekstrem lain, boleh sangat kecil (mis. satu catatan 0 detik akibat galat pencatatan); urutan pasangan ukuran diacak |
| A6 | Konteks lain (mis. waktu tempuh dua rute bus); angka bulat; selisih CV ≥ 1 poin persen; jebakan s lebih kecil–CV lebih besar dipertahankan; stem **wajib** memuat isyarat perbandingan relatif yang sama (mis. "dengan memperhitungkan perbedaan rata-rata kedua kelompok") agar opsi simpangan baku mentah tidak dapat dibela |
| A7 | Posisi lain (di bawah Q1, antara Q1 dan median, atau di atas Q3) dan banyak data lain yang habis dibagi 4 |
| A8 | Variabel diskret lain (mis. banyak mata kuliah yang diulang); n genap dan tabel frekuensi baru dengan mean tidak bulat |
| A9 | Konteks lain (mis. durasi panggilan dua *shift*) dengan n tidak sama; boleh tiga kelompok |
| A10 | Pertanyaan analisis lain dengan grafik jawaban lain (mis. sebaran waktu respons empat server → boxplot berdampingan; tren bulanan dua layanan → diagram garis) |
| A11 | Hanya teknik dari [Bab 3 §3.6.1](../06-buku-ajar/bab-03-visualisasi-data-statistik.md#361-empat-teknik-menyesatkan-yang-paling-umum): sumbu tidak dari nol pada diagram batang atau skala ganda, atau pemotongan rentang dengan konteks dan angka baru (pie beririsan banyak sudah dipakai A15); stem tetap memuat angka yang membuat kesan salah dapat dihitung; hindari angka contoh §3.6.1(a) (98 vs 100) dan Bab 3 L9 (10.200 → 10.450) |
| A12 | Kasus kebalikan: bin terlalu sempit sehingga derau tampak seperti pola |
| A13 | Boxplot baru; pernyataan benar boleh tentang pagar bawah, arah kemencengan, atau proporsi data di atas Q3; titik terpisah boleh di bawah |
| A14 | Unsur lain yang hilang (mis. label sumbu-x dan sumber, atau keterangan skala logaritmik) pada grafik berkonteks lain |
| A15 | Banyak kategori dan rentang lain (mis. enam metode pembayaran 13–20%) |
| B1 | Kolom lain bertipe bilangan padahal nominal (mis. kode produk, kode wilayah); data baru dengan satu modus jelas; "rata-rata" keliru dihitung dari data baru |
| B2 | Populasi kecil lain yang diukur seluruhnya (mis. lama pengisian daya kelima mobil listrik operasional kampus); tetap populasi (s sampel diuji di C1(a)) |
| B3 | Konteks lain dengan satu bagian berurutan dan satu tidak (mis. urutan pembicara seminar, lalu panitia cadangan); n dan r baru; hindari P(8,3)/C(8,3) Bab 4 L5 |
| B4 | Keluaran model lain (mis. prakiraan cuaca empat kategori); jumlah boleh kurang dari 1; kategori yang keliru dan pasangan gabungan berbeda |
| B5 | Proses bertahap lain (mis. rekrutmen asisten laboratorium); peluang baru; (b) tetap tentang gugur di tahap pertama |
| B6 | Proses ulang-sampai-berhasil lain (mis. pengiriman kode OTP); p baru (0,6–0,8) dan ambang baru (0,95 atau 0,999); pilih **pasangan** p dan ambang sehingga k antara 3 dan 6 (mis. p = 0,6 & 0,95 → k = 4; p = 0,65 & 0,95 → k = 3; p = 0,75 atau 0,8 & 0,999 → k = 5); hindari p = 0,6 & 0,999 (k = 8), p = 0,65 & 0,999 (k = 7), dan p = 0,8 & 0,95 (k = 2); banyak kegagalan awal dan tambahan di (c) baru |
| B7 | Proses mutu lain (mis. volume botol air minum); μ dan σ baru dengan z dua desimal; satu batas di bawah μ, satu di atas |
| B8 | Ekor dan persentil lain (mis. 4% teratas); aturan empiris dengan ±1σ atau ±3σ; hindari N(100, 15), N(45, 8), N(52, 9) dan 2,5% dari sumber |
| C1 | Dua unit lain (mis. lama pengiriman dua gudang); data A baru; ringkasan B baru dari himpunan bilangan bulat bimodal (periksa keunikannya dengan pencarian menyeluruh); boxplot B digambar ulang |
| C2 | Konteks lain (mis. tiket bantuan per kanal × selesai/eskalasi); total 1.000–1.500; (b) "tepat 1" atau "tepat 2" dari tiga sampel |
| C3 | Penyaring lain yang berdampak pada orang (mis. deteksi kecurangan ujian daring, deteksi kemiripan kode program); prior 2–8%, sensitivitas/spesifisitas baru, N tabel yang membuat sel bulat; pemeriksa kedua baru; hindari 99%/99%, 96%/92%/1,5%, 94%/91%/0,8%, dan 90%/97%/5% |
| C4 | Komponen lain (mis. dua jalur internet kampus; *gateway* pembayaran + server aplikasi); log baru; kuorum lain dengan dua suku Binomial (mis. ≥ 4 dari 5 node); hindari "≥ 2 dari 3" (Bab 4 L1) dan "≥ 3 dari 4" (latihan) |
| D | Sistem lain (mis. KRS daring pada masa pengisian, layanan pengaduan kota); variabel rasio, ordinal, interval baru; ringkasan menceng baru dengan p95 > pagar; data galat per jam dibangkitkan ulang dengan Poisson (laju jam sibuk 2–2,5 × jam lain; *seed* baru) dengan rasio varians/mean gabungan **seperti latihan** — di dalam atau tepat di batas atas rentang heuristik 0,8–1,25 (±1,10–1,25) — sehingga rasio gabungan saja tidak menentukan dan perbedaan mean antarperiode tetap menjadi bukti penentu, **dan** rasio varians/mean per periode (jam sibuk dan jam lain, dari angka tabel yang dibulatkan) masing-masing di dalam 0,8–1,25, sehingga Poisson per periode tetap layak; dengan laju jam sibuk 2–2,5 × laju jam lain 1,2–1,8 per jam, ±10–25% *seed* memenuhi semua syarat (paling sedikit ±10% pada 2,5 × laju 1,8 per jam); dengan begitu pedoman skor dan kesalahan umum D3 berlaku tanpa perubahan; laju dan selang baru yang memerlukan konversi satuan (menit ↔ jam); dua sumber galat dengan kode dan proporsi baru; satu sumber data sukarela untuk D6 |

### 3. Larangan

1. Menyalin kalimat, data, atau angka latihan ini — termasuk pengecoh PG, atau kalimat soal yang hanya diganti angkanya.
2. Mengubah level Bloom, skor, atau Sub-CPMK butir dan sub-butir, atau peta aspek butir C.
3. Menambah materi di luar kisi-kisi (Minggu 1–7, indikator §4–§5), atau menuntut rumus di luar daftar §7 yang tidak dapat diturunkan dari rumus di daftar.
4. Memakai teks atau angka Latihan Soal Bab 1–7, contoh soal kisi-kisi, atau contoh ilustratif tabel di atas secara harfiah.
5. Butir yang memerlukan tabel-t atau nilai z di luar tabel yang dibagikan.
6. Menyimpan varian, kuncinya, atau skrip verifikasinya di repositori publik.

### 4. Prosedur mutu varian

1. **Selesaikan ulang setiap butir dengan Python** (pola blok kode di [pembahasan §5](latihan-uts-pembahasan.md#5-memeriksa-angka-dengan-python)) dan cocokkan dengan kunci varian. Periksa dengan `assert`: setiap angka kunci, rasio varians/mean tabel galat D dari angka tabel yang dibulatkan (gabungan ±1,10–1,25; jam sibuk dan jam lain masing-masing 0,8–1,25), k butir B6 antara 3 dan 6, skor per bagian 20/25/40/15, sebaran per minggu 8/20/12/20/18/12/10, Sub-CPMK 40/60, dan Bloom C2/C3/C4 = 5/73/22.
2. **Pilihan ganda:** penelaah menjawab tanpa kunci untuk memastikan **tepat satu** jawaban benar per butir; letak kunci diacak ulang (sebaran huruf seimbang dan berbeda dari urutan kunci latihan); panjang opsi diperiksa agar kunci tidak menonjol.
3. **Cek waktu — uji coba berwaktu** (KENDALI `T0-15`). Penguji coba: 2–3 asisten atau mahasiswa senior yang belum melihat pembahasan maupun varian — untuk uji coba latihan ini, juga **belum membaca atau mengerjakan latihan ini** (latihan publik sejak 8 Oktober 2026) — dalam kondisi ujian (100 menit, *closed book*, kalkulator ilmiah dan tabel saja, tanpa AI); catat waktu per bagian. Uji coba dilakukan pada latihan ini sebelum varian ditetapkan, dan pada varian bila tersedia penguji coba yang belum melihatnya. Keputusan menurut **median** waktu penguji coba: **≤ 67 menit** (≤ 2/3 durasi) → lolos; **> 67 dan ≤ 75 menit** (≤ 3/4 durasi) → bersyarat: terapkan [cadangan pemangkasan pertama](#cadangan-pemangkasan-waktu); **> 75 menit** → dosen menetapkan [pemangkasan lanjutan](#cadangan-pemangkasan-waktu), lalu uji ulang. Dasar ambang: penguji coba yang menguasai materi bekerja ±1,5× lebih cepat daripada rerata mahasiswa, sehingga 2/3 durasi bagi penguji coba setara dengan seluruh durasi bagi rerata mahasiswa. Data kalibrasi tambahan (bila dosen memintanya): catatan waktu per bagian dari mahasiswa yang mengerjakan latihan ini, diserahkan tanpa nama; yang dipakai dan dicatat hanya rekap agregat (median dan sebaran waktu per bagian).
4. **Telaah sejawat** memakai [checklist-verifikasi §C](../../../00-pedoman-obe/checklist-verifikasi.md#c-lembar-telaah-sejawat) (KENDALI `T0-15`).
5. **Simpan** varian, kunci, dan skrip verifikasinya di penyimpanan privat, tidak di repositori. Untuk `mutu/02`, catat hanya angka agregat.

---

## Catatan untuk Dosen

1. **Penandaan.** Lembar latihan mencantumkan skor dan level Bloom; Sub-CPMK per butir ada di pembahasan dan cetak biru. Varian mengikuti pola yang sama.
2. **Kisi-kisi §3 vs §5 (Bagian D).** Kolom "Bagian" §3 untuk Minggu 1, 2, dan 6 belum memuat D, padahal kerangka §5 memakainya (`T0-18`).
3. **Waktu saran.** Kisi-kisi §2 membagi seluruh 100 menit (20/25/40/15), sedangkan modul Minggu 8 menganjurkan 5 menit membaca dan 10 menit memeriksa. Latihan menyalin kisi-kisi dan menegaskan bahwa waktu membaca dan memeriksa diambil dari 100 menit itu, bukan ditambahkan (`T0-18`).
4. **Rumus ekor.** Geometrik P(X > k) dan Eksponensial P(T > t) tidak ada di daftar rumus kisi-kisi §7; pembahasan menerima jalur penurunan dari rumus yang ada (`T0-18`).
5. **Ketentuan skor tambahan** (kesalahan berantai, toleransi pembulatan, kelipatan 0,25, jawaban alternatif sahih) berstatus usulan di pembahasan §0.2 sampai ditetapkan (`T0-18`). Demikian pula cakupan aturan kisi-kisi §6 (*Kriteria Penilaian Soal Uraian*): latihan menerapkannya juga pada Bagian B dan D (Petunjuk 6, pembahasan §0.1), sedangkan kisi-kisi tidak menyebut kedua bagian itu.
6. **Konvensi kuartil** (n − 1)p + 1 dinyatakan di Petunjuk 9 karena buku ajar memakai `numpy.percentile` tanpa aturan manual eksplisit; n = 9 membuat posisi kuartil bulat, dan pembahasan memberi toleransi untuk metode (n + 1)p.
7. **D3.** Rasio varians/mean gabungan 1,25 tepat di batas heuristik 0,8–1,25 buku ajar; pembahasan menjadikan perbedaan mean antarperiode sebagai bukti penentu dan menerima kedua tafsiran rasio. Varian menjaga sifat ini, termasuk rasio per periode di dalam 0,8–1,25 ([Arah variasi D](#2-yang-wajib-diubah-per-butir)); rasio gabungan yang jelas di luar rentang menambah isyarat kedua dan membuat D3 lebih mudah.
8. **C3(d)** merujuk prinsip *tabayyun* (QS Al-Hujurat [49]: 6) secara ringkas tanpa kutipan ayat — konfirmasi ketepatan rujukan saat telaah.
9. **Waktu — putuskan sebelum varian ditetapkan.** Batas kalimat pada sepuluh perintah uraian perlu konfirmasi dosen; ambang uji coba berwaktu ada di [prosedur mutu varian](#4-prosedur-mutu-varian) no. 3. [Cadangan pertama](#cadangan-pemangkasan-waktu) memuat sembilan pemangkasan yang menjaga Sub-CPMK, Bloom, dan skor setiap baris (hemat total ±2,5–4,25 menit kerja mahasiswa) dan perlu disetujui dosen **sebelum** uji coba. Pilihan pemangkasan lanjutan, termasuk opsi pengurangan butir lewat revisi kisi-kisi (`T0-18`), sebaiknya disiapkan sekarang, bukan sesudah uji coba.
10. **Data rekaan.** Seluruh angka rekaan; tidak ada merek atau lembaga nyata. Data galat per jam Bagian D dibangkitkan dengan `numpy.random.default_rng(2035)` (Poisson 3,6 untuk 21 jam sibuk; 1,5 untuk 147 jam lain; total 298 galat).

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
