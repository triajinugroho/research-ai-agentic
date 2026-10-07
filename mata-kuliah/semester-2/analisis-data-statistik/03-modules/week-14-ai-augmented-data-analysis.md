# Minggu 14: AI-Augmented Data Analysis

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — Universitas Al Azhar Indonesia — Semester Genap 2025/2026

---

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Minggu** | 14 |
| **Topik** | AI-Augmented Data Analysis |
| **CPMK** | CPMK-7: Mengevaluasi dan merancang analisis data end-to-end dengan memanfaatkan AI sebagai co-analyst secara bertanggung jawab |
| **Sub-CPMK** | 14.1: Menggunakan AI sebagai co-analyst untuk analisis data statistik |
| | 14.2: Mengevaluasi output AI secara kritis dan mendokumentasikan penggunaan AI |
| **Bloom's Taxonomy** | C5-C6 (Evaluate-Create) |
| **Durasi** | 100 menit (30 menit teori + 70 menit workshop) |
| **Prasyarat Modul** | Seluruh materi Minggu 1-13 |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Menjelaskan** kemampuan dan keterbatasan AI (khususnya LLM) sebagai alat bantu analisis data
2. **Merancang** prompt yang efektif untuk tugas-tugas analisis statistik
3. **Menerapkan** workflow kolaborasi Human-AI untuk analisis data end-to-end
4. **Mengevaluasi** output AI secara kritis — mengidentifikasi kapan AI membantu dan kapan AI menyesatkan
5. **Mendokumentasikan** penggunaan AI secara transparan sesuai prinsip etika dan reproducibility
6. **Merefleksikan** implikasi etis penggunaan AI dalam riset dan analisis data, termasuk perspektif Islam

---

## Materi Pembelajaran

### 1. AI Sebagai Co-Analyst: Kemampuan dan Keterbatasan

#### 1.1 Apa yang Bisa Dilakukan AI untuk Analisis Data?

Selama semester ini, sebagian dari kalian mungkin sudah menggunakan AI (ChatGPT, Claude, Copilot) untuk membantu tugas-tugas. Mari kita formalkan pemahaman tentang apa yang **bisa** dan **tidak bisa** dilakukan AI.

**AI Mampu:**

| Kemampuan | Contoh |
|-----------|--------|
| **Menjelaskan konsep** | "Jelaskan perbedaan precision dan recall dengan analogi sederhana" |
| **Menulis kode** | Generate kode Python untuk visualisasi, uji statistik, ML |
| **Debugging** | Menemukan error dalam kode dan menyarankan perbaikan |
| **Interpretasi output** | Menjelaskan arti output classification_report atau ANOVA |
| **Menyarankan metode** | "Data saya seperti ini, uji statistik apa yang tepat?" |
| **Brainstorming** | Membantu merumuskan pertanyaan penelitian atau hipotesis |
| **Menyusun narasi** | Membantu menulis laporan analisis dalam bahasa yang baik |

#### 1.2 Keterbatasan AI yang Wajib Dipahami

**AI TIDAK Mampu (atau Sering Gagal):**

| Keterbatasan | Penjelasan |
|-------------|------------|
| **Hallucination** | AI bisa "mengarang" hasil statistik, nilai p-value, atau referensi yang tidak ada |
| **Tidak bisa menjalankan kode** | Sebagian besar LLM hanya generate kode, bukan menjalankannya (kecuali yang memiliki fitur code interpreter) |
| **Konteks terbatas** | AI tidak "melihat" dataset kalian kecuali kalian berikan secara eksplisit |
| **Asumsi salah** | AI bisa mengasumsikan data normal padahal tidak, atau menggunakan uji yang salah |
| **Tidak memahami domain** | AI tahu statistik secara umum, tapi tidak paham konteks spesifik riset kalian |
| **Bias dalam saran** | AI cenderung merekomendasikan metode populer, bukan yang paling tepat |
| **Tidak bisa menggantikan judgment** | Keputusan akhir tentang interpretasi dan implikasi tetap tanggung jawab manusia |

