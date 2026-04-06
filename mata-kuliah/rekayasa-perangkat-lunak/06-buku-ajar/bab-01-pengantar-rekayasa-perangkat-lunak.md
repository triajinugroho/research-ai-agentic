# BAB 1: PENGANTAR REKAYASA PERANGKAT LUNAK

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 1.1 | Menjelaskan definisi rekayasa perangkat lunak dan perbedaannya dengan programming | C2 (Memahami) |
| 1.2 | Mengidentifikasi faktor software crisis dan SWEBOK v4 Knowledge Areas serta etika profesi | C2 (Memahami) |

---

## 1.1 Apa Itu Rekayasa Perangkat Lunak?

### 1.1.1 Definisi

> **Rekayasa Perangkat Lunak** (*Software Engineering*) adalah penerapan pendekatan yang **sistematis, disiplin, dan terukur** terhadap pengembangan, pengoperasian, dan pemeliharaan perangkat lunak (IEEE, 2024).

Istilah ini pertama kali muncul pada **Konferensi NATO 1968** di Garmisch, Jerman — ketika komunitas computing menyadari bahwa membangun software berskala besar memerlukan pendekatan engineering, bukan sekadar programming.

### 1.1.2 Software Engineering vs Programming

```
┌─────────────────────────────────────────────────────┐
│ Software Engineering                                 │
│  ┌─────────────────────────────────────────┐        │
│  │ Requirements → Design → Construction →   │        │
│  │ Testing → Deployment → Maintenance       │        │
│  │                                          │        │
│  │  ┌──────────────┐                       │        │
│  │  │ Programming  │ ← hanya satu fase!    │        │
│  │  └──────────────┘                       │        │
│  └─────────────────────────────────────────┘        │
│ + Project Management + Quality Assurance + Ethics    │
└─────────────────────────────────────────────────────┘
```

| Aspek | Programming | Software Engineering |
|-------|-------------|---------------------|
| Fokus | Menulis kode | Seluruh lifecycle |
| Skala | Individual/kecil | Tim, sistem besar |
| Proses | Ad-hoc | Sistematis, terukur |
| Kualitas | "Jalan dulu" | Reliable, maintainable |
| Dokumentasi | Minimal | Terstruktur (SRS, UML) |

### 1.1.3 Mengapa Software Engineering Penting?

Software ada di mana-mana: dari aplikasi ojek online yang kita gunakan setiap hari, sistem perbankan yang memproses jutaan transaksi, hingga sistem kontrol pesawat yang menyangkut keselamatan jiwa.

**Fakta penting:**
- Hanya **~30% proyek software berhasil** sepenuhnya (Standish Group CHAOS Report)
- **60% kegagalan** disebabkan oleh requirements yang buruk
- Biaya perbaikan bug meningkat **100x** jika ditemukan setelah deployment

## 1.2 Software Crisis dan Sejarahnya

### 1.2.1 Apa Itu Software Crisis?

Software crisis merujuk pada fenomena di tahun 1960-an ketika proyek software secara konsisten mengalami:
- **Terlambat** dari jadwal
- **Over-budget** dari anggaran
- **Buggy** dan tidak reliable
- **Tidak sesuai** dengan kebutuhan pengguna

### 1.2.2 Contoh Kegagalan Terkenal

| Kasus | Tahun | Dampak | Pelajaran |
|-------|-------|--------|-----------|
| Ariane 5 | 1996 | Roket meledak 37 detik setelah peluncuran | Integer overflow — pentingnya testing |
| Healthcare.gov | 2013 | Website gagal melayani jutaan pengguna | Arsitektur tidak scalable, testing minim |
| Boeing 737 MAX MCAS | 2018-2019 | 346 korban jiwa | Software safety-critical, ethical responsibility |
| Knight Capital | 2012 | Kerugian $440 juta dalam 45 menit | Deployment tanpa testing memadai |

### 1.2.3 Warisan Muslim dalam Ilmu Komputer

Sebagai mahasiswa di universitas Islam, penting mengetahui kontribusi peradaban Islam:

