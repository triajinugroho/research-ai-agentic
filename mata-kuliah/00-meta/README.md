---
id: uai-inf-meta
tipe: readme
judul: Dokumen Meta Repositori
kode_mk: PRODI-IF
nama_mk: Dokumen meta repositori
prodi: Informatika
versi: 1.0
status: berlaku
diperbarui: 2026-10-08
---

# Dokumen Meta Repositori

Folder ini menyimpan dokumen **tentang** repositori, bukan materi kuliah: berkas kendali eksekusi beserta daftar tinjauan dosen, dua laporan audit, dan dua prompt generator. Isinya tidak dipakai langsung di kelas. Untuk substansi kurikulum, acuannya tetap [registri Kurikulum Informatika 2025 Revisi 2026](../00-kurikulum-if-2025-revisi-2026/README.md). Untuk konvensi repositori, acuannya [Pedoman OBE](../00-pedoman-obe/pedoman-obe-konvensi.md), dan untuk skala nilai, [registri konversi nilai](../00-pedoman-obe/konversi-nilai.md).

> **Penyusun materi.** Seluruh materi di repositori ini disusun oleh **Tri Aji Nugroho, S.T., M.T.**, termasuk Rekayasa Perangkat Lunak (`IF52520011`), yang menurut registri kurikulum diampu oleh Dr. Ir. Winangsari Pradani, M.T. Kolom pengampu pada peta semester mengikuti registri dan dapat berbeda dari penyusun materi.

## Kendali Eksekusi

| Berkas | Isi | Status |
|---|---|---|
| [`KENDALI-EKSEKUSI.md`](KENDALI-EKSEKUSI.md) | Ceklis eksekusi yang hidup: butir terbuka per tahap (darurat sebelum UTS, akhir Ganjil, sebelum Genap 2026/2027, nilai tinggi), keputusan dosen yang ditunggu (`D-xx`), dokumen formal (`F-xx`), dan bukti commit | **Berlaku — baca pertama.** Satu-satunya tempat status pekerjaan dilacak; diperbarui setiap kali butir selesai |
| [`TINJAUAN-DOSEN-2026-10.md`](TINJAUAN-DOSEN-2026-10.md) | Daftar ringkas pilihan yang diambil agen saat dokumen bertentangan atau tugasnya ambigu (putaran eksekusi 7–8 Oktober 2026), per mata kuliah: pilihan, alternatif, dan dampak bila diubah; nomor `TD-xx`, baris ▲ menyentuh mahasiswa Mg 6–8 atau mengubah bobot/aturan | **Draf — perlu ditinjau dosen.** Keputusan dicatat di [`KENDALI-EKSEKUSI.md`](KENDALI-EKSEKUSI.md) §1; berkas ini tidak melacak status |

## Laporan Audit

| Berkas | Tanggal | Cakupan | Status |
|---|---|---|---|
| [`AUDIT-MENYELURUH-2026-10.md`](AUDIT-MENYELURUH-2026-10.md) | 7 Oktober 2026 | Seluruh `mata-kuliah/` beserta `tools/validasi-obe.py`: kesiapan tiap MK, skala nilai, referensi formal, dan arah perbaikan bertahap | **Berlaku sebagai rujukan temuan.** Status tindak lanjutnya dilacak di [`KENDALI-EKSEKUSI.md`](KENDALI-EKSEKUSI.md); dokumennya masih berstatus draf untuk telaah dosen |
| [`AUDIT-KESELARASAN-IF2205-IF2206.md`](AUDIT-KESELARASAN-IF2205-IF2206.md) | 11–12 April 2026 | Keselarasan Rekayasa Perangkat Lunak (IF2205) dan Praktikum Rekayasa Perangkat Lunak (IF2206): 13 inkonsistensi pada berkas fondasi, yang oleh laporan itu dinyatakan sudah diperbaiki semuanya — klaim ini dikoreksi (lihat catatan di bawah) | **Historis.** Disimpan sebagai rekam jejak; tidak menjadi acuan |

Catatan untuk laporan historis:

