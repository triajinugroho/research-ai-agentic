---
id: uai-inf-audit-menyeluruh-2026-10
tipe: analisis-strategis
judul: Audit Menyeluruh Repositori Materi Kuliah — Oktober 2026
kode_mk: PRODI-IF
nama_mk: Seluruh paket mata kuliah
prodi: Informatika
versi: 1.3
status: draft
diperbarui: 2026-10-07
kriteria_lam: [1-budaya-mutu, 2-relevansi-pendidikan, 5-akuntabilitas]
tahap_ppepp: [E-evaluasi, P3-pengendalian]
siklus: 2026-2027-ganjil
---

# Audit Menyeluruh Repositori — Oktober 2026

**Pemilik:** Tri Aji Nugroho, S.T., M.T. · **Tanggal audit:** 7 Oktober 2026 · **Status:** draf untuk telaah dosen

> **Pembaruan v1.3 (7 Oktober 2026).** Status setiap temuan laporan ini kini **dilacak di [`KENDALI-EKSEKUSI.md`](KENDALI-EKSEKUSI.md)** — ceklis eksekusi bertanggal dengan ID butir, tenggat, ketergantungan keputusan, dan bukti commit. Laporan ini tetap menjadi rujukan temuan; tabel status di §8 dan §9 tidak lagi diperbarui. Angka validator di §3.2 dan §7.2 dimutakhirkan (837 pelanggaran dari 547 berkas).

> **Pembaruan v1.2 (7 Oktober 2026).** Repositori disusun ulang per semester kurikulum (commit `d339d8a`, `f7904f1`).
>
> - Setiap folder MK kini berada di `mata-kuliah/semester-N/<slug>/` sesuai semester registri.
> - Dua MK kurikulum lama tanpa padanan aktif (IF3XXX, IF2206) dipindah ke [`mata-kuliah/arsip/`](../arsip/README.md).
> - Dokumen meta dipindah ke [`mata-kuliah/00-meta/`](README.md): dua laporan audit (termasuk laporan ini) dan dua `prompt-*.md`.
> - Tautan relatif ditulis ulang otomatis. V10 turun dari 20 ke 6, dan 14 tautan IF2206 yang putus ikut diperbaiki.
> - Rekayasa Perangkat Lunak (`IF52520011`) ditempatkan di [`semester-4/rekayasa-perangkat-lunak/`](../semester-4/rekayasa-perangkat-lunak/README.md). Atas keputusan dosen, **penyusun materi** tetap **Tri Aji Nugroho, S.T., M.T.**, sedangkan **pengampu menurut registri** adalah **Dr. Ir. Winangsari Pradani, M.T.** Keterangan ini tercantum di README, RPS, RTM, dan halaman depan buku ajarnya.
>
> Path dalam teks laporan ini sudah disesuaikan, dan tabel §3.1 kini mencatat status arsip. Cakupan audit tetap 536 berkas seperti pada v1.0–v1.1. Setelah penataan, `mata-kuliah/` memuat 547 berkas `.md`: 536 berkas tersebut, laporan ini, 8 README peta semester, serta README `00-meta/` dan `arsip/`.

> **Pembaruan v1.1 (7 Oktober 2026).** Tabel konversi nilai resmi UAI diterima dari dosen pengampu dan sudah diterapkan ke seluruh repositori: A ≥ 81,00; sembilan huruf (A, A−, B+, B, B−, C+, C, D, E); lulus minimal C (55,00). Skala sementara tujuh huruf (A ≥ 81, lulus ≥ 56) yang dipakai pada v1.0 sudah tidak berlaku. Validator kini menegakkannya lewat aturan V13.

> **Cakupan dan metode.** Seluruh 536 berkas di `mata-kuliah/` beserta `tools/validasi-obe.py`: 10 folder mata kuliah dan 2 lapisan rujukan. Audit dikerjakan dalam lima jalur paralel: (1) perencanaan dan asesmen Dasar AI/ML, (2) konten dan uji-jalan kode Dasar AI/ML, (3) tiga MK kurikulum baru lainnya, (4) enam MK kurikulum lama, (5) lapisan tata kelola. Setiap temuan KRITIS diverifikasi ulang secara independen. Kode dijalankan pada scikit-learn 1.5–1.9, pandas 2.3–3.0, SciPy 1.18, dan Matplotlib 3.11.
>
> Acuan kebenaran: registri [Kurikulum Informatika 2025 Revisi 2026](../00-kurikulum-if-2025-revisi-2026/README.md) untuk substansi kurikulum, [Pedoman OBE](../00-pedoman-obe/pedoman-obe-konvensi.md) untuk konvensi repositori, dan [registri konversi nilai](../00-pedoman-obe/konversi-nilai.md) untuk skala nilai.

---

## 1. Jawaban Singkat

| Pertanyaan | Jawaban |
|------------|---------|
| **Apakah Dasar AI/ML (IF52510031) sudah benar-benar siap?** | **Belum.** Rancangan dan materinya kuat dan setia pada registri: Sub-CPMK, CPMK, CPL, BK, SKS, dan bobot 5/25/35/20/15 cocok. Namun ada empat penghambat: (1) belum ada naskah UTS/UAS/kuis maupun kunci jawabannya, padahal UTS di Minggu 8 tinggal beberapa minggu; (2) enam lab menghasilkan angka yang **berlawanan** dengan pelajaran yang hendak ditunjukkannya; (3) pengaitan asesmen ke Sub-CPMK tidak sesuai materi registri, sehingga angka ketercapaian CPL akan menyimpang; (4) RPS belum disahkan dan belum memiliki bukti mutu (`mutu/`, *front-matter*). |
| **Skala nilai sudah sesuai standar UAI (A ≥ 81)?** | **Sekarang sudah.** Sebelum audit ditemukan sedikitnya delapan varian skala, dan tidak satu pun sama dengan tabel resmi. Tabel resmi UAI kini ditetapkan di satu tempat ([`konversi-nilai.md`](../00-pedoman-obe/konversi-nilai.md) v2.0): A ≥ 81,00; sembilan huruf; lulus minimal C (55,00). Tabel itu sudah diterapkan ke RPS, kerangka asesmen, pedoman praktikum, rubrik, soal UTS + kunci, dan contoh kode di **kesepuluh folder MK**. Aturan validator V13 akan menangkap bila skala lain muncul lagi. |
| **Apakah semua referensi formal sudah tersedia?** | **Belum lengkap.** Yang ada adalah transkripsi registri kurikulum (final sampai sheet 15c), pedoman OBE internal, dan kini **tabel resmi konversi nilai UAI**: rentang, huruf, dan kategori ✅ (urutan B/B− pada tabel yang diterima tertukar dan dibetulkan atas konfirmasi dosen). Yang masih 🟡/🔲: bobot nilai mutu (sementara memakai bobot umum), nama/nomor dokumen resminya, dan aturan pembulatan. Halaman UAI Helpdesk tentang sistem penilaian tidak dapat diakses dari lingkungan audit. Daftar dokumen yang perlu dikumpulkan ada di §10. |

