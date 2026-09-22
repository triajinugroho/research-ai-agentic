# BAB 8: PARADIGMA DAN RANCANGAN PENELITIAN

**Bahan rujukan penyelarasan kurikulum** — disusun Tri Aji Nugroho, S.T., M.T.
Pengampu mata kuliah menurut registri: **Andi Arniaty Arsyad, Ph.D.** (`AAA`).

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `METPEN-Sub-CPMK071-1` | Menentukan (C4) metode penelitian yang sesuai dengan pertanyaan, dengan alasan yang tertulis dan alternatif yang dipertimbangkan | C4 |

Setelah membaca bab ini, pembaca diharapkan mampu:

1. **Membedakan** (C2) paradigma penelitian dan implikasinya.
2. **Membedakan** (C2) empat kelompok rancangan.
3. **Memilih** (C4) rancangan yang sesuai dengan bentuk pertanyaan.
4. **Mempertahankan** (C5) pilihan terhadap alternatif yang ditolak.

---

## 8.1 Paradigma

### 8.1.1 Apa yang Dianggap Bukti

| Paradigma | Anggapan dasar | Bentuk bukti yang dihargai |
|-----------|----------------|---------------------------|
| **Positivis / pasca-positivis** | Ada kenyataan yang dapat diukur secara objektif | Pengukuran, uji statistik, replikasi |
| **Interpretif** | Kenyataan dimaknai berbeda oleh tiap orang | Narasi, makna, konteks |
| **Pragmatis** | Yang penting adalah menjawab pertanyaan | Apa pun yang sesuai; sering campuran |
| **Kritis** | Penelitian harus mengungkap ketimpangan | Analisis kuasa dan struktur |

### 8.1.2 Mengapa Perlu Dipahami

Mahasiswa jarang perlu menyatakan paradigmanya secara eksplisit dalam
proposal Tugas Akhir. Memahaminya tetap perlu, karena ia **mencegah tuntutan
yang tidak sesuai**.

| Tuntutan yang keliru | Sebabnya |
|---------------------|----------|
| Menuntut generalisasi dari studi kasus | Studi kasus tidak dirancang untuk itu |
| Menuntut kedalaman makna dari survei tertutup | Survei tidak dapat memberikannya |
| Menuntut angka dari penelitian interpretif | Bukan bentuk bukti yang dihargainya |
| Menuntut objektivitas penuh dari pengamatan partisipatif | Kehadiran peneliti adalah bagian metodenya |

Pertanyaan penguji "berapa persen responden yang…" pada penelitian kualitatif
dengan 12 narasumber adalah tuntutan yang tidak sesuai — dan mahasiswa yang
memahami paradigmanya dapat menjelaskan mengapa.

---

## 8.2 Empat Kelompok Rancangan

### 8.2.1 Perbandingannya

| Rancangan | Menjawab | Data | Contoh di Informatika |
|-----------|----------|------|----------------------|
| **Kuantitatif** | Berapa; apakah A memengaruhi B | Angka | Eksperimen membandingkan dua antarmuka |
| **Kualitatif** | Mengapa; bagaimana | Teks, pengamatan | Studi kasus adopsi sistem di satu dinas |
| **Campuran** | Keduanya, berurutan atau bersamaan | Keduanya | Survei lalu wawancara mendalam |
| **Perancangan** | Dapatkah artefak memenuhi kebutuhan | Kriteria evaluasi | Membangun dan mengevaluasi metode baru |

### 8.2.2 Rancangan Kuantitatif

| Jenis | Ciri | Kapan sesuai | Kesulitan khas |
|-------|------|--------------|----------------|
| **Eksperimen murni** | Penugasan acak, kelompok kontrol | Menguji sebab-akibat dengan kendali penuh | Sulit pada organisasi nyata |
| **Kuasi-eksperimen** | Tanpa penugasan acak | Konteks nyata | Ancaman validitas internal lebih besar |
| **Survei korelasional** | Mengukur hubungan | Banyak variabel, satu waktu | Tidak dapat menyimpulkan sebab |
| **Analisis data arsip** | Data yang sudah ada | Log sistem, repositori kode | Data tidak dikumpulkan untuk tujuan ini |

