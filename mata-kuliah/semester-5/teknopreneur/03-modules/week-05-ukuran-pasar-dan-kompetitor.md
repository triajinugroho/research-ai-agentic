# Minggu 5: Ukuran Pasar dan Analisis Kompetitor

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Teknopreneur (`ST52510002`) |
| Minggu | 5 dari 16 |
| Topik | TAM-SAM-SOM; perhitungan *bottom-up*; peta kompetitor |
| Sub-CPMK | `TEKNO-Sub-CPMKUAI21-1` |
| Bloom | C4 → C5 |
| Durasi | 150 menit |
| Metode | Kuliah · Studio perhitungan |
| Penilaian | Observasi (Studio 5) |

---

## Tujuan Pembelajaran

1. **Menghitung** (C3) ukuran pasar secara *bottom-up* dengan asumsi yang dinyatakan.
2. **Membedakan** (C4) perhitungan *top-down* dan *bottom-up* beserta kelemahannya.
3. **Memetakan** (C4) kompetitor langsung dan **tidak langsung**.
4. **Mengevaluasi** (C5) posisi usaha terhadap alternatif yang ada.

---

## Materi Pembelajaran

### 5.1 TAM, SAM, SOM

```
  ┌───────────────────────────────────────────────┐
  │  TAM — Total Addressable Market               │
  │  Seluruh orang yang punya masalah ini         │
  │  ┌─────────────────────────────────────────┐  │
  │  │  SAM — Serviceable Available Market     │  │
  │  │  Yang dapat dijangkau model bisnis kita │  │
  │  │  ┌───────────────────────────────────┐  │  │
  │  │  │  SOM — Serviceable Obtainable     │  │  │
  │  │  │  Yang realistis diraih 1–3 tahun  │  │  │
  │  │  └───────────────────────────────────┘  │  │
  │  └─────────────────────────────────────────┘  │
  └───────────────────────────────────────────────┘
```

| Lapis | Pertanyaan | Contoh |
|-------|-----------|--------|
| **TAM** | Berapa banyak yang punya masalah ini? | Seluruh UMKM kuliner Indonesia |
| **SAM** | Berapa yang dapat kita layani? | Yang di Jabodetabek, punya ponsel pintar, omzet > Rp 10 juta/bulan |
| **SOM** | Berapa yang realistis diraih? | 0,5% dari SAM dalam 2 tahun, berdasarkan kapasitas tim |

> **SOM adalah angka yang paling penting dan paling sering dilebih-lebihkan.** Ia harus berasal dari kapasitas nyata tim (berapa pelanggan dapat dilayani, berapa cepat dapat menjangkau), bukan dari persentase sembarang terhadap SAM.

---

### 5.2 *Top-Down* vs *Bottom-Up*

#### 5.2.1 Perbandingan

| Aspek | *Top-down* | *Bottom-up* |
|-------|-----------|-------------|
| Cara | Mulai dari angka industri, kalikan persentase | Mulai dari satuan terkecil, kalikan ke atas |
| Contoh | "Pasar SaaS Indonesia USD 2 miliar × 1% = USD 20 juta" | "64 juta UMKM × 12% kuliner × 30% pakai ponsel × 20% bersedia bayar × Rp 600rb/tahun" |
| Kelemahan | **Persentase 1% itu dari mana?** Biasanya karangan | Butuh banyak asumsi, tetapi tiap asumsi dapat diperiksa |
| Kegunaan | Memberi gambaran besar | **Dapat dipertanggungjawabkan** |

> **Ketentuan mata kuliah ini:** perhitungan **bottom-up wajib**. *Top-down* boleh disertakan sebagai pembanding, tetapi tidak diterima sendirian.

Alasannya: perhitungan *top-down* memindahkan seluruh beban pada satu angka persentase yang hampir selalu tidak berdasar. Perhitungan *bottom-up* memaksa setiap asumsi dinyatakan — dan dengan demikian dapat diperiksa dan diperdebatkan.

#### 5.2.2 Anatomi Perhitungan *Bottom-Up*

```
  Populasi dasar                     64.200.000 UMKM
      × Proporsi segmen (kuliner)    × 12%        [sumber: KemenkopUKM]
      = Segmen                       = 7.704.000
      × Punya ponsel pintar untuk
        usaha                        × 30%        [sumber: survei BPS]
      = Dapat dijangkau              = 2.311.200
      × Berada di wilayah operasi    × 4%         [Jabodetabek]
      = SAM (jumlah)                 = 92.448
      × Bersedia membayar            × 20%        [DARI 15 WAWANCARA: 3/15]
      = Pasar potensial              = 18.490
      × Harga tahunan                × Rp 600.000
      = SAM (nilai)                  = Rp 11,09 miliar/tahun
      × Pangsa realistis 2 tahun     × 3%         [kapasitas tim]
      = SOM                          = Rp 333 juta/tahun
```

**Setiap baris memiliki sumber.** Baris yang paling berharga adalah yang bertanda "DARI WAWANCARA" — karena itulah satu-satunya angka yang berasal dari data primer tim sendiri.

