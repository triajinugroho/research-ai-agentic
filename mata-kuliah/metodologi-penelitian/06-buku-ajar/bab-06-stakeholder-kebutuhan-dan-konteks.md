# BAB 6: *STAKEHOLDER*, KEBUTUHAN, DAN KONTEKS

**Bahan rujukan penyelarasan kurikulum** — disusun Tri Aji Nugroho, S.T., M.T.
Pengampu mata kuliah menurut registri: **Andi Arniaty Arsyad, Ph.D.** (`AAA`).

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `METPEN-Sub-CPMK091-1` | Mengidentifikasi (C2) dan menganalisis (C4) kebutuhan, karakteristik, konteks, serta kendala *stakeholder* sebagai dasar kriteria penelitian dan evaluasi | C2–C4 |

Setelah membaca bab ini, pembaca diharapkan mampu:

1. **Mengidentifikasi** (C2) *stakeholder* dan kepentingannya.
2. **Mengumpulkan** (C3) bukti kebutuhan dari lapangan.
3. **Menganalisis** (C4) kendala yang dihadapi tiap pihak.
4. **Memetakan** (C4) kendala menjadi kriteria penelitian dan evaluasi.

---

## 6.1 Mengapa *Stakeholder* Penting dalam Penelitian

### 6.1.1 Tiga Hal yang Ditentukannya

| Yang ditentukan | Penjelasan |
|-----------------|------------|
| **Apa yang layak diteliti** | Persoalan yang tidak dirasakan siapa pun sulit dijelaskan urgensinya |
| **Data apa yang dapat diperoleh** | Akses bergantung pada kesediaan pihak terkait |
| **Kriteria apa yang menentukan keberhasilan** | Artefak dinilai menurut kebutuhan penggunanya, bukan selera peneliti |

Hal ketiga adalah yang paling sering diabaikan dan menjadi dasar seluruh
Bab 12. Sebuah artefak yang memenuhi seluruh kriteria yang ditetapkan
penelitinya sendiri belum menunjukkan apa pun; yang dituntut adalah kriteria
yang berasal dari kebutuhan nyata.

### 6.1.2 Bukan Hanya untuk Penelitian Perancangan

Analisis *stakeholder* sering dianggap hanya relevan bagi penelitian yang
membangun artefak. Ia relevan lebih luas:

| Jenis penelitian | Peran analisis *stakeholder* |
|------------------|------------------------------|
| Eksploratif | Menentukan siapa yang diwawancarai dan mengapa |
| Deskriptif | Menentukan populasi dan kerangka sampelnya |
| Eksplanatif | Menentukan variabel kendali yang relevan pada konteks itu |
| Perancangan | Menentukan kriteria evaluasi |

---

## 6.2 Memetakan *Stakeholder*

### 6.2.1 Kuadran Kepentingan–Pengaruh

```
              PENGARUH TINGGI
         ┌──────────────┬──────────────┐
KEPEN-   │  Libatkan    │  Kelola      │
TINGAN   │  dekat       │  erat        │
TINGGI   │              │              │
         ├──────────────┼──────────────┤
KEPEN-   │  Pantau      │  Beri tahu   │
TINGAN   │              │              │
RENDAH   │              │              │
         └──────────────┴──────────────┘
           PENGARUH RENDAH
```

| Contoh pada penelitian aplikasi layanan pemda | Kuadran |
|---|---|
| Staf administrasi (pengguna harian) | Kepentingan tinggi, pengaruh rendah → **libatkan dekat** |
| Kepala dinas | Kepentingan sedang, pengaruh tinggi → kelola erat (pemberi izin) |
| Warga pengguna layanan | Kepentingan tinggi, pengaruh rendah → libatkan |
| Vendor pengembang | Kepentingan tinggi, pengaruh tinggi → kelola erat |
| Bagian TI kabupaten | Kepentingan sedang, pengaruh sedang → pantau |

### 6.2.2 Kuadran yang Paling Sering Terlewat

Kuadran **kepentingan tinggi, pengaruh rendah** berisi orang yang paling
terdampak dan paling jarang ditanya. Mereka tidak memutuskan pengadaan
sistem, tidak menandatangani izin, dan tidak diundang ke rapat evaluasi —
tetapi merekalah yang memakainya setiap hari.