> **Kuasi-eksperimen** paling sering realistis untuk Tugas Akhir yang
> melibatkan organisasi nyata. Penugasan acak jarang dapat dilakukan — dinas
> tidak akan mengacak staf mana yang memakai sistem mana. Yang penting adalah
> **menyatakan konsekuensinya** terhadap kekuatan simpulan (Bab 10).

### 8.2.3 Rancangan Kualitatif

| Jenis | Ciri | Kapan sesuai | Kesulitan khas |
|-------|------|--------------|----------------|
| **Studi kasus** | Satu atau beberapa kasus, mendalam | Fenomena dalam konteks nyatanya | Sering disalahpahami sebagai "penelitian di satu tempat" |
| **Fenomenologi** | Pengalaman yang dihayati | Bagaimana orang mengalami sesuatu | Menuntut kemampuan wawancara mendalam |
| ***Grounded theory*** | Teori dibangun dari data | Belum ada teori yang memadai | Menuntut iterasi pengumpulan-analisis |
| **Etnografi** | Pengamatan berkepanjangan | Budaya kerja, praktik sehari-hari | Menuntut waktu lapangan yang panjang |

### 8.2.4 Studi Kasus yang Sering Disalahpahami

Studi kasus **bukan** berarti "penelitian yang dilakukan di satu tempat". Ia
rancangan dengan aturannya sendiri.

| Aturan | Penjelasan |
|--------|------------|
| Unit analisis ditetapkan | Apa yang menjadi "kasus": satu organisasi? satu proyek? satu orang? |
| Batas kasus ditetapkan | Di mana kasus berakhir |
| **Beberapa sumber bukti** | Wawancara + dokumen + pengamatan + log |
| Rantai bukti | Setiap temuan dapat ditelusuri ke sumbernya |
| Kasus dipilih dengan alasan | Bukan karena kebetulan dapat diakses |

Baris ketiga adalah syarat yang paling sering tidak dipenuhi. Studi kasus
yang hanya memakai wawancara kehilangan kekuatan utamanya, yaitu
**triangulasi**.

Baris terakhir menuntut kejujuran. Kasus yang dipilih karena itulah yang
dapat diakses adalah keadaan yang wajar — dan harus dinyatakan sebagai
pembatasan, bukan disamarkan sebagai pemilihan purposif.

---

## 8.3 Penelitian Perancangan

### 8.3.1 Siklusnya

```
   ┌─────────────────────────────────────────────┐
   │  1. Identifikasi masalah & motivasi         │
   │  2. Tetapkan tujuan solusi (KRITERIA)       │
   │  3. Rancang & bangun artefak                │
   │  4. Demonstrasi                             │
   │  5. EVALUASI  ◄── terhadap kriteria         │
   │                    dari langkah 2            │
   │  6. Komunikasi                              │
   └─────────────────────────────────────────────┘
          ▲                              │
          └──────── iterasi ◄────────────┘
```

### 8.3.2 Apa yang Membedakannya dari Pengembangan

| Pembeda | Penjelasan |
|---------|------------|
| **Kriteria ditetapkan sebelum membangun** | Langkah 2 mendahului langkah 3 |
| **Evaluasi memakai pembanding** | Terhadap keadaan sekarang atau pendekatan lain |
| **Kontribusi berupa pengetahuan** | Bukan hanya artefaknya |
| **Keterbatasan artefak dilaporkan** | Termasuk di mana ia gagal |
| Iterasi didokumentasikan | Apa yang diubah, mengapa |

Urutan langkah 2 sebelum 3 adalah yang paling sering dilanggar. Kriteria yang
ditetapkan setelah artefak jadi selalu terpenuhi — dan penelitian yang
demikian tidak menghasilkan pengetahuan apa pun.

### 8.3.3 Iterasi yang Dicatat