---

## 2. Perbaikan yang Sudah Dilakukan pada Audit Ini

| Commit | Isi |
|--------|-----|
| `2fddc79` | Registri tunggal [`konversi-nilai.md`](../00-pedoman-obe/konversi-nilai.md); skala 9 huruf (A ≥ 85, A−, B−, lulus ≥ 55) di RPS dan kerangka asesmen **Dasar AI/ML, Probabilitas dan Statistik, Teknopreneur** diganti skala sementara (A ≥ 81, 7 huruf, lulus ≥ 56) — *digantikan skala resmi pada `8f09bc0`* |
| `fd1560e` | **Dasar AI/ML:** bobot 13 lab disesuaikan agar tepat 15% / 10% sesuai registri (sebelumnya 15,2% / 9,5%); soal contoh UTS B3 yang mustahil secara aritmetika dibetulkan; aturan alat bantu ujian di Lampiran diselaraskan dengan enam dokumen lain; fakta yang keliru terhadap registri dikoreksi (bukan satu-satunya MK AI wajib, Sains Data semester 4, Basis Data semester 3, nama MK prasyarat, Tugas Akhir semester 8); catatan koordinasi dengan Sains Data ditambahkan |
| `6a4d789` | **Probabilitas dan Statistik:** total bobot lab 25,08% → 25%; tiga blok kode yang gagal pada SciPy 1.18 / Matplotlib 3.11 diperbaiki (`kstest`, `boxplot(labels=)`, `np.sqrt(2**64)`) |
| `b37ec23` | Rumusan verbatim CPMK **Teknopreneur** ("Lima CPMK" padahal enam; tiga rumusan terpotong) dan tabel CPL **Metodologi Penelitian** (memuat rumusan CPMK sebagai CPL, ranah salah) dipulihkan dari registri |
| `e5f88e3` | Pedoman OBE §I butir 10 dan §K menautkan registri konversi nilai; laporan ini (v1.0) |
| `8f09bc0` | Registri [`konversi-nilai.md`](../00-pedoman-obe/konversi-nilai.md) v2.0: **tabel resmi UAI** (9 huruf, A ≥ 81,00, lulus C 55,00), status sumber per aspek |
| `e10654c` | Skala resmi diterapkan ke **10 folder MK** (52 berkas): tabel kebijakan, ambang lulus, rubrik yang memetakan skor ke huruf, soal UTS INF-101 no. 11 beserta kunci dan pembahasannya, serta contoh kode konversi nilai di modul, buku ajar, dan lab. Kedua `prompt-*.md` kini menyematkan tabel resmi. Aturan validator **V13** ditambahkan (Pedoman §Q). Laporan ini menjadi v1.1 |
| `d339d8a` | **Penataan per semester** (pemindahan mekanis dengan `git mv`, tanpa perubahan isi materi; pengecualian path di validator disesuaikan): folder MK ke `semester-N/` sesuai registri, IF3XXX dan IF2206 ke `arsip/`, `AUDIT-*.md` dan `prompt-*.md` ke `00-meta/`. Sebanyak 199 tautan relatif di 76 berkas ditulis ulang, termasuk 14 tautan IF2206 yang sebelumnya putus. V10: 20 → 6 |
| `f7904f1` | README peta mata kuliah untuk `semester-1/` … `semester-8/` dari registri `11`: kode, SKS, pengampu menurut registri, folder materi, dan catatan penyusun materi |
| `3f93e43` | Spanduk arsip dan README [`arsip/`](../arsip/README.md) serta [`00-meta/`](README.md); keterangan **penyusun materi: Tri Aji Nugroho, S.T., M.T.; pengampu (registri): Dr. Ir. Winangsari Pradani, M.T.** pada RPL; path dalam teks diperbarui di registri, pedoman, dan laporan ini. Laporan ini menjadi v1.2 |

---

## 3. Peta Repositori

### 3.1 Sepuluh Folder Mata Kuliah

