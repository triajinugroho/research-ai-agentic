# BUKU AJAR

# ANALISIS DATA STATISTIK
## Pendekatan Komputasional dengan Python dan AI

---

### Untuk Mahasiswa Program Studi Informatika

---

**Penulis:**
# Tri Aji Nugroho, S.T., M.T.

---

**Program Studi Informatika**
**Fakultas Sains dan Teknologi**
**Universitas Al Azhar Indonesia**
**Jakarta, 2025**

---

### Identitas Buku

| Komponen | Detail |
|----------|--------|
| **Judul** | Analisis Data Statistik: Pendekatan Komputasional dengan Python dan AI |
| **Penulis** | Tri Aji Nugroho, S.T., M.T. |
| **Institusi** | Universitas Al Azhar Indonesia |
| **Fakultas** | Sains dan Teknologi |
| **Program Studi** | Informatika |
| **Edisi** | Pertama, 2025 |
| **Jumlah Bab** | 13 Bab + Lampiran |
| **Sasaran Pembaca** | Mahasiswa S1 Informatika Semester 2 |
| **Pendekatan** | Outcome-Based Education (OBE), AI-Augmented |

---

### Kata Pengantar

بسم الله الرحمن الرحيم

**Assalamu'alaikum Warahmatullahi Wabarakatuh**

Segala puji bagi Allah SWT yang telah memberikan nikmat ilmu dan kemudahan dalam menyusun buku ajar ini. Shalawat serta salam senantiasa tercurahkan kepada Nabi Muhammad SAW, teladan terbaik dalam menuntut ilmu dan mengamalkannya.

Buku ajar **"Analisis Data Statistik: Pendekatan Komputasional dengan Python dan AI"** ini disusun sebagai panduan utama mata kuliah Analisis Data Statistik untuk mahasiswa Program Studi Informatika, Universitas Al Azhar Indonesia. Buku ini hadir di tengah perubahan besar dalam lanskap pendidikan dan teknologi — di mana **data telah menjadi mata uang baru** dan **kecerdasan buatan (AI) telah mengubah cara kita menganalisis informasi**.

Berbeda dari buku statistik konvensional, buku ajar ini dirancang dengan beberapa kekhususan:

1. **Pendekatan Komputasional** — Setiap konsep statistik langsung dipraktikkan dengan Python menggunakan Google Colab, sehingga mahasiswa tidak hanya menghafal rumus tetapi benar-benar memahami proses komputasi di baliknya.

2. **AI sebagai Co-Analyst** — Buku ini mengajarkan cara menggunakan AI (seperti Claude, ChatGPT, dan tools AI lainnya) sebagai mitra analisis data secara bertanggung jawab dan transparan, bukan sebagai pengganti pemikiran kritis.

3. **Konteks Indonesia** — Studi kasus dan dataset yang digunakan berasal dari konteks Indonesia (BPS, Open Data Jakarta, data ekonomi digital Indonesia), sehingga mahasiswa langsung merasakan relevansi statistik dengan kehidupan nyata.

4. **Berbasis OBE (Outcome-Based Education)** — Setiap bab dirancang untuk mencapai Capaian Pembelajaran Mata Kuliah (CPMK) yang jelas dan terukur, sesuai standar SN-Dikti/KKNI.

5. **Nilai-nilai Islami** — Sebagai bagian dari Universitas Al Azhar Indonesia, buku ini menanamkan nilai-nilai amanah, keadilan, dan transparansi dalam setiap aspek analisis data.

Buku ini terdiri dari **13 bab** yang disusun secara progresif — dari fondasi statistika deskriptif hingga frontier machine learning dan AI-augmented analysis. Setiap bab dilengkapi dengan:
- Tujuan pembelajaran yang jelas
- Penjelasan teori dengan bahasa yang mudah dipahami
- Contoh komputasi dengan kode Python yang siap dijalankan
- Studi kasus berbasis data Indonesia
- Latihan soal bertingkat (dasar, menengah, mahir)
- "AI Corner" — panduan interaksi dengan AI untuk topik tersebut

Buku ini dirancang untuk dibaca secara **berurutan** dari Bab 1 hingga Bab 13, karena setiap bab membangun fondasi untuk bab berikutnya. Namun, mahasiswa juga dapat menggunakan bab tertentu sebagai referensi mandiri sesuai kebutuhan.

Semoga buku ajar ini bermanfaat bagi mahasiswa, rekan dosen, dan siapa pun yang ingin mempelajari statistik dengan pendekatan modern. Kritik dan saran sangat kami harapkan untuk perbaikan edisi selanjutnya.

**Wassalamu'alaikum Warahmatullahi Wabarakatuh**

Jakarta, Februari 2025

**Tri Aji Nugroho, S.T., M.T.**
Dosen Pengampu Mata Kuliah Analisis Data Statistik
Program Studi Informatika
Universitas Al Azhar Indonesia

---

### Daftar Isi

