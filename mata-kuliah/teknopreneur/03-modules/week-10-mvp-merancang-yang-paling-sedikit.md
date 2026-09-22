# Minggu 10: MVP — Merancang yang Paling Sedikit

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Teknopreneur (`ST52510002`) |
| Minggu | 10 dari 16 |
| Topik | Definisi MVP yang benar; jenis MVP; merancang eksperimen |
| Sub-CPMK | `TEKNO-Sub-CPMKUAI22-1` |
| Bloom | C6 (Merancang) · P4 |
| Durasi | 150 menit |
| Metode | Kuliah · Studio pembangunan |
| Penilaian | Observasi (Studio 10) — bagian dari P-03 |

---

## Tujuan Pembelajaran

1. **Menjelaskan** (C2) apa yang dimaksud MVP dan apa yang bukan.
2. **Memilih** (C5) jenis MVP yang sesuai untuk asumsi yang hendak diuji.
3. **Merancang** (C6) eksperimen dengan hipotesis dan ukuran keberhasilan.
4. **Menguji** (P4) MVP kepada orang di luar tim dan mendokumentasikan pembelajarannya.

---

## Materi Pembelajaran

### 10.1 Apa yang Dimaksud MVP

#### 10.1.1 Definisi yang Benar

> **MVP adalah versi produk yang memungkinkan tim mengumpulkan jumlah pembelajaran tervalidasi terbesar tentang pelanggan dengan usaha sekecil mungkin.**

Tiga kata kunci:

| Kata | Maknanya |
|------|----------|
| **Pembelajaran** | Tujuannya belajar, bukan meluncurkan |
| **Tervalidasi** | Dari perilaku nyata, bukan pendapat |
| **Usaha sekecil mungkin** | Sesedikit mungkin yang dibangun |

#### 10.1.2 Yang Sering Disalahpahami

| MVP **bukan** | Penjelasan |
|---------------|------------|
| Versi murah dari produk penuh | MVP diukur dari pembelajaran, bukan dari kelengkapan |
| Produk dengan sedikit fitur | Bisa jadi tanpa produk sama sekali |
| Purwarupa yang tidak berfungsi | Harus menghasilkan perilaku nyata untuk diamati |
| Tahap sebelum "produk sebenarnya" | MVP adalah alat uji, bukan tahap |

> **Pertanyaan yang menentukan:** *"Asumsi apa yang paling berisiko, dan apa cara termurah mengujinya?"*
>
> Bila asumsi paling berisiko adalah "orang bersedia membayar", MVP termurahnya mungkin **halaman pendaftaran dengan tombol bayar** — bukan aplikasi.

---

### 10.2 Jenis MVP

| Jenis | Cara | Menguji apa | Usaha |
|-------|------|-------------|-------|
| ***Landing page*** | Halaman yang menjelaskan tawaran + tombol | Apakah ada yang tertarik | Sangat kecil |
| ***Concierge*** | Layanan dikerjakan **manual sepenuhnya** | Apakah layanannya bernilai | Kecil–sedang |
| ***Wizard of Oz*** | Tampak otomatis, di balik layar manual | Apakah alurnya berjalan | Sedang |
| **Purwarupa** | Antarmuka yang dapat diklik, belum berfungsi | Apakah alurnya dipahami | Kecil |
| ***No-code*** | Dibangun dengan alat siap pakai | Apakah produknya dipakai | Sedang |
| **Versi tunggal fitur** | Satu fitur inti saja, berfungsi | Apakah fitur inti cukup | Sedang–besar |

#### 10.2.1 Memilih Berdasarkan Asumsi

| Asumsi yang paling berisiko | Jenis MVP yang sesuai |
|-----------------------------|----------------------|
| "Ada yang tertarik dengan tawaran ini" | *Landing page* |
| "Layanannya bernilai bagi mereka" | *Concierge* |
| "Mereka bersedia membayar" | *Landing page* dengan pembayaran, atau *concierge* berbayar |
| "Mereka memahami cara memakainya" | Purwarupa yang dapat diklik |
| "Mereka akan memakainya berulang" | *No-code* atau versi tunggal fitur |
| "Teknologinya dapat dibangun" | Purwarupa teknis (bukan MVP untuk pelanggan) |

