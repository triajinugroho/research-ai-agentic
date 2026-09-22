# Minggu 4: Dari Kebutuhan ke Persyaratan Produk

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Teknopreneur (`ST52510002`) |
| Minggu | 4 dari 16 |
| Topik | Kebutuhan vs keinginan vs solusi; *constraint*; keterlacakan; prioritisasi |
| Sub-CPMK | `TEKNO-Sub-CPMK091-1` |
| Bloom | C4 (Menganalisis) |
| Durasi | 150 menit |
| Metode | Kuliah · Studio · Presentasi silang |
| Penilaian | Observasi (Studio 4) · **Milestone 1 (P-01)** |

---

## Tujuan Pembelajaran

1. **Membedakan** (C4) kebutuhan, keinginan, dan solusi.
2. **Memetakan** (C4) kebutuhan dan *constraint* menjadi persyaratan produk.
3. **Menyusun** (C4) matriks keterlacakan dari kutipan sampai persyaratan.
4. **Memprioritaskan** (C5) persyaratan berdasarkan bukti dan kendala.

---

## Materi Pembelajaran

### 4.1 Tiga Hal yang Sering Tertukar

| Istilah | Definisi | Contoh |
|---------|----------|--------|
| **Kebutuhan** | Keadaan yang ingin dicapai; **bebas solusi** | "Tahu sisa bahan tanpa menghitung manual" |
| **Keinginan** | Solusi yang diungkapkan pelanggan | "Saya mau aplikasi yang ada notifikasinya" |
| **Solusi** | Cara memenuhi kebutuhan | Aplikasi, papan tulis, atau perubahan prosedur |

Kekeliruan yang paling sering: **mencatat keinginan sebagai kebutuhan**.

> Kalimat yang sering dikutip — *"Kalau saya tanya apa yang orang inginkan, mereka akan bilang kuda yang lebih cepat"* — menggambarkan persoalannya. Kebutuhannya adalah **berpindah lebih cepat**; kudanya adalah solusi yang terbayangkan pelanggan dari pengalamannya.

Tugas tim bukan menjalankan permintaan pelanggan, melainkan **memahami kebutuhan di balik permintaan itu**.

#### 4.1.1 Cara Menerjemahkan

| Yang dikatakan pelanggan | Kebutuhan di baliknya | Pertanyaan yang mengungkapnya |
|--------------------------|----------------------|-------------------------------|
| "Mau ada notifikasi" | Tidak ingin lupa pada saat yang tepat | "Kapan Anda biasanya lupa? Apa yang terjadi saat itu?" |
| "Mau bisa diakses offline" | Koneksi tidak dapat diandalkan di lokasi | "Di mana Anda biasanya memakainya? Bagaimana sinyalnya?" |
| "Mau lebih sederhana" | Beban kognitif terlalu tinggi saat sibuk | "Bagian mana yang membuat Anda berhenti?" |
| "Mau ada laporan bulanan" | Perlu meyakinkan pihak lain (bank, keluarga) | "Laporan itu untuk siapa? Apa yang mereka lihat?" |

Kolom ketiga adalah yang membedakan tim yang mendengarkan dari tim yang mencatat.

---

### 4.2 *Constraint*: Batas yang Tidak Dapat Ditawar

Kebutuhan menyatakan apa yang ingin dicapai; ***constraint*** menyatakan **batas yang harus dihormati** oleh solusi apa pun.

| Jenis *constraint* | Contoh dari wawancara |
|--------------------|----------------------|
| Waktu | "Cuma sempat 5 detik antara satu pembeli dan berikutnya" |
| Biaya | "Kalau lebih dari 50 ribu sebulan, nggak sanggup" |
| Perangkat | "HP saya memorinya sudah penuh" |
| Keterampilan | "Saya nggak bisa yang ribet-ribet" |
| Fisik | "Tangan saya kotor, nggak bisa pegang HP" |
| Sosial | "Nggak enak kalau catat-catat di depan pembeli" |
| Regulasi | "Laporan pajaknya harus formatnya begitu" |

> ***Constraint* lebih sering menggagalkan produk daripada kurangnya fitur.** Produk yang memenuhi seluruh kebutuhan tetapi melanggar satu *constraint* yang tidak dapat ditawar tidak akan dipakai.

#### 4.2.1 Memisahkan *Constraint* Keras dan Lunak

| Jenis | Ciri | Perlakuan |
|-------|------|-----------|
| **Keras** | Melanggarnya membuat produk mustahil dipakai | Persyaratan wajib |
| **Lunak** | Melanggarnya membuat produk kurang nyaman | Dapat dikompromikan |

