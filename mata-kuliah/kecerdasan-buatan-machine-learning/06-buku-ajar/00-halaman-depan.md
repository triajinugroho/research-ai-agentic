# BUKU AJAR

# KECERDASAN BUATAN DAN MACHINE LEARNING
## Fondasi AI/ML dengan Python, scikit-learn, dan TensorFlow

---

### Untuk Mahasiswa Program Studi Informatika

---

**Penulis:**
# Tri Aji Nugroho, S.T., M.T.

---

**Program Studi Informatika**
**Fakultas Sains dan Teknologi**
**Universitas Al Azhar Indonesia**
**Jakarta, 2026**

---

### Identitas Buku

| Komponen | Detail |
|----------|--------|
| **Judul** | Kecerdasan Buatan dan Machine Learning: Fondasi AI/ML dengan Python, scikit-learn, dan TensorFlow |
| **Penulis** | Tri Aji Nugroho, S.T., M.T. |
| **Institusi** | Universitas Al Azhar Indonesia |
| **Fakultas** | Sains dan Teknologi |
| **Program Studi** | Informatika |
| **Edisi** | Pertama, 2026 |
| **Jumlah Bab** | 14 Bab + Lampiran |
| **Sasaran Pembaca** | Mahasiswa S1 Informatika Semester 5 |
| **Pendekatan** | Outcome-Based Education (OBE), AI-Augmented |
| **Bahasa Pemrograman** | Python 3.x |
| **Platform** | Google Colab |

---

### Kata Pengantar

بسم الله الرحمن الرحيم

**Assalamu'alaikum Warahmatullahi Wabarakatuh**

Segala puji bagi Allah SWT yang telah memberikan nikmat ilmu dan kemudahan dalam menyusun buku ajar ini. Shalawat serta salam senantiasa tercurahkan kepada Nabi Muhammad SAW, teladan terbaik dalam menuntut ilmu dan mengamalkannya.

Buku ajar **"Kecerdasan Buatan dan Machine Learning: Fondasi AI/ML dengan Python, scikit-learn, dan TensorFlow"** ini disusun sebagai panduan utama mata kuliah Kecerdasan Buatan dan Machine Learning untuk mahasiswa Program Studi Informatika, Universitas Al Azhar Indonesia. Buku ini hadir di tengah revolusi kecerdasan buatan yang sedang mengubah hampir seluruh aspek kehidupan manusia — di mana **AI telah menjadi teknologi paling transformatif abad ke-21** dan **machine learning menjadi fondasi dari inovasi digital modern**.

Di era di mana ChatGPT, autonomous vehicles, dan sistem rekomendasi telah menjadi bagian dari keseharian, memahami prinsip-prinsip di balik kecerdasan buatan bukan lagi kemewahan — melainkan **kebutuhan fundamental** bagi setiap mahasiswa informatika. Namun, mayoritas buku AI/ML berkualitas ditulis dalam bahasa Inggris dengan konteks Amerika dan Eropa, menciptakan kesenjangan yang signifikan bagi mahasiswa Indonesia.

Berbeda dari buku AI/ML konvensional, buku ajar ini dirancang dengan beberapa kekhususan:

1. **Pendekatan Komputasional End-to-End** — Setiap konsep AI dan machine learning langsung dipraktikkan dengan Python menggunakan scikit-learn dan TensorFlow di Google Colab, sehingga mahasiswa tidak hanya memahami teori tetapi benar-benar mampu membangun model AI yang bekerja.

2. **AI sebagai Mitra Belajar** — Buku ini mengajarkan cara menggunakan Large Language Models (seperti Claude, ChatGPT, dan tools AI lainnya) sebagai mitra belajar AI/ML secara bertanggung jawab dan transparan — sebuah pendekatan meta-learning yang unik: belajar AI *dengan bantuan* AI.

3. **Konteks Indonesia** — Studi kasus dan dataset yang digunakan berasal dari konteks Indonesia (data e-commerce Tokopedia/Shopee, data kesehatan BPJS, data transportasi TransJakarta, data pertanian BPS), sehingga mahasiswa langsung merasakan relevansi AI/ML dengan permasalahan nyata Indonesia.

4. **Berbasis OBE (Outcome-Based Education)** — Setiap bab dirancang untuk mencapai Capaian Pembelajaran Mata Kuliah (CPMK) yang jelas dan terukur, sesuai standar SN-Dikti/KKNI.

5. **Nilai-nilai Islami** — Sebagai bagian dari Universitas Al Azhar Indonesia, buku ini menanamkan nilai-nilai amanah, keadilan, dan tanggung jawab dalam pengembangan dan penerapan teknologi AI — termasuk diskusi mendalam tentang etika AI dari perspektif Islam.

Buku ini terdiri dari **14 bab** yang disusun secara progresif — dari fondasi kecerdasan buatan hingga frontier applied AI dan proyek akhir. Setiap bab dilengkapi dengan:
- Tujuan pembelajaran yang jelas
- Penjelasan teori dengan bahasa yang mudah dipahami
- Contoh komputasi dengan kode Python yang siap dijalankan
- Studi kasus berbasis data Indonesia
- Latihan soal bertingkat (dasar, menengah, mahir)
- "AI Corner" — panduan interaksi dengan AI untuk topik tersebut

Buku ini dirancang untuk dibaca secara **berurutan** dari Bab 1 hingga Bab 14, karena setiap bab membangun fondasi untuk bab berikutnya. Namun, mahasiswa juga dapat menggunakan bab tertentu sebagai referensi mandiri sesuai kebutuhan.

Semoga buku ajar ini bermanfaat bagi mahasiswa, rekan dosen, dan siapa pun yang ingin mempelajari kecerdasan buatan dan machine learning dengan pendekatan yang komprehensif, kontekstual, dan beretika. Kritik dan saran sangat kami harapkan untuk perbaikan edisi selanjutnya.

