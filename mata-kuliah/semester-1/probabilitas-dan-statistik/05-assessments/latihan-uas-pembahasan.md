---
id: uai-if52510033-latihan-uas-pembahasan
tipe: asesmen
judul: "Latihan UAS — Probabilitas dan Statistik — Pembahasan dan Pedoman Skor"
kode_mk: IF52510033
nama_mk: Probabilitas dan Statistik
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-09
---

# Pembahasan dan Pedoman Skor — Latihan UAS Probabilitas dan Statistik

## Probabilitas dan Statistik — IF52510033

> **Latihan UAS — bukan naskah UAS.** Pembahasan ini menyertai simulasi lengkap UAS Probabilitas dan Statistik Ganjil 2026/2027 untuk berlatih: komposisi, durasi (120 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UAS. Naskah UAS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> **Kerjakan dulu [latihan UAS](latihan-uas.md) dalam 120 menit tanpa AI dan tanpa membuka berkas ini.** Sesudahnya, cocokkan jawaban per butir, beri skor sendiri dengan pedoman skor parsial, lalu pelajari bagian *Kesalahan umum* dan rujukan *Pelajari ulang*. Menghafal jawaban di sini tidak membantu: naskah UAS memakai konteks dan angka lain, jadi yang perlu dikuasai adalah **langkah dan alasannya**. Judul setiap butir mencantumkan Sub-CPMK registri · level Bloom · skor; cetak biru lengkap ada di [latihan-uas-cetak-biru.md](latihan-uas-cetak-biru.md). Sub-CPMK per butir ditandai menurut isi (bawaan sementara D-03(a)) untuk menghitung ketercapaian; bobot nilai akhir UAS tetap mengikuti alokasi registri dan RPS (`PS-Sub-CPMK081-1`) — lihat [cetak biru, Identitas dan Dasar Penyusunan](latihan-uas-cetak-biru.md#identitas-dan-dasar-penyusunan).
>
> Mata kuliah IF52510033 · Semester Ganjil 2026/2027 · Penyusun: Tri Aji Nugroho, S.T., M.T.

---

## 0. Ketentuan Umum Penskoran

### 0.1 Aturan dari kisi-kisi UAS §6 (soal uraian); dalam latihan ini juga diterapkan pada Bagian B dan D (Petunjuk 6)

Sumber: [kisi-kisi UAS §6](kisi-kisi-uas.md#6-kriteria-penilaian-soal-uraian), yang berjudul *Kriteria Penilaian Soal Uraian*. Kisi-kisi tidak menyebut Bagian B (isian/hitungan pendek) dan D; penerapan aturan ini pada kedua bagian itu adalah tafsiran latihan ini (Petunjuk 6), sama seperti di Latihan UTS, dan termasuk hal yang menunggu penetapan dosen.

| Situasi | Perlakuan |
|---|---|
| Hanya angka akhir, tanpa langkah | Paling banyak **40%** skor butir |
| Langkah benar, salah hitung kecil | Paling sedikit **75%** skor butir |
| Uji yang dipilih kurang optimal, tetapi alasannya ditulis dan masuk akal | Kehilangan paling banyak **30%** skor butir |
| Uji dipilih tanpa alasan sama sekali | Kehilangan seluruh porsi aspek **rumus** |
| Asumsi tidak disebutkan padahal diminta | Kehilangan seluruh porsi aspek **asumsi** |
| Menyatakan "H₀ terbukti benar" | −50% dari porsi aspek **interpretasi** |
| Menyatakan sebab-akibat dari data korelasional | −50% dari porsi aspek **interpretasi** |

Cara menerapkan tiga aturan terakhir (usulan, §0.2):

- **Asumsi yang diminta** dinilai per baris pedoman skor yang bertanda *(diminta)*: bila asumsi pada baris itu tidak disebutkan, porsi asumsi baris itu hilang seluruhnya; baris asumsi lain pada butir yang sama tetap dinilai.
- **Pengurangan −50% interpretasi** berlaku sebagai **batas atas**: skor aspek interpretasi butir yang bersangkutan (butir C utuh, atau sub-butir D) paling banyak 50% porsinya, dibulatkan ke bawah ke kelipatan 0,25 (mis. C5: paling banyak 1 dari 2; D5: paling banyak 0,75 dari 1,5), dan dikenakan sekali per butir. Dengan cara ini kalimat yang sama tidak dihukum dua kali: bila baris tafsir yang memuat kalimat itu sudah bernilai 0 sehingga skor interpretasi butir sudah ≤ 50% porsinya, tidak ada pengurangan tambahan.

Bobot aspek kisi-kisi untuk soal uraian — ketepatan rumus **30%**, ketepatan hitung **25%**, kecocokan asumsi **25%**, kualitas interpretasi **20%** — dipenuhi tepat pada total **Bagian C**: 12 / 10 / 10 / 8 dari 40 poin. Per butir, porsinya mengikuti sifat butir dengan selisih paling besar **5 poin persen** dari bobot kisi-kisi (C2: interpretasi 15,6%; C5: interpretasi 25%):

| Butir | Rumus | Hitung | Asumsi | Interpretasi | Jumlah |
|---|---|---|---|---|---|
| C1 | 2,25 | 2 | 2 | 1,75 | 8 |
| C2 | 2,5 | 2,25 | 2 | 1,25 | 8 |
| C3 | 2,5 | 2 | 2 | 1,5 | 8 |
| C4 | 2,5 | 2 | 2 | 1,5 | 8 |
| C5 | 2,25 | 1,75 | 2 | 2 | 8 |
| **Bagian C** | **12 (30%)** | **10 (25%)** | **10 (25%)** | **8 (20%)** | **40** |

Pada Bagian D, kolom *Aspek* di pedoman skor menunjukkan aspek tiap langkah (R = rumus, H = hitung, A = asumsi, I = interpretasi), sehingga aturan di atas dapat diterapkan.

### 0.2 Ketentuan tambahan — usulan, menunggu penetapan dosen

> Ketentuan di bawah **belum** tercantum di kisi-kisi UAS §6. Statusnya **usulan, menunggu penetapan dosen** — sama dengan ketentuan serupa di Latihan UTS ([KENDALI-EKSEKUSI](../../../00-meta/KENDALI-EKSEKUSI.md), butir T0-18). Di sini ketentuan ini dipakai agar Anda dapat menilai latihan sendiri secara konsisten; untuk UAS, yang berlaku adalah ketentuan yang ditetapkan dosen di kisi-kisi.

1. **Kesalahan berantai** (*error carried forward*): bila sebuah langkah memakai angka keliru dari langkah sebelumnya tetapi prosedurnya benar, langkah itu tetap mendapat skor penuh; kesalahan hanya dihukum sekali.
2. **Toleransi pembulatan:** probabilitas dari tabel Normal ±0,0005; hasil akhir lain ±1 pada digit terakhir yang diminta. Selisih karena memakai nilai tabel (mis. z = 2,33) versus nilai eksak tidak dihukum.
3. Skor diberikan dalam kelipatan **0,25**.
4. Jawaban dengan alasan berbeda tetapi sahih secara statistika diterima penuh — pembahasan ini memuat jawaban acuan, bukan satu-satunya jawaban.
5. **Cara menerapkan** aturan "asumsi yang diminta" (per baris) dan pengurangan −50% interpretasi (sebagai batas atas, sekali per butir) di §0.1.

### 0.3 Catatan umum

- **Tabel.** Butir yang memerlukan tabel Normal: B5(b), B7(a), C4(b)–(d); nilai z = 1,96 untuk 95% (B9, B10) juga dapat dibaca dari tabel ini. Tabel-t: B8, D5, D6. Tabel F: A14. Tabel chi-square dibagikan sesuai kisi-kisi, tetapi A15 hanya memeriksa syarat kelayakan sehingga tidak memerlukannya. Nilai t untuk derajat bebas 48 (A12) tidak ada di tabel, jadi dicetak di soal.
- **Nilai antara yang dicetak.** Untuk menghemat waktu, soal mencetak Σ(x − x̄)² pada C4, P(X = 4) pada C3, dan P(ditandai) pada C1(b). Langkah yang memakai nilai itu tetap dinilai seperti tertulis di pedoman skor.
- **Batas kalimat.** Beberapa perintah uraian membatasi panjang jawaban (hitungan dan notasi tidak termasuk) agar waktu cukup. Batas ini panduan waktu, bukan aturan penskoran: yang dinilai tetap unsur pada pedoman skor. Untuk sub-butir yang dibatasi, *jawaban ringkas* menunjukkan jawaban berskor penuh yang muat dalam batas.
- **Rumus yang tidak tertulis di daftar hafalan** ([kisi-kisi UTS §7](kisi-kisi-uts.md#7-daftar-rumus-yang-harus-dihafal) dan [kisi-kisi UAS §8](kisi-kisi-uas.md#8-daftar-rumus-tambahan-di-luar-rumus-uts)) tetapi dapat diturunkan dari rumus yang ada atau dari definisi; jalur penurunannya diterima penuh:
  1. Uniform kontinu (B6): probabilitas = luas persegi panjang di bawah PDF = panjang selang/lebar seluruh selang; rata-rata = titik tengah karena PDF simetris.
  2. Eksponensial P(T > t) = e^(−λt) dan P(T ≤ t) = 1 − e^(−λt) (C3(d)): P(T > t) sama dengan P(N = 0) untuk N ~ Poisson(λt), karena "tidak ada kedatangan selama t" setara dengan "jeda lebih dari t"; P(T ≤ t) adalah komplemennya.
  3. Cohen's d berpasangan d = d̄/s_d (D7): rumus Cohen's d satu sampel di daftar §8 yang diterapkan pada selisih d dengan μ₀ = 0.
  4. Simpangan baku total n peubah bebas σ√n (C4(d)): total = n·x̄, sehingga SD total = n · σ/√n; atau kerjakan lewat x̄ dan galat baku σ/√n.
  5. Hampiran Poisson untuk Binomial λ = np (B4): rumus E[X] = np Binomial di daftar, dipakai sebagai λ.
  6. R² = r² (C5(c)): koefisien determinasi regresi linear sederhana ([Bab 13 §13.1.2](../06-buku-ajar/bab-13-korelasi-regresi-linear.md#1312-korelasi-pearson)).
  7. Margin galat proporsi E = z·√(p(1 − p)/n) (B10(a)): setengah lebar interval kepercayaan proporsi di daftar §8; rumus ukuran sampel proporsi adalah bentuk kebalikannya.

---

## 1. Bagian A — Pilihan Ganda (skor 15)

Setiap butir bernilai 1 untuk jawaban benar dan 0 untuk jawaban salah atau kosong; tidak ada pengurangan untuk jawaban salah.

**Ringkasan kunci**

| A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | A9 | A10 | A11 | A12 | A13 | A14 | A15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| c | b | d | b | a | c | b | d | a | c | d | a | b | c | a |

### A1 — Kunci (c) `[PS-Sub-CPMK081-1 · C2 · 1]`

Laporan menyatakan **di antara akun yang dibobol**, 80% tanpa 2FA: P(tanpa 2FA | dibobol) = 0,80. Kesimpulan pejabat menyatakan **di antara akun tanpa 2FA**, 80% dibobol: P(dibobol | tanpa 2FA). Arah persyaratan tertukar; nilai yang kedua bergantung pada banyaknya akun tanpa 2FA dan bisa jauh lebih kecil. **Pengecoh:** (a) angka sama tidak berarti kejadian bersyaratnya sama; (b) komplemen dari P(tanpa 2FA | dibobol) adalah P(ber-2FA | dibobol) = 20%, bukan P(dibobol | tanpa 2FA); (d) proporsi akun tanpa 2FA tidak membuat kedua arah persyaratan sama.

*Pelajari ulang:* [Bab 4 §4.4.2](../06-buku-ajar/bab-04-dasar-probabilitas.md#442-kesalahan-paling-umum-dalam-probabilitas-terapan)

### A2 — Kunci (b) `[PS-Sub-CPMK081-1 · C3 · 1]`

Aturan perkalian tanpa pengembalian: P = (3/8) × (2/7) = 6/56 = **0,1071**. **Pengecoh:** (a) (3/8)² mengandaikan pengembalian; (c) (3/8)(2/8) mengurangi pembilang tetapi lupa mengurangi penyebut; (d) 3/8 hanya peluang pengambilan pertama.

*Pelajari ulang:* [Bab 4 §4.4.3](../06-buku-ajar/bab-04-dasar-probabilitas.md#443-aturan-perkalian)

### A3 — Kunci (d) `[PS-Sub-CPMK081-1 · C2 · 1]`

Satu tiket hanya punya satu prioritas → T dan R **saling lepas**: P(T ∩ R) = 0, sehingga P(T ∪ R) = 0,3 + 0,5 = 0,8. Karena P(T)·P(R) = 0,15 ≠ 0 = P(T ∩ R), keduanya **tidak saling bebas** — mengetahui tiket itu Tinggi membuat P(R) menjadi 0. **Pengecoh:** (a) mencampur dua tiket berbeda dengan dua kejadian pada tiket yang sama; (b) saling lepas dengan peluang tak nol tidak mungkin sekaligus bebas; (c) irisannya 0, bukan 0,15.

*Pelajari ulang:* [Bab 5 §5.4.2](../06-buku-ajar/bab-05-probabilitas-bersyarat-bayes.md#542-bebas--saling-lepas)

### A4 — Kunci (b) `[PS-Sub-CPMK081-1 · C2 · 1]`

Pada prevalensi 0,5%, sebagian besar akun yang ditandai adalah akun manusia yang salah ditandai — 5% dari 99,5% akun manusia (1 − spesifisitas) jauh lebih banyak daripada 95% dari 0,5% akun bot. Menaikkan spesifisitas memangkas alarm palsu itu: PPV naik dari ±8,7% menjadi ±48,8%, sedangkan menaikkan sensitivitas hanya menjadi ±9,1% (perhitungan di §5). **Pengecoh:** (a) menambah positif benar yang jumlahnya memang sedikit; (c) menurunkan ambang menambah alarm palsu, jadi PPV turun; (d) tanpa perubahan sensitivitas dan spesifisitas, PPV tidak berubah.

*Pelajari ulang:* [Bab 5 §5.3.3](../06-buku-ajar/bab-05-probabilitas-bersyarat-bayes.md#533-sensitivitas-atau-spesifisitas)

### A5 — Kunci (a) `[PS-Sub-CPMK081-1 · C3 · 1]`

Syarat BINS: **B**iner ✓, **N** tetap = 20 ✓, **S**ama — mungkin, tetapi **I**ndependen ✗: kegagalan satu *build* menaikkan peluang *build* berikutnya gagal (*cache* bersama). Binomial akan meremehkan peluang banyak *build* gagal sekaligus. **Pengecoh:** (b) memeriksa dua syarat saja; (c) Poisson juga mensyaratkan kejadian saling bebas — syarat yang sama yang dilanggar di sini — dan untuk n = 20 dengan p yang tidak kecil, Poisson bukan hampiran Binomial yang layak; (d) Geometrik menghitung percobaan sampai kejadian pertama, bukan banyaknya kegagalan dari 20.

*Pelajari ulang:* [Bab 6 §6.3.1](../06-buku-ajar/bab-06-peubah-acak-distribusi-diskret.md#631-syarat-bins)

### A6 — Kunci (c) `[PS-Sub-CPMK081-1 · C3 · 1]`

X ~ Binomial(150; 0,04): E[X] = np = **6**; Var(X) = np(1 − p) = 5,76 → SD = **2,40**. **Pengecoh:** (a) 5,76 adalah varians; (b) rata-rata dan SD satu formulir (Bernoulli); (d) √6 = 2,45 memakai Var = mean seperti Poisson.

*Pelajari ulang:* [Bab 6 §6.6](../06-buku-ajar/bab-06-peubah-acak-distribusi-diskret.md#66-memilih-distribusi-yang-tepat)

### A7 — Kunci (b) `[PS-Sub-CPMK081-1 · C2 · 1]`

Pada peubah kontinu, peluang satu titik tepat sama dengan nol, sehingga tanda "≤" dan "<" tidak mengubah peluang. **Pengecoh:** (a) f(3) adalah kerapatan, bukan peluang — peluang adalah luas di bawah kurva; (c) PDF boleh lebih dari 1, yang harus 1 adalah luas totalnya; (d) nilai yang paling sering pun tetap berpeluang nol sebagai satu titik tepat.

*Pelajari ulang:* [Bab 7 §7.1.1](../06-buku-ajar/bab-07-distribusi-kontinu-normal.md#711-mengapa-px--x--0)

### A8 — Kunci (d) `[PS-Sub-CPMK081-1 · C2 · 1]`

Q-Q plot yang melengkung ke atas di ujung kanan dan kemencengan positif besar (2,4 ≫ 0,5) menandakan **menceng kanan**. Model Normal untuk satu berkas akan meremehkan ekor kanan (berkas yang sangat besar). **Pengecoh:** (a) n besar tidak membuat data individual menjadi Normal — Teorema Limit Pusat berbicara tentang rata-rata sampel; (b) arah kemencengan terbalik; (c) kemencengan jauh dari 0 berarti tidak simetris.

*Pelajari ulang:* [Bab 7 §7.5.2](../06-buku-ajar/bab-07-distribusi-kontinu-normal.md#752-cara-membaca-q-q-plot) · [Bab 7 §7.5.1](../06-buku-ajar/bab-07-distribusi-kontinu-normal.md#751-tiga-pendekatan)

### A9 — Kunci (a) `[PS-Sub-CPMK081-1 · C3 · 1]`

SE = s/√n = 2,4/√64 = 2,4/8 = **0,30 detik**. Galat baku mengukur sebaran x̄ dari sampel ke sampel, sedangkan s = 2,4 detik mengukur sebaran waktu muat individual. **Pengecoh:** (b) menyamakan galat baku dengan simpangan baku; (c) membagi dengan n, bukan √n, dan mengira sebaran data menyempit; (d) ±2 SE menggambarkan ketidakpastian rata-rata, bukan rentang 95% data individual (rentang data jauh lebih lebar).

*Pelajari ulang:* [Bab 8 §8.3.2](../06-buku-ajar/bab-08-ekspektasi-varians-sampling.md#832-sifat-distribusi-sampling-rata-rata)

### A10 — Kunci (c) `[PS-Sub-CPMK081-1 · C2 · 1]`

Tabel "berapa n yang cukup besar" di Bab 8: populasi sangat menceng atau banyak pencilan memerlukan n ≥ 50, kadang jauh lebih. Dengan n = 20, pendekatan Normal untuk x̄ belum tentu layak. **Pengecoh:** (a) Teorema Limit Pusat berlaku untuk n yang **cukup besar**, bukan n berapa pun; (b) n ≥ 15 hanya untuk populasi simetris tanpa pencilan; (d) Teorema Limit Pusat justru menyatakan x̄ mendekati Normal walaupun populasinya tidak Normal.

*Pelajari ulang:* [Bab 8 §8.4.3](../06-buku-ajar/bab-08-ekspektasi-varians-sampling.md#843-berapa-n-yang-cukup-besar)

### A11 — Kunci (d) `[PS-Sub-CPMK081-1 · C2 · 1]`

Yang bersifat "95%" adalah **prosedurnya**: dari banyak sampel, ±95% interval yang disusun dengan cara ini memuat μ. μ adalah konstanta; interval yang sudah dihitung memuatnya atau tidak. **Pengecoh:** (a) memperlakukan μ sebagai peubah acak; (b) interval tentang rata-rata, bukan tentang 95% mahasiswa; (c) salah tafsir "cakupan rata-rata sampel baru": IK tidak menyatakan di mana rata-rata sampel berikutnya akan jatuh.

*Pelajari ulang:* [Bab 9 §9.3](../06-buku-ajar/bab-09-estimasi-interval-kepercayaan.md#93-menafsirkan-95-kepercayaan)

### A12 — Kunci (a) `[PS-Sub-CPMK081-1 · C3 · 1]`

Titik tengah 55,0 detik dan margin 95% = 3,0 → SE = 3,0/2,01 = 1,4925. Margin 99% = 2,68 × 1,4925 = 4,0 (atau langsung 3,0 × 2,68/2,01 = 4,0) → IK 99% = **[51,0 ; 59,0] detik**. Tingkat kepercayaan lebih tinggi → interval lebih **lebar**. **Pengecoh:** (b) membagi, bukan mengalikan, dengan rasio 2,68/2,01 sehingga interval menyempit; (c) interval tidak berubah; (d) margin dilipatduakan tanpa dasar.

*Pelajari ulang:* [Bab 9 §9.2.3](../06-buku-ajar/bab-09-estimasi-interval-kepercayaan.md#923-pertukaran-antara-kepastian-dan-presisi)

### A13 — Kunci (b) `[PS-Sub-CPMK081-1 · C2 · 1]`

Dengan penyebut n − 1, E[s²] = σ² — estimator **tak bias**; penyebut n meremehkan σ², paling parah pada n kecil. **Pengecoh:** (a) s² dengan n − 1 justru sedikit lebih besar, dan efisiensi bukan alasannya; (c) penyebut n tetap konsisten karena biasnya menuju nol seiring n membesar; (d) sifat tak bias s² tidak mensyaratkan data Normal.

*Pelajari ulang:* [Bab 9 §9.1.1](../06-buku-ajar/bab-09-estimasi-interval-kepercayaan.md#911-estimator-dan-sifatnya)

### A14 — Kunci (c) `[PS-Sub-CPMK102-1 · C3 · 1]`

df antar = k − 1 = 2; df dalam = N − k = 30. MS_antar = 300/2 = 150; MS_dalam = 1.200/30 = 40; F = 150/40 = **3,75** > F₀,₀₅(2; 30) = 3,32 (tabel F) → tolak H₀. η² = SS_antar/SS_total = 300/1.500 = **0,20**. **Pengecoh:** (a) ANOVA hanya menyatakan **sedikitnya satu** rata-rata berbeda, bukan setiap pasangan — untuk itu diperlukan uji lanjut (Tukey); (b) F dibalik (MS_dalam/MS_antar); (d) η² memakai SS_total, bukan SS_dalam, sebagai penyebut.

*Pelajari ulang:* [Bab 12 §12.2.2](../06-buku-ajar/bab-12-anova-chi-square.md#1222-tabel-anova) · [Bab 12 §12.2.5](../06-buku-ajar/bab-12-anova-chi-square.md#1225-uji-lanjut-tukey-hsd)

### A15 — Kunci (a) `[PS-Sub-CPMK102-1 · C3 · 1]`

E_ij = (total baris × total kolom)/N. Ponsel: 26,4; 13,2; **4,4**. Tablet: 9,6; **4,8**; **1,6**. Tiga dari enam sel (50%) memiliki frekuensi harapan < 5, jauh melampaui batas 20% sel → syarat **tidak terpenuhi** (frekuensi harapan terkecil, 1,6, sendiri masih ≥ 1, jadi yang dilanggar adalah batas 20% itu); gabungkan kategori "ringan" dan "berat" atau pakai uji eksak Fisher. **Pengecoh:** (b) hanya melihat satu sel; (c) N ≥ 30 bukan syarat chi-square; (d) syarat diperiksa pada frekuensi **harapan**, bukan teramati.

*Pelajari ulang:* [Bab 12 §12.3.3](../06-buku-ajar/bab-12-anova-chi-square.md#1233-syarat-kelayakan-dan-alternatifnya)

---

## 2. Bagian B — Isian / Hitungan Pendek (skor 20)

### B1. Token akses heksadesimal `[PS-Sub-CPMK081-1 · C3 · 2]`

**Jawaban.**

- **(a)** Karakter berbeda dan urutan bermakna → **permutasi**: P(16,4) = 16 · 15 · 14 · 13 = **43.680 token**.
- **(b)** Token yang hanya memuat angka: P(10,4) = 10 · 9 · 8 · 7 = 5.040. Karena setiap token sama mungkin, P = 5.040/43.680 = **0,1154**. Cara lain (aturan perkalian berurutan): (10/16)(9/15)(8/14)(7/13) = 0,1154.

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| (a) Permutasi beserta alasannya (diminta): karakter berbeda dan urutan bermakna | 0,5 |
| (a) 43.680 | 0,5 |
| (b) Banyak token angka / banyak seluruh token, atau perkalian berurutan | 0,5 |
| (b) 0,1154 | 0,5 |

**Kesalahan umum.** Memakai 16⁴ = 65.536 (karakter boleh berulang, padahal soal menyebut berbeda) → (a) 0, (b) dinilai berantai bila konsisten (10⁴/16⁴ = 0,1526). Memakai C(16,4) = 1.820 (urutan diabaikan) → (a) 0; perbandingan C(10,4)/C(16,4) = 210/1.820 = 0,1154 memberi angka yang sama, jadi (b) tetap penuh.

*Pelajari ulang:* [Bab 4 §4.5.2](../06-buku-ajar/bab-04-dasar-probabilitas.md#452-permutasi--urutan-diperhatikan)

### B2. Audit repositori `[PS-Sub-CPMK081-1 · C3 · 2]`

**Jawaban.**

- **(a)** Aturan perkalian: P(K ∩ R) = P(R) · P(K | R) = 0,12 × 0,50 = **0,06**. Aturan penjumlahan umum: P(K ∪ R) = 0,18 + 0,12 − 0,06 = **0,24**.
- **(b)** P(R | K) = P(K ∩ R)/P(K) = 0,06/0,18 = **0,3333**. Nilainya berbeda dari P(K | R) = 0,50 karena kelompok acuannya berbeda: 0,06 dibagi seluruh repositori ber-kunci API (18%), bukan seluruh repositori tanpa README (12%).

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| (a) P(K ∩ R) = 0,12 × 0,50 = 0,06 (aturan perkalian) | 0,5 |
| (a) P(K ∪ R) = 0,24 (aturan penjumlahan umum) | 0,5 |
| (b) 0,06/0,18 = 0,3333 | 0,5 |
| (b) Alasan: penyebut atau kelompok acuan berbeda (arah persyaratan) | 0,5 |

**Kesalahan umum.** P(K ∩ R) = 0,18 × 0,12 = 0,0216 (mengandaikan bebas, padahal P(K | R) = 0,50 ≠ P(K) = 0,18) → baris pertama 0; P(K ∪ R) = 0,2784 dinilai berantai. Menjawab (b) 0,50 — menyamakan P(R | K) dengan P(K | R) → (b) 0.

*Pelajari ulang:* [Bab 4 §4.4.3](../06-buku-ajar/bab-04-dasar-probabilitas.md#443-aturan-perkalian) · [Bab 4 §4.3.2](../06-buku-ajar/bab-04-dasar-probabilitas.md#432-menurunkan-aturan-penjumlahan-umum) · [Bab 4 §4.4.2](../06-buku-ajar/bab-04-dasar-probabilitas.md#442-kesalahan-paling-umum-dalam-probabilitas-terapan)

### B3. Rapor daring dua tingkat `[PS-Sub-CPMK081-1 · C3 · 2]`

**Jawaban.**

- **(a)** Paralel di dalam tingkat, seri antartingkat: web 1 − 0,05² = 0,9975; basis data 1 − 0,10² = 0,99. R = 0,9975 × 0,99 = **0,9875** (0,987525).
- **(b)** Tambah di web: (1 − 0,05³)(0,99) = 0,999875 × 0,99 = **0,9899**. Tambah di basis data: 0,9975 × (1 − 0,10³) = 0,9975 × 0,999 = **0,9965**. Tambahkan di **tingkat basis data** — tingkat terlemah membatasi keandalan rangkaian seri.

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| (a) Struktur paralel di dalam tingkat dan seri antartingkat | 0,5 |
| (a) 0,9875 | 0,5 |
| (b) Kedua alternatif dihitung (0,9899 dan 0,9965) | 0,5 |
| (b) Keputusan: basis data | 0,5 |

**Kesalahan umum.** Mengalikan keempat server secara seri (0,95² × 0,90² = 0,7310) → (a) 0. Memilih web "karena server web lebih andal" tanpa hitungan → (b) 0.

*Pelajari ulang:* [Bab 5 §5.4.3](../06-buku-ajar/bab-05-probabilitas-bersyarat-bayes.md#543-keandalan-sistem)

### B4. Pesan OTP gagal `[PS-Sub-CPMK081-1 · C3 · 2]`

**Jawaban.**

- **(a)** X ~ **Binomial(n = 2.500; p = 0,0008)**. Karena n sangat besar dan p sangat kecil, Binomial dapat dihampiri **Poisson** dengan λ = np = 2.500 × 0,0008 = **2** pesan gagal per hari.
- **(b)** P(X ≤ 1) = P(0) + P(1) = e^(−2)(1 + 2) = 3 × 0,1353 = **0,4060**. (Binomial eksak: 0,4059 — hampirannya sangat dekat.)

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| (a) Binomial(2.500; 0,0008) | 0,25 |
| (a) Alasan hampiran: n besar dan p kecil | 0,5 |
| (a) λ = np = 2 | 0,25 |
| (b) P(0) + P(1) dengan PMF Poisson | 0,5 |
| (b) 0,4060 | 0,5 |

**Kesalahan umum.** Menghitung hanya P(X = 1) = 0,2707 → (b) 0,5 (PMF benar, kejadian keliru). Memakai λ = 0,0008 (peluang per pesan, bukan rata-rata per hari) → λ 0, (b) berantai.

*Pelajari ulang:* [Bab 6 §6.4.3](../06-buku-ajar/bab-06-peubah-acak-distribusi-diskret.md#643-poisson-sebagai-hampiran-binomial)

### B5. Latensi server ujian `[PS-Sub-CPMK081-1 · C3 · 2]`

**Jawaban.**

- **(a)** 36 = 48 − 2 × 6 dan 60 = 48 + 2 × 6, yaitu μ ± 2σ → **±95%** ping.
- **(b)** z = (63 − 48)/6 = **2,50**. P(X > 63) = 1 − P(Z ≤ 2,50) = 1 − 0,9938 = **0,0062** (0,62%).

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| (a) Mengenali μ ± 2σ | 0,5 |
| (a) ±95% | 0,5 |
| (b) z = 2,50 | 0,5 |
| (b) 1 − 0,9938 = 0,0062 | 0,5 |

**Kesalahan umum.** Menjawab (a) 68% (mengira 36 dan 60 sebagai μ ± 1σ) → (a) 0. Menjawab (b) 0,9938 (lupa komplemen) → 0,5.

*Pelajari ulang:* [Bab 7 §7.4.2](../06-buku-ajar/bab-07-distribusi-kontinu-normal.md#742-aturan-empiris-6895997) · [Bab 7 §7.4.3](../06-buku-ajar/bab-07-distribusi-kontinu-normal.md#743-skor-z-membandingkan-yang-tidak-sebanding)

### B6. Jeda *retry* acak `[PS-Sub-CPMK081-1 · C3 · 2]`

**Jawaban.** PDF Uniform(0, 800) setinggi 1/800 per ms; peluang = luas persegi panjang.

- **(a)** P(300 ≤ J ≤ 500) = 200/800 = **0,25**; P(J > 680) = 120/800 = **0,15**.
- **(b)** Rata-rata = titik tengah = (0 + 800)/2 = **400 ms**; P(J ≤ j) = j/800 = 0,90 → j = **720 ms**.

**Pedoman skor.** (a) 0,25 → 0,5 · 0,15 → 0,5 · (b) 400 ms → 0,5 · 720 ms → 0,5.

**Kesalahan umum.** Menghitung P(J > 680) sebagai 680/800 = 0,85 (arah ekor tertukar) → 0 untuk nilai itu. Menjawab j = 0,10 × 800 = 80 ms — itu nilai dengan P(J ≤ j) = 0,10, bukan 0,90 → 0 untuk nilai itu.

*Pelajari ulang:* [Bab 7 §7.2](../06-buku-ajar/bab-07-distribusi-kontinu-normal.md#72-distribusi-uniform-kontinu)

### B7. Jarak tempuh pengemudi `[PS-Sub-CPMK081-1 · C3 · 2]`

**Jawaban.**

- **(a)** SE = σ/√n = 18/√36 = **3 km**. Sebaran agak menceng dan n = 36 ≥ 30 → menurut Teorema Limit Pusat x̄ ≈ Normal(40; 3²). z = (45 − 40)/3 = **1,67**; P(x̄ > 45) = 1 − 0,9525 = **0,0475**.
- **(b)** Hukum akar n: galat baku separuh memerlukan n empat kali → n = **144**.

**Pedoman skor.** (a) SE = 3 → 0,5 · z = 1,67 → 0,5 · 0,0475 → 0,5 · (b) 144 → 0,5.

**Kesalahan umum.** Memakai σ = 18 sebagai penyebut z (z = 0,28; P = 0,3897) — menyamakan sebaran data dengan sebaran x̄ → kehilangan 0,5 (SE) dan 0,5 (z); P dinilai berantai. Menjawab (b) n = 72 (dua kali, bukan empat kali).

*Pelajari ulang:* [Bab 8 §8.3.3](../06-buku-ajar/bab-08-ekspektasi-varians-sampling.md#833-hukum-akar-n) · [Bab 8 §8.4.1](../06-buku-ajar/bab-08-ekspektasi-varians-sampling.md#841-pernyataan)

### B8. Durasi sesi *chatbot* `[PS-Sub-CPMK081-1 · C3 · 2]`

**Jawaban.**

- **(a)** Analis memakai z = 1,96, padahal σ populasi tidak diketahui — yang ada hanya s dari sampel — dan n = 16 kecil. Interval rata-rata semestinya memakai distribusi **t** dengan df = n − 1; interval z terlalu sempit.
- **(b)** df = **15**; t₀,₀₂₅;₁₅ = **2,131**; SE = 2,0/√16 = 0,5 menit; margin = 2,131 × 0,5 = 1,07 menit. IK 95% = 6,5 ± 1,07 = **[5,43 ; 7,57] menit** — sedikit lebih lebar daripada interval analis.

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| (a) Kekeliruan: σ tidak diketahui (s dari sampel, n kecil) → semestinya t, bukan z | 0,5 |
| (b) df = 15 dan t = 2,131 | 0,5 |
| (b) SE = 0,5 dan margin 1,07 | 0,5 |
| (b) [5,43 ; 7,57] menit | 0,5 |

**Kesalahan umum.** Menyebut kekeliruan analis "seharusnya dibagi n, bukan √n" → (a) 0. Menganggap interval analis sudah benar "karena n ≥ 15" → (a) 0. Memakai df = 16 (t = 2,120) → −0,25.

*Pelajari ulang:* [Bab 9 §9.2](../06-buku-ajar/bab-09-estimasi-interval-kepercayaan.md#92-interval-kepercayaan-rata-rata)

### B9. *Crash* aplikasi perpustakaan `[PS-Sub-CPMK081-1 · C3 · 2]`

**Jawaban.**

- **(a)** p̂ = 40/250 = 0,16; n·p̂ = 40 ≥ 10 dan n(1 − p̂) = 210 ≥ 10 → syarat **terpenuhi**.
- **(b)** SE = √(0,16 × 0,84/250) = √0,0005376 = 0,0232; margin = 1,96 × 0,0232 = 0,0454. IK 95% = 0,16 ± 0,0454 = **[0,1146 ; 0,2054]**. Batas bawahnya (±11,5%) sudah di atas 10%, jadi seluruh interval berada di atas klaim: data **tidak mendukung** klaim "paling banyak 10%"; proporsi pengguna yang mengalami *crash* diperkirakan ±11,5–20,5%.

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| (a) Kedua syarat dengan angka | 0,5 |
| (b) p̂ = 0,16 dan SE = 0,0232 | 0,5 |
| (b) Margin 0,0454 dan interval [0,1146 ; 0,2054] | 0,5 |
| (b) Kesimpulan atas klaim dengan merujuk interval: batas bawah > 0,10 → klaim tidak didukung | 0,5 |

**Kesalahan umum.** Memeriksa syarat dengan "n ≥ 30" → (a) 0. Lupa akar pada SE (memakai 0,0005376) → interval terlalu sempit; baris SE 0, interval dan kesimpulan berantai. Menolak klaim hanya karena p̂ = 16% > 10%, tanpa merujuk interval → kesimpulan 0,25.

*Pelajari ulang:* [Bab 9 §9.4](../06-buku-ajar/bab-09-estimasi-interval-kepercayaan.md#94-interval-kepercayaan-proporsi)

### B10. Survei pengelola kata sandi `[PS-Sub-CPMK081-1 · C3 · 2]`

**Jawaban.**

- **(a)** Tanpa dugaan awal, pakai p = 0,5 (memberi margin terbesar): E = 1,96 × √(0,5 × 0,5/600) = 1,96 × 0,0204 = **0,0400**, yaitu margin terbesar **±4,0 poin persen**.
- **(b)** n = 1,96² × 0,25/0,035² = 0,9604/0,001225 = **784** responden (bilangan bulat tepat; bila hasilnya pecahan, bulatkan ke atas). Tambahan dibanding (a): 784 − 600 = **184** responden.

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| (a) Margin E = z·√(p(1 − p)/n) dengan p = 0,5 | 0,5 |
| (a) ±4,0 poin persen (0,0400) | 0,5 |
| (b) Rumus ukuran sampel proporsi dengan p = 0,5 | 0,25 |
| (b) n = 784 | 0,5 |
| (b) Tambahan 184 responden | 0,25 |

**Kesalahan umum.** Lupa akar pada (a) (E = 1,96 × 0,25/600 ≈ 0,0008) → hitung (a) 0. Memakai E = 3,5 (bukan 0,035) → angka tidak masuk akal; rumus tetap dinilai. Memakai p selain 0,5 padahal tidak ada dugaan awal → rumus (a) dan (b) masing-masing paling banyak separuh.

*Pelajari ulang:* [Bab 9 §9.4](../06-buku-ajar/bab-09-estimasi-interval-kepercayaan.md#94-interval-kepercayaan-proporsi) · [Bab 9 §9.5](../06-buku-ajar/bab-09-estimasi-interval-kepercayaan.md#95-menentukan-ukuran-sampel)

---

## 3. Bagian C — Uraian Terstruktur (skor 40)

### C1. Lampiran Surel dan Pemindai *Malware* `[PS-Sub-CPMK081-1 · C3–C4 · 8]`

#### Jawaban

Misalkan M = lampiran bermalware; S₁, S₂, S₃ = berasal dari domain kampus, mitra, dan lain; T = ditandai pemindai.

**(a) (3 poin · C3).**

- Hukum probabilitas total: P(M) = P(S₁)P(M | S₁) + P(S₂)P(M | S₂) + P(S₃)P(M | S₃) = 0,70(0,001) + 0,22(0,005) + 0,08(0,05) = 0,0007 + 0,0011 + 0,0040 = **0,0058**.
- Prior P(S₃) = 0,08; *likelihood* P(M | S₃) = 0,05; *evidence* P(M) = 0,0058; posterior P(S₃ | M) = 0,0040/0,0058 = **0,6897**.
- Asumsi: porsi lampiran dan proporsi bermalware dari audit semester lalu diandaikan masih berlaku untuk lampiran sekarang.
- Tafsir: domain lain hanya 8% dari seluruh lampiran, tetapi asal ±69% lampiran bermalware.

**(b) (2,5 poin · C3).** Dengan prevalensi P(M) = 0,0058 dan P(T) = 0,025394 (dicetak; = 0,0058 × 0,95 + 0,9942 × 0,02):

- PPV = P(M | T) = P(M)·P(T | M)/P(T) = 0,0058 × 0,95/0,025394 = 0,00551/0,025394 = **0,2170**.
- NPV = P(bersih | tidak ditandai) = (0,9942 × 0,98)/(1 − 0,025394) = 0,974316/0,974606 = **0,9997**.
- Asumsi: sensitivitas dan spesifisitas pemindai sama untuk lampiran dari ketiga sumber (asumsi ini juga dipakai di (c)); juga, angka 95%/98% berlaku pada lampiran kampus ini, bukan hanya pada data uji pembuatnya. Satu asumsi sahih sudah cukup.
- Tafsir: dari lampiran yang ditandai, hanya ±22% benar bermalware (±78% alarm palsu, karena malware langka); lampiran yang tidak ditandai hampir pasti bersih (99,97%).

**(c) (2,5 poin · C4).**

- Lampiran yang dipindai = domain mitra dan domain lain (30% lampiran). Prevalensi di antaranya: P(M | S₂ ∪ S₃) = (0,0011 + 0,0040)/(0,22 + 0,08) = 0,0051/0,30 = **0,0170**.
- PPV kebijakan ini: 0,017 × 0,95/(0,017 × 0,95 + 0,983 × 0,02) = 0,01615/0,03581 = **0,4510**.
- Dari seluruh lampiran bermalware, yang tidak pernah dipindai: P(S₁ | M) = 0,0007/0,0058 = **0,1207** (±12%).
- Analisis: alarm lebih tepercaya (PPV ±22% → ±45%) dan beban pemindaian turun 70%, tetapi ±12% malware — yang datang dari domain kampus — lolos tanpa pemeriksaan. Kebijakan ini rapuh karena mengandaikan porsi malware per sumber tetap; pengirim *malware* dapat membajak akun kampus agar lampirannya tidak dipindai. Jalan tengah, mis.: domain kampus tetap dipindai dengan pemindai ringan.

*Jawaban ringkas (c), ≤ 3 kalimat di luar hitungan:* PPV naik dari ±22% menjadi ±45% dan beban pemindaian turun 70%, tetapi ±12% malware (dari domain kampus) tidak pernah diperiksa. Kebijakan ini rapuh karena mengandaikan porsi malware per sumber tetap, padahal pengirim *malware* bisa membajak akun kampus. Jadi domain kampus sebaiknya tetap dipindai, mis. dengan pemindai ringan.

#### Pedoman skor dan peta aspek

| Bagian | Langkah | Aspek | Skor |
|---|---|---|---|
| (a) | Hukum probabilitas total atas tiga sumber | Rumus | 0,5 |
| (a) | Notasi Bayes lengkap: prior, *likelihood*, *evidence*, posterior | Rumus | 0,5 |
| (a) | P(M) = 0,0058 | Hitung | 0,5 |
| (a) | P(S₃ \| M) = 0,6897 | Hitung | 0,5 |
| (a) | Asumsi tentang angka audit (diminta) | Asumsi | 0,5 |
| (a) | Tafsir posterior (diminta): 8% lampiran, ±69% malware | Interpretasi | 0,5 |
| (b) | PPV = P(M)·P(T \| M)/P(T) (0,25); NPV = P(bersih)·P(tidak ditandai \| bersih)/P(tidak ditandai) (0,25) | Rumus | 0,5 |
| (b) | PPV = 0,2170 (0,25); NPV = 0,9997 (0,25) | Hitung | 0,5 |
| (b) | Asumsi (diminta), sedikitnya satu yang sahih: sensitivitas/spesifisitas sama untuk ketiga sumber, atau angka uji pemindai berlaku pada lampiran kampus ini | Asumsi | 0,75 |
| (b) | Tafsir (diminta): PPV — sebagian besar alarm palsu (0,5); NPV — yang lolos hampir pasti bersih (0,25) | Interpretasi | 0,75 |
| (c) | Prevalensi lampiran yang dipindai sebagai probabilitas bersyarat P(M \| S₂ ∪ S₃) (0,25); PPV dengan prevalensi itu (0,25); porsi tak terpindai P(S₁ \| M) = P(M ∩ S₁)/P(M) (0,25) | Rumus | 0,75 |
| (c) | 0,0170 dan 0,4510 (0,25); 0,1207 (0,25) | Hitung | 0,5 |
| (c) | Asumsi yang membuat kebijakan rapuh (diminta): porsi malware per sumber dapat berubah karena akun kampus dibajak | Asumsi | 0,75 |
| (c) | Analisis dengan angka (diminta): yang diperoleh — PPV ±22% → ±45% atau beban turun 70% (0,25); yang dikorbankan — ±12% malware tak pernah dipindai (0,25). Jalan tengah tidak disyaratkan | Interpretasi | 0,5 |
| | **Jumlah** — rumus 2,25 · hitung 2 · asumsi 2 · interpretasi 1,75 | | **8** |

#### Kesalahan umum

- *Base rate fallacy*: "PPV = 95% karena sensitivitasnya 95%" — menukar P(T | M) dengan P(M | T) dan mengabaikan prevalensi 0,58% → rumus dan hitung (b) 0; tafsir (b) dinilai menurut isinya.
- Merata-ratakan proporsi tanpa bobot porsi: (0,1% + 0,5% + 5%)/3 = 1,87% → hukum probabilitas total 0; langkah berikutnya berantai.
- Menjawab P(S₃ | M) = 0,05 — itu *likelihood* P(M | S₃), bukan posterior.
- Pada (c), memakai prevalensi domain lain saja (5%; PPV 0,7143), padahal domain mitra juga dipindai → rumus prevalensi 0; PPV berantai.
- Pada (c), menjawab porsi tak terpindai 0,0007 — itu P(M ∩ S₁) dari **seluruh lampiran**, padahal yang ditanya porsi dari seluruh lampiran **bermalware** → rumus dan hitung untuk angka itu 0.
- Pada (c), hanya menyebut "lebih hemat" tanpa angka dan tanpa menyebut malware yang lolos → interpretasi (c) 0.

#### Contoh jawaban

| Tingkat | Contoh ringkas | Skor |
|---|---|---|
| Kurang | (a) P(M) = 0,0058 benar lewat hukum probabilitas total, tetapi "P(S₃ \| M) = 0,05"; tanpa notasi, asumsi, dan tafsir. (b) "PPV = 95% karena sensitivitasnya 95%." (c) "Setuju, lebih hemat." | 1 = (a) rumus total 0,5 + hitung 0,0058 0,5 · (b) 0 · (c) 0 |
| Cukup | (a) lengkap kecuali asumsi. (b) PPV dan NPV benar lewat rumus; tafsir hanya "±78% alarm palsu"; tanpa asumsi. (c) "Prevalensi 0,0051/0,30 = 0,017; PPV = 0,4510. PPV naik dari ±22% menjadi ±45%, tetapi malware dari domain kampus tidak diperiksa," tanpa porsinya (0,1207), tanpa asumsi, dan tanpa jalan tengah. | 5 = (a) 2,5 · (b) 1,5 · (c) 1 |
| Baik | (a) "P(M) = 0,7(0,001) + 0,22(0,005) + 0,08(0,05) = 0,0058; prior P(S₃) = 0,08, *likelihood* P(M \| S₃) = 0,05, *evidence* 0,0058, posterior 0,004/0,0058 = 0,6897, dengan asumsi angka audit masih berlaku; domain lain hanya 8% lampiran tetapi asal ±69% malware." (b) "PPV = 0,00551/0,025394 = 0,2170; NPV = 0,974316/0,974606 = 0,9997, dengan asumsi kinerja pemindai sama untuk ketiga sumber; hanya ±22% lampiran yang ditandai benar bermalware, sedangkan yang lolos hampir pasti bersih." (c) "P(M \| mitra atau lain) = 0,0051/0,30 = 0,017; PPV = 0,01615/0,03581 = 0,4510; 0,0007/0,0058 = 0,1207 malware tak pernah dipindai. PPV naik dari ±22% menjadi ±45% dan beban turun 70%, tetapi ±12% malware (dari domain kampus) lolos. Kebijakan ini rapuh karena pengirim *malware* bisa membajak akun kampus." | 8 |

Rincian skor Cukup: (a) rumus 1 + hitung 1 + tafsir 0,5 = 2,5; (b) rumus 0,5 + hitung 0,5 + tafsir PPV 0,5 = 1,5; (c) rumus prevalensi bersyarat 0,25 + rumus PPV 0,25 + hitung 0,017 dan 0,4510 0,25 + interpretasi "yang diperoleh, dengan angka" 0,25 = 1.

*Pelajari ulang:* [Bab 5 §5.1](../06-buku-ajar/bab-05-probabilitas-bersyarat-bayes.md#51-hukum-probabilitas-total) · [Bab 5 §5.2.1](../06-buku-ajar/bab-05-probabilitas-bersyarat-bayes.md#521-rumus-dan-empat-komponennya) · [Bab 5 §5.3.4](../06-buku-ajar/bab-05-probabilitas-bersyarat-bayes.md#534-menaikkan-prevalensi-strategi-yang-sering-terlupakan) · [Bab 4 §4.4](../06-buku-ajar/bab-04-dasar-probabilitas.md#44-probabilitas-bersyarat) · [Modul Minggu 5](../03-modules/week-05-teorema-bayes-kebebasan.md)

### C2. Undian Urutan Presentasi Proyek `[PS-Sub-CPMK081-1 · C3–C4 · 8]`

#### Jawaban

**(a) (2 poin · C3).** Susunan urutan: urutan tampil bermakna → **permutasi** 8! = **40.320**. Himpunan sesi pagi: yang dipersoalkan hanya keanggotaan empat kelompok, bukan urutannya → **kombinasi** C(8,4) = **70**.

**(b) (2 poin · C3).** Asumsi: undian adil — setiap susunan sama mungkin — dan setiap posisi hanya ditempati satu kelompok (posisi diundi tanpa pengembalian). Di posisi mana pun X berada, sesi X masih punya 3 posisi kosong dari 7 posisi tersisa, sehingga P(sesi sama) = 3/7 = **0,4286**. Cara pencacahan: 2 × C(6,2)/C(8,4) = 2 × 15/70 = 0,4286 (X dan Y sama-sama di pagi, ditambah sama-sama di siang).

**(c) (2 poin · C3).** Kedua kejadian **tidak saling lepas** — X pertama dan Y terakhir dapat terjadi bersamaan — jadi irisannya harus dikurangi. P(X pertama) = P(Y terakhir) = 1/8; P(keduanya) = (1/8)(1/7) = 1/56. P(X pertama ∪ Y terakhir) = 1/8 + 1/8 − 1/56 = 13/56 = **0,2321**.

**(d) (2 poin · C4).** P(A) = P(B) = 4/8 = 0,5; P(A ∩ B) = (4/8)(3/7) = 3/14 = **0,2143** ≠ P(A)·P(B) = 0,25 → A dan B **tidak saling bebas**. Masuk akal karena posisi pagi hanya empat: bila X menempati salah satunya, peluang Y mendapat posisi pagi turun dari 4/8 menjadi 3/7.

*Jawaban ringkas (d), ≤ 2 kalimat di luar hitungan:* Tidak bebas, karena P(A ∩ B) = 0,2143 ≠ 0,25 = P(A)P(B). Posisi pagi hanya empat, jadi bila X mengambil satu, peluang Y di pagi turun menjadi 3/7.

#### Pedoman skor dan peta aspek

| Bagian | Langkah | Aspek | Skor |
|---|---|---|---|
| (a) | Permutasi 8! untuk susunan (0,25); kombinasi C(8,4) untuk himpunan sesi pagi (0,25) | Rumus | 0,5 |
| (a) | Alasan pemilihan (diminta): urutan tampil bermakna (0,25); hanya keanggotaan sesi pagi yang dipersoalkan (0,25) | Asumsi | 0,5 |
| (a) | 40.320 (0,5) dan 70 (0,5) | Hitung | 1 |
| (b) | Struktur: aturan perkalian bersyarat (3 dari 7 posisi sisa) atau pencacahan 2 · C(6,2)/C(8,4) | Rumus | 0,75 |
| (b) | 3/7 = 0,4286 | Hitung | 0,5 |
| (b) | Asumsi (diminta): undian adil — setiap susunan sama mungkin, sehingga setiap kelompok berpeluang sama menempati setiap posisi | Asumsi | 0,75 |
| (c) | Aturan penjumlahan umum (0,5); irisan 1/56 = 1/8 × 1/7 dengan aturan perkalian (0,25) | Rumus | 0,75 |
| (c) | P(X pertama) = P(Y terakhir) = 1/8 (0,25); 13/56 = 0,2321 (0,25) | Hitung | 0,5 |
| (c) | Pemeriksaan saling lepas (diminta): keduanya dapat terjadi bersamaan, jadi irisan dikurangi | Asumsi | 0,75 |
| (d) | Definisi formal: P(A ∩ B) dibandingkan dengan P(A)·P(B) (atau P(B \| A) dengan P(B)) | Rumus | 0,5 |
| (d) | 0,2143 dan 0,25 | Hitung | 0,25 |
| (d) | Tidak bebas (0,5) dengan alasan posisi pagi terbatas — undian tanpa pengembalian (0,75) | Interpretasi | 1,25 |
| | **Jumlah** — rumus 2,5 · hitung 2,25 · asumsi 2 · interpretasi 1,25 | | **8** |

#### Kesalahan umum

- Menjawab (b) 1/2 "karena hanya ada dua sesi" — mengabaikan bahwa posisi X mengurangi posisi yang tersisa.
- Menjumlahkan 1/8 + 1/8 = 0,25 pada (c) tanpa mengurangi irisan → rumus (c) 0 (penjumlahan umum dan irisan), hitung 13/56 0, asumsi 0; hanya 1/8 (0,25) yang dinilai.
- Menyimpulkan (d) "bebas karena undian acak" — acak tidak sama dengan bebas; dua kejadian pada undian **tanpa pengembalian** saling bergantung.
- Memakai P(8,4) = 1.680 untuk himpunan sesi pagi (urutan di dalam sesi bukan yang ditanya) → rumus, alasan, dan hitung untuk bagian itu 0.

#### Contoh jawaban

| Tingkat | Contoh ringkas | Skor |
|---|---|---|
| Kurang | (a) "8 × 4 = 32 susunan; sesi pagi C(8,4) = 70," tanpa alasan. (b) "1/2, karena hanya ada dua sesi." (c) "1/8 + 1/8 = 0,25." (d) "Bebas, karena undiannya acak." | 1 = (a) 0,75 · (b) 0 · (c) 0,25 · (d) 0 |
| Cukup | (a) benar dengan alasan. (b) 3/7 = 0,4286 benar, tanpa asumsi. (c) "Saling lepas karena kelompoknya berbeda, jadi 1/8 + 1/8 = 0,25." (d) "0,2143 ≠ 0,25, jadi tidak bebas," tanpa alasan. | 4,75 = (a) 2 · (b) 1,25 · (c) 0,25 · (d) 1,25 |
| Baik | (a) "8! = 40.320 susunan karena urutan tampil bermakna (permutasi); C(8,4) = 70 himpunan sesi pagi karena hanya keanggotaan yang dipersoalkan (kombinasi)." (b) "Dengan asumsi undian adil (setiap susunan sama mungkin, satu posisi satu kelompok): di mana pun X, Y harus mendapat 3 dari 7 posisi sisa di sesi X → 3/7 = 0,4286." (c) "Tidak saling lepas karena X pertama dan Y terakhir bisa terjadi bersamaan, jadi 1/8 + 1/8 − (1/8)(1/7) = 13/56 = 0,2321." (d) "P(A ∩ B) = (4/8)(3/7) = 0,2143 ≠ 0,25 = P(A)P(B), jadi tidak bebas. Posisi pagi hanya empat, sehingga bila X mengambil satu, peluang Y di pagi turun menjadi 3/7." | 8 |

Rincian skor Kurang: (a) rumus kombinasi 0,25 + hitung 70 0,5 (8 × 4 bukan permutasi; tanpa alasan); (c) hanya 1/8 (0,25). Cukup: (b) rumus 0,75 + hitung 0,5; (c) hitung 1/8 0,25; (d) rumus 0,5 + hitung 0,25 + "tidak bebas" 0,5.

*Pelajari ulang:* [Bab 4 §4.5](../06-buku-ajar/bab-04-dasar-probabilitas.md#45-kaidah-pencacahan) · [Bab 4 §4.3.2](../06-buku-ajar/bab-04-dasar-probabilitas.md#432-menurunkan-aturan-penjumlahan-umum) · [Bab 5 §5.4.1](../06-buku-ajar/bab-05-probabilitas-bersyarat-bayes.md#541-definisi-formal)

### C3. Gerbang Parkir Kampus `[PS-Sub-CPMK081-1 · C3–C4 · 8]`

#### Jawaban

**(a) (2 poin · C3).** X ~ Poisson(**λ = 3** kedatangan per menit). Asumsi: kedatangan saling bebas; lajunya konstan sepanjang 07.00–08.00 (juga: dua kendaraan tidak tiba pada saat yang persis sama). P(X = 0) = e^(−3) · 3⁰/0! = **0,0498**.

**(b) (2 poin · C3).** Target "paling banyak 3 menit per jam" berarti P(X > c) ≤ 3/60 = 0,05, setara dengan P(X ≤ c) ≥ 0,95. Lanjutkan penjumlahan PMF dari nilai yang dicetak (rekursi P(k) = P(k − 1) · λ/k):

| k | P(X = k) | P(X ≤ k) | Menit per jam melampaui kapasitas k = 60 · P(X > k) |
|---|---|---|---|
| 4 | 0,1680 (dicetak) | 0,8153 | 11,08 |
| 5 | 0,1680 × 3/5 = 0,1008 | 0,9161 | **5,04** |
| 6 | 0,1008 × 3/6 = 0,0504 | **0,9665** | **2,01** |

Penjumlahan nilai PMF yang sudah dibulatkan memberi 0,8152; 0,9160; 0,9664, sehingga banyaknya menit dapat berbeda ±0,01–0,02 (mis. 60 × 0,0839 = 5,03 bila memakai 0,9161) — selisih ini diterima (toleransi pembulatan, §0.2). Dengan kapasitas 5, kedatangan melampaui kapasitas pada ±5 menit per jam > 3 menit → target **tidak terpenuhi**. Kapasitas terkecil yang memenuhi target: **c = 6** kendaraan per menit (±2 menit per jam).

**(c) (2 poin · C4).** P(X > 3) = 1 − 0,6472 = **0,3528**: pada ±35% menit (±21 dari 60 menit) kendaraan yang tiba melebihi kapasitas, sehingga antrean menumpuk — usulan ditolak. Menjelang kuliah pukul 07.30, sepeda motor cenderung datang berombongan (mis. sesudah lampu lalu lintas atau bersama teman), sehingga kedatangan tidak saling bebas dan lajunya tidak konstan; kapasitas yang diperlukan bahkan lebih dari 6. (Catatan, tidak dinilai: kedatangan berombongan membuat varians banyaknya kedatangan per menit lebih besar daripada mean.)

*Jawaban ringkas (c), ≤ 3 kalimat di luar hitungan:* P(X > 3) = 1 − 0,6472 = 0,3528, jadi pada ±35% menit (±21 menit per jam) kedatangan melebihi kapasitas dan antrean menumpuk — usulan ditolak. Menjelang 07.30 motor datang berombongan, sehingga kedatangan tidak bebas dan lajunya tidak konstan. Akibatnya kapasitas yang diperlukan bahkan lebih dari 6.

**(d) (2 poin · C3).** λ = 3 per menit = 0,05 per detik → rata-rata jeda = 1/λ = **20 detik**. Menurut **sifat tanpa memori** distribusi Eksponensial, 40 detik yang sudah lewat tidak berpengaruh: P(T ≤ 50 | T > 40) = P(T ≤ 10) = 1 − e^(−0,05 × 10) = 1 − e^(−0,5) = 1 − 0,6065 = **0,3935**. Maknanya: sudah lama menunggu tidak membuat kendaraan berikutnya lebih mungkin segera datang — peluangnya sama dengan sesaat setelah kendaraan terakhir lewat. Jalur lain: banyaknya kedatangan dalam 10 detik N ~ Poisson(0,5), P(N ≥ 1) = 1 − e^(−0,5) = 0,3935.

#### Pedoman skor dan peta aspek

| Bagian | Langkah | Aspek | Skor |
|---|---|---|---|
| (a) | λ = 3 per menit (0,25); PMF Poisson untuk k = 0 (0,25) | Rumus | 0,5 |
| (a) | 0,0498 | Hitung | 0,5 |
| (a) | Dua asumsi (diminta), 0,5 per asumsi | Asumsi | 1 |
| (b) | Menjumlahkan PMF berurutan untuk memperoleh P(X ≤ k) (0,5); target diterjemahkan menjadi P(X > c) ≤ 3/60 = 0,05, atau menit per jam = 60 · P(X > c) (0,5) | Rumus | 1 |
| (b) | P(X ≤ 5) = 0,9161 dan ±5 menit (5,03–5,04) (0,25); c = 6 dengan P(X ≤ 6) = 0,9665 atau ±2,01 menit (0,5) | Hitung | 0,75 |
| (b) | Keputusan (diminta): kapasitas 5 tidak memenuhi target karena ±5 menit > 3 menit | Interpretasi | 0,25 |
| (c) | Komplemen 1 − P(X ≤ 3) | Rumus | 0,25 |
| (c) | 0,3528 | Hitung | 0,25 |
| (c) | Kondisi nyata dan asumsi yang dilanggar (0,5); dampaknya: kapasitas perlu lebih dari 6 (0,25) | Asumsi | 0,75 |
| (c) | Analisis usulan: ±35% menit melampaui kapasitas → usulan ditolak | Interpretasi | 0,75 |
| (d) | E[T] = 1/λ dengan konversi satuan (0,25); P(T ≤ t) = 1 − e^(−λt) atau 1 − P(N = 0) Poisson (0,5) | Rumus | 0,75 |
| (d) | 20 detik (0,25); 0,3935 (0,25) | Hitung | 0,5 |
| (d) | Sifat tanpa memori (diminta) | Asumsi | 0,25 |
| (d) | Maknanya dalam konteks (diminta) | Interpretasi | 0,5 |
| | **Jumlah** — rumus 2,5 · hitung 2 · asumsi 2 · interpretasi 1,5 | | **8** |

#### Kesalahan umum

- Menetapkan kapasitas 3 "karena rata-ratanya 3" — merancang kapasitas pada rata-rata membuat sistem kewalahan pada ±35% menit (lihat (c)).
- Pada (b), membaca "3 menit per jam" sebagai probabilitas 0,03 (bukan 3/60 = 0,05) → rumus target 0; kapasitas yang dihasilkan (c = 7, karena P(X > 6) = 0,0335 > 0,03) dinilai berantai.
- Pada (b), menyatakan kapasitas 5 "hampir memenuhi" karena 0,9161 dekat 0,95 → keputusan 0.
- Tanpa konversi satuan pada (d): 1 − e^(−3 × 10) ≈ 1 → rumus (d) paling banyak 0,25, hitung 0.
- Pada (d), menghitung P(40 < T ≤ 50) = e^(−2) − e^(−2,5) = 0,0533 tanpa membaginya dengan P(T > 40) = 0,1353 — peluang tanpa syarat, padahal yang ditanya peluang bersyarat (0,0533/0,1353 = 0,3935, sama dengan hasil sifat tanpa memori) → hitung 0,3935 dan asumsi (d) 0.

#### Contoh jawaban

| Tingkat | Contoh ringkas | Skor |
|---|---|---|
| Kurang | (a) "Poisson λ = 3," tanpa asumsi dan tanpa P(X = 0). (b) "Kapasitas 3 cukup karena rata-ratanya 3." (c) "Setuju." (d) "Rata-rata jeda 1/3; P = 1 − e^(−3 × 10) ≈ 1." | 0,5 = (a) 0,25 · (b) 0 · (c) 0 · (d) 0,25 |
| Cukup | (a) λ, satu asumsi, dan 0,0498 benar. (b) "P(X ≤ 5) = 0,9161 → 60 × 0,0839 = 5,03 menit; c = 6 karena P(X ≤ 6) = 0,9665 ≥ 0,95," tanpa menyatakan bahwa kapasitas 5 tidak memenuhi target. (c) "P(X > 3) = 0,3528, jadi ±35% menit kewalahan; usulan kurang tepat," tanpa kondisi nyata. (d) 20 detik dan 0,3935 benar, tanpa menyebut sifat yang dipakai dan maknanya. | 5,75 = (a) 1,5 · (b) 1,75 · (c) 1,25 · (d) 1,25 |
| Baik | (a) "Poisson λ = 3 per menit; asumsi kedatangan saling bebas dan laju konstan; P(X = 0) = e^(−3) = 0,0498." (b) "Target: P(X > c) ≤ 3/60 = 0,05. P(5) = 0,1008, P(6) = 0,0504 → P(X ≤ 5) = 0,9161, jadi kapasitas 5 melampaui ±5,03 menit per jam > 3 — target tidak terpenuhi; P(X ≤ 6) = 0,9665 (±2 menit) → c = 6." (c) "P(X > 3) = 1 − 0,6472 = 0,3528, jadi pada ±35% menit kedatangan melebihi kapasitas — usulan ditolak. Menjelang 07.30 motor datang berombongan, jadi kedatangan tidak bebas dan lajunya tidak konstan; kapasitas yang diperlukan bahkan lebih dari 6." (d) "60/3 = 20 detik; tanpa memori, 40 detik yang lewat tidak berpengaruh: P = 1 − e^(−0,05 × 10) = 1 − e^(−0,5) = 0,3935 — lama menunggu tidak membuat kendaraan lebih mungkin segera datang." | 8 |

Rincian skor Kurang: (a) λ 0,25; (d) bentuk 1 − e^(−λt) tanpa konversi satuan 0,25. Cukup: (a) rumus 0,5 + hitung 0,5 + satu asumsi 0,5; (b) rumus 1 + hitung 0,75; (c) rumus 0,25 + hitung 0,25 + analisis 0,75; (d) rumus 0,75 + hitung 0,5.

*Pelajari ulang:* [Bab 6 §6.4.1](../06-buku-ajar/bab-06-peubah-acak-distribusi-diskret.md#641-kapan-dipakai) · [Bab 6 §6.4.2](../06-buku-ajar/bab-06-peubah-acak-distribusi-diskret.md#642-perencanaan-kapasitas) · [Bab 7 §7.3](../06-buku-ajar/bab-07-distribusi-kontinu-normal.md#73-distribusi-eksponensial)

### C4. Konsumsi Daya Server `[C4(a): PS-Sub-CPMK102-1 · C4(b)–(d): PS-Sub-CPMK081-1 · C3–C4 · 8]`

#### Jawaban

**(a) (2 poin · C3).** x̄ = 3.360/8 = **420 W**. Delapan server adalah **sampel** dari 200 server → penyebut n − 1: s² = Σ(x − x̄)²/(n − 1) = 6.300/7 = 900 → s = **30 W**.

**(b) (2 poin · C3).** z = (480 − 420)/30 = **2,00** → P(X > 480) = 1 − 0,9772 = **0,0228**. Tafsir: ±2,3% server — sekitar 5 dari 200 server — diperkirakan melebihi 480 W pada beban puncak. Asumsi: konsumsi daya per server berdistribusi Normal. Data (a) mendukungnya secara kasar — mean = median = 420 W, simpangan simetris dari −45 sampai +45 W, tanpa pencilan — tetapi dengan n = 8 pemeriksaan ini masih lemah.

**(c) (2 poin · C3).** Persentil ke-90: cari luas 0,90 di tabel: P(Z ≤ 1,28) = 0,8997 (paling dekat) → z = 1,28. Ambang = μ + zσ = 420 + 1,28 × 30 = **458,4 W** (eksak 458,45 W). Tafsir: hanya 10% server — yang konsumsinya tertinggi — melampaui ±458 W, sehingga server di atas ambang ini layak diperiksa (mis. beban atau pendinginnya).

**(d) (2 poin · C3–C4).** Asumsi: konsumsi daya ke-16 server saling bebas (karena masing-masing Normal sesuai soal, totalnya juga Normal). Total > 7.000 W setara dengan rata-rata per server x̄ > 7.000/16 = 437,5 W; SE = 30/√16 = 7,5 W → z = (437,5 − 420)/7,5 = **2,33** → P = 1 − 0,9901 = **0,0099**. (Setara: E[total] = 16 × 420 = 6.720 W; SD total = 30 × √16 = 120 W; z = 280/120 = 2,33.) Pernyataan teknisi keliru: SD total tumbuh √16 = 4 kali, bukan 16 kali, sehingga 7.680 W berada 960/120 = 8 SD di atas rata-rata total dan peluangnya praktis nol — jauh di bawah 0,0228.

*Jawaban ringkas analisis (d), ≤ 2 kalimat:* Teknisi keliru, karena SD total hanya tumbuh √16 = 4 kali (120 W), bukan 16 kali. Jadi 7.680 W berada 8 SD di atas rata-rata total 6.720 W dan peluangnya praktis nol, jauh di bawah 0,0228.

#### Pedoman skor dan peta aspek

| Bagian | Langkah | Aspek | Skor |
|---|---|---|---|
| (a) | Rumus x̄ (0,25) dan s² dengan penyebut n − 1 (0,5) | Rumus | 0,75 |
| (a) | 420 (0,25); s = 30 W (0,5) | Hitung | 0,75 |
| (a) | Alasan penyebut (diminta): delapan server adalah sampel dari 200 | Asumsi | 0,5 |
| (b) | Skor-z dan ekor kanan lewat komplemen | Rumus | 0,5 |
| (b) | z = 2,00; 0,0228 | Hitung | 0,5 |
| (b) | Asumsi Normal (diminta, 0,25); diperiksa dengan data — mean = median, simpangan simetris, tanpa pencilan (0,5). Menyebut keterbatasan n = 8 baik, tetapi tidak disyaratkan | Asumsi | 0,75 |
| (b) | Tafsir (diminta): ±2,3% server, atau ±5 dari 200 server | Interpretasi | 0,25 |
| (c) | Mencari luas 0,90 di tabel dan x = μ + zσ | Rumus | 0,75 |
| (c) | z = 1,28 (0,25); 458,4 W (0,25) | Hitung | 0,5 |
| (c) | Tafsir (diminta): 10% server dengan konsumsi tertinggi berada di atas ±458 W (0,5), dan artinya bagi tim — server di atas ambang diperiksa (0,25) | Interpretasi | 0,75 |
| (d) | E dan SD total, atau x̄ dengan SE = σ/√16 | Rumus | 0,5 |
| (d) | z = 2,33; 0,0099 | Hitung | 0,25 |
| (d) | Asumsi (diminta): konsumsi daya ke-16 server saling bebas (total ikut Normal karena setiap server Normal, sesuai soal) | Asumsi | 0,75 |
| (d) | Analisis pernyataan teknisi: SD tumbuh √n, peluang ≈ 0 | Interpretasi | 0,5 |
| | **Jumlah** — rumus 2,5 · hitung 2 · asumsi 2 · interpretasi 1,5 | | **8** |

Sub-butir (d) memuat hitung dan asumsi (C3, 1,5 poin) serta analisis pernyataan teknisi (C4, 0,5 poin), sehingga bertanda C3–C4.

#### Kesalahan umum

- s dengan penyebut n (√(6.300/8) = 28,06 W) → kehilangan rumus s² (0,5), s = 30 (0,5), dan alasan penyebut; (b)–(d) dinilai berantai.
- Pada (c), memakai z = −1,28 (ekor kiri) → 381,6 W; rumus (c) paling banyak 0,25.
- Pada (d), SD total = 16 × 30 = 480 W (menjumlahkan simpangan baku, bukan varians) → z = 0,58; rumus (d) 0, hitung berantai — padahal varians, bukan simpangan baku, yang dapat dijumlahkan untuk peubah bebas.
- Menyetujui pernyataan teknisi → interpretasi (d) 0.

#### Contoh jawaban

| Tingkat | Contoh ringkas | Skor |
|---|---|---|
| Kurang | (a) "x̄ = 420; s = √(6.300/8) = 28,06," tanpa alasan. (b) z = 60/28,06 = 2,14 → 0,0162, tanpa asumsi dan tafsir. (c) kosong. (d) "Sama dengan (b), teknisi benar." | 1,5 = (a) 0,5 · (b) 1 · (c) 0 · (d) 0 |
| Cukup | (a) benar dengan alasan sampel. (b) 0,0228 benar; "diasumsikan Normal," tanpa pemeriksaan dan tafsir. (c) 458,4 W benar, tanpa tafsir. (d) 0,0099 benar, tanpa asumsi; "teknisi salah," tanpa alasan. | 5,25 = (a) 2 · (b) 1,25 · (c) 1,25 · (d) 0,75 |
| Baik | (a) "x̄ = 420 W; s = √(6.300/7) = 30 W, penyebut n − 1 karena 8 server hanya sampel dari 200." (b) "z = 2,00 → 0,0228: ±2,3% server (±5 dari 200) melebihi 480 W; asumsi Normal — mean = median = 420, simetris tanpa pencilan, tetapi n = 8 terlalu kecil untuk memastikannya." (c) "z = 1,28 → 458,4 W; hanya 10% server di atas ±458 W, dan server itu perlu diperiksa." (d) "Dengan asumsi ke-16 server bebas: x̄ > 437,5, SE = 7,5 → z = 2,33 → 0,0099. Teknisi keliru karena SD total hanya tumbuh √16 = 4 kali (120 W); 7.680 W berada 8 SD di atas 6.720 W, jadi peluangnya praktis nol." | 8 |

Rincian skor Kurang: (a) rumus x̄ 0,25 + hitung 420 0,25; (b) rumus 0,5 + hitung berantai 0,5. Cukup: (b) rumus 0,5 + hitung 0,5 + asumsi Normal 0,25; (c) rumus 0,75 + hitung 0,5; (d) rumus 0,5 + hitung 0,25.

*Pelajari ulang:* [Bab 2](../06-buku-ajar/bab-02-statistika-deskriptif.md) (varians sampel) · [Bab 7 §7.4](../06-buku-ajar/bab-07-distribusi-kontinu-normal.md#74-distribusi-normal) · [Bab 8 §8.2](../06-buku-ajar/bab-08-ekspektasi-varians-sampling.md#82-varians-peubah-acak) · [Bab 8 §8.3.2](../06-buku-ajar/bab-08-ekspektasi-varians-sampling.md#832-sifat-distribusi-sampling-rata-rata)

### C5. Pengikut Media Sosial dan Omzet UMKM `[PS-Sub-CPMK102-1 · C3–C4 · 8]`

#### Jawaban

**(a) (2 poin · C3).** Titik UMKM viral ≈ **(30; 18)** — pengikutnya paling banyak, omzetnya termasuk paling rendah. Pada 9 titik lainnya hubungannya **positif**, kira-kira **linear**, dan **cukup kuat**. Pemisahan sah karena ada **alasan substantif**: pengikut yang datang dari satu video viral belum sempat menjadi pembeli, jadi titik itu mengikuti mekanisme yang berbeda — bukan sekadar karena letaknya jauh. Syaratnya: pemisahan dilaporkan terbuka dan kesimpulan dibatasi pada UMKM dengan pertumbuhan pengikut biasa (organik).

*Jawaban ringkas (a), ≤ 3 kalimat di luar koordinat:* Titik viral ≈ (30; 18); sembilan titik lain berhubungan positif, kira-kira linear, dan cukup kuat. Pemisahannya sah karena alasan substantif — pengikut dari video viral belum sempat menjadi pembeli. Syaratnya, pemisahan dilaporkan terbuka dan kesimpulan hanya berlaku untuk UMKM berpengikut organik.

Catatan (tidak diminta): bila titik itu ikut dihitung, r Pearson turun dari 0,80 menjadi ±0,11, sedangkan Spearman ±0,35 — satu titik dapat mengubah ringkasan korelasi secara drastis, karena itu diagram pencar wajib dilihat lebih dulu.

**(b) (2 poin · C3).** β₁ = r · s_y/s_x = 0,80 × 8/5 = **1,28** (juta rupiah per ribu pengikut); β₀ = ȳ − β₁x̄ = 30 − 1,28 × 12 = **14,64** juta. ŷ = 14,64 + 1,28 × 15 = **33,84 juta rupiah**.

**(c) (2 poin · C4).** R² = 0,80² = **0,64**: 64% keragaman omzet berkaitan linear dengan banyaknya pengikut; 36% berkaitan dengan faktor lain. **Plot P**: sebaran residual **melebar** seiring prediksi membesar (pola corong) → asumsi **E** (*equal variance*, ragam residual sama) dilanggar; tindak lanjut: transformasi log omzet atau regresi terboboti. **Plot Q**: residual tersebar acak di sekitar 0 dengan lebar kira-kira tetap, tanpa pola melengkung → tidak tampak pelanggaran L atau E.

**(d) (2 poin · C4).** Prediksi garis (b) untuk 90 ribu pengikut: ŷ = 14,64 + 1,28 × 90 = **129,84 juta rupiah**. Data observasional tidak membuktikan sebab-akibat: UMKM dengan produk bagus, usia usaha lebih lama, atau anggaran iklan besar dapat sekaligus punya banyak pengikut dan omzet tinggi (perancu), atau omzet besar yang menarik pengikut (arah terbalik); lagi pula pengikut yang dibeli bukan calon pembeli. Data hanya mencakup 3–20 ribu pengikut, sehingga 90 ribu adalah **ekstrapolasi** jauh di luar rentang dan prediksi ±130 juta — lebih dari tiga kali omzet tertinggi pada data — tidak dapat dipercaya. Klaim tidak didukung; tafsir kemiringan yang sah: setiap tambahan 1.000 pengikut **dikaitkan dengan** omzet bulanan ±Rp1,28 juta lebih tinggi, di dalam rentang 3–20 ribu pengikut.

*Jawaban ringkas (d), ≤ 3 kalimat di luar hitungan:* Data observasional: produk bagus atau anggaran iklan besar dapat membuat pengikut dan omzet sama-sama tinggi. Data hanya mencakup 3–20 ribu pengikut, jadi prediksi 129,84 juta untuk 90 ribu adalah ekstrapolasi yang tidak dapat dipercaya. Klaim tidak didukung — yang sah hanya "tiap 1.000 pengikut dikaitkan dengan omzet ±Rp1,28 juta lebih tinggi" di rentang data.

Catatan nilai (tidak dinilai): membeli pengikut palsu memberi calon pembeli kesan "laris" yang tidak sesuai kenyataan — bertentangan dengan kejujuran dan amanah dalam berdagang.

#### Pedoman skor dan peta aspek

| Bagian | Langkah | Aspek | Skor |
|---|---|---|---|
| (a) | Arah, bentuk, dan kekuatan — 0,25 per unsur | Rumus | 0,75 |
| (a) | Koordinat titik viral ≈ (30; 18) | Hitung | 0,25 |
| (a) | Sah karena alasan substantif, bukan sekadar karena jauh (diminta) | Asumsi | 0,5 |
| (a) | Syarat (diminta): dilaporkan terbuka; kesimpulan dibatasi | Interpretasi | 0,5 |
| (b) | β₁ = r · s_y/s_x (0,5); β₀ = ȳ − β₁x̄ (0,5) | Rumus | 1 |
| (b) | 1,28 (0,25); 14,64 (0,25); 33,84 juta (0,5) | Hitung | 1 |
| (c) | R² = r² | Rumus | 0,25 |
| (c) | 0,64 | Hitung | 0,25 |
| (c) | Plot P (diminta): asumsi E dilanggar (0,25) dengan tanda residual melebar seperti corong (0,25); satu tindak lanjut (0,25). Plot Q (diminta): tidak tampak pelanggaran (0,25) | Asumsi | 1 |
| (c) | Tafsir R² (diminta) | Interpretasi | 0,5 |
| (d) | Persamaan (b) dipakai pada x = 90 | Rumus | 0,25 |
| (d) | 129,84 juta | Hitung | 0,25 |
| (d) | Sebab-akibat (diminta): data observasional, dengan satu penjelasan alternatif yang sahih — perancu, arah terbalik, **atau** sifat pengikut yang dibeli (0,5). Pernyataan umum "korelasi bukan sebab-akibat" tanpa penjelasan alternatif: 0,25 | Asumsi | 0,5 |
| (d) | Rentang data (diminta): 90 ribu di luar 3–20 ribu → ekstrapolasi, prediksi tidak dapat dipercaya (0,5); tafsir kemiringan yang sah, dengan bahasa asosiatif (diminta) (0,25); kesimpulan bahwa klaim tidak didukung data (0,25) | Interpretasi | 1 |
| | **Jumlah** — rumus 2,25 · hitung 1,75 · asumsi 2 · interpretasi 2 | | **8** |

Bahasa kausal ("menaikkan", "menyebabkan") pada tafsir (c) atau (d) membatasi skor interpretasi butir ini paling banyak 1 dari 2 (§0.1), dikenakan sekali per butir.

#### Kesalahan umum

- Membaca kesepuluh titik sekaligus dan menyimpulkan hubungan "lemah" — satu titik berpengaruh menyembunyikan pola sembilan titik lainnya.
- "Dibuang saja karena pencilan" — pencilan tidak boleh dibuang tanpa alasan substantif → asumsi (a) 0.
- β₁ = r · s_x/s_y = 0,5 (terbalik) → rumus β₁ dan nilai β₁ 0; β₀ dan ŷ dinilai berantai.
- Menjawab R² = 0,80 (lupa mengkuadratkan) → rumus, hitung, dan tafsir R² 0.
- Menyebut asumsi N (kenormalan) yang dilanggar pada plot P — pola corong menandakan ragam tidak sama, bukan ketidaknormalan → baris asumsi E 0 (tanda "melebar" yang dideskripsikan benar tetap 0,25).
- Menyatakan plot Q juga melanggar asumsi (mis. "titiknya tersebar, jadi tidak linear") → baris plot Q 0.

#### Contoh jawaban

| Tingkat | Contoh ringkas | Skor |
|---|---|---|
| Kurang | (a) "Pencilan (30; 18); hubungan lemah; dibuang saja karena jauh." (b) "β₁ = 0,80 × 5/8 = 0,5; β₀ = 30 − 0,5 × 12 = 24; ŷ = 31,5." (c) "R² = 0,80; plot P dan Q sama-sama melanggar kenormalan." (d) "Benar, karena korelasinya positif; omzet akan naik berlipat." | 1,5 = (a) 0,25 · (b) 1,25 · (c) 0 · (d) 0 |
| Cukup | (a) koordinat dan "positif, linear, kuat" benar; "sah karena pencilan," tanpa alasan substantif dan syarat. (b) lengkap dan benar. (c) "R² = 0,64: 64% keragaman omzet berkaitan linear dengan pengikut; plot P melanggar asumsi E," tanpa tanda, tindak lanjut, dan penilaian plot Q. (d) "Korelasi bukan sebab-akibat, jadi klaim tidak terbukti," tanpa prediksi, tanpa rentang data, dan tanpa tafsir kemiringan. | 4,75 = (a) 1 · (b) 2 · (c) 1,25 · (d) 0,5 |
| Baik | (a) "Titik viral ≈ (30; 18); sembilan titik lain berhubungan positif, kira-kira linear, dan cukup kuat. Pemisahannya sah karena pengikut dari video viral belum sempat menjadi pembeli, asalkan dilaporkan terbuka dan kesimpulan dibatasi pada UMKM berpengikut organik." (b) "β₁ = 0,80 × 8/5 = 1,28; β₀ = 30 − 1,28 × 12 = 14,64; ŷ(15) = 14,64 + 19,2 = 33,84 juta." (c) "R² = 0,64: 64% keragaman omzet berkaitan linear dengan pengikut. Plot P: residual melebar seperti corong → asumsi E dilanggar; transformasi log omzet. Plot Q: acak dengan lebar tetap, tidak ada pelanggaran." (d) "ŷ(90) = 14,64 + 115,2 = 129,84 juta. Data observasional: produk bagus atau iklan besar dapat membuat pengikut dan omzet sama-sama tinggi. Data hanya 3–20 ribu pengikut, jadi 90 ribu adalah ekstrapolasi; klaim tidak didukung — yang sah hanya 'tiap 1.000 pengikut dikaitkan dengan omzet ±Rp1,28 juta lebih tinggi'." | 8 |

Rincian skor Kurang: (a) koordinat 0,25; (b) rumus β₀ = ȳ − β₁x̄ 0,5, lalu β₀ = 24 (0,25) dan ŷ = 31,5 (0,5) dinilai berantai; rumus dan nilai β₁ 0; (c) dan (d) 0. Bahasa kausal di (d) tidak menambah pengurangan, karena skor interpretasi butir ini sudah 0 (≤ 50% porsinya). Cukup: (a) rumus 0,75 + koordinat 0,25; (c) rumus 0,25 + hitung 0,25 + asumsi E 0,25 + tafsir R² 0,5; (d) "korelasi bukan sebab-akibat" tanpa penjelasan alternatif 0,25 + kesimpulan klaim tidak didukung 0,25.

*Pelajari ulang:* [Bab 3](../06-buku-ajar/bab-03-visualisasi-data-statistik.md) (diagram pencar) · [Bab 13 §13.2](../06-buku-ajar/bab-13-korelasi-regresi-linear.md#132-korelasi-bukan-sebab-akibat) · [Bab 13 §13.3](../06-buku-ajar/bab-13-korelasi-regresi-linear.md#133-regresi-linear-sederhana) · [Bab 13 §13.3.3](../06-buku-ajar/bab-13-korelasi-regresi-linear.md#1333-bahaya-ekstrapolasi) · [Bab 13 §13.4](../06-buku-ajar/bab-13-korelasi-regresi-linear.md#134-diagnostik-residual-asumsi-line)

---

## 4. Bagian D — Studi Kasus Terpadu: Indeks Baru Katalog Perpustakaan Digital (skor 25)

Butir utuh: `[PS-Sub-CPMK102-1: D1, D2, D5, D8 · PS-Sub-CPMK081-1: D3, D4, D6, D7 · C4 · 25]`. Peta sub-butir ke [kisi-kisi §5](kisi-kisi-uas.md#5-bentuk-soal-studi-kasus-terpadu-bagian-d--25): D1–D8 = butir 1–8, dengan skor sama dengan bobotnya (2/3/4/4/4/3/3/2%).

### D1. Skala dan ringkasan `[PS-Sub-CPMK102-1 · C3 · 2]`

**Jawaban.** `kesulitan_kueri` **ordinal** (urutan mudah < sedang < sulit bermakna, jarak antartingkat tidak dijamin sama); `waktu_baru_ms` **rasio** (0 ms berarti tanpa waktu tunggu); `ditemukan_baru` **nominal** (biner, tanpa urutan).

- (i) **Tidak sah**: simpangan baku memperlakukan kode 1–2–3 seolah jaraknya sama. Pengganti yang sah: frekuensi atau proporsi tiap tingkat, atau median beserta kuartil kategori.
- (ii) **Sah**: koefisien variasi memerlukan nol yang bermakna, dan waktu respons berskala rasio.
- (iii) **Tidak sah**: kategori nominal tidak berurutan, jadi median tidak bermakna. Pengganti yang sah: proporsi "ya" = 30/36 = 83% (atau modus "ya").

| Langkah | Aspek | Skor |
|---|---|---|
| Tiga skala, 0,25 per skala | R | 0,75 |
| (i) Tidak sah (0,25); pengganti sah untuk ordinal (0,25) | R | 0,5 |
| (ii) Sah | R | 0,25 |
| (iii) Tidak sah (0,25); pengganti sah untuk nominal (0,25) | R | 0,5 |

**Kesalahan umum.** Menyebut `kesulitan_kueri` interval lalu menerima (i) → skala itu dan (i) 0. Menolak (ii) "karena koefisien variasi hanya untuk membandingkan dua kelompok" → (ii) 0; koefisien variasi juga sah untuk satu variabel rasio.

### D2. Berpasangan atau bebas `[PS-Sub-CPMK102-1 · C4 · 3]`

**Jawaban.** **Berpasangan**: setiap kueri yang sama dijalankan pada kedua indeks, jadi kedua pengukuran membentuk pasangan per kueri. Pembanding Welch (keliru): t = 31/√(95²/36 + 90²/36) = 31/√475,69 = 31/21,81 = **1,42**. Nilainya jauh lebih kecil karena uji bebas memasukkan variasi besar **antarkueri** (s = 95 dan 90 ms — ada kueri yang memang lambat dan ada yang cepat) ke penyebut, sedangkan selisih per kueri menghilangkan variasi itu (s_d = 48 ms); akibatnya uji yang keliru kehilangan kuasa dan bisa gagal menemukan penurunan yang nyata.

*Jawaban ringkas (≤ 3 kalimat di luar hitungan):* Berpasangan, karena kueri yang sama dijalankan pada kedua indeks. Welch keliru memberi t = 31/21,81 = 1,42. Nilainya kecil karena variasi antarkueri (s = 95 dan 90 ms) ikut masuk penyebut, padahal selisih per kueri menghilangkannya (s_d = 48 ms).

| Langkah | Aspek | Skor |
|---|---|---|
| Berpasangan | R | 0,5 |
| Alasan dari cara data dikumpulkan (kueri yang sama, dua kali) | A | 0,75 |
| t Welch = 1,42 | H | 0,75 |
| Penjelasan (diminta): variasi antarkueri masuk penyebut uji bebas, sedangkan selisih per kueri menghilangkannya (s_d = 48). Menyebut akibatnya — kehilangan kuasa — dianjurkan, tetapi tidak disyaratkan | I | 1 |

**Kesalahan umum.** "Bebas, karena indeks lama dan baru berbeda" — yang menentukan adalah apakah **unit yang sama** diukur dua kali → R dan A 0 (uji dipilih dengan alasan keliru); D5–D7 dinilai berantai bila konsisten.

### D3. Hipotesis, arah, dan α `[PS-Sub-CPMK081-1 · C4 · 4]`

**Jawaban.** H₀: μ_d ≤ 0 (atau μ_d = 0) — indeks baru tidak lebih cepat; H₁: μ_d > 0 — indeks baru lebih cepat (d = lama − baru). **Satu sisi kanan**, karena keputusan migrasi hanya diambil bila indeks baru lebih cepat. Arah harus ditetapkan sebelum melihat data; memilih arah sesudah melihat hasil (HARKing) diam-diam melipatgandakan galat Tipe I. α: galat Tipe I = bermigrasi padahal indeks baru tidak lebih cepat (biaya lisensi dan pelatihan tanpa manfaat); galat Tipe II = melewatkan percepatan yang nyata. Karena galat Tipe I berbiaya langsung, mis. **α = 0,01**; α = 0,05 juga diterima bila alasannya menimbang kedua galat.

*Jawaban ringkas (≤ 3 kalimat di luar notasi):* H₀: μ_d ≤ 0; H₁: μ_d > 0, satu sisi kanan karena tim hanya bermigrasi bila indeks baru lebih cepat, dan arah ini ditetapkan sebelum melihat data karena memilihnya sesudah melihat hasil menggandakan galat Tipe I. Galat Tipe I berarti membayar lisensi dan pelatihan untuk indeks yang tidak lebih cepat, sedangkan galat Tipe II berarti melewatkan percepatan yang nyata. Karena galat Tipe I berbiaya langsung, saya memilih α = 0,01.

| Langkah | Aspek | Skor |
|---|---|---|
| H₀ dan H₁ dalam notasi μ_d, H₀ memuat tanda sama dengan. H₀ dan H₁ yang benar tetapi tidak dalam notasi μ_d (mis. μ_lama dan μ_baru): 0,5 | R | 1 |
| Arah satu sisi dengan alasan dari keputusan migrasi | R | 1 |
| Mengapa arah ditetapkan sebelum melihat data | A | 0,75 |
| α dengan alasan dari konsekuensi galat Tipe I dan Tipe II | I | 1,25 |

Uji **dua sisi** dengan alasan yang ditulis (mis. "tim juga perlu tahu bila indeks baru lebih lambat") diterima sebagai pilihan kurang optimal: langkah arah 0,5 dari 1; langkah lain dinilai biasa, dan D5 memakai batas *p-value* dua sisi. Dua sisi tanpa alasan → langkah arah 0. α = 0,05 "karena lazim" tanpa menimbang galat → langkah α paling banyak 0,25.

### D4. Asumsi dan Teorema Limit Pusat `[PS-Sub-CPMK081-1 · C4 · 4]`

**Jawaban.** (1) **Pasangan saling bebas** antarkueri — diperiksa dengan menelaah rancangan: kueri berbeda, urutan pengujian diacak, *cache* dikosongkan sebelum setiap kueri. (2) **Selisih d berdistribusi kira-kira Normal, atau n cukup besar** — diperiksa pada **selisih** (histogram atau Q-Q plot d), bukan pada waktu lama dan baru secara terpisah. Histogram d agak menceng tanpa pencilan ekstrem; menurut tabel Bab 8, sebaran agak menceng memerlukan n ≥ 30, jadi dengan n = 36 distribusi sampling d̄ sudah mendekati Normal menurut Teorema Limit Pusat dan uji-t berpasangan layak. Homogenitas ragam tidak diperlukan pada uji berpasangan.

*Jawaban ringkas (≤ 3 kalimat):* Pasangan antarkueri saling bebas — diperiksa dari rancangan (kueri berbeda, urutan diacak, *cache* dikosongkan) — dan selisih d kira-kira Normal atau n cukup besar — diperiksa dengan histogram atau Q-Q plot selisih d. Histogram d agak menceng tanpa pencilan, dan untuk sebaran agak menceng aturan praktisnya n ≥ 30. Dengan n = 36, distribusi sampling d̄ sudah mendekati Normal menurut Teorema Limit Pusat, jadi uji-t layak.

| Langkah | Aspek | Skor |
|---|---|---|
| Asumsi kebebasan (0,5) dan cara memeriksanya dari rancangan (0,75) | A | 1,25 |
| Asumsi kenormalan **selisih** atau n besar (0,5; kenormalan disebut tanpa menyebut selisih: 0,25) dan cara memeriksanya pada d (0,75) | A | 1,25 |
| Analisis TLP: bentuk sebaran selisih (agak menceng) → aturan n ≥ 30 (0,5); distribusi sampling d̄ mendekati Normal (0,5); n = 36 memadai (0,5) | I | 1,5 |

**Kesalahan umum.** Memeriksa kenormalan waktu lama dan baru secara terpisah, atau menuntut uji Levene — keduanya tidak relevan untuk uji berpasangan → cara memeriksa asumsi kedua 0. Menyatakan "data harus Normal" tanpa Teorema Limit Pusat → analisis TLP 0. Menyebut "n ≥ 30, jadi TLP berlaku" tanpa mengaitkannya dengan bentuk sebaran selisih → baris aturan n ≥ 30 0 (aturan itu bergantung pada bentuk sebaran).

### D5. Statistik uji dan *p-value* `[PS-Sub-CPMK102-1 · C3 · 4]`

**Jawaban.** SE = s_d/√n = 48/6 = 8 ms; t = d̄/SE = 31/8 = **3,875**; df = 35. Dari tabel-t df = 35: t₀,₀₀₅ = 2,724 < 3,875 → **p < 0,005** (satu sisi; dua sisi p < 0,01). Keputusan: **tolak H₀** pada α = 0,01 (juga pada 0,05). Tafsir: bila indeks baru sebenarnya tidak lebih cepat, penurunan rata-rata sebesar 31 ms atau lebih hanya akan muncul pada kurang dari 0,5% pengulangan studi seperti ini.

| Langkah | Aspek | Skor |
|---|---|---|
| SE = 8 | R | 0,5 |
| t = 3,875 | H | 0,75 |
| df = 35 | R | 0,25 |
| Batas *p-value* dari tabel (p < 0,005 satu sisi, atau p < 0,01 dua sisi sesuai D3) | H | 1 |
| Keputusan pada α pilihan | I | 0,5 |
| Tafsir *p-value* yang benar: peluang data seekstrem ini **bila H₀ benar** | I | 1 |

**Kesalahan umum.** "Peluang H₀ benar kurang dari 0,5%" — membalik arah persyaratan, *p* = P(data | H₀), bukan P(H₀ | data) → tafsir 0. Memakai Welch (t = 1,42) lalu menyimpulkan "H₀ terbukti benar" → kesalahan uji dihukum di D2; di sini hitungan dinilai berantai, tetapi "H₀ terbukti benar" membatasi skor interpretasi D5 paling banyak 0,75 dari 1,5 (§0.1).

### D6. Interval kepercayaan selisih `[PS-Sub-CPMK081-1 · C3 · 3]`

**Jawaban.** d̄ ± t₀,₀₂₅;₃₅ · s_d/√n = 31 ± 2,030 × 8 = 31 ± 16,24 → **[14,76 ; 47,24] ms**. Tafsir: rata-rata penurunan waktu respons yang sebenarnya diperkirakan antara ±15 dan ±47 ms dengan tingkat kepercayaan 95% — artinya, dari banyak pengulangan, ±95% interval yang disusun dengan cara ini memuat μ_d. Interval seluruhnya di atas 0, sejalan dengan D5.

| Langkah | Aspek | Skor |
|---|---|---|
| Rumus dengan t₀,₀₂₅;₃₅ = 2,030 dan SE = 8 | R | 1 |
| [14,76 ; 47,24] ms | H | 1 |
| Tafsir kontekstual yang benar | I | 1 |

**Kesalahan umum.** Memakai s_d = 48 sebagai margin (31 ± 1,96 × 48) — itu sebaran selisih per kueri, bukan ketidakpastian rata-ratanya → rumus 0, dan interval tidak dinilai berantai karena tidak ada SE. "95% probabilitas μ_d di antara 14,76 dan 47,24" → tafsir 0,5.

### D7. Ukuran efek dan kebermaknaan praktis `[PS-Sub-CPMK081-1 · C4 · 3]`

**Jawaban.** d = d̄/s_d = 31/48 = **0,65** → efek **sedang** (0,5–0,8). Kriteria tim: penurunan sedikitnya 50 ms. Seluruh IK 95% [14,76 ; 47,24] ms berada **di bawah** 50 ms, jadi penurunannya nyata secara statistik tetapi belum mencapai ambang yang ditetapkan tim sendiri. Signifikansi statistik tidak sama dengan kebermaknaan praktis: keputusan migrasi perlu menimbang manfaat lain (mis. ketepatan hasil pencarian) dan biaya lisensi, bukan hanya *p-value*.

*Jawaban ringkas (≤ 3 kalimat di luar hitungan):* d = 31/48 = 0,65, efek sedang. Seluruh IK 95% (14,76–47,24 ms) berada di bawah ambang 50 ms, jadi penurunannya nyata secara statistik tetapi belum bermakna praktis menurut kriteria tim. Keputusan migrasi perlu menimbang manfaat lain dan biaya, bukan hanya *p-value*.

| Langkah | Aspek | Skor |
|---|---|---|
| d = 0,65 | H | 0,75 |
| Kategori sedang | I | 0,5 |
| Membandingkan IK dengan 50 ms: seluruh interval di bawah ambang | I | 1,25 |
| Kesimpulan: signifikan statistik ≠ bermakna praktis | I | 0,5 |

**Kesalahan umum.** Membandingkan d̄ = 31 dengan 50 tanpa memakai interval → langkah IK 0,5 dari 1,25. "Signifikan dan efeknya sedang, jadi bermakna" tanpa kriteria tim → langkah IK dan kesimpulan 0.

### D8. Batas inferensi `[PS-Sub-CPMK102-1 · C4 · 2]`

**Jawaban.** Pernyataan kepala perpustakaan melampaui studi karena cara data diperoleh: 36 kueri **disusun tim**, bukan sampel acak dari kueri pengguna, dan diuji **di luar jam layanan dengan *cache* kosong**, sehingga hasilnya tidak mewakili kueri dan beban pencarian pengguna sebenarnya (mis. pada jam sibuk). Rumusan yang didukung data: pada 36 kueri uji dalam kondisi terkendali itu, indeks baru rata-rata ±15–47 ms lebih cepat (IK 95%).

| Langkah | Aspek | Skor |
|---|---|---|
| Alasan dari cara data diperoleh (diminta): sedikitnya satu sumber keterbatasan yang sahih — kueri pilihan tim, bukan sampel acak; atau kondisi uji di luar jam layanan dengan *cache* kosong (0,5) — beserta akibatnya: tidak mewakili pencarian pengguna sebenarnya (0,5) | A | 1 |
| Rumusan kesimpulan yang didukung data (diminta): dibatasi pada kueri dan kondisi uji (0,75), dengan arah atau besar efek (0,25) | I | 1 |

**Kesalahan umum.** "Datanya kurang" tanpa menyebut aspek cara data diperoleh → alasan 0. Menyetujui pernyataan itu "karena p < 0,005" → 0. Rumusan pengganti yang masih umum ("indeks baru lebih cepat") tanpa batas kueri dan kondisi uji → rumusan 0,25 (arah efek saja).

### Contoh jawaban Bagian D

| Tingkat | Contoh ringkas | Skor |
|---|---|---|
| Kurang | D1: "`kesulitan_kueri` interval, `waktu_baru_ms` rasio, `ditemukan_baru` ordinal; ketiga ringkasan sah." D2: "Bebas, karena indeksnya berbeda; t Welch = 1,42." D3: "H₀: μ_lama = μ_baru; H₁: μ_lama ≠ μ_baru; α = 0,05," tanpa alasan. D4: "Data harus Normal." D5: "SE = 8, t = 3,875, jadi peluang H₀ benar 0,5%; tolak H₀," tanpa df dan batas *p*. D6: "31 ± 1,96 × 48 = [−63,08 ; 125,08]." D7: "d = 0,65, efek besar." D8: "Datanya kurang." | 4,5 |
| Cukup | D1: skala benar; "(i) tidak sah, pakai median; (ii) sah; (iii) tidak sah," tanpa pengganti untuk (iii). D2: berpasangan dengan alasan, tanpa Welch dan penjelasan. D3: H₀: μ_d ≤ 0, H₁: μ_d > 0, satu sisi dengan alasan; "α = 0,05 karena lazim"; tanpa alasan arah sebelum data. D4: "Pasangan antarkueri saling bebas dan selisih d kira-kira Normal," tanpa cara memeriksa; "histogram d agak menceng, jadi perlu n ≥ 30; n = 36 ≥ 30, uji-t layak." D5: hitungan, batas *p*, dan keputusan benar; "peluang H₀ benar < 0,5%." D6: interval benar; "95% probabilitas μ_d di dalamnya." D7: d = 0,65 sedang; "signifikan dan efek sedang, jadi bermakna." D8: "Tidak dapat digeneralisasi ke jam sibuk, karena pengujian dilakukan di luar jam layanan," tanpa rumusan kesimpulan yang didukung. | 15 |
| Baik | Delapan jawaban di bawah tabel ini. | 25 |

Rincian skor Kurang: D1 0,5 (waktu rasio 0,25 + (ii) sah 0,25) · D2 0,75 (Welch) · D3 0,5 (H₀/H₁ benar tetapi tidak dalam notasi μ_d) · D4 0,25 (kenormalan disebut tanpa menyebut selisih) · D5 1,75 (SE 0,5 + t 0,75 + keputusan 0,5) · D6 0 · D7 0,75 · D8 0 = **4,5**. Cukup: D1 1,75 (skala 0,75 + (i) 0,5 + (ii) 0,25 + (iii) "tidak sah" 0,25) · D2 1,25 (berpasangan 0,5 + alasan 0,75) · D3 2,25 (H₀/H₁ 1 + arah 1 + α 0,25) · D4 2 (asumsi kebebasan 0,5 + asumsi kenormalan selisih 0,5 + TLP: agak menceng → n ≥ 30 0,5 dan n = 36 memadai 0,5) · D5 3 · D6 2,5 (tafsir 0,5) · D7 1,25 (d 0,75 + kategori 0,5) · D8 1 (alasan beserta akibatnya) = **15**.

**Contoh jawaban Baik (25 poin), harfiah:**

- **D1.** "`kesulitan_kueri` ordinal, `waktu_baru_ms` rasio, `ditemukan_baru` nominal. (i) tidak sah — jarak antartingkat tidak dijamin sama; ganti dengan proporsi tiap tingkat. (ii) sah. (iii) tidak sah — nominal tidak berurutan; ganti dengan proporsi 'ya' = 83%."
- **D2.** "Berpasangan, karena kueri yang sama dijalankan pada kedua indeks. Welch keliru memberi t = 31/21,81 = 1,42. Nilainya kecil karena variasi antarkueri (s = 95 dan 90 ms) ikut masuk penyebut, padahal selisih per kueri menghilangkannya (s_d = 48 ms)."
- **D3.** "H₀: μ_d ≤ 0; H₁: μ_d > 0, satu sisi kanan karena tim hanya bermigrasi bila indeks baru lebih cepat, dan arah ditetapkan sebelum melihat data karena memilihnya sesudah melihat hasil menggandakan galat Tipe I. Galat Tipe I berarti membayar lisensi untuk indeks yang tidak lebih cepat, galat Tipe II melewatkan percepatan yang nyata. Karena galat Tipe I berbiaya langsung, α = 0,01."
- **D4.** "Pasangan antarkueri bebas — diperiksa dari rancangan (kueri berbeda, urutan diacak, *cache* dikosongkan); selisih d kira-kira Normal atau n besar — diperiksa dengan histogram atau Q-Q plot d. Histogram d agak menceng tanpa pencilan, dan untuk sebaran agak menceng aturan praktisnya n ≥ 30. Dengan n = 36 distribusi sampling d̄ mendekati Normal menurut Teorema Limit Pusat, jadi uji-t layak."
- **D5.** "SE = 48/6 = 8; t = 31/8 = 3,875; df = 35; t > t₀,₀₀₅ = 2,724 → p < 0,005; tolak H₀ pada α = 0,01. Bila indeks baru sebenarnya tidak lebih cepat, penurunan rata-rata ≥ 31 ms hanya muncul pada kurang dari 0,5% pengulangan."
- **D6.** "31 ± 2,030 × 8 = [14,76 ; 47,24] ms: rata-rata penurunan sebenarnya diperkirakan 15–47 ms dengan tingkat kepercayaan 95%, artinya ±95% interval yang disusun dengan prosedur ini memuat μ_d."
- **D7.** "d = 31/48 = 0,65, efek sedang. Seluruh IK 95% (14,76–47,24 ms) di bawah ambang 50 ms, jadi penurunannya nyata secara statistik tetapi belum bermakna praktis menurut kriteria tim. Keputusan migrasi perlu menimbang manfaat lain dan biaya, bukan hanya *p-value*."
- **D8.** "Pernyataan itu melampaui studi karena 36 kueri disusun tim, bukan sampel acak kueri pengguna, sehingga tidak mewakili pencarian pengguna sebenarnya. Yang didukung data: pada 36 kueri uji dalam kondisi terkendali itu, indeks baru rata-rata ±15–47 ms lebih cepat."

*Pelajari ulang:* [Bab 1 §1.4.2](../06-buku-ajar/bab-01-pengantar-statistika-ketidakpastian.md#142-empat-skala-pengukuran) · [Bab 1 §1.3.3](../06-buku-ajar/bab-01-pengantar-statistika-ketidakpastian.md#133-sampel-yang-baik-dan-yang-menyesatkan) · [Bab 2 §2.3.3](../06-buku-ajar/bab-02-statistika-deskriptif.md#233-koefisien-variasi) · [Bab 10 §10.1.2](../06-buku-ajar/bab-10-uji-hipotesis-satu-sampel.md#1012-merumuskan-hipotesis) · [Bab 10 §10.2.1](../06-buku-ajar/bab-10-uji-hipotesis-satu-sampel.md#1021-konsekuensi-dalam-konteks-nyata) · [Bab 10 §10.4](../06-buku-ajar/bab-10-uji-hipotesis-satu-sampel.md#104-memahami-p-value) · [Bab 10 §10.5](../06-buku-ajar/bab-10-uji-hipotesis-satu-sampel.md#105-signifikansi-statistik-vs-praktis) · [Bab 11 §11.3](../06-buku-ajar/bab-11-uji-hipotesis-dua-sampel.md#113-uji-t-berpasangan) · [Bab 8 §8.4.3](../06-buku-ajar/bab-08-ekspektasi-varians-sampling.md#843-berapa-n-yang-cukup-besar) · [Bab 9 §9.2](../06-buku-ajar/bab-09-estimasi-interval-kepercayaan.md#92-interval-kepercayaan-rata-rata) · [Bab 9 §9.3](../06-buku-ajar/bab-09-estimasi-interval-kepercayaan.md#93-menafsirkan-95-kepercayaan) · [Modul Minggu 12](../03-modules/week-12-uji-hipotesis-dua-sampel.md)

---

## 5. Memeriksa Angka dengan Python

Semua angka di pembahasan ini — angka kunci, angka antara pada langkah jawaban, dan angka pada *Kesalahan umum* serta contoh *Kurang*/*Cukup* — diperiksa ulang dengan Python (NumPy, SciPy) pada 9 Oktober 2026. Blok berikut dapat dijalankan di Google Colab **sesudah** Anda mengerjakan secara manual — UAS tetap tanpa komputer dan tanpa AI. Setiap nilai di kolom *Keluaran Python* pada tabel di bawahnya dicetak oleh salah satu baris `print` blok ini (komentar di ujung baris memuat keluaran yang diharapkan; Python memakai titik desimal, komentar memakai koma desimal dan titik koma sebagai pemisah daftar).

```python
# Pemeriksaan angka Latihan UAS Probabilitas dan Statistik: angka kunci, angka antara, dan angka pada kesalahan umum
from math import comb, perm, exp, factorial, sqrt
import numpy as np
from scipy import stats

def ppv(prev, sens, spes):
    """P(kondisi | positif) dengan Teorema Bayes."""
    return prev*sens / (prev*sens + (1 - prev)*(1 - spes))

# A2 — tanpa pengembalian; pengecoh dengan pengembalian, penyebut tidak dikurangi, pengambilan pertama saja
print("A2 =", round(3/8 * 2/7, 4), round((3/8)**2, 4), round(3/8 * 2/8, 4), 3/8)  # 0,1071 0,1406 0,0938 0,375
# A4 — PPV dasar, bila sensitivitas naik, bila spesifisitas naik
print("A4 =", round(ppv(.005, .95, .95), 4), round(ppv(.005, .995, .95), 4), round(ppv(.005, .95, .995), 4))  # 0,0872 0,0909 0,4884
# A6 — Binomial(150; 0,04): mean, varians, SD; pengecoh Bernoulli dan Var = mean
print("A6 =", 150*.04, round(150*.04*.96, 2), round(sqrt(150*.04*.96), 2), round(sqrt(.04*.96), 2), round(sqrt(6), 2))  # 6 5,76 2,4 0,2 2,45
# A9 — galat baku; pengecoh membagi n
print("A9 =", 2.4/sqrt(64), 2.4/64)  # 0,3 0,0375
# A12 — IK 99% dari IK 95% [52 ; 58]; pengecoh membagi rasio t
se = 3/2.01
print("A12 =", round(55 - 2.68*se, 2), round(55 + 2.68*se, 2), round(55 - 3*2.01/2.68, 2), round(55 + 3*2.01/2.68, 2))  # 51 59 52,75 57,25
# A14 — ANOVA: F, F tabel (2; 30), eta-kuadrat; pengecoh F terbalik dan SS_antar/SS_dalam
print("A14 =", (300/2)/(1200/30), round(stats.f.ppf(.95, 2, 30), 2), 300/1500, round((1200/30)/(300/2), 2), 300/1200)  # 3,75 3,32 0,2 0,27 0,25
# A15 — frekuensi harapan tabel 2 x 3 dan banyaknya sel < 5
O = np.array([[30, 12, 2], [6, 6, 4]])
E = O.sum(1, keepdims=True) * O.sum(0) / O.sum()
print("A15 =", E.round(1).tolist(), int((E < 5).sum()))  # [[26,4; 13,2; 4,4]; [9,6; 4,8; 1,6]] 3
# B1 — token 4 karakter berbeda dari 16; hanya angka; pengecoh 16^4 dan kombinasi
print("B1 =", perm(16, 4), round(perm(10, 4)/perm(16, 4), 4), 16**4, round(10**4/16**4, 4), comb(16, 4), round(comb(10, 4)/comb(16, 4), 4))  # 43680 0,1154 65536 0,1526 1820 0,1154
# B2 — irisan, gabungan, bersyarat arah lain; pengecoh bila diandaikan bebas
print("B2 =", round(.12*.5, 2), round(.18 + .12 - .06, 2), round(.06/.18, 4), round(.18*.12, 4), round(.18 + .12 - .0216, 4))  # 0,06 0,24 0,3333 0,0216 0,2784
# B3 — dua tingkat seri dengan replika paralel; tambahan replika; pengecoh semua seri
rw, rd = 1 - .05**2, 1 - .10**2
print("B3 =", round(rw*rd, 4), round((1 - .05**3)*rd, 4), round(rw*(1 - .10**3), 4), round(.95**2 * .90**2, 4))  # 0,9875 0,9899 0,9965 0,731
# B4 — hampiran Poisson lambda = 2, Binomial eksak, pengecoh P(X = 1)
print("B4 =", round(3*exp(-2), 4), round(stats.binom.cdf(1, 2500, .0008), 4), round(2*exp(-2), 4))  # 0,406 0,4059 0,2707
# B5 — aturan empiris (nilai eksak) dan ekor kanan z = 2,5
print("B5 =", round(stats.norm.cdf(60, 48, 6) - stats.norm.cdf(36, 48, 6), 4), (63 - 48)/6, round(stats.norm.sf(2.5), 4), round(stats.norm.cdf(2.5), 4))  # 0,9545 2,5 0,0062 0,9938
# B6 — Uniform(0, 800); pengecoh arah ekor dan persentil dari ekor yang salah
U = stats.uniform(0, 800)
print("B6 =", U.cdf(500) - U.cdf(300), round(U.sf(680), 2), U.mean(), U.ppf(.9), round(680/800, 2), U.ppf(.1))  # 0,25 0,15 400 720 0,85 80
# B7 — galat baku, z tabel 1,67, ukuran sampel separuh SE; pengecoh memakai sigma
print("B7 =", 18/sqrt(36), round(5/3, 2), round(1 - stats.norm.cdf(1.67), 4), 36*4, round(5/18, 2), round(1 - stats.norm.cdf(.28), 4))  # 3 1,67 0,0475 144 0,28 0,3897
# B8 — interval analis (z), interval-t df 15, t df 16
t15 = stats.t.ppf(.975, 15)
print("B8 =", round(6.5 - 1.96*.5, 2), round(6.5 + 1.96*.5, 2), round(t15, 3), round(t15*.5, 2),
      round(6.5 - t15*.5, 2), round(6.5 + t15*.5, 2), round(stats.t.ppf(.975, 16), 3))  # 5,52 7,48 2,131 1,07 5,43 7,57 2,12
# B9 — syarat, SE, margin, interval proporsi; dibandingkan dengan klaim 10%
p = 40/250; se_p = sqrt(p*(1 - p)/250)
print("B9 =", 250*p, 250*(1 - p), round(se_p, 4), round(1.96*se_p, 4), round(p - 1.96*se_p, 4), round(p + 1.96*se_p, 4), p - 1.96*se_p > .10)  # 40 210 0,0232 0,0454 0,1146 0,2054 True
# B10 — margin terbesar untuk n = 600; n untuk margin 3,5 poin persen; tambahan responden
n_b = round(1.96**2*.25/.035**2, 6)
print("B10 =", round(1.96*sqrt(.25/600), 4), n_b, int(n_b) - 600)  # 0,04 784 184
# C1 — probabilitas total, posterior, P(ditandai), PPV, NPV, kebijakan mitra + lain, pengecoh
pM = .70*.001 + .22*.005 + .08*.05
pT = pM*.95 + (1 - pM)*.02
npv = (1 - pM)*.98 / ((1 - pM)*.98 + pM*.05)
prev23 = (.22*.005 + .08*.05)/.30
print("C1 =", round(pM, 4), round(.004/pM, 4), round(pT, 6), round(ppv(pM, .95, .98), 4), round(npv, 4),
      round(prev23, 4), round(ppv(prev23, .95, .98), 4), round(.0007/pM, 4))  # 0,0058 0,6897 0,025394 0,217 0,9997 0,017 0,451 0,1207
print("C1 pengecoh =", round(ppv(.05, .95, .98), 4), round((.001 + .005 + .05)/3, 4))  # 0,7143 0,0187
# C2 — 8!, C(8,4), sesi sama (dua cara), X pertama atau Y terakhir, P(A ∩ B); pengecoh P(8,4)
print("C2 =", factorial(8), comb(8, 4), round(3/7, 4), round(2*comb(6, 2)/comb(8, 4), 4),
      round(1/8 + 1/8 - 1/56, 4), round(4/8 * 3/7, 4), perm(8, 4))  # 40320 70 0,4286 0,4286 0,2321 0,2143 1680
# C3 — Poisson(3): P(0), PMF 4–6, kumulatif 3–6, menit per jam melampaui kapasitas 4–6, P(X > 3)
X = stats.poisson(3)
print("C3(a,b) =", round(X.pmf(0), 4), [round(float(X.pmf(k)), 4) for k in (4, 5, 6)],
      [round(float(X.cdf(k)), 4) for k in (3, 4, 5, 6)], [round(60*float(X.sf(k)), 2) for k in (4, 5, 6)])  # 0,0498 [0,168; 0,1008; 0,0504] [0,6472; 0,8153; 0,9161; 0,9665] [11,08; 5,04; 2,01]
# penjumlahan nilai PMF yang sudah dibulatkan (cara manual) dan pengecoh "3 menit = 0,03"
print("C3 manual =", round(.6472 + .1680, 4), round(.6472 + .1680 + .1008, 4), round(.6472 + .1680 + .1008 + .0504, 4),
      min(k for k in range(20) if X.sf(k) <= .03))  # 0,8152 0,916 0,9664 7
# Eksponensial: rata-rata jeda, P(T <= 10) dengan tanpa memori, pengecoh tanpa syarat
print("C3(c,d) =", round(X.sf(3), 4), round(60*X.sf(3), 1), 60/3, round(1 - exp(-.05*10), 4),
      round(exp(-2) - exp(-2.5), 4), round(exp(-2), 4), round((exp(-2) - exp(-2.5))/exp(-2), 4))  # 0,3528 21,2 20 0,3935 0,0533 0,1353 0,3935
# C4 — x̄, Σ(x − x̄)², s, median; P(X > 480); persentil 90; rak 16 server; pengecoh
w = np.array([435, 390, 420, 465, 405, 420, 375, 450])
print("C4(a) =", w.mean(), ((w - w.mean())**2).sum(), w.std(ddof=1), np.median(w), round(w.std(ddof=0), 2))  # 420 6300 30 420 28,06
print("C4(b–d) =", round(stats.norm.sf(2), 4), round(200*stats.norm.sf(2), 1), round(420 + 1.28*30, 1),
      round(stats.norm.ppf(.9, 420, 30), 2), round((7000/16 - 420)/(30/4), 4), round(1 - stats.norm.cdf(2.33), 4),
      (16*480 - 16*420)/(30*4))  # 0,0228 4,6 458,4 458,45 2,3333 0,0099 8
print("C4 pengecoh =", round(60/28.06, 2), round(1 - stats.norm.cdf(2.14), 4), round(420 - 1.28*30, 1), round(280/480, 2))  # 2,14 0,0162 381,6 0,58
# C5 — sembilan UMKM: ringkasan, β1, β0, ŷ(15), R², ŷ(90); dengan titik viral; pengecoh β1 terbalik
x = np.array([3, 8, 10, 11, 12, 12, 15, 17, 20]); y = np.array([16, 19, 32, 35, 28, 34, 30, 41, 35])
r = np.corrcoef(x, y)[0, 1]; b1 = r*y.std(ddof=1)/x.std(ddof=1); b0 = y.mean() - b1*x.mean()
print("C5 =", x.mean(), x.std(ddof=1), y.mean(), y.std(ddof=1), round(r, 2), round(b1, 2), round(b0, 2),
      round(b0 + 15*b1, 2), round(r**2, 2), round(b0 + 90*b1, 2), y.max())  # 12 5 30 8 0,8 1,28 14,64 33,84 0,64 129,84 41
xj, yj = np.append(x, 30), np.append(y, 18)
print("C5 + viral =", round(np.corrcoef(xj, yj)[0, 1], 2), round(stats.spearmanr(xj, yj)[0], 2),
      "| pengecoh =", .8*5/8, 30 - .5*12, 24 + .5*15)  # 0,11 0,35 | pengecoh = 0,5 24 31,5
# D — ringkasan D1, Welch (keliru), uji-t berpasangan, t tabel df 35, IK 95%, Cohen's d; pengecoh
se_d = 48/sqrt(36); t = 31/se_d
print("D1 =", round(90/381, 3), round(30/36, 3), "| D2 Welch =", round(sqrt(95**2/36 + 90**2/36), 2), round(31/sqrt(95**2/36 + 90**2/36), 2))  # 0,236 0,833 | D2 Welch = 21,81 1,42
print("D5 =", se_d, t, [round(float(stats.t.ppf(1 - a, 35)), 3) for a in (.05, .025, .01, .005)], round(stats.t.sf(t, 35), 5))  # 8 3,875 [1,69; 2,03; 2,438; 2,724] 0,00022
print("D6 =", round(31 - 2.030*se_d, 2), round(31 + 2.030*se_d, 2), "| D7 =", round(31/48, 2),
      "| pengecoh D6 =", round(31 - 1.96*48, 2), round(31 + 1.96*48, 2))  # 14,76 47,24 | D7 = 0,65 | pengecoh D6 = -63,08 125,08
```

| Butir | Nilai kunci; angka antara dan angka kesalahan umum | Keluaran Python (baris `print`) |
|---|---|---|
| A2 | 0,1071; pengecoh 0,1406, 0,0938, 0,375 | 0,1071 / 0,1406 / 0,0938 / 0,375 |
| A4 | PPV 8,7% → 9,1% (sensitivitas) vs 48,8% (spesifisitas) | 0,0872 / 0,0909 / 0,4884 |
| A6 | 6 dan 2,40; pengecoh 5,76, 0,20, 2,45 | 6 / 5,76 / 2,4 / 0,2 / 2,45 |
| A9 | 0,30 detik; pengecoh 0,0375 | 0,3 / 0,0375 |
| A12 | [51,0 ; 59,0]; pengecoh [52,75 ; 57,25] | 51 / 59 / 52,75 / 57,25 |
| A14 | F = 3,75 > 3,32; η² = 0,20; pengecoh 0,27 dan 0,25 | 3,75 / 3,32 / 0,2 / 0,27 / 0,25 |
| A15 | E = 26,4; 13,2; 4,4; 9,6; 4,8; 1,6 — 3 sel < 5 | [[26,4; 13,2; 4,4]; [9,6; 4,8; 1,6]] / 3 |
| B1 | 43.680; 0,1154; kesalahan umum 65.536, 0,1526, 1.820, 0,1154 | 43680 / 0,1154 / 65536 / 0,1526 / 1820 / 0,1154 |
| B2 | 0,06; 0,24; 0,3333; kesalahan umum 0,0216 dan 0,2784 | 0,06 / 0,24 / 0,3333 / 0,0216 / 0,2784 |
| B3 | 0,9875; web 0,9899; basis data 0,9965; kesalahan umum 0,7310 | 0,9875 / 0,9899 / 0,9965 / 0,731 |
| B4 | 0,4060 (Binomial eksak 0,4059); kesalahan umum 0,2707 | 0,406 / 0,4059 / 0,2707 |
| B5 | ±95% (eksak 95,45%); z = 2,5; 0,0062; kesalahan umum 0,9938 | 0,9545 / 2,5 / 0,0062 / 0,9938 |
| B6 | 0,25; 0,15; 400 ms; 720 ms; kesalahan umum 0,85 dan 80 ms | 0,25 / 0,15 / 400 / 720 / 0,85 / 80 |
| B7 | 3 km; z = 1,67; 0,0475; 144; kesalahan umum z = 0,28 → 0,3897 | 3 / 1,67 / 0,0475 / 144 / 0,28 / 0,3897 |
| B8 | interval analis [5,52 ; 7,48]; t = 2,131; margin 1,07; [5,43 ; 7,57]; t df 16 = 2,120 | 5,52 / 7,48 / 2,131 / 1,07 / 5,43 / 7,57 / 2,12 |
| B9 | syarat 40 dan 210; SE 0,0232; margin 0,0454; [0,1146 ; 0,2054]; batas bawah > 0,10 | 40 / 210 / 0,0232 / 0,0454 / 0,1146 / 0,2054 / True |
| B10 | margin 0,0400; n = 784; tambahan 184 | 0,04 / 784 / 184 |
| C1 | 0,0058; 0,6897; P(T) 0,025394; PPV 0,2170; NPV 0,9997; prevalensi mitra + lain 0,0170; PPV 0,4510; tak terpindai 0,1207; kesalahan umum 0,7143 dan 1,87% | 0,0058 / 0,6897 / 0,025394 / 0,217 / 0,9997 / 0,017 / 0,451 / 0,1207; 0,7143 / 0,0187 |
| C2 | 40.320; 70; 0,4286 (dua cara); 0,2321; 0,2143; kesalahan umum 1.680 | 40320 / 70 / 0,4286 / 0,4286 / 0,2321 / 0,2143 / 1680 |
| C3 | 0,0498; P(4–6) 0,1680, 0,1008, 0,0504; kumulatif 0,6472–0,9665; menit per jam 11,08 / 5,04 / 2,01; penjumlahan nilai dibulatkan 0,8152 / 0,9160 / 0,9664; kesalahan umum c = 7; 0,3528 (±21 menit); 20 detik; 0,3935; kesalahan umum 0,0533 dan 0,1353 | 0,0498 / [0,168; 0,1008; 0,0504] / [0,6472; 0,8153; 0,9161; 0,9665] / [11,08; 5,04; 2,01]; 0,8152 / 0,916 / 0,9664 / 7; 0,3528 / 21,2 / 20 / 0,3935 / 0,0533 / 0,1353 / 0,3935 |
| C4 | 420; 6.300; 30; median 420; s penyebut n 28,06; 0,0228 (±4,6 dari 200 server); 458,4 (eksak 458,45); z = 2,33; 0,0099; 8 SD; kesalahan umum 2,14 → 0,0162, 381,6, 0,58 | 420 / 6300 / 30 / 420 / 28,06; 0,0228 / 4,6 / 458,4 / 458,45 / 2,3333 / 0,0099 / 8; 2,14 / 0,0162 / 381,6 / 0,58 |
| C5 | x̄ 12, s_x 5, ȳ 30, s_y 8, r 0,80; 1,28; 14,64; 33,84; R² 0,64; ŷ(90) 129,84; omzet tertinggi data 41; dengan titik viral r ±0,11, Spearman ±0,35; kesalahan umum 0,5 / 24 / 31,5 | 12 / 5 / 30 / 8 / 0,8 / 1,28 / 14,64 / 33,84 / 0,64 / 129,84 / 41; 0,11 / 0,35 / 0,5 / 24 / 31,5 |
| D1, D2, D5–D7 | KV 24%; 83%; Welch: SE 21,81, t 1,42; SE 8; t 3,875; t tabel df 35; p < 0,005; [14,76 ; 47,24]; d 0,65; kesalahan umum [−63,08 ; 125,08] | 0,236 / 0,833 / 21,81 / 1,42; 8 / 3,875 / [1,69; 2,03; 2,438; 2,724] / 0,00022; 14,76 / 47,24 / 0,65 / −63,08 / 125,08 |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
