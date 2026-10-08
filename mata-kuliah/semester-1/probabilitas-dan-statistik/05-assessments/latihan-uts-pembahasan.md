---
id: uai-if52510033-latihan-uts-pembahasan
tipe: asesmen
judul: "Latihan UTS — Probabilitas dan Statistik — Pembahasan dan Pedoman Skor"
kode_mk: IF52510033
nama_mk: Probabilitas dan Statistik
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-08
---

# Pembahasan dan Pedoman Skor — Latihan UTS Probabilitas dan Statistik

> **Latihan UTS — bukan naskah UTS.** Pembahasan ini menyertai simulasi lengkap UTS Probabilitas dan Statistik Ganjil 2026/2027 untuk berlatih: komposisi, durasi (100 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UTS. Naskah UTS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> **Kerjakan dulu [latihan UTS](latihan-uts.md) dalam 100 menit tanpa membuka berkas ini.** Sesudahnya, cocokkan jawaban per butir, beri skor sendiri dengan pedoman skor parsial, lalu pelajari bagian *Kesalahan umum*. Menghafal jawaban di sini tidak membantu: naskah UTS memakai konteks dan angka lain, jadi yang perlu dikuasai adalah **langkah dan alasannya**. Judul setiap butir mencantumkan Sub-CPMK registri · level Bloom · skor; cetak biru lengkap ada di [latihan-uts-cetak-biru.md](latihan-uts-cetak-biru.md). Sub-CPMK per butir ditandai menurut isi (bawaan sementara D-03(a)) untuk menghitung ketercapaian; bobot nilai akhir UTS tetap mengikuti RPS dan kisi-kisi (`PS-Sub-CPMK102-1`) — lihat [cetak biru, Identitas dan Dasar Penyusunan](latihan-uts-cetak-biru.md#identitas-dan-dasar-penyusunan).
>
> Mata kuliah IF52510033 · Semester Ganjil 2026/2027 · Penyusun: Tri Aji Nugroho, S.T., M.T.

---

## 0. Ketentuan Umum Penskoran

### 0.1 Aturan dari kisi-kisi UTS §6 (soal uraian); dalam latihan ini juga diterapkan pada Bagian B dan D (Petunjuk 6)

Sumber: [kisi-kisi UTS §6](kisi-kisi-uts.md#6-kriteria-penilaian-soal-uraian), yang berjudul *Kriteria Penilaian Soal Uraian*. Kisi-kisi tidak menyebut Bagian B (isian/hitungan pendek) dan D; penerapan aturan ini pada kedua bagian itu adalah tafsiran latihan ini (Petunjuk 6) dan termasuk hal yang menunggu penetapan dosen (KENDALI T0-18).

| Situasi | Perlakuan |
|---|---|
| Hanya angka akhir, tanpa langkah | Paling banyak **40%** skor butir |
| Langkah benar, salah hitung kecil di akhir | Paling sedikit **75%** skor butir |
| Rumus benar, tetapi asumsi tidak diperiksa padahal diminta | Kehilangan seluruh porsi aspek **asumsi** |
| Hitungan benar, tanpa kalimat interpretasi | Kehilangan seluruh porsi aspek **interpretasi** |
| Satuan tidak ditulis | −10% dari porsi aspek **ketepatan hitung** butir itu |

Bobot aspek untuk soal uraian (Bagian C): ketepatan prosedur **35%**, ketepatan hitung **25%**, kecocokan asumsi **20%**, validitas interpretasi **20%**. Setiap butir C di bawah dilengkapi peta langkah → aspek yang jumlahnya tepat 3,5 / 2,5 / 2 / 2 poin.

### 0.2 Ketentuan tambahan — usulan, menunggu penetapan dosen (KENDALI T0-18)

> Ketentuan di bawah **belum** tercantum di kisi-kisi UTS §6. Statusnya **usulan, menunggu penetapan dosen** ([KENDALI-EKSEKUSI](../../../00-meta/KENDALI-EKSEKUSI.md), butir T0-18). Di sini ketentuan ini dipakai agar Anda dapat menilai latihan sendiri secara konsisten; untuk UTS, yang berlaku adalah ketentuan yang ditetapkan dosen di kisi-kisi.

1. **Kesalahan berantai** (*error carried forward*): bila sebuah langkah memakai angka keliru dari langkah sebelumnya tetapi prosedurnya benar, langkah itu tetap mendapat skor penuh; kesalahan hanya dihukum sekali.
2. **Toleransi pembulatan:** probabilitas dari tabel Normal ±0,0005; hasil akhir lain ±1 pada digit terakhir yang diminta. Selisih karena memakai tabel versus nilai eksak tidak dihukum.
3. Skor diberikan dalam kelipatan **0,25**.
4. Jawaban dengan alasan berbeda tetapi sahih secara statistika diterima penuh — pembahasan ini memuat jawaban acuan, bukan satu-satunya jawaban.

### 0.3 Catatan umum

- Tabel-t dibagikan sesuai kisi-kisi, tetapi tidak ada butir yang memerlukannya (cakupan Minggu 1–7).
- **Batas kalimat.** Beberapa perintah uraian membatasi panjang jawaban (mis. "paling banyak 3 kalimat"; hitungan tidak termasuk) agar waktu cukup. Batas ini panduan waktu, bukan aturan penskoran: yang dinilai tetap unsur pada pedoman skor. Jawaban acuan di bawah kadang lebih panjang karena memuat penjelasan dan alternatif; untuk sub-butir yang dibatasi, *jawaban ringkas* menunjukkan jawaban berskor penuh yang muat dalam batas.
- Dua rumus "ekor" tidak ada di [daftar rumus kisi-kisi §7](kisi-kisi-uts.md#7-daftar-rumus-yang-harus-dihafal): Geometrik P(X > k) = (1 − p)ᵏ (dipakai di B6) dan Eksponensial P(T > t) = e^(−λt) (dipakai di D4). Keduanya dapat **diturunkan** dari rumus yang ada di daftar; pembahasan B6 dan D4 menunjukkan jalur penurunannya, dan jalur itu diterima penuh.

---

## 1. Bagian A — Pilihan Ganda (skor 20)

Skor penuh untuk jawaban benar, 0 untuk salah atau kosong; tidak ada pengurangan untuk jawaban salah.

**Ringkasan kunci**

| A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | A9 | A10 | A11 | A12 | A13 | A14 | A15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| b | a | d | c | c | a | c | b | d | a | b | d | a | c | d |

### A1 — Kunci (b) `[PS-Sub-CPMK102-1 · C3 · 1,5]`

`kota` nominal → modus sah; `level_member` ordinal → median sah; `saldo_rp` rasio (Rp0 = tidak ada saldo) → perbandingan "dua kali" sah. **Pengecoh:** (a) median `id_pengguna` tidak sah — ID adalah bilangan acak penanda identitas, jadi nominal walaupun bertipe bilangan bulat; (c) rata-rata data ordinal tidak sah, walaupun pernyataan rasio saldonya sah; (d) "tahun 2024 sekian kali tahun 2012" tidak sah karena tahun berskala interval (tahun 0 bukan "tidak ada waktu").

### A2 — Kunci (a) `[PS-Sub-CPMK102-1 · C3 · 1,5]`

Sampel kenyamanan: hanya pengguna yang sedang memakai Wi-Fi di satu lokasi dan satu rentang jam. Mahasiswa yang sudah berhenti memakai Wi-Fi (mungkin justru yang paling tidak puas) atau memakainya di lokasi dan jam lain tidak terwakili; memperbesar n dengan cara yang sama tidak menghapus bias. **Pengecoh:** (b) mitos "n besar pasti representatif"; (c) bukan sensus seluruh mahasiswa; (d) ringkasan apa pun mewarisi bias sampelnya.

### A3 — Kunci (d) `[PS-Sub-CPMK102-1 · C2 · 1]`

Ekor kanan panjang (beberapa panggilan > 30 menit) menarik mean ke atas → mean > median (menceng kanan); median lebih mewakili panggilan tipikal. **Pengecoh:** (a) arahnya terbalik; (b) mengabaikan ekor; (c) pada sebaran menceng kanan modus justru cenderung paling kecil — alasan "tidak terpengaruh ekor" benar, tetapi kesimpulannya keliru.

### A4 — Kunci (c) `[PS-Sub-CPMK102-1 · C2 · 1]`

Mean sama tidak berarti pengalaman sama. p95 menggambarkan pengalaman 5% pengguna paling lambat: lebih dari 6,5 detik di Y, lebih dari 1,8 detik di X — ekor Y jauh lebih panjang. **Pengecoh:** (a) hanya melihat mean; (b) ekor kanan panjang berarti sebagian pengguna sangat **lambat**, bukan sangat cepat; (d) modus tidak menjawab pertanyaan tentang ekor.

### A5 — Kunci (c) `[PS-Sub-CPMK102-1 · C2 · 1]`

Median dan IQR *robust* (tahan) terhadap satu nilai ekstrem: satu data baru hanya menggeser posisi median dan kuartil sedikit, dan besarnya nilai ekstrem itu tidak ikut dihitung. Mean, simpangan baku, dan *range* sensitif terhadap nilai ekstrem, sehingga opsi (a), (b), dan (d) masing-masing memuat sedikitnya satu ukuran yang berubah besar.

### A6 — Kunci (a) `[PS-Sub-CPMK102-1 · C3 · 1,5]`

Hitung koefisien variasi: CV P = 9.000/60.000 = **15%**; CV Q = 7.200/45.000 = **16%** → P relatif lebih stabil. Simpangan baku mentah menyesatkan di sini karena tingkat harga kedua pasar berbeda: fluktuasi Rp9.000 terjadi pada harga Rp60.000, sedangkan Rp7.200 pada harga Rp45.000 — relatif terhadap harganya, fluktuasi di Q lebih besar; CV adalah ukuran stabilitas harga yang lazim karena membagi simpangan baku dengan rata-ratanya. **Pengecoh:** (b) arah CV terbalik; (c) membandingkan simpangan baku mentah antara dua kelompok yang rata-ratanya berbeda, padahal stem meminta perbedaan tingkat harga diperhitungkan; (d) CV berbeda (15% ≠ 16%).

### A7 — Kunci (c) `[PS-Sub-CPMK102-1 · C3 · 1,5]`

Median = persentil 50 dan Q3 = persentil 75, jadi di antaranya terletak ±25% data → 0,25 × 360 = **±90 hari**. **Pengecoh:** (a) 11 = 58 − 47 adalah selisih **nilai** aduan, bukan banyaknya hari; (b) 18 = IQR, juga selisih nilai; (d) 180 hari adalah 50% data tengah, yaitu antara Q1 dan Q3.

### A8 — Kunci (b) `[PS-Sub-CPMK102-1 · C3 · 1,5]`

n = 40 (genap) → median = rata-rata data ke-20 dan ke-21. Frekuensi kumulatif: 18 SKS sampai data ke-6, 20 SKS sampai ke-20, 21 SKS sampai ke-32. Data ke-20 = 20 dan data ke-21 = 21 → median **20,5 SKS**; modus **20 SKS** (frekuensi terbesar, 14). **Pengecoh:** (c) 20,8 adalah mean (832/40); (a) mengambil data ke-20 saja; (d) mengambil kategori tengah dan nilai terbesar.

### A9 — Kunci (d) `[PS-Sub-CPMK102-1 · C3 · 1,5]`

Rata-rata gabungan berbobot: (30 × 3,20 + 20 × 3,45)/50 = (96 + 69)/50 = **3,30 MB**. **Pengecoh:** (c) 3,325 adalah rata-rata dua rata-rata tanpa bobot — keliru karena banyaknya berkas di kedua kelas berbeda.

### A10 — Kunci (a) `[PS-Sub-CPMK102-1 · C3 · 1,5]`

Pertanyaannya tentang **hubungan dua variabel kuantitatif** (pengguna serentak dan latensi) yang dibedakan menurut **kelompok** (pusat data) → diagram pencar dengan warna per kelompok. **Pengecoh:** (b) menunjukkan tren waktu, bukan hubungan dengan banyaknya pengguna; (c) rata-rata menghapus hubungan per titik; (d) hanya menunjukkan sebaran latensi.

### A11 — Kunci (b) `[PS-Sub-CPMK102-1 · C3 · 1,5]`

Teknik **pemotongan rentang data** ([Bab 3 §3.6.1(c)](../06-buku-ajar/bab-03-visualisasi-data-statistik.md#361-empat-teknik-menyesatkan-yang-paling-umum)): grafik hanya menampilkan Agustus–Desember, bagian yang naik (40 → 45 ribu, +12,5%), padahal sepanjang 2025 pengguna aktif turun dari 72 ribu menjadi 45 ribu, yaitu (72 − 45)/72 = **37,5%**. Judul "Terus Naik" memberi kesan tren yang berlawanan dengan data lengkap. Perbaikan: tampilkan seluruh rentang Januari–Desember, atau nyatakan dengan jelas bahwa grafik hanya memuat lima bulan terakhir dan ganti judulnya. **Pengecoh:** (a) sumbu dari nol dan angka yang benar hanya lolos satu cek kejujuran — rentang yang dipotong tetap menyesatkan; (c) grafik garis justru tepat untuk tren bulanan; (d) mencantumkan sumber tidak memulihkan bagian data yang dibuang.

### A12 — Kunci (d) `[PS-Sub-CPMK102-1 · C2 · 1]`

Bin yang terlalu lebar menutup struktur sebaran (dua puncak, ekor panjang), sehingga sebaran tampak lebih sederhana daripada kenyataannya. **Pengecoh:** (a) adalah risiko bin terlalu **sempit**; (b) luas tetap sebanding bila tinggi batang = frekuensi; (c) urutan bin tetap mengikuti sumbu numerik.

### A13 — Kunci (a) `[PS-Sub-CPMK102-1 · C3 · 1,5]`

IQR = 40 − 20 = 20; pagar atas = Q3 + 1,5 × IQR = 40 + 30 = **70 jam** < 95 → titik 95 pencilan. **Pengecoh:** (b) garis di dalam kotak adalah median, bukan mean; (c) 66 adalah ujung kumis, bukan Q3 — yang dilampaui 25% data adalah Q3 = 40; (d) median dekat Q1 berarti sebaran **menceng kanan**.

### A14 — Kunci (c) `[PS-Sub-CPMK102-1 · C2 · 1]`

Satuan, sumber, dan periode adalah unsur wajib grafik yang jujur. Tanpa ketiganya pembaca tidak dapat memeriksa skala, asal, dan rentang waktu data, sehingga klaim "tren" tidak dapat diverifikasi. **Pengecoh:** (a) grafik garis justru tepat untuk deret waktu; (b) bukan sekadar estetika; (d) diagram lingkaran tidak cocok untuk tren.

### A15 — Kunci (d) `[PS-Sub-CPMK102-1 · C3 · 1,5]`

Proporsi yang berdekatan (12–17%) sulit dibedakan dari sudut juring lingkaran, apalagi bila tiga dimensi dan dimiringkan. Diagram batang (mis. horizontal) yang **diurutkan**, dengan sumbu dari nol, memudahkan pengurutan. **Pengecoh:** (a) dan (b) diagram lingkaran; (c) histogram dipakai untuk data kuantitatif, bukan kategori.

---

## 2. Bagian B — Isian / Hitungan Pendek (skor 25)

### B1. Kode pos `[PS-Sub-CPMK102-1 · C3 · 2]`

**Jawaban.**

- **(a)** Skala **nominal**: kode pos adalah label wilayah; selisih dan urutan angkanya tidak bermakna. Tipe *integer* di basis data hanya cara penyimpanan, bukan skala pengukuran; "rata-rata" 18.577,2 bahkan tidak menunjuk wilayah mana pun.
- **(b)** Modus = **12110**, muncul 3 dari 5 data (**60%**). Juga sah: tabel frekuensi/proporsi (12110: 60%; 16424: 20%; 40132: 20%) atau banyaknya kategori berbeda (3).

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| Skala nominal | 0,5 |
| Alasan: label; tipe data ≠ skala | 0,5 |
| Memilih ringkasan sah (modus/proporsi/frekuensi) | 0,5 |
| Nilai benar (12110; 60% atau 3 dari 5) | 0,5 |

**Kesalahan umum.** Menjawab median atau mean sebagai "ringkasan sah" → 0 untuk dua langkah terakhir. Menyebut skala "rasio karena bertipe bilangan bulat" mencampur tipe data dengan skala pengukuran.

### B2. Waktu *boot* lima server `[PS-Sub-CPMK102-1 · C3 · 2]`

**Jawaban.** Data mencakup **seluruh** server → populasi → penyebut N.

1. μ = (30 + 34 + 31 + 37 + 33)/5 = 165/5 = 33 detik.
2. Simpangan: −3, 1, −2, 4, 0 → Σ(x − μ)² = 9 + 1 + 4 + 16 + 0 = 30.
3. σ² = 30/5 = **6 detik²**; σ = √6 = **2,45 detik**.

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| Alasan: data mencakup seluruh server (populasi) → penyebut N | 0,5 |
| μ = 33 dan Σ(x − μ)² = 30 | 0,5 |
| σ² = 6 detik² | 0,5 |
| σ = 2,45 detik (dengan satuan) | 0,5 |

**Kesalahan umum.** Memakai n − 1 pada populasi (s² = 7,5; s = 2,74) → 1 (langkah μ dan Σ(x − μ)², serta σ = √7,5 = 2,74 detik dengan kesalahan berantai §0.2 butir 1); yang hilang hanya langkah alasan penyebut dan σ² = 6. Penyebut n − 1 dipakai bila data adalah **sampel** dari populasi yang lebih besar — seperti di C1(a).

### B3. Paket kuis daring `[PS-Sub-CPMK081-1 · C3 · 3]`

**Jawaban.**

1. Soal logika: urutan tampil dibedakan → **permutasi** P(9,3) = 9 · 8 · 7 = **504**.
2. Soal statistika: satu halaman, urutan tidak dibedakan → **kombinasi** C(7,2) = (7 · 6)/2 = **21**.
3. Kedua pilihan dilakukan berturut-turut → aturan perkalian: 504 × 21 = **10.584 paket**.

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| Permutasi untuk soal logika, dengan alasan (urutan tampil dibedakan) | 0,5 |
| P(9,3) = 504 | 0,5 |
| Kombinasi untuk soal statistika, dengan alasan (urutan tidak dibedakan) | 0,5 |
| C(7,2) = 21 | 0,5 |
| Aturan perkalian (dikalikan, bukan dijumlahkan) | 0,5 |
| 10.584 | 0,5 |

Setiap hasil hitung dipisah dari langkah metodenya, sehingga satu salah hitung kecil di akhir hanya mengurangi 0,5 (skor 2,5 dari 3 = 83%, sesuai aturan "paling sedikit 75%" di §0.1).

**Kesalahan umum.** 1.764 (= C(9,3) · C(7,2), urutan soal logika diabaikan) → 2; 21.168 (= P(9,3) · P(7,2)) → 2; 525 (hasil dijumlahkan, bukan dikalikan) → 2. Skor 2 pada dua kasus pertama memakai ketentuan kesalahan berantai (§0.2 butir 1): baris hasil akhir (0,5) tetap diberikan karena 1.764 atau 21.168 adalah hasil kali yang benar dari angka mahasiswa; yang hilang hanya baris metode dan hasil P(9,3) atau C(7,2). Pada 525, yang hilang adalah baris aturan perkalian dan hasil akhir.

### B4. Keluaran model klasifikasi `[PS-Sub-CPMK081-1 · C3 · 3]`

**Jawaban.**

- **(a)** Semua nilai ≥ 0 (aksioma 1 terpenuhi). Kategori saling lepas dan lengkap, sehingga menurut aksioma 3 (aditivitas) P(S) = 0,42 + 0,25 + 0,21 + 0,15 = **1,03**, bertentangan dengan aksioma 2 (P(S) = 1). **Tidak sah.**
- **(b)** Lainnya = 1 − (0,42 + 0,25 + 0,21) = **0,12**.
- **(c)** P(bukan Banjir) = 1 − 0,42 = **0,58** (aturan komplemen). P(Sampah ∪ Jalan rusak) = 0,25 + 0,21 = **0,46** (saling lepas, irisan 0).

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| (a) Jumlah 1,03 | 0,5 |
| (a) Rujukan aksioma P(S) = 1 (dengan aditivitas) | 0,5 |
| (b) 1 − (0,42 + 0,25 + 0,21) | 0,5 |
| (b) 0,12 | 0,5 |
| (c) 0,58 | 0,5 |
| (c) 0,46 dengan alasan saling lepas | 0,5 |

**Kesalahan umum.** Menyatakan "sah karena semua nilai di antara 0 dan 1" — hanya memeriksa aksioma 1. Pada (b), membagi semua nilai dengan 1,03 (normalisasi), padahal soal menyatakan hanya nilai "Lainnya" yang keliru.

### B5. Seleksi beasiswa tiga tahap `[PS-Sub-CPMK081-1 · C3 · 4]`

**Jawaban.**

- **(a)** Aturan perkalian berantai: P(diterima) = P(B) · P(T | B) · P(W | T) = 0,6 × 0,5 × 0,8 = **0,24**.
- **(b)** Gugur di berkas ⊂ tidak diterima, sehingga P(gugur berkas ∩ tidak diterima) = P(gugur berkas) = 1 − 0,6 = 0,4. P(tidak diterima) = 1 − 0,24 = 0,76. P(gugur berkas | tidak diterima) = 0,4/0,76 = **0,5263**.

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| (a) Rumus perkalian berantai P(B) · P(T \| B) · P(W \| T) | 1 |
| (a) Substitusi 0,6 × 0,5 × 0,8 | 0,5 |
| (a) 0,24 | 0,5 |
| (b) P(tidak diterima) = 1 − 0,24 = 0,76 (komplemen) | 0,5 |
| (b) Irisan = P(gugur berkas) = 0,4, dengan alasan gugur berkas termasuk tidak diterima | 0,75 |
| (b) 0,5263 | 0,75 |

**Kesalahan umum.** Menjawab (b) = 0,4 (menukar P(A | B) dengan P(A)) → (b) paling banyak 0,5 (langkah komplemen saja). Mengalikan 0,4 × 0,76 sebagai "irisan" — kedua kejadian tidak saling bebas; justru yang satu termasuk di dalam yang lain.

### B6. Pengiriman data sensor `[PS-Sub-CPMK081-1 · C3 · 4]`

**Jawaban.**

- **(a)** X ~ **Geometrik(p = 0,7)**; E[X] = 1/p = 1/0,7 = **1,43 percobaan**.
- **(b)** P(X ≤ k) = 1 − 0,3ᵏ ≥ 0,99 ⇔ 0,3ᵏ ≤ 0,01. Coba: 0,3³ = 0,027 (belum memenuhi), 0,3⁴ = 0,0081 (memenuhi) → **k = 4** (P(X ≤ 4) = 0,9919). Cara logaritma: k ≥ ln 0,01/ln 0,3 = 3,82 → dibulatkan ke atas menjadi 4.
- **(c)** P(X > 2 + 3 | X > 2) = P(X > 3) = 0,3³ = **0,0270** (2,70%) — sifat **tanpa memori**: kegagalan sebelumnya tidak mengubah peluang ke depan.

**Jalur bila rumus ekor Geometrik tidak dihafal** (rumus P(X > k) tidak ada di daftar kisi-kisi §7, tetapi dapat diturunkan):

- "X > k" berarti **k percobaan pertama semuanya gagal**. Karena percobaan saling bebas, aturan perkalian memberi P(X > k) = 0,3 × 0,3 × … × 0,3 = 0,3ᵏ, sehingga P(X ≤ k) = 1 − 0,3ᵏ (aturan komplemen).
- Atau jumlahkan PMF P(X = k) = 0,3^(k−1) · 0,7 dari daftar rumus: P(X ≤ 3) = 0,7 + 0,21 + 0,063 = 0,973 (belum ≥ 0,99); P(X ≤ 4) = 0,973 + 0,0189 = 0,9919 → k = 4.
- Untuk (c), definisi probabilitas bersyarat: P(X > 5 | X > 2) = P(X > 5)/P(X > 2) = 0,3⁵/0,3² = 0,3³ = 0,0270.

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| (a) Geometrik dengan p = 0,7 | 0,5 |
| (a) E[X] = 1,43 | 0,5 |
| (b) P(X ≤ k) = 1 − 0,3ᵏ (CDF Geometrik, komplemen "k kali gagal", atau penjumlahan PMF) | 0,5 |
| (b) Ketaksamaan 0,3ᵏ ≤ 0,01 diselesaikan (coba-coba atau logaritma), atau penjumlahan PMF sampai ≥ 0,99 | 0,5 |
| (b) k = 4 | 0,5 |
| (c) Peluang bersyarat P(X > 5 \| X > 2) = P(X > 3) | 0,5 |
| (c) 0,0270 (0,027 diterima) | 0,5 |
| (c) Menyebut sifat tanpa memori | 0,5 |

**Kesalahan umum.** Menjawab k = 3 karena 0,973 "hampir" 0,99; pada (c) menghitung peluang **tepat** 3 percobaan tambahan, P(X = 3) = 0,3² × 0,7 = 0,063, padahal yang ditanya **lebih dari** 3; atau memakai P(X > 5) = 0,0024 tanpa syarat "sudah gagal dua kali".

### B7. Berat kemasan kopi `[PS-Sub-CPMK081-1 · C3 · 3]`

**Jawaban.**

- **(a)** z = (250 − 252)/4 = −0,50. P(Z < −0,50) = 1 − P(Z ≤ 0,50) = 1 − 0,6915 = **0,3085** → 30,85% kemasan di bawah label.
- **(b)** z₁ = (248 − 252)/4 = −1,00; z₂ = (258 − 252)/4 = 1,50. P = P(Z ≤ 1,50) − P(Z ≤ −1,00) = 0,9332 − (1 − 0,8413) = 0,9332 − 0,1587 = **0,7745** → 77,45%.

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| (a) z = −0,50 | 0,5 |
| (a) Pembacaan tabel + simetri | 0,5 |
| (a) 0,3085 / 30,85% | 0,5 |
| (b) z₁ = −1,00 dan z₂ = 1,50 | 0,5 |
| (b) Pembacaan tabel kedua nilai | 0,5 |
| (b) 0,7745 / 77,45% | 0,5 |

**Kesalahan umum.** Menjawab (a) 0,6915 (lupa simetri: tabel memberi P(Z ≤ 0,50), padahal yang dicari ekor kiri); pada (b) menjumlahkan kedua luas tabel atau lupa mengubah P(Z ≤ −1,00) menjadi 1 − 0,8413.

### B8. Batas garansi baterai `[PS-Sub-CPMK081-1 · C3 · 4]`

**Jawaban.**

- **(a)** P(X < T) = 0,03 → P(Z < z) = 0,03 (ekor kiri, z negatif). Tabel memuat z positif: cari luas 0,97 → P(Z ≤ 1,88) = 0,9699 (paling dekat; P(Z ≤ 1,89) = 0,9706) → z = −1,88. T = μ + zσ = 30 − 1,88 × 4 = **22,48 jam**. (Nilai eksak 22,48 jam, z = −1,8808.) Diterima T dalam rentang 22,44–22,48 jam.
- **(b)** 38 = μ + 2σ. Sekitar 95% data berada dalam μ ± 2σ, sehingga 5% di luar, terbagi rata di dua ekor → **≈ 2,5%** ponsel bertahan lebih dari 38 jam. (Nilai eksak 2,28%; tidak diminta.)

**Pedoman skor.**

| Langkah | Skor |
|---|---|
| (a) Arah benar: ekor kiri, z negatif (boleh ditunjukkan dengan sketsa; sketsa tidak wajib) | 0,5 |
| (a) Mencari 0,97 di tabel → z = −1,88 | 0,75 |
| (a) Rumus x = μ + zσ | 0,5 |
| (a) T = 22,48 jam (dengan satuan) | 0,75 |
| (b) 38 = μ + 2σ | 0,5 |
| (b) 95% dalam ±2σ | 0,5 |
| (b) Dibagi dua → 2,5% | 0,5 |

**Kesalahan umum.** Memakai z = +1,88 (T = 37,52 jam) → (a) paling banyak 1,25. Pada (b), menjawab 5% (lupa membagi dua ekor).

---

## 3. Bagian C — Uraian Terstruktur (skor 40)

### C1. Durasi Penanganan Tiket Gangguan `[PS-Sub-CPMK102-1 · C3–C4 · 10]`

#### Jawaban

**(a) (4 poin · C3).** Data terurut: 3, 4, 4, 5, 6, 6, 7, 8, 20 (n = 9).

| Ukuran | Perhitungan | Hasil |
|---|---|---|
| Mean | 63/9 | **7,00 jam** |
| Median | data ke-5 | **6 jam** |
| Σ(x − x̄)² | tercetak di soal (16 + 9 + 9 + 4 + 1 + 1 + 0 + 1 + 169) | 210 |
| Simpangan baku sampel | s² = 210/8 = 26,25 → s = √26,25 | **5,12 jam** |
| Q1 | posisi (9 − 1) · 0,25 + 1 = 3 → data ke-3 | **4 jam** |
| Q3 | posisi (9 − 1) · 0,75 + 1 = 7 → data ke-7 | **7 jam** |
| IQR | 7 − 4 | **3 jam** |
| Batas pencilan | 4 − 4,5 = −0,5 dan 7 + 4,5 = 11,5 | [−0,5 ; 11,5] |
| Pencilan | 20 > 11,5 | **20 jam** |

**(b) (2 poin · C4).** Klaim **tidak didukung**. Mean A ditarik ke atas oleh satu tiket 20 jam. Karena ada pencilan, ukuran yang tepat adalah median dan IQR: median A = 6 jam < median B = 7 jam, dan IQR A = 3 jam < IQR B = 4 jam — tiket tipikal di Gedung A lebih cepat dan 50% tengahnya lebih rapat. Sebaliknya s A = 5,12 jam jauh di atas s B = 2,55 jam, tetapi besarnya s A didominasi satu kasus ekstrem. Kesimpulan: kedua gedung tidak setara — A umumnya lebih cepat, tetapi memiliki kasus ekstrem yang perlu ditelusuri; B lebih lambat secara tipikal. Soal meminta memakai hasil (a) dan ringkasan B tanpa menghitung ukuran baru; perhitungan tambahan seperti mean A tanpa tiket 20 jam (5,38 jam) atau CV (73% vs 36%) boleh, tetapi **tidak disyaratkan**. (Catatan yang baik tetapi juga tidak disyaratkan: dengan n = 9 per gedung, kesimpulan ini masih sementara.)

*Jawaban ringkas (≤ 3 kalimat):* Mean A = 7 jam ditarik satu tiket 20 jam, jadi bandingkan median dan IQR: median A 6 < median B 7 jam dan IQR A 3 < IQR B 4 jam. Tiket tipikal di A lebih cepat dan lebih seragam, tetapi A memiliki satu kasus ekstrem yang perlu ditelusuri. Jadi klaim "setara" tidak didukung data.

**(c) (2 poin · C3).** Boxplot B sudah tercetak di lembar latihan; Anda hanya menggambar A (skala 3 karakter per jam).

```
Gedung A           ├──[=====|==]──┤                                   ●
Gedung B              ├──[=====|=====]──┤
          +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+--
          0     2     4     6     8     10    12    14    16    18    20    22   (jam)
```

- A: kotak 4–7, median 6, kumis 3 dan 8 (nilai data terjauh yang masih di dalam pagar −0,5 dan 11,5), titik pencilan di 20.
- B (tercetak): kotak 5–9, median 7, kumis 4 dan 10, tanpa pencilan (pagar B: −1 dan 15).

**(d) (2 poin · C4).** Boxplot B menyembunyikan **dua kelompok** (bimodalitas): empat tiket selesai 4–5 jam dan empat tiket 9–10 jam, sedangkan median 7 jam hanya diwakili **satu** tiket di luar kedua jenis itu (data B: 4, 4, 5, 5, 7, 9, 9, 10, 10 — satu-satunya himpunan bilangan bulat yang cocok dengan ringkasan). Lima angka ringkasan tidak memuat bentuk sebaran; median 7 jam tidak mewakili kedua jenis tiket. Usulan: *dot plot*/*strip plot* (n kecil, setiap tiket tampak) atau histogram yang **dipisah/diwarnai per jenis tiket**, atau boxplot terpisah per jenis — sehingga kinerja tiap jenis dapat dinilai sendiri.

*Jawaban ringkas (≤ 3 kalimat):* Boxplot B menyembunyikan dua kelompok tiket (4–5 jam dan 9–10 jam), sedangkan median 7 jam hanya diwakili satu tiket. Usul *dot plot* yang diwarnai per jenis tiket, karena n kecil sehingga setiap tiket dan kedua kelompok tampak.

#### Pedoman skor dan peta aspek

| Bagian | Langkah | Aspek | Skor |
|---|---|---|---|
| (a) | Mengurutkan; rumus mean, median | Prosedur | 0,5 |
| (a) | Mean 7 dan median 6 benar | Hitung | 0,5 |
| (a) | Rumus s dengan penyebut n − 1 (memakai Σ(x − x̄)² = 210 yang tercetak) | Prosedur | 0,5 |
| (a) | s = 5,12 jam | Hitung | 0,5 |
| (a) | Posisi kuartil dan rumus pagar | Prosedur | 0,5 |
| (a) | Q1, Q3, IQR, pagar, pencilan = 20 | Hitung | 1,5 |
| (b) | Memilih median/IQR karena ada pencilan; menyadari mean A tertarik pencilan | Asumsi | 1 |
| (b) | Kesimpulan "tidak setara" konsisten dengan angka: membedakan pengalaman tipikal (median/IQR) dari kasus ekstrem (tiket 20 jam), tanpa melampaui data | Interpretasi | 1 |
| (c) | Boxplot A: kotak 4–7 dan median 6 | Prosedur | 0,5 |
| (c) | Boxplot A: kumis 3 dan 8 — sampai nilai data terjauh di dalam pagar, bukan sampai pagar atau sampai 20 | Prosedur | 1 |
| (c) | Boxplot A: titik pencilan 20 digambar terpisah | Prosedur | 0,5 |
| (d) | Lima angka ringkasan tidak menangkap bimodalitas | Asumsi | 1 |
| (d) | Grafik usulan + alasan (pisah per jenis) | Interpretasi | 1 |
| | **Jumlah** — prosedur 3,5 · hitung 2,5 · asumsi 2 · interpretasi 2 | | **10** |

#### Kesalahan umum

- s dengan penyebut n (4,83 jam) → kehilangan 0,5 prosedur dan 0,5 hitung — data adalah **sampel** sembilan tiket.
- Kuartil dengan metode (n + 1)p (Q1 = 4; Q3 = 7,5; IQR = 3,5; pagar −1,25 dan 12,75) → −0,25 karena tidak mengikuti konvensi di Petunjuk 9; pencilan tetap 20.
- Kumis A ditarik sampai 20 → −0,5; sampai 11,5 (pagar) → −0,25.
- Pada (b), kesimpulan yang melampaui data (mis. "Gedung A pasti lebih baik") → interpretasi (b) paling banyak 0,5. Menyebut keterbatasan n = 9 tidak disyaratkan.

#### Contoh jawaban

| Tingkat | Contoh ringkas | Skor |
|---|---|---|
| Kurang | "Mean A = 7, s = 4,83 (dibagi 9). Mean B juga 7, jadi klaim benar, kinerja setara." Boxplot A kumis sampai 20. (d) "Boxplot sudah cukup karena sudah ada median." | 1,5–3 |
| Cukup | (a) benar kecuali Q3 = 7,5. (b) "CV A 73% > CV B 36%, jadi A kurang konsisten dan klaim salah" — tidak menyadari peran pencilan dan tidak membahas median. (c) benar. (d) "Pakai histogram," tanpa alasan. | 5–7 |
| Baik | Seluruh (a) benar. (b) membedakan pengalaman tipikal (median 6 vs 7; IQR 3 vs 4) dari ekor (satu tiket 20 jam) dan menyimpulkan tidak setara tanpa melampaui data. (c) lengkap. (d) "Ada dua kelompok 4–5 dan 9–10 jam; median 7 hanya diwakili satu tiket dan tidak mewakili keduanya; usul *dot plot* diwarnai per jenis tiket." | 9–10 |

### C2. Kegagalan Transaksi Marketplace `[PS-Sub-CPMK081-1 · C3–C4 · 10]`

#### Jawaban

**(a) (3,5 poin · C3).**

- P(gagal) = 96/1.200 = **0,0800**.
- P(gagal | COD) = P(gagal ∩ COD)/P(COD) = 36/216 = **0,1667** (laju kegagalan COD: di antara transaksi COD, 16,67% gagal).
- P(COD | gagal) = 36/96 = **0,3750** (porsi COD dalam kegagalan: di antara transaksi yang gagal, 37,5% berasal dari COD).
- P(COD ∪ gagal) = P(COD) + P(gagal) − P(COD ∩ gagal) = 216/1.200 + 96/1.200 − 36/1.200 = 276/1.200 = **0,2300**.

Pembedaan makna kedua probabilitas bersyarat (laju vs porsi) dinilai di (c).

**(b) (4 poin · C3).** Urutan tidak bermakna (yang ditelusuri adalah himpunan transaksi) → kombinasi: C(96,3) = (96 · 95 · 94)/3! = **142.880 himpunan**. Karena pemilihan acak tanpa pengembalian, setiap himpunan 3 transaksi berpeluang sama, sehingga peluang = banyak himpunan yang memenuhi / banyak seluruh himpunan. Himpunan dengan tepat 2 COD: pilih 2 dari 36 COD **dan** 1 dari 60 non-COD → aturan perkalian C(36,2) · C(60,1) = 630 × 60 = 37.800.
P(tepat 2 COD) = 37.800/142.880 = **0,2646**.
Cara lain: 3 × (36/96)(35/95)(60/94) = 0,2646 (aturan perkalian berurutan; faktor 3 = banyaknya posisi transaksi non-COD).

**(c) (2,5 poin · C4).** Keduanya benar sebagian karena menjawab pertanyaan berbeda. Manajer melihat **laju**: P(gagal | COD) = 16,67%, sekitar 2,7 kali laju QRIS (36/576 = 6,25%). Analis melihat **porsi**: P(COD | gagal) = 37,5%, jadi 62,5% kegagalan berasal dari non-COD; QRIS menyumbang 36 kegagalan — sama banyak dengan COD — karena volumenya besar. Menghapus COD paling banyak menghilangkan 36 dari 96 kegagalan (jika pembeli tidak berpindah metode) sambil kehilangan 180 transaksi berhasil. Data ini observasional satu minggu: tidak membuktikan COD *menyebabkan* kegagalan (bisa terkait jenis pembeli atau wilayah). Kesimpulan yang tidak melampaui data: "COD memiliki laju kegagalan tertinggi per transaksi, tetapi bukan sumber mayoritas kegagalan; penyebab kegagalan COD dan QRIS perlu ditelusuri sebelum memutuskan." Laju VA (24/408 = 5,88%) boleh disebut, tetapi tidak disyaratkan karena soal hanya meminta laju QRIS.

*Jawaban ringkas (≤ 3 kalimat):* Manajer melihat laju — P(gagal | COD) = 16,67%, sekitar 2,7 kali laju QRIS 6,25% — sedangkan analis melihat porsi: P(COD | gagal) = 37,5%, jadi 62,5% kegagalan berasal dari non-COD. Data observasional satu minggu ini tidak membuktikan COD menyebabkan kegagalan. Kesimpulan: COD memiliki laju gagal tertinggi tetapi bukan sumber mayoritas kegagalan, jadi penyebab kegagalan COD dan QRIS perlu ditelusuri sebelum menghapus metode apa pun.

#### Pedoman skor dan peta aspek

| Bagian | Langkah | Aspek | Skor |
|---|---|---|---|
| (a) | Memilih sel/marginal yang tepat; rumus bersyarat dua arah | Prosedur | 1,5 |
| (a) | Rumus penjumlahan umum dengan irisan dikurangi | Prosedur | 0,5 |
| (a) | 0,0800; 0,1667; 0,3750 | Hitung | 1 |
| (a) | 0,2300 | Hitung | 0,5 |
| (b) | Rumus C(n,r) untuk C(96,3) | Prosedur | 0,5 |
| (b) | Struktur C(36,2) · C(60,1)/C(96,3) atau 3 × hasil kali berurutan | Prosedur | 1 |
| (b) | Penjelasan aturan pencacahan (diminta): urutan tidak bermakna → kombinasi (0,5); tanpa pengembalian → setiap himpunan berpeluang sama (0,5); COD dan non-COD dipilih terpisah lalu dikalikan — aturan perkalian (0,5) | Asumsi | 1,5 |
| (b) | 142.880 dan 0,2646 | Hitung | 1 |
| (c) | Membedakan laju (COD 16,67% vs QRIS 6,25%) dan porsi (37,5%) dengan angka | Interpretasi | 1 |
| (c) | Kesimpulan terukur yang tidak melampaui data | Interpretasi | 1 |
| (c) | Data observasional — tidak membuktikan sebab | Asumsi | 0,5 |
| | **Jumlah** — prosedur 3,5 · hitung 2,5 · asumsi 2 · interpretasi 2 | | **10** |

#### Kesalahan umum

- P(gagal | COD) = 36/96 (arah persyaratan tertukar) → kehilangan 0,5 prosedur dan 0,5 hitung pada (a); interpretasi (c) dinilai dengan kesalahan berantai.
- P(COD ∪ gagal) = 312/1.200 (irisan tidak dikurangi) → kehilangan langkah rumus penjumlahan umum dan hitungnya.
- Peluang (b) dihitung **dengan** pengembalian, 3 × 0,375² × 0,625 = 0,2637 → struktur peluang 0,5 (bukan 1), penjelasan tanpa pengembalian dan aturan perkalian 0, hitung 0,2646 0; bagian C(96,3) tetap dinilai (paling banyak 2 dari 4).
- Memakai permutasi P(96,3) = 857.280 untuk himpunan — urutan tidak bermakna.

#### Contoh jawaban

| Tingkat | Contoh ringkas | Skor |
|---|---|---|
| Kurang | (a) "P(gagal \| COD) = 36/96 = 0,375 dan P(COD \| gagal) = 36/216 = 0,167"; P(COD ∪ gagal) = 312/1.200 (irisan tidak dikurangi). (b) P(96,3) = 857.280, peluang tidak dihitung. (c) "Manajer benar, COD paling banyak gagal." | 1,5–3,5 |
| Cukup | (a) benar; (b) C(96,3) benar tetapi peluang memakai pengembalian (0,2637); (c) "COD paling sering gagal per transaksi, tetapi QRIS juga banyak gagal," tanpa angka porsi dan tanpa catatan kausalitas. | 5,5–7 |
| Baik | Seluruh angka benar dengan langkah dan penjelasan pencacahan. (c) membedakan laju (16,67% vs 6,25%) dan porsi (37,5%), menghitung dampak maksimal penghapusan COD, dan menegaskan data observasional tidak membuktikan sebab. | 9–10 |

### C3. Detektor Teks-AI dan Prinsip *Tabayyun* `[PS-Sub-CPMK081-1 · C3–C4 · 10]`

#### Jawaban

**(a) (3 poin · C3).** Populasi = laporan yang diperiksa detektor (laporan yang penggunaan AI-nya sudah diungkapkan di AI Usage Log tidak diperiksa). Misalkan H = laporan ditulis AI tanpa diungkapkan; H′ = laporan ditulis sendiri; E = laporan ditandai.

- Prior: P(H) = 0,05; P(H′) = 0,95. **Asumsi prior:** proporsi 5% dari audit semester lalu diandaikan masih berlaku untuk laporan yang diperiksa semester ini (perilaku mahasiswa dan cara audit tidak berubah).
- *Likelihood*: P(E | H) = 0,90 (sensitivitas); P(E | H′) = 1 − 0,97 = 0,03.
- *Evidence* (probabilitas total): P(E) = 0,05 × 0,90 + 0,95 × 0,03 = 0,045 + 0,0285 = **0,0735**.
- Posterior: P(H | E) = 0,045/0,0735 = **0,6122**.

**(b) (2 poin · C3).**

| 2.000 laporan yang diperiksa | Ditandai | Tidak ditandai | Total |
|---|---|---|---|
| Ditulis AI tanpa diungkapkan (5%) | 90 | 10 | 100 |
| Ditulis sendiri (95%) | 57 | 1.843 | 1.900 |
| **Total** | **147** | **1.853** | **2.000** |

P(ditulis sendiri | tidak ditandai) = 1.843/1.853 = **0,9946**. Pemeriksaan silang: dari tabel yang sama, P(AI | ditandai) = 90/147 = 0,6122 — cocok dengan (a).

**(c) (2,5 poin · C3–C4).** Posterior (a) menjadi prior baru: 0,6122. Dengan P(E₂ | H) = 0,85 dan P(E₂ | H′) = 1 − 0,98 = 0,02:
P(H | E, E₂) = (0,6122 × 0,85)/(0,6122 × 0,85 + 0,3878 × 0,02) = 0,52037/(0,52037 + 0,00776) = 0,52037/0,52813 = **0,9853**.
Lewat frekuensi: 90 × 0,85 = 76,5 dan 57 × 0,02 = 1,14 → 76,5/77,64 = 0,9853.
Bila hasil antara dibulatkan ke 4 desimal (0,5204 dan 0,0078), diperoleh 0,5204/0,5282 = 0,9852. Selisih ini hanya akibat pembulatan antara: **0,9853 dan 0,9852 sama-sama diterima** (kisi-kisi §6, aspek ketepatan hitung: "pembulatan wajar").
Analisis asumsi (diminta): bebas bersyarat **kurang masuk akal** untuk dua detektor teks-AI, karena keduanya mungkin memakai ciri teks yang mirip (mis. kalimat yang sangat rapi atau kosakata baku), sehingga laporan jujur yang mengecoh detektor pertama cenderung juga mengecoh detektor kedua; kesalahannya berkorelasi dan 0,9853 terlalu optimistis. Asumsi lebih masuk akal bila kedua detektor dibangun dengan metode dan data latih yang berbeda. Tafsiran angka (a)–(c) dinilai di (d).

*Jawaban ringkas (analisis asumsi, ≤ 2 kalimat):* Kurang masuk akal: kedua detektor mungkin memakai ciri teks yang mirip, sehingga laporan jujur yang mengecoh detektor pertama cenderung juga mengecoh detektor kedua. Kesalahannya berkorelasi, jadi 0,9853 terlalu optimistis.

**(d) (2,5 poin · C4).** Usulan **ditolak**. Dari 147 laporan yang ditandai per 2.000 laporan, 57 (39%) ditulis sendiri — lebih dari sepertiga yang dihukum adalah mahasiswa jujur. Ini bertentangan dengan amanah dan keadilan, dan dengan prinsip *tabayyun*: tuduhan harus diperiksa kebenarannya lebih dulu. Bahkan setelah detektor kedua, posterior ±98,5% berarti kira-kira 1–2 dari 100 laporan yang ditandai kedua detektor masih ditulis sendiri (±1 laporan jujur per 2.000, yaitu 1,14); keluaran detektor adalah bukti awal, bukan putusan. Angka sensitivitas, spesifisitas, dan prior 5% berasal dari uji internal dan audit semester lalu, sehingga dapat berbeda pada laporan semester ini. Satu langkah prosedur yang cukup (soal meminta **satu**), mis.: klarifikasi dengan mahasiswa — AI Usage Log, riwayat draf, atau tanya jawab lisan — sebelum keputusan; atau pemeriksaan kedua yang independen; atau keputusan oleh dosen dengan hak jawab mahasiswa. Rangkaian lengkap (penyaring → pemeriksaan kedua → klarifikasi → keputusan dengan hak jawab) adalah jawaban baik, tetapi tidak disyaratkan.

*Jawaban ringkas (≤ 4 kalimat):* Tolak: dari 147 laporan yang ditandai per 2.000, 57 (39%) ditulis sendiri, dan setelah detektor kedua pun ±1–2 dari 100 laporan yang ditandai masih jujur. Angka sensitivitas, spesifisitas, dan prior 5% berasal dari uji internal dan audit semester lalu, sehingga bisa berbeda untuk laporan semester ini. Prinsip *tabayyun* menuntut tuduhan diperiksa dulu: keluaran detektor adalah bukti awal, bukan putusan. Usul: klarifikasi dengan mahasiswa (AI Usage Log, riwayat draf, atau tanya jawab lisan) sebelum keputusan.

#### Pedoman skor dan peta aspek

| Bagian | Langkah | Aspek | Skor |
|---|---|---|---|
| (a) | Notasi prior, *likelihood*, *evidence*; hukum probabilitas total; rumus Bayes | Prosedur | 1,5 |
| (a) | 0,0735 dan 0,6122 | Hitung | 1 |
| (a) | Menyebut asumsi prior (diminta): 5% dari audit semester lalu diandaikan berlaku untuk laporan yang diperiksa semester ini | Asumsi | 0,5 |
| (b) | Empat sel dan total pada kerangka tabel terisi lengkap dan konsisten (diagram pohon setara diterima) | Prosedur | 1 |
| (b) | Nilai sel dan total benar (90, 10, 57, 1.843; 147, 1.853) | Hitung | 0,5 |
| (b) | 0,9946 | Hitung | 0,5 |
| (c) | Posterior (a) sebagai prior baru (atau rumus gabungan) | Prosedur | 1 |
| (c) | 0,9853 (0,9852 dari pembulatan antara 4 desimal juga diterima) | Hitung | 0,5 |
| (c) | Analisis kewajaran asumsi bebas bersyarat (diminta) dengan alasan, mis. ciri teks serupa → kesalahan berkorelasi → posterior terlalu optimistis | Asumsi | 1 |
| (d) | Memakai angka (a)–(c) dengan tafsiran yang benar: 57 dari 147 (39%) laporan jujur; posterior ±98,5% / ±1 per 2.000 setelah detektor kedua | Interpretasi | 1 |
| (d) | Prinsip *tabayyun* dikaitkan dengan angka (bukti awal ≠ putusan) | Interpretasi | 0,5 |
| (d) | Satu langkah prosedur yang lebih adil, dengan alasan | Interpretasi | 0,5 |
| (d) | Keterbatasan angka uji internal dan audit (diminta) | Asumsi | 0,5 |
| | **Jumlah** — prosedur 3,5 · hitung 2,5 · asumsi 2 · interpretasi 2 | | **10** |

Seluruh poin asumsi dan interpretasi C3 terkait perintah yang tertulis di soal: (a) asumsi prior, (c) analisis asumsi bebas bersyarat, (d) angka (a)–(c), keterbatasan angka uji, *tabayyun*, dan satu langkah prosedur. Sub-butir (c) memuat hitung posterior berantai (C3, 1,5 poin) dan analisis asumsi (C4, 1 poin), sehingga bertanda C3–C4.

#### Kesalahan umum

- *Base rate fallacy*: "P(AI | ditandai) = 90% karena sensitivitasnya 90%" — menukar P(E | H) dengan P(H | E) dan mengabaikan prior 5%.
- Menjawab (c) dengan 0,90 × 0,85 = 0,765 → prosedur (c) 0 dan hitung (c) 0; asumsi (c) tetap dinilai; di (d) angka 0,765 dinilai dengan kesalahan berantai.
- Pada (d), hanya menulis "detektor bisa salah" tanpa angka dari (a)–(c) dan tanpa keterbatasan angka uji.

#### Contoh jawaban

| Tingkat | Contoh ringkas | Skor |
|---|---|---|
| Kurang | "P(AI \| ditandai) = 90% karena sensitivitasnya 90%." Tabel tidak lengkap. (c) "0,90 × 0,85 = 0,765." (d) "Setuju, detektor sudah akurat 90%." | 0,5–3 |
| Cukup | (a) angka benar tetapi asumsi prior yang diminta tidak disebut; (b) benar; (c) 0,9853 benar, tetapi asumsi bebas bersyarat yang diminta tidak dianalisis; (d) "Tidak setuju karena detektor bisa salah; sebaiknya mahasiswa ditanya dulu," tanpa angka dan tanpa keterbatasan angka uji. | 5,5–7 |
| Baik | Seluruh angka benar dengan notasi. (c) menyebut bahwa kedua detektor mungkin memakai ciri yang sama sehingga 0,9853 terlalu optimistis. (d) "57 dari 147 laporan yang ditandai (39%) ditulis sendiri; bahkan setelah detektor kedua masih ±1–2 dari 100 yang ditandai itu jujur, dan angka uji berasal dari uji internal semester lalu. Menghukum langsung melanggar *tabayyun*. Usul: klarifikasi lisan dan AI Usage Log sebelum keputusan." | 9–10 |

### C4. Server Replika LMS `[PS-Sub-CPMK081-1 · C3–C4 · 10]`

#### Jawaban

**(a) (3 poin · C4).** P(S1 mati) = 25/500 = 0,05; P(S2 mati) = 20/500 = 0,04; P(S1 ∩ S2 mati) = 9/500 = 0,018. Bila saling bebas, P(S1 ∩ S2) = 0,05 × 0,04 = 0,002. Karena 0,018 ≠ 0,002 (sembilan kali lipat), kedua kejadian **tidak saling bebas**; setara dengan P(S1 mati | S2 mati) = 9/20 = 0,45 ≫ P(S1 mati) = 0,05. Keduanya juga **tidak saling lepas**, karena P(S1 ∩ S2) = 0,018 > 0 (pernah mati bersamaan). Tafsiran: ada penyebab bersama — catu daya, jaringan, rak, atau pembaruan serentak — yang perlu ditelusuri; replika yang mati bersamaan tidak memberi perlindungan yang diharapkan.

*Jawaban ringkas (tafsiran, ≤ 2 kalimat):* Ada penyebab bersama (mis. catu daya, jaringan, atau rak yang sama) yang membuat kedua server cenderung mati bersamaan. Akibatnya replika tidak memberi perlindungan sebesar yang diharapkan, sehingga penyebab bersama itu perlu ditelusuri.

**(b) (2 poin · C3).** Struktur gabungan: *load balancer* **seri** dengan kelompok tiga server aplikasi (replika penuh) yang tersusun **paralel**.

- Kelompok replika (paralel): R_rep = 1 − (1 − 0,96)³ = 1 − 0,04³ = 1 − 0,000064 = 0,999936.
- Layanan (seri dengan *load balancer*): R = 0,99 × 0,999936 = **0,9899** (0,98993664).
- Nilai batas: bila banyaknya replika n terus ditambah, 0,04ⁿ → 0 sehingga R_rep → 1 dan R → **0,99**. Keandalan layanan tidak pernah melampaui keandalan *load balancer*, yang menjadi titik kegagalan tunggal (*single point of failure*). (Dengan n = 4, R = 0,989997 — replika keempat hanya menambah ±0,00006; perbaikan yang berarti adalah *load balancer* cadangan.)

**(c) (3 poin · C3).** BINS: **B**iner (hidup/mati) ✓; **I**ndependen — diandaikan sesuai (b) (lihat (a)); **N** tetap = 4 ✓; **S**ama, p = 0,96 untuk tiap server — diandaikan sesuai (b). X = banyaknya server klaster yang hidup, X ~ Binomial(4; 0,96). Kuorum mayoritas 4 server = sedikitnya 3 hidup:
P(X ≥ 3) = C(4,3)(0,96)³(0,04) + C(4,4)(0,96)⁴ = 0,141558 + 0,849347 = **0,9909** (0,99090432).
E[X] = np = 4 × 0,96 = **3,84 server**.
Catatan: menambahkan bahwa data (a) menunjukkan peluang hidup S1 (0,95) dan S2 (0,96) sedikit berbeda, sehingga syarat S pun hanya pendekatan, menunjukkan pemahaman baik — tidak wajib dan tidak mengurangi skor.

**(d) (2 poin · C4).** Pertanyaan dibatasi pada temuan **uji kebebasan** (a), jadi jawaban acuannya syarat **I (independen)** yang tidak terpenuhi: kegagalan berkelompok (S1 dan S2 mati bersamaan 9 kali lebih sering daripada bila bebas). Bila kegagalan berkorelasi positif, peluang dua server atau lebih mati bersamaan lebih besar daripada hitungan Binomial, sehingga keandalan kuorum yang sebenarnya **lebih rendah** dari 0,9909 — angka (c) **terlalu optimistis** (demikian pula angka kelompok replika di (b)). Contoh pemeriksaan (tidak diminta): dengan gangguan bersama berpeluang 0,01 yang mematikan keempat server sekaligus dan peluang hidup tiap server tetap 0,96, keandalan kuorum turun menjadi ±0,9848. Saran: pisahkan catu daya/zona server dan hitung ulang keandalan dari log.

*Jawaban ringkas (≤ 3 kalimat):* Syarat I (independen) tidak terpenuhi: S1 dan S2 mati bersamaan sembilan kali lebih sering daripada bila bebas. Kegagalan yang berkelompok membuat peluang dua server atau lebih mati bersamaan lebih besar daripada hitungan Binomial. Jadi keandalan kuorum sebenarnya lebih rendah dari 0,9909 — angka (c) terlalu optimistis.

Perlakuan jawaban syarat S (agar penilaian seragam). Data (a) juga menunjukkan peluang mati yang berbeda, 0,05 dan 0,04 (peluang hidup 0,95 vs 0,96), sehingga syarat **S** pun secara fakta tidak terpenuhi.

- **I** saja, atau **I dan S** → skor penuh untuk langkah asumsi (S sebagai temuan tambahan yang sah).
- **S saja** (dengan alasan 0,95 vs 0,96) → asumsi **0,25 dari 1**: faktanya benar, tetapi tidak menjawab temuan uji kebebasan yang ditanyakan. Interpretasi dinilai menurut alasannya: arah "terlalu optimistis" dengan alasan bahwa peluang hidup S1 lebih kecil dari 0,96 sahih (dengan p = 0,95/0,96/0,96/0,96 keandalan kuorum 0,9898 < 0,9909) → interpretasi **paling banyak 0,5 dari 1**.

#### Pedoman skor dan peta aspek

| Bagian | Langkah | Aspek | Skor |
|---|---|---|---|
| (a) | Membandingkan P(S1 ∩ S2) dengan P(S1) · P(S2) (atau P(S1 \| S2) dengan P(S1)) | Prosedur | 1 |
| (a) | 0,05; 0,04; 0,018 vs 0,002 | Hitung | 1 |
| (a) | Tidak bebas, tidak saling lepas, penyebab bersama | Interpretasi | 1 |
| (b) | Struktur seri–paralel: kelompok replika 1 − (1 − r)³, lalu dikalikan keandalan *load balancer* | Prosedur | 1 |
| (b) | 0,9899 (0,5) dan batas 0,99 karena 0,04ⁿ → 0 (0,5) | Hitung | 1 |
| (c) | Kejadian kuorum = X ≥ 3 dengan X ~ Binomial(4; 0,96); rumus Binomial untuk k = 3 dan k = 4; E[X] = np | Prosedur | 1,5 |
| (c) | Pemeriksaan BINS satu per satu | Asumsi | 1 |
| (c) | 0,9909 dan 3,84 | Hitung | 0,5 |
| (d) | Menunjuk syarat I yang tidak terpenuhi (lihat perlakuan jawaban S di atas) | Asumsi | 1 |
| (d) | Terlalu optimistis + alasan arah | Interpretasi | 1 |
| | **Jumlah** — prosedur 3,5 · hitung 2,5 · asumsi 2 · interpretasi 2 | | **10** |

#### Kesalahan umum

- "S1 dan S2 saling lepas karena servernya berbeda" — saling lepas berarti **tidak pernah** terjadi bersamaan; di sini terjadi 9 kali.
- Menghitung kelompok replika secara seri (0,99 × 0,96³ = 0,8759) — replika penuh tersusun paralel.
- Kejadian kuorum ditulis X ≥ 2 (salah membaca "3 dari 4"; P = 0,9998) → prosedur (c) paling banyak 0,75, hitung (c) 0,25 (E[X] saja); X = 3 saja (0,1416) → prosedur (c) 0,75.

#### Contoh jawaban

| Tingkat | Contoh ringkas | Skor |
|---|---|---|
| Kurang | "S1 dan S2 saling lepas karena servernya berbeda, jadi juga bebas." (b) replika dihitung seri: 0,99 × 0,96³ = 0,8759, dan "batas 100% bila replika cukup banyak". (c) hanya 4 × 0,96³ × 0,04 = 0,1416. (d) "Terlalu pesimistis." | 0,5–3 |
| Cukup | (a) menghitung 0,018 vs 0,002 dan menyimpulkan tidak bebas, tetapi tidak membahas saling lepas atau penyebab bersama. (b) benar. (c) 0,9909 benar tanpa memeriksa BINS. (d) "Syarat I tidak terpenuhi," tanpa arah dampak. | 5–7 |
| Baik | Seluruh angka benar. (a) menyatakan tidak bebas dan tidak saling lepas, dengan contoh penyebab bersama. (c) memeriksa BINS dan menandai I serta S sebagai asumsi. (d) menjelaskan bahwa kegagalan berkelompok menaikkan P(≥ 2 mati) sehingga 0,9909 terlalu optimistis, lalu memberi saran. | 9–10 |

---

## 4. Bagian D — Studi Kasus Terpadu: Sistem Antrean Daring Rawat Jalan (skor 15)

Butir utuh: `[PS-Sub-CPMK102-1: D1, D2, D6 · PS-Sub-CPMK081-1: D3, D4, D5 · C4 · 15]`. Peta sub-butir ke [kisi-kisi §5](kisi-kisi-uts.md#5-bentuk-soal-studi-kasus-terpadu-bagian-d): D1 = butir 1 (2%), D2 = butir 2 (3%), D3 = butir 3 (3%), D4 = butir 4 (3%), D5 = butir 5 (3%), D6 = butir 6 (1%).

### D1. Skala variabel `[PS-Sub-CPMK102-1 · C3 · 2]`

**Jawaban.** `waktu_tunggu_menit` **rasio** (0 menit = tidak menunggu; "dua kali lebih lama" bermakna). `rating_kepuasan` **ordinal** (urutan bermakna, jarak antarbintang tidak dijamin sama). `jam_daftar` **interval** (selisih bermakna, mis. 07.10 − 06.45 = 25 menit, tetapi pukul 00.00 bukan "tanpa waktu", sehingga "pukul 14.00 dua kali pukul 07.00" tidak bermakna). Pemusatan yang sah untuk rating: **median** (atau modus), bukan mean.

**Pedoman skor.** 0,5 per skala benar (× 3) + 0,5 ukuran pemusatan sah. `jam_daftar` "rasio" dengan alasan "durasi sejak tengah malam" → 0,25.

**Kesalahan umum.** Menyebut `rating_kepuasan` "interval" lalu memilih mean sebagai ukuran pemusatannya → kehilangan 0,5 skala dan 0,5 ukuran pemusatan; jarak antarbintang tidak dijamin sama. Menyebut `jam_daftar` "rasio" karena berupa angka jam — pukul 00.00 bukan "tidak ada waktu", jadi perbandingan "dua kali" tidak bermakna. Menyebut `waktu_tunggu_menit` "interval" karena ada nilai 0 — justru 0 menit berarti benar-benar tidak menunggu, ciri skala rasio.

### D2. Ukuran waktu tunggu dan usulan membuang pencilan `[PS-Sub-CPMK102-1 · C4 · 3]`

**Jawaban.** Sebaran **menceng kanan**: mean 47 > median 31; Q3 − median = 21 > median − Q1 = 13; ekor sampai 260 menit. Laporkan **median 31 menit** (pengalaman tipikal) bersama **p95 140 menit** (atau IQR 18–52 menit) untuk pengalaman terburuk. Batas atas pencilan = 52 + 1,5 × (52 − 18) = 52 + 51 = **103 menit**. Usulan staf **ditolak**: p95 = 140 > 103, jadi sedikitnya ±5% (±70 pasien) berada di atas pagar — bukan salah catat, melainkan pengalaman nyata pasien (kemungkinan jam sibuk). Membuangnya menyembunyikan masalah; telusuri penyebabnya.

*Jawaban ringkas (≤ 3 kalimat di luar hitungan):* Sebaran menceng kanan (mean 47 > median 31; ekor sampai 260 menit), jadi laporkan median 31 menit untuk pengalaman tipikal dan p95 140 menit untuk pengalaman terburuk. Hitungan: pagar atas = 52 + 1,5 × (52 − 18) = 103 menit. Usulan ditolak: p95 = 140 > 103, jadi sedikitnya 5% (±70) pasien berada di atas pagar — itu pengalaman nyata, bukan salah catat, sehingga penyebabnya ditelusuri, bukan datanya dibuang.

**Pedoman skor.** Bentuk sebaran dengan bukti 0,75 · ukuran yang dilaporkan + alasan 0,75 · batas 103 menit 0,75 · analisis usulan dengan angka p95 0,75.

**Kesalahan umum.**

- Hanya melaporkan mean 47 menit — pada sebaran menceng kanan mean ditarik ekor dan melebihi pengalaman tipikal (median 31 menit).
- Menghitung pagar dari median, bukan dari Q3: 31 + 1,5 × 34 = 82 menit → batas keliru (langkah batas 0).
- Menyetujui pembuangan data "karena pencilan" tanpa membandingkan p95 = 140 menit dengan pagar 103 menit. Pencilan tidak boleh dibuang tanpa alasan substantif (kisi-kisi §4.2); di sini sedikitnya 5% pasien berada di atas pagar, jadi itu pengalaman nyata, bukan salah catat → analisis usulan 0.

### D3. Distribusi galat per jam `[PS-Sub-CPMK081-1 · C4 · 3]`

**Jawaban.** **Poisson** — cacah kejadian dalam selang waktu tetap; parameter λ = laju galat per jam (≈ 1,77 untuk seluruh jam). Asumsi (dua di antaranya): kejadian saling bebas; laju konstan sepanjang waktu; tidak ada dua galat tepat bersamaan dalam selang sangat kecil. Pemeriksaan:

1. **Laju konstan** — mean jam sibuk 3,62 lebih dari dua kali mean jam lain 1,51, jadi laju **tidak konstan** sepanjang hari. Inilah bukti penentu.
2. **Rasio varians/mean** — seluruh jam 2,21/1,77 = **1,25**, sedikit di atas 1 (overdispersi ringan, cocok dengan campuran dua laju), tetapi tepat di batas atas rentang heuristik 0,8–1,25 pada Bab 6 dan modul Minggu 6, sehingga rasio gabungan saja **belum menentukan**. Per periode varians ≈ mean (3,25/3,62 = 0,90; 1,53/1,51 = 1,01) → di dalam tiap periode Poisson layak.

Keputusan: dua model Poisson terpisah, **λ ≈ 3,6/jam** (07.00–10.00) dan **λ ≈ 1,5/jam** (jam lain).

*Jawaban ringkas (≤ 4 kalimat di luar hitungan):* Poisson dengan λ = laju galat per jam (≈ 1,77 untuk seluruh jam), dengan asumsi galat saling bebas dan lajunya konstan. Laju tidak konstan: mean jam sibuk 3,62 lebih dari dua kali mean jam lain 1,51, sedangkan rasio gabungan 2,21/1,77 = 1,25 di batas rentang 0,8–1,25 belum menentukan. Di dalam tiap periode varians ≈ mean (rasio 0,90 dan 1,01). Keputusan: dua model Poisson terpisah, λ ≈ 3,6/jam untuk 07.00–10.00 dan λ ≈ 1,5/jam untuk jam lain.

**Pedoman skor.** Distribusi + parameter 0,75 · dua asumsi 0,75 · pemeriksaan dengan tabel (perbedaan mean antarperiode dan rasio varians/mean per periode) 0,75 · keputusan per periode 0,75. Rasio gabungan 1,25 boleh ditafsirkan "sedikit di atas 1" atau "masih di batas rentang 0,8–1,25" — keduanya benar bila dihitung tepat.

**Kesalahan umum.** Satu model Poisson λ = 1,77 yang hanya beralasan rasio gabungan ≤ 1,25, tanpa membahas perbedaan mean antarperiode → keputusan paling banyak 0,25.

### D4. Waktu antargalat `[PS-Sub-CPMK081-1 · C3 · 3]`

**Jawaban.**

- **(i)** 1/λ = 1/1,5 jam = 0,667 jam = **40 menit**.
- **(ii)** T ~ Eksponensial(λ = 1,5/jam), t = 45 menit = 0,75 jam: P(T > 0,75) = e^(−1,5 × 0,75) = e^(−1,125) = **0,3247**.
- **(iii)** Banyaknya galat dalam 45 menit N ~ Poisson(λt = 1,125), dan P(N = 0) = e^(−λt) adalah ekspresi yang sama dengan (ii), karena "waktu sampai galat berikutnya lebih dari 45 menit" setara dengan "tidak ada galat dalam 45 menit". Menghitung ulang 0,3247 boleh, tetapi tidak disyaratkan.

**Jalur bila rumus ekor Eksponensial tidak dihafal** (daftar kisi-kisi §7 hanya memuat E[X] = 1/λ untuk Eksponensial): pakai rumus Poisson dari daftar. Kejadian "T > 0,75 jam" sama dengan "tidak ada galat dalam 0,75 jam", dan N ~ Poisson(1,5 × 0,75 = 1,125), sehingga P(N = 0) = e^(−1,125) · 1,125⁰/0! = e^(−1,125) = 0,3247. Jalur ini diterima penuh untuk (ii).

**Pedoman skor.** (i) 1 · (ii) 1 (konversi menit → jam wajib; tanpa konversi, e^(−67,5) ≈ 0 → 0,25) · (iii) 0,5 menyebut N ~ Poisson(λt = 1,125) atau P(N = 0) = e^(−λt) + 0,5 alasan kesetaraan kejadian.

**Kesalahan umum.** Memakai λ = 1,77 (laju gabungan) padahal soal menetapkan 1,5 untuk jam di luar 07.00–10.00 → e^(−1,77 × 0,75) = e^(−1,3275) = 0,2651.

### D5. Galat 504 `[PS-Sub-CPMK081-1 · C3 · 3]`

**Jawaban.** P(504) = 0,7 × 0,8 + 0,3 × 0,1 = 0,56 + 0,03 = **0,59**. P(jaringan | 504) = 0,56/0,59 = **0,9492**. Keputusan: hubungi **tim jaringan** lebih dulu (≈ 95%). Probabilitas pilihan itu keliru = P(*bug* | 504) = 0,03/0,59 = 1 − 0,9492 = **0,0508** — sekitar 1 dari 20 galat 504 sebenarnya bersumber dari *bug*, sehingga tim aplikasi tetap perlu dilibatkan bila jaringan terbukti normal.

**Pedoman skor.** P(504) dengan probabilitas total 0,75 · P(jaringan | 504) 0,75 · keputusan dengan angka 0,75 · probabilitas keliru 0,0508 (komplemen atau Bayes) 0,75.

**Kesalahan umum.** Menjawab "P(jaringan) = 0,8" — itu P(504 | jaringan), bukan P(jaringan | 504).

### D6. Batas inferensi `[PS-Sub-CPMK102-1 · C4 · 1]`

**Jawaban.** Salah satu, dengan alasan:

1. Rating hanya dari 252 pasien (18%) yang mengisi sukarela dan sudah dilayani → tidak dapat disimpulkan kepuasan **seluruh** pasien (bias seleksi; pasien yang batal tidak tercatat).
2. Data satu minggu dari satu rumah sakit → tidak dapat digeneralisasi ke minggu lain atau rumah sakit lain.
3. Tidak dapat disimpulkan bahwa galat sistem **menyebabkan** waktu tunggu panjang (data observasional; keduanya bisa sama-sama dipicu jam sibuk).
4. Komposisi 70/30 sumber galat berasal dari catatan tim, bukan diukur dari log ini.

**Pedoman skor.** Pernyataan sahih 0,5 · alasan yang merujuk cara data diperoleh 0,5. Menuliskan hal yang justru **dapat** disimpulkan → 0.

**Kesalahan umum.** Menuliskan kesimpulan yang justru **dapat** ditarik dari data, mis. "median waktu tunggu minggu itu 31 menit" atau "laju galat jam sibuk lebih tinggi daripada jam lain" → 0. Menulis "datanya kurang" tanpa menyebut kesimpulan apa yang tidak dapat ditarik dan tanpa merujuk cara data diperoleh (sukarela, satu minggu, satu rumah sakit, observasional) → 0. Pernyataan sahih tanpa alasan, mis. "tidak bisa digeneralisasi" → 0,5.

### Contoh jawaban Bagian D

| Tingkat | Contoh ringkas | Skor |
|---|---|---|
| Kurang | D1: rating "interval", dilaporkan mean. D2: "Laporkan mean 47 menit; usul staf baik supaya data bersih." D3: "Poisson λ = 1,77," tanpa asumsi. D4: memakai λ = 1,77 → e^(−1,77 × 0,75) = e^(−1,3275) = 0,2651, tanpa (iii). D5: "P(jaringan) = 0,8." D6: "Data sudah cukup untuk semua kesimpulan." | 2–5 |
| Cukup | D1 benar. D2: melaporkan median dan menghitung pagar 103 menit, tetapi menyetujui pembuangan. D3: Poisson dengan dua asumsi tertulis, tanpa memakai informasi jam sibuk. D4 benar. D5: 0,9492 benar, probabilitas keliru tidak dihitung. D6: "Tidak bisa digeneralisasi," tanpa alasan. | 8–11 |
| Baik | Seluruh sub-butir benar. D2 menolak pembuangan dengan argumen p95 > pagar. D3 menyimpulkan dua laju terpisah dari perbedaan mean antarperiode dan rasio varians/mean per periode. D5 memberi keputusan berbasis angka. D6: "Kepuasan seluruh pasien tidak dapat disimpulkan karena hanya 18% yang mengisi secara sukarela dan hanya yang sudah dilayani." | 13,5–15 |

---

## 5. Memeriksa Angka dengan Python

Seluruh angka kunci di atas diperiksa ulang dengan Python (NumPy, SciPy) pada 8 Oktober 2026. Blok berikut dapat dijalankan di Google Colab **sesudah** Anda mengerjakan secara manual — UTS tetap tanpa komputer dan tanpa AI. Setiap nilai di kolom *Keluaran Python* pada tabel di bawahnya dicetak oleh salah satu baris `print` blok ini (komentar di ujung baris memuat keluaran yang diharapkan; Python memakai titik desimal).

```python
# Pemeriksaan angka kunci Latihan UTS Probabilitas dan Statistik
from math import comb, perm, exp, log, ceil
from collections import Counter
from itertools import product
import numpy as np
from scipy import stats

# A6 — koefisien variasi Pasar P dan Pasar Q
print("A6 =", 9000/60000, 7200/45000)                                                  # 0,15 0,16
# A7 — ±25% data antara median dan Q3, 360 hari
print("A7 =", 0.25 * 360)                                                              # 90,0
# A8 — median, modus, dan mean beban studi 40 mahasiswa
sks = np.repeat([18, 20, 21, 24], [6, 14, 12, 8])
print("A8 =", np.median(sks), np.bincount(sks).argmax(), sks.mean())                  # 20,5 20 20,8
# A9 — rata-rata gabungan berbobot
print("A9 =", round((30*3.20 + 20*3.45) / 50, 3))                                     # 3,3
# A11 — penurunan setahun (data lengkap) vs kenaikan pada rentang yang ditampilkan (ribu pengguna)
print("A11 =", (72 - 45) / 72, (45 - 40) / 40)                                      # 0,375 0,125
# A13 — pagar atas boxplot (Q1 = 20, Q3 = 40)
print("A13 =", 40 + 1.5*(40 - 20))                                                    # 70,0
# B1 — "rata-rata" kode pos yang keliru, modus, dan proporsinya
kode_pos = [12110, 12110, 16424, 12110, 40132]
modus, frek = Counter(kode_pos).most_common(1)[0]
print("B1 =", np.mean(kode_pos), modus, frek / len(kode_pos))                         # 18577,2 12110 0,6
# B2 — populasi lima server
boot = np.array([30, 34, 31, 37, 33])
print("B2 sigma^2 =", boot.var(ddof=0), "| sigma =", round(boot.std(ddof=0), 4))       # 6,0 | 2,4495
# B3 — paket kuis
print("B3 =", perm(9, 3), comb(7, 2), perm(9, 3) * comb(7, 2))                       # 504 21 10584
# B4 — jumlah keluaran model, nilai "Lainnya" terkoreksi, komplemen, gabungan saling lepas
print("B4 =", round(0.42 + 0.25 + 0.21 + 0.15, 2), round(1 - (0.42 + 0.25 + 0.21), 2),
      round(1 - 0.42, 2), round(0.25 + 0.21, 2))                                      # 1,03 0,12 0,58 0,46
# B5 — seleksi beasiswa: (a) diterima, (b) gugur berkas | tidak diterima
print("B5 =", round(0.6*0.5*0.8, 2), round(0.4 / 0.76, 4))                            # 0,24 0,5263
# B6 — Geometrik p = 0,7: E[X], P(X <= 3), P(X <= 4), k terkecil, P(X > 5 | X > 2)
G = stats.geom(0.7)
k_min = next(k for k in range(1, 20) if G.cdf(k) >= 0.99)
print("B6 =", round(G.mean(), 4), [round(float(G.cdf(k)), 4) for k in (3, 4)], k_min,
      ceil(log(0.01) / log(0.3)), round(G.sf(5) / G.sf(2), 4))                       # 1,4286 [0,973, 0,9919] 4 4 0,027
# B7, B8 — Normal
print("B7 =", round(stats.norm.cdf(250, 252, 4), 4), round(stats.norm.cdf(258, 252, 4) - stats.norm.cdf(248, 252, 4), 4))  # 0,3085 0,7745
print("B8 =", round(stats.norm.ppf(0.03), 4), round(stats.norm.ppf(0.03, 30, 4), 2),
      round(30 - 1.88*4, 2), round(stats.norm.sf(38, 30, 4), 4))                     # -1,8808 22,48 22,48 0,0228
# C1 — Gedung A (kuartil metode linear = posisi (n-1)p + 1)
A = np.array([3, 4, 4, 5, 6, 6, 7, 8, 20])
q1, q3 = np.percentile(A, [25, 75])
iqr = q3 - q1
pagar_bawah, pagar_atas = q1 - 1.5*iqr, q3 + 1.5*iqr
print("C1 =", A.mean(), np.median(A), ((A - A.mean())**2).sum(), round(A.std(ddof=1), 4), q1, q3, iqr,
      pagar_bawah, pagar_atas, A[(A < pagar_bawah) | (A > pagar_atas)])              # 7,0 6,0 210,0 5,1235 4,0 7,0 3,0 -0,5 11,5 [20]
# C1(b) — tambahan yang boleh (tidak disyaratkan): mean A tanpa 20; CV A dan CV B (%)
print("C1(b) =", round(A[A < 20].mean(), 2), round(A.std(ddof=1) / A.mean() * 100), round(2.55 / 7 * 100))  # 5,38 73 36
q1w, q3w = np.percentile(A, [25, 75], method="weibull")                              # metode (n+1)p
print("C1 (n+1)p =", q1w, q3w, q1w - 1.5*(q3w - q1w), q3w + 1.5*(q3w - q1w))      # 4,0 7,5 -1,25 12,75
B = np.array([4, 4, 5, 5, 7, 9, 9, 10, 10])   # satu-satunya himpunan bilangan bulat yang cocok dengan ringkasan B
print("C1 B =", B.mean(), round(B.std(ddof=1), 2), np.percentile(B, [25, 50, 75]))   # 7,0 2,55 [5. 7. 9.]
# C2 — (a) empat peluang; (b) C(96,3) dan tepat 2 COD; (c) laju QRIS
print("C2 =", 96/1200, round(36/216, 4), 36/96, 276/1200, comb(96, 3),
      round(comb(36, 2) * 60 / comb(96, 3), 4), 36/576)                              # 0,08 0,1667 0,375 0,23 142880 0,2646 0,0625
# C3 — detektor teks-AI: evidence, posterior, P(ditulis sendiri | tidak ditandai), posterior berantai
p_E = 0.05*0.90 + 0.95*0.03
post1 = 0.05*0.90 / p_E
post2 = post1*0.85 / (post1*0.85 + (1 - post1)*0.02)
print("C3 =", round(p_E, 4), round(post1, 4), round(1843/1853, 4), round(post2, 4))  # 0,0735 0,6122 0,9946 0,9853
# C3(b)–(d) — sel tabel 2.000 laporan, posterior berantai lewat frekuensi dan lewat pembulatan antara 4 desimal, porsi jujur
sel = [round(2000*0.05*0.90), round(2000*0.05*0.10), round(2000*0.95*0.03), round(2000*0.95*0.97)]
print("C3 sel =", sel, "| frekuensi =", round(76.5/77.64, 4), "| 4 desimal =", round(0.5204/(0.5204 + 0.0078), 4),
      "| 57/147 =", round(57/147, 4), "| 57 x 0,02 =", round(57*0.02, 2))           # [90, 10, 57, 1843] | 0,9853 | 0,9852 | 0,3878 | 1,14
# C4 — (a) kebebasan; (b) load balancer seri replika paralel; (c) kuorum >= 3 dari 4
print("C4(a) =", 25/500, 20/500, 9/500, round(0.05*0.04, 4), 9/20)                   # 0,05 0,04 0,018 0,002 0,45
X = stats.binom(4, 0.96)
print("C4 =", round(0.99*(1 - 0.04**3), 6), round(0.99*(1 - 0.04**4), 6),
      round(X.pmf(3), 6), round(X.pmf(4), 6), round(X.sf(2), 8), X.mean())         # 0,989937 0,989997 0,141558 0,849347 0,99090432 3,84
# C4(d) — pemeriksaan arah (tidak diminta): syarat S dilanggar; gangguan bersama 0,01
ps = [0.95, 0.96, 0.96, 0.96]
r_s = sum(np.prod([p if h else 1 - p for h, p in zip(hidup, ps)])
          for hidup in product([0, 1], repeat=4) if sum(hidup) >= 3)
r_bersama = 0.99 * stats.binom(4, 0.96 / 0.99).sf(2)
print("C4(d) =", round(r_s, 4), round(r_bersama, 4))                                  # 0,9898 0,9848
# D2, D3 — pagar atas waktu tunggu dan 5% dari 1.400 pasien; laju gabungan dan rasio varians/mean
print("D2 =", 52 + 1.5*(52 - 18), round(0.05*1400), "| D3 =", round(298/168, 2),
      round(2.21/1.77, 2), round(3.25/3.62, 2), round(1.53/1.51, 2))                 # 103,0 70 | 1,77 1,25 0,9 1,01
# D4 — rata-rata waktu antargalat (menit); P(T > 0,75 jam) lewat Eksponensial dan lewat Poisson
print("D4 =", 60/1.5, round(exp(-1.5*0.75), 4), round(stats.poisson(1.125).pmf(0), 4))   # 40,0 0,3247 0,3247
# D5 — probabilitas total P(504), posterior jaringan, probabilitas keputusan keliru
print("D5 =", round(0.7*0.8 + 0.3*0.1, 2), round(0.56/0.59, 4), round(0.03/0.59, 4))    # 0,59 0,9492 0,0508
```

| Butir | Nilai kunci | Keluaran Python (baris `print`) |
|---|---|---|
| A6 | CV 15% vs 16% | 0,15 / 0,16 |
| A7 | ±90 hari | 90,0 |
| A8 | median 20,5; modus 20 (mean 20,8 = pengecoh) | 20,5 / 20 / 20,8 |
| A9 | 3,30 MB | 3,3 |
| A11 | turun 37,5% sepanjang 2025; naik 12,5% pada rentang yang ditampilkan | 0,375 / 0,125 |
| A13 | pagar atas 70 jam | 70,0 |
| B1 | modus 12110, 60% ("rata-rata" keliru 18.577,2) | 18577,2 / 12110 / 0,6 |
| B2 | σ² = 6; σ = 2,45 | 6,0 / 2,4495 |
| B3 | 504; 21; 10.584 | 504 / 21 / 10584 |
| B4 | 1,03; 0,12; 0,58; 0,46 | 1,03 / 0,12 / 0,58 / 0,46 |
| B5 | 0,24; 0,5263 | 0,24 / 0,5263 |
| B6 | 1,43; k = 4; 0,0270 | 1,4286 / [0,973, 0,9919] / 4 / 4 (logaritma) / 0,027 |
| B7 | 0,3085; 0,7745 | 0,3085 / 0,7745 (tabel = eksak) |
| B8 | z = −1,88; T = 22,48 jam; ≈ 2,5% | −1,8808 / 22,48 (eksak) / 22,48 (z tabel −1,88) / 0,0228 (nilai eksak, bukan aturan empiris) |
| C1 | 7; 6; Σ = 210; 5,12; 4; 7; 3; −0,5 dan 11,5; pencilan 20 | 7,0 / 6,0 / 210,0 / 5,1235 / 4,0 / 7,0 / 3,0 / −0,5 / 11,5 / [20] |
| C1(b) (tambahan, tidak disyaratkan) | mean A tanpa 20: 5,38; CV 73% vs 36% | 5,38 / 73 / 36 |
| C1 (metode lain, data B) | (n + 1)p: Q3 7,5, pagar −1,25 dan 12,75; B: x̄ 7, s 2,55, Q1 5, median 7, Q3 9 | 4,0 / 7,5 / −1,25 / 12,75; 7,0 / 2,55 / [5, 7, 9] |
| C2 | 0,08; 0,1667; 0,375; 0,23; 142.880; 0,2646; QRIS 6,25% | 0,08 / 0,1667 / 0,375 / 0,23 / 142880 / 0,2646 / 0,0625 |
| C3 | 0,0735; 0,6122; 0,9946; 0,9853 (0,9852 dengan pembulatan antara 4 desimal); sel 90, 10, 57, 1.843; 39%; 1,14 | 0,0735 / 0,6122 / 0,9946 / 0,9853; [90, 10, 57, 1843] / 0,9853 / 0,9852 / 0,3878 / 1,14 |
| C4 | 0,05; 0,04; 0,018 vs 0,002; 0,45; 0,9899 (batas 0,99); 0,9909; 3,84; arah (d): S dilanggar 0,9898, gangguan bersama 0,9848 | 0,05 / 0,04 / 0,018 / 0,002 / 0,45; 0,989937 (n = 4: 0,989997) / 0,141558 + 0,849347 = 0,99090432 / 3,84; 0,9898 / 0,9848 |
| D2, D3 | pagar 103 menit; ±70 pasien; λ ≈ 1,77; rasio 1,25; 0,90; 1,01 | 103,0 / 70 / 1,77 / 1,25 / 0,9 / 1,01 |
| D4 | 40 menit; 0,3247 | 40,0 / 0,3247 / 0,3247 |
| D5 | 0,59; 0,9492; 0,0508 | 0,59 / 0,9492 / 0,0508 |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
