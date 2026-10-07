# Studio 06: Uji Kelayakan Teknologi dan Operasional

| Aspek | Keterangan |
|-------|------------|
| Minggu | 6 · Sub-CPMK `UAI21-1` · Bobot 6,25% (Observasi) |
| Durasi | 50' di kelas + 60' mandiri |
| Luaran | Dokumen penilaian kelayakan + keputusan |

---

## Tujuan Studio

1. Menilai kemampuan tim terhadap komponen teknologi yang dibutuhkan secara jujur.
2. Mengidentifikasi ketergantungan pihak ketiga dan risikonya.
3. **Menghitung beban operasional untuk 100 pengguna.**
4. Memutuskan *build vs buy* dan menyatakan keputusan kelayakan.

---

## Langkah-langkah

### LANGKAH 1: Menguraikan Komponen Teknologi

Dari persyaratan produk (Studio 4), uraikan komponen yang dibutuhkan:

| Komponen | Untuk persyaratan | Kemampuan tim | Perkiraan waktu | Ketidakpastian |
|----------|-------------------|---------------|-----------------|----------------|
| | K-01 | menguasai / familiar / belum tahu | | rendah / sedang / **tinggi** |

**Kaidah penilaian kemampuan:**

| Tingkat | Ciri | Pengganda waktu |
|---------|------|-----------------|
| **Menguasai** | Pernah mengerjakan hal serupa **sampai selesai** | ×1 |
| **Familiar** | Memahami konsep, belum pernah menyelesaikan | ×2–3 |
| **Belum tahu** | Baru mendengar namanya | **Tidak dapat diperkirakan** |

> Komponen dengan kemampuan "belum tahu" **tidak dapat dimasukkan ke dalam rencana** sebelum diuji. Yang harus dilakukan: sisihkan waktu untuk mempelajarinya dan membuat percobaan kecil terlebih dahulu.

### LANGKAH 2: Menguji Ketidakpastian Tertinggi Lebih Dahulu

| Komponen berketidakpastian tinggi | Cara mengujinya | Waktu yang disediakan | Hasil |
|-----------------------------------|-----------------|----------------------|-------|
| | (percobaan kecil, bukan produk) | (maksimal 1 minggu) | |

> Bila sebuah komponen **belum tentu dapat dikerjakan**, kegagalannya membatalkan seluruh rencana. Menguji lebih dahulu adalah cara termurah mengetahuinya.

### LANGKAH 3: Memetakan Ketergantungan Pihak Ketiga

| Penyedia | Untuk apa | Biaya sekarang | Bila berhenti besok? | Biaya berpindah | Alternatif |
|----------|-----------|----------------|---------------------|-----------------|------------|
| | | | | rendah/sedang/tinggi | |

**Empat pertanyaan wajib untuk setiap ketergantungan:**

1. Apa yang terjadi bila layanan ini berhenti besok?
2. Berapa biaya berpindah ke penyedia lain — dalam waktu dan uang?
3. Apakah ada alternatif yang setara?
4. Berapa proporsi biaya kita yang mengalir ke penyedia ini?

> Bila jawaban nomor 4 melebihi separuh biaya langsung, **seluruh margin bergantung pada pihak yang dapat mengubah harga sepihak**. Ini adalah risiko yang wajib dicatat pada daftar risiko Studio 7.

### LANGKAH 4: Menghitung Beban Operasional

Ini bagian inti studio ini.

**Untuk 100 pengguna per bulan:**

| Kegiatan | Waktu per pengguna | Frekuensi/bulan | Total jam/bulan |
|----------|--------------------|-----------------|-----------------|
| *Onboarding* pengguna baru | | | |
| Menjawab pertanyaan | | | |
| Menangani masalah | | | |
| Memeriksa kualitas (bila ada) | | | |
| Menagih dan menangani kegagalan bayar | | | |
| Pemeliharaan dan pemantauan | | (tetap) | |
| **TOTAL** | | | |

**Bandingkan dengan pendapatan:**

| Aspek | Perhitungan | Nilai |
|-------|-------------|-------|
| Pendapatan dari 100 pengguna | 100 × harga bulanan | |
| Beban operasional (jam) | dari tabel di atas | |
| **Setara berapa orang penuh waktu?** | jam ÷ 160 | |
| Biaya orang (bila dibayar) | orang × nilai bulanan | |
| **Sisa untuk semua biaya lain** | pendapatan − biaya orang | |

> **Hasil perhitungan ini sering membatalkan rencana yang tampak masuk akal.** Bila 100 pengguna menghasilkan Rp 5 juta dan menuntut 58 jam kerja per bulan, sisa untuk server, pemasaran, dan keuntungan hampir tidak ada.

