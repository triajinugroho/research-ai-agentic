---
id: uai-inf-arsip
tipe: readme
judul: Arsip — Materi Kurikulum Sebelumnya
kode_mk: PRODI-IF
nama_mk: Arsip kurikulum sebelumnya
prodi: Informatika
versi: 1.0
status: berlaku
diperbarui: 2026-10-07
---

# Arsip — Kurikulum Sebelumnya

Folder ini berisi materi yang disusun untuk **kurikulum sebelumnya** dan **tidak memiliki padanan aktif** pada [Kurikulum Informatika 2025 Revisi 2026](../00-kurikulum-if-2025-revisi-2026/README.md). Materi disimpan sebagai rekam jejak pengembangan dan sebagai **bank konten** bagi mata kuliah di kurikulum baru — bukan sebagai materi ajar yang berlaku. Dasar keputusan: [catatan dampak kurikulum §2.1–§2.2](../00-kurikulum-if-2025-revisi-2026/91-validasi-dan-catatan-dampak.md#21-pemetaan-mata-kuliah-repositori--kurikulum-baru) dan [audit menyeluruh, butir 2.4](../00-meta/AUDIT-MENYELURUH-2026-10.md).

> **Penyusun materi.** Seluruh materi di folder ini — seperti seluruh materi di repositori ini — disusun oleh **Tri Aji Nugroho, S.T., M.T.** Kolom *Pengampu (registri)* di bawah mengikuti [registri kurikulum](../00-kurikulum-if-2025-revisi-2026/11-susunan-mata-kuliah-dan-dosen.md) dan dapat berbeda dari penyusun materi.

## Isi Arsip

| Folder | Mata kuliah (kode lama) | SKS lama | Berkas | Alasan diarsipkan | Padanan / penerus di kurikulum baru |
|---|---|---|---|---|---|
| [`kecerdasan-buatan-machine-learning/`](kecerdasan-buatan-machine-learning/) | Kecerdasan Buatan dan Machine Learning (`IF3XXX`) | 4 (2 teori + 2 praktikum) | 57 | Digantikan oleh MK baru dengan nama, SKS (4 → 3), dan arsitektur CPMK yang berbeda | **Dasar Kecerdasan Artifisial dan Pembelajaran Mesin** (`IF52510031`, 3 SKS, semester 5) — materi aktif: [`../semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/`](../semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/) |
| [`praktikum-rekayasa-perangkat-lunak/`](praktikum-rekayasa-perangkat-lunak/) | Praktikum Rekayasa Perangkat Lunak (`IF2206`) | 1 (praktikum) | 23 | **Tidak ada** dalam kurikulum baru — tidak tercantum pada sheet 8, 9, 11, 14, maupun 15 ([catatan dampak §2.2c](../00-kurikulum-if-2025-revisi-2026/91-validasi-dan-catatan-dampak.md#22-perubahan-yang-berdampak-besar)) | Tidak ada penerus langsung. Lab dapat dilebur ke **Rekayasa Perangkat Lunak** (`IF52520011`, semester 4 — [`../semester-4/rekayasa-perangkat-lunak/`](../semester-4/rekayasa-perangkat-lunak/)), **Proyek Perangkat Lunak** (`IF52520017`, semester 6), atau **Pengujian Perangkat Lunak** (`IF52510029`, semester 5) |

## Pemanfaatan sebagai Bank Konten

### Kecerdasan Buatan dan Machine Learning (`IF3XXX`)

Penerus langsungnya adalah `IF52510031`, yang materinya sudah tersedia di folder semester 5. Bagian lanjutan materi arsip dapat dipakai sebagai bank konten bagi MK rumpun Kecerdasan Artifisial berikut (ketiganya MKP wajib, bukan MK peminatan/MKPP):

| Bagian materi arsip | Dapat dipakai untuk | Kode | Semester | Pengampu (registri) |
|---|---|---|---|---|
| Minggu 11 · Bab 10 · Lab 11 — *Neural Networks & Deep Learning* | Jaringan Syaraf Tiruan dan Pembelajaran Mendalam | `IF52510032` | 5 | Dr. Ir. Ade Jamal, M.T. |
| Minggu 12 · Bab 11 · Lab 12 — *Natural Language Processing* | Pengolahan Bahasa Alami | `IF52510024` | 7 | Dr. Ir. Winangsari Pradani, M.T. |
| Minggu 13 · Bab 12 · Lab 13 — *Computer Vision* (CNN) | Pengolahan Citra | `IF52510016` | 6 | Dr. Ir. Winangsari Pradani, M.T. |

### Praktikum Rekayasa Perangkat Lunak (`IF2206`)

Nasib folder ini masih menunggu keputusan prodi (lihat [catatan dampak §3 butir 2](../00-kurikulum-if-2025-revisi-2026/91-validasi-dan-catatan-dampak.md#3-usulan-urutan-tindak-lanjut)). Pembagian berikut hanya **usulan** peleburan lab:

| Lab arsip | Usulan tujuan peleburan | Kode | Semester | Pengampu (registri) |
|---|---|---|---|---|
| Lab 01–04 — lingkungan pengembangan, Git *branching* & *pull request*, SRS, *user story* & *sprint planning* | Rekayasa Perangkat Lunak | `IF52520011` | 4 | Dr. Ir. Winangsari Pradani, M.T. |
| Lab 05–07, 11–14 — *frontend*, *backend* Flask, basis data & ORM, CI/CD, Docker, *AI pair programming*, *sprint review* | Proyek Perangkat Lunak | `IF52520017` | 6 | Denny Hermawan, S.T., M.Kom. |
| Lab 09–10 — *unit testing* (pytest, Jest), *integration* & *API testing* | Pengujian Perangkat Lunak | `IF52510029` | 5 | Dr. Nurbojatmiko, S.Kom., M.Kom. |

Materi Rekayasa Perangkat Lunak (`IF52520011`) di folder semester 4 juga disusun oleh Tri Aji Nugroho, S.T., M.T., walaupun pengampu menurut registri adalah Dr. Ir. Winangsari Pradani, M.T.

## Ketentuan Arsip

- **Tidak dipelihara.** Materi arsip tidak lagi diperbarui mengikuti kurikulum maupun perkembangan pustaka. Kode dapat usang — misalnya contoh TensorFlow/Keras di `IF3XXX` belum disesuaikan dengan **Keras 3** (penyimpanan `model.save('dir/')` dan format `.h5`, `ImageDataGenerator`) dan scikit-learn 1.6 (`mean_squared_error(squared=False)`). Uji ulang setiap kode sebelum dipakai kembali.
- **Skala nilai sudah diselaraskan.** Konversi nilai pada RPS, kerangka asesmen, dan rubrik kedua MK sudah mengikuti skala resmi UAI di [registri konversi nilai](../00-pedoman-obe/konversi-nilai.md). Bila ada perbedaan, registri itulah yang berlaku.
- **Arsitektur lama tidak dipetakan ulang.** CPMK lokal (`CPMK-1` … `CPMK-7`), kode MK lama, dan bobot penilaian lama dibiarkan apa adanya; materi arsip belum memakai CPMK global prodi maupun enam teknik penilaian kurikulum baru. Temuan validator OBE pada folder ini (mis. V1 metadata, V4 pola kode lama) merupakan warisan kurikulum sebelumnya.
- **Penanda arsip.** Berkas materi di folder arsip tidak memiliki front-matter YAML dan tidak diberi front-matter baru; status arsip ditandai dengan spanduk di bagian atas README dan RPS masing-masing MK. Bila kelak front-matter ditambahkan, gunakan `status: arsip`.
- **Memakai kembali.** Salin bagian yang diperlukan ke folder MK tujuan di `semester-N/`, lalu selaraskan dengan RPS, CPMK, dan Sub-CPMK MK tersebut. Jangan mengembangkan materi baru di dalam folder arsip.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
