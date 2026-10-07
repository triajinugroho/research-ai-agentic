# Rubrik Penilaian Tugas

## Probabilitas dan Statistik — IF52510033

**Semester Ganjil 2026/2027**
**Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.

---

## 1. Peta Rubrik

| Instrumen | Sub-CPMK | Bobot Total | Rubrik |
|-----------|----------|-------------|--------|
| Laporan Lab (13×) | `PS-Sub-CPMK102-1` | 25% | §2 |
| Kuis (4×) | `PS-Sub-CPMK081-1` | 15% | §3 |
| Proyek | Keduanya | 10% | [project-guidelines.md](project-guidelines.md) |
| UTS | `PS-Sub-CPMK102-1` | 25% | [kisi-kisi-uts.md](kisi-kisi-uts.md) |
| UAS | `PS-Sub-CPMK081-1` | 25% | [kisi-kisi-uas.md](kisi-kisi-uas.md) |

---

## 2. Rubrik Laporan Lab (25% — `PS-Sub-CPMK102-1`)

Kriteria kurikulum: *ketepatan prosedur; kesesuaian grafik; validitas interpretasi.*

### 2.1 Aspek dan Bobot

| Aspek | Bobot |
|-------|-------|
| Ketepatan prosedur | 30% |
| Kesesuaian grafik | 20% |
| Validitas interpretasi | 30% |
| Tantangan tambahan | 10% |
| Kerapian dan AI Usage Log | 10% |

### 2.2 Deskriptor Tingkat

#### Ketepatan Prosedur (30%)

| Skor | Deskriptor |
|------|------------|
| **4** (90–100) | Seluruh langkah statistik benar dan berurutan. Fungsi yang dipakai tepat beserta parameternya (misalnya `ddof` yang sesuai). Tidak ada langkah yang terlewat. |
| **3** (75–89) | Langkah utama benar. Ada satu-dua kekeliruan kecil pada parameter fungsi yang tidak mengubah kesimpulan. |
| **2** (60–74) | Sebagian besar langkah benar, tetapi ada kesalahan yang memengaruhi sebagian hasil. |
| **1** (40–59) | Banyak langkah keliru atau terlewat. Prosedur tidak dapat direproduksi. |
| **0** | Tidak dikerjakan atau notebook tidak dapat dijalankan sama sekali. |

#### Kesesuaian Grafik (20%)

| Skor | Deskriptor |
|------|------------|
| **4** | Jenis grafik tepat untuk jenis data dan pertanyaan. Judul menjelaskan isi. Kedua sumbu berlabel dengan satuan. n dan sumber dicantumkan. Terbaca dalam hitam-putih. |
| **3** | Jenis grafik tepat dan terbaca. Ada satu unsur label yang kurang. |
| **2** | Jenis grafik kurang sesuai, atau beberapa unsur label hilang. |
| **1** | Grafik menyesatkan (misalnya bar chart tidak dari nol) atau tanpa label sama sekali. |
| **0** | Tidak ada grafik padahal diminta. |

#### Validitas Interpretasi (30%)

| Skor | Deskriptor |
|------|------------|
| **4** | Setiap keluaran disertai kalimat interpretasi yang tepat. Kesimpulan persis sebatas yang didukung data. Batas keberlakuan dinyatakan. |
| **3** | Sebagian besar keluaran ditafsirkan dengan tepat. Ada satu tafsir yang kurang tajam. |
| **2** | Interpretasi ada tetapi dangkal, atau ada klaim yang sedikit melampaui data. |
| **1** | Notebook berisi angka tanpa tafsir, atau ada klaim sebab-akibat dari data korelasional. |
| **0** | Tidak ada interpretasi sama sekali. |

> **Aturan tegas:** notebook yang hanya menampilkan angka tanpa kalimat interpretasi memperoleh **maksimal skor 1** pada aspek ini, berapa pun benarnya perhitungannya.

