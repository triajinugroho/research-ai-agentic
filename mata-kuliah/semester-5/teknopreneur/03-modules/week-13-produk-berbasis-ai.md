# Minggu 13: Produk Berbasis AI — Kelayakan dan Batasnya

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Teknopreneur (`ST52510002`) |
| Minggu | 13 dari 16 |
| Topik | Kapan AI memberi nilai; biaya nyata; ketergantungan; risiko khas; regulasi |
| Sub-CPMK | `TEKNO-Sub-CPMKUAI21-1` |
| Bloom | C4 → C5 |
| Durasi | 150 menit |
| Metode | Kuliah · Studi kasus · Studio penilaian |
| Penilaian | Observasi (Studio 13) |

---

## Kedudukan Minggu Ini

Pada AI Curriculum Infusion Matrix, mata kuliah ini berstatus **mode E (Eksplisit)** dengan pilar **AI Product** dan peran *"AI venture, feasibility dan business model"*. Minggu ini adalah pemenuhan status itu.

Yang dibahas bukan **cara membangun** model AI — itu cakupan mata kuliah Dasar Kecerdasan Artifisial dan Pembelajaran Mesin. Yang dibahas adalah:

> **Apakah usaha berbasis AI ini layak, dan apa risikonya?**

Dan pertanyaan itu sering berjawab **tidak**.

---

## Tujuan Pembelajaran

1. **Menganalisis** (C4) apakah komponen AI memberi nilai yang sepadan pada usaha tertentu.
2. **Menghitung** (C3) biaya nyata komponen AI dan dampaknya pada margin.
3. **Mengevaluasi** (C5) risiko khas produk berbasis AI.
4. **Memutuskan** (C5) apakah memakai AI — termasuk memutuskan **tidak**.

---

## Materi Pembelajaran

### 13.1 Kapan AI Memberi Nilai

#### 13.1.1 Empat Keadaan AI Berguna

| Keadaan | Contoh |
|---------|--------|
| **Volume tinggi, keputusan berulang** | Menyaring ribuan pengajuan; menandai konten |
| **Pola rumit yang sulit diaturkan** | Mengenali objek pada citra; memahami maksud teks |
| **Personalisasi pada skala** | Rekomendasi bagi ribuan pengguna |
| **Data melimpah dan berkualitas** | Riwayat yang cukup untuk dipelajari |

#### 13.1.2 Lima Keadaan AI Tidak Diperlukan

| Keadaan | Mengapa | Alternatif |
|---------|---------|------------|
| **Aturannya sudah jelas dan stabil** | Aturan biasa lebih murah, cepat, dan tepat | `if-else` |
| **Volume rendah** | Biaya membangun tidak sepadan | Dikerjakan manusia |
| **Kesalahan berakibat berat** | Model selalu memiliki galat | Pengambil keputusan manusia |
| **Data tidak tersedia** | Tidak ada yang dapat dipelajari | Kumpulkan data dahulu |
| **Keterjelasan penuh dituntut** | Banyak model sulit dijelaskan | Model sederhana atau aturan |

> **Kesalahan yang paling sering pada usaha rintisan 2026:** menambahkan komponen AI karena **terdengar menarik bagi investor atau pengguna**, bukan karena ia memberi nilai.
>
> Komponen AI yang tidak diperlukan menambah biaya, menambah ketergantungan, menambah risiko, dan **mengurangi margin** — untuk nilai yang tidak bertambah.

#### 13.1.3 Uji Sederhana

Tiga pertanyaan:

1. **Bila komponen AI ini diganti dengan aturan sederhana, seberapa buruk hasilnya?**
   Bila hanya sedikit lebih buruk, AI tidak sepadan.
2. **Bila komponen AI ini diganti dengan manusia, berapa biayanya?**
   Bila lebih murah daripada AI, pakai manusia dahulu.