> **Prinsip utama:** AI adalah **alat yang sangat kuat** tapi **bukan pengganti pemahaman**. Seperti kalkulator tidak menggantikan pemahaman matematika, AI tidak menggantikan pemahaman statistik.

---

### 2. Prompt Engineering untuk Statistik

#### 2.1 Mengapa Prompt Penting?

Kualitas output AI sangat bergantung pada kualitas prompt (instruksi) yang diberikan. Prompt yang baik menghasilkan jawaban yang relevan dan akurat. Prompt yang buruk menghasilkan jawaban yang generik atau bahkan menyesatkan.

#### 2.2 Struktur Prompt yang Efektif

**Framework CRIDE:**

| Komponen | Penjelasan | Contoh |
|----------|------------|--------|
| **C**ontext | Berikan konteks tentang siapa Anda dan apa yang sedang dikerjakan | "Saya mahasiswa Informatika semester 2 yang sedang menganalisis data survei kepuasan mahasiswa" |
| **R**ole | Tentukan peran AI | "Bertindak sebagai tutor statistik yang sabar" |
| **I**nstruction | Tulis instruksi yang jelas dan spesifik | "Bantu saya memilih uji statistik yang tepat" |
| **D**ata | Sertakan informasi tentang data | "Dataset memiliki 200 baris, 5 kolom, variabel dependen berskala ordinal" |
| **E**xpectation | Tentukan format output yang diharapkan | "Jelaskan dalam 3 langkah, sertakan kode Python" |

#### 2.3 Contoh Prompt untuk Berbagai Tugas Analisis

**Prompt 1: Meminta Penjelasan Konsep**

```
Konteks: Saya mahasiswa semester 2, baru belajar regresi linear berganda.

Pertanyaan: Jelaskan apa itu multicollinearity dan mengapa itu bermasalah
dalam regresi berganda. Gunakan analogi sederhana. Kemudian tunjukkan
bagaimana cara mendeteksinya menggunakan VIF di Python (sklearn/statsmodels).

Format: Penjelasan konseptual dulu, baru kode Python.
```

**Prompt 2: Meminta Bantuan Memilih Uji Statistik**

```
Saya memiliki dataset tentang nilai ujian mahasiswa dari 4 kelas berbeda
(Kelas A, B, C, D). Setiap kelas memiliki sekitar 30 mahasiswa.
Saya ingin tahu apakah rata-rata nilai antar kelas berbeda secara signifikan.

Data saya:
- Variabel dependen: nilai ujian (numerik, kontinu, 0-100)
- Variabel independen: kelas (kategorikal, 4 level)
- Sampel per kelompok: ~30
- Saya belum cek normalitas dan homogenitas varians

Pertanyaan:
1. Uji statistik apa yang paling tepat? Jelaskan mengapa.
2. Asumsi apa yang perlu saya cek terlebih dahulu?
3. Berikan kode Python lengkap untuk: cek asumsi, jalankan uji, dan
   interpretasi hasil.
```

**Prompt 3: Meminta AI Mengevaluasi Output**

```
Berikut adalah output dari regresi linear berganda yang saya jalankan:

                 coef    std err   t      P>|t|     [0.025    0.975]
const          3.4521    1.234    2.797   0.006     1.012     5.892
pengalaman     0.8234    0.156    5.278   0.000     0.515     1.132
pendidikan     0.4512    0.203    2.222   0.028     0.050     0.852
usia          -0.0123    0.045   -0.273   0.785    -0.101     0.077

R-squared: 0.672    Adjusted R-squared: 0.661

Tolong interpretasikan output ini. Variabel mana yang signifikan?
Apa arti R-squared? Apakah model ini baik? Apa rekomendasi selanjutnya?
```

**Prompt 4: Chain-of-Thought untuk Analisis Multi-Langkah**