| Folder | Kode lama → kode resmi | SKS | Sem | Pengampu menurut registri | Kesiapan | Arah |
|--------|------------------------|:---:|:---:|---------------------------|----------|------|
| [`semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/`](../semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/) | — → `IF52510031` | 3 | V | Tri Aji Nugroho, S.T., M.T. | **Belum siap** | Tuntaskan Tahap 0 (§8) sebelum UTS |
| [`semester-1/probabilitas-dan-statistik/`](../semester-1/probabilitas-dan-statistik/) | — → `IF52510033` | 3 | I | Tri Aji Nugroho, S.T., M.T. | Siap dengan perbaikan | Naskah UTS + kunci; CSV lab; pengaitan Sub-CPMK |
| [`semester-5/teknopreneur/`](../semester-5/teknopreneur/) | — → `ST52510002` | 3 | V | Tri Aji Nugroho, S.T., M.T. | Siap dengan perbaikan | Persetujuan prodi untuk syarat lulus tambahan; label teknik; sitasi hukum |
| [`semester-7/metodologi-penelitian/`](../semester-7/metodologi-penelitian/) | — → `IF52510021` | 2 | VII | **Andi Arniaty Arsyad, Ph.D.** | Belum siap | Pengesahan, pemetaan Sub-CPMK, dan rubrik — keputusan pada pengampu (skala nilai sudah diselaraskan, v1.1) |
| [`semester-2/algoritma-pemrograman/`](../semester-2/algoritma-pemrograman/) | INF-101 → `IF52520004` | 2 | II | Tri Aji Nugroho, S.T., M.T. | Pilot OBE v2.0 tuntas, **tetapi pada skema yang sudah digantikan** | Selaraskan ulang sebelum Genap 2026/2027 |
| [`semester-2/praktikum-algoritma-pemrograman/`](../semester-2/praktikum-algoritma-pemrograman/) | INF-102 → `IF52520005` | 1 | II | Tri Aji Nugroho, S.T., M.T. | Skema lama; bobot rubrik salah salin | Selaraskan ulang |
| [`semester-2/analisis-data-statistik/`](../semester-2/analisis-data-statistik/) | TBD-STAT → `IF52520025` | **2 → 3** | II | Tri Aji Nugroho, S.T., M.T. | Skema lama; 55 berkas tanpa *footer* | Selaraskan ulang **berat**: tambah SKS dan pisahkan dari Probabilitas dan Statistik |
| [`semester-4/rekayasa-perangkat-lunak/`](../semester-4/rekayasa-perangkat-lunak/) | IF2205 → `IF52520011` | 3 | IV | **Dr. Ir. Winangsari Pradani, M.T.** (penyusun materi: Tri Aji Nugroho, S.T., M.T.) | Skema lama | ~~Serahkan ke pengampu baru atau arsipkan sebagai rujukan~~ **Diputuskan (v1.2):** tetap di repositori, ditempatkan di semester 4 dengan keterangan penyusun materi vs pengampu registri; selaraskan ke registri bersama pengampu |
| [`arsip/praktikum-rekayasa-perangkat-lunak/`](../arsip/praktikum-rekayasa-perangkat-lunak/) | IF2206 → **tidak ada** | 1 | — | — | ~~14 tautan putus~~ **Diarsipkan (v1.2)**; 14 tautan sudah diperbaiki (`d339d8a`) | ~~Arsipkan~~ Sudah diarsipkan; peleburan ke RPL / Proyek PL / Pengujian PL menunggu prodi |
| [`arsip/kecerdasan-buatan-machine-learning/`](../arsip/kecerdasan-buatan-machine-learning/) | IF3XXX → digantikan `IF52510031` | 4 | — | — | **Diarsipkan (v1.2)**; kode Keras 3 / sklearn 1.6 sebagian rusak | ~~Arsipkan~~ Sudah dipindah ke `arsip/` dengan spanduk pada README dan RPS; `status: arsip` **belum diterapkan** (berkas materi arsip belum ber-*front-matter*); dipakai sebagai bank konten untuk JST, NLP, dan Pengolahan Citra |

Path folder relatif terhadap `mata-kuliah/` (susunan per semester sejak v1.2). Kolom *Pengampu menurut registri* mengikuti [registri `11`](../00-kurikulum-if-2025-revisi-2026/11-susunan-mata-kuliah-dan-dosen.md). Seluruh materi di kesepuluh folder disusun oleh Tri Aji Nugroho, S.T., M.T., termasuk Rekayasa Perangkat Lunak dan Metodologi Penelitian yang pengampu registrinya berbeda.

### 3.2 Lapisan Rujukan

| Lapisan | Kondisi | Masalah utama |
|---------|---------|---------------|
| [`00-kurikulum-if-2025-revisi-2026/`](../00-kurikulum-if-2025-revisi-2026/) | Transkripsi registri resmi, final sampai sheet 15c. Bobot Sub-CPMK seluruh 58 MK dan 154 Sub-CPMK konsisten secara aritmetika. | Ada beberapa ketidakcocokan internal yang perlu **dilaporkan ke tim kurikulum, bukan diubah diam-diam** (§7.3) |
| [`00-pedoman-obe/`](../00-pedoman-obe/) | v2.0, disusun untuk enam MK lama | **Bertabrakan dengan registri** pada kode BK, model CPMK, format Sub-CPMK, dan kode asesmen. Keduanya sama-sama mengklaim sebagai acuan tertinggi (§7.1) |
| [`tools/validasi-obe.py`](../../tools/validasi-obe.py) | Berjalan; **837 pelanggaran** (v1.3; 851 saat audit awal) | Hanya mengenali INF-101 sebagai mata kuliah; tidak memahami skema kode registri (§7.2) |

---

## 4. Dasar AI/ML (IF52510031) — Temuan yang Masih Terbuka

### 4.1 KRITIS — tuntaskan sebelum UTS

**K1. Belum ada naskah ujian dan kunci.** `05-assessments/` hanya berisi kisi-kisi. Kisi-kisi itu belum memuat cetak biru butir (nomor butir × indikator × Bloom × Sub-CPMK × skor). Contoh UAS C2 sama dengan Latihan 5 Bab 12, sedangkan [`00-halaman-depan.md`](../semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/06-buku-ajar/00-halaman-depan.md) menyatakan Latihan Soal "dapat dipakai langsung sebagai bank soal ujian". Artinya mahasiswa sudah memegang soalnya. Hal yang sama berlaku untuk kuis K-01…K-04.

**K2. Enam lab menunjukkan kebalikan dari pelajarannya.** Semuanya berjalan tanpa galat, tetapi angka yang dihasilkan bertentangan dengan teks lab. Hasilnya sama pada tiga *seed* berbeda, jadi ini bawaan desain data, bukan kebetulan.

