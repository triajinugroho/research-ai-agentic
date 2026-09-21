# Studio 05: Perhitungan Pasar dan Peta Kompetitor

| Aspek | Keterangan |
|-------|------------|
| Minggu | 5 · Sub-CPMK `UAI21-1` · Bobot 6,25% (Observasi) |
| Durasi | 45' di kelas + 90' mandiri |
| Luaran | Spreadsheet perhitungan + peta kompetitor + tabel perbandingan |

---

## Tujuan Studio

1. Menghitung TAM, SAM, dan SOM secara *bottom-up* dengan sumber.
2. Menyatakan setiap asumsi secara terbuka dan mengujinya.
3. Memetakan kompetitor langsung, tidak langsung, dan alternatif non-produk.
4. Mengidentifikasi mengapa orang meninggalkan solusi yang ada.

---

## Langkah-langkah

### LANGKAH 1: Menyiapkan Spreadsheet

Bangun dengan **sel asumsi terpisah** agar dapat diubah:

```
 A                          B            C           D
 1  ASUMSI                  NILAI        SUMBER      TANGGAL AKSES
 2  Jumlah UMKM Indonesia    64.200.000   KemenkopUKM  2026-09-20
 3  Proporsi kuliner         12%          BPS          2026-09-20
 4  Pakai ponsel untuk usaha 30%          BPS          2026-09-20
 5  Berada di Jabodetabek    4%           BPS          2026-09-20
 6  Bersedia membayar        20%          WAWANCARA    3 dari 15
 7  Harga tahunan            Rp 600.000   Rencana tim  -
 8  Pangsa realistis 2 th    3%           Kapasitas tim -
 9
10  PERHITUNGAN              HASIL        RUMUS
11  Segmen kuliner           =B2*B3
12  Dapat dijangkau          =B11*B4
13  SAM (jumlah)             =B12*B5
14  Pasar potensial          =B13*B6
15  SAM (nilai)              =B14*B7
16  SOM (nilai)              =B15*B8
```

**Ketentuan:**

- [ ] Setiap asumsi pada baris terpisah dengan **sumber dan tanggal akses**
- [ ] Perhitungan memakai **rumus**, bukan angka yang diketik
- [ ] Asumsi yang berasal dari wawancara sendiri **ditandai khusus**
- [ ] Mengubah satu asumsi langsung mengubah seluruh hasil

### LANGKAH 2: Memverifikasi Setiap Sumber

| Pemeriksaan | Pertanyaan |
|-------------|-----------|
| **Definisi** | Apa definisi "UMKM" yang dipakai sumber ini? Sama dengan yang kita maksud? |
| **Tahun** | Data tahun berapa? Masih relevan? |
| **Cakupan** | Nasional atau daerah tertentu? |
| **Metode** | Sensus, survei, atau perkiraan? |
| **Dapat ditelusuri** | Apakah ada tautan ke terbitan aslinya? |

> **Angka yang tidak dapat ditelusuri ke terbitan aslinya tidak boleh dipakai.** Ini berlaku khusus pada angka yang diperoleh dari AI — model bahasa sering menghasilkan angka yang terdengar meyakinkan lengkap dengan nama lembaga, tanpa terbitan yang benar-benar ada.

### LANGKAH 3: Analisis Sensitivitas

| Asumsi | Nilai dasar | Pesimis | Optimis | SOM pesimis | SOM optimis |
|--------|-------------|---------|---------|-------------|-------------|
| Bersedia membayar | 20% | 10% | 30% | | |
| Pangsa 2 tahun | 3% | 1,5% | 5% | | |
| Harga tahunan | Rp 600rb | Rp 400rb | Rp 800rb | | |

**Yang dilaporkan:**

> "SOM tahun kedua: **Rp 111 juta – Rp 833 juta**, dengan nilai tengah Rp 333 juta. Asumsi yang paling menentukan adalah kesediaan membayar (n=15, angka paling tidak pasti). Akan diuji dengan [cara] pada [waktu]."

### LANGKAH 4: Mengumpulkan Kompetitor

| Lapis | Minimal | Cara mencari |
|-------|---------|--------------|
| **Langsung** | 2 | Pencarian; toko aplikasi; rekomendasi narasumber |
| **Tidak langsung** | 2 | Apa lagi yang dipakai untuk pekerjaan yang sama? |
| **Alternatif non-produk** | 1 | **Dari wawancara: apa yang mereka pakai sekarang?** |