3. **Apakah pelanggan membayar untuk AI, atau untuk hasilnya?**
   Hampir selalu untuk hasilnya — dan hasilnya mungkin dapat dicapai tanpa AI.

---

### 13.2 Biaya Nyata Produk AI

Ini bagian yang paling sering diabaikan dan paling menentukan kelayakan.

#### 13.2.1 Komponen Biaya

| Komponen | Sering dilupakan? | Catatan |
|----------|-------------------|---------|
| Biaya API model per pemakaian | Tidak | Paling terlihat |
| **Biaya per pengguna per bulan** | **Ya** | Bergantung intensitas pemakaian |
| Biaya pelabelan data | **Ya** | Bila melatih model sendiri |
| Biaya komputasi pelatihan | Tidak | Bila melatih model sendiri |
| **Biaya pemeriksaan manusia** | **Ya** | Keluaran yang harus diperiksa |
| **Biaya penanganan kesalahan** | **Ya** | Ketika model salah |
| Biaya pemantauan dan pelatihan ulang | **Ya** | Kinerja menurun seiring waktu |

#### 13.2.2 Menghitung Dampak pada Margin

Contoh: layanan yang memakai model bahasa untuk meringkas dokumen.

| Komponen | Perhitungan | Biaya/pengguna/bulan |
|----------|-------------|----------------------|
| Pemakaian model | 40 permintaan × biaya per permintaan | Rp 12.000 |
| Pemeriksaan manusia (10% keluaran) | 4 pemeriksaan × 3 menit × nilai waktu | Rp 6.000 |
| Penanganan keluhan keliru | 0,5 kejadian × 10 menit | Rp 2.500 |
| Infrastruktur | — | Rp 2.000 |
| **Total biaya langsung** | | **Rp 22.500** |

Bila harga langganan Rp 50.000/bulan:

$$\text{Margin kotor} = \frac{50.000 - 22.500}{50.000} = 55\%$$

Margin 55% untuk produk perangkat lunak **jauh di bawah** yang lazim (70–85%). Ini bukan berarti usaha ini tidak layak — tetapi ia mengubah seluruh perhitungan *unit economics* Minggu 7.

> **Yang harus diperiksa:** apakah biaya per pengguna **turun** seiring skala? Untuk biaya API, sering tidak — ia naik sebanding pemakaian. Ini berbeda dari perangkat lunak biasa, di mana biaya marginal mendekati nol.

#### 13.2.3 Biaya yang Berubah

| Risiko | Contoh |
|--------|--------|
| Harga penyedia naik | Perubahan harga API yang berlaku mendadak |
| Model diganti | Versi lama dihentikan; perilaku berubah |
| Kuota dibatasi | Batas pemakaian diturunkan |
| Layanan dihentikan | Penyedia menutup layanan |

**Yang harus disiapkan:** perhitungan *"berapa margin kita bila biaya model naik 3×?"* — sebagai bagian analisis sensitivitas.

---

### 13.3 Risiko Khas Produk AI

| Risiko | Penjelasan | Mitigasi |
|--------|------------|----------|
| **Keluaran salah yang meyakinkan** | Model menghasilkan sesuatu yang tampak benar tetapi salah | Pemeriksaan manusia pada keputusan penting |
| **Kinerja menurun seiring waktu** | Data dunia berubah; model tidak | Pemantauan; pelatihan ulang berkala |
| **Ketimpangan antarkelompok** | Bekerja lebih buruk untuk sebagian pengguna | Pengukuran terpisah per kelompok |
| **Ketergantungan penyedia** | Seluruh produk bergantung pada satu penyedia | Alternatif disiapkan; biaya berpindah dihitung |
| **Data pengguna ke pihak ketiga** | Data dikirim ke penyedia model | Dinyatakan kepada pengguna; periksa ketentuan penyedia |
| **Ekspektasi berlebihan** | Pengguna mengira model lebih mampu daripada sebenarnya | Nyatakan batas kemampuan secara terbuka |
| **Regulasi berubah** | Aturan AI masih berkembang | Pantau; rancang agar dapat menyesuaikan |

