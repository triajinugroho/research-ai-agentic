---
id: uai-inf-kamus-data
tipe: pedoman
judul: Kamus Data Metadata — Standar Data, Metadata, dan Kode Referensi
prodi: Informatika
universitas: Universitas Al Azhar Indonesia
versi: 1.0
status: berlaku
diperbarui: 2026-09-05
berlaku_untuk: [INF-101, INF-102, TBD-STAT, IF2205, IF2206, IF3XXX]
---

# Kamus Data Metadata

> **Dasar regulasi.** Berkas ini memenuhi secara harfiah dua dari empat prinsip **Permendiktisaintek No. 14 Tahun 2026 (Satu Data Diktisaintek)** — *standar data* dan *metadata* — serta menyiapkan dua sisanya (*interoperabilitas* dan *kode referensi/data induk*).
>
> **Aturan pengikat:** *front-matter* **mencerminkan** isi dokumen, tidak menggantikannya. Bila front-matter dan tabel di dalam dokumen berbeda, itu cacat yang ditangkap validator (V3, V7).

## A. Field Wajib pada Semua Berkas

| Field | Tipe | Enumerasi / Format | Contoh | Padanan PDDikti |
|---|---|---|---|---|
| `id` | string | `[a-z0-9-]`, **tidak pernah berubah** | `uai-inf101-rps` | — |
| `tipe` | enum | `rps` `rtm` `modul` `lab` `bab-buku-ajar` `asesmen` `rubrik` `mutu` `pedoman` `pedoman-praktikum` `analisis-strategis` `dataset` `readme` | `rps` | — |
| `judul` | string | bebas | `Rencana Pembelajaran Semester — Algoritma dan Pemrograman` | — |
| `kode_mk` | string | kode resmi, atau `TBD-*` bila belum ditetapkan | `INF-101` | Kode Mata Kuliah |
| `nama_mk` | string | nama formal lengkap | `Algoritma dan Pemrograman` | Nama Mata Kuliah |
| `prodi` | string | `Informatika` | `Informatika` | Program Studi |
| `versi` | string | semver ringkas | `2.0` | — |
| `status` | enum | `draft` `berlaku` `arsip` | `berlaku` | — |
| `diperbarui` | date | **ISO 8601** `YYYY-MM-DD` | `2026-09-05` | — |

## B. Field Kondisional menurut `tipe`

| `tipe` | Field tambahan wajib |
|---|---|
| `rps` | `sks`, `sks_teori`, `sks_praktikum`, `semester_jenis`, `semester_kurikulum`, `tahun_akademik`, `siklus`, `moda`, `dosen`, `prasyarat[]`, `korekuisit[]`, `pl[]`, `cpl[]`, `bk[]`, `cpmk[]`, `cpl_status` |
| `modul`, `lab` | `minggu[]`, `sub_cpmk[]`, `bloom_c[]`, `bloom_a[]`, `bloom_p[]`, `estimasi_menit` |
| `bab-buku-ajar` | `bab`, `sub_cpmk[]`, `bloom_c[]`, `bloom_a[]`, `bloom_p[]`, `level_ai` |
| `asesmen`, `rubrik` | `asesmen_id`, `mengukur_cpmk[]`, `mengukur_sub_cpmk[]`, `bobot_persen`, `ai_diizinkan` |
| `mutu` | `kriteria_lam[]`, `tahap_ppepp[]`, `siklus` |
| `pedoman` | `berlaku_untuk[]` |

**Field opsional (semua tipe):** `penulis`, `lisensi`, `kata_kunci[]`, `sdg[]`, `iku[]`, `kode_mk_status`.

## C. Enumerasi Nilai

| Field | Nilai sah |
|---|---|
| `status` | `draft` · `berlaku` · `arsip` |
| `cpl_status` | `resmi` · `interim` |
| `kode_mk_status` | `resmi` · `sementara` |
| `semester_jenis` | `ganjil` · `genap` |
| `moda` | `tatap-muka` · `daring` · `kombinasi` |
| `level_ai` | `understand` · `apply` · `create` (UNESCO AI Competency Framework for Students, Januari 2026) |
| `bloom_c` | `C1`–`C6` |
| `bloom_a` | `A1`–`A5` |
| `bloom_p` | `P1`–`P5` |
| `tahap_ppepp` | `P1-penetapan` · `P2-pelaksanaan` · `E-evaluasi` · `P3-pengendalian` · `P4-peningkatan` |
| `kriteria_lam` | `1-budaya-mutu` · `2-relevansi-pendidikan` · `3-relevansi-penelitian` · `4-relevansi-pkm` · `5-akuntabilitas` · `6-diferensiasi-misi` |
| `ai_diizinkan` | `true` · `false` |

## D. Aturan Penamaan `id` (Kode Referensi / Data Induk)

Pola: `uai-<kode_mk_slug>-<tipe>-<diskriminator>`

| Contoh | Keterangan |
|---|---|
| `uai-inf101-rps` | RPS mata kuliah INF-101 |
| `uai-inf101-modul-w03` | Modul minggu ke-3 |
| `uai-inf101-bab-09` | Bab 9 buku ajar |
| `uai-inf101-asesmen-uts` | Naskah UTS |
| `uai-inf101-mutu-02` | Berkas mutu kedua (pengukuran ketercapaian CPL) |

**Sifat `id`:** stabil seumur hidup dokumen. Berkas boleh di-*rename*, folder boleh dipindah — `id` **tidak ikut berubah**. Stabilitas identitas inilah syarat interoperabilitas; itu sebabnya `id` sengaja tidak diturunkan dari *path*.

## E. Kode Referensi Lintas Dokumen

| Jenis | Pola | Himpunan nilai sah didefinisikan di |
|---|---|---|
| Profil Lulusan | `PL01`–`PL05` | `profil-lulusan.md` |
| CPL | `CPLUAI1`, `CPL03`, `CPL-FSTS1`, … | `cpl-master.md` |
| Bahan Kajian | `BK01`–`BK22` | `registri-bahan-kajian.md` |
| CPMK | `CPMK-1` … `CPMK-n` | §D RPS mata kuliah bersangkutan |
| Sub-CPMK | `Sub-CPMK-<induk>.<urut>` | §E RPS mata kuliah bersangkutan |
| Asesmen | `ASM-K1`, `ASM-UTS`, `ASM-UAS`, `ASM-T1`, `ASM-PRJ`, `ASM-PAR` | §G RPS mata kuliah bersangkutan |
| Regulasi | `[REG-1]` … `[REG-11]` | `pedoman-obe-konvensi.md` §B |

Validator memeriksa **integritas referensial** setiap kode terhadap himpunan nilai sahnya (V3).

## F. Catatan Teknis

- **Format:** YAML *front-matter* — standar de-facto ekosistem Markdown; terbaca oleh `python-frontmatter`, Pandoc, Hugo/Jekyll; dirender sebagai tabel oleh GitHub; mudah diekspor ke JSON/CSV.
- **Keterbatasan:** *front-matter* **tidak ikut terbawa** saat konversi ke Word/PDF melalui Pandoc. Ini bukan kehilangan data — metadata memang lapisan mesin, sedangkan isi dokumen tetap lengkap tanpanya.
- **Indeks turunan:** `obe-registry.json` pada Fase 5 **di-generate** dari front-matter, tidak pernah ditulis tangan.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
