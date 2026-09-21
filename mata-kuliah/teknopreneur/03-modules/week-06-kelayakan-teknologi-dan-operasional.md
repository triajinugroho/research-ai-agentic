# Minggu 6: Kelayakan Teknologi dan Operasional

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Teknopreneur (`ST52510002`) |
| Minggu | 6 dari 16 |
| Topik | Kelayakan teknis; ketergantungan pihak ketiga; kebutuhan operasional; *build vs buy* |
| Sub-CPMK | `TEKNO-Sub-CPMKUAI21-1` |
| Bloom | C4 → C5 |
| Durasi | 150 menit |
| Metode | Kuliah · Studio penilaian |
| Penilaian | Observasi (Studio 6) |

---

## Tujuan Pembelajaran

1. **Menganalisis** (C4) kelayakan teknis solusi yang direncanakan.
2. **Mengenali** (C4) ketergantungan pihak ketiga dan risikonya.
3. **Mengevaluasi** (C5) kebutuhan operasional di luar pembangunan produk.
4. **Memutuskan** (C5) antara membangun sendiri dan memakai yang tersedia.

---

## Materi Pembelajaran

### 6.1 Tiga Pertanyaan Kelayakan

| Pertanyaan | Ranah |
|-----------|-------|
| **Dapatkah dibangun?** | Kelayakan teknis |
| **Dapatkah dijalankan?** | Kelayakan operasional |
| **Dapatkah dibiayai?** | Kelayakan finansial (Minggu 7) |

Tim yang berlatar teknis cenderung hanya menjawab pertanyaan pertama — dan pertanyaan kedua yang lebih sering menggagalkan usaha.

---

### 6.2 Kelayakan Teknis

#### 6.2.1 Daftar Pemeriksaan

| Aspek | Pertanyaan |
|-------|-----------|
| Komponen inti | Apa yang **harus** dibangun sendiri karena menjadi pembeda? |
| Keterampilan tim | Apakah tim memiliki keterampilan itu? Bila tidak, bagaimana memperolehnya? |
| Waktu | Berapa lama versi pertama yang dapat dipakai? |
| Ketergantungan | Apa yang bergantung pada pihak lain? |
| Ketidakpastian teknis | Adakah bagian yang **belum tentu bisa** dikerjakan? |

Baris terakhir sering dilewati. Bila ada bagian yang belum tentu dapat dikerjakan, **ia harus diuji lebih dahulu** sebelum yang lain dibangun — karena kegagalannya membatalkan segalanya.

#### 6.2.2 Menilai Kemampuan Tim dengan Jujur

| Tingkat | Ciri | Konsekuensi |
|---------|------|-------------|
| Menguasai | Pernah mengerjakan hal serupa sampai selesai | Dapat diperkirakan waktunya |
| Familiar | Memahami konsepnya, belum pernah menyelesaikan | Perkiraan waktu × 2–3 |
| Belum tahu | Baru mendengar namanya | **Tidak dapat diperkirakan** — harus dipelajari dan diuji dahulu |

> Penilaian yang jujur di sini menentukan kelayakan rencana. Tim yang menuliskan "kami akan membangun sistem rekomendasi" padahal belum pernah melatih model apa pun sedang membuat rencana yang tidak dapat dipertanggungjawabkan.

---

### 6.3 Ketergantungan Pihak Ketiga

#### 6.3.1 Jenis dan Risikonya

| Jenis | Contoh | Risiko |
|-------|--------|--------|
| API berbayar | Peta, pembayaran, pengiriman pesan | Harga naik; layanan dihentikan; kuota dibatasi |
| Model AI | Penyedia LLM | **Biaya berubah; model diubah; ketersediaan** |
| Platform | *Marketplace*, media sosial | Aturan berubah sepihak |
| Infrastruktur | Layanan awan | Biaya melonjak seiring skala |
| Data | Sumber data eksternal | Akses dicabut; format berubah |

#### 6.3.2 Menilai Risiko Ketergantungan

| Pertanyaan | Mengapa penting |
|-----------|-----------------|
| Apa yang terjadi bila layanan ini berhenti besok? | Menguji ketahanan |
| Berapa biaya berpindah ke penyedia lain? | Mengukur keterkuncian |
| Apakah ada alternatif yang setara? | Menentukan daya tawar |
| Berapa proporsi biaya kita yang mengalir ke penyedia ini? | Menentukan kerentanan margin |