**Wassalamu'alaikum Warahmatullahi Wabarakatuh**

Jakarta, Agustus 2026

**Tri Aji Nugroho, S.T., M.T.**
Dosen Pengampu Mata Kuliah Kecerdasan Buatan dan Machine Learning
Program Studi Informatika
Universitas Al Azhar Indonesia

---

### Daftar Isi

| Bab | Judul | Halaman |
|-----|-------|---------|
| — | Halaman Depan | i |
| — | Kata Pengantar | ii |
| — | Mengapa Buku Ini? — Positioning dan Keunggulan | iv |
| — | Daftar Isi | vi |
| — | Daftar Tabel | viii |
| — | Daftar Gambar | ix |
| — | Peta Capaian Pembelajaran | x |
| **BAGIAN I** | **FONDASI AI** | |
| 1 | Pengantar Kecerdasan Buatan: Sejarah, Definisi, dan Lanskap Modern | 1 |
| 2 | Matematika untuk Machine Learning: Aljabar Linear, Kalkulus, dan Probabilitas | 30 |
| 3 | Eksplorasi Data dan Preprocessing untuk ML | 65 |
| 4 | Fondasi Machine Learning: Konsep, Tipe, dan Workflow | 100 |
| **BAGIAN II** | **SUPERVISED LEARNING** | |
| 5 | Regresi: Linear, Polynomial, dan Regularisasi | 135 |
| 6 | Klasifikasi: Logistic Regression, KNN, dan Naive Bayes | 170 |
| 7 | Ensemble Methods: Decision Tree, Random Forest, dan Gradient Boosting | 210 |
| **BAGIAN III** | **ADVANCED MACHINE LEARNING** | |
| 8 | Unsupervised Learning: Clustering dan Dimensionality Reduction | 250 |
| 9 | Neural Networks dan Deep Learning Fundamentals | 290 |
| 10 | Model Evaluation, Hyperparameter Tuning, dan MLOps Dasar | 330 |
| **BAGIAN IV** | **APPLIED AI & FRONTIER** | |
| 11 | Natural Language Processing (NLP) dengan Python | 370 |
| 12 | Computer Vision dan Convolutional Neural Networks | 410 |
| 13 | AI-Augmented Development dan Responsible AI | 450 |
| 14 | Proyek Akhir: Membangun Solusi AI End-to-End untuk Masalah Indonesia | 490 |
| — | **Penutup: Refleksi dan Langkah ke Depan** | 530 |
| **LAMPIRAN** | | |
| A | Instalasi dan Setup Python / Google Colab | 540 |
| B | Daftar Library Python yang Digunakan | 548 |
| C | Template AI Usage Log | 555 |
| D | Panduan Penggunaan AI secara Bertanggung Jawab | 560 |
| E | Glosarium Istilah AI/ML | 570 |
| F | Referensi Dataset Indonesia untuk ML | 585 |
| G | Cheat Sheet scikit-learn API | 590 |
| H | Cheat Sheet Keras API | 600 |

---

### Peta Capaian Pembelajaran

```
PROFIL LULUSAN PRODI INFORMATIKA UAI
    │
    ├── CPL-S2  : Menjunjung tinggi nilai-nilai etika dan moral dalam profesi
    ├── CPL-KU2 : Mampu menerapkan pemikiran logis, kritis, dan sistematis
    ├── CPL-KK1 : Menguasai konsep dasar ilmu komputer dan informatika
    ├── CPL-KK4 : Mampu merancang dan mengembangkan sistem cerdas
    ├── CPL-P1  : Mampu menggunakan tools pengembangan perangkat lunak
    └── CPL-P3  : Mampu mengaplikasikan ilmu dalam penyelesaian masalah
         │
         ▼
    CAPAIAN PEMBELAJARAN MATA KULIAH (CPMK)
    ┌───────────────────────────────────────────────────────────────────┐
    │ CPMK-1 [C2] Menjelaskan konsep dasar AI, sejarah, dan           │
    │   paradigma machine learning                                     │
    │   → Bab 1, 2                                                     │
    │                                                                   │
    │ CPMK-2 [C3] Menerapkan teknik preprocessing data dan             │
    │   eksplorasi data untuk pipeline ML                              │
    │   → Bab 3, 4                                                     │
    │                                                                   │
    │ CPMK-3 [C3-C4] Menerapkan dan menganalisis algoritma             │
    │   supervised learning (regresi dan klasifikasi)                   │
    │   → Bab 5, 6, 7                                                  │
    │                                                                   │
    │ CPMK-4 [C4] Menganalisis dan menerapkan algoritma                │
    │   unsupervised learning dan neural networks                      │
    │   → Bab 8, 9                                                     │
    │                                                                   │
    │ CPMK-5 [C5] Mengevaluasi performa model ML dan melakukan         │
    │   hyperparameter tuning                                          │
    │   → Bab 10                                                       │
    │                                                                   │
    │ CPMK-6 [C4-C5] Menganalisis dan mengevaluasi aplikasi AI         │
    │   pada domain NLP dan computer vision                            │
    │   → Bab 11, 12                                                   │
    │                                                                   │
    │ CPMK-7 [C5-C6] Merancang solusi AI end-to-end yang               │
    │   bertanggung jawab dengan konteks Indonesia                     │
    │   → Bab 13, 14                                                   │
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
1. Buku ini dirancang untuk 16 minggu perkuliahan (2 SKS), termasuk proyek akhir
2. Setiap bab dapat diselesaikan dalam 1-2 pertemuan; Bab 14 (Proyek Akhir) berjalan paralel di minggu 13-16
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