> **Kaidah:** pilih jenis MVP yang **paling murah** yang masih dapat menguji asumsi itu. Membangun lebih dari yang diperlukan untuk menguji adalah pemborosan — dan pada tahap ini, waktu adalah sumber daya paling langka.

#### 10.2.2 *Concierge MVP* — Sering Terabaikan

Layanan dikerjakan **sepenuhnya manual** oleh tim, tanpa sistem apa pun.

| Kelebihan | Keterangan |
|-----------|------------|
| Dapat dimulai **hari ini** | Tidak perlu membangun apa pun |
| Pembelajaran paling dalam | Tim melihat langsung setiap kesulitan |
| Mengungkap kebutuhan tak terduga | Yang tidak muncul dalam wawancara |
| Menguji nilai, bukan antarmuka | Memisahkan dua hal yang sering tertukar |

| Ketentuan etis | Penjelasan |
|----------------|------------|
| **Pengguna tahu ini tahap awal** | Tidak berpura-pura sebagai layanan mapan |
| **Tidak mengklaim otomatis** | Bila dikerjakan manual, tidak dikatakan "sistem kami" |
| Data dijaga | Meski dikerjakan manual |

> Menyembunyikan bahwa layanan dikerjakan manual, sambil mengklaim otomatisasi, adalah bentuk **`tadlis`** — menyembunyikan keadaan sebenarnya dari pihak yang bertransaksi.

---

### 10.3 Merancang Eksperimen

#### 10.3.1 Format

| Unsur | Isi |
|-------|-----|
| **Asumsi yang diuji** | Dinyatakan sebagai kalimat yang dapat salah |
| **Hipotesis** | "Bila [tindakan], maka [hasil] sebesar [angka]" |
| **Cara mengukur** | Apa yang diamati, bagaimana |
| **Ukuran keberhasilan** | Angka yang ditetapkan **sebelum** eksperimen |
| **Jumlah peserta** | Berapa orang, dari mana |
| **Durasi** | Kapan mulai dan berakhir |

Contoh:

| Unsur | Isi |
|-------|-----|
| Asumsi | Pedagang bersedia mencatat penjualan setelah jam ramai, bukan per transaksi |
| Hipotesis | Bila diberi alat pencatatan sekaligus, maka ≥ 3 dari 5 peserta akan memakainya ≥ 4 hari dalam seminggu |
| Cara mengukur | Catatan harian yang terisi; wawancara singkat tiap 2 hari |
| Ukuran keberhasilan | **≥ 3 dari 5** |
| Peserta | 5 pedagang dari wawancara sebelumnya |
| Durasi | 7 hari |

> **Ukuran keberhasilan ditetapkan sebelum eksperimen.** Tanpa itu, hasil apa pun akan ditafsirkan sebagai keberhasilan — karena tim menginginkannya berhasil.

#### 10.3.2 Merancang agar Dapat Gagal

Eksperimen yang tidak dapat gagal tidak mengajarkan apa pun.

| Eksperimen yang tidak dapat gagal | Perbaikan |
|-----------------------------------|-----------|
| "Kami akan menunjukkan purwarupa dan menanyakan pendapat" | "Kami akan meminta mereka menyelesaikan tugas X tanpa dibantu; ukuran keberhasilan: 4 dari 5 selesai < 2 menit" |
| "Kami akan melihat apakah mereka suka" | "Kami akan melihat apakah mereka kembali memakainya dalam 3 hari tanpa diingatkan" |
| "Kami akan mengumpulkan umpan balik" | "Kami akan mencatat berapa yang menyelesaikan pendaftaran sampai tahap pembayaran" |

Perbedaannya: kolom kanan mengamati **perilaku**, kolom kiri mengumpulkan **pendapat**. Pendapat dapat menyenangkan; perilaku tidak berbohong.

---

### 10.4 Menguji MVP

#### 10.4.1 Ketentuan Pengujian

| Aspek | Ketentuan |
|-------|-----------|
| Peserta | **Minimal 5 orang di luar tim** |
| Siapa | Sesuai persona; bukan teman yang ingin membantu |
| Cara | Amati mereka memakainya; **jangan membantu kecuali benar-benar macet** |
| Yang dicatat | Apa yang mereka lakukan, di mana berhenti, apa yang mereka katakan |
| Yang dihindari | Menjelaskan cara pakai lebih dahulu |