- Laporan ini disusun untuk **kurikulum lama**. IF2205 kini menjadi Rekayasa Perangkat Lunak `IF52520011` di [`semester-4/rekayasa-perangkat-lunak/`](../semester-4/rekayasa-perangkat-lunak/). IF2206 tidak ada di kurikulum baru, dan materinya disimpan di [`arsip/praktikum-rekayasa-perangkat-lunak/`](../arsip/praktikum-rekayasa-perangkat-lunak/).
- Jalur berkas di tabel laporan (mis. `rekayasa-perangkat-lunak/02-rtm/...`) mengikuti susunan sebelum penataan per semester. Jalur yang berlaku sekarang ada pada butir di atas.
- Skala dan aturan kelulusan di dalamnya dipertahankan apa adanya sebagai catatan historis. Validator mengecualikan berkas ini dari aturan V13. Skala yang berlaku hanya yang tercantum di registri konversi nilai.
- **Koreksi (7 Oktober 2026).** Klaim laporan bahwa ke-13 inkonsistensi "semuanya sudah diperbaiki" tidak sepenuhnya benar. Pada saat audit (7 Oktober 2026), [audit menyeluruh §6](AUDIT-MENYELURUH-2026-10.md#6-enam-mk-kurikulum-lama) mencatat bahwa templat *AI Usage Log* beredar dalam **6 versi** dan ada **rubrik proyek ketiga** di modul `week-15` Rekayasa Perangkat Lunak. Isi laporan historis tidak diubah; perbaikannya dikerjakan dan statusnya dilacak di [`KENDALI-EKSEKUSI.md`](KENDALI-EKSEKUSI.md) butir T2-12.

## Prompt Generator

| Berkas | Kegunaan | Status |
|---|---|---|
| [`prompt-algoritma-pemrograman.md`](prompt-algoritma-pemrograman.md) | Prompt lengkap pembangkit paket **Algoritma dan Pemrograman**: analisis strategis, RPS, RTM, 16 modul, 13 lab, buku ajar 14 bab, dan asesmen. Prompt ini asal-usul paket [`semester-2/algoritma-pemrograman/`](../semester-2/algoritma-pemrograman/) (dulu INF-101, kini `IF52520004`) | **Perlu sinkronisasi Fase 2.5** Pedoman OBE |
| [`prompt-paket-mata-kuliah-informatika.md`](prompt-paket-mata-kuliah-informatika.md) | Prompt generik untuk MK Prodi Informatika lainnya. Prompt ini memuat variabel `[PLACEHOLDER]`, tiga templat tipe MK (A Teori, B Praktikum, C Teori+Lab), spesifikasi tiap berkas, dan urutan pembangkitan per batch | **Perlu sinkronisasi Fase 2.5** Pedoman OBE |

**Arti status "perlu sinkronisasi Fase 2.5".** Kedua prompt membawa spanduk *"Konvensi dalam berkas ini kedaluwarsa"*. Fase 2.5 (*sinkronisasi generator*) pada [Pedoman OBE §J Peta Jalan Pembaruan](../00-pedoman-obe/pedoman-obe-konvensi.md#j-peta-jalan-pembaruan) baru dikerjakan **sebagian** untuk kedua prompt — skala nilai dan lokasi keluaran (lihat tabel di bawah); bagian lainnya belum; lihat juga [audit menyeluruh §7.4 dan Tahap 2 butir 2.5](AUDIT-MENYELURUH-2026-10.md#74-dokumen-meta-yang-usang).

| Aspek | Keadaan di kedua prompt |
|---|---|
| Tabel konversi nilai resmi UAI (9 huruf, A ≥ 81,00, lulus C 55,00) | ✅ Sudah tersemat |
| Lokasi keluaran per semester `mata-kuliah/semester-N/[SLUG_MK]/` dan templat tautan `../../../00-…` dari folder tingkat-1 paket | ✅ Sudah diperbarui (Oktober 2026) |
| Kode Sub-CPMK kanonik, CPL resmi prodi, taksonomi tiga ranah C/A/P | 🔲 Belum. Validator melaporkan pola kode lama (V4) |
| *Front-matter* YAML, artefak mutu (PPEPP), sitasi regulasi terbaru | 🔲 Belum. Kedua prompt juga belum ber-*front-matter* (V1) |
| Kode MK, SKS, dan bobot asesmen dari registri kurikulum | 🔲 Belum. Prompt masih memakai kode lama atau sementara (`IF1XXX`, INF-101, IF2101, ...), dan kisi-kisi kurikulum di prompt generik masih berupa rancangan lama, bukan registri |
| Atribusi akreditasi, serta peran "penyusun materi" vs "pengampu (registri)" | 🔲 Belum. Tabel identitas masih memakai "BAN-PT/LAM-INFOKOM" dan menyebut penyusun sebagai "Dosen Pengampu" |

**Aturan pakai sebelum Fase 2.5 selesai:**

1. Jangan menjalankan prompt untuk regenerasi materi tanpa penyesuaian. Bila Pedoman OBE dan registri berbeda dengan prompt, **Pedoman OBE dan registri yang berlaku**.
2. Bila prompt tetap dipakai, sesuaikan hasilnya dengan Pedoman OBE dan registri. Tempatkan hasilnya di `mata-kuliah/semester-N/[SLUG_MK]/`, lalu jalankan [`tools/validasi-obe.py`](../../tools/validasi-obe.py) dari akar repositori: `python3 tools/validasi-obe.py`.

## Kaitan dengan Folder Lain

| Folder | Isi |
|---|---|
| [`00-kurikulum-if-2025-revisi-2026/`](../00-kurikulum-if-2025-revisi-2026/README.md) | Registri kurikulum resmi (transkripsi), acuan substansi |
| [`00-pedoman-obe/`](../00-pedoman-obe/pedoman-obe-konvensi.md) | Pedoman dan registri OBE internal, termasuk [konversi nilai](../00-pedoman-obe/konversi-nilai.md) |
| `semester-1/` … `semester-8/` | Paket mata kuliah per semester kurikulum, mis. [`semester-2/`](../semester-2/README.md) dan [`semester-4/`](../semester-4/README.md) |
| [`arsip/`](../arsip/README.md) | Materi kurikulum lama tanpa padanan aktif |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
