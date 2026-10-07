# Minggu 13: *Design Science* dan Evaluasi Artefak

---

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata kuliah | Metodologi Penelitian (`IF52510021`) |
| Minggu | 13 dari 16 |
| Topik | Menilai artefak dengan kriteria yang tertelusur ke kebutuhan |
| Sub-CPMK | `METPEN-Sub-CPMK091-1` |
| ICM | ICM-12 — Menetapkan kriteria evaluasi artefak yang tertelusur ke kebutuhan *stakeholder* |
| Durasi | 2 × 50 menit |
| Metode | Kuliah + lokakarya |
| Bacaan | [Bab 12 — *Design Science* dan Evaluasi Artefak](../06-buku-ajar/bab-12-design-science-dan-evaluasi-artefak.md) |

---

## Tujuan Pembelajaran

1. **Menjelaskan** (C2) apa yang membuat pembangunan artefak menjadi penelitian.
2. **Menetapkan** (C4) kriteria evaluasi yang tertelusur ke kebutuhan *stakeholder*.
3. **Memilih** (C4) pembanding yang wajar.
4. **Menetapkan** (C5) ambang keberhasilan beserta alasannya.

---

## Materi Pembelajaran

### 13.1 Kapan Membangun Menjadi Penelitian

| Membangun saja | Penelitian perancangan |
|----------------|------------------------|
| Tujuan: sistem berfungsi | Tujuan: menjawab pertanyaan |
| Kriteria: berjalan tanpa galat | Kriteria ditetapkan dari kebutuhan, sebelum membangun |
| Pembanding: tidak ada | Pembanding: keadaan sekarang atau pendekatan lain |
| Laporan: cara membangun | Laporan: apa yang dipelajari |
| Kegagalan: tidak dilaporkan | **Kegagalan: temuan** |

Pertanyaan yang memisahkan keduanya: *setelah artefak ini selesai, apa yang
kita ketahui yang tidak kita ketahui sebelumnya?*

### 13.2 Empat Jenis Artefak

| Jenis | Contoh | Pengetahuan yang dihasilkan |
|-------|--------|----------------------------|
| **Konstruk** | Kosakata, taksonomi, skema pelabelan | Cara memandang persoalan |
| **Model** | Kerangka, representasi, arsitektur | Hubungan antarbagian persoalan |
| **Metode** | Algoritma, prosedur, teknik | Cara mengerjakan yang lebih baik |
| **Instansiasi** | Sistem, prototipe, alat | Bahwa sesuatu dapat diwujudkan dan bagaimana perilakunya |

Mayoritas Tugas Akhir menghasilkan instansiasi. Kelemahan khasnya: instansiasi
adalah jenis artefak yang **paling sulit menghasilkan pengetahuan yang dapat
dipindahkan**, karena banyak hal yang menentukan keberhasilannya khas pada
sistem itu.

Cara mengatasinya: **menarik keluar yang dapat dipindahkan**. Bukan "sistem
ini berhasil", melainkan "pendekatan X berhasil pada keadaan Y, dan gagal
ketika Z".

### 13.3 Kriteria Evaluasi yang Tertelusur

Inilah inti tugas T12 dan indikator kedua Sub-CPMK 091-1.

| Kriteria | Ambang | Cara mengukur | **Tertelusur ke** |
|----------|--------|---------------|-------------------|
| Waktu penyelesaian satu berkas | ≤3 menit | Pencatatan waktu, 20 percobaan, 5 pengguna | Kendala K-01 (staf punya 5 menit/berkas pada jam sibuk) — wawancara N1, N3 |
| Berjalan pada perangkat lama | RAM 4 GB, tanpa galat | Uji pada 3 perangkat kantor nyata | Kendala K-02 (spesifikasi komputer kantor) — pengamatan |
| Tahan koneksi terputus | Pekerjaan tidak hilang bila terputus ≤10 menit | Uji dengan pemutusan buatan, 10 kali | Kendala K-03 (jaringan sering terputus) — wawancara N2, log |
| Dapat dipakai tanpa pelatihan | ≥4 dari 5 pengguna baru selesai tanpa dipandu | Uji pengguna, tugas baku | Kendala K-04 (pergantian staf tinggi) — wawancara N1 |
| Ketelitian ekstraksi data | ≥95% | Bandingkan dengan pemeriksaan manual, 200 berkas | Kebutuhan KB-01 (kesalahan data menyebabkan kerja ulang) — wawancara N1, N2, N3 |