#### 13.3.1 Risiko Ketimpangan dalam Konteks Indonesia

Model yang dilatih pada data yang terpusat pada satu kelompok akan bekerja lebih buruk untuk kelompok lain. Pada konteks Indonesia, ini sering berarti:

| Ketimpangan | Contoh |
|-------------|--------|
| Bahasa | Model bahasa bekerja lebih baik untuk bahasa Indonesia baku daripada bahasa daerah atau campuran |
| Wilayah | Data terpusat di Jawa |
| Ekonomi | Pola yang dipelajari mencerminkan kelompok yang sudah terdigitalisasi |

> Usaha yang menyatakan melayani "seluruh UMKM Indonesia" tetapi modelnya dilatih pada data pengguna perkotaan **wajib menyatakan batas itu** — bukan sebagai kelemahan yang disembunyikan, melainkan sebagai informasi yang dibutuhkan calon pengguna.

#### 13.3.2 Menyatakan Batas Kemampuan

Prinsip **menjauhi `gharar`** menuntut kejelasan tentang apa yang dibeli pengguna. Untuk produk AI, ini berarti:

| Yang harus dinyatakan | Contoh |
|-----------------------|--------|
| Bahwa hasilnya dapat salah | "Ringkasan dihasilkan otomatis dan dapat mengandung kekeliruan" |
| Kapan hasil perlu diperiksa | "Untuk keputusan penting, periksa dokumen aslinya" |
| Batas cakupan | "Dirancang untuk dokumen berbahasa Indonesia baku" |
| Bahwa data diproses pihak ketiga | Bila memang demikian |

Menyembunyikan bahwa keluaran dapat salah, atau mengklaim ketepatan yang tidak dimiliki, adalah **`tadlis`**.

---

### 13.4 Regulasi AI

| Tingkat | Keadaan 2026 |
|---------|--------------|
| **Indonesia** | Berkembang; UU PDP sudah berlaku dan mencakup pemrosesan data oleh sistem AI |
| **Internasional** | Regulasi AI Uni Eropa memengaruhi produk yang menjangkau pasar sana |
| **Sektoral** | Sektor keuangan dan kesehatan memiliki ketentuan tersendiri |

#### 13.4.1 Yang Perlu Disiapkan

| Hal | Alasan |
|-----|--------|
| Dokumentasi sumber data latih | Dituntut banyak kerangka regulasi |
| Catatan keputusan yang melibatkan AI | Untuk audit dan penanganan keberatan |
| Mekanisme keberatan | Pengguna dapat meminta peninjauan manusia |
| Pernyataan pemakaian AI | Pengguna tahu bahwa AI terlibat |

> Menyiapkan hal-hal ini sejak awal jauh lebih murah daripada menambahkannya setelah produk berjalan.

---

### 13.5 Keputusan: Memakai AI atau Tidak

Studio 13 menuntut **keputusan yang dinyatakan**, bukan sekadar pembahasan.

| Keputusan | Yang harus disertakan |
|-----------|-----------------------|
| **Memakai AI** | Komponen apa · mengapa sepadan · biaya per pengguna · ketergantungan · risiko dan mitigasi · batas yang dinyatakan kepada pengguna |
| **Tidak memakai AI** | **Alasan yang kuat** · alternatif yang dipakai · kondisi apa yang akan mengubah keputusan ini |

