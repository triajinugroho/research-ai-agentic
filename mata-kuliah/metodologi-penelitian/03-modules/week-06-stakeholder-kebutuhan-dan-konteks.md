# Minggu 6: *Stakeholder*, Kebutuhan, dan Konteks

---

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata kuliah | Metodologi Penelitian (`IF52510021`) |
| Minggu | 6 dari 16 |
| Topik | Mengumpulkan bukti kebutuhan dan memetakan kendala |
| Sub-CPMK | `METPEN-Sub-CPMK091-1` |
| ICM | ICM-06 — Mengumpulkan bukti kebutuhan *stakeholder* dan memetakan kendalanya |
| Durasi | 2 × 50 menit |
| Metode | Kuliah + **presentasi mahasiswa (T6, 8%)** |
| Bacaan | [Bab 6](../06-buku-ajar/bab-06-stakeholder-kebutuhan-dan-konteks.md) |

---

## Tujuan Pembelajaran

1. **Mengidentifikasi** (C2) *stakeholder* dan kepentingannya.
2. **Mengumpulkan** (C3) bukti kebutuhan dari lapangan.
3. **Menganalisis** (C4) kendala yang dihadapi tiap *stakeholder*.
4. **Memetakan** (C4) kendala menjadi kriteria penelitian dan evaluasi.

---

## Materi Pembelajaran

### 6.1 Mengapa *Stakeholder* Penting dalam Penelitian

Pada penelitian yang melibatkan orang atau organisasi — yang mencakup
sebagian besar Tugas Akhir Informatika — kebutuhan *stakeholder* menentukan
tiga hal:

| Yang ditentukan | Contoh |
|-----------------|--------|
| **Apa yang layak diteliti** | Persoalan yang tidak dirasakan siapa pun sulit dijelaskan urgensinya |
| **Data apa yang dapat diperoleh** | Akses bergantung pada kesediaan pihak terkait |
| **Kriteria apa yang menentukan keberhasilan** | Artefak dinilai menurut kebutuhan penggunanya, bukan selera peneliti |

Hal ketiga adalah yang paling sering diabaikan dan yang menjadi dasar T12
pada Minggu 13.

### 6.2 Memetakan *Stakeholder*

```
              PENGARUH TINGGI
         ┌──────────────┬──────────────┐
KEPEN-   │  Libatkan    │  Kelola      │
TINGAN   │  dekat       │  erat  ◄── prioritas
TINGGI   │              │              │
         ├──────────────┼──────────────┤
KEPEN-   │  Pantau      │  Beri tahu   │
TINGAN   │              │              │
RENDAH   │              │              │
         └──────────────┴──────────────┘
           PENGARUH RENDAH
```

| Contoh pada penelitian aplikasi layanan pemda |  |
|---|---|
| Staf administrasi (pengguna harian) | Kepentingan tinggi, pengaruh rendah → **libatkan dekat** |
| Kepala dinas | Kepentingan sedang, pengaruh tinggi → kelola erat (pemberi izin akses) |
| Warga pengguna layanan | Kepentingan tinggi, pengaruh rendah → libatkan |
| Vendor pengembang | Kepentingan tinggi, pengaruh tinggi → kelola erat |

Kuadran kiri atas — kepentingan tinggi, pengaruh rendah — biasanya berisi
orang yang paling terdampak dan paling jarang ditanya. Justru merekalah
sumber bukti kebutuhan yang paling bernilai.

### 6.3 Mengumpulkan Bukti Kebutuhan

| Cara | Kekuatan | Keterbatasan |
|------|----------|--------------|
| Wawancara semi-terstruktur | Mendalam; menangkap yang tak terduga | Memakan waktu; sulit digeneralisasi |
| Pengamatan langsung | Melihat yang tidak diceritakan | Kehadiran peneliti memengaruhi |
| Analisis dokumen | Data historis; tidak mengganggu | Hanya yang tercatat |
| Kuesioner | Menjangkau banyak | Hanya menjawab yang ditanyakan |
| Analisis log sistem | Perilaku nyata | Tidak menjelaskan sebab |

