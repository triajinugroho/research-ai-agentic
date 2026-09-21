# Studio 07: Model *Unit Economics*

| Aspek | Keterangan |
|-------|------------|
| Minggu | 7 · Sub-CPMK `UAI21-1` · Bobot 6,25% (Observasi) |
| Durasi | 45' di kelas + 90' mandiri |
| Luaran | Spreadsheet model + daftar risiko + **Milestone 2 (P-02)** |

---

## Tujuan Studio

1. Membangun model *unit economics* dengan sel asumsi terpisah.
2. Menghitung CAC, LTV, margin kotor, dan *payback period*.
3. Melakukan analisis sensitivitas pada asumsi utama.
4. Menyusun daftar risiko dengan tanda awal dan mitigasi.

---

## Langkah-langkah

### LANGKAH 1: Menyusun Spreadsheet

```
 A                                B         C
 1  ASUMSI                        NILAI     SUMBER / DASAR
 2  Harga bulanan                 50.000    Rencana; W03 W07 menyebut ≤50rb
 3  Rata-rata lama berlangganan   8 bulan   ASUMSI - belum terukur
 4  Biaya server/pengguna/bulan   2.000     Halaman harga penyedia
 5  Biaya API/pengguna/bulan      0         -
 6  Biaya dukungan/pengguna/bulan 8.000     10 menit x nilai waktu
 7  Biaya transaksi               2%        Penyedia pembayaran
 8  Waktu tim untuk akuisisi      3 jam     Perkiraan dari uji coba
 9  Nilai waktu per jam           50.000    Standar tim
10  Biaya promosi/pengguna        25.000    Perkiraan
11
12  PERHITUNGAN                   HASIL     RUMUS
13  Biaya langsung/pengguna/bln   =B4+B5+B6+(B2*B7)
14  Margin kotor (Rp)             =B2-B13
15  Margin kotor (%)              =B14/B2
16  CAC                           =(B8*B9)+B10
17  LTV                           =B14*B3
18  LTV/CAC                       =B17/B16
19  Payback (bulan)               =B16/B14
20  Titik impas (pengguna)        =biaya tetap bulanan/B14
```

**Ketentuan:**

- [ ] Setiap asumsi pada baris terpisah dengan dasarnya
- [ ] Asumsi yang **belum terukur ditandai** (seperti baris 3)
- [ ] Perhitungan memakai rumus
- [ ] **Waktu tim dihitung sebagai biaya** (baris 8–9)

> **CAC yang tidak menghitung waktu tim adalah CAC yang terlalu rendah.** Pada tahap awal, waktu tim biasanya komponen terbesar — dan ia nyata, meski tidak dibayarkan.

### LANGKAH 2: Membaca Hasil

| Besaran | Hasil tim | Patokan | Tafsir |
|---------|-----------|---------|--------|
| Margin kotor | | 70–85% untuk perangkat lunak | |
| LTV/CAC | | 3 (kebiasaan industri) | |
| *Payback* | | < 12 bulan | |
| Titik impas | | — | |

**Kaidah membaca:**

| LTV/CAC | Tafsir |
|---------|--------|
| < 1 | **Setiap pelanggan baru menambah kerugian** |
| 1–2 | Marginal; tidak ada ruang untuk kesalahan |
| ≈ 3 | Sehat |
| > 5 | Mungkin kurang berinvestasi pada pertumbuhan |

> **Peringatan:** LTV bergantung pada lama berlangganan, yang pada usaha berumur beberapa minggu **belum dapat diketahui**. Angka LTV pada tahap ini adalah dugaan — dan wajib dinyatakan demikian.

### LANGKAH 3: Analisis Sensitivitas (WAJIB)

| Asumsi | Dasar | −50% | +50% | LTV/CAC pesimis | LTV/CAC optimis |
|--------|-------|------|------|-----------------|-----------------|
| Lama berlangganan | | | | | |
| Margin kotor | | | | | |
| CAC | | | | | |

**Yang dilaporkan:**

| Pertanyaan | Jawaban |
|-----------|---------|
| Asumsi mana yang paling menentukan? | |
| Pada nilai berapa LTV/CAC turun di bawah 1? | |
| Asumsi mana yang paling tidak pasti? | |
| Bagaimana asumsi itu akan diuji? | |

> Baris terakhir mengubah kelemahan menjadi **rencana pengujian** — dan itulah yang membedakan analisis tahap awal yang baik.

### LANGKAH 4: Menguji Harga dari Bukti Wawancara

| Pertanyaan yang sudah ditanyakan | Jawaban dari wawancara | Implikasi harga |
|----------------------------------|------------------------|-----------------|
| "Berapa waktu yang habis untuk ini?" | | Nilai waktu yang dihemat |
| "Berapa kerugian yang timbul?" | | Nilai masalah |
| **"Berapa yang sudah Anda keluarkan untuk mengatasinya?"** | | **Kesediaan membayar terbukti** |

Baris ketiga adalah yang paling bernilai: ia menanyakan **apa yang sudah benar-benar dibayarkan**, bukan apa yang akan dibayarkan.

**Periksa kekeliruan khas:**