| Kolom | Mengapa wajib |
|-------|---------------|
| Ambang | Angka, ditetapkan sebelum evaluasi |
| Cara mengukur | Prosedur yang dapat diulang |
| **Tertelusur ke** | **Menghubungkan kembali ke bukti lapangan Minggu 6** |

Kolom terakhir adalah yang membedakan kriteria penelitian dari daftar
keinginan pengembang. Kriteria tanpa kolom itu berasal dari asumsi peneliti,
dan tidak dapat dipertahankan ketika ditanya "mengapa 3 menit, bukan 5?".

### 13.4 Menetapkan Ambang

| Sumber ambang | Contoh | Kekuatan |
|---------------|--------|----------|
| **Kendala lapangan** | 3 menit, karena staf punya 5 menit dan butuh sisa untuk verifikasi | Kuat |
| **Keadaan sekarang** | Lebih baik dari cara manual yang memakan 8 menit | Kuat |
| **Pustaka** | Ketelitian ≥95%, sesuai [sumber] pada tugas serupa | Kuat |
| **Standar yang berlaku** | Sesuai pedoman aksesibilitas | Kuat |
| Angka bulat yang terdengar baik | "Akurasi 90%" | **Lemah** |

Baris terakhir adalah kesalahan yang paling sering. Angka 90% tidak berasal
dari mana pun — dan pertanyaan pertama penguji hampir selalu "mengapa 90%?".

### 13.5 Memilih Pembanding

| Pembanding | Kapan sesuai | Bahaya |
|------------|--------------|--------|
| **Keadaan sekarang** | Hampir selalu; paling bermakna | Sulit diukur bila tidak tercatat |
| Pendekatan lain dari pustaka | Bila ada yang setara | Implementasi ulang mungkin tidak adil |
| Versi sederhana dari artefak sendiri | Menguji sumbangan tiap bagian | — |
| Batas bawah (*naive baseline*) | Menunjukkan bahwa persoalan tidak sepele | Tidak cukup sendirian |

> Membandingkan hanya dengan batas bawah yang sengaja lemah adalah bentuk
> ketidakjujuran yang halus. Sebuah metode yang mengalahkan tebakan acak
> belum menunjukkan apa pun bila cara yang dipakai orang sekarang jauh lebih
> baik daripada tebakan acak.

### 13.6 Melaporkan Kegagalan

| Yang wajib dilaporkan | Contoh |
|-----------------------|--------|
| Kriteria yang tidak tercapai | "Waktu penyelesaian 3,8 menit; ambang 3 menit tidak tercapai" |
| Keadaan di mana artefak gagal | "Gagal pada berkas dengan tulisan tangan; 12% dari sampel" |
| Kemungkinan sebabnya | Dengan bukti, bukan dugaan |
| Apa yang sudah dicoba | Iterasi yang tidak berhasil |

Melaporkan kegagalan **menaikkan** nilai sebuah penelitian perancangan.
Penelitian yang seluruh kriterianya tercapai sempurna hampir selalu berarti
kriterianya terlalu longgar atau ditetapkan setelah hasil terlihat.

### 13.7 Untuk Penelitian Non-Artefak

Mahasiswa yang penelitiannya tidak membangun artefak mengganti T12 dengan
kriteria mutu penelitian yang setara:

| Aspek | Kriteria |
|-------|----------|
| Kecukupan data | Ambang saturasi; ukuran sampel minimum |
| Kualitas analisis | Pemeriksaan kesesuaian; kasus menyimpang dicari |
| Ketertelusuran | Setiap temuan dapat ditunjuk ke data |
| Keterbatasan | Dinyatakan dan dianalisis akibatnya |

Penggantian ini disepakati dengan dosen pengampu.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

| # | Kegiatan |
|---|----------|
| 1 | Membaca [Bab 12](../06-buku-ajar/bab-12-design-science-dan-evaluasi-artefak.md) |
| 2 | Membuka kembali tabel kendala→kriteria dari T6 |

### Di Kelas (100 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10 | Umpan balik T11 |
| 10–35 | Kuliah: kapan membangun menjadi penelitian; empat jenis artefak |
| 35–50 | Kuliah: kriteria tertelusur; menetapkan ambang; memilih pembanding |
| 50–60 | **Rehat** |
| 60–90 | **Lokakarya 13** — [Kriteria Evaluasi Artefak](../04-labs/lab-13-kriteria-evaluasi-artefak.md) |
| 90–100 | Latihan silang: menantang ambang teman dengan pertanyaan "mengapa angka itu?" |