| Lab | Minggu | Apa yang terjadi | Arah perbaikan |
|-----|:------:|------------------|----------------|
| [14 — Audit bias](../semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/04-labs/lab-14-audit-bias-dan-model-card.md) | 14 | Setelah kolom `wilayah` dibuang, selisih *recall* antarwilayah turun dari **0,704 ke 0,061**, tetapi kode tetap mencetak teks tetap "Ketimpangan TIDAK hilang". *Recall* keseluruhan hanya ±5%. Papua, kelompok terkecil, justru mendapat *recall* terbaik. *(diverifikasi ulang)* | Beri data fitur proksi yang berkorelasi dengan `wilayah`; pakai `class_weight` atau ambang yang sesuai; jadikan kalimat kesimpulan bergantung pada hasil hitung |
| [13 — JST](../semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/04-labs/lab-13-jaringan-saraf-tiruan.md) | 13 | Pada perbandingan utama, MLP mendapat ROC-AUC CV **0,443** (lebih buruk dari acak). Penyebabnya, `early_stopping` memantau akurasi pada data 11% positif sehingga berhenti di iterasi ±12. *(diverifikasi ulang)* | Pakai konfigurasi Langkah 4 (`n_iter_no_change=20`); tambahkan catatan di Bab 12 |
| [04 — Kebocoran](../semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/04-labs/lab-04-validasi-silang-deteksi-kebocoran.md) | 4 | Hanya kebocoran `nomor_invoice` yang terlihat. Pembagian berkelompok (+0,0002) dan pembagian temporal (−0,005) tidak berdampak, dan penskalaan tidak berpengaruh pada Random Forest. Mahasiswa bisa menyimpulkan bahwa pembagian berkelompok dan temporal tidak penting. | Tambah efek acak per pelanggan dan *drift* waktu; tunjukkan kebocoran seleksi fitur dengan banyak fitur derau |
| [03 — Pipeline](../semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/04-labs/lab-03-pipeline-prapemrosesan.md) | 3 | AUC versi bocor (0,5718) **lebih rendah** daripada versi *Pipeline* (0,5722), padahal mahasiswa diminta menjelaskan "mengapa cara pertama lebih tinggi". `roc_auc_score(...).round(4)` juga gagal pada sklearn ≥ 1.7 (pola yang sama ada di `week-11`). | Rancang ulang demonstrasi; ganti `.round()` dengan `round()` |
| [11 — Clustering](../semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/04-labs/lab-11-clustering-dan-metriknya.md) | 11 | Membandingkan ID klaster mentah K-Means dengan Hierarchical: tercatat 30 dari 34 provinsi "berbeda", padahal yang sebenarnya berbeda hanya 6 (ARI 0,57) | Selaraskan label dengan `linear_sum_assignment`, atau laporkan ARI |
| [09 — Pohon keputusan](../semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/04-labs/lab-09-pohon-keputusan-dan-ensemble.md) | 9 | Pohon kedalaman 3 yang "dapat dijelaskan kepada nasabah" memprediksi *Lancar* di setiap daun (F1 = 0) | Atur data atau `class_weight` agar pohon dangkal bermakna |

Selain itu, [Lab 10](../semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/04-labs/lab-10-svm-naive-bayes-penyetelan.md) melanggar aturan kebocoran #6 milik mata kuliah sendiri: SVM hasil penyetelan "dibandingkan secara adil" pada lipatan yang sama dengan lipatan yang dipakai untuk memilihnya. Perbaikannya, gunakan CV bersarang.

**K3. Pengaitan asesmen ke Sub-CPMK tidak sesuai materi registri.** Registri mengaitkan satu teknik ke satu Sub-CPMK: UTS → `102-1`, UAS → `082-1`. Isi ujian tidak mengikuti pembagian itu:

- Sekitar 23% isi UTS adalah formulasi masalah, yang termasuk `082-1`.
- UAS memuat PCA, kurva pembelajaran, dan *fairness*, yang menurut registri termasuk `102-1`.
- Minggu 6, 7, 11, dan 14 di RPS ditandai `082-1`, padahal metrik, metrik *clustering*, visualisasi, dan *bias/fairness* tercantum di Materi `102-1`.
- Lab 14 ditandai `102-1` di RTM dan lab, tetapi `082-1` di RPS.

Akibatnya, ketercapaian CPL yang dihitung dari nilai ini tidak sahih. **Pilihan:** (a) tandai setiap butir ujian dengan Sub-CPMK dan hitung ketercapaian per butir; atau (b) usulkan revisi alokasi teknik kepada tim kurikulum. Pola yang sama terjadi pada Probabilitas dan Statistik, Teknopreneur, dan Metodologi Penelitian, jadi ini isu tingkat registri.

**K4. Level Bloom ujian di bawah level Sub-CPMK.** UTS bagian A (30%) berisi soal "Sebutkan/Jelaskan" (C1–C2), padahal `102-1` menuntut C3–C4. Sekitar 55% UAS berada di bawah C4, padahal `082-1` menuntut C4–C6.

### 4.2 TINGGI

| # | Temuan | Lokasi |
|---|--------|--------|
| T1 | RPS belum disahkan: tabel pengesahan kosong dan nama Koordinator Rumpun R06 belum diisi. Syarat lulus tambahan (capaian tiap Sub-CPMK ≥ 50%; wajib proyek dan presentasi) dapat membuat mahasiswa dengan nilai akhir ≥ 55,00 tidak lulus, sehingga **perlu persetujuan prodi** ([`konversi-nilai.md` §C](../00-pedoman-obe/konversi-nilai.md)) | RPS §I, §N; kerangka asesmen §6.1 |
| T2 | Teori *fairness* keliru. Kleinberg dkk. (2016) membuktikan konflik antara **kalibrasi** dan keseimbangan galat, bukan antara *demographic parity*, *equal opportunity*, dan *equalized odds*. Klaim "tidak ada model yang memenuhi semuanya" juga salah, karena pengklasifikasi konstan memenuhi ketiganya. | `bab-13`, `week-14`, `lab-14` |
| T3 | Lab 4–14 tidak punya bagian **Persiapan** dan tidak meminta mahasiswa menjalankan sel pembuka, sehingga Langkah 1 gagal dengan `NameError: RANDOM_STATE` | `04-labs/lab-04` … `lab-14` |
| T4 | Klaim "data nyata berkonteks Indonesia" tidak sesuai kenyataan: 10 dari 13 lab memakai data sintetis. Lab 9 ("Data Nyata") dan Lab 13 ("data tabular nyata") dibangkitkan dengan `rng`. RPS Minggu 3 menjanjikan "dataset BPS", tetapi Lab 3 sintetis. Lab 11 memakai 34 provinsi tanpa sumber dan tahun. | RPS, RTM, `datasets/README.md`, `mengapa-buku-ini.md` |
| T5 | Belum ada bukti mutu: tanpa `mutu/`, tanpa *front-matter* di 57 berkas, tanpa tabel migrasi, tanpa formulir penilaian kontribusi anggota kelompok. Validator membalas "tidak ditemukan" untuk `--mk IF52510031`. | seluruh folder |
| T6 | **Sains Data (IF52520026, semester 4) berstatus *Core*, memakai CPMK082 dan CPMK102 yang sama, dan ditempuh *sebelum* mata kuliah ini.** Tumpang tindih Minggu 2–7 hampir pasti terjadi. Perlu kesepakatan tertulis dengan dosen pengampu Sains Data; catatan koordinasinya sudah ditambahkan di RPS §M.3. | RPS §M |