Membedakan keduanya menuntut penggalian. "Harus offline" bisa keras (di lokasi memang tidak ada sinyal) atau lunak (pengguna khawatir tetapi sebenarnya sinyal memadai). Pertanyaan yang membedakan: *"Kapan terakhir kali Anda benar-benar tidak dapat sinyal di sana?"*

---

### 4.3 Matriks Keterlacakan

#### 4.3.1 Bentuknya

| ID | Kebutuhan | Bukti | *Constraint* terkait | Persyaratan produk | Prioritas |
|----|-----------|-------|---------------------|--------------------|-----------|
| K-01 | Tahu sisa bahan tanpa menghitung manual | W03, W05, W09 | Waktu 5 detik; tangan kotor | Pencatatan dapat diselesaikan dalam ≤ 5 detik tanpa menyentuh layar berulang | **Wajib** |
| K-02 | Tidak lupa mencatat saat ramai | W03, W05 | Sedang melayani pembeli | Pencatatan dapat ditunda dan diselesaikan sekaligus setelah jam ramai | **Wajib** |
| K-03 | Tahu kapan harus belanja | W03, W08 | Biaya < Rp 50rb/bulan | Perkiraan kebutuhan belanja berdasarkan pola pemakaian | Penting |
| K-04 | Meyakinkan bank untuk pinjaman | W07 | Format laporan tertentu | Ekspor ringkasan bulanan | Dapat ditunda |

#### 4.3.2 Aturan Keterlacakan

| Aturan | Alasan |
|--------|--------|
| **Setiap kebutuhan memiliki ≥ 1 kode bukti** | Tanpa bukti, ia dugaan |
| **Kebutuhan yang hanya disebut 1 narasumber ditandai** | Mungkin kekhususan, bukan pola |
| **Setiap persyaratan berasal dari kebutuhan** | Persyaratan tanpa induk adalah fitur yang diinginkan tim, bukan pelanggan |
| **Setiap *constraint* memiliki bukti** | *Constraint* karangan membatasi solusi tanpa alasan |

> **Baris ketiga adalah pemeriksaan yang paling sering menggugurkan.** Tim yang berlatar teknis cenderung menambahkan persyaratan yang menarik secara teknis ("integrasi dengan API X", "dashboard real-time") yang tidak berasal dari kebutuhan mana pun.

---

### 4.4 Prioritisasi

#### 4.4.1 Kerangka MoSCoW

| Tingkat | Makna | Kriteria |
|---------|-------|----------|
| **Must** | Tanpa ini produk tidak dapat dipakai | Melanggar *constraint* keras bila tidak ada |
| **Should** | Penting, tetapi produk masih berfungsi tanpanya | Disebut banyak narasumber |
| **Could** | Menyenangkan bila ada | Disebut sedikit narasumber |
| **Won't (kali ini)** | Sengaja tidak dikerjakan sekarang | Dicatat agar tidak dibahas berulang |

Kategori keempat sering dilewati dan paling berguna: ia **menutup perdebatan** yang jika tidak dicatat akan muncul kembali setiap minggu.

#### 4.4.2 Memprioritaskan dengan Bukti

| Pertimbangan | Pertanyaan |
|--------------|-----------|
| Frekuensi | Berapa narasumber menyebutnya? |
| Intensitas | Seberapa kuat bahasanya? |
| Biaya masalah | Berapa waktu/uang yang disebut hilang? |
| Usaha mengatasi | Apakah mereka sudah mencoba sesuatu? |
| Kesulitan membangun | Berapa lama tim membutuhkannya? |

Prioritas tertinggi: **tinggi pada empat kolom pertama, rendah pada kolom kelima**. Ini adalah titik masuk yang paling efisien.

---

### 4.5 Milestone 1 — Bukti Masalah

Minggu ini menandai titik pemeriksaan pertama. Yang dikumpulkan:

| Berkas | Isi |
|--------|-----|
| Catatan wawancara | **Minimal 8**, sesuai format Minggu 2 |
| Persona dan JTBD | Dengan keterlacakan penuh |
| Peta perjalanan | Dengan baris bukti |
| Matriks kebutuhan → persyaratan | Dengan keterlacakan penuh |
| **Ringkasan 1 halaman** | **Apa yang ternyata berbeda dari dugaan awal** |
| Pernyataan arah | Melanjutkan ranah yang sama, atau mengubahnya — dengan alasan |

#### 4.5.1 Tentang Ringkasan "Apa yang Berbeda"

