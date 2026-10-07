# Studio 12: Audit Etika dan Kepatuhan

| Aspek | Keterangan |
|-------|------------|
| Minggu | 12 · Sub-CPMK `UAI22-1` · Bagian dari P-03 |
| Durasi | 40' di kelas + 60' mandiri |
| Luaran | Daftar periksa terisi + laporan temuan + analisis dampak |

---

## Tujuan Studio

1. Mengaudit usaha sendiri terhadap kepatuhan hukum dan etika.
2. Mengenali pola gelap dalam rancangan sendiri.
3. Menganalisis dampak usaha terhadap pihak yang tidak menjadi pengguna.
4. Menyusun rencana perbaikan yang konkret.

---

## Ketentuan Khusus Studio Ini

> **Temuan yang jujur dinilai lebih tinggi daripada daftar periksa yang seluruhnya tercentang.**
>
> Hampir tidak ada rancangan tahap awal yang sudah memenuhi seluruh butir. Tim yang mencentang semuanya tanpa temuan akan diminta menelusuri ulang.

---

## Langkah-langkah

### LANGKAH 1: Audit Legalitas

| # | Butir | Keadaan | Temuan | Rencana |
|---|-------|---------|--------|---------|
| L1 | Bentuk badan usaha yang sesuai sudah dipertimbangkan | ✓ / ✗ | | |
| L2 | Nama usaha diperiksa ketersediaannya sebagai merek | ✓ / ✗ | | |
| L3 | Lisensi seluruh pustaka memperbolehkan penggunaan yang direncanakan | ✓ / ✗ | | |
| L4 | Lisensi aset visual (gambar, font) diperiksa | ✓ / ✗ | | |
| L5 | **Kepemilikan karya antaranggota disepakati tertulis** | ✓ / ✗ | | |

**Cara memeriksa L2:** telusuri basis data merek Direktorat Jenderal Kekayaan Intelektual dan pencarian umum. Catat hasilnya.

**Cara memeriksa L3:** untuk tiap pustaka, buka berkas lisensinya. Perhatikan: MIT dan Apache umumnya memperbolehkan penggunaan komersial; GPL menuntut karya turunan juga terbuka.

### LANGKAH 2: Audit Perlindungan Data

| # | Butir | Keadaan | Temuan | Rencana |
|---|-------|---------|--------|---------|
| D1 | **Setiap data yang dikumpulkan dapat dijawab "untuk apa"** | ✓ / ✗ | | |
| D2 | Data yang tidak dibutuhkan **tidak** dikumpulkan | ✓ / ✗ | | |
| D3 | Persetujuan jelas dan **tidak tercentang otomatis** | ✓ / ✗ | | |
| D4 | Tujuan pemrosesan dinyatakan dengan bahasa yang dipahami | ✓ / ✗ | | |
| D5 | Ada cara pengguna meminta penghapusan datanya | ✓ / ✗ | | |
| D6 | Data disimpan dengan pengamanan yang memadai | ✓ / ✗ | | |
| D7 | Pihak ketiga yang menerima data dinyatakan | ✓ / ✗ | | |

**Latihan D1 — uji setiap kolom:**

| Data yang dikumpulkan | Untuk apa | Apa yang terjadi bila tidak dikumpulkan? | **Tetap kumpulkan?** |
|-----------------------|-----------|------------------------------------------|---------------------|
| | | | |

> **Prinsip minimalisasi** paling mudah dipenuhi dan paling sering diabaikan. Setiap kolom yang tidak lolos uji ini harus dihapus.

**Termasuk data wawancara tim sendiri:**

- [ ] Catatan wawancara tidak memuat nama lengkap, NIK, alamat lengkap, atau nomor telepon
- [ ] Narasumber diberi tahu tujuan pengumpulan
- [ ] Dokumen tidak dibagikan secara terbuka

### LANGKAH 3: Audit Pola Gelap

Telusuri alur produk sendiri dan periksa:

| # | Pola | Ada? | Di mana | Perbaikan |
|---|------|------|---------|-----------|
| P1 | Pendaftaran mudah, pembatalan sulit | ya/tidak | | |
| P2 | Biaya tersembunyi sampai langkah terakhir | ya/tidak | | |
| P3 | Tombol "tidak" dibuat samar | ya/tidak | | |
| P4 | Urgensi atau kelangkaan palsu | ya/tidak | | |
| P5 | Uji coba otomatis menjadi berbayar tanpa pemberitahuan | ya/tidak | | |
| P6 | Persetujuan digabung dengan tindakan lain | ya/tidak | | |

**Padanan prinsip muamalah:**

| Pola | Prinsip yang dilanggar |
|------|------------------------|
| P1, P5 | `Gharar` — ketidakjelasan |
| P2, P4 | `Tadlis` — menyembunyikan keadaan |
| P3, P6 | `Tadlis` — memanipulasi persetujuan |

### LANGKAH 4: Tiga Uji Sederhana

Terapkan pada seluruh rancangan:

