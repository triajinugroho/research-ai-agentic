# Lokakarya 13: Kriteria Evaluasi Artefak

---

## Informasi Lokakarya

| Aspek | Keterangan |
|-------|------------|
| Mata kuliah | Metodologi Penelitian (`IF52510021`) |
| Lokakarya | 13 dari 13 dalam urutan topik — menyertai [Minggu 13](../03-modules/week-13-design-science-dan-evaluasi-artefak.md) |
| Sub-CPMK | `METPEN-Sub-CPMK091-1` |
| Durasi | 30 menit + latihan silang 10 menit |
| Keluaran | **T12** (7%, Unjuk Kerja) |

---

## Tujuan Lokakarya

Menetapkan kriteria evaluasi yang setiap barisnya dapat ditunjuk kembali ke
kendala *stakeholder* yang ditemukan pada Lokakarya 6.

---

## Persiapan

| # | Yang disiapkan |
|---|----------------|
| 1 | **Tabel kendala berkode (K-01, K-02, …) dari T6** |
| 2 | Rancangan penelitian (T8) |
| 3 | Deskripsi artefak yang akan dibangun/dievaluasi |

---

## Langkah-Langkah

### Langkah 1 — Menetapkan Jenis dan Batas Artefak (5 menit)

```markdown
Jenis artefak : konstruk / model / metode / instansiasi
Apa yang dibangun :
Apa yang TIDAK dibangun :
Pengetahuan yang diharapkan dihasilkan :
  (bukan "sistem tersedia", melainkan
   "diketahui bahwa ... pada keadaan ...")
```

> Baris terakhir adalah yang membedakan penelitian perancangan dari
> pengembangan. Instansiasi adalah jenis artefak yang paling sulit
> menghasilkan pengetahuan yang dapat dipindahkan — karena itu bagian ini
> perlu dirumuskan dengan hati-hati.

### Langkah 2 — Menurunkan Kriteria dari Kendala (15 menit)

| Kriteria | **Tertelusur ke** | Cara mengukur | Ambang | Sumber ambang |
|----------|-------------------|---------------|--------|---------------|
| | K-__ (wawancara N_) | | | kendala / keadaan sekarang / pustaka / standar |
| | K-__ | | | |
| | KB-__ | | | |

| Ujian | Bila gagal |
|-------|------------|
| Setiap kriteria punya kolom "tertelusur ke" terisi | Kriteria berasal dari asumsi peneliti |
| Cara mengukur dapat diulang orang lain | Terlalu kabur |
| Ambang berasal dari salah satu dari empat sumber sah | Angka bulat yang terdengar baik tidak sah |
| Kriteria mencakup kendala berkemungkinan tinggi | Kendala terpenting terlewat |

Contoh lengkap:

| Kriteria | Tertelusur ke | Cara mengukur | Ambang | Sumber ambang |
|----------|---------------|---------------|--------|---------------|
| Waktu penyelesaian satu berkas | K-01 (N1, N3: "paling cuma 5 menit per berkas kalau lagi ramai") | Pencatatan waktu, 20 percobaan, 5 pengguna | ≤3 menit | Kendala: 5 menit tersedia, sisanya untuk verifikasi |
| Berjalan pada perangkat kantor | K-02 (pengamatan: 3 unit RAM 4 GB) | Uji pada 3 perangkat nyata | Tanpa galat, respons ≤2 detik | Keadaan sekarang |
| Ketelitian ekstraksi | KB-01 (N1, N2, N3: kesalahan data menyebabkan kerja ulang) | Bandingkan dengan pemeriksaan manual, 200 berkas | ≥95% | Pustaka: [sitasi] pada tugas serupa |

### Langkah 3 — Menetapkan Pembanding (5 menit)

| Pembanding | Apa yang dibandingkan | Bagaimana diukur | Adil? |
|------------|----------------------|------------------|-------|
| Keadaan sekarang | | | |
| [pendekatan lain] | | | |

| Ujian keadilan | Pertanyaan |
|----------------|------------|
| Apakah pembanding disetel dengan usaha yang sebanding? | Atau sengaja dibiarkan lemah? |
| Apakah keadaan sekarang benar-benar diukur? | Atau hanya diperkirakan? |
| Apakah pembanding dipakai pada data yang sama? | Perbandingan pada data berbeda tidak sahih |

> Membandingkan hanya dengan batas bawah yang sengaja lemah adalah bentuk
> ketidakjujuran yang halus. Mengalahkan tebakan acak tidak menunjukkan apa
> pun bila cara yang dipakai orang sekarang jauh lebih baik daripada tebakan
> acak.

### Langkah 4 — Merencanakan Pelaporan Kegagalan (5 menit)

```markdown
## Rencana Pelaporan Hasil Evaluasi

Kriteria yang tidak tercapai akan dilaporkan dengan:
- angka yang dicapai dan selisihnya dari ambang
- keadaan di mana artefak gagal (dengan contoh)
- kemungkinan sebabnya, dengan bukti
- apa yang sudah dicoba dan tidak berhasil

Saya TIDAK akan menurunkan ambang setelah melihat hasil.
Bila ambang ternyata tidak sesuai, perubahannya dicatat
beserta alasan dan tanggalnya.
```