Ini bukan bagian formalitas. Sub-CPMK `UAI32-1` menilai **bukti adaptasi keputusan**, dan inilah tempat pertama ia dapat ditunjukkan.

| Jawaban | Penilaian |
|---------|-----------|
| "Dugaan kami sepenuhnya benar" | Kemungkinan besar wawancaranya memimpin, atau buktinya tidak benar-benar dibaca |
| "Masalah utamanya ternyata bukan A melainkan B, karena [bukti]" | **Inilah yang dicari** |
| "Kami mengubah segmen dari X ke Y karena [bukti]" | Dinilai tinggi |
| "Kami menghentikan ranah ini karena [bukti]" | **Sah dan tidak merugikan nilai** |

> Baris terakhir perlu ditegaskan. Tim yang menemukan bahwa ranah pilihannya ternyata tidak memuat masalah yang cukup terasa, **dan menyatakannya berdasarkan bukti**, telah melakukan pekerjaan yang benar. Mereka akan mengganti ranah dan melanjutkan dengan siklus yang dipersingkat — dengan bimbingan dosen.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 4 buku ajar](../06-buku-ajar/bab-04-dari-kebutuhan-ke-persyaratan.md).
- Menyelesaikan minimal 8 wawancara.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 15' | Laporan kilat: apa yang berubah dari dugaan awal |
| Konsep | 30' | Kebutuhan vs keinginan vs solusi; *constraint* |
| Studio | 45' | Menyusun matriks keterlacakan |
| **Presentasi silang** | 40' | **Kegiatan inti:** tim menukar matriks; mencari persyaratan tanpa induk |
| Konsep | 15' | Prioritisasi MoSCoW |
| Penutup | 5' | Pengumpulan P-01 |

**Kegiatan inti — audit silang:** setiap tim menerima matriks tim lain dan mencari:

1. Persyaratan yang **tidak berasal dari kebutuhan mana pun**.
2. Kebutuhan yang **tidak memiliki bukti**.
3. *Constraint* yang **tampaknya karangan**.
4. Keinginan yang **dicatat sebagai kebutuhan**.

Temuan dipresentasikan singkat kepada tim asal. Bagian ini sering tidak nyaman dan selalu berguna.

### Setelah Kelas (120 menit)

- Memperbaiki matriks berdasarkan audit silang.
- Menyelesaikan [Studio 4](../04-labs/lab-04-matriks-kebutuhan-persyaratan.md).

---

## Penugasan

**S-04 — Matriks Kebutuhan → Persyaratan** dan **P-01 — Milestone 1**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Matriks keterlacakan + berkas Milestone 1 lengkap |
| Kriteria khusus | **Keterlacakan penuh**; tidak ada persyaratan tanpa induk |
| Isi tambahan | Ringkasan "apa yang ternyata berbeda" + pernyataan arah |
| Tenggat | Akhir Minggu 4 |
| Bobot | 3,4% (Observasi); P-01 dinilai sebagai bagian komponen Observasi `091-1` |

---

## Rangkuman

1. **Kebutuhan bebas solusi; keinginan adalah solusi yang diungkapkan pelanggan.**
2. Tugas tim adalah memahami **kebutuhan di balik permintaan**, bukan menjalankan permintaan.
3. ***Constraint* lebih sering menggagalkan produk daripada kurangnya fitur.**
4. *Constraint* **keras** membuat produk mustahil dipakai bila dilanggar; yang **lunak** dapat dikompromikan.
5. **Matriks keterlacakan**: setiap persyaratan berasal dari kebutuhan; setiap kebutuhan memiliki bukti.
6. **Persyaratan tanpa induk** adalah fitur yang diinginkan tim, bukan pelanggan.
7. MoSCoW; kategori **"Won't kali ini"** menutup perdebatan berulang.
8. Prioritas tertinggi: tinggi pada frekuensi, intensitas, biaya, dan usaha mengatasi — **rendah pada kesulitan membangun**.
9. Milestone 1 menuntut **ringkasan apa yang ternyata berbeda dari dugaan awal**.
10. **Menghentikan ranah berdasarkan bukti adalah pilihan yang sah** dan tidak merugikan nilai.

---

## Referensi

1. Blank, S., & Dorf, B. (2020). *The Startup Owner's Manual*, Bab 4. Wiley.
2. Wiegers, K., & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.
3. Osterwalder, A., et al. (2014). *Value Proposition Design*. Wiley.
4. Fitzpatrick, R. (2013). *The Mom Test*. Founder Centric.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