#### Tantangan Tambahan (10%)

| Skor | Deskriptor |
|------|------------|
| **4** | Seluruh tantangan dikerjakan lengkap dan benar, termasuk melengkapi kode yang sengaja dikosongkan. |
| **3** | Seluruh tantangan dikerjakan, ada satu yang kurang lengkap. |
| **2** | Sebagian tantangan dikerjakan. |
| **1** | Hanya satu tantangan dikerjakan. |
| **0** | Tidak ada tantangan dikerjakan. |

#### Kerapian dan AI Usage Log (10%)

| Skor | Deskriptor |
|------|------------|
| **4** | Notebook terstruktur dengan sel Markdown sebagai penanda bagian. Kode berkomentar bahasa Indonesia. AI Usage Log terisi jujur dan ditandatangani. Bagian refleksi terisi. |
| **3** | Terstruktur baik, log terisi, refleksi ada tetapi singkat. |
| **2** | Struktur kurang rapi atau log terisi seadanya. |
| **1** | Tidak terstruktur; log terisi tetapi tidak informatif. |
| **0** | **AI Usage Log tidak ada** → laporan dikembalikan dan dinilai sebagai terlambat. |

### 2.3 Rumus Nilai Laporan Lab

$$\text{Nilai} = 0{,}30 S_1 + 0{,}20 S_2 + 0{,}30 S_3 + 0{,}10 S_4 + 0{,}10 S_5$$

dengan Sᵢ adalah skor 0–4 yang dikonversi ke skala 0–100 (skor 4 = 100, 3 = 82, 2 = 67, 1 = 50, 0 = 0).

### 2.4 Contoh Perhitungan

Seorang mahasiswa memperoleh skor: prosedur 4, grafik 3, interpretasi 3, tantangan 2, kerapian 4.

| Aspek | Skor | Nilai | Bobot | Kontribusi |
|-------|------|-------|-------|------------|
| Prosedur | 4 | 100 | 30% | 30,0 |
| Grafik | 3 | 82 | 20% | 16,4 |
| Interpretasi | 3 | 82 | 30% | 24,6 |
| Tantangan | 2 | 67 | 10% | 6,7 |
| Kerapian | 4 | 100 | 10% | 10,0 |
| **Total** | | | **100%** | **87,7** |

---

## 3. Rubrik Kuis (15% — `PS-Sub-CPMK081-1`)

Kriteria kurikulum: *ketepatan rumus dan hitung; kecocokan asumsi; kualitas interpretasi.*

### 3.1 Aspek dan Bobot

| Aspek | Bobot | Deskripsi |
|-------|-------|-----------|
| Ketepatan rumus | 30% | Rumus yang dipilih sesuai jenis persoalan |
| Ketepatan hitung | 30% | Perhitungan benar sampai hasil akhir; satuan tepat |
| Kecocokan asumsi | 20% | Asumsi distribusi/metode disebutkan dan diperiksa |
| Kualitas interpretasi | 20% | Angka diterjemahkan menjadi kesimpulan kontekstual |

### 3.2 Aturan Penilaian per Soal

| Situasi | Nilai Soal |
|---------|------------|
| Rumus benar, hitung benar, asumsi disebut, interpretasi tepat | 100% |
| Rumus benar, salah hitung kecil di langkah akhir | 75–85% |
| Rumus benar, asumsi tidak disebut padahal diminta | Kehilangan seluruh 20% aspek asumsi |
| Hitungan benar tanpa kalimat interpretasi | Kehilangan seluruh 20% aspek interpretasi |
| Rumus salah tetapi penerapannya konsisten dan rapi | Maksimal 35% |
| Hanya angka akhir, tanpa langkah | Maksimal 40% |
| Satuan tidak ditulis | −10% dari aspek ketepatan hitung |
| Tidak dikerjakan | 0% |

### 3.3 Contoh Penerapan