Iterasi adalah bagian sah dari penelitian perancangan. Yang membedakannya
dari coba-coba adalah **pencatatan**.

```markdown
## Iterasi #2 — 3 Desember 2026

Yang diubah : Cara memasukkan data diubah dari formulir
              bertahap menjadi satu layar

Karena      : Pada uji iterasi #1, 4 dari 5 peserta berhenti
              di langkah ketiga. Tiga menyebut alasan yang
              sama: tidak tahu berapa langkah lagi tersisa.

Kriteria yang terpengaruh: K-01 (waktu ≤3 menit)
              Sebelum: rata-rata 4,7 menit
              Sesudah: rata-rata 3,1 menit

Yang TIDAK diubah: kriteria dan ambangnya
```

Baris terakhir penting. Iterasi mengubah artefak, **bukan kriterianya**.
Kriteria yang berubah di tengah harus dicatat sebagai perubahan tersendiri
dengan alasan yang terpisah.

---

## 8.4 Memilih dengan Alasan

### 8.4.1 Tabel Pemilihan

| Aspek | Rancangan pilihan | Alternatif 1 (ditolak) | Alternatif 2 (ditolak) |
|-------|-------------------|------------------------|------------------------|
| Nama rancangan | Studi kasus jamak, 3 dinas | Survei ke 100 dinas | Kuasi-eksperimen |
| Menjawab RQ1 ("mengapa")? | Ya | **Tidak** — kuesioner tidak menjawab "mengapa" | Tidak |
| Menjawab RQ2 ("bagaimana berkaitan")? | Ya — analisis lintas kasus | Sebagian | Tidak |
| Data dapat diperoleh? | Ya — 3 dinas bersedia (surel 12 Okt) | **Tidak** — tidak ada daftar kontak; tingkat balasan survei dinas 8–15% | Tidak — tidak mungkin mengacak |
| Waktu cukup (10 minggu)? | Ya — 3 × 2 minggu + analisis | Ya | Tidak |
| Keterampilan tersedia? | Ya — analisis tematik | Ya | Tidak — analisis eksperimental |
| Kekuatan | Kedalaman; konteks terlihat | Cakupan luas | Kekuatan kausal |
| **Kelemahan yang diterima** | **Tidak dapat digeneralisasi** | Tidak menjelaskan sebab | — |

### 8.4.2 Baris Terakhir

Baris "kelemahan yang diterima" adalah yang paling sering ditanyakan penguji
dan paling menunjukkan kematangan.

| Pertanyaan penguji | Jawaban yang lemah | Jawaban yang kuat |
|--------------------|--------------------|-------------------|
| "Apakah hasilnya dapat digeneralisasi?" | "Bisa, karena ketiga dinas mewakili…" | "Tidak. Rancangan ini menghasilkan pemahaman mendalam pada tiga kasus, bukan generalisasi statistik. Yang dapat dipindahkan adalah kerangka pemetaannya, yang dapat diuji pada kasus lain." |
| "Mengapa tidak survei saja?" | "Kami merasa studi kasus lebih cocok" | "Survei tidak dapat menjawab RQ1 yang bertanya 'mengapa'. Selain itu tingkat balasan survei dinas pada penelitian serupa 8–15% [sumber], yang dari 100 dinas menghasilkan 8–15 responden — tidak lebih banyak dari yang kami wawancarai." |

Setiap rancangan menukar sesuatu. Peneliti yang mengetahui apa yang
ditukarnya berdiri di atas dasar yang kokoh; yang mengklaim rancangannya
tidak memiliki kelemahan kehilangan kepercayaan.

### 8.4.3 Rencana Cadangan

Akses yang gagal adalah penyebab paling umum Tugas Akhir tertunda.