### LANGKAH 5: Memisahkan Beban yang Berskala

| Beban | Berskala? | Bila tidak: rencana menggantikannya |
|-------|-----------|-------------------------------------|
| | ya / tidak | |

**Kaidah:**

- Pada tahap awal, beban yang tidak berskala **disarankan** — ia memberi pembelajaran yang tidak diperoleh dengan cara lain.
- Yang keliru adalah **merencanakan pertumbuhan tanpa rencana menggantikannya**.
- Untuk setiap beban yang tidak berskala, tuliskan: pada jumlah pengguna berapa ia menjadi penghalang, dan apa yang akan menggantikannya.

### LANGKAH 6: Keputusan *Build vs Buy*

| Komponen | Pembeda kita? | Tim mampu? | Waktu bangun | Biaya beli | **Keputusan** | Alasan |
|----------|---------------|------------|--------------|-----------|---------------|--------|
| | ya/tidak | ya/tidak | | | bangun/beli | |

**Kaidah:** *bangun apa yang menjadi pembeda; pakai yang tersedia untuk sisanya.*

Periksa: adakah komponen yang **menjadi pembeda tetapi diputuskan "beli"**? Bila ya, apa yang membedakan produk tim dari produk lain yang memakai layanan yang sama?

### LANGKAH 7: Menyatakan Keputusan Kelayakan

```markdown
## Keputusan Kelayakan Teknologi dan Operasional

### Ringkasan Temuan

| Aspek | Keadaan |
|-------|---------|
| Komponen berketidakpastian tinggi | |
| Ketergantungan yang paling berisiko | |
| Beban operasional per 100 pengguna | ... jam/bulan |
| Setara berapa orang penuh waktu | |
| Sisa pendapatan setelah biaya orang | |

### Titik Kegagalan yang Teridentifikasi

1.
2.
3.

### KEPUTUSAN

Pilih salah satu:

- [ ] **LANJUT** — seluruh pertanyaan kelayakan terjawab memadai
- [ ] **UBAH** — [apa yang diubah] karena [hambatan yang ditemukan]
- [ ] **HENTIKAN** — karena [hambatan mendasar yang tidak dapat diatasi]

### Alasan

[Satu paragraf, merujuk pada angka di atas]
```

> **Pilihan "HENTIKAN" adalah pilihan yang sah dan tidak merugikan nilai**, asalkan didukung analisis yang benar. Menemukan ketidaklayakan pada Minggu 6 jauh lebih murah daripada menemukannya pada Minggu 14.

---

## Tantangan Tambahan

### Tantangan 1 — Memeriksa Harga Sebenarnya

Untuk setiap layanan pihak ketiga, buka halaman harganya dan hitung biaya nyata pada 100, 1.000, dan 10.000 pengguna. Apakah biayanya turun per pengguna, atau naik sebanding?

### Tantangan 2 — Simulasi Satu Hari Operasional

Selama satu hari, salah satu anggota berperan sebagai "petugas operasional": menangani seluruh pertanyaan dan masalah yang muncul dari pengujian. Catat berapa waktu yang benar-benar terpakai.

### Tantangan 3 — Rencana Ketika Penyedia Berhenti

Pilih satu ketergantungan terbesar. Susun rencana konkret: bila layanan itu berhenti besok, apa yang dilakukan pada hari 1, minggu 1, dan bulan 1?

---

## Checklist Penyelesaian

- [ ] Komponen teknologi diuraikan dari persyaratan produk
- [ ] Kemampuan tim dinilai **jujur** (menguasai/familiar/belum tahu)
- [ ] Komponen berketidakpastian tinggi **diuji lebih dahulu**
- [ ] Ketergantungan pihak ketiga dipetakan dengan **empat pertanyaan wajib**
- [ ] **Beban operasional untuk 100 pengguna dihitung**
- [ ] Beban dibandingkan dengan pendapatan dari 100 pengguna
- [ ] Beban yang tidak berskala diidentifikasi beserta rencana menggantikannya
- [ ] Keputusan *build vs buy* dengan alasan
- [ ] **Keputusan kelayakan dinyatakan**: lanjut / ubah / hentikan
- [ ] AI Usage Log disertakan

---

## Referensi

1. [Modul Minggu 6](../03-modules/week-06-kelayakan-teknologi-dan-operasional.md)
2. [Bab 6 buku ajar](../06-buku-ajar/bab-06-kelayakan-teknologi-dan-operasional.md)
3. Ries, E. (2011). *The Lean Startup*, Bab 6. Crown Business.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