- [ ] Harga tidak ditetapkan terlalu rendah "agar cepat banyak pengguna"
- [ ] Bila ada versi gratis, ada rencana pendapatan yang jelas
- [ ] Harga tidak sekadar menyamai kompetitor tanpa alasan
- [ ] Ada rencana **menguji harga**, bukan hanya mengasumsikannya

### LANGKAH 5: Daftar Risiko

Minimal **8 risiko**, mencakup sekurang-kurangnya lima kategori:

| ID | Kategori | Risiko | Kemungkinan | Dampak | **Tanda awal** | Mitigasi |
|----|----------|--------|-------------|--------|----------------|----------|
| R-01 | Pasar | | T/S/R | T/S/R | | |
| R-02 | Teknis | | | | | |
| R-03 | Operasional | | | | | |
| R-04 | Finansial | | | | | |
| R-05 | Kompetitif | | | | | |
| R-06 | Regulasi | | | | | |
| R-07 | Tim | | | | | |
| R-08 | Ketergantungan | | | | | |

**Kolom "tanda awal" wajib diisi.** Ia menjawab: *"bagaimana kita tahu risiko ini mulai terjadi, sebelum terlambat?"*

| Risiko | Tanda awal yang lemah | Tanda awal yang kuat |
|--------|----------------------|---------------------|
| Pengguna berhenti | "Pengguna berkurang" | "Pemakaian minggu ke-6 turun > 30% dibanding minggu ke-2" |
| Biaya API naik | "Biaya naik" | "Pengumuman perubahan harga dari penyedia" |
| Konflik tim | "Tim tidak akur" | "Dua tenggat berturut-turut terlewat oleh peran yang sama" |

### LANGKAH 6: Menyusun Milestone 2

```markdown
# Milestone 2 — Bukti Kelayakan

## 1. Ringkasan

| Aspek | Angka |
|-------|-------|
| Total wawancara sampai titik ini | (minimal 12) |
| SOM tahun kedua (rentang) | |
| Margin kotor | |
| LTV/CAC | |
| Beban operasional per 100 pengguna | ... jam/bulan |

## 2. Temuan Kelayakan

| Aspek | Temuan | Sumber |
|-------|--------|--------|
| Pasar | | S-05 |
| Kompetitor | | S-05 |
| Teknologi | | S-06 |
| Operasional | | S-06 |
| Finansial | | S-07 |

## 3. Tiga Risiko Terbesar

| Risiko | Mengapa terbesar | Tanda awal | Mitigasi |
|--------|------------------|------------|----------|
|        |                  |            |          |

## 4. Asumsi yang Paling Tidak Pasti

| Asumsi | Mengapa tidak pasti | Bagaimana akan diuji | Kapan |
|--------|---------------------|---------------------|-------|
|        |                     |                     |       |

## 5. KESIMPULAN KELAYAKAN

- [ ] **LANJUT** — karena [alasan berbasis angka]
- [ ] **UBAH ARAH** — [apa yang diubah] karena [angka]
- [ ] **HENTIKAN** — karena [angka yang menunjukkan ketidaklayakan]

## 6. Lampiran

Seluruh berkas S-05, S-06, S-07 + catatan wawancara + AI Usage Log
```

---

## Tantangan Tambahan

### Tantangan 1 — Model dengan Tiga Skenario

Buat tiga kolom skenario (pesimis, tengah, optimis) yang seluruhnya bergerak bersama. Pada skenario pesimis, apakah usaha masih layak? Berapa lama modal bertahan?

### Tantangan 2 — Menguji Harga Sungguhan

Buat *landing page* sederhana dengan harga yang direncanakan dan tombol "berlangganan". Tunjukkan kepada 10 orang dari segmen. Berapa yang menekan tombol? Ini data yang jauh lebih berharga daripada jawaban hipotetis.

### Tantangan 3 — Menghitung Titik Impas Tim

Berapa pengguna dibutuhkan agar pendapatan menutupi nilai waktu seluruh anggota tim (misalnya 20 jam/minggu per orang)? Berapa lama untuk mencapainya menurut rencana *go-to-market*?

---

## Checklist Penyelesaian

- [ ] Spreadsheet dengan **sel asumsi terpisah** dan rumus
- [ ] **Waktu tim dihitung** sebagai komponen CAC
- [ ] Biaya dukungan per pengguna dimasukkan ke margin kotor
- [ ] Asumsi yang belum terukur **ditandai**
- [ ] **Analisis sensitivitas pada minimal 3 asumsi**
- [ ] Dinyatakan pada nilai berapa LTV/CAC turun di bawah 1
- [ ] Harga ditelusuri ke bukti wawancara
- [ ] Ada **rencana menguji harga**
- [ ] **Minimal 8 risiko** dengan **tanda awal** yang konkret
- [ ] **Minimal 12 wawancara** terdokumentasi
- [ ] Milestone 2 lengkap dengan **kesimpulan kelayakan**
- [ ] AI Usage Log disertakan

---

## Referensi

1. [Modul Minggu 7](../03-modules/week-07-unit-economics-harga-risiko.md)
2. [Bab 7 buku ajar](../06-buku-ajar/bab-07-unit-economics-harga-risiko.md)
3. Croll, A., & Yoskovitz, B. (2013). *Lean Analytics*. O'Reilly.
4. Skok, D. *SaaS Metrics 2.0*. <https://www.forentrepreneurs.com/saas-metrics-2/>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