```
Saya ingin menganalisis hubungan antara jam belajar, metode belajar
(online/offline), dan IPK mahasiswa. Dataset saya memiliki 150 mahasiswa.

Tolong bantu saya menyusun rencana analisis step-by-step:
1. Mulai dari eksplorasi data (apa yang harus saya lihat?)
2. Uji statistik apa yang tepat untuk menjawab pertanyaan saya?
3. Bagaimana cara menginterpretasi hasilnya?
4. Visualisasi apa yang sebaiknya saya buat?

Pikirkan langkah demi langkah (think step by step).
Untuk setiap langkah, jelaskan MENGAPA langkah itu diperlukan.
```

---

### 3. Workflow Human-AI Collaboration

#### 3.1 Alur Kolaborasi 6 Langkah

Berikut adalah workflow yang direkomendasikan untuk kolaborasi Human-AI dalam analisis data:

```
┌─────────────────────────────────────────────────────────────────┐
│                WORKFLOW HUMAN-AI COLLABORATION                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐                                               │
│  │ 1. HUMAN     │  Definisikan pertanyaan penelitian            │
│  │    DEFINES   │  Pahami konteks dan tujuan analisis           │
│  │    QUESTION  │  → AI TIDAK BISA melakukan ini untuk Anda     │
│  └──────┬───────┘                                               │
│         ▼                                                       │
│  ┌──────────────┐                                               │
│  │ 2. AI DRAFTS │  Minta AI menyusun rencana analisis          │
│  │    ANALYSIS  │  "Berdasarkan pertanyaan X, susun rencana     │
│  │    PLAN      │   analisis step-by-step"                      │
│  └──────┬───────┘                                               │
│         ▼                                                       │
│  ┌──────────────┐                                               │
│  │ 3. HUMAN     │  Review rencana → apakah masuk akal?          │
│  │    REVIEWS   │  Sesuaikan dengan pengetahuan domain          │
│  │    & ADJUSTS │  Tambahkan/hapus langkah yang perlu           │
│  └──────┬───────┘                                               │
│         ▼                                                       │
│  ┌──────────────┐                                               │
│  │ 4. AI        │  Minta AI menulis kode Python                 │
│  │    GENERATES │  "Tuliskan kode untuk langkah 1-3..."         │
│  │    CODE      │  Review kode sebelum menjalankan              │
│  └──────┬───────┘                                               │
│         ▼                                                       │
│  ┌──────────────┐                                               │
│  │ 5. HUMAN     │  Jalankan kode → periksa output               │
│  │    VERIFIES  │  Apakah hasilnya masuk akal?                  │
│  │    & INTERPRETS  Interpretasikan dalam konteks domain        │
│  └──────┬───────┘                                               │
│         ▼                                                       │
│  ┌──────────────┐                                               │
│  │ 6. ITERATE   │  Ulangi jika perlu                            │
│  │              │  Perbaiki analisis berdasarkan temuan          │
│  │              │  Minta AI membantu menyempurnakan             │
│  └──────────────┘                                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### 3.2 Aturan Emas Kolaborasi

1. **Selalu mulai dari pertanyaan ANDA** — Jangan minta AI merumuskan pertanyaan
2. **Review setiap output AI** — Jangan copy-paste tanpa memahami
3. **Jalankan kode dan periksa** — AI bisa generate kode yang error atau menghasilkan output yang salah
4. **Interpretasi tetap tanggung jawab ANDA** — AI bisa membantu menjelaskan, tapi keputusan akhir ada di tangan Anda
5. **Dokumentasikan semuanya** — Catat prompt, output, dan modifikasi yang dilakukan

---

### 4. Kapan AI Membantu vs Menyesatkan

#### 4.1 Kesalahan Umum AI dalam Statistik

Berikut adalah kesalahan-kesalahan yang **sering** dilakukan AI dalam konteks analisis statistik:

| Jenis Kesalahan | Contoh | Cara Mendeteksi |
|-----------------|--------|-----------------|
| **Hallucinated statistics** | "Menurut studi Smith (2023), p-value-nya 0.003..." (studi tidak ada) | Verifikasi referensi, hitung sendiri jika memungkinkan |
| **Wrong test recommendation** | Merekomendasikan t-test padahal data tidak normal dan sampel kecil | Cek asumsi sendiri sebelum mengikuti saran AI |
| **Incorrect interpretation** | "p > 0.05 berarti H0 terbukti benar" (salah! seharusnya "gagal menolak H0") | Bandingkan dengan materi kuliah dan textbook |
| **Fabricated output** | Generate output Python yang "terlihat benar" tapi sebenarnya dibuat-buat | Selalu jalankan kode sendiri, jangan percaya output yang ditampilkan AI |
| **Overclaiming causation** | "X menyebabkan Y" padahal hanya menunjukkan korelasi | Terapkan critical thinking: apakah desain studi mendukung kausalitas? |
| **Ignoring assumptions** | Langsung menjalankan ANOVA tanpa cek normalitas dan homogenitas varians | Selalu cek asumsi — ini yang membedakan analyst yang baik dan yang asal-asalan |

#### 4.2 Red Flags: Kapan Harus Waspada

Waspadalah ketika AI:
- Memberikan angka yang **terlalu presisi** tanpa menjalankan kode (misal: "p-value = 0.00342")
- Menyatakan sesuatu dengan **sangat yakin** tanpa menyebutkan asumsi atau keterbatasan
- Merekomendasikan metode **tanpa menjelaskan** mengapa metode itu dipilih
- Mengutip **referensi** yang tidak bisa kalian temukan di Google Scholar
- Memberikan interpretasi yang **bertentangan** dengan materi kuliah kalian

#### 4.3 Contoh Praktis: Mengevaluasi Output AI

```python
# Misalkan Anda bertanya ke AI: "Analisis apakah ada perbedaan
# rata-rata gaji antara 3 departemen"
# AI menyarankan kode berikut:

