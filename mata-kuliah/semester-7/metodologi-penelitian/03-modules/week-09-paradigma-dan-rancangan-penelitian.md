# Minggu 9: Paradigma dan Rancangan Penelitian

---

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata kuliah | Metodologi Penelitian (`IF52510021`) |
| Minggu | 9 dari 16 |
| Topik | Memilih rancangan yang menjawab pertanyaan |
| Sub-CPMK | `METPEN-Sub-CPMK071-1` |
| ICM | ICM-08 — Memilih paradigma dan rancangan penelitian dengan alasan yang tertulis |
| Durasi | 2 × 50 menit |
| Metode | Kuliah + lokakarya + pertahanan lisan + **Kuis 2** |
| Bacaan | [Bab 8 — Paradigma dan Rancangan Penelitian](../06-buku-ajar/bab-08-paradigma-dan-rancangan-penelitian.md) |

---

## Tujuan Pembelajaran

1. **Membedakan** (C2) paradigma penelitian dan implikasinya.
2. **Membedakan** (C2) rancangan kuantitatif, kualitatif, campuran, dan *design science*.
3. **Memilih** (C4) rancangan yang sesuai dengan bentuk pertanyaan penelitian.
4. **Mempertahankan** (C5) pilihan itu terhadap alternatif yang ditolak.

---

## Materi Pembelajaran

### 9.1 Paradigma Menentukan Apa yang Dianggap Bukti

| Paradigma | Anggapan dasar | Bentuk bukti yang dihargai |
|-----------|----------------|---------------------------|
| **Positivis / pasca-positivis** | Ada kenyataan yang dapat diukur secara objektif | Pengukuran, uji statistik, replikasi |
| **Interpretif** | Kenyataan dimaknai berbeda oleh tiap orang | Narasi, makna, konteks |
| **Pragmatis** | Yang penting adalah menjawab pertanyaan | Apa pun yang sesuai; sering campuran |
| **Kritis** | Penelitian harus mengungkap ketimpangan | Analisis kuasa dan struktur |

Mahasiswa jarang perlu menyatakan paradigmanya secara eksplisit dalam
proposal Tugas Akhir. Namun **memahaminya mencegah kekeliruan yang umum**:
menuntut generalisasi dari studi kasus, atau menuntut kedalaman makna dari
survei tertutup.

### 9.2 Empat Kelompok Rancangan

| Rancangan | Menjawab | Data | Contoh di Informatika |
|-----------|----------|------|----------------------|
| **Kuantitatif** | Berapa, apakah A memengaruhi B | Angka | Eksperimen membandingkan dua antarmuka |
| **Kualitatif** | Mengapa, bagaimana | Teks, pengamatan | Studi kasus adopsi sistem di satu dinas |
| **Campuran** | Keduanya, berurutan atau bersamaan | Keduanya | Survei lalu wawancara mendalam |
| **Design science** | Dapatkah artefak memenuhi kebutuhan | Kriteria evaluasi | Membangun dan mengevaluasi metode baru |

### 9.3 Rancangan Kuantitatif

| Jenis | Ciri | Kapan sesuai |
|-------|------|--------------|
| **Eksperimen murni** | Penugasan acak, kelompok kontrol | Menguji sebab-akibat dengan kendali penuh |
| **Kuasi-eksperimen** | Tanpa penugasan acak | Konteks nyata; tidak mungkin mengacak |
| **Survei korelasional** | Mengukur hubungan | Banyak variabel, satu waktu |
| **Analisis data arsip** | Data yang sudah ada | Log sistem, repositori kode |

> Kuasi-eksperimen adalah rancangan yang paling sering realistis untuk Tugas
> Akhir yang melibatkan organisasi nyata. Penugasan acak jarang dapat
> dilakukan; yang penting adalah **menyatakan konsekuensinya** terhadap
> kekuatan simpulan (dibahas Minggu 11).

### 9.4 Rancangan Kualitatif

