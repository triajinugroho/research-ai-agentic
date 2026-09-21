# Minggu 15: Presentasi Proyek

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 15 dari 16 |
| Topik | Penyajian dan pertanggungjawaban hasil proyek |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` dan `DAIML-Sub-CPMK102-1` · ICM-14 |
| Bloom | C5 (Mengevaluasi) — C6 (Mencipta) |
| Durasi | 150 menit |
| Metode | Presentasi kelompok dan tanya jawab |
| Penilaian | **Unjuk Kerja — presentasi (P-04), 10%** |

---

## Tujuan Pertemuan

1. Menyajikan hasil proyek secara runtut kepada audiens yang tidak mengikuti prosesnya.
2. **Mempertanggungjawabkan setiap keputusan teknis** yang diambil sepanjang proyek.
3. Menilai pekerjaan kelompok lain secara kritis dan membangun.

---

## Format Pelaksanaan

### Susunan Waktu per Kelompok (28 menit)

| Bagian | Durasi | Isi |
|--------|--------|-----|
| 1. Masalah dan formulasi | 3' | Mengapa penting; bagaimana dirumuskan menjadi *task* ML; metrik dan alasannya |
| 2. Data dan prapemrosesan | 4' | Sumber, kualitas, keputusan pembersihan, pencegahan kebocoran |
| 3. Metode dan protokol | 4' | Model yang dibandingkan; bagaimana perbandingan dijaga adil |
| 4. Hasil dan analisis kesalahan | 6' | *Baseline*, metrik, kasus yang salah dan polanya |
| 5. Keterbatasan dan dampak | 3' | Apa yang tidak dapat dilakukan model; siapa yang berisiko dirugikan |
| **6. Tanya jawab** | **8'** | Pertanyaan dapat diarahkan kepada anggota mana pun |

### Ketentuan

| Aspek | Ketentuan |
|-------|-----------|
| Slide | Maksimal 15 halaman |
| Pembicara | **Setiap anggota wajib berbicara** |
| Penguasaan | Seluruh anggota wajib menguasai keseluruhan isi |
| Demonstrasi langsung | Tidak diwajibkan; bila dilakukan, sudah diuji sebelumnya |
| Bahasa | Indonesia baku; istilah teknis boleh bilingual |

---

## Isi yang Wajib Ada pada Slide

| # | Unsur | Mengapa dinilai |
|---|-------|-----------------|
| 1 | Formulasi *task* yang lengkap | Inti `Sub-CPMK082-1` |
| 2 | **Skor *baseline*** | Tanpa ini, angka kinerja tidak bermakna |
| 3 | Pernyataan pencegahan kebocoran beserta buktinya | Kriteria kurikulum `Sub-CPMK102-1` |
| 4 | Tabel perbandingan model dengan **simpangan antarlipatan** | Perbandingan yang jujur |
| 5 | Metrik yang sesuai masalah, beserta alasan pemilihannya | Inti `Sub-CPMK102-1` |
| 6 | **Analisis kesalahan** — pola pada kasus yang salah | Kedalaman pemahaman |
| 7 | Audit *fairness* antarkelompok | Materi Minggu 14 |
| 8 | Keterbatasan yang dinyatakan jujur | Kriteria kurikulum |

> Kelompok yang menampilkan akurasi tanpa *baseline*, atau melaporkan model terbaik tanpa menyebut simpangan antarlipatan, kehilangan nilai pada aspek yang bersangkutan — sekalipun proyeknya secara teknis baik.

---

## Pertanyaan yang Akan Diajukan

Setiap kelompok harus menyiapkan jawaban atas pertanyaan berikut. Pertanyaan diarahkan kepada **anggota mana pun**, bukan hanya yang menyampaikan bagian itu.

### Tentang Formulasi

1. Mengapa masalah ini dirumuskan sebagai klasifikasi (atau regresi), bukan yang lain?
2. Apa yang akan dilakukan pengguna dengan keluaran model ini?
3. Metrik apa yang dipilih, dan mengapa bukan metrik yang lain?
4. Berapa ambang keberhasilan yang ditetapkan sejak awal? Tercapai atau tidak?

### Tentang Data

5. Berapa baris dibuang, dan atas dasar apa?
6. Bagaimana nilai hilang ditangani? Apa pola kehilangannya?
7. Adakah fitur yang **tidak** dipakai meski tersedia? Mengapa?
8. **Bagaimana Anda memastikan tidak ada kebocoran?** Tunjukkan buktinya.

### Tentang Metode

9. Mengapa model ini yang dipilih untuk diterapkan?
10. Apakah seluruh model memperoleh anggaran penyetelan yang sebanding?
11. Berapa simpangan antarlipatan? Apakah selisih antarmodel lebih besar daripada simpangan itu?
12. Apakah data uji pernah dipakai lebih dari sekali?

### Tentang Hasil

13. Berapa skor *baseline*, dan seberapa jauh model mengunggulinya?
14. Kasus seperti apa yang paling sering salah diprediksi?
15. Adakah kelompok yang kinerjanya lebih buruk? Berapa selisihnya?
16. Bila model ini dipakai besok, kesalahan apa yang paling merugikan?

### Tentang Tanggung Jawab

17. Siapa yang dapat dirugikan bila model ini salah?
18. Apakah model ini layak dipakai tanpa pengawasan manusia? Mengapa?
19. Bagian mana yang dibantu AI? **Jelaskan salah satu baris kodenya.**

> Pertanyaan 19 bukan jebakan. Kelompok yang memakai AI sesuai kebijakan [RPS §K.1](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md) akan menjawabnya dengan mudah.

---

## Rubrik Penilaian Presentasi (10%)

Menelusur ke `DAIML-Sub-CPMK082-1`. Kriteria kurikulum: *ketepatan problem-model; correctness training; reproduksibilitas eksperimen.*

| Aspek | Bobot | 4 (Sangat Baik) | 3 (Baik) | 2 (Cukup) | 1 (Kurang) |
|-------|-------|-----------------|----------|-----------|------------|
| **Ketepatan formulasi** | 2,5% | *Task*, metrik, dan ambang keberhasilan dirumuskan tepat dan beralasan | Tepat, alasan kurang tajam | Dapat diterima tetapi bukan yang optimal | Formulasi tidak sesuai masalah |
| **Kebenaran metode** | 2,5% | Protokol adil; tanpa kebocoran; *baseline* ada; simpangan dilaporkan | Benar dengan kekurangan kecil | Ada kekeliruan yang memengaruhi kesimpulan | Kebocoran atau protokol tidak sah |
| **Kedalaman analisis** | 2,0% | Analisis kesalahan tajam; audit *fairness* dilakukan; keterbatasan jujur | Analisis memadai | Dangkal | Tidak ada analisis kesalahan |
| **Kualitas penyajian** | 1,5% | Runtut; slide jelas; waktu terkelola; seluruh anggota berbicara | Jelas dengan sedikit lompatan | Sulit diikuti sebagian | Tidak terstruktur |
| **Penguasaan saat tanya jawab** | 1,5% | **Seluruh anggota** menjawab tepat dan berbasis data | Sebagian besar menguasai | Hanya satu-dua yang menguasai | Tidak dapat menjawab pertanyaan dasar |

### Konversi Skor

$$\text{Nilai aspek} = \frac{\text{skor } (1\text{–}4)}{4} \times \text{bobot aspek}$$

---

## Penilaian Sejawat

Setiap mahasiswa menilai dua kelompok lain. Penilaian ini **tidak masuk nilai akhir**, tetapi wajib dikumpulkan dan menjadi bahan umpan balik.

| Aspek | Pertanyaan |
|-------|------------|
| Kejelasan | Apakah Anda memahami masalah yang mereka selesaikan? |
| Kebenaran | Adakah keputusan metodologis yang Anda ragukan? Sebutkan. |
| Kejujuran | Apakah keterbatasan dinyatakan atau disembunyikan? |
| Pertanyaan | Satu pertanyaan yang ingin Anda ajukan tetapi belum sempat |

---

## Catatan Penting tentang Hasil

> **Kelompok yang modelnya tidak mengungguli *baseline* TIDAK dirugikan.**
>
> Yang dinilai adalah ketepatan formulasi, kebenaran prosedur, kesesuaian metrik, dan kejujuran analisis. Melaporkan *"model kami hanya sedikit mengungguli baseline; berikut analisis mengapa, dan berikut yang akan kami lakukan dengan waktu lebih"* dengan prosedur yang benar bernilai **lebih tinggi** daripada melaporkan akurasi 0,99 yang ternyata mengandung kebocoran.
>
> Ini bukan kelonggaran. Ini adalah inti dari apa yang hendak diajarkan mata kuliah ini: seorang insinyur yang jujur tentang batas karyanya jauh lebih berharga daripada yang selalu melaporkan hasil mengesankan.

---

## Susunan Acara

| Waktu | Kegiatan |
|-------|----------|
| 0–10' | Pengantar; penjelasan tata cara; pembagian lembar penilaian sejawat |
| 10–150' | Presentasi kelompok, masing-masing 28 menit (5 kelompok per sesi) |
| Penutup | Umpan balik menyeluruh; pengumuman persiapan UAS |

> Bila jumlah kelompok melebihi kapasitas satu pertemuan, presentasi dibagi ke dalam sesi tambahan yang dijadwalkan terpisah.

---

## Setelah Presentasi

- Mengumpulkan [Lab 14](../04-labs/lab-14-audit-bias-dan-model-card.md) — jatuh tempo hari ini.
- Mempersiapkan UAS dengan [kisi-kisi UAS](../05-assessments/kisi-kisi-uas.md).
- Menyimpan repositori proyek sebagai portofolio — ini adalah karya yang dapat ditunjukkan kepada calon pemberi kerja.

---

## Rangkuman

1. Presentasi menguji **pertanggungjawaban atas keputusan**, bukan kemampuan berbicara.
2. Delapan unsur wajib pada slide, dengan ***baseline*** dan **simpangan** sebagai yang paling sering terlewat.
3. **Setiap anggota wajib berbicara dan menguasai keseluruhan isi.**
4. Sembilan belas pertanyaan pada modul ini adalah daftar persiapan yang sesungguhnya.
5. **Hasil yang tidak mengungguli *baseline* tidak merugikan** bila prosedurnya benar dan analisisnya jujur.
6. Kebocoran yang ditemukan saat tanya jawab jauh lebih merugikan daripada kinerja yang sederhana.

---

## Referensi

1. [Panduan Proyek](../05-assessments/project-guidelines.md).
2. [Rencana Tugas Mahasiswa §E](../02-rtm/rtm-dasar-kecerdasan-artifisial-pembelajaran-mesin.md).
3. Mitchell, M., et al. (2019). Model Cards for Model Reporting. *FAT* '19*.
4. Kapoor, S., & Narayanan, A. (2023). Leakage and the Reproducibility Crisis in ML-based Science. *Patterns*, 4(9).
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
