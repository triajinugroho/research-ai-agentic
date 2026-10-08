---
id: uai-inf-kendali-eksekusi
tipe: mutu
judul: Kendali Eksekusi — Ceklis Perbaikan Repositori
kode_mk: PRODI-IF
nama_mk: Seluruh paket mata kuliah
prodi: Informatika
versi: 1.0
status: berlaku
diperbarui: 2026-10-08
kriteria_lam: [1-budaya-mutu, 5-akuntabilitas]
tahap_ppepp: [P3-pengendalian]
siklus: 2026-2027-ganjil
---

# Kendali Eksekusi — Ceklis Perbaikan Repositori

**Pemilik:** Tri Aji Nugroho, S.T., M.T. · **Sumber temuan:** [audit menyeluruh v1.3](AUDIT-MENYELURUH-2026-10.md), diverifikasi ulang terhadap `main` (`de6cfc8`) pada 7 Oktober 2026; status diperbarui 8 Oktober 2026 setelah eksekusi Tahap 0–1 (§7) · **Posisi semester:** Ganjil 2026/2027, perkiraan Minggu 5

> **Cara pakai.** (1) Sebelum bekerja — manusia maupun sesi AI — baca berkas ini dan pilih butir dengan tenggat terdekat yang tidak berstatus ⏸. (2) Setelah selesai, ubah status menjadi ☑ beserta hash commit atau tanggal bukti, lalu perbarui `diperbarui:`. (3) ID tidak pernah dinomori ulang; butir baru diberi nomor berikutnya pada tahap yang sesuai. (4) Keputusan dosen dicatat di tabel §1 (tanggal + isi), lalu butir yang bergantung dilepas dari ⏸. (5) **Repositori ini publik:** sampai D-08 diputuskan, naskah ujian, kunci, bank soal, dan nilai per mahasiswa tidak di-commit; tiga pasang UTS + kunci Genap 2025/2026 yang sudah ada menunggu D-08.
>
> **Status:** ☐ terbuka (termasuk yang menunggu keputusan dosen — lihat kolom *Butuh*) · ◐ sebagian · ☑ selesai · ⏸ menunggu pihak luar (prodi, pengampu lain, dokumen resmi) · **Mg** = minggu perkuliahan.
>
> **Singkatan:** Probstat = Probabilitas dan Statistik · AP / DP = Algoritma Pemrograman / Dasar Pemrograman · JST = Jaringan Syaraf Tiruan dan Pembelajaran Mendalam · PL = Perangkat Lunak · AF = kerangka asesmen (*assessment framework*).

## 0. Kalender Kunci (isi sesuai kalender akademik)

| Titik | Minggu | Tanggal |
|---|---|---|
| Hari ini (perkiraan) | Ganjil Mg 5 | 8 Oktober 2026 |
| UTS Ganjil 2026/2027 | Mg 8 | … |
| UAS Ganjil 2026/2027 | Mg 16 | … |
| Evaluasi PPEPP Ganjil | Mg 17 | … |
| Mulai Genap 2026/2027 | Mg 1 | ± Februari 2027 |

## 1. Keputusan yang Dibutuhkan (D)