| Jenis | Ciri | Kapan sesuai |
|-------|------|--------------|
| **Studi kasus** | Satu atau beberapa kasus, mendalam | Fenomena dalam konteks nyatanya |
| **Fenomenologi** | Pengalaman yang dihayati | Bagaimana orang mengalami sesuatu |
| ***Grounded theory*** | Teori dibangun dari data | Belum ada teori yang memadai |
| **Etnografi** | Pengamatan berkepanjangan | Budaya kerja, praktik sehari-hari |

Studi kasus adalah yang paling lazim dan paling sering disalahpahami. Studi
kasus **bukan** berarti "penelitian di satu tempat"; ia adalah rancangan
dengan aturannya sendiri — unit analisis yang ditetapkan, beberapa sumber
bukti, dan rantai bukti yang dapat ditelusuri.

### 9.5 *Design Science*

Rancangan yang paling sesuai untuk mayoritas Tugas Akhir Informatika yang
membangun artefak. Siklusnya:

```
   ┌─────────────────────────────────────────────┐
   │  1. Identifikasi masalah & motivasi         │
   │  2. Tetapkan tujuan solusi                  │
   │  3. Rancang & bangun artefak                │
   │  4. Demonstrasi                             │
   │  5. EVALUASI  ◄── terhadap kriteria yang    │
   │                    ditetapkan di langkah 2   │
   │  6. Komunikasi                              │
   └─────────────────────────────────────────────┘
          ▲                              │
          └──────── iterasi ◄────────────┘
```

| Yang membedakan dari pengembangan biasa | Penjelasan |
|-----------------------------------------|------------|
| Kriteria ditetapkan **sebelum** membangun | Langkah 2 mendahului langkah 3 |
| Evaluasi memakai pembanding | Terhadap *baseline* atau keadaan sekarang |
| Kontribusi berupa pengetahuan | Bukan hanya artefaknya |
| Keterbatasan artefak dilaporkan | Termasuk di mana ia gagal |

Kriteria evaluasi dibahas tuntas pada Minggu 13.

### 9.6 Memilih dengan Alasan

Tabel pemilihan yang menjadi isi T8:

| Aspek | Rancangan pilihan | Alternatif 1 (ditolak) | Alternatif 2 (ditolak) |
|-------|-------------------|------------------------|------------------------|
| Nama rancangan | Studi kasus jamak, 3 dinas | Survei ke 100 dinas | Eksperimen |
| Menjawab RQ? | Ya — RQ bertanya "mengapa" | Tidak dapat menjawab "mengapa" | RQ bukan tentang sebab-akibat |
| Data dapat diperoleh? | Ya — 3 dinas sudah menyatakan bersedia | Tingkat balasan survei dinas rendah | Tidak mungkin mengacak |
| Waktu cukup? | Ya — 3 × 2 minggu | Ya | Tidak |
| Kekuatan | Kedalaman; konteks | Cakupan luas | Kekuatan kausal |
| Kelemahan yang diterima | Tidak dapat digeneralisasi | Tidak menjelaskan sebab | — |

> Baris "kelemahan yang diterima" adalah baris yang paling sering ditanyakan
> penguji dan paling menunjukkan kematangan. Setiap rancangan menukar sesuatu;
> peneliti yang mengetahui apa yang ditukarnya berdiri di atas dasar yang
> kokoh.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

| # | Kegiatan |
|---|----------|
| 1 | Membaca [Bab 8](../06-buku-ajar/bab-08-paradigma-dan-rancangan-penelitian.md) |
| 2 | Mencatat rancangan yang dipakai 5 makalah dari matriks T4 |

### Di Kelas (100 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10 | **Kuis 2** — mencocokkan bentuk RQ dengan rancangan |
| 10–20 | Pembahasan hasil UTS |
| 20–45 | Kuliah: paradigma; empat kelompok rancangan; *design science* |
| 45–55 | **Rehat** |
| 55–80 | **Lokakarya 9** — [Pemilihan Rancangan Penelitian](../04-labs/lab-09-pemilihan-rancangan-penelitian.md) |
| 80–100 | **Pertahanan lisan T8** (5 menit per mahasiswa, bergilir); sisanya dijadwalkan |

### Setelah Kelas

