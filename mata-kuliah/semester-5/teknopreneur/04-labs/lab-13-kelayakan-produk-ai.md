# Studio 13: Kelayakan Produk Berbasis AI

| Aspek | Keterangan |
|-------|------------|
| Minggu | 13 · Sub-CPMK `UAI21-1` · Bobot 6,25% (Observasi) |
| Durasi | 45' di kelas + 60' mandiri |
| Luaran | Dokumen penilaian + **keputusan memakai AI atau tidak** |

---

## Tujuan Studio

1. Menguji apakah komponen AI memberi nilai yang sepadan.
2. Menghitung biaya nyata AI per pengguna dengan harga terkini.
3. Mengukur dampaknya pada margin dan *unit economics*.
4. **Memutuskan** — termasuk memutuskan tidak memakai AI.

---

## Ketentuan Khusus Studio Ini

> **Menjawab "usaha ini tidak memerlukan AI" dengan alasan yang kuat dinilai setara** dengan menjawab "perlu". Yang dinilai adalah kualitas penalarannya.
>
> Pada tahun ketika hampir setiap usaha mengklaim memakai AI, kemampuan menyatakan *"kami tidak memerlukannya, dan inilah alasannya"* adalah tanda penilaian yang matang.

---

## Langkah-langkah

### LANGKAH 1: Uji Tiga Pertanyaan

Untuk setiap komponen AI yang dipertimbangkan:

| # | Pertanyaan | Jawaban | Kesimpulan |
|---|-----------|---------|------------|
| 1 | Bila diganti **aturan sederhana**, seberapa buruk hasilnya? | | Bila hanya sedikit lebih buruk → AI tidak sepadan |
| 2 | Bila diganti **manusia**, berapa biayanya? | | Bila lebih murah → pakai manusia dahulu |
| 3 | Apakah pelanggan membayar untuk **AI** atau untuk **hasilnya**? | | Hampir selalu hasilnya |

**Lakukan pengujian nyata untuk pertanyaan 1:**

| Kasus uji | Hasil dengan aturan sederhana | Hasil dengan AI | Selisih |
|-----------|------------------------------|-----------------|---------|
| | | | |

> Ambil 10 kasus nyata dari data tim. Kerjakan dengan aturan `if-else` sederhana dan dengan AI. Bandingkan. Selisih yang kecil berarti AI tidak sepadan dengan biayanya.

### LANGKAH 2: Memeriksa Lima Keadaan AI Tidak Diperlukan

| Keadaan | Berlaku untuk usaha kami? | Bukti |
|---------|---------------------------|-------|
| Aturannya sudah jelas dan stabil | ya / tidak | |
| Volume rendah | ya / tidak | |
| Kesalahan berakibat berat | ya / tidak | |
| Data tidak tersedia | ya / tidak | |
| Keterjelasan penuh dituntut | ya / tidak | |

**Bila ada satu "ya", jelaskan mengapa AI tetap dipertimbangkan.**

### LANGKAH 3: Menghitung Biaya Nyata

**Periksa harga terkini** — bukan perkiraan.

| Komponen | Cara menghitung | Sumber harga | Tanggal | Biaya/pengguna/bulan |
|----------|-----------------|--------------|---------|----------------------|
| Pemakaian model | [n] permintaan × [harga] | | | |
| Penyimpanan/vektor | | | | |
| **Pemeriksaan manusia** | [%] keluaran × [menit] × nilai waktu | — | — | |
| **Penanganan kesalahan** | [frekuensi] × [menit] | — | — | |
| Pemantauan dan pelatihan ulang | | | | |
| **TOTAL** | | | | |

> Dua baris bertanda tebal paling sering dilupakan. Keluaran AI yang salah tidak hilang sendiri — seseorang harus memeriksanya dan menanganinya.

### LANGKAH 4: Dampak pada Margin

| Aspek | Tanpa AI | Dengan AI |
|-------|----------|-----------|
| Harga bulanan | | |
| Biaya langsung/pengguna | | |
| **Margin kotor (%)** | | |
| LTV | | |
| **LTV/CAC** | | |

**Pertanyaan yang harus dijawab:**

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa penurunan margin akibat AI? | |
| Apakah nilai tambahnya sepadan dengan penurunan itu? | |
| **Apakah biaya AI turun seiring skala?** | |
| Berapa margin bila **biaya model naik 3×**? | |

> Biaya API umumnya **naik sebanding pemakaian**, tidak turun seiring skala — berbeda dari perangkat lunak biasa yang biaya marginalnya mendekati nol. Ini mengubah seluruh logika *unit economics*.

### LANGKAH 5: Memetakan Ketergantungan

| Penyedia | Untuk apa | Proporsi biaya langsung | Bila berhenti besok | Biaya berpindah | Alternatif |
|----------|-----------|------------------------|---------------------|-----------------|------------|
| | | % | | | |

**Bila proporsi melebihi 50%:** seluruh margin bergantung pada pihak yang dapat mengubah harga sepihak. Catat sebagai risiko utama.