#### 5.2.3 Kejujuran dalam Asumsi

| Praktik yang tidak jujur | Perbaikan |
|--------------------------|-----------|
| Memilih persentase yang membuat angka besar | Nyatakan rentang: pesimis, tengah, optimis |
| Menyembunyikan sumber | Tautan dan tanggal akses untuk tiap angka |
| Memakai angka tanpa memeriksa relevansinya | Pastikan definisinya sesuai (UMKM menurut siapa?) |
| Mengutip angka dari AI tanpa verifikasi | **Telusuri ke sumber primer** |

> **Peringatan khusus tentang AI:** model bahasa sangat mahir menghasilkan angka pasar yang terdengar meyakinkan — lengkap dengan CAGR dan nama lembaga riset — tanpa sumber yang dapat ditelusuri. Angka semacam itu **wajib diverifikasi**. Yang tidak dapat ditelusuri ke terbitan aslinya dianggap tidak ada.

---

### 5.3 Analisis Kompetitor

#### 5.3.1 Tiga Lapis Kompetitor

| Lapis | Definisi | Contoh (pencatatan usaha mikro) |
|-------|----------|--------------------------------|
| **Langsung** | Produk sejenis untuk segmen sama | Aplikasi kasir UMKM lain |
| **Tidak langsung** | Produk berbeda, pekerjaan sama | Spreadsheet, aplikasi catatan umum |
| **Alternatif non-produk** | Cara lain menyelesaikan pekerjaan | **Buku tulis, ingatan, bantuan anak** |

> Lapis ketiga adalah **kompetitor terbesar bagi hampir semua usaha tahap awal**, dan yang paling sering dilupakan.

Buku tulis memiliki keunggulan yang sulit dikalahkan: gratis, tidak perlu dipelajari, tidak pernah kehabisan baterai, tidak bergantung sinyal, dan sudah menjadi kebiasaan. Produk yang ingin menggantikannya harus **jauh lebih baik**, bukan sedikit lebih baik — karena biaya berpindah kebiasaan itu nyata.

#### 5.3.2 Peta Posisi

```
         Mudah dipakai
              ▲
              │        ● Buku tulis
              │
   Murah ─────┼──────────────────► Mahal
              │  ◆ (posisi kita?)
              │              ● Aplikasi kasir
              │                besar
         Sulit dipakai
```

Peta dua sumbu memaksa tim memilih **dua dimensi yang paling menentukan keputusan pelanggan** — dan dimensi itu harus berasal dari wawancara, bukan dari dugaan.

#### 5.3.3 Tabel Perbandingan

| Aspek | Kompetitor A | Kompetitor B | Buku tulis | Kita |
|-------|--------------|--------------|------------|------|
| Harga | Rp 99rb/bln | Gratis + iklan | Rp 5rb | ? |
| Waktu belajar | 2 jam | 30 menit | 0 | ? |
| Butuh sinyal | Ya | Ya | Tidak | ? |
| Waktu per transaksi | 15 detik | 20 detik | **3 detik** | ? |
| Bukti dari wawancara | W07: "ribet" | — | W03, W05, W09 | — |

Kolom terakhir dikosongkan pada Minggu 5 dan diisi pada Minggu 9–10. Baris terakhir adalah yang membedakan analisis ini dari salinan materi pemasaran.

#### 5.3.4 Mengapa Orang Tidak Memakai Kompetitor

Pertanyaan ini lebih berguna daripada daftar fitur:

| Pertanyaan | Yang diungkapnya |
|-----------|------------------|
| Berapa banyak dari narasumber yang pernah mencoba kompetitor? | Seberapa dikenal alternatifnya |
| Yang mencoba lalu berhenti — mengapa? | **Titik kegagalan yang dapat diserang** |
| Yang tidak pernah mencoba — mengapa? | Hambatan masuk |
| Yang masih memakainya — apa yang mereka sukai? | **Apa yang tidak boleh kita rusak** |

Baris kedua adalah tambang informasi. Dalam contoh Minggu 2, narasumber berkata: *"Pernah beli aplikasi kasir, tapi ribet. Dipakai dua minggu, terus balik ke buku lagi."* Kalimat itu menunjukkan bahwa kesadaran bukan masalah — kemudahan pakai yang menjadi masalah.

---

### 5.4 Kesalahan Khas Analisis Pasar

| # | Kesalahan | Mengapa merusak |
|---|-----------|-----------------|
| 1 | Hanya *top-down* | Tidak dapat diperiksa |
| 2 | Mengabaikan kompetitor tidak langsung | Kompetitor terbesar justru terlewat |
| 3 | "Tidak ada kompetitor" | Hampir selalu berarti belum mencari, atau tidak ada pasar |
| 4 | Angka tanpa sumber | Tidak dapat dipertanggungjawabkan |
| 5 | SOM sebagai persentase sembarang dari SAM | Tidak berdasar kapasitas nyata |
| 6 | Definisi populasi dasar tidak diperiksa | "UMKM" menurut siapa? Definisi berbeda antarlembaga |
| 7 | Tidak memakai data wawancara sendiri | Membuang satu-satunya data primer yang dimiliki |