- **Al-Khwarizmi** (780-850 M): Bapak Algoritma — kata "algorithm" berasal dari nama beliau. Kitab *Al-Jabr wa al-Muqabala* menjadi fondasi aljabar dan computational thinking.
- **Al-Jazari** (1136-1206 M): Insinyur mekanik yang merancang automata dan mesin otomatis — cikal bakal konsep automation yang menjadi inti DevOps modern.
- **Ibn al-Haytham** (965-1040 M): Bapak Scientific Method — pendekatan empiris dan eksperimental yang menjadi dasar software testing.

## 1.3 SWEBOK v4 (2024)

### 1.3.1 Apa Itu SWEBOK?

**SWEBOK** (*Software Engineering Body of Knowledge*) adalah dokumen referensi yang mendefinisikan body of knowledge untuk profesi software engineering, diterbitkan oleh IEEE Computer Society.

SWEBOK v4 (2024) mendefinisikan **15 Knowledge Areas**:

| No | Knowledge Area | Deskripsi | Relevansi Kuliah Ini |
|----|---------------|-----------|---------------------|
| 1 | Software Requirements | Elicitation, analysis, specification | Minggu 3-4 |
| 2 | Software Design | Architecture, detailed design, patterns | Minggu 5-6 |
| 3 | Software Construction | Coding, debugging, code review | Minggu 7 |
| 4 | Software Testing | Levels, techniques, automation | Minggu 9-10 |
| 5 | Software Maintenance | Corrective, adaptive, perfective | Minggu 12 |
| 6 | Software Configuration Mgmt | Version control, change management | Minggu 7 |
| 7 | SE Management | Planning, measurement, risk | Minggu 12 |
| 8 | SE Process | Process models, improvement | Minggu 2 |
| 9 | SE Models & Methods | Modeling, formal methods | Minggu 5-6 |
| 10 | Software Quality | QA, metrics, standards | Minggu 9-10 |
| 11 | SE Professional Practice | Ethics, economics, teamwork | Minggu 1, 14 |
| 12 | SE Economics | Cost estimation, value | Minggu 12 |
| 13 | Computing Foundations | Algorithms, data structures | Prasyarat |
| 14 | Mathematical Foundations | Logic, discrete math | Prasyarat |
| 15 | Engineering Foundations | Empirical methods, design | Sepanjang semester |

## 1.4 Mengapa Belajar SE di Era AI?

AI generatif (ChatGPT, Claude, Copilot) bisa generate code. Lalu mengapa masih perlu belajar SE?

| AI Bisa | SE Tetap Dibutuhkan |
|---------|---------------------|
| Generate code dari prompt | Memahami kebutuhan stakeholder yang ambigu |
| Suggest code completion | Merancang arsitektur yang scalable & maintainable |
| Detect bugs dalam code | Memutuskan trade-off design (security vs performance) |
| Generate unit tests | Memastikan software memenuhi kebutuhan bisnis |
| Explain code | Mengelola tim dan proses pengembangan |
| Refactor code | Bertanggung jawab atas kualitas dan etika software |

**Kesimpulan:** AI adalah **tool**, bukan pengganti engineer. Software engineer yang mahir menggunakan AI akan jauh lebih produktif — tetapi mereka tetap perlu memahami fondasi SE.

## 1.5 Etika Profesi Software Engineer

### 1.5.1 ACM/IEEE Code of Ethics

ACM dan IEEE bersama menerbitkan **Software Engineering Code of Ethics** dengan 8 prinsip utama:

1. **PUBLIC** — Bertindak sesuai kepentingan publik
2. **CLIENT & EMPLOYER** — Bertindak demi kepentingan klien dengan tetap menjaga kepentingan publik
3. **PRODUCT** — Memastikan produk memenuhi standar profesional tertinggi
4. **JUDGMENT** — Menjaga integritas dan independensi profesional
5. **MANAGEMENT** — Mengelola pengembangan secara etis
6. **PROFESSION** — Memajukan integritas dan reputasi profesi
7. **COLLEAGUES** — Berlaku adil dan mendukung rekan sejawat
8. **SELF** — Terus belajar dan mengembangkan diri

### 1.5.2 Perspektif Islam dalam Etika SE