### Setelah Kelas

| # | Kegiatan |
|---|----------|
| 1 | Menyelesaikan **T12 — Kriteria evaluasi artefak** (7%) |
| 2 | Membaca [Bab 13](../06-buku-ajar/bab-13-riset-berbantuan-ai-dan-reproducibility.md) |

---

## Penugasan

### T12 — Kriteria Evaluasi Artefak (7%, Unjuk Kerja) ★

| Aspek | Ketentuan |
|-------|-----------|
| Keluaran | Dokumen 2–3 halaman |
| Isi | Artefak · kriteria **tertelusur ke kebutuhan dari T6** · cara mengukur · ambang + alasan · pembanding |
| Non-artefak | Diganti kriteria mutu penelitian, disepakati dengan dosen |
| Tenggat | Akhir Minggu 13 |

---

## AI Corner — Minggu 13

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI menyebutkan aspek evaluasi yang biasa dipakai untuk jenis artefak tertentu | **Meminta AI menetapkan ambang untuk artefak Anda** |
| Meminta AI memeriksa apakah kriteria Anda terukur | Meminta AI mengisi kolom "tertelusur ke" |
| Meminta AI menanyakan "mengapa angka itu?" untuk tiap ambang | Menerima ambang dari AI tanpa menelusurinya ke kendala lapangan |
| Meminta AI menyebutkan pembanding yang mungkin terlewat | Meminta AI menilai apakah artefak Anda "sudah baik" |

### Mengapa Ambang dari AI Tidak Dapat Dipakai

Ditanya berapa ambang akurasi yang wajar, model bahasa akan menjawab dengan
angka yang lazim dalam pustaka — 90%, 95%, F1 0,8. Angka-angka itu berasal
dari **konteks penelitian lain**: tugas yang berbeda, data yang berbeda, dan
akibat kesalahan yang berbeda.

Ambang yang sahih berasal dari salah satu dari empat sumber pada §13.4,
seluruhnya berakar pada keadaan penelitian Anda sendiri. Ambang yang diambil
dari jawaban model masuk ke baris terakhir tabel itu: angka bulat yang
terdengar baik.

### Pemakaian yang Dianjurkan — Penantang Ambang

```
Berikut kriteria evaluasi artefak saya, dengan ambang dan
penelusurannya ke kendala lapangan:
[tempelkan tabel lengkap dengan kolom "tertelusur ke"]

Tugas Anda:
1. Untuk setiap ambang, tanyakan "mengapa angka itu dan
   bukan angka lain?" — dan tandai baris yang penelusuran
   saya tidak menjawabnya.
2. Tandai kriteria yang cara mengukurnya belum dapat diulang
   orang lain.
3. Sebutkan aspek yang biasanya dievaluasi pada artefak
   sejenis dan tidak ada dalam daftar saya — hanya namanya.

Jangan mengusulkan angka. Jangan mengisi kolom penelusuran.
```

---

## Referensi

1. Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information Systems Research. *MIS Quarterly*, 28(1), 75–105.
2. Peffers, K., et al. (2007). A Design Science Research Methodology for Information Systems Research. *Journal of Management Information Systems*, 24(3), 45–77.
3. Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A Framework for Evaluation in Design Science Research. *European Journal of Information Systems*, 25(1), 77–89.
4. Gregor, S., & Hevner, A. R. (2013). Positioning and Presenting Design Science Research for Maximum Impact. *MIS Quarterly*, 37(2), 337–355.
5. Wieringa, R. J. (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Bab buku ajar | [Bab 12](../06-buku-ajar/bab-12-design-science-dan-evaluasi-artefak.md) |
| Lokakarya | [Lokakarya 13](../04-labs/lab-13-kriteria-evaluasi-artefak.md) |
| Sumber kebutuhan | [Minggu 6 — *Stakeholder*](week-06-stakeholder-kebutuhan-dan-konteks.md) |
| Minggu sebelumnya | [Minggu 12](week-12-analisis-data-dan-penarikan-simpulan.md) |
| Minggu berikutnya | [Minggu 14](week-14-riset-berbantuan-ai-dan-reproducibility.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