> Lapis ketiga hampir selalu ada dan hampir selalu terlewat. Dalam banyak kasus ia adalah **buku tulis, ingatan, atau meminta bantuan orang lain** — dan ia gratis, sudah dikuasai, dan tidak pernah gagal.

### LANGKAH 5: Tabel Perbandingan

| Aspek | Kompetitor A | Kompetitor B | Alternatif non-produk | Kita (rencana) |
|-------|--------------|--------------|----------------------|----------------|
| Harga | | | | |
| Waktu belajar | | | | |
| Waktu per tugas inti | | | | |
| Butuh koneksi | | | | |
| Kelebihan utama | | | | |
| Kelemahan utama | | | | |
| **Bukti dari wawancara** | | | | |

**Baris terakhir wajib.** Bila tidak ada narasumber yang menyebut sebuah kompetitor, tim perlu memeriksa: apakah kompetitor itu relevan, atau hanya ditemukan dari pencarian?

### LANGKAH 6: Mengapa Orang Meninggalkan Kompetitor

Dari catatan wawancara, kumpulkan:

| Kompetitor | Berapa yang pernah mencoba | Berapa yang berhenti | **Alasan berhenti** | Bukti |
|------------|----------------------------|---------------------|---------------------|-------|
| | /15 | | | |

> Kolom "alasan berhenti" adalah tambang informasi: ia menunjukkan **titik kegagalan yang dapat diserang**. Bila 4 dari 15 mencoba aplikasi kasir dan seluruhnya berhenti karena "ribet", maka kemudahan pakai adalah celah yang nyata — dan itu lebih berharga daripada daftar fitur kompetitor.

### LANGKAH 7: Peta Posisi

Pilih **dua dimensi yang paling menentukan keputusan pelanggan** — dari wawancara, bukan dugaan.

```
        [Dimensi 1 — tinggi]
                ▲
                │
                │
  [Dim 2 ───────┼───────► Dim 2
   rendah]      │          tinggi]
                │
                │
        [Dimensi 1 — rendah]
```

Tempatkan seluruh kompetitor dan posisi rencana tim. **Sebutkan dari kutipan mana kedua dimensi itu berasal.**

---

## Tantangan Tambahan

### Tantangan 1 — Perhitungan dari Dua Arah

Hitung SOM dengan cara kedua yang sama sekali berbeda (misalnya: dari kapasitas tim — berapa pelanggan dapat dilayani per bulan). Apakah kedua hasil berdekatan? Bila jauh berbeda, mana yang lebih dipercaya dan mengapa?

### Tantangan 2 — Mencoba Kompetitor

Daftar dan pakai sendiri dua kompetitor selama satu minggu untuk mengerjakan tugas yang sama. Catat: berapa lama belajar, apa yang menyulitkan, apa yang bagus. Ini memberi pemahaman yang tidak diperoleh dari membaca deskripsi.

### Tantangan 3 — Menguji Angka ke Narasumber

Sampaikan perhitungan tim kepada satu narasumber: *"kami memperkirakan sekitar 20% pedagang seperti Anda bersedia membayar Rp 50 ribu sebulan untuk ini. Menurut Anda?"* Catat reaksinya.

---

## Checklist Penyelesaian

- [ ] Spreadsheet dengan **sel asumsi terpisah** dan rumus
- [ ] **Setiap asumsi memiliki sumber dan tanggal akses**
- [ ] Definisi setiap sumber diperiksa relevansinya
- [ ] Asumsi dari wawancara sendiri ditandai khusus
- [ ] **Perhitungan bottom-up** — *top-down* hanya sebagai pembanding
- [ ] Analisis sensitivitas pada minimal 2 asumsi
- [ ] Hasil dilaporkan sebagai **rentang**, bukan angka tunggal
- [ ] Minimal 5 kompetitor: 2 langsung, 2 tidak langsung, 1 alternatif non-produk
- [ ] Tabel perbandingan dengan **baris bukti wawancara**
- [ ] Tabel "mengapa orang berhenti memakai kompetitor"
- [ ] Peta posisi dengan dimensi yang berasal dari kutipan
- [ ] AI Usage Log — **termasuk verifikasi angka yang diperoleh dari AI**

---

## Referensi

1. [Modul Minggu 5](../03-modules/week-05-ukuran-pasar-dan-kompetitor.md)
2. [Bab 5 buku ajar](../06-buku-ajar/bab-05-ukuran-pasar-dan-kompetitor.md)
3. [Panduan sumber data](../datasets/README.md)
4. Badan Pusat Statistik. <https://www.bps.go.id>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
