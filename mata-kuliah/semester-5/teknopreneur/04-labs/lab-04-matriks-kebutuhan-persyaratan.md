# Studio 04: Matriks Kebutuhan → Persyaratan

| Aspek | Keterangan |
|-------|------------|
| Minggu | 4 · Sub-CPMK `091-1` · Bobot 3,4% (Observasi) |
| Durasi | 45' di kelas + 60' mandiri |
| Luaran | Matriks keterlacakan + berkas **Milestone 1 (P-01)** |

---

## Tujuan Studio

1. Membedakan kebutuhan, keinginan, dan solusi pada data wawancara sendiri.
2. Menyusun matriks yang setiap persyaratannya terlacak ke kutipan.
3. Memprioritaskan persyaratan berdasarkan bukti dan kendala.
4. Menyusun Milestone 1 lengkap dengan pernyataan arah.

---

## Langkah-langkah

### LANGKAH 1: Memilah Kutipan

Dari seluruh kutipan, pilah ke dalam tiga kolom:

| Kutipan | Jenis | Kebutuhan di baliknya |
|---------|-------|----------------------|
| "Mau ada notifikasinya" | **Keinginan** | Tidak ingin lupa pada saat yang tepat |
| "Nggak sempat nulis kalau ramai" | **Kebutuhan** | (sudah berupa kebutuhan) |
| "Pakai aplikasi kasir aja" | **Solusi** | — (perlu digali kebutuhannya) |

**Cara menerjemahkan keinginan menjadi kebutuhan:**

Tanyakan "kenapa" pada keinginan itu, sampai sampai pada keadaan yang ingin dicapai — bukan cara mencapainya.

```
  "Mau ada notifikasi"
      └─ Kenapa?
         "Biar nggak lupa"
             └─ Lupa apa?
                "Lupa catat kalau sudah selesai ramai"
                    └─ KEBUTUHAN: tidak kehilangan data penjualan
                       karena lupa mencatat setelah jam ramai
```

> Perhatikan: kebutuhan itu dapat dipenuhi dengan notifikasi **atau** dengan cara lain — misalnya pencatatan yang tidak perlu diingat sama sekali. Menerjemahkan keinginan membuka kemungkinan yang lebih baik.

### LANGKAH 2: Mengumpulkan *Constraint*

| Jenis | *Constraint* | Bukti | Keras / Lunak |
|-------|--------------|-------|---------------|
| Waktu | | | |
| Biaya | | | |
| Perangkat | | | |
| Keterampilan | | | |
| Fisik | | | |
| Sosial | | | |
| Regulasi | | | |

**Membedakan keras dan lunak:**

| Pertanyaan penguji | Bila jawabannya... |
|--------------------|--------------------|
| "Kapan terakhir kali itu benar-benar terjadi?" | Tidak pernah → kemungkinan lunak |
| "Apa yang terjadi bila dilanggar?" | Tidak dapat dipakai sama sekali → keras |
| "Berapa narasumber yang menyebutkannya?" | Banyak → lebih mungkin keras |

### LANGKAH 3: Menyusun Matriks

| ID | Kebutuhan | Bukti | *Constraint* terkait | Persyaratan produk | Prioritas |
|----|-----------|-------|---------------------|--------------------|-----------|
| K-01 | | | | | |
| K-02 | | | | | |

**Aturan penyusunan:**

| Aturan | Cara memeriksa |
|--------|----------------|
| Setiap kebutuhan memiliki ≥ 1 bukti | Kolom "Bukti" tidak kosong |
| Kebutuhan dari 1 narasumber ditandai | Beri tanda `*` |
| **Setiap persyaratan berasal dari kebutuhan** | Tidak ada baris persyaratan tanpa induk |
| Setiap *constraint* memiliki bukti | Dari tabel Langkah 2 |
| Persyaratan **dapat diperiksa** | Dinyatakan dengan angka bila mungkin |

**Contoh persyaratan yang dapat diperiksa:**

| Lemah | Kuat |
|-------|------|
| "Harus mudah dipakai" | "Pencatatan satu transaksi selesai dalam ≤ 5 detik" |
| "Harus cepat" | "Halaman utama terbuka < 2 detik pada koneksi 3G" |
| "Harus murah" | "Biaya bagi pengguna ≤ Rp 50.000/bulan" |

### LANGKAH 4: Prioritisasi

| ID | Frekuensi (/15) | Intensitas | Biaya masalah | Sudah diupayakan | Kesulitan bangun | **MoSCoW** |
|----|-----------------|------------|---------------|------------------|------------------|------------|
| K-01 | | | | | | |

**Kaidah:**

