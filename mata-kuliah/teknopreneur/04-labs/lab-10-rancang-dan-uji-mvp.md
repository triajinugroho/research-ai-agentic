# Studio 10: Merancang dan Menguji MVP

| Aspek | Keterangan |
|-------|------------|
| Minggu | 10 · Sub-CPMK `UAI22-1` · Bagian dari P-03 (25%) |
| Durasi | 40' di kelas + pembangunan dan pengujian mandiri |
| Luaran | MVP + rancangan eksperimen + catatan pengujian ≥ 5 orang |

---

## Tujuan Studio

1. Menentukan asumsi paling berisiko yang hendak diuji.
2. Memilih jenis MVP paling murah yang masih dapat mengujinya.
3. Merancang eksperimen dengan ukuran keberhasilan yang ditetapkan lebih dahulu.
4. Menguji MVP kepada minimal 5 orang di luar tim dan mendokumentasikannya.

---

## Langkah-langkah

### LANGKAH 1: Menentukan Asumsi Paling Berisiko

| Asumsi | Bila keliru, seberapa fatal? | Seberapa yakin kita? | **Prioritas uji** |
|--------|------------------------------|---------------------|-------------------|
| Ada yang mengalami masalah ini | | | |
| Masalahnya cukup terasa | | | |
| Solusi kami menyelesaikannya | | | |
| Mereka bersedia memakainya | | | |
| **Mereka bersedia membayar** | | | |
| Kami dapat menjangkau mereka | | | |

> **Prioritas uji tertinggi:** asumsi yang **paling fatal bila keliru** dan **paling tidak diyakini**.

### LANGKAH 2: Memilih Jenis MVP

| Asumsi yang diuji | Jenis MVP termurah yang memadai |
|-------------------|--------------------------------|
| Ada yang tertarik | *Landing page* |
| Layanannya bernilai | *Concierge* (manual sepenuhnya) |
| Bersedia membayar | *Landing page* berbayar atau *concierge* berbayar |
| Memahami cara memakainya | Purwarupa yang dapat diklik |
| Memakainya berulang | *No-code* atau versi tunggal fitur |

**Pilihan tim:** ____________

**Mengapa bukan yang lebih sederhana?** [Jelaskan — bila tidak dapat dijelaskan, pilih yang lebih sederhana]

> **Kaidah:** membangun lebih dari yang diperlukan untuk menguji adalah pemborosan. Waktu adalah sumber daya paling langka.

### LANGKAH 3: Merancang Eksperimen

```markdown
## Rancangan Eksperimen

| Unsur | Isi |
|-------|-----|
| **Asumsi yang diuji** | [dinyatakan sebagai kalimat yang DAPAT SALAH] |
| **Hipotesis** | Bila [tindakan], maka [hasil] sebesar [angka] |
| **Cara mengukur** | [apa yang diamati, bagaimana] |
| **UKURAN KEBERHASILAN** | [angka — ditetapkan SEKARANG, sebelum eksperimen] |
| Peserta | [berapa orang, dari mana] |
| Durasi | [kapan mulai, kapan berakhir] |
| Yang TIDAK diuji | [batas eksperimen ini] |
```

**Uji "dapatkah gagal?":**

| Pertanyaan | Jawaban |
|-----------|---------|
| Hasil apa yang akan membuat kami menyimpulkan asumsi ini keliru? | |
| Apakah hasil itu **mungkin terjadi**? | |

> Bila tidak ada hasil yang akan membuat tim menyimpulkan asumsinya keliru, **rancangan itu harus diperbaiki**. Eksperimen yang tidak dapat gagal tidak mengajarkan apa pun.

### LANGKAH 4: Membangun MVP

| Ketentuan | Rincian |
|-----------|---------|
| Waktu | Maksimal 1 minggu |
| Bentuk | Bebas — yang penting **dapat diuji** |
| Kelengkapan | **Sesedikit mungkin** yang masih dapat menguji asumsi |
| Kejujuran | Bila dikerjakan manual, **tidak mengklaim otomatis** |

**Ketentuan etis untuk *concierge* dan *wizard of oz*:**

- [ ] Pengguna tahu ini tahap awal
- [ ] **Tidak mengklaim otomatisasi yang tidak ada**
- [ ] Data pengguna dijaga meski proses manual

> Menyembunyikan bahwa layanan dikerjakan manual sambil mengklaim sistem otomatis adalah **`tadlis`** — menyembunyikan keadaan sebenarnya dari pihak yang bertransaksi.

### LANGKAH 5: Menguji

| Ketentuan | Rincian |
|-----------|---------|
| Peserta | **Minimal 5 orang di luar tim**, sesuai persona |
| Siapa | Bukan teman yang ingin membantu |
| Cara | Beri tugas, lalu **amati tanpa membantu** |
| Larangan | **Jangan menjelaskan cara pakai lebih dahulu** |
| Bila macet | Tunggu 30 detik sebelum membantu; catat waktunya |