> **Soal:** Sebuah server menerima rata-rata 6 permintaan per detik. Hitung probabilitas menerima lebih dari 10 permintaan dalam satu detik. Sebutkan asumsi yang Anda pakai.

| Jawaban mahasiswa | Penilaian |
|-------------------|-----------|
| Menulis "Poisson, λ=6, asumsi: kejadian bebas dan laju konstan", menghitung P(X>10) = 1 − P(X≤10) = 0,0426, lalu menulis "artinya sekitar 4,3% dari detik akan mengalami beban di atas 10 permintaan" | **100%** |
| Rumus dan hitungan benar, tetapi tidak menyebutkan asumsi | **80%** |
| Rumus dan hitungan benar, asumsi disebut, tetapi tanpa kalimat interpretasi | **80%** |
| Menulis "0,0426" saja | **40%** |
| Memakai Binomial (tidak sesuai), tetapi penerapannya konsisten dan rapi | **≤ 35%** |

---

## 4. Rubrik Penilaian Sejawat (Presentasi Proyek)

**Tidak berbobot nilai**, tetapi **wajib diisi** sebagai bagian dari keterlibatan kelas.

| Aspek | 1 | 2 | 3 | 4 | 5 |
|-------|---|---|---|---|---|
| Kejelasan pertanyaan penelitian | | | | | |
| Kualitas dan kejujuran visualisasi | | | | | |
| Ketepatan metode statistik | | | | | |
| Kejujuran menyampaikan keterbatasan | | | | | |
| Penguasaan saat tanya jawab | | | | | |

**Satu hal yang paling saya pelajari dari presentasi ini:**

**Satu saran perbaikan yang konstruktif:**

---

## 5. Rubrik Penilaian Kontribusi Anggota Kelompok

Diisi oleh **setiap anggota** untuk dirinya dan rekan sekelompok, dikumpulkan bersama laporan proyek.

| Anggota | Pengumpulan data | Analisis | Penulisan | Presentasi | Koordinasi | Total (0–20) |
|---------|------------------|----------|-----------|------------|------------|--------------|
| Nama 1 | | | | | | |
| Nama 2 | | | | | | |
| Nama 3 | | | | | | |
| Nama 4 | | | | | | |

Skala per aspek: 0 = tidak berkontribusi · 1 = sedikit · 2 = memadai · 3 = baik · 4 = memimpin.

**Penggunaan:** bila rata-rata penilaian sejawat terhadap seorang anggota berada di bawah 8 dari 20, nilai proyek anggota itu dapat **dikurangi hingga 30%** setelah dikonfirmasi dosen melalui wawancara.

---

## 6. Pengurangan Nilai Umum

| Pelanggaran | Pengurangan |
|-------------|-------------|
| Terlambat ≤ 24 jam | −10% |
| Terlambat 24–48 jam | −25% |
| Terlambat 48–72 jam | −50% |
| Terlambat > 72 jam | Tidak dinilai |
| Notebook tidak dapat dijalankan ulang | −20% |
| AI Usage Log tidak ada | Dikembalikan; dinilai sebagai terlambat |
| Data dimanipulasi agar hasil signifikan | **Nilai 0 dan dilaporkan ke Program Studi** |
| Menyalin pekerjaan mahasiswa lain | **Nilai 0 untuk kedua pihak** |

---

## 7. Banding Nilai

| Tahap | Ketentuan |
|-------|-----------|
| Pengajuan | Maksimal 3 hari kerja setelah nilai diumumkan |
| Bentuk | Tertulis, menyebutkan butir mana dan alasan keberatan |
| Yang tidak dapat dibanding | Nilai yang diberikan berdasarkan rubrik yang sudah diterapkan konsisten |
| Yang dapat dibanding | Kesalahan penjumlahan, butir yang terlewat dinilai, salah baca jawaban |
| Konsekuensi | Nilai dapat naik **atau turun** setelah peninjauan ulang menyeluruh |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
