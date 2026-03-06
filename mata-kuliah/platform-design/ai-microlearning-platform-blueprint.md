# NusaBelajar: AI-Powered Micro-Learning Platform Blueprint

## Platform Visi & Misi Pembelajaran Cerdas untuk Indonesia

**Versi:** 1.0
**Tanggal:** Maret 2026
**Penyusun:** Tri Aji Nugroho, S.T., M.T.
**Institusi Asal:** Program Studi Informatika, Universitas Al Azhar Indonesia

---

## Daftar Isi

1. [Ringkasan Eksekutif](#1-ringkasan-eksekutif)
2. [Fondasi Ilmu Pembelajaran](#2-fondasi-ilmu-pembelajaran)
3. [Arsitektur Konten Micro-Learning](#3-arsitektur-konten-micro-learning)
4. [AI-Powered Adaptive Learning Engine](#4-ai-powered-adaptive-learning-engine)
5. [Engagement & Gamifikasi](#5-engagement--gamifikasi)
6. [Asesmen & Feedback Loop](#6-asesmen--feedback-loop)
7. [Arsitektur Teknis Platform](#7-arsitektur-teknis-platform)
8. [Integrasi Nilai Islami & Konteks Indonesia](#8-integrasi-nilai-islami--konteks-indonesia)
9. [Roadmap Implementasi](#9-roadmap-implementasi)

---

## 1. Ringkasan Eksekutif

### 1.1 Masalah yang Diselesaikan

Pendidikan Informatika di Indonesia menghadapi tiga tantangan kritis:

1. **Engagement Gap** — Mahasiswa menghadiri kuliah 150 menit tetapi hanya aktif belajar ~30% waktu. Materi textbook ribuan baris jarang dibaca tuntas.
2. **Retention Gap** — Tanpa spaced repetition, 80% materi dilupakan dalam 1 minggu (Ebbinghaus, 1885). Mahasiswa belajar SKS (*Sistem Kebut Semalam*) menjelang ujian.
3. **Personalization Gap** — Semua mahasiswa mendapat materi yang sama dengan kecepatan yang sama, padahal kemampuan awal dan kecepatan belajar sangat bervariasi.

### 1.2 Solusi: NusaBelajar

**NusaBelajar** adalah platform micro-learning berbasis AI yang mentransformasi 179+ dokumen Markdown (4 mata kuliah Informatika) menjadi **~1.200 nugget pembelajaran** berdurasi 5-10 menit, dilengkapi:

- **Adaptive Learning Engine** yang menyesuaikan jalur belajar per individu
- **AI Tutor** berbasis Claude/ChatGPT dengan konteks spesifik per nugget
- **Spaced Repetition System** untuk retensi jangka panjang
- **Interactive Coding** dengan feedback instan (bukan blok kode statis)
- **Gamifikasi** yang bermakna, terhubung ke capaian pembelajaran (CPMK)

### 1.3 Target Audiens

| Segmen | Deskripsi |
|--------|-----------|
| **Primer** | Mahasiswa Informatika seluruh Indonesia yang mempelajari Algoritma, Statistik, dan AI/ML |
| **Sekunder** | Profesional yang ingin reskilling/upskilling ke bidang AI dan Data Science |
| **Tersier** | Self-learner yang ingin belajar CS fundamental dalam bahasa Indonesia |

### 1.4 Diferensiasi Unik

| Aspek | Platform Lain (Coursera, Dicoding) | NusaBelajar |
|-------|-------------------------------------|-------------|
| Bahasa | Inggris / subtitle | Native Indonesian + bilingual technical terms |
| Konten | Video panjang (30-60 min) | Micro-nugget (5-10 min), multi-modal |
| Adaptivitas | Linear path | AI-adaptive per learner |
| Konteks | Global/Western examples | Indonesian datasets, BPS data, local case studies |
| Assessment | End-of-module quiz | Micro-assessment setiap nugget + spaced review |
| Coding | Passive video watching | Interactive coding dengan instant feedback |
| Pedagogik | Generic | OBE-aligned, CPMK-traceable, Bloom's-leveled |
| Nilai | Secular | Islamic values integrated naturally |

---

## 2. Fondasi Ilmu Pembelajaran

Setiap fitur platform didasarkan pada riset pembelajaran (learning science) yang tervalidasi. Berikut tujuh prinsip utama dan implementasinya:

### 2.1 Spaced Repetition (Pengulangan Berjarak)

**Basis riset:** Ebbinghaus Forgetting Curve (1885), Pimsleur (1967), SuperMemo SM-2 (Wozniak, 1987)

**Prinsip:** Informasi yang di-review pada interval yang semakin panjang (1 hari → 3 hari → 7 hari → 14 hari → 30 hari) bertahan jauh lebih lama dalam memori jangka panjang.

**Implementasi di NusaBelajar:**
- Setiap nugget yang selesai dipelajari masuk ke **Review Queue** pribadi
- Algoritma SM-2 yang dimodifikasi menentukan kapan nugget perlu di-review
- Review berbentuk **flashcard konsep** + **mini coding challenge** (bukan mengulang nugget penuh)
- Dashboard menampilkan "Strength Meter" per konsep (0-100%)
- Notifikasi harian: "5 konsep perlu di-review hari ini" (estimasi 10-15 menit)

**Penjadwalan interval:**

```
Jika jawaban benar dan mudah:   interval × 2.5
Jika jawaban benar tapi ragu:   interval × 1.5
Jika jawaban salah:             reset ke 1 hari
```

### 2.2 Active Recall (Pemanggilan Aktif)

**Basis riset:** Testing Effect (Roediger & Karpicke, 2006)

**Prinsip:** Mengingat informasi secara aktif (tanpa melihat catatan) jauh lebih efektif daripada membaca ulang. Tes bukan hanya alat pengukuran — tes adalah alat pembelajaran.

**Implementasi:**
- Setiap nugget **diakhiri** dengan 2-3 pertanyaan recall (bukan di-skip)
- Pertanyaan muncul **sebelum** jawaban terungkap (retrieval practice)
- Format beragam: pilihan ganda, isi kode, drag-and-drop flowchart, jelaskan-dengan-kata-sendiri
- AI Tutor bisa diminta untuk "quiz me" kapan saja

### 2.3 Interleaving (Pencampuran Topik)

**Basis riset:** Rohrer & Taylor (2007), Kornell & Bjork (2008)

**Prinsip:** Mencampur topik berbeda dalam satu sesi belajar (ABCABC) lebih efektif daripada blocking (AABBCC), meskipun terasa lebih sulit.

**Implementasi:**
- Mode **"Daily Mix"** menyajikan 5-7 nugget dari topik berbeda
- Review session mencampur konsep dari berbagai minggu dan mata kuliah
- Contoh: sesi 20 menit bisa berisi: 1 nugget sorting baru + 1 review list comprehension + 1 review probabilitas
- Cross-course connections: "Kamu baru belajar linear regression di AI/ML — ini relevan dengan materi statistik inferensi"

### 2.4 Elaborative Interrogation (Pertanyaan Elaboratif)

**Basis riset:** Pressley et al. (1987), Chi et al. (1994)

**Prinsip:** Bertanya "mengapa?" dan "bagaimana?" saat belajar meningkatkan pemahaman mendalam dibandingkan hanya membaca fakta.

**Implementasi:**
- AI Tutor secara proaktif bertanya: *"Mengapa binary search memerlukan data terurut? Apa yang terjadi jika tidak?"*
- Setiap nugget konsep memiliki **"Pertanyaan Pemicu"** di awal (bukan di akhir)
- Reflection prompts: *"Jelaskan konsep ini seolah-olah kamu menjelaskan ke teman yang belum paham"*
- AI mendeteksi jawaban superfisial dan meminta elaborasi

### 2.5 Dual Coding (Pengkodean Ganda)

**Basis riset:** Paivio (1986), Mayer's Multimedia Learning Theory (2001)

**Prinsip:** Informasi yang disajikan dalam dua format (verbal + visual) diingat lebih baik daripada satu format saja.

**Implementasi:**
- Setiap konsep abstrak disertai **diagram visual** (flowchart, ASCII art, animated visualization)
- Kode Python selalu berpasangan dengan **execution trace visual** (step-by-step visualization)
- Algoritma sorting/searching ditampilkan dengan **animasi langkah-per-langkah**
- Pilihan mode: "Baca penjelasan" vs "Lihat diagram" vs "Keduanya"

### 2.6 Desirable Difficulty (Kesulitan yang Diinginkan)

**Basis riset:** Bjork & Bjork (2011)

**Prinsip:** Belajar yang terasa sedikit sulit (tapi tidak terlalu sulit) menghasilkan retensi terbaik. Zona optimal: 85% success rate (Wilson et al., 2019).

**Implementasi:**
- Adaptive difficulty: jika mahasiswa menjawab 3 soal berturut-turut benar → naikkan difficulty
- Jika gagal 2 berturut-turut → turunkan difficulty dan sajikan scaffolding
- Target: setiap learner berada di **Zone of Proximal Development** (Vygotsky)
- Hint system bertingkat: Hint 1 (petunjuk arah) → Hint 2 (setengah solusi) → Hint 3 (solusi lengkap dengan penjelasan)

### 2.7 Concrete Examples (Contoh Konkret)

**Basis riset:** Rawson et al. (2015), Analogy-based learning

**Prinsip:** Konsep abstrak jauh lebih mudah dipahami ketika disertai contoh konkret yang familiar.

**Implementasi:**
- Setiap konsep memiliki minimal 2 contoh: 1 konteks kehidupan sehari-hari + 1 konteks coding
- Semua contoh menggunakan **konteks Indonesia**: antrian TransJakarta (queue), data BPS (statistics), e-commerce Tokopedia (sorting)
- **"Analogi Box"** di setiap nugget: *"Dictionary di Python itu seperti buku telepon — kamu cari nama (key) untuk menemukan nomor (value)"*

### 2.8 Mapping Prinsip → Fitur Platform

| Prinsip | Fitur Utama | Metrik Keberhasilan |
|---------|-------------|---------------------|
| Spaced Repetition | Review Queue + SM-2 scheduler | Retention rate ≥80% setelah 30 hari |
| Active Recall | Micro-quiz setiap nugget | Quiz completion rate ≥90% |
| Interleaving | Daily Mix mode | Cross-topic transfer accuracy |
| Elaborative Interrogation | AI Tutor proactive questions | Depth of explanation score |
| Dual Coding | Visual + verbal setiap konsep | Comprehension test improvement |
| Desirable Difficulty | Adaptive difficulty engine | Learner di 80-90% success zone |
| Concrete Examples | Indonesian context examples | Relatability survey score |

---

## 3. Arsitektur Konten Micro-Learning

### 3.1 Strategi Dekomposisi

Setiap modul kuliah 150 menit didekomposisi menjadi **8-12 nugget** berdurasi 5-10 menit. Prinsip dekomposisi:

**Aturan Satu Konsep:** Setiap nugget mengajarkan tepat SATU konsep atau keterampilan. Jika perlu lebih dari 10 menit untuk menjelaskan, pecah lagi.

**Taksonomi Nugget:**

| Tipe | Kode | Durasi | Deskripsi | Rasio per Modul |
|------|------|--------|-----------|-----------------|
| **Concept** | `C` | 5-8 min | Penjelasan teori/konsep dengan dual coding | 30% |
| **Example** | `E` | 5-7 min | Contoh konkret dengan walkthrough | 20% |
| **Code-Along** | `A` | 8-10 min | Live coding interaktif step-by-step | 20% |
| **Practice** | `P` | 5-10 min | Latihan mandiri dengan hint system | 15% |
| **Quiz** | `Q` | 3-5 min | Micro-assessment (2-3 soal) | 10% |
| **Reflection** | `R` | 3-5 min | Elaborative interrogation + self-assessment | 5% |

**Pola sekuens standar per konsep:**

```
C → E → A → P → Q
(Concept → Example → Code-Along → Practice → Quiz)
```

### 3.2 Konvensi Penamaan Nugget

```
nugget-{COURSE}-{WEEK}-{SEQ}-{TYPE}-{TOPIC-SLUG}.md
```

| Komponen | Format | Contoh |
|----------|--------|--------|
| COURSE | `alp` (Algoritma), `pap` (Praktikum), `ads` (Statistik), `aiml` (AI/ML) | `alp` |
| WEEK | `WW` (2 digit) | `01` |
| SEQ | `NN` (2 digit, urutan dalam minggu) | `03` |
| TYPE | `concept`, `example`, `codealong`, `practice`, `quiz`, `reflection` | `concept` |
| TOPIC-SLUG | kebab-case Indonesian | `apa-itu-algoritma` |

**Contoh lengkap:** `nugget-alp-01-01-concept-apa-itu-algoritma.md`

### 3.3 Struktur Folder

```
mata-kuliah/
├── platform-design/              # Blueprint & schemas (file ini)
│
├── nuggets/                      # Semua micro-lessons
│   ├── alp/                      # Algoritma dan Pemrograman
│   │   ├── week-01/
│   │   │   ├── nugget-alp-01-01-concept-apa-itu-algoritma.md
│   │   │   ├── nugget-alp-01-02-example-algoritma-kehidupan.md
│   │   │   ├── nugget-alp-01-03-concept-computational-thinking.md
│   │   │   ├── nugget-alp-01-04-practice-dekomposisi-masalah.md
│   │   │   ├── nugget-alp-01-05-concept-representasi-algoritma.md
│   │   │   ├── nugget-alp-01-06-codealong-pseudocode-flowchart.md
│   │   │   ├── nugget-alp-01-07-concept-pengenalan-python.md
│   │   │   ├── nugget-alp-01-08-codealong-hello-world-colab.md
│   │   │   ├── nugget-alp-01-09-practice-flowchart-dasar.md
│   │   │   └── nugget-alp-01-10-quiz-minggu-01.md
│   │   ├── week-02/
│   │   │   └── ...
│   │   └── week-16/
│   │
│   ├── pap/                      # Praktikum
│   ├── ads/                      # Analisis Data Statistik
│   └── aiml/                     # AI & Machine Learning
│
├── knowledge-graph/              # Graf pengetahuan
│   ├── nodes.json                # Semua konsep
│   ├── edges.json                # Relasi antar konsep
│   └── cross-course-map.json    # Koneksi lintas mata kuliah
│
├── assessments/                  # Bank soal platform
│   ├── alp/
│   │   ├── week-01-items.json
│   │   └── ...
│   └── ...
│
└── gamification/                 # Konfigurasi gamifikasi
    ├── badges.json
    ├── levels.json
    └── challenges.json
```

### 3.4 Metadata Frontmatter Nugget

Setiap nugget memiliki YAML frontmatter berisi metadata lengkap. Schema lengkap ada di `schemas/nugget-schema.yaml`.

```yaml
---
id: "nugget-alp-01-01"
title: "Apa Itu Algoritma?"
course: "alp"                     # alp | pap | ads | aiml
week: 1
sequence: 1
type: "concept"                   # concept | example | codealong | practice | quiz | reflection
topic_slug: "apa-itu-algoritma"

# Pedagogical metadata
cpmk: ["CPMK-1"]
sub_cpmk: ["CPMK-1.1"]
bloom_level: "C1"                 # C1-C6
difficulty: 1                     # 1 (pemula) - 5 (mahir)
estimated_minutes: 6

# Prerequisites & connections
prerequisites: []                 # nugget IDs yang harus selesai dulu
related: ["nugget-alp-01-02", "nugget-alp-01-03"]
cross_course: []                  # koneksi ke nugget mata kuliah lain

# Content metadata
modality: ["text", "diagram"]     # text | diagram | code | animation | audio
has_interactive_code: false
has_quiz: false
quiz_count: 0

# Spaced repetition
review_priority: "high"           # high | medium | low
key_concepts:                     # konsep untuk flashcard review
  - "Definisi algoritma"
  - "5 karakteristik algoritma"
  - "Al-Khwarizmi sebagai bapak algoritma"

# Tags
tags: ["algoritma", "pengantar", "computational-thinking", "sejarah"]
---
```

### 3.5 Estimasi Volume Konten

| Mata Kuliah | Minggu Aktif | Nugget/Minggu | Total Nugget |
|-------------|--------------|---------------|--------------|
| Algoritma & Pemrograman (ALP) | 14 | 10 | ~140 |
| Praktikum ALP (PAP) | 13 | 8 | ~104 |
| Analisis Data Statistik (ADS) | 14 | 10 | ~140 |
| AI & Machine Learning (AIML) | 14 | 12 | ~168 |
| **TOTAL** | | | **~552 nugget** |

Ditambah **review nuggets** dan **cross-course bridges**: **~650 nugget** total.

Ditambah **assessment items** (3 per nugget average): **~1.950 soal**.

### 3.6 Knowledge Graph

Knowledge Graph menghubungkan semua konsep across 4 mata kuliah. Setiap node adalah satu konsep, setiap edge adalah relasi.

**Tipe Node:**

| Tipe | Deskripsi | Contoh |
|------|-----------|--------|
| `concept` | Konsep teoritis | "Algoritma", "Big-O Notation" |
| `skill` | Keterampilan praktis | "Menulis for loop", "Membangun model regresi" |
| `tool` | Tool/library | "Python", "scikit-learn", "pandas" |

**Tipe Edge:**

| Tipe | Deskripsi | Contoh |
|------|-----------|--------|
| `prerequisite` | A harus dikuasai sebelum B | variabel → ekspresi |
| `builds_on` | B memperdalam A | linear search → binary search |
| `related` | Terkait tapi tidak bersyarat | list comprehension ↔ lambda function |
| `applies_in` | Konsep A dipakai di mata kuliah B | statistik deskriptif → EDA untuk ML |
| `contrasts` | Konsep yang sering dibandingkan | list vs tuple, BFS vs DFS |

**Cross-Course Bridges (contoh penting):**

```
ALP: Variabel & Tipe Data ──applies_in──→ ADS: Tipe Data Statistik
ALP: List & Dictionary ──applies_in──→ ADS: DataFrame Pandas
ALP: Fungsi & Modularitas ──applies_in──→ AIML: Pipeline sklearn
ADS: Regresi Linear ──builds_on──→ AIML: Supervised Learning
ADS: Probabilitas ──applies_in──→ AIML: Naive Bayes
ADS: Uji Hipotesis ──applies_in──→ AIML: Model Evaluation
ALP: Sorting Algorithms ──contrasts──→ AIML: Algorithm Complexity
ALP: Rekursi ──builds_on──→ AIML: Decision Tree (recursive splitting)
```

---

## 4. AI-Powered Adaptive Learning Engine

### 4.1 Learner Profile Model

Setiap learner memiliki profil komprehensif yang terus diperbarui. Schema lengkap: `schemas/learner-profile-schema.json`.

**Komponen utama:**

```
Learner Profile
├── Identity (nama, institusi, semester)
├── Knowledge State
│   ├── Per Sub-CPMK mastery level (0.0 - 1.0)
│   ├── Per concept strength (dari spaced repetition)
│   └── Bloom's level reached per topic
├── Learning Behavior
│   ├── Preferred modality (text/visual/code/mixed)
│   ├── Average session duration
│   ├── Peak learning hours
│   ├── Completion rate per nugget type
│   └── Time-to-mastery velocity
├── Engagement
│   ├── Streak data
│   ├── XP & level
│   ├── Badges earned
│   └── Social interactions
└── Review State
    ├── Cards due for review
    ├── SM-2 parameters per concept
    └── Retention predictions
```

### 4.2 Bayesian Knowledge Tracing (BKT)

Platform menggunakan **Bayesian Knowledge Tracing** untuk memperkirakan probabilitas mahasiswa telah menguasai setiap Sub-CPMK.

**Parameter per skill:**

| Parameter | Simbol | Deskripsi | Default |
|-----------|--------|-----------|---------|
| P(L₀) | Prior | Probabilitas sudah tahu sebelum belajar | 0.1 |
| P(T) | Transition | Probabilitas belajar dari tidak tahu → tahu | 0.3 |
| P(G) | Guess | Probabilitas menjawab benar padahal belum tahu | 0.2 |
| P(S) | Slip | Probabilitas menjawab salah padahal sudah tahu | 0.1 |

**Update rule setelah menjawab soal:**

```
Jika jawaban BENAR:
  P(Lₙ|benar) = P(Lₙ) × (1 - P(S)) / [P(Lₙ) × (1 - P(S)) + (1 - P(Lₙ)) × P(G)]

Jika jawaban SALAH:
  P(Lₙ|salah) = P(Lₙ) × P(S) / [P(Lₙ) × P(S) + (1 - P(Lₙ)) × (1 - P(G))]

Setelah update:
  P(Lₙ₊₁) = P(Lₙ|obs) + (1 - P(Lₙ|obs)) × P(T)
```

**Mastery threshold:** P(L) ≥ 0.85 → konsep dianggap "mastered"

### 4.3 Tiga Mode Pembelajaran

#### Mode 1: Guided Path (Jalur Terbimbing)

Untuk mahasiswa yang mengikuti perkuliahan formal di universitas.

- Mengikuti urutan minggu per minggu sesuai RPS
- Nugget disajikan sequential dalam satu minggu
- Cocok untuk: mahasiswa semester aktif, yang ingin mengikuti kurikulum

```
Minggu 1 → Minggu 2 → ... → UTS → ... → UAS
  ↓           ↓
  10 nugget   10 nugget
  sequential  sequential
```

#### Mode 2: Adaptive Path (Jalur Adaptif)

AI menyusun jalur belajar optimal berdasarkan:

1. **Current mastery** — skip nugget yang sudah dikuasai (dari pre-test)
2. **Knowledge gaps** — prioritaskan prerequisite yang belum terpenuhi
3. **Learning velocity** — sesuaikan kecepatan sajian
4. **Forgetting prediction** — sisipkan review saat strength menurun
5. **Interleaving** — campur topik untuk transfer learning lebih baik

```
Algoritma:
  Pre-test → [skip nugget 1-3] → nugget 4 → nugget 5 → [review statistik] → nugget 6
                                                              ↑
                                              (interleaving dari mata kuliah lain)
```

#### Mode 3: Explorer (Jelajah Bebas)

Untuk self-learner yang ingin belajar topik spesifik.

- Tampilkan knowledge graph visual — klik node untuk mulai belajar
- AI merekomendasikan: *"Sebelum belajar Binary Search, pastikan kamu sudah paham List dan Sorting"*
- Tidak terikat urutan minggu

### 4.4 AI Tutor: Kontekstual & Sokratik

AI Tutor bukan chatbot generik — ia memiliki konteks spesifik dari nugget yang sedang dipelajari.

**Arsitektur:**

```
[Learner Question]
    ↓
[Context Assembly]
    ├── Current nugget content (full markdown)
    ├── Learner profile (mastery state, history)
    ├── Related nuggets (prerequisites, next)
    ├── Common misconceptions for this topic
    └── Pedagogical guidelines (Socratic method)
    ↓
[LLM (Claude API)] → system prompt: "Kamu adalah tutor Sokratik..."
    ↓
[Response with guardrails]
    ├── Jawab dengan pertanyaan balik (bukan langsung jawab)
    ├── Berikan hint bertingkat
    ├── Gunakan analogi Indonesia
    └── Track: apakah mahasiswa akhirnya paham? (update BKT)
```

**System prompt AI Tutor:**

```
Kamu adalah NusaTutor, asisten belajar yang sabar dan Sokratik.
Konteks: mahasiswa sedang mempelajari [NUGGET_TITLE] dari mata kuliah [COURSE].
Mastery level mereka saat ini: [MASTERY_LEVEL].

ATURAN:
1. JANGAN langsung memberi jawaban. Ajukan pertanyaan yang mengarahkan.
2. Gunakan analogi dari kehidupan sehari-hari di Indonesia.
3. Jika mahasiswa stuck >2 kali, berikan hint yang lebih eksplisit.
4. Jika diminta membuatkan kode, minta mereka coba dulu, baru review.
5. Bahasa: Indonesia dengan istilah teknis bilingual.
6. Setelah mahasiswa paham, berikan challenge kecil untuk konfirmasi.
```

**Fitur AI Tutor:**

| Fitur | Deskripsi |
|-------|-----------|
| **"Jelaskan Lagi"** | Minta penjelasan ulang dengan analogi berbeda |
| **"Quiz Me"** | Generate soal on-the-fly berdasarkan nugget |
| **"Debug Kodeku"** | Paste kode, AI Tutor analisis error tanpa langsung fix |
| **"Hubungkan"** | *"Apa hubungan konsep ini dengan [topik lain]?"* |
| **"Simplify"** | Jelaskan seolah ke anak SD (untuk konsep sulit) |
| **"Challenge Me"** | Soal yang lebih sulit dari level saat ini |

### 4.5 Spaced Repetition Engine

**Integrasi ke daily learning flow:**

```
Daily Session (20-30 menit)
├── [5 min] Review Queue — konsep yang jatuh tempo hari ini
├── [15-20 min] New Learning — nugget baru sesuai path
└── [5 min] Preview — micro-preview nugget besok (priming effect)
```

**Review card types:**

| Tipe | Format | Contoh |
|------|--------|--------|
| **Concept Recall** | Flashcard teks | "Apa 5 karakteristik algoritma yang baik?" |
| **Code Recall** | Complete the code | `for i in _____(5): print(i)` |
| **Visual Recall** | Identify diagram | "Simbol flowchart apa ini? [Diamond]" |
| **Explain** | Free text | "Jelaskan perbedaan list dan tuple" |
| **Debug** | Fix the bug | "Kode ini infinite loop. Perbaiki." |

---

## 5. Engagement & Gamifikasi

### 5.1 Sistem XP (Experience Points)

XP diberikan untuk setiap aktivitas belajar, dengan bobot berdasarkan **Bloom's Taxonomy level** (aktivitas higher-order thinking mendapat lebih banyak XP).

| Aktivitas | XP | Bloom's |
|-----------|-----|---------|
| Membaca nugget concept | 10 | C1-C2 |
| Menyelesaikan example | 15 | C2 |
| Code-along selesai | 20 | C3 |
| Practice benar (first try) | 30 | C3-C4 |
| Quiz perfect score | 40 | C3-C4 |
| Reflection submitted | 25 | C4-C5 |
| Challenge solved | 50 | C5-C6 |
| Review card correct | 10 | (retention) |
| Membantu peer (jawab forum) | 30 | C5-C6 |
| Weekly streak bonus | 50 | (konsistensi) |

### 5.2 Level System

| Level | Nama (Indonesian) | XP Required | Perks |
|-------|-------------------|-------------|-------|
| 1 | Pemula (Novice) | 0 | Akses semua nugget dasar |
| 2-5 | Penjelajah (Explorer) | 500-2000 | Unlock Daily Mix mode |
| 6-10 | Praktisi (Practitioner) | 2000-5000 | Unlock AI Tutor extended sessions |
| 11-15 | Analis (Analyst) | 5000-10000 | Unlock Challenge mode |
| 16-20 | Ahli (Expert) | 10000-20000 | Unlock peer mentoring |
| 21-25 | Master | 20000-35000 | Unlock content creation tools |
| 26-30 | Guru (Teacher) | 35000-50000 | Unlock instructor dashboard |

### 5.3 Badge System

Badges dikaitkan dengan **pencapaian pedagogis yang bermakna**, bukan hanya aktivitas.

**Badge Categories:**

| Kategori | Contoh Badge | Kriteria |
|----------|-------------|----------|
| **Mastery** | "Al-Khwarizmi" | Kuasai semua CPMK-1 (Algoritma Dasar) |
| **Mastery** | "Pythonista" | Kuasai semua CPMK-2 sampai CPMK-4 |
| **Mastery** | "Data Whisperer" | Kuasai semua CPMK ADS |
| **Mastery** | "ML Engineer" | Kuasai semua CPMK AIML |
| **Consistency** | "Istiqomah 7" | 7-day learning streak |
| **Consistency** | "Istiqomah 30" | 30-day learning streak |
| **Consistency** | "Istiqomah 100" | 100-day learning streak |
| **Depth** | "Deep Thinker" | 10 reflection nuggets completed |
| **Breadth** | "Renaissance" | Nugget selesai dari semua 4 mata kuliah |
| **Social** | "Penolong" | Bantu 10 peers di forum |
| **Social** | "Mentor" | Peer rating ≥4.5 dari 20+ interactions |
| **Challenge** | "Problem Solver" | 50 challenges solved |
| **Review** | "Memory Master" | 30-day retention ≥90% |

### 5.4 Streak System — "Istiqomah"

Terinspirasi dari nilai Islami **istiqomah** (konsistensi dalam kebaikan):

- **Daily Goal:** Minimal 1 nugget + review queue = "hari aktif"
- **Streak Counter:** Berapa hari berturut-turut aktif
- **Freeze:** 1 "streak freeze" per minggu (untuk hari sibuk/sakit) — seperti konsep rukhshah dalam Islam
- **Streak Milestones:** 7, 14, 30, 60, 100, 365 hari
- **Recovery:** Jika streak putus, tampilkan motivasi: *"Sebaik-baik amalan adalah yang dilakukan secara konsisten, meskipun sedikit"* (HR. Bukhari)

### 5.5 Social Learning — "Halaqah Digital"

**Halaqah** (lingkaran belajar) adalah tradisi pembelajaran Islami yang diadaptasi ke platform digital:

| Fitur | Deskripsi |
|-------|-----------|
| **Study Circle** | Grup 4-6 orang yang belajar mata kuliah yang sama |
| **Weekly Challenge** | Tantangan kolaboratif mingguan untuk setiap circle |
| **Peer Teaching** | Mahasiswa yang sudah master bisa mengajar peer (mendapat XP bonus) |
| **Discussion Thread** | Forum per nugget — pertanyaan & jawaban |
| **Code Review** | Peer review kode praktik (structured feedback form) |
| **Leaderboard** | Per halaqah (bukan global) — mendorong kolaborasi, bukan kompetisi ekstrem |

---

## 6. Asesmen & Feedback Loop

### 6.1 Micro-Assessment per Nugget

Setiap nugget diakhiri dengan 2-3 pertanyaan. Format bervariasi:

| Format | Cocok untuk | Auto-graded? |
|--------|-------------|-------------|
| **Multiple Choice** | Recall facts, identify concepts | Ya |
| **Fill-in-Code** | Syntax, API usage | Ya |
| **Drag-and-Drop** | Ordering steps, matching | Ya |
| **Short Code** | Write 3-5 lines to solve problem | Ya (test cases) |
| **Explain** | Conceptual understanding | AI-graded + peer review |
| **Debug** | Find and fix error | Ya (test cases) |

**Schema:** `schemas/assessment-item-schema.json`

### 6.2 Adaptive Difficulty

```
Student answers correctly 3× in a row at difficulty level 2
    → System promotes to difficulty level 3
    → New questions are harder (higher Bloom's level)

Student answers incorrectly 2× in a row at difficulty level 3
    → System demotes to difficulty level 2
    → Provides scaffolding hint
    → Recommends reviewing prerequisite nugget
```

**Difficulty mapping ke Bloom's:**

| Difficulty | Bloom's | Question Type |
|------------|---------|---------------|
| 1 (Dasar) | C1-C2 | Definisi, identifikasi, pilih yang benar |
| 2 (Menengah) | C3 | Terapkan konsep, tulis kode sederhana |
| 3 (Mahir) | C4 | Analisis kode, bandingkan pendekatan |
| 4 (Lanjut) | C5 | Evaluasi efisiensi, optimasi |
| 5 (Expert) | C6 | Rancang solusi baru, creative problem solving |

### 6.3 AI-Generated Practice Problems

AI dapat generate soal baru on-demand berdasarkan:

- Topik nugget saat ini
- Difficulty level learner
- Konteks Indonesia (selalu)
- Tipe soal yang diminta

**Prompt template untuk AI question generation:**

```
Generate 1 soal {difficulty_level} untuk topik "{topic}".
Bloom's level: {bloom_level}.
Konteks: gunakan skenario kehidupan di Indonesia.
Format: {question_format}.
Sertakan: soal, pilihan jawaban (jika MC), jawaban benar, penjelasan.
Bahasa: Indonesia dengan istilah teknis bilingual.
```

### 6.4 Portfolio & Evidence of Mastery

Setiap learner membangun portfolio digital yang mencakup:

| Artefak | Sumber | Bukti Mastery |
|---------|--------|---------------|
| **Code Submissions** | Practice & code-along nuggets | Kode yang lolos semua test cases |
| **Reflections** | Reflection nuggets | Penjelasan konsep dengan kata sendiri |
| **Challenge Solutions** | Weekly challenges | Solusi kreatif untuk masalah kompleks |
| **Peer Teaching** | Forum answers | Kemampuan menjelaskan ke orang lain |
| **Project** | Final project | End-to-end implementation |
| **Mastery Map** | Knowledge graph | Visual CPMK mastery progress |

### 6.5 Instructor Dashboard

Dashboard untuk dosen/instruktur:

| Panel | Metrik |
|-------|--------|
| **Cohort Overview** | % mahasiswa on-track, behind, ahead |
| **CPMK Heatmap** | Sub-CPMK mana yang paling banyak gagal (→ perlu re-teaching) |
| **At-Risk Alerts** | Mahasiswa yang streak putus >7 hari, atau mastery <50% |
| **Content Analytics** | Nugget mana yang paling lama diselesaikan, paling sering di-skip |
| **Assessment Analytics** | Soal mana yang discrimination index-nya rendah (soal buruk) |
| **Engagement Trends** | Jam belajar, session frequency, completion rates |

---

## 7. Arsitektur Teknis Platform

### 7.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENT LAYER                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐  │
│  │ PWA Web  │  │ Mobile   │  │ Offline-first Cache  │  │
│  │ (React/  │  │ (React   │  │ (Service Workers +   │  │
│  │  Next.js)│  │  Native) │  │  IndexedDB)          │  │
│  └────┬─────┘  └────┬─────┘  └──────────┬───────────┘  │
└───────┼──────────────┼───────────────────┼──────────────┘
        │              │                   │
        └──────────────┼───────────────────┘
                       │ REST + WebSocket
┌──────────────────────┼──────────────────────────────────┐
│                  API GATEWAY                             │
│              (Authentication, Rate Limiting)             │
└──────────────────────┼──────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
┌───────┴───────┐ ┌────┴────┐ ┌──────┴──────┐
│ CONTENT       │ │ LEARNER │ │ AI          │
│ SERVICE       │ │ SERVICE │ │ SERVICE     │
│               │ │         │ │             │
│ • Nugget DB   │ │ • Profile│ │ • AI Tutor │
│ • Knowledge   │ │ • BKT   │ │ • Question │
│   Graph       │ │ • SR    │ │   Generator│
│ • Search      │ │   Engine│ │ • Grader   │
│ • Manifest    │ │ • XP    │ │ • RAG      │
└───────┬───────┘ └────┬────┘ └──────┬──────┘
        │              │              │
┌───────┴──────────────┴──────────────┴───────────────────┐
│                  DATA LAYER                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐  │
│  │PostgreSQL│  │ Redis    │  │ S3/Blob  │  │Elastic │  │
│  │(profiles,│  │(cache,   │  │(media,   │  │Search  │  │
│  │ progress)│  │ sessions)│  │ exports) │  │(content│  │
│  └──────────┘  └──────────┘  └──────────┘  │ search)│  │
│                                             └────────┘  │
└─────────────────────────────────────────────────────────┘
```

### 7.2 Content Pipeline

Transformasi dari Markdown source → platform content:

```
[Markdown Source]                    [Structured Content]
mata-kuliah/                         nuggets/
├── algoritma-pemrograman/    ──→    ├── alp/
│   ├── 03-modules/                  │   ├── week-01/
│   │   └── week-01-*.md             │   │   ├── nugget-alp-01-01-*.md
│   └── 05-buku-ajar/               │   │   ├── nugget-alp-01-02-*.md
│       └── bab-01-*.md              │   │   └── ...
└── ...                              └── ...

Pipeline steps:
1. PARSE     — Extract sections from long-form markdown
2. DECOMPOSE — Split into atomic concepts (1 concept = 1 nugget)
3. CLASSIFY  — Assign type (concept/example/practice/etc.)
4. ENRICH    — Add frontmatter metadata (CPMK, Bloom's, difficulty)
5. LINK      — Build knowledge graph edges
6. ASSESS    — Generate assessment items per nugget
7. VALIDATE  — Check CPMK traceability, prerequisite chains
8. PUBLISH   — Deploy to content service
```

### 7.3 Offline Capability

Kritis untuk infrastruktur Indonesia (banyak daerah dengan koneksi lambat):

| Fitur | Offline Support |
|-------|----------------|
| Nugget content (text + diagrams) | Fully cached via Service Worker |
| Interactive code exercises | Local execution via Pyodide (Python in browser) |
| Quiz & assessment | Cached, sync results when online |
| AI Tutor | Offline: pre-cached FAQ per nugget. Online: full LLM |
| Spaced repetition review | Fully offline (SM-2 runs client-side) |
| Progress sync | Queue locally, sync when connected |

**Tech stack untuk offline:**
- **Service Workers** — cache content assets
- **IndexedDB** — store learner progress, review queue
- **Pyodide** — Python runtime in WebAssembly (run code tanpa server)
- **Background Sync API** — sync progress when connection restored

### 7.4 Tech Stack Rekomendasi

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Frontend | Next.js (React) + PWA | SSR untuk SEO, offline-first, responsive |
| Mobile | React Native / Capacitor | Code sharing dengan web |
| Backend | FastAPI (Python) | Match dengan ekosistem Python ML |
| Database | PostgreSQL + Redis | Relational + cache |
| Search | Elasticsearch / Meilisearch | Full-text search konten nugget |
| AI/LLM | Claude API (Anthropic) | AI Tutor, question generation, grading |
| Code Execution | Pyodide (client) + Judge0 (server) | Interactive coding |
| Auth | Firebase Auth / Supabase Auth | Social login, mudah setup |
| Storage | S3-compatible (MinIO) | Media assets |
| Deployment | Docker + Kubernetes | Scalable |
| CDN | Cloudflare | Indonesia edge servers |

---

## 8. Integrasi Nilai Islami & Konteks Indonesia

### 8.1 Prinsip Integrasi

Nilai Islami diintegrasikan secara **natural dan bermakna** — bukan dipaksakan. Tiga level integrasi:

| Level | Pendekatan | Contoh |
|-------|-----------|--------|
| **Implicit** | Nilai tercermin dalam desain platform | Sistem istiqomah (streak), halaqah (study circle) |
| **Contextual** | Muncul saat relevan dengan materi | Al-Khwarizmi saat belajar algoritma, etika AI dari perspektif Islam |
| **Explicit** | Referensi langsung ke ajaran Islam | Hadits tentang konsistensi belajar, konsep amanah dalam integritas akademik |

### 8.2 Mapping Nilai → Fitur

| Nilai Islami | Fitur Platform |
|-------------|----------------|
| **Istiqomah** (konsistensi) | Streak system dengan nama "Istiqomah" |
| **Amanah** (kepercayaan) | AI Usage Log — jujur dalam penggunaan AI |
| **Halaqah** (lingkaran ilmu) | Study Circle feature |
| **Ilmu yang bermanfaat** | Peer teaching rewards |
| **Al-Khwarizmi heritage** | Badge "Al-Khwarizmi" untuk mastery algoritma |
| **Tafakkur** (refleksi) | Reflection nuggets |
| **Al-'Adl** (keadilan) | Fair adaptive system — setiap mahasiswa mendapat path yang sesuai |
| **Rukhshah** (keringanan) | Streak freeze 1x per minggu |

### 8.3 Indonesian Context Integration

**Dataset Indonesia untuk setiap mata kuliah:**

| Mata Kuliah | Dataset Indonesia |
|-------------|-------------------|
| Algoritma | Data kependudukan (BPS), antrian TransJakarta, menu warteg |
| Statistik | Sensus penduduk, data curah hujan BMKG, indeks harga konsumen |
| AI/ML | Sentimen Twitter Indonesia, harga properti Jakarta, klasifikasi batik |

**Contoh soal selalu menggunakan konteks lokal:**
- Sorting: mengurutkan data harga sembako di pasar tradisional
- Search: mencari data mahasiswa di sistem akademik universitas
- Regression: prediksi harga rumah di DKI Jakarta
- Classification: klasifikasi jenis batik dari gambar
- Clustering: segmentasi pelanggan e-commerce Indonesia

### 8.4 Bilingual Glossary System

Setiap istilah teknis memiliki entry di glossary platform:

```json
{
  "term_en": "Binary Search",
  "term_id": "Pencarian Biner",
  "definition_id": "Algoritma pencarian yang membagi data terurut menjadi dua bagian secara berulang",
  "definition_en": "A search algorithm that repeatedly divides a sorted dataset in half",
  "first_appears": "nugget-alp-10-01",
  "related_terms": ["Linear Search", "Sorting", "Divide and Conquer"]
}
```

Saat learner hover/tap istilah teknis dalam nugget, popup bilingual muncul.

---

## 9. Roadmap Implementasi

### Phase 1: Content Foundation (Bulan 1-2)

**Goal:** Transformasi konten INF-101 (Algoritma & Pemrograman) sebagai pilot.

| Task | Output | Prioritas |
|------|--------|-----------|
| Finalisasi nugget schema & templates | `schemas/*.yaml`, `schemas/*.json` | P0 |
| Dekomposisi Week 1-4 ALP → nuggets | ~40 nugget files | P0 |
| Build knowledge graph untuk ALP | `knowledge-graph/nodes.json`, `edges.json` | P0 |
| Generate assessment items Week 1-4 | ~120 soal | P1 |
| Dekomposisi Week 5-16 ALP → nuggets | ~100 nugget files | P1 |
| Dekomposisi PAP (Praktikum) → nuggets | ~104 nugget files | P2 |

### Phase 2: Platform MVP (Bulan 3-4)

**Goal:** Platform minimal yang bisa digunakan mahasiswa.

| Task | Output |
|------|--------|
| Setup Next.js + PWA skeleton | Web app |
| Content service (serve nuggets from markdown) | REST API |
| Basic learner auth (email/Google) | Auth system |
| Sequential nugget navigation (Guided Path) | Core UX |
| Micro-quiz per nugget (auto-graded MCQ) | Assessment engine |
| Basic progress tracking | Dashboard sederhana |
| Pyodide integration (run Python in browser) | Interactive code |

### Phase 3: AI & Adaptive Features (Bulan 5-8)

**Goal:** Diferensiasi utama — platform menjadi "cerdas".

| Task | Output |
|------|--------|
| BKT engine implementation | Adaptive mastery tracking |
| Adaptive Path mode | Personalized learning paths |
| Spaced Repetition engine (SM-2) | Review queue system |
| AI Tutor integration (Claude API + RAG) | Contextual AI assistant |
| AI question generation | Dynamic practice problems |
| Daily Mix mode (interleaving) | Mixed topic sessions |
| Offline mode (Service Workers + IndexedDB) | Offline learning |

### Phase 4: Full Platform (Bulan 9-12)

**Goal:** Platform lengkap dengan semua 4 mata kuliah.

| Task | Output |
|------|--------|
| Dekomposisi ADS → nuggets | ~140 nuggets |
| Dekomposisi AIML → nuggets | ~168 nuggets |
| Cross-course knowledge graph | Full concept map |
| Gamification system (XP, badges, streaks) | Engagement layer |
| Social features (halaqah, forum, peer teaching) | Community |
| Instructor dashboard | Analytics |
| Explorer mode (knowledge graph navigation) | Self-directed learning |
| Mobile app (React Native) | Mobile access |

### Phase 5: Scale & Iterate (Bulan 13+)

| Task | Output |
|------|--------|
| A/B testing pada adaptive algorithms | Optimized learning paths |
| Buka platform untuk universitas lain | Multi-tenant |
| Tambah mata kuliah baru | Content expansion |
| Bahasa Inggris support | Internationalization |
| Analytics research: what works? | Learning science insights |

---

## Lampiran A: File Schema Reference

| Schema File | Deskripsi |
|-------------|-----------|
| `schemas/nugget-schema.yaml` | Frontmatter schema untuk setiap micro-lesson nugget |
| `schemas/learner-profile-schema.json` | Model profil learner (knowledge state, behavior, engagement) |
| `schemas/knowledge-graph-schema.json` | Schema node dan edge knowledge graph |
| `schemas/assessment-item-schema.json` | Format soal/quiz dengan metadata |
| `schemas/gamification-schema.json` | Rules XP, badges, levels, streaks |
| `schemas/course-manifest.yaml` | Konfigurasi mapping nuggets → weeks → CPMK per course |

## Lampiran B: Example Files

| File | Deskripsi |
|------|-----------|
| `examples/nugget-alp-01-01-concept-apa-itu-algoritma.md` | Contoh nugget tipe concept |
| `examples/nugget-alp-01-02-example-algoritma-kehidupan.md` | Contoh nugget tipe example |
| `examples/nugget-alp-01-03-practice-flowchart-dasar.md` | Contoh nugget tipe practice + embedded quiz |
| `examples/week-01-decomposition-map.yaml` | Peta dekomposisi Week 1 → nuggets |

---

## Lampiran C: Metrik Keberhasilan Platform

| Metrik | Target | Cara Ukur |
|--------|--------|-----------|
| Daily Active Users | 60% enrolled students | Analytics |
| Average session duration | 15-25 minutes | Time tracking |
| Nugget completion rate | ≥85% | Progress data |
| 7-day retention | ≥70% | Spaced repetition accuracy |
| 30-day retention | ≥60% | Spaced repetition accuracy |
| CPMK mastery rate | ≥80% students reach P(L)≥0.85 | BKT data |
| UTS/UAS score improvement | +15% vs non-platform cohort | Grade comparison |
| Student satisfaction (NPS) | ≥50 | Survey |
| Streak average | ≥14 days | Gamification data |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
