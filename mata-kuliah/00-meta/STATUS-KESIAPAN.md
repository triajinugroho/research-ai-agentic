---
id: uai-inf-status-kesiapan
tipe: analisis-strategis
judul: Dasbor Kesiapan Mata Kuliah
kode_mk: PRODI-IF
nama_mk: Seluruh paket mata kuliah
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-11-07
---

# Dasbor Kesiapan Mata Kuliah

**Per 7 November 2026 · Pemilik:** Tri Aji Nugroho, S.T., M.T.

Satu halaman untuk menjawab "MK mana yang siap dipakai, apa yang masih kurang, dan keputusan apa yang menunggu". Rincian temuan ada di [audit menyeluruh Oktober 2026](AUDIT-MENYELURUH-2026-10.md). Dasbor ini mencatat **keadaan terkini** dan diperbarui setiap kali status berubah.

---

## 1. Ringkasan per Mata Kuliah

| MK | Semester | Kurikulum materi | Keselarasan registri (V14) | Lab berjalan | Naskah UTS | `mutu/` | Kesiapan |
|----|:--------:|------------------|:--------------------------:|:------------:|:----------:|:-------:|----------|
| [Probabilitas dan Statistik](../semester-1/probabilitas-dan-statistik/README.md) `IF52510033` | I | 2025 Rev. 2026 | ✅ | ✅ 13/13 | 🟡 draf di dosen | ❌ | **Siap dipakai**, dengan catatan cakupan UTS (§3, K-1) |
| [Dasar Kecerdasan Artifisial dan Pembelajaran Mesin](../semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/README.md) `IF52510031` | V | 2025 Rev. 2026 | ✅ | ✅ 13/13 | 🟡 draf di dosen | ❌ | **Siap dipakai**; naskah UAS dan kuis berikutnya belum ada |
| [Teknopreneur](../semester-5/teknopreneur/README.md) `ST52510002` | V | 2025 Rev. 2026 | ✅ | — (studio) | 🟡 draf di dosen | ❌ | **Siap dengan catatan**: syarat lulus tambahan perlu persetujuan prodi |
| [Metodologi Penelitian](../semester-7/metodologi-penelitian/README.md) `IF52510021` | VII | 2025 Rev. 2026 | ✅ | — (lokakarya) | ❌ keputusan pengampu | ❌ | **Menunggu pengampu** (Andi Arniaty Arsyad, Ph.D.) |
| [Algoritma Pemrograman](../semester-2/algoritma-pemrograman/README.md) `IF52520004` | II | Lama (INF-101) | ❌ 2 Sub-CPMK | belum diuji | ada (skema lama) | ✅ | **Perlu diselaraskan** sebelum Februari 2027 |
| [Praktikum Algoritma Pemrograman](../semester-2/praktikum-algoritma-pemrograman/README.md) `IF52520005` | II | Lama (INF-102) | ❌ 2 Sub-CPMK | belum diuji | ada (skema lama) | ❌ | **Perlu diselaraskan** sebelum Februari 2027 |
| [Analisis Data Statistik](../semester-2/analisis-data-statistik/README.md) `IF52520025` | II | Lama (2 SKS) | ❌ 3 Sub-CPMK | belum diuji | ada (skema lama) | ❌ | **Perlu diselaraskan berat**: 2 → 3 SKS, pisahkan dari ProbStat |
| [Rekayasa Perangkat Lunak](../semester-4/rekayasa-perangkat-lunak/README.md) `IF52520011` | IV | Lama (IF2205) | ❌ 5 Sub-CPMK | belum diuji | ada (skema lama) | ❌ | **Perlu diselaraskan**; pengampu registri Dr. Ir. Winangsari Pradani, M.T. |

**Keterangan:**
- **V14** dihitung otomatis oleh `python3 tools/validasi-obe.py`: ✅ berarti setiap Sub-CPMK registri MK itu disebut di RPS-nya; ❌ *n* berarti *n* Sub-CPMK registri belum disebut.
- **Lab berjalan** diukur dengan `python3 tools/uji-lab.py <folder-mk>` pada scikit-learn 1.9, pandas 3.0, dan NumPy 2.5.
- **Naskah UTS** 🟡: draf naskah dan kunci sudah disusun, tetapi **sengaja tidak disimpan di repositori** karena repositori ini publik. Cetak biru butirnya ada di kisi-kisi UTS masing-masing MK.

---

## 2. Yang Sudah Diperbaiki sejak Audit Oktober 2026