- **Amanah** (الأمانة): Kode yang ditulis harus jujur — tidak menyembunyikan bug, tidak memanipulasi data pengguna, menjaga kepercayaan stakeholder
- **Keadilan (Al-'Adl)**: Software harus accessible dan fair untuk semua pengguna — tidak diskriminatif, memperhatikan inclusivity
- **Ihsan** (الإحسان): Berusaha menulis kode yang excellent — clean code sebagai bentuk ihsan, memberikan yang terbaik meskipun tidak diminta

### 1.5.3 Studi Kasus Etika

**Kasus: Algoritma Diskriminatif**
Sebuah sistem AI untuk seleksi karyawan ternyata bias terhadap gender tertentu karena data training yang tidak representatif. Bagaimana seorang software engineer seharusnya merespons?

- Sebagai engineer yang amanah: melaporkan temuan meskipun sulit
- Sebagai engineer yang adil: memperbaiki bias dan memastikan fairness
- Sebagai engineer yang ihsan: proaktif melakukan audit sebelum deployment

---

## AI Corner: Pengenalan AI untuk SE (Level: Basic)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| Memahami konsep SE | "Jelaskan perbedaan software engineering dan programming dengan analogi konstruksi bangunan" | Bandingkan jawaban AI dengan materi kuliah |
| Eksplorasi SWEBOK | "Sebutkan 15 Knowledge Areas SWEBOK v4 dan berikan contoh masing-masing" | Verifikasi dengan dokumen resmi IEEE |
| Diskusi etika | "Berikan contoh dilema etika yang dihadapi software engineer" | AI bisa memberikan perspektif, tapi keputusan tetap di tangan engineer |

**Aturan AI di kuliah ini:**
- AI diizinkan sebagai **learning partner** untuk tugas (wajib AI Usage Log)
- AI **TIDAK diizinkan** untuk ujian (UTS/UAS) dan kuis
- Selalu verifikasi output AI — AI bisa hallucinate

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Jelaskan definisi rekayasa perangkat lunak menurut IEEE.
2. Sebutkan 5 perbedaan antara programming dan software engineering.
3. Apa yang dimaksud dengan "software crisis"? Berikan 2 contoh kasus.
4. Sebutkan 5 dari 15 Knowledge Areas dalam SWEBOK v4.

### Level Menengah (C3-C4)
5. Mengapa pendekatan systematic diperlukan dalam pengembangan software berskala besar? Berikan analogi dengan disiplin engineering lain.
6. Analisis kasus Boeing 737 MAX dari perspektif software engineering — apa yang bisa diperbaiki?
7. Bandingkan peran software engineer di era sebelum dan sesudah AI generatif.

### Level Mahir (C5-C6)
8. Seorang klien meminta Anda membangun fitur yang menurut Anda melanggar privasi pengguna. Bagaimana Anda merespons berdasarkan ACM Code of Ethics dan nilai Islam?
9. Rancang proposal singkat bagaimana SWEBOK v4 bisa dijadikan framework untuk mengaudit kualitas proyek software di startup Indonesia.

---

## Rangkuman

1. **Rekayasa Perangkat Lunak** adalah pendekatan sistematis, disiplin, dan terukur untuk seluruh lifecycle software — bukan sekadar programming.
2. **Software crisis** (1968) mendorong lahirnya SE sebagai disiplin ilmu untuk mengatasi proyek yang gagal.
3. **SWEBOK v4** (2024) mendefinisikan 15 Knowledge Areas yang menjadi body of knowledge profesi SE.
4. Di **era AI**, SE tetap krusial — AI adalah tool, bukan pengganti engineer yang memahami kebutuhan, arsitektur, dan etika.
5. **Etika profesi** berdasarkan ACM/IEEE Code of Ethics dan nilai Islam (amanah, keadilan, ihsan) menjadi fondasi praktik SE yang bertanggung jawab.
6. **Al-Khwarizmi** menginspirasi kata "algorithm" — peradaban Islam memiliki kontribusi besar dalam fondasi ilmu komputer.

---

## Referensi

1. IEEE Computer Society. (2024). *SWEBOK v4: Guide to the Software Engineering Body of Knowledge*. IEEE.
2. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 1. Pearson.
3. ACM/IEEE. (2015). *Software Engineering Code of Ethics and Professional Practice*.
4. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). Chapter 1.
5. Standish Group. (2020). *CHAOS Report 2020*. The Standish Group International.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
