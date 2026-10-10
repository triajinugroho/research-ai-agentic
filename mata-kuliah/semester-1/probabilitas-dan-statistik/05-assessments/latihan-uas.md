---
id: uai-if52510033-latihan-uas
tipe: asesmen
judul: "Latihan UAS — Probabilitas dan Statistik"
kode_mk: IF52510033
nama_mk: Probabilitas dan Statistik
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-09
---

# LATIHAN UJIAN AKHIR SEMESTER (SIMULASI)

## Probabilitas dan Statistik — IF52510033

> **Latihan UAS — bukan naskah UAS.** Simulasi lengkap UAS Probabilitas dan Statistik Ganjil 2026/2027 untuk berlatih: komposisi, durasi (120 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UAS. Naskah UAS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> **Cara memakai latihan ini.** Kerjakan dalam satu kali duduk dengan batas waktu **120 menit**, *closed book*, **tanpa AI** dan **tanpa membuka pembahasan** — sesuai aturan UAS ([kisi-kisi UAS §1](kisi-kisi-uas.md#1-ketentuan-ujian)). Siapkan kalkulator ilmiah *non-programmable* dan alat tulis; sebagai pengganti tabel yang dibagikan pengawas, pakai [Lampiran A.1–A.5 buku ajar](../06-buku-ajar/lampiran.md#lampiran-a-tabel-distribusi) saja — [tabel Z](../06-buku-ajar/lampiran.md#a1-tabel-z--distribusi-normal-standar), [tabel t](../06-buku-ajar/lampiran.md#a2-tabel-t--distribusi-student), tabel chi-square, dan tabel F. Bagian Lampiran lain, termasuk tabel korelasi A.6 dan formularium, tidak boleh dibuka. Catat menit yang Anda pakai untuk setiap bagian. Baru **sesudah** waktu habis, cocokkan jawaban Anda dengan [pembahasan dan pedoman skor](latihan-uas-pembahasan.md), lalu hitung skor Anda sendiri. Penandaan Sub-CPMK per butir ada di pembahasan dan di [cetak biru butir](latihan-uas-cetak-biru.md).

---

**UNIVERSITAS AL AZHAR INDONESIA**
Fakultas Sains dan Teknologi — Program Studi Informatika

| | |
|---|---|
| **Mata kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Asesmen** | Latihan UAS (simulasi) — persiapan UAS Semester Ganjil 2026/2027, Minggu 16 |
| **Kelas** | IF26A, IF26H |
| **Penyusun** | Tri Aji Nugroho, S.T., M.T. |
| **Durasi** | 120 menit |
| **Sifat** | *Closed book* |
| **Cakupan** | Komprehensif Minggu 1–15, penekanan Minggu 9–14 |

> **Amanah berlatih.** Latihan ini tidak dinilai; manfaatnya bergantung pada kejujuran Anda sendiri. Kerjakan tanpa bantuan orang lain, catatan, atau AI, dengan waktu yang benar-benar dibatasi — sama seperti amanah akademik yang berlaku saat UAS ([kerangka asesmen §7](assessment-framework.md#7-integritas-akademik)).

---

## Petunjuk Umum

1. **Alat bantu yang diizinkan:** kalkulator ilmiah *non-programmable* dan alat tulis.
2. **Tabel:** saat UAS, pengawas membagikan tabel distribusi Normal baku (luas kumulatif P(Z ≤ z)), tabel-t, tabel chi-square, dan tabel F bersama lembar soal. Saat berlatih, pakai Lampiran A.1–A.5 buku ajar (formatnya sama); semua nilai tabel yang diperlukan latihan ini ada di sana. Nilai yang derajat bebasnya tidak tercantum di tabel dicetak langsung pada soal.
3. **Rumus tidak disediakan** — hafalkan [daftar rumus kisi-kisi UAS §8](kisi-kisi-uas.md#8-daftar-rumus-tambahan-di-luar-rumus-uts) beserta [daftar rumus kisi-kisi UTS §7](kisi-kisi-uts.md#7-daftar-rumus-yang-harus-dihafal).
4. **Dilarang:** catatan dan formularium dalam bentuk apa pun (termasuk Lampiran buku ajar; saat berlatih, buka hanya tabel A.1–A.5 sebagai pengganti tabel dari pengawas), telepon genggam, jam pintar, laptop, dan **AI dalam bentuk apa pun**.
5. Latihan terdiri atas empat bagian. Total skor **100**.

   | Bagian | Bentuk | Jumlah butir | Skor | Waktu saran |
   |---|---|---|---|---|
   | A | Pilihan ganda | 15 | 15 | 15 menit |
   | B | Isian / hitungan pendek | 10 | 20 | 25 menit |
   | C | Uraian terstruktur | 5 | 40 | 50 menit |
   | D | Studi kasus terpadu | 1 | 25 | 25 menit |

   Waktu saran mengikuti kisi-kisi UAS §2 dan jumlahnya 115 menit, sehingga hanya tersisa 5 menit. Latihan ini memperhitungkan 5 menit untuk membaca seluruh soal di awal dan sedikitnya 5 menit untuk memeriksa ulang di akhir, jadi usahakan setiap bagian selesai sedikit lebih cepat daripada waktu sarannya. Bila waktu terasa sempit, kerjakan **Bagian D lebih dahulu** (saran kisi-kisi §2).

   **Panjang latihan ini masih dikalibrasi.** Taksiran waktu kerjanya ±104–110 menit (A ±15–17, B ±21,5–22,6, C ±45–47, D ±22–23 menit); bersama 5 menit membaca dan sedikitnya 5 menit memeriksa, totalnya ±114–120 menit. Jadi latihan ini diperkirakan muat dalam 120 menit, tetapi hampir tanpa sisa, dan waktu kemungkinan terasa sempit; taksiran ini belum diuji dengan pengerjaan sungguhan. Catat waktu yang Anda pakai per bagian. Bila waktu habis, tandai butir terakhir yang selesai, lalu selesaikan sisanya dan catat waktu tambahannya terpisah. Panjang naskah UAS ditetapkan dari uji coba berwaktu sebelum UAS; bila dosen memintanya, serahkan catatan waktu Anda tanpa nama sebagai data pelengkap (yang dipakai hanya rekap agregatnya). Bila panjangnya disesuaikan, latihan ini diperbarui dengan cara yang sama.

6. Untuk Bagian B, C, dan D **tuliskan langkah**. Jawaban yang hanya berisi angka akhir tanpa langkah memperoleh **paling banyak 40%** skor butir. Beberapa perintah membatasi panjang jawaban (mis. "paling banyak 2 kalimat"); hitungan dan notasi tidak termasuk batas itu. Batas ini membantu Anda mengatur waktu — yang dinilai adalah unsur jawaban, bukan panjangnya.
7. **Anjuran (tidak wajib):** tuliskan "diketahui" dan "ditanya" dalam notasi sebelum menghitung probabilitas; untuk soal Normal, buat sketsa kurva dan arsir daerah yang dicari; untuk uji hipotesis, tulis H₀ dan H₁ secara eksplisit sebelum menghitung.
8. Pakai koma sebagai pemisah desimal. Kecuali diminta lain, bulatkan probabilitas sampai **4 angka di belakang koma** dan nilai lain sampai **2 angka di belakang koma**. Tuliskan satuan. *p-value* yang dibaca dari tabel-t dinyatakan sebagai batas, mis. "p < 0,01".
9. **Tag butir:** tag seperti `[C3 · 1]` menyatakan level Bloom dan skor butir. Pada Bagian B, C, dan D, skor tiap sub-butir tertulis dalam kurung; pada Bagian C dan D juga level Bloom-nya.
10. Seluruh data dalam latihan ini adalah **data rekaan**.

---

## Bagian A — Pilihan Ganda (15 butir, skor 15)

Lingkari **satu** jawaban yang paling tepat. Setiap butir bernilai 1.

**A1.** `[C2 · 1]`
Laporan keamanan kampus: *"80% akun surel yang dibobol tahun ini tidak memakai autentikasi dua faktor (2FA)."* Seorang pejabat menyimpulkan: *"Jadi, 80% akun tanpa 2FA akan dibobol."* Kesimpulan itu …

- (a) tepat, karena kedua kalimat memakai angka 80% untuk kelompok akun yang sama.
- (b) keliru; yang benar 20%, yaitu komplemen dari 80%.
- (c) keliru; laporan memberi P(tanpa 2FA | dibobol), bukan P(dibobol | tanpa 2FA).
- (d) tepat, asalkan lebih dari separuh akun kampus tanpa 2FA.

**A2.** `[C3 · 1]`
Sebuah laboratorium memiliki 8 *flashdisk* pinjaman; 3 di antaranya terinfeksi *malware*. Asisten memeriksa *flashdisk* itu satu per satu dalam urutan acak (**tanpa pengembalian**) dan berhenti begitu menemukan yang terinfeksi. Probabilitas ia baru menemukannya pada pemeriksaan **ketiga** adalah …

- (a) 0,1465
- (b) 0,1786
- (c) 0,3571
- (d) 0,5000

**A3.** `[C2 · 1]`
Setiap tiket bantuan TI diberi tepat satu tingkat prioritas. Untuk satu tiket, T = "prioritas Tinggi" dengan P(T) = 0,3 dan R = "prioritas Rendah" dengan P(R) = 0,5. Pernyataan yang benar adalah …

- (a) T dan R saling bebas, karena prioritas satu tiket tidak memengaruhi tiket lain.
- (b) T dan R saling lepas sekaligus saling bebas, karena P(T ∩ R) = 0.
- (c) P(T ∩ R) = 0,15, karena T dan R saling bebas.
- (d) T dan R saling lepas, sehingga P(T ∪ R) = 0,8; keduanya tidak saling bebas.

**A4.** `[C2 · 1]`
Model penanda akun bot pada aplikasi kampus bersensitivitas dan berspesifisitas 95%; hanya 0,5% akun yang benar-benar bot. Untuk **menaikkan PPV** sebanyak mungkin, perbaikan yang diprioritaskan adalah …

- (a) Menaikkan sensitivitas menjadi 99,5% dengan spesifisitas tetap 95%.
- (b) Menaikkan spesifisitas menjadi 99,5% dengan sensitivitas tetap 95%.
- (c) Menurunkan ambang skor agar lebih banyak akun bot tertandai.
- (d) Menambah data latih tanpa mengubah sensitivitas dan spesifisitas.

**A5.** `[C3 · 1]`
Server *continuous integration* menjalankan 20 *build* berurutan tiap malam dengan *cache* bersama; bila satu *build* gagal karena *cache* rusak, *build* berikutnya cenderung ikut gagal. Untuk banyaknya *build* gagal, pernyataan yang paling tepat adalah …

- (a) Binomial kurang tepat, karena syarat percobaan saling bebas tidak terpenuhi.
- (b) Binomial(20, p) tepat, karena banyaknya *build* tetap dan hasilnya biner.
- (c) Poisson tepat, karena yang dihitung adalah banyaknya kejadian gagal.
- (d) Geometrik tepat, karena *build* dijalankan berurutan sampai ada yang gagal.

**A6.** `[C3 · 1]`
Pemindai OCR formulir pendaftaran salah membaca 4% formulir, saling bebas antarformulir. Dalam sehari dipindai 150 formulir. Rata-rata dan simpangan baku banyaknya formulir salah baca per hari berturut-turut adalah …

- (a) 6 dan 5,76
- (b) 0,04 dan 0,20
- (c) 6 dan 2,40
- (d) 6 dan 2,45

**A7.** `[C2 · 1]`
Waktu unggah berkas T (detik) adalah peubah acak kontinu dengan fungsi densitas f(t). Pernyataan yang benar adalah …

- (a) P(T = 3) = f(3), yaitu tinggi kurva densitas di t = 3.
- (b) P(T ≤ 3) = P(T < 3), karena untuk peubah kontinu P(T = 3) = 0.
- (c) f(t) tidak boleh lebih dari 1, karena f(t) adalah probabilitas.
- (d) P(T = 3) > 0 bila 3 detik adalah waktu unggah yang paling sering.

**A8.** `[C2 · 1]`
Q-Q plot Normal untuk 2.000 ukuran berkas di penyimpanan awan kampus melengkung ke atas di ujung kanan; kemencengannya 2,4. Pernyataan yang paling tepat adalah …

- (a) Data mendekati Normal karena n besar; model Normal layak untuk ukuran satu berkas.
- (b) Data menceng kiri, sehingga mean ukuran berkas lebih kecil daripada median.
- (c) Kemencengan 2,4 menandakan sebaran simetris dengan ekor yang ringan.
- (d) Data menceng kanan; model Normal tidak layak untuk ukuran satu berkas.

**A9.** `[C3 · 1]`
Sebanyak 81 pengukuran waktu muat halaman LMS menghasilkan rata-rata 3,1 detik dengan simpangan baku 2,7 detik. Pernyataan yang benar adalah …

- (a) Galat baku 0,30 detik; ia mengukur sebaran x̄, bukan sebaran waktu muat.
- (b) Galat baku 2,70 detik, karena galat baku sama dengan simpangan baku sampel.
- (c) Galat baku 0,033 detik (2,7/81); sebaran waktu muat menyempit bila n bertambah.
- (d) Sekitar 95% waktu muat individual berada dalam 3,1 ± 2 × 0,30 detik.

**A10.** `[C2 · 1]`
Lama sesi pengguna aplikasi pemesanan makanan kantin sangat menceng kanan dengan beberapa nilai ekstrem. Tim ingin mendekati distribusi sampling x̄ dari 20 sesi acak dengan distribusi Normal. Pendekatan itu …

- (a) layak, karena Teorema Limit Pusat berlaku untuk populasi apa pun dan n berapa pun.
- (b) layak, karena n ≥ 15 sudah cukup untuk semua bentuk populasi.
- (c) belum tentu layak; populasi sangat menceng biasanya memerlukan n ≥ 50, kadang lebih.
- (d) tidak pernah layak, karena populasi tidak Normal selalu menghasilkan x̄ tidak Normal.

**A11.** `[C2 · 1]`
Survei acak menghasilkan interval kepercayaan (IK) 95% untuk rata-rata waktu tempuh mahasiswa ke kampus: [38,2 ; 45,8] menit. Pernyataan yang benar adalah …

- (a) Ada probabilitas 95% bahwa μ berada antara 38,2 dan 45,8 menit.
- (b) Sekitar 95% mahasiswa menempuh perjalanan 38,2–45,8 menit.
- (c) Bila survei diulang, 95% rata-rata sampel baru akan jatuh di antara 38,2 dan 45,8.
- (d) Bila prosedur ini diulang pada banyak sampel, ±95% interval yang dihasilkan memuat μ.

**A12.** `[C3 · 1]`
IK 95% untuk rata-rata waktu kompilasi sebuah proyek, dihitung dari 49 kali kompilasi dengan t₀,₀₂₅;₄₈ ≈ 2,01, adalah [52,0 ; 58,0] detik. Dengan data yang sama dan t₀,₀₀₅;₄₈ ≈ 2,68, IK 99%-nya adalah …

- (a) [51,0 ; 59,0] detik
- (b) [52,75 ; 57,25] detik
- (c) [52,0 ; 58,0] detik
- (d) [49,0 ; 61,0] detik

**A13.** `[C2 · 1]`
Seorang analis menghitung varians sampel dengan penyebut n − 1, bukan n. Alasan yang paling tepat adalah …

- (a) Agar s² lebih kecil, sehingga estimatornya menjadi lebih efisien.
- (b) Agar s² tak bias: rata-rata s² dari banyak sampel sama dengan σ².
- (c) Karena dengan penyebut n, s² tidak konsisten walaupun n sangat besar.
- (d) Karena penyebut n − 1 hanya sah bila data berdistribusi Normal.

**A14.** `[C3 · 1]`
ANOVA satu arah membandingkan waktu kompresi tiga algoritma (11 pengukuran per algoritma, N = 33): SS_antar = 300 dan SS_dalam = 1.200, sehingga MS_antar = 150 dan MS_dalam = 40. Pada α = 0,05 (tabel F), pernyataan yang benar adalah …

- (a) F = 3,75 > F tabel, tolak H₀; jadi setiap pasangan algoritma pasti berbeda nyata.
- (b) F = 0,27 < F tabel, gagal menolak H₀; sedangkan η² = 0,20.
- (c) F = 3,75 > F tabel, tolak H₀; η² = 0,20, yaitu 20% keragaman terkait algoritma.
- (d) F = 3,75 > F tabel, tolak H₀; η² = 0,25, yaitu SS_antar dibagi SS_dalam.

**A15.** `[C3 · 1]`
Tim akan menguji kebebasan jenis perangkat dan tingkat keluhan pengguna aplikasi peminjaman ruang dengan uji chi-square.

| Jenis perangkat | Tidak ada keluhan | Keluhan ringan | Keluhan berat | Total |
|---|---|---|---|---|
| Ponsel | 30 | 12 | 2 | 44 |
| Tablet | 6 | 6 | 4 | 16 |
| **Total** | **36** | **18** | **6** | **60** |

Frekuensi harapan baris Ponsel: 26,4; 13,2; 4,4. Pernyataan yang benar tentang syarat kelayakan uji ini adalah …

- (a) Tidak terpenuhi: 3 dari 6 sel memiliki frekuensi harapan < 5, yang terkecil 1,6.
- (b) Terpenuhi, karena hanya 1 dari 6 sel yang frekuensi harapannya kurang dari 5.
- (c) Terpenuhi, karena N = 60 ≥ 30 dan tidak ada satu pun sel yang kosong.
- (d) Tidak terpenuhi hanya karena 2 sel teramati < 5; frekuensi harapan tak perlu dihitung.

---

## Bagian B — Isian / Hitungan Pendek (10 butir, skor 20)

Tuliskan langkah singkat dan jawaban akhir. Setiap butir bernilai 2.

**B1.** `[C3 · 2]`
Sebuah sistem membuat token akses sementara berupa 4 karakter **berbeda** dari 16 karakter heksadesimal (0–9 dan a–f); urutan karakter bermakna, mis. 3a9f ≠ a39f.

- (a) Berapa banyak token yang mungkin? Tunjukkan aturan pencacahannya dan mengapa aturan itu yang tepat di sini. *(1)*
- (b) Bila setiap token sama mungkin, hitung probabilitas sebuah token acak hanya memuat angka 0–9. *(1)*

**B2.** `[C3 · 2]`
Audit repositori proyek mahasiswa menemukan: 18% repositori memuat kunci API di dalam kode (K) dan 12% tidak memiliki berkas README (R). Di antara repositori tanpa README, 50% memuat kunci API. Satu repositori dipilih acak.

- (a) Hitung P(K ∩ R), lalu probabilitas repositori itu memiliki sedikitnya satu dari kedua masalah. *(1)*
- (b) Hitung P(R | K), lalu jelaskan dalam satu kalimat mengapa nilainya berbeda dari 50%. *(1)*

**B3.** `[C3 · 2]`
Layanan rapor daring sebuah sekolah berjalan pada dua tingkat yang tersusun **seri**: tingkat web (2 server replika, masing-masing tersedia dengan peluang 0,95) dan tingkat basis data (2 server replika, masing-masing 0,90). Setiap tingkat berfungsi bila sedikitnya satu replikanya hidup; semua server diandaikan saling bebas.

- (a) Hitung keandalan layanan. *(1)*
- (b) Anggaran cukup untuk **satu** server tambahan. Bila ditambahkan di tingkat web, keandalan layanan menjadi 0,9899. Hitung keandalannya bila server itu ditambahkan di tingkat basis data, lalu tentukan tingkat yang lebih baik. *(1)*

**B4.** `[C3 · 2]`
Layanan SMS kode OTP mengirim 2.500 pesan per hari; setiap pesan gagal terkirim dengan peluang 0,0008, saling bebas. Misalkan X = banyaknya pesan gagal per hari.

- (a) Tuliskan distribusi X beserta parameternya. Jelaskan mengapa distribusi Poisson layak dipakai sebagai hampirannya, dan tentukan λ. *(1)*
- (b) Dengan hampiran Poisson, hitung P(X ≤ 1). *(1)*

**B5.** `[C3 · 2]`
Latensi (*ping*) dari kampus ke server ujian daring berdistribusi Normal dengan μ = 48 ms dan σ = 6 ms.

- (a) Perkirakan persentase ping antara 36 ms dan 60 ms dengan aturan empiris, tanpa tabel. *(1)*
- (b) Hitung skor-z ping 63 ms, lalu dengan tabel Normal baku hitung proporsi ping yang melebihi 63 ms. *(1)*

**B6.** `[C3 · 2]`
Agar permintaan ulang tidak bertabrakan, sebuah aplikasi menunggu jeda acak J sebelum mencoba lagi (*retry*), dengan J berdistribusi Uniform kontinu pada selang 0–800 ms.

- (a) Hitung P(300 ≤ J ≤ 500) dan P(J > 680). *(1)*
- (b) Tentukan rata-rata J dan nilai j sehingga P(J ≤ j) = 0,90. *(1)*

**B7.** `[C3 · 2]`
Jarak tempuh harian pengemudi ojek daring di sebuah kota mempunyai rata-rata μ = 40 km dan simpangan baku σ = 18 km; sebarannya agak menceng kanan. Diambil sampel acak 36 pengemudi.

- (a) Hitung galat baku x̄, lalu dengan Teorema Limit Pusat hitung P(x̄ > 45 km). *(1,5)*
- (b) Berapa ukuran sampel yang diperlukan agar galat baku menjadi separuh dari (a)? *(0,5)*

**B8.** `[C3 · 2]`
Rekaman 16 sesi percakapan acak dengan *chatbot* layanan akademik: durasi rata-rata 6,5 menit, simpangan baku 2,0 menit. Untuk rata-rata durasi seluruh sesi, seorang analis melaporkan interval kepercayaan 95% berikut: 6,5 ± 1,96 × 2,0/√16 = [5,52 ; 7,48] menit.

- (a) Jelaskan kekeliruan prosedur analis itu. *(0,5)*
- (b) Hitung ulang interval itu dengan prosedur yang benar memakai tabel-t; tuliskan derajat bebas dan nilai t yang Anda pakai. *(1,5)*

**B9.** `[C3 · 2]`
Pengembang aplikasi perpustakaan versi baru mengklaim aplikasinya tertutup sendiri (*crash*) pada paling banyak 10% pengguna. Dalam uji coba, 40 dari 250 pengguna acak mengalami *crash*; galat baku proporsinya 0,0232.

- (a) Periksa syarat kelayakan interval kepercayaan proporsi. *(0,5)*
- (b) Hitung interval kepercayaan 95% untuk proporsi pengguna yang mengalami *crash*. Dengan interval itu, jelaskan apakah klaim pengembang didukung data, dan mengapa p̂ = 16% saja belum cukup untuk menilai klaim itu. *(1,5)*

**B10.** `[C3 · 2]`
Unit TI kampus akan menyurvei 600 mahasiswa acak untuk mengestimasi proporsi pemakai pengelola kata sandi (*password manager*) pada tingkat kepercayaan 95%, tanpa dugaan awal tentang proporsinya. Hasilnya juga dilaporkan terpisah untuk mahasiswa baru, yang diperkirakan 150 dari 600 responden.

- (a) Hitung margin galat terbesar untuk seluruh responden dan untuk subkelompok mahasiswa baru. *(1)*
- (b) Pimpinan meminta margin galat subkelompok mahasiswa baru paling besar ±5 poin persen. Berapa mahasiswa baru minimum yang harus disurvei, dan berapa tambahannya dibanding 150? *(1)*

---

## Bagian C — Uraian Terstruktur (5 butir, skor 40)

Jawaban dinilai pada empat aspek kisi-kisi UAS §6: ketepatan rumus, ketepatan hitung, kecocokan asumsi, dan kualitas interpretasi. Bobot aspek kisi-kisi (30/25/25/20%) dipenuhi pada total Bagian C; porsi aspek per butir ada di pembahasan.

### C1. Lampiran Surel dan Pemindai *Malware* `[C3–C4 · 8]`

Server surel sebuah kampus menerima lampiran dari tiga sumber. Rekap log server satu semester:

| Sumber lampiran | Porsi dari seluruh lampiran | Proporsi lampiran yang mengandung *malware* |
|---|---|---|
| Domain kampus | 70% | 0,1% |
| Domain mitra | 22% | 0,5% |
| Domain lain | 8% | 5% |

Kampus berencana memasang pemindai *malware* dengan sensitivitas 95% dan spesifisitas 98%.

(a) Sebuah lampiran ternyata mengandung *malware*. Berapa probabilitas lampiran itu berasal dari domain lain? Kerjakan dengan Teorema Bayes: tulis keempat komponennya (prior, *likelihood*, *evidence*, posterior) dalam notasi, dan hitung *evidence* dengan hukum probabilitas total. Syarat apa yang harus dipenuhi ketiga sumber agar hukum itu sah? Akhiri dengan membandingkan posterior dan prior-nya dalam satu kalimat. *(3 poin · C3)*

(b) Bila pemindai dijalankan pada **semua** lampiran, probabilitas sebuah lampiran ditandai pemindai adalah 0,025394. Hitung PPV dan NPV, lalu tafsirkan kedua angka itu. Sebutkan asumsi tentang sensitivitas dan spesifisitas pemindai yang diperlukan perhitungan ini. *(2,5 poin · C3)*

(c) Untuk menghemat beban server, administrator mengusulkan pemindai **hanya** dijalankan pada lampiran domain mitra dan domain lain; dengan kebijakan ini, PPV pemindai menjadi 0,4510. Dari seluruh lampiran yang mengandung *malware*, hitung proporsi yang tidak pernah dipindai. Analisis usulan itu dengan angka dari (b) dan (c) — apa yang diperoleh, apa yang dikorbankan, dan satu asumsi tentang perilaku pengirim *malware* yang membuat kebijakan itu rapuh — dalam paling banyak 2 kalimat di luar hitungan. *(2,5 poin · C4)*

### C2. Undian Urutan Presentasi Proyek `[C3–C4 · 8]`

Kelas IF26A memiliki 8 kelompok proyek. Urutan presentasi Minggu 15 diundi: kedelapan kelompok diurutkan secara acak; urutan 1–4 tampil di sesi pagi dan urutan 5–8 di sesi siang.

(a) Hitung banyaknya susunan urutan presentasi yang mungkin dan banyaknya kemungkinan himpunan empat kelompok di sesi pagi. Pada setiap hitungan, tunjukkan apakah urutan diperhitungkan dan bagaimana hal itu menentukan aturan pencacahannya. *(3 poin · C3)*

(b) Kelompok X dan Y ingin tampil di sesi yang sama: keduanya di sesi pagi **atau** keduanya di sesi siang. Hitung probabilitas keduanya di sesi pagi, lalu probabilitas keduanya di sesi yang sama; tunjukkan apakah kedua kejadian itu dapat terjadi bersamaan dan bagaimana hal itu menentukan aturan penjumlahan yang Anda pakai. Sebutkan asumsi tentang undian yang Anda perlukan. *(3 poin · C3)*

(c) Misalkan A = "X tampil di sesi pagi" dan B = "Y tampil di sesi pagi". Dengan definisi formal kebebasan dua kejadian, analisis apakah A dan B saling bebas; lalu uraikan mengapa hasil itu wajar untuk undian ini, dalam paling banyak 2 kalimat. *(2 poin · C4)*

### C3. Gerbang Parkir Kampus `[C3–C4 · 8]`

Pada pukul 07.00–08.00, sepeda motor tiba di gerbang parkir kampus rata-rata 3 kendaraan per menit. Tim sarana memodelkan banyaknya kedatangan per menit, X, dengan distribusi Poisson. Diketahui P(X ≤ 3) = 0,6472, P(X = 4) = 0,1680, dan P(X = 5) = 0,1008.

(a) Tuliskan parameter distribusi itu dan dua asumsi model Poisson, lalu hitung probabilitas tidak ada kendaraan yang tiba dalam satu menit. *(2 poin · C3)*

(b) Tim menargetkan kedatangan melebihi kapasitas gerbang pada rata-rata paling banyak 3 menit per jam. Lengkapi tabel berikut untuk gerbang berkapasitas 5 dan 6 kendaraan per menit: hitung banyaknya menit per jam yang diperkirakan melampaui kapasitas, lalu tentukan apakah target terpenuhi. *(2 poin · C3)*

| Kapasitas k | P(X = k) | P(X ≤ k) | Menit per jam yang melampaui kapasitas | Target terpenuhi? |
|---|---|---|---|---|
| 5 | | | | |
| 6 | | | | |

(c) Seorang pengelola mengusulkan gerbang berkapasitas 3 kendaraan per menit "karena rata-ratanya 3". Analisis usulan ini dengan P(X > 3). Sebutkan pula satu kondisi nyata menjelang kuliah pukul 07.30 yang membuat asumsi Poisson diragukan, asumsi yang dilanggarnya, dan dampaknya pada kapasitas yang diperlukan. Jawab dalam paling banyak 2 kalimat di luar hitungan. *(2 poin · C4)*

(d) Hitung rata-rata jeda antarkedatangan dalam detik. Sudah 40 detik berlalu tanpa kedatangan: hitung probabilitas sebuah kendaraan tiba dalam 10 detik berikutnya, sebutkan sifat distribusi yang Anda pakai, dan jelaskan maknanya dalam konteks ini. *(2 poin · C3)*

### C4. Konsumsi Daya Server `[C3 · 8]`

Pusat data kampus memiliki 200 server identik. Tim mengukur konsumsi daya (watt) 8 server yang dipilih acak pada beban puncak; hasilnya, sudah diurutkan dari yang terkecil:

375, 390, 405, 420, 420, 435, 450, 465 (Σx = 3.360; jumlah kuadrat simpangan terhadap rata-ratanya: Σ(x − x̄)² = 6.300)

(a) Hitung rata-rata, median, dan simpangan baku sampel data ini, lalu periksa kesimetrisan sebarannya dengan membandingkan rata-rata dan median. *(2 poin · C3)*

Untuk (b)–(d), anggap konsumsi daya satu server berdistribusi Normal dengan μ dan σ sama dengan rata-rata dan simpangan baku di (a).

(b) Hitung dan tafsirkan proporsi server yang konsumsinya melebihi 480 W. Sebutkan asumsi yang mendasari pemakaian model Normal, dan jelaskan sejauh mana hasil (a) mendukungnya. *(2 poin · C3)*

(c) Tim memasang ambang peringatan pada persentil ke-90 konsumsi daya. Hitung ambang itu dalam watt dan tafsirkan maknanya bagi tim dalam satu kalimat. *(2 poin · C3)*

(d) Satu rak berisi 16 server dengan pemutus daya 7.000 W. Hitung probabilitas total konsumsi daya satu rak melebihi 7.000 W, sebutkan asumsi tentang ke-16 server yang Anda perlukan, dan tafsirkan probabilitas itu bagi pengelola pusat data dalam satu kalimat. *(2 poin · C3)*

### C5. Pengikut Media Sosial dan Omzet UMKM `[C3–C4 · 8]`

Data 10 UMKM kuliner di sebuah kota: x = banyaknya pengikut akun media sosial (ribu), y = omzet bulanan (juta rupiah).

```
 y (juta Rp)
  44 |
     |
  40 |                                  ●
     |
     |                      ●                 ●
     |                        ●
     |                    ●
  30 |                              ●
     |                        ●
     |
     |
     |
  20 |                ●
     |                                                            ●
     |      ●
     |
     +------------------------------------------------------------------
      0         5         10        15        20        25        30   x (ribu pengikut)
```

*(Sketsa: setiap baris mewakili 2 juta rupiah; posisi vertikal titik dibulatkan ke kelipatan 2.)*

Pengikut satu UMKM melonjak karena videonya viral pekan lalu. Analis memisahkan UMKM itu; ringkasan 9 UMKM lainnya: x̄ = 12 ribu, s_x = 5 ribu, ȳ = 30 juta, s_y = 8 juta, r = 0,80, dan x berentang 3–20 ribu.

(a) Tunjukkan titik yang kemungkinan adalah UMKM viral itu (perkirakan koordinatnya), lalu deskripsikan arah, bentuk, dan kekuatan hubungan pada 9 titik lainnya. Apakah memisahkan titik itu dari analisis sah? Beri alasannya dan sebutkan syaratnya. Jawab dalam paling banyak 2 kalimat di luar koordinat. *(2 poin · C3)*

(b) Hitung kemiringan dan intersep garis regresi omzet terhadap pengikut, lalu prediksi omzet UMKM dengan 15 ribu pengikut. *(2 poin · C3)*

(c) Hitung dan tafsirkan R². Plot residual regresi serupa pada data dua kota lain yang lebih besar (masing-masing 120 UMKM, pengikut 2–25 ribu) ada di bawah. Analisis kedua plot: untuk setiap plot, pilah apakah ada asumsi LINE yang dilanggar; bila ada, sebutkan asumsinya, tanda yang Anda lihat, dan satu tindak lanjut. *(2 poin · C4)*

```
 Plot P (kota P)                            Plot Q (kota Q)
 residual (juta Rp)                         residual (juta Rp)
 +12 |                               ·  ·    +12 |
     |                        ·        ·         |
  +6 |                  ·        ·  ·         +6 |   ·       ·       ·       ·      ·
     |  ·   ·   ·   ·      ·    ·                | ·     ·      ·       ·       ·
   0 +·--·-·--·--·-·--·--·---·-----·------     0 +·----·----·-----·----·---·-----·---·
     | ·  ·    ·  ·    ·    ·                    |    ·    ·   ·    ·     ·    ·   ·
  −6 |               ·    ·    ·      ·       −6 |  ·         ·       ·       ·
     |                       ·    ·      ·       |
 −12 |                              ·   ·    −12 |
     +------------------------------------       +------------------------------------
      15        25        35        45            15        25        35        45
                prediksi omzet (juta Rp)                    prediksi omzet (juta Rp)
```

*(Sketsa: hanya sebagian dari 120 titik tiap kota yang digambar.)*

(d) Pemilik UMKM berpengikut 10 ribu berkata: *"Garis regresi itu membuktikan bahwa pengikut menaikkan omzet. Saya akan membeli 80 ribu pengikut agar omzet saya naik berlipat."* Hitung prediksi garis (b) untuk 90 ribu pengikut. Lalu analisis klaim itu dari sisi sebab-akibat dan rentang data, nyatakan apakah klaim itu didukung data, dan tuliskan tafsir kemiringan (b) yang sah — dalam paling banyak 2 kalimat di luar hitungan. *(2 poin · C4)*

---

## Bagian D — Studi Kasus Terpadu (1 butir, skor 25)

`[C4 · 25]` — butir utuh C4; skor dan level Bloom tiap sub-butir tertulis dalam kurung.

### Indeks Baru Katalog Perpustakaan Digital

Tim TI perpustakaan sebuah universitas mengganti mesin indeks pencarian katalog digital. Tim menyusun 36 kueri uji, lalu menjalankan setiap kueri sekali pada indeks lama dan sekali pada indeks baru, di server yang sama dan di luar jam layanan; urutan pengujian diacak dan *cache* dikosongkan sebelum setiap kueri.

| Variabel | Contoh isi |
|---|---|
| `waktu_lama_ms`, `waktu_baru_ms` | waktu respons pada indeks lama dan indeks baru (ms) |
| `kesulitan_kueri` | mudah / sedang / sulit — penilaian pustakawan sebelum pengujian |
| `ditemukan_baru` | ya / tidak — apakah buku yang dicari muncul di 10 hasil teratas indeks baru |

**Ringkasan waktu respons** (n = 36 kueri):

| | Rata-rata | Simpangan baku |
|---|---|---|
| Indeks lama | 412 ms | 95 ms |
| Indeks baru | 381 ms | 90 ms |
| Selisih per kueri, d = lama − baru | 31 ms | 48 ms |

Histogram selisih d agak menceng kanan tanpa pencilan ekstrem (kemencengan 0,7). **Sebelum** pengujian, tim menetapkan bahwa penurunan rata-rata **sedikitnya 50 ms** dianggap bermakna bagi pengguna. Migrasi ke indeks baru memerlukan biaya lisensi tahunan dan pelatihan staf.

**D1.** Draf laporan tim memuat tiga ringkasan di bawah. Terapkan konsep skala pengukuran pada setiap ringkasan: tentukan skala variabelnya dan apakah ringkasan itu sah; untuk yang tidak sah, tuliskan pengganti yang sah. Jawab pada tabel isian di bawah. *(2 poin · C3)*

- (i) "Simpangan baku `kesulitan_kueri` = 0,8 (mudah = 1, sedang = 2, sulit = 3)."
- (ii) "Koefisien variasi `waktu_baru_ms` = 90/381 = 24%."
- (iii) "Median `ditemukan_baru` = ya (30 dari 36 kueri)."

| Ringkasan | Skala variabel | Sah? | Pengganti yang sah (bila tidak sah) |
|---|---|---|---|
| (i) | | | |
| (ii) | | | |
| (iii) | | | |

**D2.** Apakah rancangan ini berpasangan atau dua sampel bebas? Beri alasan dari cara data dikumpulkan. Bila kedua kolom waktu dianalisis sebagai dua sampel bebas, t Welch-nya 1,42. Analisis apakah t itu sesuai untuk data ini: variasi apa yang masuk ke penyebutnya, dan apa yang terjadi pada variasi itu bila data dianalisis sesuai rancangannya? Jawab dalam paling banyak 2 kalimat. *(3 poin · C4)*

**D3.** Nyatakan H₀ dan H₁ dalam notasi parameter yang sesuai dengan rancangan pada D2 (mis. μ_d atau μ₁ − μ₂). Analisis arah uji yang tepat untuk keputusan migrasi beserta alasannya, dan mengapa arah itu harus ditetapkan sebelum melihat data. Tetapkan α dengan menghubungkannya pada konsekuensi galat Tipe I dan Tipe II dalam konteks ini. Jawab dalam paling banyak 2 kalimat di luar notasi. *(4 poin · C4)*

**D4.** Sebutkan dua asumsi uji yang Anda pilih beserta cara memeriksa tiap asumsi. Dengan informasi histogram selisih, analisis apakah n = 36 memadai agar uji-t layak, dengan merujuk Teorema Limit Pusat. Jawab dalam paling banyak 2 kalimat. *(4 poin · C4)*

**D5.** Hitung statistik uji beserta derajat bebasnya, tentukan batas *p-value* dari tabel-t, ambil keputusan pada α pilihan Anda di D3, dan tafsirkan *p-value* itu dengan benar dalam satu kalimat. *(4 poin · C3)*

**D6.** Hitung interval kepercayaan 95% untuk parameter yang Anda uji di D3 dan tafsirkan dalam konteks. *(3 poin · C3)*

**D7.** Hitung Cohen's d yang sesuai dengan rancangan pada D2 dan tentukan besarnya menurut kategori Cohen. Dengan kriteria tim (sedikitnya 50 ms) dan interval di D6, analisis apakah penurunan itu bermakna secara praktis. Jawab dalam paling banyak 2 kalimat di luar hitungan. *(3 poin · C4)*

**D8.** Kepala perpustakaan menulis dalam laporannya: *"Indeks baru akan mempercepat pencarian bagi seluruh pengguna katalog."* Analisis mengapa pernyataan itu melampaui studi ini dengan merujuk cara data diperoleh, lalu tuliskan rumusan kesimpulan yang didukung data. Jawab dalam paling banyak 2 kalimat. *(2 poin · C4)*

---

**— Selesai. Periksa kembali satuan, pembulatan, dan rumusan H₀/H₁, lalu cocokkan jawaban Anda dengan [pembahasan dan pedoman skor](latihan-uas-pembahasan.md). Materi Minggu 1–7 dapat diulang lewat [Latihan UTS](latihan-uts.md). —**

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