| Temuan audit | Status | Bukti |
|--------------|--------|-------|
| K2 — enam lab Dasar AI/ML menunjukkan kebalikan dari pelajarannya | ✅ Lab 3, 4, 9, 10, 11, 13, 14 dirancang ulang; kesimpulan dihitung dari angka dan stabil di beberapa *seed* | `04-labs/` Dasar AI/ML |
| T2 — teori *fairness* keliru | ✅ Dikoreksi di Modul 14, Bab 13, Lab 14, dan kisi-kisi UAS A4 (Chouldechova 2017; Kleinberg dkk. 2016) | Bab 13 §13.3.2 |
| T3 — Lab 4–14 tanpa bagian Persiapan | ✅ Ditambahkan | Lab 4–14 Dasar AI/ML |
| `.round()` pada skor sklearn gagal di versi ≥ 1.7 | ✅ Diganti `round(…)` | Lab 3, Modul 11 |
| Rumus pembanding model √(s₁²+s₂²) | ✅ Di Lab 10 dan 13 diganti perbandingan berpasangan per lipatan | Lab 10, 13 |
| Lab 10 melanggar aturan kebocoran #6 | ✅ SVM disetel di dalam setiap lipatan (CV bersarang) | Lab 10 Langkah 8 |
| 0.3 — 8 CSV lab ProbStat tidak ada | ✅ Delapan dataset sintetis dan pembangkitnya ada di `datasets/` | [Panduan Dataset](../semester-1/probabilitas-dan-statistik/datasets/README.md) |
| 0.1 / K1 / K4 — naskah UTS tanpa cetak biru, Bloom di bawah Sub-CPMK | 🟡 Cetak biru butir di kisi-kisi; draf naskah dan kunci di dosen (tidak di repo publik) | Kisi-kisi UTS tiga MK |
| K3 — teknik ↔ Sub-CPMK tidak cocok | 🟡 Setiap butir UTS ditandai Sub-CPMK (opsi a); keputusan permanen tetap pada dosen | Cetak biru butir |
| V8 — 55 berkas ADS tanpa *footer* | ✅ Seluruh 60 berkas dilengkapi | Validator V8 = 0 |
| V10 — tautan putus | ✅ 0; validator kini mengabaikan isi blok kode | Validator V10 = 0 |
| Validator tidak memahami registri | ✅ Aturan baru **V14** (penempatan, kode Sub-CPMK, cakupan Sub-CPMK di RPS) | [Pedoman §Q](../00-pedoman-obe/pedoman-obe-konvensi.md#q-aturan-validasi) |
| Web interaktif ProbStat tidak terhubung | ✅ Peta Minggu ↔ Bagian; setiap modul menautkan bagian yang sesuai | [README ProbStat](../semester-1/probabilitas-dan-statistik/README.md#pendamping-interaktif) |
| Tidak ada pintu masuk mahasiswa | ✅ Bagian "Mulai di Sini" di README empat MK baru | README MK |

---

## 3. Keputusan yang Menunggu Dosen

| # | Keputusan | Mengapa penting | Rujukan |
|---|-----------|-----------------|---------|
| K-1 | **Cakupan UTS ProbStat.** Registri menempatkan UTS pada `PS-Sub-CPMK102-1`, tetapi kisi-kisi yang sudah diumumkan memuat Minggu 4–7 (materi `081-1`): ±66% poin UTS. Pertahankan dengan penandaan per butir, atau geser ke kuis/UAS mulai siklus berikutnya? | Ketercapaian CPL dihitung dari pemetaan ini | Kisi-kisi UTS §Cetak Biru |
| K-2 | **Urutan otoritas** registri vs Pedoman OBE, dan format kode asesmen (`ASM-*` atau `K-01/T-01/P-01`) | Setiap penyelarasan MK lama bergantung pada keputusan ini | Audit §7.1 |
| K-3 | **Syarat lulus tambahan** (≥ 50% per Sub-CPMK, wajib presentasi, 15 wawancara): ajukan ke prodi atau cabut | Dapat membuat mahasiswa dengan nilai akhir ≥ 55,00 tidak lulus | [`konversi-nilai.md` §C](../00-pedoman-obe/konversi-nilai.md) |
| K-4 | **Kunci ujian lama di repositori publik.** `kunci-uts-*.md` Algoritma Pemrograman, Praktikum Algoritma Pemrograman, dan Analisis Data Statistik dapat dibaca siapa pun. Pindahkan ke penyimpanan tertutup, atau perlakukan sebagai soal latihan dan susun naskah baru | Soal yang sudah terbuka tidak lagi mengukur kemampuan | `05-assessments/`, `04-assessments/` MK semester II |
| K-5 | **Metodologi Penelitian:** teruskan ke Andi Arniaty Arsyad, Ph.D. untuk pengesahan RPS, rubrik, dan naskah ujian | Pengampu registri berbeda dari penyusun | [README MK](../semester-7/metodologi-penelitian/README.md) |
| K-6 | **GitHub Pages** untuk `docs/` (Settings → Pages → `main` → `/docs`) | Tautan versi daring web interaktif di modul baru aktif setelah ini | [`docs/README.md`](../../docs/README.md) |

---

## 4. Pekerjaan Berikutnya (Urut Prioritas)

1. **Naskah UAS + kunci** Dasar AI/ML, ProbStat, dan Teknopreneur dengan cetak biru butir (Minggu 16), disimpan di luar repositori publik.
2. **Kuis K-02 sampai K-04** Dasar AI/ML beserta kuncinya.
3. **`mutu/` dan *front-matter*** untuk empat MK baru, agar evaluasi Minggu 17 menghasilkan bukti ketercapaian **per butir**.
4. **Selaraskan empat MK semester II dan IV** ke registri. V14 menjadi daftar periksa: temuan V14 = 0 berarti setiap Sub-CPMK registri sudah masuk RPS.
5. **Uji lab MK lama** dengan `tools/uji-lab.py` sebelum Genap 2026/2027.
6. **Pedoman OBE v3.0 dan sinkronisasi prompt** (Fase 2.5), setelah keputusan K-2.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
