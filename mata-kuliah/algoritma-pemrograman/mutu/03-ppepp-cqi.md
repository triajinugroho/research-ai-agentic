---
id: uai-inf101-mutu-03
tipe: mutu
judul: Siklus PPEPP dan Peningkatan Mutu Berkelanjutan — Algoritma dan Pemrograman
kode_mk: INF-101
nama_mk: Algoritma dan Pemrograman
prodi: Informatika
siklus: 2025-2026-genap
kriteria_lam: [1-budaya-mutu, 5-akuntabilitas]
tahap_ppepp: [P1-penetapan, P2-pelaksanaan, E-evaluasi, P3-pengendalian, P4-peningkatan]
versi: 1.0
status: draft
diperbarui: 2026-09-05
---

# Siklus PPEPP — INF-101

> Menjawab pertanyaan: **bagaimana kita menutup lingkaran.**
>
> Instrumen Akreditasi LAM-INFOKOM 2.0 mengukur **setiap** dari enam kriteria dengan siklus PPEPP. Karena itu PPEPP bukan lampiran, melainkan kerangka waktu yang menaungi seluruh dokumen mata kuliah ini.

## 1. Kalender Siklus

| Tahap | Kegiatan | Waktu | Bukti |
|---|---|---|---|
| **P**enetapan | RPS, rubrik, dan ambang ketercapaian ditetapkan dan ditelaah sejawat | Sebelum minggu 1 | RPS `status: berlaku`; `git tag` awal siklus |
| **P**elaksanaan | Perkuliahan berjalan sesuai RPS | Minggu 1–16 | Modul mingguan, AI Usage Log, berita acara perkuliahan |
| **E**valuasi | Menghitung ketercapaian CPMK dan CPL dari nilai | Minggu 17 | `02-pengukuran-ketercapaian-cpl.md` §4 |
| **P**engendalian | Koreksi **dalam siklus berjalan** untuk CPMK yang tertinggal | Minggu 9–16 | §2 berkas ini |
| **P**eningkatan | Perubahan RPS/materi untuk siklus berikutnya | Sebelum siklus baru | §3 berkas ini + `git diff` antar-tag |

**Pengendalian bukan menunggu akhir semester.** Sinyal paling awal adalah hasil `ASM-K1` (minggu 4) dan `ASM-UTS` (minggu 8). Bila sebuah CPMK tampak tertinggal pada titik itu, tindakan diambil saat itu juga — bukan dicatat sebagai temuan untuk semester depan.

## 2. Log Siklus Berjalan — 2025-2026-genap

| Tahap | Tanggal | Temuan / Kegiatan | Tindakan | Status |
|---|---|---|---|:-:|
| **Penetapan** | 2026-09-05 | Pembaruan menyeluruh dokumen mata kuliah mengikuti Pedoman OBE v2.0: CPL resmi prodi, kode Sub-CPMK kanonik, taksonomi C/A/P, artefak mutu | RPS v2.0 disusun; tiga berkas `mutu/` dibuat; tabel migrasi kode ditetapkan | ✅ |
| **Penetapan** | — | 🔲 Penetapan resmi ambang ketercapaian CPL oleh prodi | Menunggu SK | ⏳ |
| **Pelaksanaan** | — | Perkuliahan siklus berjalan | — | ⏳ |
| **Evaluasi** | — | Penghitungan ketercapaian CPMK/CPL | — | ⏳ |

Pada siklus pertama, log ini wajar hanya berisi tahap Penetapan. Itu **bukan kelemahan** — ia menunjukkan siklus mutu baru dimulai dan tercatat jujur, yang justru lebih baik di hadapan asesor daripada tabel yang tampak lengkap tanpa dasar.

## 3. Rencana Tindak Lanjut Siklus Berikutnya

Maksimal lima butir, masing-masing tertaut ID capaian agar dapat diverifikasi.

| No | Temuan / Peluang | Tindakan yang direncanakan | Tertaut | Target siklus |
|:-:|---|---|---|---|
| 1 | Butir soal UTS/UAS belum seluruhnya ditandai Sub-CPMK, sehingga pengukuran CPL belum dapat dihitung penuh | Menandai seluruh butir kisi-kisi dan naskah ujian dengan kode Sub-CPMK | Seluruh Sub-CPMK | 2025-2026-genap |
| 2 | Ranah Psikomotorik (P) sebagian besar diukur di INF-102; rujukan silang belum formal | Menyusun mekanisme rujukan silang nilai unjuk kerja INF-102 ke CPMK INF-101 | Sub-CPMK ber-ranah P | 2026-2027-genap |
| 3 | Ambang ketercapaian masih berstatus usulan | Mengajukan penetapan ambang ke program studi | — | 2025-2026-genap |
| 4 | Tema proyek berdampak belum terhimpun sebagai bukti kriteria 4 | Menghimpun README proyek bertanda `#berdampak` sebagai lampiran bukti PkM | Sub-CPMK-7.9, 7.10 | 2025-2026-genap |

## 4. Riwayat Perubahan

Repositori ini berbasis git, sehingga **riwayat commit adalah jejak bukti PPEPP yang paling kredibel** — ia memperlihatkan *apa* yang berubah, *kapan*, dan *mengapa*, tanpa memerlukan dokumen tambahan.

| Penanda | Keterangan |
|---|---|
| `pra-migrasi-kode-v1` | Keadaan dokumen sebelum penggantian kode Sub-CPMK — titik balik bila diperlukan |
| *(akan ditambahkan)* `siklus-2025-2026-genap` | Penanda penetapan dokumen untuk siklus berjalan |

**Cara membaca bukti peningkatan antar siklus:**

```
git diff siklus-2025-2026-genap..siklus-2026-2027-genap -- mata-kuliah/algoritma-pemrograman/
```

Perintah tersebut memperlihatkan seluruh perubahan RPS, materi, dan asesmen antar dua siklus — inilah bukti *continuous quality improvement* yang diminta kriteria 1 (Budaya Mutu).

## 5. Telaah Sejawat

| Peran | Nama | Tanggal | Catatan |
|---|---|---|---|
| Penyusun | Tri Aji Nugroho, S.T., M.T. | 2026-09-05 | Penetapan siklus 2025-2026-genap |
| Penelaah sejawat | 🔲 *(menunggu)* | | |
| Pengesahan prodi | 🔲 *(menunggu)* | | |

Telaah sejawat atas RPS dan rubrik merupakan bukti langsung kriteria **Budaya Mutu**; karena itu tabel ini bagian dari artefak, bukan formalitas.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