| Akibat mengabaikan kuadran ini | Contoh |
|-------------------------------|--------|
| Kriteria berasal dari pengambil keputusan | "Sistem harus terintegrasi dengan sistem pusat" |
| Kebutuhan harian tidak terwakili | "Sistem harus dapat dipakai saat jaringan putus" |
| Sebab kegagalan tidak terlihat | Sistem yang memenuhi seluruh kriteria pengadaan dan tetap ditinggalkan |

> Ketentuan mata kuliah ini: **minimal satu narasumber berasal dari kuadran
> kepentingan tinggi–pengaruh rendah**. Tanpa itu, analisis kebutuhan
> menggambarkan apa yang diinginkan pihak yang memutuskan, bukan apa yang
> dibutuhkan pihak yang memakai.

### 6.2.3 Kepentingan yang Bertentangan

| Pihak | Yang diinginkan | Bertentangan dengan |
|-------|-----------------|---------------------|
| Kepala dinas | Laporan yang lengkap dan terperinci | Staf: input yang sesedikit mungkin |
| Bagian TI | Standardisasi lintas dinas | Staf: penyesuaian dengan alur kerja masing-masing |
| Vendor | Cakupan fitur yang luas | Staf: kesederhanaan |
| Warga | Proses yang cepat | Dinas: verifikasi yang teliti |

Pertentangan kepentingan bukan kekacauan yang harus diselesaikan peneliti.
Ia adalah **temuan** — dan sering menjelaskan mengapa sebuah sistem yang
dirancang dengan baik tetap tidak dipakai.

Penelitian yang melaporkan pertentangan ini, beserta bagaimana ia
terselesaikan atau tidak dalam praktik, memberi kontribusi yang jelas.

---

## 6.3 Mengumpulkan Bukti Kebutuhan

### 6.3.1 Lima Cara

| Cara | Kekuatan | Keterbatasan |
|------|----------|--------------|
| Wawancara semi-terstruktur | Mendalam; menangkap yang tak terduga | Memakan waktu; sulit digeneralisasi |
| Pengamatan langsung | Melihat yang tidak diceritakan | Kehadiran peneliti memengaruhi |
| Analisis dokumen | Data historis; tidak mengganggu | Hanya yang tercatat |
| Kuesioner | Menjangkau banyak | Hanya menjawab yang ditanyakan |
| Analisis log sistem | Perilaku nyata, bukan yang dilaporkan | Tidak menjelaskan sebab |

### 6.3.2 Triangulasi

Cara yang berbeda sering menghasilkan gambaran yang berbeda — dan
perbedaannya adalah temuan.

| Sumber | Yang ditemukan |
|--------|----------------|
| Wawancara | "Kami selalu mencatat setiap transaksi" |
| Log sistem | Pencatatan berhenti setiap hari setelah pukul 11.00 |
| Pengamatan | Antrean panjang dari pukul 10.30; tidak ada waktu mencatat |

Ketiganya tidak bertentangan; ketiganya menggambarkan bagian yang berbeda.
Narasumber tidak berbohong — ia menggambarkan niatnya dan hari-hari yang
normal. Log menggambarkan apa yang sebenarnya terjadi. Pengamatan
menjelaskan sebabnya.

> Studi kasus yang hanya memakai wawancara kehilangan kekuatan utamanya.
> Ketentuan minimal untuk studi kasus: **dua sumber bukti yang berbeda**.

### 6.3.3 Bertanya tentang Peristiwa

| Pertanyaan lemah | Pertanyaan kuat |
|------------------|-----------------|
| "Apakah sistem ini membantu?" | "Kapan terakhir kali Anda memakainya? Untuk apa?" |
| "Fitur apa yang Anda inginkan?" | "Apa yang Anda kerjakan sebelum dan sesudah memakai sistem ini?" |
| "Apakah pelatihan cukup?" | "Ketika pertama kali memakainya, bagian mana yang membuat Anda berhenti?" |
| "Seberapa penting kecepatan?" | "Pernahkah Anda meninggalkan pekerjaan karena sistem lambat? Ceritakan." |

Prinsipnya sama dengan yang dipakai mata kuliah
[Teknopreneur](../../teknopreneur/README.md): jawaban tentang peristiwa yang
sudah terjadi tidak dapat disesuaikan dengan harapan pewawancara.

| Sebab jawaban tentang pendapat lemah | Penjelasan |
|--------------------------------------|------------|
| Kesopanan | Menolak gagasan orang yang bertamu terasa tidak enak |
| Ketidakmampuan meramal diri sendiri | Manusia buruk memperkirakan perilakunya sendiri |
| Pertanyaan yang memimpin | Bentuknya sudah mengandung jawaban yang diharapkan |