### 4.3 SEDANG

- **Sanksi tidak konsisten.** Untuk notebook yang tidak dapat dijalankan ulang, sanksinya −20% di satu dokumen dan "skor maksimum 2" di dokumen lain. Untuk analisis keterbatasan yang hilang, ada tiga sanksi bertumpuk: nilai nol, −15%, dan level 1. Kerangka asesmen menyebut "seluruh penilaian memakai skala 1–4", tetapi kuis memakai 40/60.
- **Status lab tidak jelas: dikerjakan di kelas atau di rumah?** Partisipasi 0% dibenarkan dengan alasan "lab dikerjakan di dalam kelas", tetapi tenggat lab jatuh pada pertemuan minggu berikutnya.
- **Beban belajar:** setiap modul merencanakan 330 menit per minggu, padahal RPS/RTM menetapkan 510 menit untuk 3 SKS.
- **Urutan materi:** P-03 (Minggu 14, bobot 15%) menuntut audit *bias* dan *model card* yang baru diajarkan pada minggu yang sama. Minggu 15 hanya muat ±5 kelompok dalam 150 menit.
- **Kunci jawaban** belum ada untuk 154 butir Latihan Soal, termasuk yang numerik. Hasil hitung manual *backprop* di Bab 12 berbeda pembulatan dengan keluaran kode lab, sehingga berisiko saat dijadikan kunci UAS.
- **Rumus pembanding model √(s₁²+s₂²)** mengabaikan bahwa lipatan berpasangan dan membandingkan dengan SD, bukan SE. Ganti dengan rerata dan SD selisih per lipatan.
- **Bloom Bab 4–5 (C5–C6)** melampaui plafon `102-1` (C3–C4). Pemetaan level UNESCO di halaman depan menyimpang dari Pedoman OBE §P.
- **Sitasi:** temuan Kapoor & Narayanan (2023) dikutip keliru. Makalah itu menghimpun kebocoran pada 294 makalah di 17 bidang dari tinjauan terdahulu, bukan "meninjau 294 makalah dan menemukan kebocoran di sebagian besar". UNESCO (2024) perlu diganti versi 16 Januari 2026 [REG-9]. CS2023 perlu mencantumkan AAAI.
- **Klaim "verbatim dari registri"** tidak tepat, karena Kriteria dan Materi Sub-CPMK diterjemahkan. Gunakan frasa "diadaptasi dari", atau salin persis.
- **Daftar larangan AI** berisi 6 butir di RPS dan kerangka asesmen, tetapi 4 butir di RTM, rubrik, dan buku.

---

## 5. Tiga MK Kurikulum Baru Lainnya

| MK | Sudah baik | Masih perlu dikerjakan |
|----|-----------|-----------------------|
| **Probabilitas dan Statistik** (sedang berjalan, semester I) | Setia pada registri; bobot 100% konsisten; *footer* lengkap; kode lain berjalan pada pustaka terbaru | Naskah UTS + kunci sebelum Minggu 8. **8 berkas CSV lab tidak ada di repositori** ("tersedia di LMS"), ada 26 pemanggilan `read_csv`, dan peta dataset salah. Pengaitan Sub-CPMK keliru: Kuis 1 berisi deskriptif tetapi dikaitkan ke `081-1`, dan 60% UTS adalah probabilitas tetapi dikaitkan ke `102-1`. Dua rubrik proyek berbeda (5 aspek vs 7 aspek). Bab 13 bukan bab AI. |
| **Teknopreneur** | Setia pada registri, kecuali rumusan CPMK yang **sudah dipulihkan** | Syarat lulus tambahan (≥ 15 wawancara, MVP diuji ke ≥ 5 orang, *Demo Day*, ≥ 50% per Sub-CPMK) perlu persetujuan prodi. Label teknik di RPS §F keliru (studio 9–12 masuk Unjuk Kerja, bukan Observasi). Tenggat *milestone* lebih awal daripada isinya. **Sitasi hukum usang:** UU 11/2020 → UU 6/2023; UU ITE perlu mencantumkan UU 1/2024; Kominfo → Komdigi (SE Menkominfo 9/2023); fatwa DSN-MUI tanpa nomor. Belum ada pemetaan CPL09 untuk mahasiswa non-IF (statusnya MKF). |
| **Metodologi Penelitian** (pengampu: AAA) | Sub-CPMK verbatim; bobot 35/40/5/10/10 konsisten; atribusi pengampu ditandai di 29 berkas | Skala nilai **sudah diselaraskan** ke skala resmi UAI (RPS §H.6 baru; kerangka asesmen §J.1–J.2 dengan deskriptor per huruf dipertahankan; lulus C 55,00). RPS belum punya bagian Pengesahan. T3/T4/T7 (18%) dikaitkan ke Sub-CPMK yang salah. 16% nilai tidak punya rubrik. *README* utama mencantumkan Tri Aji Nugroho sebagai pengampu seluruh repositori tanpa catatan. **Keputusan perbaikan ada pada pengampu.** |

**Kesamaan keempat MK baru:**

- Tidak ada satu pun dari 228 berkas yang memiliki *front-matter*.
- Belum ada folder `mutu/`.
- Belum ada naskah ujian beserta kuncinya.
- *Anchor* tautan Lampiran rusak (*slug* judul tidak cocok).
- Struktur RPS tidak mengikuti templat A–L pada Pedoman §H: tidak ada baris Moda dan tidak ada bagian Pengukuran Ketercapaian CPL.