from scipy import stats

# AI-generated code
f_stat, p_value = stats.f_oneway(dept_a, dept_b, dept_c)
print(f"F-statistic: {f_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# CHECKLIST EVALUASI:
# [?] Apakah AI menyarankan cek normalitas dulu?        → Sering TIDAK
# [?] Apakah AI menyarankan cek homogenitas varians?    → Sering TIDAK
# [?] Apakah AI menyertakan post-hoc test?              → Kadang LUPA
# [?] Apakah AI menjelaskan effect size?                 → Hampir TIDAK PERNAH
# [?] Apakah interpretasi p-value-nya benar?             → BIASANYA ya, tapi cek

# YANG SEHARUSNYA dilakukan (versi lengkap):
# 1. Cek normalitas: stats.shapiro(dept_a), dll.
# 2. Cek homogenitas: stats.levene(dept_a, dept_b, dept_c)
# 3. Jika asumsi terpenuhi → ANOVA; jika tidak → Kruskal-Wallis
# 4. Jika signifikan → post-hoc (Tukey's HSD)
# 5. Hitung effect size (eta-squared)
# 6. Interpretasi dalam konteks
```

---

### 5. Dokumentasi Penggunaan AI: Transparansi dan Reproducibility

#### 5.1 Mengapa Dokumentasi Penting?

Dalam sains dan analisis data, **reproducibility** (kemampuan orang lain untuk mereproduksi hasil Anda) adalah prinsip fundamental. Ketika AI digunakan sebagai bagian dari proses analisis, dokumentasi AI usage menjadi **sama pentingnya** dengan dokumentasi kode dan data.

#### 5.2 Template Dokumentasi AI

Gunakan template berikut di setiap tugas dan proyek:

```markdown
## Dokumentasi Penggunaan AI

### Informasi Umum
- **AI Tool:** [Claude / ChatGPT / Copilot / lainnya]
- **Versi/Model:** [Claude 3.5 Sonnet / GPT-4o / dll.]
- **Tanggal penggunaan:** [DD/MM/YYYY]
- **Tujuan penggunaan:** [Brainstorming / Coding / Debugging / Interpretasi / dll.]

### Log Interaksi

#### Interaksi 1
- **Prompt:** [Copy-paste prompt yang digunakan]
- **Ringkasan output AI:** [Apa yang AI jawab — tidak perlu copy-paste seluruh output]
- **Apa yang diambil:** [Bagian mana dari output AI yang digunakan]
- **Modifikasi:** [Apa yang diubah dari output AI dan mengapa]
- **Evaluasi:** [Apakah output AI akurat? Ada masalah?]

#### Interaksi 2
- ...

### Refleksi
- **Apa yang AI bantu percepat?** [...]
- **Apa yang AI salah atau kurang tepat?** [...]
- **Apa yang saya pelajari dari interaksi ini?** [...]
- **Apakah saya bisa menjelaskan semua kode/analisis tanpa AI?** [Ya/Tidak — jika tidak, bagian mana?]
```

#### 5.3 Contoh Dokumentasi yang Baik vs Buruk

**Dokumentasi BURUK:**
> "Menggunakan ChatGPT untuk membantu tugas."

**Dokumentasi BAIK:**
> **Interaksi 1:** Saya bertanya ke Claude cara melakukan Shapiro-Wilk test di Python. Claude memberikan kode menggunakan `scipy.stats.shapiro()`. Saya menggunakan kode tersebut langsung karena sudah sesuai. Output menunjukkan p-value = 0.234, yang saya interpretasikan sendiri sebagai data tidak menyimpang signifikan dari normalitas (gagal menolak H0 pada alpha = 0.05).
>
> **Interaksi 2:** Saya meminta Claude membantu memvisualisasikan residual plot. Kode yang diberikan menggunakan `plt.scatter()` tapi saya modifikasi menjadi `sns.residplot()` karena hasilnya lebih informatif dan saya sudah familiar dengan seaborn dari Minggu 3.

---

### 6. Etika AI dalam Riset dan Analisis Data

#### 6.1 Prinsip Etika AI dalam Konteks Akademik

| Prinsip | Penjelasan | Implementasi |
|---------|------------|-------------|
| **Transparansi** | Jujur tentang penggunaan AI | Dokumentasi lengkap di setiap tugas |
| **Accountability** | Bertanggung jawab atas hasil akhir | Anda yang menandatangani, Anda yang bertanggung jawab |
| **Competence** | Mampu menjelaskan apa yang dikerjakan | Jika tidak bisa menjelaskan, jangan klaim sebagai pekerjaan Anda |
| **Integrity** | Tidak menyesatkan tentang kontribusi AI | Bedakan mana pemikiran Anda, mana bantuan AI |
| **Fairness** | Tidak menggunakan AI untuk keuntungan yang tidak adil | Ikuti kebijakan AI yang berlaku (ujian tanpa AI) |

#### 6.2 Perspektif Islam tentang Etika AI

Sebagai mahasiswa Universitas Al Azhar Indonesia, kita memiliki landasan nilai-nilai Islami yang sangat relevan dengan etika penggunaan AI:

**Amanah (Kepercayaan):**
- Ketika dosen memberikan tugas, itu adalah **amanah** — kepercayaan bahwa kalian akan belajar dan memahami materi
- Menggunakan AI tanpa memahami hasilnya adalah **mengkhianati amanah** tersebut
- Mendokumentasikan AI usage adalah bentuk **menjaga amanah** — jujur tentang proses

**Keadilan (Al-'Adl):**
- Menggunakan AI harus **adil** — tidak merugikan diri sendiri (tidak belajar) maupun orang lain (unfair advantage di ujian)
- Prinsip keadilan juga berarti **tidak bias** — mengevaluasi output AI secara objektif, bukan menerimanya begitu saja

**Ihsan (Keunggulan):**
- Ihsan berarti melakukan sesuatu dengan **sebaik-baiknya**
- Dalam konteks AI, ihsan berarti menggunakan AI untuk **meningkatkan kualitas** analisis, bukan untuk **mengurangi usaha**
- Ihsan juga berarti **terus belajar** — AI sebagai guru tambahan, bukan pengganti proses belajar

> **Hadist relevan:** *"Sesungguhnya Allah menyukai jika seseorang mengerjakan sesuatu pekerjaan, ia mengerjakannya dengan itqan (sempurna/sungguh-sungguh)."* (HR. Thabrani)
>
> Menggunakan AI tools dengan bijak, bertanggung jawab, dan jujur adalah bentuk **itqan** dalam era digital.

#### 6.3 Citing AI dalam Karya Akademik

Saat ini belum ada standar universal untuk mengutip AI, tapi berikut panduan yang bisa diikuti:

```
Dalam teks:
"Analisis kode Python untuk visualisasi ini dikembangkan dengan bantuan
Claude (Anthropic, 2025), yang kemudian dimodifikasi oleh penulis untuk
menyesuaikan dengan konteks dataset Indonesia."

Dalam daftar pustaka (gaya APA):
Anthropic. (2025). Claude [Large language model]. https://claude.ai

OpenAI. (2025). ChatGPT [Large language model]. https://chat.openai.com
```

---

### 7. The Future: AI dalam Analisis Data dan Riset

#### 7.1 Tren yang Sedang Berkembang

| Tren | Penjelasan | Relevansi untuk Kalian |
|------|------------|----------------------|
| **Agentic AI** | AI yang bisa menjalankan langkah-langkah analisis secara otonom (bukan hanya generate teks) | Analisis data semi-otomatis akan semakin umum |
| **AutoML** | Automated Machine Learning — AI memilih model dan hyperparameter terbaik secara otomatis | Fondasi statistik tetap perlu untuk mengevaluasi hasil AutoML |
| **AI Code Assistants** | GitHub Copilot, Cursor — AI yang membantu menulis kode real-time | Bisa mempercepat coding, tapi perlu pemahaman untuk mengevaluasi |
| **Multimodal AI** | AI yang memahami teks, gambar, tabel, grafik | Upload grafik dan minta AI menginterpretasi |
| **AI in Scientific Research** | AI membantu literature review, hypothesis generation, analysis | Memahami statistik menjadi **lebih** penting, bukan kurang |

#### 7.2 Pesan Penting

> Perkembangan AI **tidak** membuat statistik menjadi kurang penting. Justru sebaliknya — semakin mudah analisis dilakukan oleh AI, semakin penting kemampuan manusia untuk:
>
> 1. **Merumuskan pertanyaan yang tepat**
> 2. **Mengevaluasi apakah metode yang digunakan AI benar**
> 3. **Menginterpretasi hasil dalam konteks yang bermakna**
> 4. **Mengkomunikasikan temuan kepada stakeholder**
>
> Ini semua membutuhkan **fondasi statistik yang kuat** — yang kalian telah bangun selama 14 minggu ini.

---

## Workshop: Analisis Data End-to-End dengan AI sebagai Co-Analyst

### Instruksi Workshop (70 menit)

#### Persiapan (5 menit)

```python
# Dataset untuk workshop
# Gunakan dataset tips dari seaborn (restoran, tip, dll.)
import seaborn as sns
import pandas as pd

tips = sns.load_dataset('tips')
print(tips.head())
print(tips.info())
print(tips.describe())
```

#### Tahap 1: Rumuskan Pertanyaan (10 menit) — TANPA AI

Tanpa menggunakan AI, rumuskan **2 pertanyaan penelitian** berdasarkan dataset tips. Contoh:

1. "Apakah ada perbedaan rata-rata tip antara hari kerja dan akhir pekan?"
2. "Apakah total bill memprediksi besarnya tip? Seberapa kuat hubungannya?"

**Tulis pertanyaan Anda di markdown cell.**

#### Tahap 2: Minta AI Menyusun Rencana Analisis (10 menit)

Gunakan AI assistant pilihan Anda. Contoh prompt:

```
Saya memiliki dataset restoran dengan kolom berikut:
- total_bill (float): total tagihan dalam dollar
- tip (float): jumlah tip dalam dollar
- sex (kategorikal): Male/Female
- smoker (kategorikal): Yes/No
- day (kategorikal): Thur/Fri/Sat/Sun
- time (kategorikal): Lunch/Dinner
- size (int): jumlah orang di meja

Pertanyaan penelitian saya:
[TULIS PERTANYAAN ANDA DI SINI]

Susun rencana analisis step-by-step yang mencakup:
1. Eksplorasi data apa yang perlu dilakukan
2. Uji statistik apa yang tepat dan mengapa
3. Visualisasi apa yang sebaiknya dibuat
4. Bagaimana menginterpretasi hasilnya

Saya menggunakan Python dengan pandas, scipy, sklearn, matplotlib, seaborn.
```

**Catat rencana yang diberikan AI. Review secara kritis — apakah ada yang perlu ditambah/dihapus?**

#### Tahap 3: Minta AI Generate Kode (15 menit)

Minta AI menulis kode Python untuk rencana analisis tersebut. Kemudian:

1. **Review kode** sebelum menjalankan — apakah masuk akal?
2. **Jalankan kode** di Google Colab
3. **Debug** jika ada error — bisa minta bantuan AI juga
4. **Periksa output** — apakah hasilnya masuk akal?

#### Tahap 4: Evaluasi dan Interpretasi (15 menit) — ANDA yang Memutuskan

Setelah mendapat hasil, jawab pertanyaan berikut **dengan pemikiran Anda sendiri**:

1. Apakah asumsi uji statistik terpenuhi?
2. Apa yang ditunjukkan oleh p-value/metrik yang diperoleh?
3. Apa practical significance dari temuan ini?
4. Apa limitasi dari analisis ini?

**Boleh minta AI membantu menjelaskan, tapi interpretasi akhir harus ANDA yang tulis.**

#### Tahap 5: Dokumentasi (10 menit)

Lengkapi dokumentasi AI usage menggunakan template yang sudah disediakan di bagian 5.2.

#### Tahap 6: Refleksi (5 menit)

Tulis refleksi singkat di markdown cell:

```markdown
## Refleksi Workshop

### Apa yang AI bantu percepat dalam analisis ini?
[Jawaban Anda]

### Apa yang AI salah atau kurang tepat?
[Jawaban Anda]

### Bagian mana yang HARUS dilakukan oleh manusia (bukan AI)?
[Jawaban Anda]

### Apa yang saya pelajari tentang kolaborasi Human-AI?
[Jawaban Anda]
```

---

## Refleksi Besar: Apa yang Bisa AI Lakukan yang Anda Tidak Bisa? Dan Sebaliknya?

### Yang AI Bisa Tapi Manusia Sulit

- Menulis kode dalam hitungan detik
- Mengingat ratusan fungsi dan parameter library
- Menjelaskan konsep dengan berbagai analogi
- Bekerja 24/7 tanpa lelah
- Memproses informasi dari ribuan textbook

### Yang Manusia Bisa Tapi AI Tidak Bisa (atau Belum Bisa)

- **Memahami konteks** — Mengapa analisis ini penting? Untuk siapa?
- **Merumuskan pertanyaan bermakna** — AI menjawab pertanyaan, bukan membuat pertanyaan
- **Judgment etis** — Apakah analisis ini bisa merugikan seseorang?
- **Kreativitas sejati** — Menghubungkan temuan data dengan pengetahuan dunia nyata
- **Tanggung jawab** — AI tidak bisa "disalahkan" jika analisis salah
- **Empati dan komunikasi** — Menyampaikan temuan yang sensitif kepada stakeholder

> **Kesimpulan:** AI adalah co-pilot terbaik yang bisa Anda miliki. Tapi **pilot-nya tetap Anda**.

---

## Latihan Mandiri

### Latihan 1: Evaluasi Kritis Output AI (15 menit)

Berikut adalah "jawaban AI" terhadap pertanyaan statistik. Identifikasi mana yang **benar**, mana yang **salah**, dan jelaskan mengapa.

1. **AI bilang:** "P-value 0.03 berarti ada 3% probabilitas bahwa H0 benar."
   - Benar atau salah? Mengapa?

2. **AI bilang:** "Karena R-squared = 0.95, maka model regresi ini sangat bagus dan tidak perlu perbaikan."
   - Benar atau salah? Mengapa?

3. **AI bilang:** "Untuk membandingkan 2 kelompok, gunakan ANOVA."
   - Benar atau salah? Mengapa?

4. **AI bilang:** "k-NN tidak memerlukan data yang di-standardisasi karena algoritma ini robust."
   - Benar atau salah? Mengapa?

### Latihan 2: Prompt Engineering Challenge (20 menit)

Tulis prompt untuk masing-masing skenario berikut. Gunakan framework CRIDE.

1. Anda ingin AI membantu mengecek apakah kode ANOVA Anda sudah benar
2. Anda ingin AI menjelaskan mengapa model decision tree Anda overfitting
3. Anda ingin AI menyarankan cara memvisualisasikan hubungan antara 3 variabel

### Latihan 3: Refleksi Etika (10 menit)

Jawab pertanyaan-pertanyaan berikut:

1. Seorang teman submit tugas yang 100% di-generate oleh AI, tanpa modifikasi apapun dan tanpa memahami isinya. Menurut Anda, apa masalahnya? Bagaimana menurut perspektif amanah dalam Islam?
2. Apakah menurut Anda 5 tahun dari sekarang, semua analisis data akan dilakukan oleh AI? Mengapa atau mengapa tidak?
3. Apa tanggung jawab seorang data analyst yang menggunakan AI dalam analisisnya?

---

## Rangkuman Modul

| Konsep | Poin Penting |
|--------|-------------|
| **AI sebagai Co-Analyst** | AI mampu membantu coding, menjelaskan konsep, dan brainstorming, tetapi tidak bisa menggantikan pemahaman, judgment, dan tanggung jawab |
| **Prompt Engineering** | Prompt yang efektif memiliki konteks, role, instruksi spesifik, data, dan ekspektasi output yang jelas (CRIDE) |
| **Workflow Human-AI** | 6 langkah: Human defines → AI drafts → Human reviews → AI codes → Human verifies → Iterate |
| **Kesalahan AI** | Hallucination, wrong test, overclaiming causation, ignoring assumptions — selalu verifikasi |
| **Dokumentasi** | Transparansi penggunaan AI adalah prinsip etika dan reproducibility fundamental |
| **Etika Islam** | Amanah (jujur), keadilan (fair use), ihsan (excellence) — landasan penggunaan AI yang bertanggung jawab |
| **The Future** | AI membuat fondasi statistik LEBIH penting, bukan kurang — karena kita perlu mengevaluasi apa yang AI hasilkan |

---

## Referensi

### Referensi Utama
1. UNESCO. (2021). *Recommendation on the Ethics of Artificial Intelligence*. UNESCO Digital Library.
2. ACM. (2018). *ACM Code of Ethics and Professional Conduct*. Association for Computing Machinery.

### Referensi Pendukung
3. Mollick, E. (2024). *Co-Intelligence: Living and Working with AI*. Portfolio/Penguin.
4. Crawford, K. (2021). *Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence*. Yale University Press.

### Referensi Islam dan Etika
5. Abdallah, S. & Mohtar, S. (2023). "Artificial Intelligence in Islamic Ethics: Challenges and Opportunities." *Journal of Islamic Ethics*, 7(1), 1-28.

### Bacaan Lanjutan
6. Google AI Principles — [ai.google/principles](https://ai.google/principles)
7. Anthropic Usage Policy — [anthropic.com/usage-policy](https://www.anthropic.com/usage-policy)

---

## Persiapan Minggu Depan

Minggu 15 adalah **Presentasi Proyek Akhir**. Pastikan:

1. **Notebook** sudah lengkap dan semua cell sudah dijalankan
2. **Laporan** (3-5 halaman) sudah final
3. **Slide presentasi** sudah siap (10 menit per kelompok)
4. **AI Usage Log** sudah terdokumentasi lengkap
5. **Latih presentasi** — siapkan pembagian peran dalam kelompok
6. **Siapkan mental** untuk Q&A — pahami setiap langkah analisis kalian

---

*Modul ini merupakan bagian dari mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia. Semester Genap 2025/2026.*