### 6.3.4 Kata "Biasanya"

Ketika narasumber menjawab *"Biasanya sih kami catat dulu"*, yang diterima
adalah **ringkasan** — yang sudah melewati penyaringan ingatan dan citra
diri.

Tindak lanjut yang tepat selalu sama: **"Kemarin bagaimana?"**

Jawaban atas pertanyaan lanjutan itu sering berbeda dari ringkasannya, dan
perbedaan itulah temuannya.

---

## 6.4 Dari Kendala ke Kriteria

### 6.4.1 Pekerjaan yang Dinilai

Ini adalah indikator kedua Sub-CPMK 091-1: *memetakan constraint ke kriteria
kebutuhan/penilaian artefak*.

| Kode | Kendala yang ditemukan | Sumber | Kriteria yang diturunkan |
|------|------------------------|--------|--------------------------|
| K-01 | Staf hanya punya 5 menit per berkas pada jam sibuk | Wawancara N1, N3 | Waktu penyelesaian tugas ≤3 menit |
| K-02 | Komputer kantor berspesifikasi lama (RAM 4 GB) | Pengamatan | Berjalan pada perangkat dengan RAM 4 GB |
| K-03 | Jaringan sering terputus | Wawancara N2; log sistem | Berfungsi dengan koneksi terputus ≤10 menit |
| K-04 | Pergantian staf tinggi | Wawancara N1 | Dapat dipakai tanpa pelatihan formal |
| KB-01 | Kesalahan data menyebabkan kerja ulang | N1, N2, N3 | Ketelitian ekstraksi ≥95% |

### 6.4.2 Kolom Sumber

Kolom ketiga adalah yang membedakan kriteria penelitian dari daftar keinginan
pengembang.

| Kriteria dengan kolom sumber | Kriteria tanpa kolom sumber |
|------------------------------|-----------------------------|
| Dapat dipertahankan ketika ditanya "mengapa 3 menit?" | Hanya dapat dijawab "menurut kami cukup" |
| Menunjukkan kebutuhan yang nyata | Menunjukkan asumsi peneliti |
| Dapat diperiksa penguji | Tidak dapat diperiksa |
| Menjadi dasar ambang evaluasi (Bab 12) | Ambang menjadi angka bulat tanpa dasar |

### 6.4.3 Penomoran Kendala

Kendala diberi kode (K-01, K-02, …) sejak awal karena akan dirujuk kembali
pada Bab 12, ketika kriteria evaluasi ditetapkan.

```
Kutipan narasumber
      ↓
Kendala K-01
      ↓
Kriteria kebutuhan
      ↓
Kriteria evaluasi + ambang (Bab 12)
      ↓
Cara mengukur
```

Rantai inilah yang diperiksa pada penilaian proposal, dengan bobot **30%**
dari komponen T14.

---

## 6.5 Etika Pengumpulan Data dari Manusia

### 6.5.1 Ketentuan

| Ketentuan | Bentuk konkretnya |
|-----------|-------------------|
| Persetujuan | Dinyatakan lisan atau tertulis, setelah tujuan dijelaskan |
| Kejujuran | Nyatakan bahwa ini penelitian tugas akhir atau mata kuliah |
| Kerahasiaan | Identitas diinisialkan; jabatan digeneralisasi bila perlu |
| Hak menarik diri | Narasumber dapat berhenti kapan pun, tanpa alasan |
| Penyimpanan | Data disimpan terbatas, dihapus setelah tidak diperlukan |
| Izin lembaga | Bila melibatkan organisasi, izin resmi diurus lebih dahulu |

### 6.5.2 Izin Lembaga

Ketentuan terakhir sering menjadi penghambat yang tidak diperkirakan.

| Keadaan | Waktu yang diperlukan |
|---------|----------------------|
| Wawancara pribadi tanpa nama lembaga | Biasanya tidak perlu izin resmi |
| Wawancara staf dalam kapasitas jabatannya | Sering perlu izin |
| Akses ke data atau sistem lembaga | Hampir selalu perlu izin resmi |
| Penelitian yang menyebut nama lembaga | Perlu izin publikasi |

Mengurus izin lembaga dapat memakan beberapa minggu — dan itulah sebabnya
penghubungan calon narasumber dimulai sejak Minggu 5, bukan Minggu 6.