---

## 6. Enam MK Kurikulum Lama

| Temuan | Lokasi | Tingkat |
|--------|--------|:-------:|
| ~~Terdapat **delapan varian skala nilai** di MK lama, termasuk tiga skala berbeda di dalam INF-101 sendiri. Soal UTS INF-101 no. 11 menyebut skala tanpa C+ sebagai "standar UAI".~~ **Selesai (Oktober 2026):** semua skala mengikuti tabel resmi; soal no. 11 kini memakai skala resmi, kuncinya `A-`, dan pembahasan distraktornya diperbarui. | `semester-2/algoritma-pemrograman/04-assessments/uts-algoritma-pemrograman.md` | ~~TINGGI~~ |
| Bobot di rubrik INF-102 tersalin dari templat teori (15/10/20/25/25/5), berbeda dengan RPS-nya (25/25/35/10/5) | `semester-2/praktikum-algoritma-pemrograman/04-assessments/rubrik-tugas.md` | KRITIS (bila dipakai lagi) |
| INF-101 lulus validator dengan 0 pelanggaran, padahal 7 CPMK lokal dan 55 Sub-CPMK-nya **tidak sesuai registri** (resmi: CPMK032/033, 2 Sub-CPMK, bobot 5/25/30/20/20) | `semester-2/algoritma-pemrograman/01-rps/` | KRITIS (untuk Genap 2026/2027) |
| Materi Analisis Data Statistik (probabilitas → regresi) kini sebagian besar menjadi isi Probabilitas dan Statistik semester I | `semester-2/analisis-data-statistik/` | KRITIS (untuk Genap 2026/2027) |
| 55 dari 59 berkas ADS tanpa *footer*; buku ajar bertahun "2025"; tabel literasi AI berhenti di Bab 12–13 | `semester-2/analisis-data-statistik/06-buku-ajar/` | SEDANG |
| ~~14 tautan `../../../` putus di lab 01–04 IF2206~~ **Selesai (v1.2):** diperbaiki saat penataan per semester (`d339d8a`) | `arsip/praktikum-rekayasa-perangkat-lunak/03-modul-praktikum/` | ~~SEDANG~~ |
| Kode Keras 3 / sklearn 1.6 rusak di IF3XXX (`model.save('dir/')`, `.h5`, `mean_squared_error(squared=False)`, `ImageDataGenerator`) | `arsip/kecerdasan-buatan-machine-learning/06-buku-ajar/lampiran.md` dll. | RENDAH (diarsipkan) |
| SK LAM-INFOKOM diatribusikan ke **BAN-PT** | `00-strategic-analysis/strategic-analysis.md` di ADS, IF2205, IF3XXX; kedua `00-meta/prompt-*.md` | SEDANG |
| `AUDIT-KESELARASAN-IF2205-IF2206.md` menyatakan 13 isu selesai, padahal templat AI Usage Log masih ada 6 versi dan ada rubrik proyek ketiga di `week-15` | `00-meta/AUDIT-KESELARASAN-IF2205-IF2206.md` | RENDAH |

---

## 7. Lapisan Tata Kelola

### 7.1 Dua "sumber kebenaran" yang bertabrakan

Pedoman OBE v2.0 (§Kedudukan) dan README registri kurikulum **sama-sama** menyatakan diri berlaku bila terjadi perbedaan. Keduanya berbeda pada hal yang mendasar:

| Aspek | Pedoman OBE v2.0 | Registri Kurikulum 2025 Rev. 2026 |
|-------|------------------|-----------------------------------|
| Kode Bahan Kajian | BK01 = *Social Issues*, BK12 = *Algorithmic Foundations*, BK14 = *Programming Fundamentals* (22 BK) | **BK01 = *Artificial Intelligence***, BK02 = *Algorithmic Foundations*, BK12 = SDF, **BK14 = *Security*** (19 BK) |
| CPMK | Lokal per MK, `CPMK-1` … `CPMK-7` | Tingkat prodi, `CPMK032`, `CPMK082`, … (26 CPMK) |
| Sub-CPMK | `Sub-CPMK-3.2` | `DAIML-Sub-CPMK082-1` |
| Kode asesmen | `ASM-K1`, `ASM-UTS`, … | Enam teknik terikat Sub-CPMK (MK baru memakai skema ketiga: `K-01`, `T-01`, `P-01`) |

Akibatnya, `bk: [BK12, BK14, BK01]` di RPS INF-101 berarti "SDF, Security, AI" bila dibaca dengan kode resmi, dan validator tetap meloloskannya. **Rekomendasi:** registri mengatur seluruh substansi kurikulum. Pedoman OBE v3.0 hanya mengatur konvensi repositori yang tidak dicakup registri, yaitu metadata, status sitasi, `mutu/` dan PPEPP, *footer*, tabel migrasi, dan validator.

### 7.2 Validator

Hasil saat audit awal: **851 pelanggaran** dari 536 berkas. Hasil v1.3 (setelah penataan per semester): **837 pelanggaran** dari 547 berkas — V1 518, V4 253, V8 60, V10 6 (sisa V10 adalah contoh tautan di dalam blok kode), V13 0.

| Kode | Jumlah | Penjelasan |
|------|-------:|-----------|
| V1 | 518 | Tanpa *front-matter* |
| V4 | 253 | Kode lama `CPMK-x.y` atau `Sub-CPMK x.y` |
| V8 | 60 | Pelanggaran konvensi |
| V10 | 20 (v1.3: 6) | Tautan putus |

Hanya INF-101 yang dikenali sebagai mata kuliah, sehingga pemeriksaan V3/V5/V6/V7 **tidak pernah berjalan** untuk 9 folder lain. Pola *regex*-nya juga tidak mengenali skema registri. Validator perlu membaca kode sah langsung dari registri (`03`, `06`, `11`, `13`, `15b–e`), dan mencocokkan bobot dengan `15a`. Pemeriksaan skala nilai **sudah ada** lewat aturan baru V13 (cakupan: tabel Markdown; skala yang ditulis dalam prosa atau kode belum diperiksa mesin).