> **Kesalahan paling merusak dalam pengujian MVP:** menjelaskan cara memakainya lebih dahulu. Dalam pemakaian nyata tidak ada yang menjelaskan. Bila peserta tidak dapat mulai tanpa penjelasan, itu **temuan**, bukan hambatan pengujian.

#### 10.4.2 Format Catatan Pengujian

```markdown
## Pengujian MVP #02

| Aspek | Isi |
|-------|-----|
| Tanggal | 2026-11-03 |
| Peserta | D. — pedagang kelontong, sesuai persona 1 |
| Durasi | 18 menit |
| Tugas yang diminta | "Catat penjualan hari ini seperti biasanya Anda lakukan" |

### Yang Diamati

| Waktu | Yang terjadi |
|-------|--------------|
| 0:00 | Membuka aplikasi, diam 12 detik mencari tombol |
| 0:12 | Menekan menu yang salah dua kali |
| 0:40 | Menemukan tombol tambah; mulai mengisi |
| 1:20 | Berhenti: "ini harus isi semua ya?" |
| 2:05 | Selesai satu entri |

### Kutipan

- "Ini harus isi semua ya? Kalau buru-buru gimana?"
- "Kalau cuma buat catat jualan, buku saya lebih cepat."

### Hasil terhadap Ukuran Keberhasilan

Ukuran: menyelesaikan 3 entri dalam < 2 menit.
Hasil: **TIDAK TERCAPAI** — 1 entri dalam 2 menit.

### Yang Dipelajari

Hambatan bukan pada konsep, melainkan pada jumlah kolom wajib.
Peserta membandingkan langsung dengan buku tulis — kompetitor
tidak langsung yang teridentifikasi pada Minggu 5.

### Tindakan

Uji versi dengan 2 kolom wajib saja pada pengujian berikutnya.
```

Bagian "Hasil terhadap Ukuran Keberhasilan" wajib menyatakan **tercapai atau tidak** secara tegas. Menuliskan "cukup baik" tanpa membandingkan dengan ukuran yang ditetapkan adalah cara menghindari kesimpulan.

---

### 10.5 Membaca Hasil Eksperimen

| Hasil | Tafsir | Tindakan |
|-------|--------|----------|
| Melampaui ukuran keberhasilan | Asumsi didukung | Lanjut; uji asumsi berikutnya |
| Mendekati ukuran | Tidak meyakinkan | Perbaiki dan uji ulang |
| Jauh di bawah ukuran | **Asumsi kemungkinan keliru** | Cari tahu mengapa; pertimbangkan mengubah arah |
| Tidak dapat disimpulkan | Rancangan eksperimen bermasalah | Perbaiki rancangan, ulangi |

#### 10.5.1 Ketika Hasilnya Mengecewakan

Ini adalah momen yang paling menentukan dalam seluruh mata kuliah.

| Reaksi yang keliru | Reaksi yang tepat |
|--------------------|-------------------|
| "Mereka belum paham nilainya" | "Apa yang membuat mereka tidak melanjutkan?" |
| "Kita perlu lebih banyak fitur" | "Apakah asumsi dasarnya yang keliru?" |
| "Pesertanya tidak sesuai" | "Apakah persona kita yang perlu dipertajam?" |
| "Nanti kalau sudah rapi pasti dipakai" | "Apa bukti bahwa kerapian yang menjadi hambatan?" |

> Kolom kiri adalah cara menolak bukti. Kolom kanan adalah cara belajar darinya.
>
> Sub-CPMK `UAI32-1` menilai **bukti adaptasi keputusan**. Momen inilah tempat penilaian itu berlangsung.

---

### 10.6 Yang Dinilai dari MVP

> **MVP paling sederhana yang diuji dengan baik lebih bernilai daripada aplikasi lengkap yang tidak pernah ditunjukkan kepada siapa pun.**