| MoSCoW | Kriteria |
|--------|----------|
| **Must** | Melanggar *constraint* keras bila tidak ada |
| **Should** | Disebut oleh ≥ setengah narasumber |
| **Could** | Disebut sedikit, kesulitan rendah |
| **Won't (kali ini)** | Sengaja ditunda — **wajib dicatat alasannya** |

> Kategori keempat menutup perdebatan yang, bila tidak dicatat, akan muncul kembali setiap minggu.

### LANGKAH 5: Audit Silang (di kelas, 40 menit)

Tukar matriks dengan tim lain. Cari:

| # | Yang dicari | Temuan |
|---|-------------|--------|
| 1 | Persyaratan **tanpa induk kebutuhan** | |
| 2 | Kebutuhan **tanpa bukti** | |
| 3 | *Constraint* yang **tampak karangan** | |
| 4 | **Keinginan yang dicatat sebagai kebutuhan** | |
| 5 | Persyaratan yang **tidak dapat diperiksa** | |

Sampaikan temuan kepada tim asal. Bagian ini sering tidak nyaman dan selalu berguna.

### LANGKAH 6: Menyusun Milestone 1

```markdown
# Milestone 1 — Bukti Masalah

## 1. Ringkasan Wawancara

| Aspek | Angka |
|-------|-------|
| Jumlah wawancara | (minimal 8) |
| Narasumber yang menolak/tidak relevan | |
| Rentang tanggal | |
| Rujukan yang diperoleh | |

## 2. Temuan Utama

| Tema | Jumlah narasumber | Kutipan penanda |
|------|-------------------|-----------------|
|      |                   |                 |

## 3. Apa yang Ternyata Berbeda dari Dugaan Awal

[Satu halaman. WAJIB. Bandingkan dugaan Minggu 1 dengan temuan.]

| Dugaan Minggu 1 | Temuan | Bukti |
|-----------------|--------|-------|
|                 |        |       |

## 4. Pernyataan Arah

Pilih salah satu dan jelaskan:

- [ ] **Melanjutkan ranah yang sama** — karena [alasan berbasis bukti]
- [ ] **Mempersempit segmen** menjadi [segmen] — karena [bukti]
- [ ] **Mengubah fokus masalah** dari [A] ke [B] — karena [bukti]
- [ ] **Mengganti ranah** — karena [bukti bahwa masalahnya tidak cukup terasa]

## 5. Lampiran

- Seluruh catatan wawancara
- Persona dan JTBD
- Peta perjalanan
- Matriks kebutuhan → persyaratan
- AI Usage Log
```

> **Bagian 3 dan 4 adalah yang paling dinilai.** Tim yang menyatakan "dugaan kami sepenuhnya benar" akan diminta menelusuri ulang: biasanya pertanyaannya yang memimpin, atau buktinya tidak benar-benar dibaca.

---

## Tantangan Tambahan

### Tantangan 1 — Persyaratan yang Dibuang

Susun daftar persyaratan yang **sempat terpikir tetapi dibuang** karena tidak berasal dari kebutuhan mana pun. Berapa banyak? Dari mana asalnya — dugaan tim, atau ketertarikan teknis?

### Tantangan 2 — Menguji *Constraint*

Ambil satu *constraint* yang tim tandai sebagai "keras". Uji ke dua narasumber: *"kalau [constraint] dilanggar sedikit, apakah masih bisa dipakai?"* Apakah ia benar-benar keras?

### Tantangan 3 — Persyaratan Berangka

Ubah seluruh persyaratan menjadi bentuk yang dapat diperiksa dengan angka. Yang tidak dapat diangkakan — bagaimana cara memeriksanya?

---

## Checklist Penyelesaian

- [ ] Kutipan dipilah menjadi kebutuhan / keinginan / solusi
- [ ] Keinginan diterjemahkan menjadi kebutuhan dengan "kenapa" berlapis
- [ ] *Constraint* dikumpulkan dengan bukti dan dipilah keras/lunak
- [ ] Matriks memiliki **keterlacakan penuh**
- [ ] **Tidak ada persyaratan tanpa induk kebutuhan**
- [ ] Persyaratan dinyatakan dalam bentuk yang **dapat diperiksa**
- [ ] Prioritisasi MoSCoW dengan alasan
- [ ] Audit silang dilakukan dan temuannya ditindaklanjuti
- [ ] **Minimal 8 wawancara** terdokumentasi
- [ ] Milestone 1 lengkap, termasuk **bagian "apa yang berbeda"** dan **pernyataan arah**
- [ ] AI Usage Log disertakan

---

## Referensi

1. [Modul Minggu 4](../03-modules/week-04-dari-kebutuhan-ke-persyaratan.md)
2. [Bab 4 buku ajar](../06-buku-ajar/bab-04-dari-kebutuhan-ke-persyaratan.md)
3. Wiegers, K., & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