> **Kesalahan paling merusak:** menjelaskan cara memakainya lebih dahulu. Dalam pemakaian nyata tidak ada yang menjelaskan. Bila peserta tidak dapat mulai tanpa penjelasan, itu **temuan**, bukan hambatan pengujian.

### LANGKAH 6: Mendokumentasikan Pengujian

```markdown
## Pengujian MVP #NN

| Aspek | Isi |
|-------|-----|
| Tanggal | |
| Peserta | [inisial] — [peran], sesuai persona [1/2] |
| Durasi | |
| Tugas yang diminta | "[kalimat persis yang diucapkan]" |

### Yang Diamati (catat waktu)

| Waktu | Yang terjadi |
|-------|--------------|
| 0:00 | |
| | |

### Kutipan

1. "..."
2. "..."

### Hasil terhadap Ukuran Keberhasilan

Ukuran: [angka yang ditetapkan sebelumnya]
Hasil: **TERCAPAI / TIDAK TERCAPAI** — [angka nyata]

### Yang Dipelajari

[Termasuk yang tidak berjalan]

### Tindakan

[Apa yang akan diubah sebelum pengujian berikutnya]
```

> **Bagian "Hasil terhadap Ukuran Keberhasilan" wajib menyatakan tercapai atau tidak secara tegas.** Menuliskan "cukup baik" tanpa membandingkan dengan ukuran yang ditetapkan adalah cara menghindari kesimpulan.

### LANGKAH 7: Menyimpulkan

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa dari 5 peserta yang mencapai ukuran keberhasilan? | |
| Apakah hipotesis **didukung**? | ya / tidak / tidak dapat disimpulkan |
| Pola apa yang muncul pada kegagalan? | |
| Apa yang **paling mengejutkan**? | |
| **Tindakan:** lanjut / perbaiki dan uji ulang / ubah arah | |

**Bila hasilnya mengecewakan**, periksa reaksi tim:

| Reaksi yang keliru | Reaksi yang tepat |
|--------------------|-------------------|
| "Mereka belum paham nilainya" | "Apa yang membuat mereka tidak melanjutkan?" |
| "Kita perlu lebih banyak fitur" | "Apakah asumsi dasarnya yang keliru?" |
| "Pesertanya tidak sesuai" | "Apakah persona kita perlu dipertajam?" |
| "Nanti kalau sudah rapi pasti dipakai" | "Apa bukti bahwa kerapian yang menjadi hambatan?" |

---

## Tantangan Tambahan

### Tantangan 1 — Dua MVP Berbeda

Bangun dua versi MVP yang sangat berbeda (misalnya *concierge* dan *no-code*) untuk menguji asumsi yang sama. Bandingkan: mana yang memberi pembelajaran lebih dalam? Mana yang lebih murah?

### Tantangan 2 — Merekam Pengujian

Dengan izin, rekam layar satu sesi pengujian. Tonton ulang bersama tim. Berapa banyak yang terlewat saat pengamatan langsung?

### Tantangan 3 — Menguji ke Orang yang Sama Sekali Asing

Lima peserta pertama biasanya masih dari jaringan tim. Uji kepada **satu orang yang sama sekali tidak dikenal** dari segmen yang sama. Apakah hasilnya berbeda?

---

## Checklist Penyelesaian

- [ ] Asumsi paling berisiko ditentukan dengan tabel prioritas
- [ ] Jenis MVP dipilih sebagai **yang termurah yang masih memadai**
- [ ] Rancangan eksperimen lengkap dengan **ukuran keberhasilan ditetapkan lebih dahulu**
- [ ] Uji "dapatkah gagal?" dijalankan dan lolos
- [ ] MVP dibangun dalam maksimal 1 minggu
- [ ] Ketentuan etis dipenuhi (tidak mengklaim otomatisasi yang tidak ada)
- [ ] **Diuji kepada minimal 5 orang di luar tim**
- [ ] **Tidak menjelaskan cara pakai lebih dahulu**
- [ ] Setiap pengujian didokumentasikan dengan catatan waktu
- [ ] Setiap catatan menyatakan **tercapai/tidak** secara tegas
- [ ] Kesimpulan dan tindakan dinyatakan
- [ ] AI Usage Log disertakan

---

## Referensi

1. [Modul Minggu 10](../03-modules/week-10-mvp-merancang-yang-paling-sedikit.md)
2. [Bab 9 buku ajar](../06-buku-ajar/bab-09-mvp-merancang-yang-paling-sedikit.md)
3. Ries, E. (2011). *The Lean Startup*. Crown Business.
4. Krug, S. (2009). *Rocket Surgery Made Easy*. New Riders.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