### 6.5.3 Amanah atas Keterangan Orang Lain

Narasumber memberikan keterangan tentang pekerjaannya, kesulitannya, dan
kadang kegagalannya, berdasarkan penjelasan yang peneliti sampaikan di awal.

| Pelanggaran yang halus | Bentuknya |
|------------------------|-----------|
| Memakai keterangan untuk hal lain | Dinyatakan untuk tugas kuliah, dipakai untuk proposal proyek |
| Menyertakan detail yang mengidentifikasi | "Kepala seksi di dinas X" pada organisasi kecil |
| Mengutip keluhan tentang atasan | Meskipun diinisialkan, konteksnya dapat mengungkap |
| Menyimpan rekaman setelah selesai | Tanpa keperluan dan tanpa pemberitahuan |

Baris kedua dan ketiga menuntut pertimbangan. Inisialisasi tidak menjamin
kerahasiaan bila detail lain cukup untuk mengenali orangnya — dan akibat
kekeliruan ini ditanggung narasumber, bukan peneliti.

---

## AI Corner — Bab 6

### Batas Pemakaian

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI memeriksa apakah panduan wawancara memimpin jawaban | **Mengarang kutipan atau data narasumber** |
| Meminta AI merapikan transkrip yang Anda rekam sendiri | Menyimpulkan wawancara yang tidak dilakukan |
| Meminta AI menyebutkan *stakeholder* yang mungkin terlewat | Mengisi peta *stakeholder* |
| Meminta AI memeriksa apakah kriteria Anda terukur | Menurunkan kriteria dari kendala |

### Data Lapangan Tidak Dapat Digantikan

Mengarang data narasumber adalah **pemalsuan data penelitian**: nilai
keluaran nol, dan perkara diproses sesuai ketentuan fakultas.

Perlakuan ini setara dengan pemalsuan data eksperimen karena akibatnya sama.
Peneliti berikutnya yang membangun di atas temuan itu membangun di atas
sesuatu yang tidak ada.

### Mengapa Transkrip Tidak Boleh Langsung Diringkas

| Yang hilang dalam ringkasan | Mengapa penting |
|-----------------------------|-----------------|
| Jeda dan keraguan | Menandai bagian yang sulit diceritakan |
| Pengulangan | Hal yang diulang tiga kali biasanya yang paling mengganggu |
| Kalimat yang terpotong | Sering menandai hal yang tidak ingin dikatakan langsung |
| Istilah lokal narasumber | Menunjukkan cara mereka memahami persoalannya |

Ketentuan mata kuliah ini: **yang mewawancarai adalah yang menulis
catatannya**. AI boleh merapikan ejaan dan tata kalimat setelahnya, dengan
pemakaian dicatat dalam Deklarasi AI.

### Pemakaian yang Dianjurkan

```
Berikut panduan wawancara saya untuk staf administrasi
tentang pemakaian sistem pencatatan:
[tempelkan panduan]

Tugas Anda:
1. Tandai pertanyaan yang memimpin jawaban.
2. Tandai pertanyaan yang menanyakan pendapat, dan usulkan
   bentuk yang menanyakan peristiwa yang sudah terjadi.
3. Sebutkan aspek konteks kerja yang mungkin belum saya
   tanyakan — hanya aspeknya, bukan pertanyaannya.
4. Tandai istilah teknis yang mungkin tidak dipahami
   responden yang bukan pengguna teknologi sehari-hari.

Jangan menulis panduan baru.
```

Butir 4 sering paling berguna pada konteks Indonesia, di mana istilah yang
terasa biasa bagi mahasiswa Informatika asing bagi respondennya.

---

## Latihan Soal

### Tingkat Dasar

1. Sebutkan tiga hal yang ditentukan analisis *stakeholder* dalam penelitian.
2. Jelaskan kuadran kepentingan–pengaruh dan sebutkan kuadran mana yang paling sering terlewat.
3. Sebutkan lima cara mengumpulkan bukti kebutuhan beserta keterbatasannya.
4. Apa yang dimaksud triangulasi, dan mengapa perbedaan antarsumber merupakan temuan?
5. Apa tindak lanjut yang tepat ketika narasumber menjawab dengan kata "biasanya"?

### Tingkat Menengah