> **Kasus yang layak dibahas:** banyak usaha yang dibangun di atas satu API pihak ketiga mengalami guncangan ketika harga API itu dinaikkan berlipat. Pelajarannya bukan "jangan pakai API pihak ketiga" — melainkan **ketahui berapa biaya berpindah, dan jangan biarkan seluruh margin bergantung pada satu penyedia yang dapat mengubah harga sepihak.**

---

### 6.4 Kelayakan Operasional

Ini bagian yang paling sering diabaikan tim berlatar teknis. **Produk bukan usaha.** Menjalankan usaha menuntut hal-hal di luar membangun produk.

| Kebutuhan operasional | Pertanyaan |
|-----------------------|-----------|
| Dukungan pengguna | Siapa menjawab pertanyaan pengguna? Berapa lama waktunya? |
| Penerimaan pengguna baru (*onboarding*) | Apakah pengguna dapat mulai sendiri, atau perlu dibantu? |
| Penagihan dan pembayaran | Bagaimana uang masuk? Siapa yang menangani kegagalan pembayaran? |
| Pemeliharaan | Siapa memperbaiki bila rusak pada pukul 22.00? |
| Pemantauan | Bagaimana tahu ada yang rusak sebelum pengguna mengeluh? |
| Kepatuhan | Perizinan, pajak, perlindungan data |
| Pengadaan konten/data | Bila produk membutuhkan data yang terus diperbarui |

#### 6.4.1 Menghitung Beban Operasional

Untuk setiap 100 pengguna, perkirakan:

| Kegiatan | Waktu per pengguna per bulan | Total untuk 100 pengguna |
|----------|------------------------------|--------------------------|
| *Onboarding* | 20 menit | 33 jam |
| Dukungan | 10 menit | 17 jam |
| Penanganan masalah | 5 menit | 8 jam |
| **Total** | | **58 jam/bulan** |

58 jam per bulan untuk 100 pengguna berarti **hampir satu orang penuh waktu**. Bila harga produk Rp 50.000/bulan, pendapatan dari 100 pengguna adalah Rp 5 juta — tidak cukup membayar satu orang.

> **Inilah jenis perhitungan yang membatalkan rencana yang tampak masuk akal.** Ia tidak memerlukan model finansial rumit — hanya kejujuran tentang berapa waktu yang benar-benar dibutuhkan.

#### 6.4.2 Beban yang Tidak Berskala

| Beban | Berskala? | Akibat |
|-------|-----------|--------|
| Biaya server | Ya, dengan biaya | Dapat ditangani |
| *Onboarding* manual per pengguna | **Tidak** | Menjadi penghalang pertumbuhan |
| Dukungan melalui pesan pribadi | **Tidak** | Menjadi penghalang pertumbuhan |
| Pemeriksaan kualitas manual | **Tidak** | Menjadi penghalang pertumbuhan |

Pada tahap awal, beban yang tidak berskala **justru disarankan** — ia memberi pembelajaran yang tidak diperoleh dengan cara lain. Yang keliru adalah **merencanakan pertumbuhan tanpa rencana menggantikannya**.

---

### 6.5 *Build vs Buy*

| Pertimbangan | Bangun sendiri | Pakai yang ada |
|--------------|----------------|----------------|
| Apakah ini **pembeda** kita? | Ya → bangun | Tidak → pakai |
| Apakah tim mampu? | Ya | Tidak → pakai |
| Berapa waktu yang dibutuhkan? | Lama → pertimbangkan | Cepat |
| Berapa biayanya dalam skala? | Mungkin lebih murah | Bisa mahal seiring skala |
| Seberapa penting kendali penuh? | Tinggi → bangun | Rendah → pakai |

#### 6.5.1 Kaidah Praktis

> **Bangun apa yang menjadi pembeda Anda; pakai yang tersedia untuk sisanya.**

Tim yang membangun sistem pembayaran sendiri padahal pembeda mereka adalah antarmuka yang sederhana telah menghabiskan waktu pada bagian yang tidak menghasilkan keunggulan apa pun — dan memikul risiko keamanan yang besar tanpa perlu.

Sebaliknya, tim yang memakai layanan siap pakai untuk **inti pembedanya** akan menemukan bahwa produknya tidak berbeda dari produk lain yang memakai layanan yang sama.

---

### 6.6 Kelayakan sebagai Keputusan, Bukan Laporan