```markdown
## Rencana Cadangan

Bila akses ke 3 dinas gagal (sebagian atau seluruhnya):

Skenario A — 2 dari 3 dinas tersedia
  Rancangan tetap; dinyatakan sebagai 2 kasus
  RQ2 tetap dapat dijawab dengan perbandingan terbatas

Skenario B — hanya 1 dinas tersedia
  Rancangan berubah menjadi studi kasus tunggal
  RQ2 diubah: dari perbandingan antarlayanan dalam satu dinas
  Konsekuensi: kontribusi diturunkan; dinyatakan di §1.6

Skenario C — tidak ada akses lembaga
  Rancangan berubah menjadi wawancara individu pengguna
  yang dihubungi secara pribadi
  RQ1 tetap; RQ2 dibatalkan
  Tenggat memutuskan: Minggu 11
```

Baris terakhir — tenggat memutuskan — adalah yang membuat rencana cadangan
berguna. Tanpa tenggat, tim menunggu terus sampai terlambat berpindah.

---

## AI Corner — Bab 8

### Batas Pemakaian

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI menjelaskan ciri sebuah rancangan | Meminta AI memilih rancangan untuk Anda |
| Meminta AI menyebutkan rancangan yang mungkin terlewat sebagai kandidat | Menerima pilihan AI tanpa menilai kelayakannya |
| Meminta AI berperan sebagai penguji atas pilihan Anda | Meminta AI menjawab pertanyaan penguji |
| Meminta AI menjelaskan istilah metodologis | Meminta AI menilai apakah rancangan Anda "sudah benar" |

### Kecenderungan Model

| Kecenderungan | Sebabnya |
|---------------|----------|
| Mengusulkan eksperimen dengan kelompok kontrol | Rancangan yang paling sering ditulis dalam pustaka metodologi |
| Mengusulkan ukuran sampel besar | Angka yang lazim dalam contoh buku teks |
| Mengabaikan kendala akses | Tidak mengetahui keadaan Anda |
| Mengusulkan rancangan campuran | Terdengar menyeluruh; sering tidak layak dalam 10 minggu |

Rancangan yang tepat bergantung pada hal yang tidak diketahui model: berapa
lama waktu Anda tersisa, lembaga mana yang sudah bersedia, keterampilan
analisis apa yang Anda kuasai, dan siapa pembimbing Anda.

### Pemakaian yang Dianjurkan

```
Berikut RQ saya dan keadaan nyata penelitian saya:
RQ            : [tempelkan, dengan bentuk masing-masing]
Waktu tersisa : 10 minggu
Akses         : 3 dinas bersedia (surel 12 Okt); 1 belum menjawab
Keterampilan analisis yang saya kuasai : [sebutkan]
Rancangan yang saya pilih : [sebutkan]

Tugas Anda:
1. Berperanlah sebagai penguji. Ajukan 5 pertanyaan tersulit
   tentang pilihan rancangan saya.
2. Sebutkan rancangan lain yang mungkin belum saya
   pertimbangkan — hanya namanya dan satu alasan.
3. Untuk setiap RQ, sebutkan rancangan yang TIDAK dapat
   menjawabnya.

Jangan merekomendasikan rancangan. Jangan menjawab pertanyaan
yang Anda ajukan sendiri.
```

---

## Latihan Soal

### Tingkat Dasar

1. Sebutkan empat paradigma dan bentuk bukti yang dihargai masing-masing.
2. Mengapa memahami paradigma mencegah tuntutan yang tidak sesuai?
3. Sebutkan empat kelompok rancangan dan pertanyaan yang dijawabnya.
4. Sebutkan lima aturan studi kasus yang membedakannya dari "penelitian di satu tempat".
5. Sebutkan lima pembeda penelitian perancangan dari pengembangan biasa.

### Tingkat Menengah

6. Untuk setiap RQ berikut, tentukan rancangan yang sesuai dan satu yang **tidak** dapat menjawabnya:
   - "Berapa proporsi aplikasi pemda yang memenuhi kriteria aksesibilitas?"
   - "Mengapa staf berhenti memakai sistem setelah bulan ketiga?"
   - "Apakah pelatihan menaikkan intensitas pemakaian?"
   - "Dapatkah metode P menurunkan waktu pemrosesan tanpa menurunkan ketelitian?"