6. Ubah lima pertanyaan berikut menjadi pertanyaan tentang peristiwa yang sudah terjadi:
   - "Apakah sistem ini mudah dipakai?"
   - "Fitur apa yang paling Anda butuhkan?"
   - "Seberapa sering Anda mengalami gangguan?"
   - "Apakah pelatihan yang diberikan memadai?"
   - "Apakah Anda akan merekomendasikan sistem ini?"

7. Susun peta *stakeholder* untuk penelitian Anda dengan minimal 5 pihak, lengkap dengan kuadran dan apa yang mereka inginkan. Tandai pihak yang kepentingannya bertentangan dan jelaskan pertentangannya.

8. Susun tabel kendala → kriteria dengan minimal 5 baris, setiap baris berkode dan bersumber. Tandai baris yang sumbernya masih berupa asumsi Anda.

9. Untuk penelitian Anda, tentukan: izin lembaga apa yang diperlukan, kepada siapa diajukan, dan berapa lama perkiraan waktunya. Susun rencana bila izin tidak diberikan.

### Tingkat Mahir

10. **Latihan triangulasi.** Untuk satu kendala yang Anda temukan dari wawancara, cari data pendukung dari sumber lain (log, dokumen, pengamatan). Laporkan: apakah gambarannya sama, dan bila berbeda, apa yang dijelaskan oleh perbedaan itu.

11. Tunjukkan tabel kendala → kriteria Anda kepada salah satu narasumber. Minta ia mengoreksinya. Catat setiap koreksi verbatim. Analisis: koreksi mana yang tidak dapat Anda perkirakan dari meja, dan mengapa.

12. Wawancarai dua *stakeholder* dari kuadran yang berbeda — satu pengguna harian, satu pengambil keputusan. Bandingkan kendala yang mereka sebut. Susun analisis: di mana keduanya sepakat, di mana bertentangan, dan **kriteria mana yang akan berbeda** bila hanya satu di antaranya yang diwawancarai.

---

## Rangkuman

| Gagasan pokok | Rumusan singkat |
|---------------|-----------------|
| Tiga hal yang ditentukan | Apa yang layak diteliti, data yang dapat diperoleh, kriteria keberhasilan |
| Kuadran yang terlewat | Kepentingan tinggi–pengaruh rendah: paling terdampak, paling jarang ditanya |
| Pertentangan kepentingan | Temuan, bukan kekacauan |
| Triangulasi | Perbedaan antarsumber menjelaskan, bukan membingungkan |
| Pertanyaan yang kuat | Tentang peristiwa yang sudah terjadi |
| Kata "biasanya" | Lanjutkan dengan "kemarin bagaimana?" |
| Kolom sumber | Membedakan kriteria penelitian dari daftar keinginan |
| Penomoran kendala | Dirujuk kembali pada Bab 12 sebagai rantai ketertelusuran |
| Izin lembaga | Memakan minggu; diurus sejak jauh hari |
| Batas AI | Data lapangan tidak dapat digantikan; mengarangnya adalah pemalsuan data |

---

## Referensi

1. Freeman, R. E. (2010). *Strategic Management: A Stakeholder Approach*. Cambridge University Press.
2. Sharp, H., Finkelstein, A., & Galal, G. (1999). Stakeholder Identification in the Requirements Engineering Process. *Proceedings of DEXA '99*.
3. Runeson, P., & Höst, M. (2009). Guidelines for Conducting and Reporting Case Study Research in Software Engineering. *Empirical Software Engineering*, 14(2), 131–164.
4. Fitzpatrick, R. (2013). *The Mom Test*. Founder Centric.
5. Portigal, S. (2013). *Interviewing Users: How to Uncover Compelling Insights*. Rosenfeld Media.
6. Republik Indonesia. (2022). *Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi*.
7. Yin, R. K. (2018). *Case Study Research and Applications* (6th ed.). SAGE Publications.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul mingguan | [Minggu 6](../03-modules/week-06-stakeholder-kebutuhan-dan-konteks.md) |
| Lokakarya | [Lokakarya 6](../04-labs/lab-06-analisis-stakeholder-dan-kebutuhan.md) |
| Dipakai lagi pada | [Bab 12 — Evaluasi Artefak](bab-12-design-science-dan-evaluasi-artefak.md) |
| Bab sebelumnya | [Bab 5](bab-05-pertanyaan-tujuan-ruang-lingkup-kontribusi.md) |
| Bab berikutnya | [Bab 7 — Kerangka Konseptual](bab-07-kerangka-konseptual.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