### 7.3 Ketidakcocokan di dalam registri — laporkan, jangan diubah sendiri

- **Logika Informatika:** sheet 13 mencatat CPMK032 dan CPMK081, sedangkan sheet 14/15 mencatat CPMK051 dan CPMK071. Karena itu kolom "Σ MK" pada empat CPMK di sheet 13 salah.
- **Komposisi SKS di `11`:** tertulis MKP 111 + MKPP 9, padahal tabelnya menjumlah MKP 117 (19 + 5 + 117 + 3 = 144).
- **Rentang CPMK per MK:** tertulis "2–3" atau "2–6", padahal sebenarnya 2–7.
- **Salah ketik:** `CPLUA3`; CPL08 tercantum dua kali di `07`; kode dosen ENR/ERN.
- **Catatan `91` §2 sudah usang:** masih menyebut folder Probabilitas dan Statistik serta Teknopreneur belum ada, dan menyatakan kode CPL resmi "konsisten di seluruh materi". *(v1.2: bagian folder sudah diberi catatan pembaruan bertanggal 2026-10-07 beserta path baru; klaim konsistensi kode CPL di §2.3 belum ditinjau.)*
- **Urutan semester:** Sains Data (semester 4, *Core*, *end-to-end ML*) mendahului Dasar AI/ML (semester 5).

### 7.4 Dokumen meta yang usang

> **Pembaruan v1.2:** `CLAUDE.md` dan `README.md` akar sudah ditulis ulang (susunan per semester, jumlah berkas aktual, kode resmi, rujukan ke registri, validator, dan bobot dari `15a`). Kedua prompt sudah memakai lokasi `mata-kuliah/semester-N/` dan tabel skala resmi, tetapi bagian lainnya (kode Sub-CPMK lama, atribusi BAN-PT) masih menunggu Fase 2.5. Butir di bawah dipertahankan sebagai catatan temuan awal.

- **`CLAUDE.md`:**
  - menyebut "179+ dokumen" dan "4–6 mata kuliah" (kenyataannya 536 berkas dan 10 MK);
  - jalurnya masih `mata kuliah/` dengan spasi;
  - bobot asesmen dan klaim "7 CPMK per MK" masih versi lama;
  - tidak menyebut registri kurikulum maupun validator.
- **Kedua `00-meta/prompt-*.md`:** masih membangkitkan kode Sub-CPMK gaya lama (nomor CPMK dan urutan tanpa prefiks) dan atribusi BAN-PT, sehingga regenerasi konten akan memasukkan kembali kesalahan lama. Ini adalah Fase 2.5 Pedoman, yang **belum dikerjakan**.
- **`ROADMAP-ENHANCEMENT.md` (RPL dan PRPL):** masih berstatus "✅ Complete" per April 2026 dan belum menyadari adanya kurikulum baru.

---

## 8. Arah Perbaikan Menyeluruh

**Prinsip:** *registri mengatur isi, repositori menghasilkan bukti.* Nilai tertinggi repositori ini bukan banyaknya berkas, melainkan kemampuannya membuktikan rantai PL → CPL → CPMK → Sub-CPMK → butir asesmen → nilai → ketercapaian, sehingga dapat diperiksa mesin dan asesor. Kemampuan itulah yang dicari oleh kriteria 1 dan 5 LAM-INFOKOM 2.0, yang membedakan "Baik Sekali" dari "Unggul".

### Tahap 0 — Darurat (sebelum UTS Minggu 8)

| # | Pekerjaan | MK |
|---|-----------|----|
| 0.1 | Naskah UTS + kunci + pedoman skor, dengan **setiap butir bertanda Sub-CPMK dan Bloom (≥ C3)**, tanpa memakai ulang Latihan Soal buku | Dasar AI/ML, Probabilitas dan Statistik |
| 0.2 | Naskah kuis berikutnya beserta kuncinya | Dasar AI/ML (K-02, K-03, K-04) |
| 0.3 | Unggah atau tautkan 8 CSV lab | Probabilitas dan Statistik |
| 0.4 | Tambahkan bagian Persiapan ("jalankan sel pembuka Lampiran D") di Lab 4–14 | Dasar AI/ML |
| 0.5 | Ajukan syarat lulus tambahan ke prodi, atau cabut | Dasar AI/ML, Teknopreneur |

### Tahap 1 — Sebelum minggu pelaksanaannya / akhir Ganjil 2026/2027

| # | Pekerjaan |
|---|-----------|
| 1.1 | Rancang ulang data Lab 9, 10, 11, 13, 14 sebelum minggunya tiba (Lab 3 dan 4 untuk siklus berikut), lalu tambahkan **pemeriksaan otomatis**: setiap lab memuat `assert` atas hasil yang diharapkan, agar kontradiksi seperti di §4.1 K2 tertangkap sebelum sampai ke kelas |
| 1.2 | Koreksi teori *fairness* (Bab 13, Minggu 14, Lab 14) dan rumus pembanding model |
| 1.3 | Naskah UAS + kunci; kunci 154 Latihan Soal (atau tandai sebagian sebagai bank soal tertutup) |
| 1.4 | `mutu/` (peta mutu, pengukuran ketercapaian **per butir**, log PPEPP) dan *front-matter* untuk empat MK baru, agar evaluasi minggu 17 menghasilkan bukti |
| 1.5 | Kesepakatan tertulis pembagian materi dengan pengampu Sains Data dan JST |
| 1.6 | Sitasi hukum Teknopreneur |

### Tahap 2 — Sebelum Genap 2026/2027 (Februari 2027)