7. Susun tabel pemilihan rancangan lengkap untuk penelitian Anda, dengan dua alternatif yang ditolak dan baris "kelemahan yang diterima".

8. Sebuah tim memilih kuasi-eksperimen karena penugasan acak tidak mungkin. Sebutkan tiga ancaman validitas internal yang menjadi lebih besar karenanya, dan bagaimana masing-masing dapat dikurangi.

9. Susun rencana cadangan untuk penelitian Anda dengan minimal dua skenario, masing-masing menyebutkan: apa yang berubah pada rancangan, apa yang berubah pada RQ, konsekuensinya bagi kontribusi, dan **tenggat memutuskan**.

### Tingkat Mahir

10. Ambil satu makalah penelitian perancangan dari matriks Bab 4. Telusuri: apakah kriteria evaluasinya ditetapkan sebelum atau sesudah pembangunan? Bagaimana Anda mengetahuinya dari naskahnya? Bila tidak dapat dipastikan, apa yang kurang dari pelaporannya?

11. Siapkan jawaban untuk sepuluh pertanyaan penguji tentang pilihan rancangan Anda. Untuk setiap jawaban, tunjukkan bagian dokumen mana yang mendukungnya. Tandai pertanyaan yang belum dapat Anda jawab dan susun rencana memperoleh jawabannya.

12. Susun dua versi rancangan untuk RQ yang sama: satu yang menghasilkan bukti terkuat tanpa batasan sumber daya, satu yang layak dengan waktu dan akses yang benar-benar Anda miliki. Bandingkan keduanya: apa yang hilang, apa yang tetap dapat disimpulkan, dan bagaimana Anda akan menyatakan perbedaan itu dalam proposal.

---

## Rangkuman

| Gagasan pokok | Rumusan singkat |
|---------------|-----------------|
| Paradigma | Menentukan apa yang dianggap bukti; mencegah tuntutan yang tidak sesuai |
| Kuasi-eksperimen | Paling realistis pada organisasi nyata; konsekuensinya dinyatakan |
| Studi kasus | Bukan "penelitian di satu tempat"; menuntut beberapa sumber bukti |
| Kasus yang dipilih karena dapat diakses | Wajar; dinyatakan sebagai pembatasan, bukan disamarkan |
| Penelitian perancangan | Kriteria mendahului pembangunan |
| Iterasi | Mengubah artefak, bukan kriterianya |
| Tabel pemilihan | Dua alternatif ditolak dengan alasan konkret |
| Kelemahan yang diterima | Paling sering ditanyakan; paling menunjukkan kematangan |
| Rencana cadangan | Berguna hanya bila ada tenggat memutuskan |
| Batas AI | Rancangan bergantung pada keadaan Anda yang tidak diketahui model |

---

## Referensi

1. Creswell, J. W., & Creswell, J. D. (2023). *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches* (6th ed.). SAGE Publications.
2. Yin, R. K. (2018). *Case Study Research and Applications: Design and Methods* (6th ed.). SAGE Publications.
3. Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A Design Science Research Methodology for Information Systems Research. *Journal of Management Information Systems*, 24(3), 45–77.
4. Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information Systems Research. *MIS Quarterly*, 28(1), 75–105.
5. Runeson, P., & Höst, M. (2009). Guidelines for Conducting and Reporting Case Study Research in Software Engineering. *Empirical Software Engineering*, 14(2), 131–164.
6. Easterbrook, S., et al. (2008). Selecting Empirical Methods for Software Engineering Research. Dalam *Guide to Advanced Empirical Software Engineering*. Springer.
7. Wieringa, R. J. (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul mingguan | [Minggu 9](../03-modules/week-09-paradigma-dan-rancangan-penelitian.md) |
| Lokakarya | [Lokakarya 9](../04-labs/lab-09-pemilihan-rancangan-penelitian.md) |
| Bab sebelumnya | [Bab 7](bab-07-kerangka-konseptual.md) |
| Bab berikutnya | [Bab 9 — Pengumpulan Data dan Instrumen](bab-09-pengumpulan-data-dan-instrumen.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