Untuk T6, **wawancara dengan ≥3 narasumber nyata adalah ketentuan mutlak**.
Kebutuhan yang diasumsikan tanpa bukti lapangan tidak dinilai.

### 6.4 Bertanya tentang Peristiwa, Bukan Pendapat

| Pertanyaan lemah | Pertanyaan kuat |
|------------------|-----------------|
| "Apakah sistem ini membantu?" | "Kapan terakhir kali Anda memakainya? Untuk apa?" |
| "Fitur apa yang Anda inginkan?" | "Apa yang Anda kerjakan sebelum dan sesudah memakai sistem ini?" |
| "Apakah pelatihan cukup?" | "Ketika pertama kali memakainya, bagian mana yang membuat Anda berhenti?" |
| "Seberapa penting kecepatan?" | "Pernahkah Anda meninggalkan pekerjaan karena sistem lambat? Ceritakan." |

Prinsip ini sama dengan yang dipakai mata kuliah
[Teknopreneur](../../teknopreneur/README.md): jawaban tentang peristiwa yang
sudah terjadi tidak dapat disesuaikan dengan harapan pewawancara.

### 6.5 Dari Kendala ke Kriteria

Inilah pekerjaan yang dinilai pada indikator kedua Sub-CPMK 091-1.

| Kendala yang ditemukan | Sumber | Kriteria yang diturunkan |
|------------------------|--------|--------------------------|
| Staf hanya punya 5 menit per berkas pada jam sibuk | Wawancara N1, N3 | Waktu penyelesaian tugas ≤3 menit |
| Komputer kantor berspesifikasi lama | Pengamatan | Berjalan pada perangkat dengan RAM 4 GB |
| Jaringan sering terputus | Wawancara N2; log sistem | Berfungsi dengan koneksi terputus ≤10 menit |
| Pergantian staf tinggi | Wawancara N1 | Dapat dipakai tanpa pelatihan formal |

Kolom kanan adalah **kriteria evaluasi yang tertelusur** — setiap baris dapat
ditunjuk kembali ke bukti lapangan. Kriteria yang tidak memiliki kolom tengah
adalah kriteria yang berasal dari asumsi peneliti.

### 6.6 Etika Pengumpulan Data dari Manusia

| Ketentuan | Bentuk konkretnya |
|-----------|-------------------|
| Persetujuan | Dinyatakan lisan atau tertulis, setelah tujuan dijelaskan |
| Kejujuran | Nyatakan bahwa ini penelitian tugas akhir/mata kuliah |
| Kerahasiaan | Identitas diinisialkan; data pribadi tidak disertakan |
| Hak menarik diri | Narasumber dapat berhenti kapan pun |
| Penyimpanan | Data disimpan aman, dihapus setelah tidak diperlukan |
| Izin lembaga | Bila melibatkan organisasi, izin resmi diperlukan |

Ketentuan terakhir sering menjadi penghambat yang tidak diperkirakan.
Mengurus izin lembaga dapat memakan beberapa minggu — dan itulah sebabnya
penghubungan calon narasumber dimulai sejak Minggu 5.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (120 menit)

| # | Kegiatan |
|---|----------|
| 1 | Membaca [Bab 6](../06-buku-ajar/bab-06-stakeholder-kebutuhan-dan-konteks.md) |
| 2 | **Melakukan ≥3 wawancara** dengan narasumber nyata |
| 3 | Menyusun peta *stakeholder* dan tabel kendala→kriteria |
| 4 | Menyiapkan presentasi 10 menit |

### Di Kelas (100 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–20 | Kuliah singkat: pemetaan *stakeholder*; kendala→kriteria; etika |
| 20–50 | **Presentasi T6** — gelombang 1 |
| 50–60 | **Rehat** |
| 60–90 | **Presentasi T6** — gelombang 2 |
| 90–100 | Rangkuman: pola kendala yang muncul di seluruh kelas |