| # | Pekerjaan |
|---|-----------|
| 2.1 | **Pedoman OBE v3.0:** urutan otoritas (Excel resmi > registri > pedoman > `CLAUDE.md`/prompt); ganti registri BK lama dengan BK registri; format kode CPMK/Sub-CPMK/asesmen mengikuti registri |
| 2.2 | **Validator v3:** baca kode, bobot, dan SKS dari registri; kenali kode `XX-Sub-CPMKnnn-n`; perluas V13 ke skala dalam kode/prosa; jalankan kode lab |
| 2.3 | **Selaraskan ulang tiga MK semester II** ke registri: Algoritma Pemrograman `IF52520004` (2 Sub-CPMK; bobot 5/25/30/20/20; pisahkan dari Dasar Pemrograman semester I), Praktikum `IF52520005` (bobot 5/5/50/20/10/10), Analisis Data Statistik `IF52520025` (**3 SKS**; bobot 15/25/10/25/25; fokus pada akuisisi, kualitas data, EDA, dan analitik berbantuan AI yang tervalidasi — bukan mengulang Probabilitas dan Statistik) |
| 2.4 | ~~Arsipkan `kecerdasan-buatan-machine-learning/` dan `praktikum-rekayasa-perangkat-lunak/` (`status: arsip` + spanduk), serahkan `rekayasa-perangkat-lunak/` kepada pengampu baru~~ **Selesai sebagian (v1.2):** kedua folder sudah dipindah ke `arsip/` dan diberi spanduk arsip, tetapi spanduk baru ada pada README dan RPS masing-masing folder (4 dari 80 berkas materi arsip: 57 + 23; indeks `arsip/README.md` tidak dihitung). `semester-4/rekayasa-perangkat-lunak/` tetap di repositori dengan keterangan penyusun materi: Tri Aji Nugroho, S.T., M.T.; pengampu (registri): Dr. Ir. Winangsari Pradani, M.T. **Sisa pekerjaan:** (a) ~~`status: arsip`~~ — ditutup oleh kebijakan: berkas arsip sengaja tidak diberi *front-matter* dan ditandai spanduk ([`arsip/README.md`](../arsip/README.md), Ketentuan Arsip); (b) penyelarasan RPL ke registri `IF52520011` masih perlu dikoordinasikan dengan pengampu |
| 2.5 | **Fase 2.5:** perbarui `CLAUDE.md`, README utama, dan kedua prompt agar regenerasi tidak memasukkan kembali kesalahan lama |
| 2.6 | Laporkan temuan §7.3 kepada tim kurikulum |

### Tahap 3 — Nilai tinggi (setelah fondasi rapi)

| Gagasan | Manfaat |
|---------|---------|
| **`obe-registry.json`** yang dibangkitkan dari registri dan *front-matter* | Satu indeks *machine-readable* untuk validator, dasbor, dan tutor AI (Pedoman Fase 5) |
| **CI pada GitHub Actions** yang menjalankan validator dan semua notebook lab dengan versi pustaka terkunci | Repositori ini pertama kali memiliki "uji otomatis"; regresi seperti `kstest`/`.round()` tertangkap sebelum semester |
| **Bank soal bertanda** (Sub-CPMK × Bloom × tingkat kesulitan × riwayat pemakaian) | Ujian setiap semester dapat disusun ulang dengan aman; analisis butir menjadi bukti kriteria 5 |
| **Dasbor ketercapaian CPL** dari nilai per butir | Bukti PPEPP (kriteria 1) yang hidup; dapat dipakai bersama oleh MK lain yang berbagi CPMK082/102 |
| **Penerbitan buku ajar ber-ISBN / OER** dan dataset Indonesia yang terkurasi | Luaran yang terhitung untuk IKU dan kriteria 3–4 LAM; membedakan UAI secara nyata |

---

## 9. Keputusan yang Dibutuhkan dari Dosen

1. **Skala nilai — sisa verifikasi.** Tabel resmi lengkap sudah diterima dan diterapkan (7 Oktober 2026). Yang masih perlu dipastikan dari dokumen resmi: bobot nilai mutu (kini bobot umum 4,00/3,70/3,30/3,00/2,70/2,30/2,00/1,00/0,00), nama/nomor dokumen, dan aturan pembulatan.
2. **Syarat lulus tambahan** (≥ 50% per Sub-CPMK, wajib presentasi, 15 wawancara): ajukan ke prodi atau cabut?
3. **Ketidakcocokan teknik ↔ Sub-CPMK:** tandai per butir (dalam kendali dosen) atau usulkan revisi registri?
4. **Nasib folder** IF2205, IF2206, dan IF3XXX. *(v1.2 — sudah diputuskan: IF3XXX dan IF2206 diarsipkan; IF2205 ditempatkan di `semester-4/rekayasa-perangkat-lunak/` sebagai `IF52520011` dengan keterangan penyusun materi. Yang tersisa hanya keputusan prodi tentang peleburan lab IF2206.)*
5. **Urutan otoritas** registri vs Pedoman OBE, dan apakah kode asesmen memakai `ASM-*` atau `K-01/T-01/P-01`.
6. **Metodologi Penelitian:** teruskan ke Andi Arniaty Arsyad, Ph.D. untuk pengesahan dan rubrik; beri tahu juga bahwa skala resmi UAI sudah diterapkan di bahan mata kuliah tersebut.

## 10. Dokumen Formal yang Perlu Dikumpulkan

Simpan salinannya di `00-pedoman-obe/sumber/`, lalu ubah status 🟡/🔲 terkait menjadi ✅.

| Dokumen | Untuk apa |
|---------|-----------|
| **Dokumen resmi sumber tabel "Kategori Penilaian"** (peraturan akademik UAI: bobot nilai mutu, pembulatan, syarat kehadiran) | Mencatat nomor dokumen dan memverifikasi bobot di [`konversi-nilai.md`](../00-pedoman-obe/konversi-nilai.md) §B; dasar "kehadiran 75%" |
| Berkas Excel resmi `Revisi_2026_Kurikulum_OBE_IF_2025_2.xlsx` | Sumber primer registri; sheet 16–20 (teknik, mekanisme, bobot, rumusan akhir) belum final |
| SK ambang ketercapaian CPL | Ambang "tuntas" yang kini masih usulan |
| Matriks butir Instrumen LAM-INFOKOM 2.0 | Pemetaan bukti per butir |
| Teks resmi Permendiktisaintek 39/2025, 10/2026, 14/2026 | Mengubah sitasi 🟡 menjadi ✅ |
| Persetujuan Universitas/Fakultas atas CPMKUAI* dan CPMKFSTS* (T-9 di `91`) | Status resmi CPMK lintas prodi |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