| # | Kegiatan |
|---|----------|
| 1 | Menyelesaikan **T8 — Pemilihan rancangan + pertahanan** (5%) |
| 2 | Membaca [Bab 9](../06-buku-ajar/bab-09-pengumpulan-data-dan-instrumen.md) |

---

## Penugasan

### T8 — Pemilihan Rancangan Penelitian (5%, Unjuk Kerja)

| Aspek | Ketentuan |
|-------|-----------|
| Keluaran | Dokumen 2 halaman + pertahanan lisan 5 menit |
| Isi | Rancangan terpilih · **dua alternatif yang dipertimbangkan dan alasan ditolak** · kesesuaian dengan tiap RQ · kelayakan waktu dan sumber daya · kelemahan yang diterima |
| Tenggat | Minggu 9 |

---

## AI Corner — Minggu 9

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI menjelaskan ciri sebuah rancangan | Meminta AI memilih rancangan untuk penelitian Anda |
| Meminta AI menyebutkan rancangan yang mungkin Anda lewatkan sebagai alternatif | Menerima pilihan AI tanpa memeriksa kelayakannya sendiri |
| Meminta AI berperan sebagai penguji yang menanyakan pilihan Anda | Meminta AI menjawab pertanyaan penguji |
| Meminta AI menjelaskan istilah metodologis | Meminta AI menilai apakah rancangan Anda "sudah benar" |

### Mengapa Pemilihan Rancangan Tidak Dapat Diwakilkan

Rancangan yang tepat bergantung pada hal-hal yang tidak diketahui model:
berapa lama waktu Anda tersisa, lembaga mana yang sudah bersedia memberi
akses, keterampilan analisis apa yang Anda kuasai, dan siapa pembimbing
Anda. Rancangan yang disusun tanpa mengetahui hal-hal itu adalah rancangan
untuk peneliti yang tidak ada.

Lebih jauh, model cenderung mengusulkan rancangan yang **paling sering
ditulis dalam pustaka metodologi** — biasanya eksperimen dengan kelompok
kontrol — yang justru paling jarang dapat dijalankan mahasiswa dalam
organisasi nyata.

### Pemakaian yang Dianjurkan

```
Berikut RQ saya dan keadaan nyata penelitian saya:
RQ  : [tempelkan]
Waktu tersisa : 10 minggu
Akses  : 3 dinas bersedia; 1 belum dijawab
Keterampilan analisis yang saya kuasai : [sebutkan]
Rancangan yang saya pilih : [sebutkan]

Tugas Anda:
1. Berperanlah sebagai penguji. Ajukan 5 pertanyaan tersulit
   tentang pilihan rancangan saya.
2. Sebutkan rancangan lain yang mungkin belum saya
   pertimbangkan — hanya namanya dan satu alasan.

Jangan merekomendasikan rancangan. Jangan menjawab
pertanyaan yang Anda ajukan.
```

---

## Referensi

1. Creswell, J. W., & Creswell, J. D. (2023). *Research Design* (6th ed.). SAGE Publications.
2. Yin, R. K. (2018). *Case Study Research and Applications* (6th ed.). SAGE Publications.
3. Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A Design Science Research Methodology for Information Systems Research. *Journal of Management Information Systems*, 24(3), 45–77.
4. Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information Systems Research. *MIS Quarterly*, 28(1), 75–105.
5. Easterbrook, S., et al. (2008). Selecting Empirical Methods for Software Engineering Research. Dalam *Guide to Advanced Empirical Software Engineering*. Springer.
6. Wohlin, C., et al. (2012). *Experimentation in Software Engineering*. Springer.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Bab buku ajar | [Bab 8](../06-buku-ajar/bab-08-paradigma-dan-rancangan-penelitian.md) |
| Lokakarya | [Lokakarya 9](../04-labs/lab-09-pemilihan-rancangan-penelitian.md) |
| Minggu sebelumnya | [Minggu 8 — UTS](week-08-uts-review-dan-ujian.md) |
| Minggu berikutnya | [Minggu 10](week-10-pengumpulan-data-dan-instrumen.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