| Yang dinilai | Yang **tidak** dinilai |
|--------------|------------------------|
| Ketepatan memilih asumsi yang diuji | Kecanggihan teknologi |
| Kejelasan hipotesis dan ukuran keberhasilan | Kelengkapan fitur |
| Kualitas pengamatan selama pengujian | Kerapian antarmuka |
| **Kedalaman pembelajaran, termasuk dari kegagalan** | Apakah hasilnya berhasil |
| Tindakan yang diambil berdasarkan hasil | — |

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 9 buku ajar](../06-buku-ajar/bab-09-mvp-merancang-yang-paling-sedikit.md).
- Menentukan **asumsi paling berisiko** yang hendak diuji.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Pembahasan BMC; ketidaksesuaian yang ditemukan pada uji cerita |
| Konsep | 30' | Definisi MVP; jenis MVP; memilih berdasarkan asumsi |
| **Studio** | 40' | **Kegiatan inti:** merancang eksperimen — asumsi, hipotesis, ukuran keberhasilan |
| Presentasi silang | 25' | Tim menukar rancangan; mencari eksperimen yang tidak dapat gagal |
| Konsep | 20' | Ketentuan pengujian; format catatan |
| Studio | 20' | Mulai membangun MVP |
| Penutup | 5' | Target: MVP diuji ke 5 orang sebelum Minggu 11 |

**Kegiatan inti — audit "dapatkah gagal?":** tim menukar rancangan eksperimen dan memeriksa: *"adakah hasil yang mungkin terjadi yang akan membuat tim ini menyimpulkan asumsinya keliru?"*

Bila jawabannya tidak ada, rancangan itu harus diperbaiki.

### Setelah Kelas (120 menit)

- Membangun MVP (bentuk apa pun yang sesuai).
- **Menguji kepada minimal 5 orang di luar tim** sebelum Minggu 11.
- Menyelesaikan [Studio 10](../04-labs/lab-10-rancang-dan-uji-mvp.md).

---

## Penugasan

**S-10 — Rancang dan Uji MVP**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | MVP (tautan/berkas) + rancangan eksperimen + catatan pengujian |
| Pengujian | **Minimal 5 orang di luar tim**, sesuai persona |
| Rancangan | Asumsi · hipotesis · cara mengukur · **ukuran keberhasilan ditetapkan sebelumnya** |
| Catatan | Format §10.4.2, termasuk **pernyataan tegas tercapai/tidak** |
| Penutup | Apa yang dipelajari dan **tindakan** yang diambil |
| Tenggat | Awal pertemuan Minggu 11 |
| Bobot | Bagian dari P-03 (dinilai Minggu 11) |
| Yang menggugurkan | Tidak diuji di luar tim; ukuran keberhasilan ditetapkan setelah melihat hasil |

---

## Rangkuman

1. **MVP diukur dari pembelajaran**, bukan dari kelengkapan.
2. Pertanyaan yang menentukan: **asumsi apa yang paling berisiko, dan apa cara termurah mengujinya?**
3. Pilih jenis MVP **paling murah** yang masih dapat menguji asumsi itu.
4. ***Concierge MVP*** memberi pembelajaran paling dalam dan dapat dimulai hari ini.
5. Menyembunyikan bahwa layanan dikerjakan manual sambil mengklaim otomatis adalah **`tadlis`**.
6. **Ukuran keberhasilan ditetapkan sebelum eksperimen.**
7. Eksperimen yang **tidak dapat gagal tidak mengajarkan apa pun**.
8. Amati **perilaku**, bukan pendapat. Pendapat dapat menyenangkan; perilaku tidak berbohong.
9. **Jangan menjelaskan cara pakai lebih dahulu** — dalam pemakaian nyata tidak ada yang menjelaskan.
10. Hasil yang mengecewakan adalah **momen penilaian adaptasi**, bukan kegagalan.
11. **MVP sederhana yang diuji baik > aplikasi lengkap yang tidak pernah ditunjukkan.**

---

## Referensi

1. Ries, E. (2011). *The Lean Startup*, Bab 6–7. Crown Business.
2. Blank, S., & Dorf, B. (2020). *The Startup Owner's Manual*, Bab 7. Wiley.
3. Maurya, A. (2012). *Running Lean* (2nd ed.). O'Reilly.
4. Krug, S. (2009). *Rocket Surgery Made Easy*. New Riders.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