| # | Pertanyaan | Jawaban | Bagian yang gagal |
|---|-----------|---------|-------------------|
| 1 | Apakah pengguna akan setuju **bila mereka tahu sepenuhnya** apa yang terjadi? | | |
| 2 | Apakah kami bersedia **menjelaskan rancangan ini secara terbuka** kepada pengguna? | | |
| 3 | Apakah kami bersedia **bila orang tua kami menjadi penggunanya**? | | |

> Rancangan yang gagal pada salah satu pertanyaan ini perlu ditinjau ulang — bukan dibenarkan dengan alasan bahwa "semua orang melakukannya".

### LANGKAH 5: Analisis Dampak

| # | Pertanyaan | Jawaban |
|---|-----------|---------|
| 1 | **Siapa yang dapat dirugikan bila produk ini berhasil?** | |
| 2 | Kelompok mana yang **tidak terlayani** oleh produk ini? | |
| 3 | Apa yang terjadi bila produk ini **disalahgunakan**? | |
| 4 | Apakah ada pihak yang **kehilangan mata pencaharian**? | |
| 5 | Apakah produk ini **memperkuat ketimpangan** yang ada? | |

**Untuk setiap jawaban yang tidak kosong:**

| Dampak | Seberapa besar | Dapatkah dikurangi? | Bagaimana |
|--------|----------------|---------------------|-----------|
| | | | |

> **Menjawab "tidak ada" pada seluruh lima pertanyaan hampir selalu berarti belum dipikirkan.** Setiap produk yang mengubah cara orang mengerjakan sesuatu memiliki dampak pada pihak yang berkepentingan dengan cara lama.

### LANGKAH 6: Laporan Temuan

```markdown
# Laporan Audit Etika dan Kepatuhan

## 1. Ringkasan

| Kategori | Butir terpenuhi | Butir tidak terpenuhi |
|----------|-----------------|----------------------|
| Legalitas | /5 | |
| Perlindungan data | /7 | |
| Pola gelap | /6 | |
| Tiga uji sederhana | /3 | |

## 2. Temuan yang Paling Perlu Ditangani

| Prioritas | Temuan | Mengapa penting | Rencana | Kapan |
|-----------|--------|-----------------|---------|-------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## 3. Analisis Dampak

[Dari Langkah 5]

## 4. Yang Kami Putuskan Tidak Mengubah

| Hal | Mengapa tidak diubah | Risikonya |
|-----|---------------------|-----------|
| | | |

## 5. Pernyataan

Kami telah menelusuri seluruh alur produk dan menyatakan temuan
di atas apa adanya, termasuk yang belum kami perbaiki.

Tanda tangan seluruh anggota: ____________________
```

> **Bagian 4 penting.** Tidak seluruh temuan dapat diperbaiki dalam waktu yang tersedia. Yang dituntut adalah **menyatakannya**, bukan menyembunyikannya.

---

## Tantangan Tambahan

### Tantangan 1 — Mengaudit Aplikasi yang Dipakai Sehari-hari

Pilih satu aplikasi yang Anda pakai. Telusuri alur pendaftaran dan pembatalannya. Berapa pola gelap yang ditemukan? Bandingkan kemudahan mendaftar dengan kemudahan membatalkan.

### Tantangan 2 — Menulis Kebijakan Privasi yang Dapat Dipahami

Tulis kebijakan privasi produk tim dalam **bahasa yang dipahami segmen Anda** — bukan bahasa hukum. Maksimal satu halaman. Uji ke dua narasumber: apakah mereka memahaminya?

### Tantangan 3 — Wawancara tentang Dampak

Wawancarai satu orang dari pihak yang mungkin dirugikan bila produk berhasil (misalnya perantara yang perannya tergantikan). Apa pandangannya? Adakah rancangan yang mengurangi kerugian itu?

---

## Checklist Penyelesaian

- [ ] Audit legalitas 5 butir dengan temuan
- [ ] **Setiap kolom data diuji** dengan pertanyaan "untuk apa"
- [ ] Audit perlindungan data 7 butir
- [ ] Ketentuan data berlaku juga pada **catatan wawancara tim**
- [ ] Audit pola gelap 6 butir dengan padanan prinsip muamalah
- [ ] **Tiga uji sederhana** dijalankan
- [ ] **Analisis dampak lima pertanyaan** diisi
- [ ] Laporan temuan lengkap, termasuk **bagian "yang tidak diubah"**
- [ ] Temuan dinyatakan **jujur**, bukan seluruhnya tercentang
- [ ] AI Usage Log disertakan

---

## Referensi

1. [Modul Minggu 12](../03-modules/week-12-tata-kelola-legalitas-etika.md)
2. [Bab 11 buku ajar](../06-buku-ajar/bab-11-tata-kelola-legalitas-etika.md)
3. Undang-Undang No. 27 Tahun 2022 tentang Pelindungan Data Pribadi.
4. Brignull, H. *Deceptive Patterns*. <https://www.deceptive.design>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