### LANGKAH 6: Menilai Risiko Khas

| Risiko | Berlaku? | Tanda awal | Mitigasi |
|--------|----------|------------|----------|
| Keluaran salah yang meyakinkan | | | |
| Kinerja menurun seiring waktu | | | |
| **Ketimpangan antarkelompok** | | | |
| Ketergantungan penyedia | | | |
| Data pengguna ke pihak ketiga | | | |
| Ekspektasi berlebihan pengguna | | | |
| Regulasi berubah | | | |

**Untuk ketimpangan antarkelompok, periksa konteks Indonesia:**

| Dimensi | Apakah model bekerja setara? | Bagaimana tahu? |
|---------|------------------------------|-----------------|
| Bahasa (baku / daerah / campuran) | | |
| Wilayah | | |
| Tingkat digitalisasi pengguna | | |

### LANGKAH 7: Menyatakan Batas kepada Pengguna

| Yang harus dinyatakan | Kalimat yang akan dipakai |
|-----------------------|---------------------------|
| Bahwa hasilnya dapat salah | |
| Kapan hasil perlu diperiksa | |
| Batas cakupan | |
| Bahwa data diproses pihak ketiga | |

> Menyembunyikan bahwa keluaran dapat salah, atau mengklaim ketepatan yang tidak dimiliki, adalah **`tadlis`**. Menyatakannya adalah pemenuhan prinsip menjauhi `gharar`.

### LANGKAH 8: Keputusan

```markdown
## Keputusan Komponen AI

### Ringkasan Penilaian

| Aspek | Temuan |
|-------|--------|
| Hasil uji tiga pertanyaan | |
| Keadaan "AI tidak diperlukan" yang berlaku | |
| Biaya AI per pengguna per bulan | |
| Penurunan margin | |
| Ketergantungan terbesar | |
| Risiko terbesar | |

### KEPUTUSAN

- [ ] **MEMAKAI AI** untuk [komponen]
- [ ] **TIDAK MEMAKAI AI**

### Alasan

[Merujuk pada angka di atas]

### Bila MEMAKAI: yang disiapkan

- Batas yang dinyatakan kepada pengguna: [kalimat]
- Mekanisme pemeriksaan manusia: [cara]
- Rencana bila penyedia berhenti/menaikkan harga: [rencana]
- Cara mengukur ketimpangan antarkelompok: [cara]

### Bila TIDAK MEMAKAI: yang dipakai sebagai gantinya

- Pendekatan: [aturan / manusia / lainnya]
- **Kondisi yang akan mengubah keputusan ini:** [kapan AI menjadi masuk akal]
```

---

## Tantangan Tambahan

### Tantangan 1 — Membandingkan Aturan dan AI pada 20 Kasus

Ambil 20 kasus nyata dari data tim. Kerjakan dengan aturan sederhana dan dengan AI. Hitung: berapa persen kasus yang hasilnya berbeda? Pada kasus yang berbeda, mana yang lebih tepat?

### Tantangan 2 — Menghitung pada Tiga Skala

Hitung biaya AI pada 100, 1.000, dan 10.000 pengguna. Buat grafik biaya per pengguna terhadap jumlah pengguna. Apakah menurun? Bandingkan dengan biaya server yang umumnya menurun.

### Tantangan 3 — Menguji Persepsi Pengguna

Tunjukkan dua versi kepada lima orang dari segmen: satu yang menyatakan memakai AI, satu yang tidak menyebutkannya. Apakah ada perbedaan reaksi? Apakah mereka **membayar lebih** untuk yang memakai AI?

---

## Checklist Penyelesaian

- [ ] **Uji tiga pertanyaan** dijalankan dengan pengujian nyata pada kasus
- [ ] Lima keadaan "AI tidak diperlukan" diperiksa
- [ ] **Biaya dihitung dengan harga terkini yang diperiksa**, bukan perkiraan
- [ ] Biaya **pemeriksaan manusia** dan **penanganan kesalahan** dimasukkan
- [ ] Dampak pada margin dan LTV/CAC dihitung
- [ ] Dijawab: apakah biaya turun seiring skala?
- [ ] Dijawab: berapa margin bila biaya model naik 3×?
- [ ] Ketergantungan dipetakan dengan proporsi biaya
- [ ] Risiko khas dinilai, termasuk **ketimpangan konteks Indonesia**
- [ ] **Batas kemampuan yang akan dinyatakan kepada pengguna** dirumuskan
- [ ] **Keputusan dinyatakan** dengan alasan berbasis angka
- [ ] AI Usage Log disertakan

---

## Referensi

1. [Modul Minggu 13](../03-modules/week-13-produk-berbasis-ai.md)
2. [Bab 12 buku ajar](../06-buku-ajar/bab-12-produk-berbasis-ai.md)
3. Ng, A. (2021). *AI Transformation Playbook*. Landing AI.
4. Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and Machine Learning*.
5. Dokumentasi harga penyedia model (diperiksa pada saat penyusunan).
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