Hasil analisis kelayakan bukan dokumen untuk diarsipkan. Ia menghasilkan **salah satu dari tiga keputusan**:

| Keputusan | Kapan |
|-----------|-------|
| **Lanjut** | Seluruh pertanyaan kelayakan terjawab memadai |
| **Ubah** | Ada hambatan yang dapat diatasi dengan mengubah cakupan atau pendekatan |
| **Hentikan** | Ada hambatan mendasar yang tidak dapat diatasi tim ini dalam waktu ini |

> Keputusan ketiga adalah keputusan yang sah dan **tidak merugikan nilai**, asalkan didukung analisis yang benar. Menemukan ketidaklayakan pada Minggu 6 jauh lebih murah daripada menemukannya pada Minggu 14 — atau, di dunia nyata, setelah dua tahun dan tabungan yang habis.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 6 buku ajar](../06-buku-ajar/bab-06-kelayakan-teknologi-dan-operasional.md).
- Menyusun daftar komponen teknologi yang dibutuhkan solusi tim.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Pembahasan S-05; angka pasar yang perlu diverifikasi ulang |
| Konsep | 30' | Kelayakan teknis; penilaian kemampuan tim yang jujur |
| Konsep | 25' | Ketergantungan pihak ketiga; *build vs buy* |
| **Studio** | 50' | **Kegiatan inti:** menghitung beban operasional untuk 100 pengguna |
| Presentasi silang | 25' | Tim menyajikan titik kegagalan operasionalnya |
| Penutup | 10' | Penugasan |

**Kegiatan inti — perhitungan beban operasional:** tiap tim menghitung berapa jam per bulan dibutuhkan untuk melayani 100 pengguna, lalu membandingkannya dengan pendapatan dari 100 pengguna pada harga yang direncanakan.

Hasilnya hampir selalu mengejutkan. Tim yang menemukan bahwa rencananya tidak dapat berjalan pada skala itu kemudian mendiskusikan: apa yang harus diotomatiskan, atau berapa harga yang sebenarnya diperlukan?

### Setelah Kelas (120 menit)

- Menyelesaikan [Studio 6](../04-labs/lab-06-uji-kelayakan-teknologi.md).
- Menyiapkan model *unit economics* untuk Minggu 7.

---

## Penugasan

**S-06 — Uji Kelayakan Teknologi dan Operasional**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Dokumen penilaian kelayakan |
| Isi | Komponen teknologi · **penilaian jujur kemampuan tim** · ketergantungan pihak ketiga dan risikonya · **perhitungan beban operasional untuk 100 pengguna** · keputusan *build/buy* · titik kegagalan |
| Penutup | **Keputusan: lanjut, ubah, atau hentikan** — dengan alasan |
| Tenggat | Awal pertemuan Minggu 7 |
| Bobot | 6,25% (Observasi) |

---

## Rangkuman

1. Tiga pertanyaan kelayakan: **dapatkah dibangun, dijalankan, dan dibiayai?**
2. Tim teknis cenderung hanya menjawab yang pertama; **yang kedua lebih sering menggagalkan usaha**.
3. Bagian yang **belum tentu dapat dikerjakan wajib diuji lebih dahulu**.
4. Penilaian kemampuan tim yang jujur: menguasai / familiar / belum tahu — dengan konsekuensi berbeda.
5. **Ketergantungan pihak ketiga** menuntut jawaban atas: apa bila berhenti besok, dan berapa biaya berpindah.
6. **Produk bukan usaha.** Beban operasional di luar pembangunan sering menentukan.
7. **Perhitungan beban per 100 pengguna** sering membatalkan rencana yang tampak masuk akal.
8. Beban yang tidak berskala disarankan pada tahap awal — **yang keliru adalah merencanakan pertumbuhan tanpa rencana menggantikannya**.
9. **Bangun apa yang menjadi pembeda; pakai yang tersedia untuk sisanya.**
10. Analisis kelayakan menghasilkan **keputusan**: lanjut, ubah, atau **hentikan** — dan yang ketiga sah.

---

## Referensi

1. Blank, S., & Dorf, B. (2020). *The Startup Owner's Manual*, Bab 6. Wiley.
2. Ries, E. (2011). *The Lean Startup*, Bab 6. Crown Business.
3. Kalbach, J. (2020). *The Jobs to Be Done Playbook*. Two Waves Books.
4. Dokumentasi harga penyedia layanan awan dan API (diperiksa saat penyusunan rencana).
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