Nomor D-01 … D-06 sama dengan [audit §9](AUDIT-MENYELURUH-2026-10.md#9-keputusan-yang-dibutuhkan-dari-dosen) butir 1–6.

| ID | Keputusan | Lingkup | Tenggat | Status / keputusan |
|---|---|---|---|---|
| D-01 | Skala nilai — sisa verifikasi: bobot nilai mutu, nama/nomor dokumen resmi, aturan pembulatan (dokumen: F-01) | semua MK | sebelum Mg 16 | ⏸ menunggu F-01 |
| D-02 | Syarat lulus tambahan — ajukan ke prodi atau cabut: Dasar AI/ML (≥ 50% per Sub-CPMK; wajib proyek dan presentasi), Teknopreneur (15 wawancara, MVP ke ≥ 5 orang, *Demo Day*, ≥ 50%), Metodologi ("pelanggar ketentuan mutlak maks. C"), Probstat (kehadiran 75% sebagai syarat lulus, bukan hanya syarat UAS) | 4 MK Ganjil | sebelum Mg 8 | ☐ |
| D-03 | Teknik ↔ Sub-CPMK tidak sesuai isi ujian, kuis, dan lab. **Usul:** semester ini tandai Sub-CPMK per butir dan hitung ketercapaian per butir; usulan revisi alokasi registri masuk T2-08 | 4 MK Ganjil | **Mg 5** (prasyarat naskah) | ☐ — bawaan sementara opsi tag per butir dipakai pada draf naskah 8 Okt (TD-48) |
| D-04 | Nasib Praktikum RPL IF2206: arsip permanen, dilebur (RPL / Proyek PL / Pengujian PL), atau diusulkan kembali | arsip | sebelum Genap | ⏸ prodi |
| D-05 | Urutan otoritas (Excel > registri > Pedoman > CLAUDE.md/prompt) dan skema kode asesmen (`ASM-*` vs `K-01/T-01/P-01`) | tata kelola | sebelum Mg 10 | ☐ |
| D-06 | Metodologi Penelitian: serahkan paket ke Andi Arniaty Arsyad, Ph.D. (pengesahan RPS, rubrik, naskah UTS/UAS, kapasitas presentasi) | semester-7 | **Mg 5** | ☐ |
| D-07 | Satu forum dengan Dr. Ir. Ade Jamal, M.T.: Dasar AI/ML ↔ JST (batas MLP Mg 13) dan ↔ Sains Data; Algoritma Pemrograman ↔ Dasar Pemrograman; Praktikum AP ↔ Praktikum DP | sem 2, 5 | JST sebelum Mg 13; lainnya sebelum Genap | ☐ |
| D-08 | Penyimpanan naskah, kunci, bank soal, dan nilai: **usul** simpan privat (LMS/Drive/repo privat); repo publik hanya kisi-kisi, cetak biru butir, dan angka agregat. Putuskan juga nasib 3 pasang UTS + kunci Genap 2025/2026 yang sudah publik | semua | **Mg 5** | ☐ — bawaan sementara: draf naskah 8 Okt tidak di-commit, diserahkan langsung ke dosen (TD-47) |
| D-09 | Dasar AI/ML: lab dikerjakan di kelas atau dilanjutkan di rumah (dasar Partisipasi 0%) | sem 5 | sebelum Mg 7 | ☐ |
| D-10 | RPL: siapa menyelaraskan ke `IF52520011` dan apakah materi dipakai oleh pengampu registri, Dr. Ir. Winangsari Pradani, M.T. | sem 4 | sebelum Mg 17 | ☐ |
| D-11 | Nama MK di materi `IF52520004/05`: "Algoritma Pemrograman" (registri) atau "Algoritma dan Pemrograman" (CLAUDE.md aturan 2, Pedoman §I.2) | sem 2 | sebelum Genap | ☐ |
| D-12 | Tinjau 56 pilihan agen di [TINJAUAN-DOSEN-2026-10](TINJAUAN-DOSEN-2026-10.md): setujui atau ubah, catat di sini dengan nomor TD | semua | baris ▲: **Mg 6**; lainnya Mg 10 | ☐ |

## 2. Tahap 0 — Darurat, sebelum UTS (Mg 5–8)

| ID | Pekerjaan · *selesai bila* | MK | Tenggat | Butuh | Status |
|---|---|---|---|---|---|
| T0-01 | Naskah UTS + kunci + pedoman skor · *cetak biru butir × Sub-CPMK × Bloom ≥ C3; bukan dari Latihan Soal atau contoh kisi-kisi; SD sampel masuk lembar rumus* | Dasar AI/ML | Mg 8 (draf Mg 7) | D-03, D-08 | ◐ draf privat 8 Okt (naskah, kunci, cetak biru; dikerjakan ulang mandiri oleh pemeriksa) — tunggu D-03, D-08, T0-15 |
| T0-02 | Naskah UTS + kunci + pedoman skor · *butir bertanda PS-Sub-CPMK dan Bloom* | Probstat | Mg 8 | D-03, D-08 | ◐ draf privat 8 Okt (naskah, kunci, cetak biru; dikerjakan ulang mandiri oleh pemeriksa) — tunggu D-03, D-08, T0-15 |
| T0-03 | Naskah UTS + kunci/rubrik · *bukan salinan contoh A1–C1; kaidah "konsisten" diberi rentang skor* | Teknopreneur | Mg 8 | D-03, D-08 | ◐ draf privat 8 Okt (naskah, kunci, cetak biru; dikerjakan ulang mandiri oleh pemeriksa) — tunggu D-03, D-08, T0-15 |
| T0-04 | Naskah UTS + kunci (oleh/bersama pengampu) | Metodologi | Mg 8 | D-06, D-08 | ⏸ |
| T0-05 | Kuis: Dasar AI/ML K-02 (Mg 7), K-03 (Mg 10), K-04 (Mg 13); Probstat K-02 (Mg 5), K-03, K-04; Metodologi K2 (Mg 9), K3 (Mg 12) · *naskah + kunci bertanda Sub-CPMK; K-01 yang sudah lewat diarsipkan privat beserta skor per butir* (Teknopreneur tanpa kuis) | 3 MK Ganjil | per minggu kuis | D-03, D-08 | ◐ K-02 Dasar AI/ML (versi A + cadangan B) draf privat 8 Okt |
| T0-06 | Cabut klaim "Latihan Soal dapat dipakai sebagai bank soal kuis/ujian" · *halaman depan Probstat :137, Dasar AI/ML :124, Teknopreneur :130, Metodologi :158*; kunci tertutup untuk butir hitungan Latihan Soal Dasar AI/ML menyusul (Mg 17) | 4 MK Ganjil | Mg 8 | — | ◐ klaim dicabut di 4 halaman depan `1f9b410`; kunci tertutup menyusul |
| T0-07 | Unggah atau tautkan 8 CSV lab; perbaiki peta dataset dan klaim "nyata" · *kolom "Dipakai pada" = header tiap lab* | Probstat | **Mg 7** | — | ◐ peta dataset, klaim "nyata", catatan sintetis 8 lab `5ffd5d5`; sisa: unggah 8 CSV, sifat/sumber 7 CSV (TD-36) |
| T0-08 | Satu aturan alat bantu ujian (formularium, tabel, kalkulator) di RPS, RTM, AF, kisi-kisi, modul Mg 8/16, dan Lampiran — seperti Dasar AI/ML `fd1560e` | Probstat, Teknopreneur | Mg 7 | — | ☑ `1f9b410`–`be5383e` |
| T0-09 | Bagian **Persiapan** (jalankan sel pembuka Lampiran D) di Lab 4–14 | Dasar AI/ML | **Mg 6** | — | ☑ `1f9b410`–`be5383e` |
| T0-10 | Lab 6: Lasso tidak menolkan fitur, tiga model identik · *data diberi fitur derau/kolinear; ≥ 1 koefisien nol; dikunci `assert`* | Dasar AI/ML | **Mg 6** | — | ☑ `1f9b410`–`be5383e` |
| T0-11 | Lab 7: positif 1,3% (21 di data uji), F1 k-NN = 0 · *≥ 100 positif di uji; angka teks = keluaran; `assert`* | Dasar AI/ML | Mg 7 | — | ☑ `1f9b410`–`be5383e` |
| T0-12 | Satu tabel sanksi (notebook tak jalan, kebocoran, keterbatasan); skala kuis 40/60 di AF; ketentuan lab sesuai D-09 | Dasar AI/ML | Mg 7 | D-09 | ◐ satu tabel AF §7, tanpa sanksi ganda (TD-01…06); ketentuan lab tunggu D-09 |
| T0-13 | Penetapan siklus: tag git `siklus-2026-2027-ganjil` di remote; RPS 4 MK dilengkapi baris Moda + bagian Pengukuran Ketercapaian CPL (Pedoman §H), lalu disahkan | 4 MK Ganjil | Mg 8 | D-02, D-06 | ☐ |
| T0-14 | Kapasitas presentasi T6 (Mg 6) dan pertahanan T8 (Mg 9) | Metodologi | Mg 6 | D-06 | ⏸ |
| T0-15 | Telaah sejawat naskah UTS memakai [checklist-verifikasi](../00-pedoman-obe/checklist-verifikasi.md) §C, termasuk uji coba berwaktu oleh penelaah yang belum melihat naskah (TD-49) | 4 MK Ganjil | Mg 8 | T0-01…04 | ☐ |
| T0-16 | Status di README akar dan README semester 1, 5, 7 membedakan "materi lengkap" dari "asesmen/mutu belum lengkap" | meta | Mg 8 | — | ☑ `1f9b410`–`be5383e` |
| T0-17 | Catatan kerja registri: `91` dan README registri (rentang CPMK 2–7; §2.2b bobot; §2.3 klaim kode CPL) serta status Pedoman §J/§K | tata kelola | Mg 8 | — | ☑ `1f9b410`–`be5383e` |
| T0-18 | Kisi-kisi UTS Probstat sebelum diumumkan: waktu saran vs Modul Mg 8, kolom Bagian D (Mg 1, 2, 6), aturan skor §6, rumus eksponensial/geometrik (TD-31, TD-32) | Probstat | Mg 7 | D-12 | ☐ |

## 3. Tahap 1 — Sebelum minggu pelaksanaan dan akhir Ganjil (Mg 9–17)

| ID | Pekerjaan · *selesai bila* | MK | Tenggat | Butuh | Status |
|---|---|---|---|---|---|
| T1-01 | Lab 9: pohon kedalaman 3 memprediksi satu kelas (F1 = 0) · *F1 uji > 0; `assert`* | Dasar AI/ML | Mg 9 | — | ☑ `1f9b410`–`be5383e` |
| T1-02 | Lab 10: kebocoran seleksi · *SVM tersetel dinilai dengan CV bersarang; Langkah 9 memakai `X_train`* | Dasar AI/ML | Mg 10 | — | ☑ `1f9b410`–`be5383e` |
| T1-03 | Modul Mg 11: `.round()` pada skor *float* gagal di sklearn ≥ 1.7; Lab 11: bandingkan ID klaster mentah · *`round(x, n)`; label diselaraskan atau ARI* | Dasar AI/ML | Mg 11 | — | ☑ `1f9b410`–`be5383e` |
| T1-04 | Lab 13: ROC-AUC MLP 0,443 (*early stopping*) · *konfigurasi Langkah 4; AUC > 0,5 dikunci `assert`; catatan di Bab 12* | Dasar AI/ML | Mg 13 | — | ☑ `1f9b410`–`be5383e` |
| T1-05 | Lab 14: kesimpulan audit bias berupa teks tetap yang bertentangan dengan hasil · *fitur proksi; recall bermakna; kesimpulan dihitung; tag Sub-CPMK sama di lab, RTM, rubrik, RPS* | Dasar AI/ML | Mg 14 | D-03 | ◐ lab ☑ `1f9b410`; tag Sub-CPMK tunggu D-03 (TD-27) |
| T1-06 | Teori *fairness* (Kleinberg) keliru · *5 lokasi: Bab 13 (+ Latihan d), modul Mg 14, Lab 14, kisi-kisi UAS A4* | Dasar AI/ML | Mg 14 | — | ☑ `1f9b410`–`be5383e` |
| T1-07 | Pembanding model √(s₁²+s₂²) → selisih berpasangan per lipatan; seragamkan `ddof` · *8 lokasi* | Dasar AI/ML | Mg 9–16 | — | ☑ semua lokasi, `be5383e` + commit 8 Okt (TD-07) |
| T1-08 | `assert` hasil kunci di setiap lab, dikalibrasi dan dicatat "diuji pada" versi pustaka Colab | Dasar AI/ML | per minggu lab | — | ◐ Lab 3–7, 9–14 ber-`assert` + "diuji pada"; sisa Lab 1–2 |
| T1-09 | Label "data sintetis (simulasi)" pada lab yang sintetis; klaim "data nyata/BPS" hanya untuk data bersumber | Dasar AI/ML | Mg 9 | — | ☑ `1f9b410`–`be5383e` |
| T1-10 | Naskah UAS + kunci/rubrik (privat) · *butir bertanda Sub-CPMK; ≥ C4 untuk 082-1* | 4 MK Ganjil | Mg 16 (draf Mg 14) | D-03, D-08 | ☐ |
| T1-11 | Urutan P-03 vs materi *model card*; sesi presentasi tambahan Mg 15; formulir kontribusi anggota kelompok | Dasar AI/ML | Mg 11 | — | ☑ `1f9b410`–`be5383e` |
| T1-12 | Perbaikan akademik: Bloom Bab 4–5; peta level UNESCO; sitasi Kapoor & Narayanan, UNESCO [REG-9], CS2023 + AAAI; satu daftar larangan AI; "verbatim" → "diadaptasi"; TensorFlow di README/Mg 1; anchor Lampiran I | Dasar AI/ML | Mg 17 (daftar AI: Mg 7) | — | ◐ sisa: format sitasi UNESCO seragam (TD-29) |
| T1-13 | Satu rubrik proyek; slot presentasi Mg 15 untuk dua kelas; *peer review* ≠ partisipasi; anchor Lampiran H; tag Sub-CPMK header Lab 04–11 (102-1 vs RPS 081-1) | Probstat | Mg 13 | D-03 (tag) | ◐ satu rubrik, slot Mg 15, *peer review* (TD-33–35); tag tunggu D-03 |
| T1-14 | Label teknik RPS §F; tenggat milestone ≥ studio isinya; sitasi hukum (UU 6/2023, UU 1/2024, SE Menkominfo 9/2023 → Komdigi, nomor fatwa DSN-MUI, POJK 22/2023, nama kementerian UMKM); Persiapan studio; UAI32-1 = C6; README "5 CPMK" → 6; prasyarat; CPL09 non-IF; penguji luar *Demo Day*; anchor Lampiran | Teknopreneur | Mg 9–13 (tenggat P-02: Mg 7) | — | ◐ sisa: Bab 14 §14.1 vs RTM/AF (TD-42, D-02); penguji luar tidak hadir (TD-41) |
| T1-15 | Melalui pengampu: Pengesahan; T3/T4/T7 → 071-1; rubrik T1/T3/T7/K1–K3 dan bobot aspek R1–R9; seminar Mg 15; prasyarat; ranah CPL di README; nama lembaga; anchor Lampiran F | Metodologi | Mg 7–17 | D-06 | ⏸ (anchor Lampiran F ☑ `5ffd5d5`) |
| T1-16 | `mutu/01–03` + *front-matter* RPS/asesmen · *lembar per butir (mutu/02) dan kerangka log (mutu/03) siap sebelum UTS; front-matter RPS ditulis setelah validator mengenali kode registri* | 4 MK Ganjil | mutu/02 + kerangka mutu/03: Mg 8; mutu/01: Mg 13; mutu/03 terisi: Mg 17 | D-05, T2-02 (front-matter) | ☐ |
| T1-17 | Ambang ketercapaian usulan seragam di satu berkas Pedoman; ajukan SK (F-03) | tata kelola | Mg 10 | — | ☐ |
| T1-18 | Pengendalian pasca-UTS: sinyal per Sub-CPMK dan tindakan koreksi dicatat di `mutu/03` | 4 MK Ganjil | Mg 9–10 | T1-16 | ☐ |
| T1-19 | Evaluasi PPEPP: ketercapaian Sub-CPMK/CPMK/CPL (**agregat saja** di repo), ≤ 5 tindak lanjut, tag penutup siklus | 4 MK Ganjil | Mg 17 | T1-16, F-03 | ☐ |
| T1-20 | Lab 3: `.round()` pada skor *float* gagal di sklearn ≥ 1.7; demonstrasi kebocoran Lab 3 dan Lab 4 tidak menunjukkan efeknya · *skor bocor > Pipeline; efek pembagian berkelompok dan temporal nyata; `assert`* | Dasar AI/ML | crash: segera; demo: sebelum Ganjil 2027/2028 | — | ☑ `1f9b410`–`be5383e` |
| T1-21 | Modul Mg 10 dan Lampiran: `SVC(probability=True)` memicu *FutureWarning* di scikit-learn 1.9 (parameter dihapus di 1.11) · *ROC-AUC via `decision_function`, seperti Lab 10* | Dasar AI/ML | Mg 10 | — | ☐ |

## 4. Tahap 2 — Sebelum Genap 2026/2027 (± Februari 2027)

| ID | Pekerjaan · *selesai bila* | Lingkup | Butuh | Status |
|---|---|---|---|---|
| T2-01 | **Pedoman OBE v3.0**: urutan otoritas; BK registri; kode CPMK/Sub-CPMK/asesmen; §I.1 tanggal; pengecualian "Bab 13 = AI" (Probstat, Teknopreneur); `berlaku_untuk`; field kamus `penyusun`/`pengampu_registri`/`kode_mk_lama`; §Q sesuai implementasi; keputusan `05-` vs `06-buku-ajar`; peran INF-101 sebagai *golden template* (§J) | tata kelola | D-05 | ☐ |
| T2-02 | **Validator v3**: baca kode, bobot, dan SKS dari registri; kenali `XX-Sub-CPMKnnn-n` (target Mg 12, untuk T1-16); mode *baseline* (exit 0 bila tak ada temuan baru); V10 abaikan blok kode; V13 untuk kode/prosa; `--help` | tools | D-05 | ◐ `--help`, V10 abaikan kode, mode *baseline* + `tools/validasi-obe-baseline.json` (`5892c13`, 8 Okt); sisa bergantung D-05 |
| T2-03 | Algoritma Pemrograman → `IF52520004`: spanduk kode resmi; tabel migrasi; 2 Sub-CPMK; bobot 5/25/30/20/20; tidak mengulang Dasar Pemrograman; naskah UTS baru + UAS; AI Corner Bab 5; `mutu/` siklus genap; tutup Fase 1 | sem 2 | D-05, D-07, D-11 | ◐ spanduk kode resmi `1f9b410` |
| T2-04 | Praktikum AP → `IF52520005`: bobot 5/5/50/20/10/10; rubrik-tugas; header 13 lab; RTS/RAS baru; 5 *footer*; spanduk kode resmi; tabel migrasi; `mutu/01–03` | sem 2 | T2-03, D-07 | ◐ spanduk kode resmi `1f9b410` |
| T2-05 | Analisis Data Statistik → `IF52520025`: spanduk kode resmi; tabel migrasi; `mutu/01–03`; 3 SKS; 15/25/10/25/25; refokus (akuisisi, kualitas data, EDA, analitik berbantuan AI); 55 *footer*; edisi 2025; tabel literasi AI Bab 1–14; Bab 14; BAN-PT; tautkan `regresi-berganda.html`; naskah UTS baru + UAS | sem 2 | D-05 | ◐ spanduk kode resmi + BAN-PT `1f9b410` |
| T2-06 | Rekayasa Perangkat Lunak → `IF52520011`: tabel migrasi; 5 Sub-CPMK; 5/5/30/20/20/20; rujukan IF2206; `mutu/01–03` (bersama pengampu registri); naskah UTS/UAS | sem 4 | D-04, D-10 | ⏸ |
| T2-12 | RPL, perbaikan yang tidak bergantung pada D-04/D-10: satu rubrik proyek (week-15), satu templat AI Usage Log, atribusi BAN-PT → LAM-INFOKOM, spanduk historis ROADMAP | sem 4 | — | ☑ `1f9b410`–`be5383e` (TD-44–46) |
| T2-13 | RPL: judul T1 berbeda — RTM "SRS Sistem Informasi Kampus" vs `rubrik-tugas` "SRS Sistem Perpustakaan" | sem 4 | D-10 | ☐ |
| T2-07 | Fase 2.5: kedua prompt (kode Sub-CPMK, CPMK registri, BAN-PT, penyusun vs pengampu, *front-matter*) | 00-meta | D-05, T2-01 | ◐ skala + lokasi `e10654c`, `3f93e43` |
| T2-08 | Laporan ke tim kurikulum: audit §7.3, CPL09 Metodologi (sheet 9 vs 14/15e), T-1…T-3, usulan alokasi teknik (D-03) · *dicatat di `91` §1.2 dan §3* | registri | — | ☐ |
| T2-09 | *Front-matter* bertahap semua berkas `semester-*` | semua | T2-02 | ◐ hanya INF-101 |
| T2-10 | README 00-meta masih mengulang klaim AUDIT-KESELARASAN "13 inkonsistensi … semuanya sudah diperbaiki", padahal audit §6 membantahnya — beri catatan koreksi | 00-meta | — | ☑ `1f9b410` |
| T2-11 | Arsip: BAN-PT (opsional); kode Keras 3 / sklearn 1.6 diuji saat dipakai ulang | arsip | D-04 | ☐ |

## 5. Tahap 3 — Nilai Tinggi (setelah fondasi)

| ID | Pekerjaan | Butuh | Status |
|---|---|---|---|
| T3-01 | `obe-registry.json` dibangkitkan deterministik dari registri dan *front-matter* | T2-01, T2-02 | ☐ |
| T3-02 | CI GitHub Actions: validator mode *baseline* + jalankan kode lab dengan `requirements.txt` berversi terkunci | T1-08, T2-02 | ☐ |
| T3-03 | Bank soal bertanda Sub-CPMK × Bloom × kesulitan × riwayat — **privat** | D-03, D-08 | ☐ |
| T3-04 | Dasbor ketercapaian CPL lintas MK dari nilai agregat per butir | T1-19, T3-01 | ☐ |
| T3-05 | Buku ajar ber-ISBN/OER (berkas LICENSE) dan dataset Indonesia terkurasi (sumber, tahun, lisensi) | keputusan lisensi | ☐ |
| T3-06 | Lapisan mutu program: pemetaan butir LAM-INFOKOM 2.0, `pemetaan-iabee.md`, PPEPP prodi | F-04 | ☐ |

## 6. Dokumen Formal (F) — simpan di `00-pedoman-obe/sumber/`

| ID | Dokumen | Untuk | Tenggat | Status |
|---|---|---|---|---|
| F-01 | Dokumen resmi "Kategori Penilaian": nama/nomor, bobot nilai mutu, pembulatan, syarat kehadiran 75% | D-01, [konversi-nilai](../00-pedoman-obe/konversi-nilai.md) §B | sebelum Mg 16 | ☐ |
| F-02 | Excel resmi registri; ekstraksi ulang setelah sheet 16–20 final | registri | salinan Mg 8 | ☐ |
| F-03 | SK ambang ketercapaian CPL | T1-17, T1-19 | sebelum Mg 17 | ☐ |
| F-04 | Matriks butir Instrumen LAM-INFOKOM 2.0 | T3-06 | berkelanjutan | ☐ |
| F-05 | Teks resmi Permendiktisaintek 39/2025, 10/2026, 14/2026 | Pedoman §B | sebelum Feb 2027 | ☐ |
| F-06 | Persetujuan Universitas/Fakultas atas CPMKUAI\* dan CPMKFSTS\* (T-9) | Teknopreneur, RPL | sebelum Mg 17 | ☐ |

## 7. Sudah Selesai (rekam jejak)

| Tanggal | Pekerjaan | Bukti |
|---|---|---|
| 2026-10-07 | Skala nilai resmi UAI di 10 folder MK + registri tunggal + validator V13 | `8f09bc0`, `e10654c` |
| 2026-10-07 | Dasar AI/ML: bobot lab 15/10, soal B3, aturan alat bantu, fakta registri, catatan koordinasi Sains Data | `fd1560e` |
| 2026-10-07 | Probstat: total bobot lab 25%; 3 blok kode untuk SciPy 1.18 / Matplotlib 3.11 | `6a4d789` |
| 2026-10-07 | Rumusan verbatim CPMK Teknopreneur dan CPL Metodologi | `b37ec23` |
| 2026-10-07 | Susunan per semester, peta semester 1–8, arsip, penyusun vs pengampu RPL | `d339d8a`, `f7904f1`, `3f93e43` |
| 2026-10-07 | Laporan audit v1.3 dan berkas kendali ini | `f0f980c`, `e9f785c` |
| 2026-10-08 | Eksekusi Tahap 0–1 (17 editor + verifikasi adversarial 2 putaran + kritikus): Lab 3–7, 9–14 dan dokumen Dasar AI/ML, Probstat, Teknopreneur, RPL T2-12, meta, validator | `1f9b410`, `5892c13`, `be5383e` |
| 2026-10-08 | Tindak lanjut kritikus (pembanding berpasangan, *fairness*, sanksi, label data), [TINJAUAN-DOSEN](TINJAUAN-DOSEN-2026-10.md), *baseline* dan dokumentasi validator; draf naskah UTS 3 MK + K-02 diserahkan privat | `5ffd5d5`, *(commit ini)* |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