| Bab | Judul | Halaman |
|-----|-------|---------|
| — | Halaman Depan | i |
| — | Kata Pengantar | ii |
| — | Daftar Isi | iv |
| — | Daftar Tabel | vi |
| — | Daftar Gambar | vii |
| — | Peta Capaian Pembelajaran | viii |
| **BAGIAN I** | **FONDASI STATISTIKA** | |
| 1 | Pengantar Statistika di Era AI | 1 |
| 2 | Statistika Deskriptif dan Eksplorasi Data dengan Python | 25 |
| 3 | Visualisasi Data dan Data Storytelling | 55 |
| 4 | Probabilitas Dasar dan Teorema Bayes | 85 |
| **BAGIAN II** | **INFERENSI STATISTIK** | |
| 5 | Distribusi Probabilitas dan Central Limit Theorem | 115 |
| 6 | Sampling, Estimasi, dan Bootstrap | 145 |
| 7 | Uji Hipotesis | 175 |
| **BAGIAN III** | **PEMODELAN STATISTIK** | |
| 8 | Korelasi dan Regresi Linear Sederhana | 210 |
| 9 | Regresi Berganda dan Evaluasi Model | 245 |
| 10 | ANOVA dan Uji Non-Parametrik | 275 |
| 11 | Analisis Data Kategorikal | 310 |
| **BAGIAN IV** | **FRONTIER: ML DAN AI** | |
| 12 | Pengantar Machine Learning Statistik | 340 |
| 13 | AI-Augmented Data Analysis | 375 |
| **LAMPIRAN** | | |
| A | Tabel Statistik (Z, t, Chi-Square, F) | 405 |
| B | Formularium Statistik | 415 |
| C | Glosarium Istilah | 425 |
| D | Panduan Instalasi dan Setup Python | 435 |
| E | Daftar Pustaka | 440 |
| F | Indeks | 445 |

---

### Peta Capaian Pembelajaran

```
PROFIL LULUSAN PRODI INFORMATIKA UAI
    │
    ├── CPL-S2  : Menjunjung tinggi nilai-nilai etika dan moral dalam profesi
    ├── CPL-KU2 : Mampu menerapkan pemikiran logis, kritis, dan sistematis
    ├── CPL-KK1 : Menguasai konsep dasar ilmu komputer dan informatika
    ├── CPL-KK3 : Mampu menganalisis data dan informasi
    ├── CPL-P1  : Mampu menggunakan tools pengembangan perangkat lunak
    └── CPL-P3  : Mampu mengaplikasikan ilmu dalam penyelesaian masalah
         │
         ▼
    CAPAIAN PEMBELAJARAN MATA KULIAH (CPMK)
    ┌───────────────────────────────────────────────────────────────────┐
    │ CPMK-1 [C2] Menjelaskan peran statistika dalam data science & AI │
    │   → Bab 1                                                        │
    │                                                                   │
    │ CPMK-2 [C3] Menerapkan statistika deskriptif dan visualisasi     │
    │   → Bab 2, 3                                                     │
    │                                                                   │
    │ CPMK-3 [C3] Menerapkan probabilitas dan distribusi               │
    │   → Bab 4, 5                                                     │
    │                                                                   │
    │ CPMK-4 [C4] Menganalisis data dengan inferensi statistik         │
    │   → Bab 6, 7                                                     │
    │                                                                   │
    │ CPMK-5 [C4-C5] Menganalisis hubungan variabel (regresi)         │
    │   → Bab 8, 9                                                     │
    │                                                                   │
    │ CPMK-6 [C4] Menganalisis data dengan ANOVA & non-parametrik     │
    │   → Bab 10, 11                                                   │
    │                                                                   │
    │ CPMK-7 [C5-C6] Merancang analisis end-to-end dengan AI          │
    │   → Bab 12, 13                                                   │
    └───────────────────────────────────────────────────────────────────┘
```

### Petunjuk Penggunaan Buku

**Untuk Mahasiswa:**
1. Baca setiap bab secara berurutan sebelum perkuliahan (flipped classroom)
2. Jalankan semua kode Python di Google Colab
3. Kerjakan latihan soal di akhir bab secara mandiri sebelum melihat jawaban
4. Gunakan "AI Corner" sebagai panduan untuk berinteraksi dengan AI secara bertanggung jawab
5. Catat pertanyaan dan diskusikan di kelas

**Untuk Dosen:**
1. Buku ini dirancang untuk 16 minggu perkuliahan (2 SKS)
2. Setiap bab dapat diselesaikan dalam 1-2 pertemuan
3. Gunakan bersama RPS, RTM, dan lab manual yang tersedia di repository
4. Latihan soal di buku dapat digunakan sebagai tugas tambahan

**Konvensi Penulisan:**

| Simbol | Makna |
|--------|-------|
| `kode` | Kode Python yang dapat dijalankan |
| **Tebal** | Istilah penting atau konsep kunci |
| *Miring* | Istilah asing atau penekanan |
| > Blockquote | Catatan penting atau tips |
| ⚠️ | Peringatan umum tentang kesalahan yang sering terjadi |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
— Program Studi Informatika, Universitas Al Azhar Indonesia