> Kegiatan 90–100 sering menghasilkan pengamatan yang berguna. Kendala
> tertentu — jaringan tidak stabil, perangkat lama, pergantian staf — muncul
> pada hampir semua penelitian berkonteks Indonesia, dan menyadarinya
> membantu setiap mahasiswa memperbaiki kriterianya.

### Setelah Kelas

| # | Kegiatan |
|---|----------|
| 1 | Memperbaiki dokumen T6 berdasarkan umpan balik |
| 2 | Membaca [Bab 7](../06-buku-ajar/bab-07-kerangka-konseptual.md) |
| 3 | Menyiapkan diri untuk UTS Minggu 8 |

---

## Penugasan

### T6 — Presentasi Analisis *Stakeholder* (8%, Unjuk Kerja) ★

| Aspek | Ketentuan |
|-------|-----------|
| Keluaran | Presentasi 10 menit + dokumen pendukung |
| Isi | Peta *stakeholder* · **bukti dari ≥3 narasumber nyata** · kendala per pihak · pemetaan kendala→kriteria |
| Ketentuan mutlak | Narasumber nyata dan terdokumentasi |
| Tenggat | Presentasi di kelas Minggu 6 |

---

## AI Corner — Minggu 6

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI memeriksa apakah panduan wawancara memimpin jawaban | **Mengarang kutipan atau data narasumber** |
| Meminta AI merapikan transkrip yang Anda rekam sendiri | Meminta AI menyimpulkan wawancara yang tidak dilakukan |
| Meminta AI menyebutkan *stakeholder* yang mungkin terlewat | Meminta AI mengisi peta *stakeholder* |
| Meminta AI memeriksa apakah kriteria Anda terukur | Meminta AI menurunkan kriteria dari kendala |

Mengarang data narasumber adalah **pemalsuan data penelitian** dan
diperlakukan demikian: nilai keluaran nol, dan perkara diproses sesuai
ketentuan fakultas.

### Pemakaian yang Dianjurkan

```
Berikut panduan wawancara saya untuk staf administrasi
tentang pemakaian sistem pencatatan:
[tempelkan panduan]

Tugas Anda:
1. Tandai pertanyaan yang memimpin jawaban.
2. Tandai pertanyaan yang menanyakan pendapat, dan usulkan
   bentuk yang menanyakan peristiwa yang sudah terjadi.
3. Sebutkan aspek konteks kerja yang mungkin belum saya tanyakan.

Jangan menulis panduan baru.
```

---

## Referensi

1. Freeman, R. E. (2010). *Strategic Management: A Stakeholder Approach*. Cambridge University Press.
2. Sharp, H., Finkelstein, A., & Galal, G. (1999). Stakeholder Identification in the Requirements Engineering Process. *Proceedings of DEXA '99*.
3. Runeson, P., & Höst, M. (2009). Guidelines for Conducting and Reporting Case Study Research in Software Engineering. *Empirical Software Engineering*, 14(2), 131–164.
4. Fitzpatrick, R. (2013). *The Mom Test*. Founder Centric.
5. Republik Indonesia. (2022). *Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi*.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Bab buku ajar | [Bab 6](../06-buku-ajar/bab-06-stakeholder-kebutuhan-dan-konteks.md) |
| Lokakarya | [Lokakarya 6](../04-labs/lab-06-analisis-stakeholder-dan-kebutuhan.md) |
| Lanjutan | [Minggu 13 — Kriteria Evaluasi Artefak](week-13-design-science-dan-evaluasi-artefak.md) |
| Minggu sebelumnya | [Minggu 5](week-05-pertanyaan-tujuan-ruang-lingkup-kontribusi.md) |
| Minggu berikutnya | [Minggu 7](week-07-kerangka-konseptual.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