> **Tentang nomor 3:** pernyataan "tidak ada kompetitor" hampir selalu keliru. Bila benar-benar tidak ada yang menyelesaikan pekerjaan ini, kemungkinan besar **pekerjaan ini tidak cukup penting** bagi orang untuk membayar penyelesaiannya. Ketiadaan kompetitor adalah tanda bahaya, bukan peluang.

---

### 5.5 Menyatakan Ketidakpastian

Angka pasar selalu mengandung ketidakpastian. Menyembunyikannya membuat analisis tampak lebih meyakinkan dan lebih rapuh.

Cara menyatakannya:

| Cara | Contoh |
|------|--------|
| **Rentang** | "SOM tahun kedua: Rp 200–450 juta, bergantung tingkat konversi" |
| **Analisis sensitivitas** | "Bila kesediaan membayar 10% (bukan 20%), SOM menjadi Rp 167 juta" |
| **Asumsi yang paling rapuh** | "Angka paling tidak pasti: proporsi yang bersedia membayar (n=15)" |
| **Cara memverifikasinya** | "Akan diuji dengan *landing page* berbayar pada Minggu 10" |

Baris terakhir mengubah asumsi dari kelemahan menjadi **rencana pengujian** — dan itulah yang membedakan analisis tahap awal yang baik.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 5 buku ajar](../06-buku-ajar/bab-05-ukuran-pasar-dan-kompetitor.md).
- Mengumpulkan minimal tiga sumber data pasar untuk ranah tim.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Pembahasan P-01; tim yang mengubah arah menjelaskan |
| Konsep | 30' | TAM-SAM-SOM; *bottom-up* vs *top-down* |
| **Studio** | 45' | **Kegiatan inti:** menyusun perhitungan *bottom-up* di spreadsheet |
| Konsep | 25' | Tiga lapis kompetitor; peta posisi |
| Studio | 30' | Peta kompetitor; tabel perbandingan |
| Penutup | 10' | Penugasan |

**Kegiatan inti — perhitungan di depan kelas:** satu tim mengerjakan perhitungannya di papan/layar sementara kelas menantang setiap asumsi: *"angka 30% itu dari mana? Definisi UMKM yang dipakai apa? Apakah sumbernya masih berlaku tahun ini?"*

Latihan ini hampir selalu menurunkan angka yang semula dihitung tim — dan itulah pelajarannya.

### Setelah Kelas (120 menit)

- Menyelesaikan [Studio 5](../04-labs/lab-05-perhitungan-pasar-dan-peta-kompetitor.md).
- Melanjutkan wawancara menuju target 12 sebelum Minggu 7.

---

## Penugasan

**S-05 — Perhitungan Pasar dan Peta Kompetitor**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Spreadsheet perhitungan + peta kompetitor + tabel perbandingan |
| Kriteria khusus | **Perhitungan *bottom-up* wajib**; setiap baris bersumber |
| Kompetitor | Minimal 5, **termasuk tidak langsung dan alternatif non-produk** |
| Ketidakpastian | Rentang dan analisis sensitivitas pada 2 asumsi utama |
| Tenggat | Awal pertemuan Minggu 6 |
| Bobot | 6,25% (Observasi) |
| Yang menggugurkan | Angka tanpa sumber; hanya *top-down*; "tidak ada kompetitor" |

---

## Rangkuman

1. **TAM-SAM-SOM**; SOM adalah yang paling penting dan paling sering dilebih-lebihkan.
2. **SOM harus berasal dari kapasitas nyata tim**, bukan persentase sembarang dari SAM.
3. **Perhitungan *bottom-up* wajib**; *top-down* tidak diterima sendirian.
4. Setiap baris perhitungan **memiliki sumber**; yang berasal dari wawancara sendiri paling berharga.
5. **Angka pasar dari AI wajib diverifikasi ke sumber primer.**
6. Tiga lapis kompetitor; **alternatif non-produk** (buku tulis, ingatan) adalah yang terbesar.
7. **"Tidak ada kompetitor" hampir selalu berarti belum mencari — atau tidak ada pasar.**
8. Pertanyaan paling berguna: **mengapa orang yang mencoba kompetitor lalu berhenti?**
9. Ketidakpastian dinyatakan sebagai **rentang, sensitivitas, dan rencana pengujian**.
10. Definisi populasi dasar wajib diperiksa — "UMKM" berbeda definisinya antarlembaga.

---

## Referensi

1. Blank, S., & Dorf, B. (2020). *The Startup Owner's Manual*, Bab 5. Wiley.
2. Croll, A., & Yoskovitz, B. (2013). *Lean Analytics*, Bab 4. O'Reilly.
3. Badan Pusat Statistik. *Statistik E-Commerce Indonesia* dan *Profil UMK*. <https://www.bps.go.id>
4. Kementerian Koperasi dan UKM RI. *Data UMKM*.
5. Google, Temasek, & Bain (terbitan terbaru). *e-Conomy SEA Report*.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