Melaporkan kegagalan **menaikkan** nilai penelitian perancangan. Penelitian
yang seluruh kriterianya tercapai sempurna hampir selalu berarti kriterianya
terlalu longgar atau ditetapkan setelah hasil terlihat.

---

## Untuk Penelitian Non-Artefak

Mahasiswa yang penelitiannya tidak membangun artefak menggantinya dengan
kriteria mutu penelitian:

| Aspek | Kriteria | Ambang | Cara memeriksa |
|-------|----------|--------|----------------|
| Kecukupan data | Saturasi tema | Tidak ada tema baru pada 3 wawancara terakhir | Catatan penandaan per wawancara |
| Kualitas analisis | Kesesuaian antarpenilai | Kappa ≥0,6 pada 20% data | Penandaan silang |
| Ketertelusuran | Setiap tema punya kutipan pendukung | ≥3 kutipan per tema | Rantai bukti |
| Kasus menyimpang | Dicari dan dianalisis | Minimal 1 dicari untuk tiap tema | Catatan |

Penggantian ini disepakati dengan dosen pengampu.

---

## Latihan Silang (10 menit)

Bertukar tabel dengan teman. Untuk setiap ambang, ajukan pertanyaan:

```markdown
## Menantang Ambang
Penulis : [nama]     Penantang : [nama]

Untuk setiap baris:
1. "Mengapa angka itu dan bukan angka lain?"
   Apakah kolom "sumber ambang" menjawabnya? ya / tidak

2. "Bagaimana saya mengukurnya bila saya yang melakukannya?"
   Apakah cara mengukurnya cukup jelas? ya / tidak

3. "Dari kendala mana ini berasal?"
   Apakah kolom penelusuran menunjuk kendala tertentu? ya / tidak

Baris dengan jawaban "tidak" :
```

---

## Tantangan Tambahan

| # | Tantangan |
|---|-----------|
| 1 | Tunjukkan tabel kriteria kepada salah satu narasumber dari T6. Tanyakan: "Kalau sistemnya memenuhi ini semua, apakah Bapak/Ibu akan memakainya?" Catat jawabannya. |
| 2 | Ukur keadaan sekarang secara nyata — berapa lama cara yang dipakai sekarang, berapa tingkat kesalahannya. Tanpa angka ini, pembanding hanya perkiraan. |
| 3 | Untuk setiap kriteria, tulis: "Bila kriteria ini tidak tercapai, apa yang masih dapat saya simpulkan?" |

Tantangan 1 sering mengungkap kriteria yang benar secara teknis tetapi tidak
menyentuh yang paling penting bagi penggunanya.

---

## Daftar Periksa Penyelesaian

| # | Butir | ☐ |
|---|-------|---|
| 1 | Jenis dan batas artefak ditetapkan | ☐ |
| 2 | Pengetahuan yang diharapkan dirumuskan, bukan hanya produknya | ☐ |
| 3 | **Setiap kriteria tertelusur ke kendala berkode dari T6** | ☐ |
| 4 | Cara mengukur setiap kriteria dapat diulang | ☐ |
| 5 | Setiap ambang berasal dari salah satu dari empat sumber sah | ☐ |
| 6 | Pembanding ditetapkan dan diuji keadilannya | ☐ |
| 7 | Keadaan sekarang diukur, bukan diperkirakan | ☐ |
| 8 | Rencana pelaporan kegagalan tertulis | ☐ |
| 9 | Latihan silang dijalankan; baris bermasalah diperbaiki | ☐ |
| 10 | Deklarasi AI disertakan | ☐ |

---

## AI Corner — Lokakarya 13

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI menyebutkan aspek evaluasi yang lazim untuk jenis artefak tertentu | **Menetapkan ambang untuk artefak Anda** |
| Meminta AI memeriksa keterukuran kriteria | Mengisi kolom "tertelusur ke" |
| Meminta AI menanyakan "mengapa angka itu?" untuk tiap ambang | Menerima ambang tanpa menelusurinya ke kendala |
| Meminta AI menyebutkan pembanding yang mungkin terlewat | Menilai apakah artefak Anda "sudah baik" |

Ditanya berapa ambang akurasi yang wajar, model menjawab dengan angka yang
lazim dalam pustaka — 90%, 95%, F1 0,8. Angka itu berasal dari konteks
penelitian lain: tugas berbeda, data berbeda, akibat kesalahan berbeda.

Ambang yang sahih berakar pada keadaan penelitian Anda sendiri.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul | [Minggu 13](../03-modules/week-13-design-science-dan-evaluasi-artefak.md) |
| Bab buku ajar | [Bab 12](../06-buku-ajar/bab-12-design-science-dan-evaluasi-artefak.md) |
| Sumber kendala | [Lokakarya 6](lab-06-analisis-stakeholder-dan-kebutuhan.md) |
| Lokakarya sebelumnya | [Lokakarya 12](lab-12-rencana-analisis-data.md) |
| Lokakarya berikutnya | [Lokakarya 14](lab-14-paket-reproduksi-dan-deklarasi-ai.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