> **Menjawab "tidak perlu AI" dengan alasan yang kuat dinilai setara** dengan menjawab "perlu". Yang dinilai adalah kualitas penalarannya, bukan pilihannya.
>
> Pada tahun ketika hampir setiap usaha mengklaim memakai AI, kemampuan menyatakan **"usaha ini tidak memerlukannya, dan inilah alasannya"** adalah tanda penilaian yang matang — bukan ketertinggalan.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 12 buku ajar](../06-buku-ajar/bab-12-produk-berbasis-ai.md).
- Memeriksa harga terkini penyedia model yang relevan bagi usaha tim.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Pembahasan S-12; temuan audit etika yang menarik |
| Konsep | 30' | Kapan AI berguna dan kapan tidak; uji tiga pertanyaan |
| **Studio** | 45' | **Kegiatan inti:** menghitung biaya AI per pengguna dan dampaknya pada margin |
| Konsep | 30' | Risiko khas; ketimpangan; menyatakan batas kemampuan |
| Studi kasus | 25' | Dua usaha: satu yang AI-nya sepadan, satu yang tidak |
| Penutup | 10' | Penugasan |

**Kegiatan inti — perhitungan biaya AI:** tiap tim menghitung biaya komponen AI per pengguna per bulan, lalu memasukkannya ke model *unit economics* Minggu 7 dan melihat perubahan margin.

Hasilnya sering mengejutkan tim yang merencanakan pemakaian model bahasa secara intensif: margin dapat turun dari 80% ke bawah 50%, dan itu mengubah seluruh kelayakan.

### Setelah Kelas (120 menit)

- Menyelesaikan [Studio 13](../04-labs/lab-13-kelayakan-produk-ai.md).
- Menyiapkan draf *pitch deck* untuk Minggu 14.

---

## Penugasan

**S-13 — Penilaian Kelayakan Komponen AI**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Dokumen penilaian |
| Isi | Uji tiga pertanyaan §13.1.3 · **perhitungan biaya nyata per pengguna** · dampak pada margin · ketergantungan penyedia · risiko dan mitigasi · batas yang akan dinyatakan kepada pengguna |
| **Penutup** | **Keputusan: memakai AI atau tidak** — dengan alasan |
| Kriteria khusus | Perhitungan biaya memakai **harga terkini yang diperiksa**, bukan perkiraan |
| Tenggat | Awal pertemuan Minggu 14 |
| Bobot | 6,25% (Observasi) |

---

## Rangkuman

1. Minggu ini memenuhi status **mode E (Eksplisit), pilar AI Product** pada AI Infusion Matrix.
2. Pertanyaannya bukan "bagaimana membangun AI", melainkan **"apakah usaha berbasis AI ini layak?"**
3. Empat keadaan AI berguna; **lima keadaan AI tidak diperlukan**.
4. Kesalahan tersering: menambahkan AI karena **terdengar menarik**, bukan karena memberi nilai.
5. **Uji tiga pertanyaan:** seberapa buruk bila diganti aturan; berapa biaya bila diganti manusia; pelanggan membayar untuk AI atau untuk hasilnya.
6. **Biaya nyata AI sering mengubah margin secara drastis** — dan sering tidak turun seiring skala.
7. Analisis sensitivitas wajib memuat: **berapa margin bila biaya model naik 3×?**
8. Risiko khas mencakup **keluaran salah yang meyakinkan** dan **ketimpangan antarkelompok**.
9. Pada konteks Indonesia, ketimpangan sering berwujud **bahasa, wilayah, dan tingkat digitalisasi**.
10. **Menyatakan batas kemampuan** adalah pemenuhan prinsip menjauhi `gharar` dan `tadlis`.
11. **Memutuskan "tidak perlu AI" dengan alasan kuat dinilai setara** dengan memutuskan memakainya.

---

## Referensi

1. Ng, A. (2021). *AI Transformation Playbook*. Landing AI.
2. Agrawal, A., Gans, J., & Goldfarb, A. (2022). *Power and Prediction*. Harvard Business Review Press.
3. Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and Machine Learning*. <https://fairmlbook.org>
4. Undang-Undang No. 27 Tahun 2022 tentang Pelindungan Data Pribadi.
5. Dokumentasi harga penyedia model (diperiksa pada saat penyusunan rencana).
6. Tim Kurikulum Informatika UAI (2026). *AI Curriculum Infusion Matrix*.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
