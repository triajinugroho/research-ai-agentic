# BAB 13: AI-AUGMENTED DATA ANALYSIS

**Tri Aji Nugroho, S.T., M.T.**
Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-7.6 | Menjelaskan kemampuan dan keterbatasan AI (LLM) sebagai co-analyst dalam analisis data statistik | C2 |
| CPMK-7.7 | Merancang prompt yang efektif untuk berbagai tugas analisis statistik menggunakan framework CRIDE | C6 |
| CPMK-7.8 | Mengevaluasi output AI secara kritis dan memvalidasi kebenaran analisis statistik yang dihasilkan AI | C5 |
| CPMK-7.9 | Merancang workflow kolaborasi Human-AI untuk analisis data end-to-end yang bertanggung jawab | C6 |
| CPMK-7.10 | Mengevaluasi implikasi etis penggunaan AI dalam riset dan analisis data, termasuk perspektif nilai-nilai Islami | C5 |

---

## 13.1 AI Sebagai Co-Analyst: Paradigma Baru dalam Analisis Data

### 13.1.1 Evolusi Peran AI dalam Analisis Data

Sepanjang 12 bab sebelumnya, kita telah membangun fondasi statistika yang kokoh — dari statistika deskriptif, probabilitas, inferensi, regresi, ANOVA, hingga machine learning. Kini, di bab penutup ini, kita membahas bagaimana **AI (Artificial Intelligence)**, khususnya **Large Language Models (LLM)** seperti ChatGPT, Claude, dan Gemini, dapat menjadi **mitra kerja** (co-analyst) dalam proses analisis data.

Paradigma ini bukan tentang menggantikan kemampuan statistik yang telah kalian pelajari, melainkan tentang **memperkuat** dan **mempercepat** proses analisis dengan memanfaatkan AI secara cerdas dan bertanggung jawab.

```
EVOLUSI PERAN TEKNOLOGI DALAM ANALISIS DATA
────────────────────────────────────────────

Era 1: Manual (sebelum 1960-an)
  [Manusia] ──── hitung tangan ────► [Hasil]
  Alat: tabel statistik, kalkulator mekanik

Era 2: Komputasi (1960-2010)
  [Manusia] ──── software ────► [Hasil]
  Alat: SPSS, SAS, R, Python

Era 3: AI-Augmented (2020-an)
  [Manusia] ◄──── kolaborasi ────► [AI]
       │                              │
       └──── keputusan bersama ──────►[Hasil]
  Alat: LLM + Python + domain knowledge

Catatan: Manusia TETAP di pusat keputusan di setiap era.
```

### 13.1.2 Apa yang Bisa Dilakukan AI untuk Analisis Data?

Selama semester ini, sebagian dari kalian mungkin sudah menggunakan AI untuk membantu tugas-tugas. Mari kita formalkan pemahaman tentang apa yang **bisa** dan **tidak bisa** dilakukan AI.

**AI Mampu:**

| Kemampuan | Contoh Penggunaan |
|-----------|-------------------|
| **Menjelaskan konsep** | "Jelaskan perbedaan precision dan recall dengan analogi sederhana" |
| **Menulis kode** | Generate kode Python untuk visualisasi, uji statistik, machine learning |
| **Debugging** | Menemukan error dalam kode dan menyarankan perbaikan |
| **Interpretasi output** | Menjelaskan arti output `classification_report` atau ANOVA |
| **Menyarankan metode** | "Data saya seperti ini, uji statistik apa yang tepat?" |
| **Brainstorming** | Membantu merumuskan pertanyaan penelitian atau hipotesis |
| **Menyusun narasi** | Membantu menulis laporan analisis dalam bahasa yang baik |

### 13.1.3 Keterbatasan AI yang Wajib Dipahami

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

> **Prinsip utama:** AI adalah **alat yang sangat kuat** tetapi **bukan pengganti pemahaman**. Seperti kalkulator tidak menggantikan pemahaman matematika, AI tidak menggantikan pemahaman statistik.

---

## 13.2 Prompt Engineering untuk Analisis Statistik

### 13.2.1 Mengapa Prompt Penting?

Kualitas output AI sangat bergantung pada kualitas **prompt** (instruksi) yang diberikan. Prompt yang baik menghasilkan jawaban yang relevan dan akurat. Prompt yang buruk menghasilkan jawaban yang generik atau bahkan menyesatkan.

Perhatikan perbedaan berikut:

**Prompt buruk:**
```
Analisis data saya.
```

**Prompt baik:**
```
Saya punya data nilai ujian 30 mahasiswa Informatika UAI.
Distribusinya right-skewed berdasarkan histogram.
Saya ingin menguji apakah rata-rata nilai berbeda dari 75.
Data berbentuk numerik kontinu, satu kelompok.
Uji statistik apa yang tepat dan mengapa?
Berikan kode Python menggunakan scipy.stats.
```

Prompt kedua menghasilkan jawaban yang jauh lebih akurat karena memberikan **konteks**, **deskripsi data**, **pertanyaan spesifik**, dan **format output** yang diharapkan.

### 13.2.2 Framework CRIDE untuk Prompt Statistik

```
┌─────────────────────────────────────────────────────────────┐
│              FRAMEWORK CRIDE UNTUK PROMPT AI                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  C ── Context                                               │
│       Siapa Anda? Apa yang sedang dikerjakan?               │
│       "Saya mahasiswa Informatika semester 2 yang sedang    │
│        menganalisis data survei kepuasan mahasiswa."        │
│                                                             │
│  R ── Role                                                  │
│       Peran apa yang dimainkan AI?                          │
│       "Bertindak sebagai tutor statistik yang sabar."       │
│                                                             │
│  I ── Instruction                                           │
│       Apa yang harus dilakukan AI? (Spesifik!)             │
│       "Bantu saya memilih uji statistik yang tepat."       │
│                                                             │
│  D ── Data                                                  │
│       Informasi tentang dataset Anda.                       │
│       "200 baris, 5 kolom, variabel dependen ordinal."     │
│                                                             │
│  E ── Expectation                                           │
│       Format output yang diharapkan.                        │
│       "Jelaskan dalam 3 langkah, sertakan kode Python."    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 13.2.3 Contoh Prompt untuk Berbagai Tugas Analisis

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

### 13.2.4 Teknik Prompt Lanjutan

Selain framework CRIDE, beberapa teknik prompt lanjutan yang berguna untuk analisis statistik:

| Teknik | Deskripsi | Contoh Penggunaan |
|--------|-----------|-------------------|
| **Chain-of-Thought** | Minta AI berpikir langkah demi langkah | "Pikirkan step by step sebelum memberikan jawaban akhir" |
| **Few-shot** | Berikan contoh input-output yang diinginkan | "Contoh interpretasi yang baik: ... Sekarang interpretasikan output ini: ..." |
| **Persona** | Tetapkan peran spesifik untuk AI | "Anda adalah seorang statistikawan senior yang kritis dan teliti" |
| **Constraint** | Batasi cakupan jawaban AI | "Jelaskan hanya menggunakan konsep yang sudah diajarkan di mata kuliah statistika dasar" |
| **Self-correction** | Minta AI mengevaluasi jawabannya sendiri | "Setelah menjawab, periksa kembali apakah ada kesalahan dalam jawabanmu" |

---

## 13.3 Workflow AI-Augmented Analysis

### 13.3.1 Alur Kolaborasi Human-AI 6 Langkah

Berikut adalah workflow yang direkomendasikan untuk kolaborasi Human-AI dalam analisis data:

```
┌─────────────────────────────────────────────────────────────────┐
│                WORKFLOW HUMAN-AI COLLABORATION                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐                                               │
│  │ 1. HUMAN     │  Definisikan pertanyaan penelitian            │
│  │    DEFINES   │  Pahami konteks dan tujuan analisis           │
│  │    QUESTION  │  >>> AI TIDAK BISA melakukan ini untuk Anda   │
│  └──────┬───────┘                                               │
│         v                                                       │
│  ┌──────────────┐                                               │
│  │ 2. AI DRAFTS │  Minta AI menyusun rencana analisis          │
│  │    ANALYSIS  │  "Berdasarkan pertanyaan X, susun rencana     │
│  │    PLAN      │   analisis step-by-step"                      │
│  └──────┬───────┘                                               │
│         v                                                       │
│  ┌──────────────┐                                               │
│  │ 3. HUMAN     │  Review rencana: apakah masuk akal?           │
│  │    REVIEWS   │  Sesuaikan dengan pengetahuan domain          │
│  │    & ADJUSTS │  Tambahkan/hapus langkah yang perlu           │
│  └──────┬───────┘                                               │
│         v                                                       │
│  ┌──────────────┐                                               │
│  │ 4. AI        │  Minta AI menulis kode Python                 │
│  │    GENERATES │  "Tuliskan kode untuk langkah 1-3..."         │
│  │    CODE      │  Review kode sebelum menjalankan              │
│  └──────┬───────┘                                               │
│         v                                                       │
│  ┌──────────────┐                                               │
│  │ 5. HUMAN     │  Jalankan kode, periksa output                │
│  │    VERIFIES  │  Apakah hasilnya masuk akal?                  │
│  │  & INTERPRETS│  Interpretasikan dalam konteks domain         │
│  └──────┬───────┘                                               │
│         v                                                       │
│  ┌──────────────┐                                               │
│  │ 6. ITERATE   │  Ulangi jika perlu                            │
│  │              │  Perbaiki analisis berdasarkan temuan          │
│  │              │  Minta AI membantu menyempurnakan             │
│  └──────────────┘                                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 13.3.2 Aturan Emas Kolaborasi Human-AI

1. **Selalu mulai dari pertanyaan ANDA** — Jangan minta AI merumuskan pertanyaan penelitian. Kemampuan merumuskan pertanyaan yang bermakna adalah keterampilan manusia yang tidak bisa digantikan AI.

2. **Review setiap output AI** — Jangan copy-paste tanpa memahami. Perlakukan output AI seperti **draft pertama** dari seorang asisten junior yang cerdas tetapi bisa salah.

3. **Jalankan kode dan periksa** — AI bisa generate kode yang error atau menghasilkan output yang salah secara diam-diam (*silent errors*).

4. **Interpretasi tetap tanggung jawab ANDA** — AI bisa membantu menjelaskan, tetapi keputusan akhir tentang makna dan implikasi temuan ada di tangan Anda.

5. **Dokumentasikan semuanya** — Catat prompt, output, dan modifikasi yang dilakukan. Ini penting untuk reproducibility dan integritas akademik.

### 13.3.3 Contoh Penerapan Workflow: Analisis Tips Restoran

Berikut ilustrasi penerapan workflow 6 langkah menggunakan dataset `tips` dari seaborn:

**Langkah 1 — Human Defines Question (tanpa AI):**
```
Pertanyaan penelitian:
1. Apakah ada perbedaan rata-rata tip antara waktu makan siang dan malam?
2. Faktor apa saja yang memprediksi besarnya tip?
```

**Langkah 2 — AI Drafts Analysis Plan:**
```
Prompt ke AI:
"Saya memiliki dataset restoran dengan kolom: total_bill (float),
tip (float), sex (Male/Female), smoker (Yes/No), day (Thur/Fri/Sat/Sun),
time (Lunch/Dinner), size (int).

Pertanyaan: [masukkan pertanyaan di atas]
Susun rencana analisis step-by-step."
```

**Langkah 3 — Human Reviews:** Periksa apakah AI menyarankan cek asumsi normalitas, homogenitas varians, dan effect size (sering terlewat oleh AI).

**Langkah 4 — AI Generates Code:** Minta kode Python untuk setiap langkah analisis.

**Langkah 5 — Human Verifies:** Jalankan kode, periksa output, interpretasikan sendiri.

**Langkah 6 — Iterate:** Perbaiki jika diperlukan, minta AI membantu menyempurnakan.

---

## 13.4 Menggunakan AI untuk Tahapan Analisis Data

### 13.4.1 AI untuk Exploratory Data Analysis (EDA)

AI sangat membantu dalam tahap EDA karena mampu menyarankan visualisasi dan ringkasan statistik yang relevan berdasarkan tipe data.

**Contoh prompt EDA:**
```
Dataset saya memiliki 500 baris dan kolom berikut:
- usia (int): 18-65 tahun
- pendapatan (float): dalam juta Rupiah
- pendidikan (kategorikal): SMA, D3, S1, S2
- kota (kategorikal): Jakarta, Bandung, Surabaya, Yogyakarta
- kepuasan (ordinal, 1-5)

Buatkan kode Python untuk EDA lengkap yang mencakup:
1. Ringkasan statistik per variabel
2. Distribusi setiap variabel numerik (histogram + KDE)
3. Distribusi variabel kategorikal (bar chart)
4. Korelasi antar variabel numerik (heatmap)
5. Deteksi outlier menggunakan boxplot dan IQR method
6. Pengecekan missing values

Gunakan matplotlib dan seaborn. Berikan komentar penjelasan.
```

### 13.4.2 AI untuk Hypothesis Generation

AI dapat membantu brainstorming hipotesis berdasarkan deskripsi dataset dan temuan awal EDA. Namun, **judgment tentang relevansi hipotesis tetap di tangan peneliti**.

**Contoh prompt:**
```
Dari EDA saya menemukan bahwa:
- Pendapatan memiliki distribusi right-skewed
- Ada korelasi positif antara usia dan pendapatan (r = 0.65)
- Mahasiswa S2 memiliki median pendapatan lebih tinggi dari S1
- Ada outlier pendapatan di kota Jakarta

Berdasarkan temuan ini, sarankan 3-5 hipotesis statistik
yang layak diuji. Untuk setiap hipotesis, sebutkan:
- H0 dan H1
- Uji statistik yang tepat
- Alasan mengapa hipotesis ini menarik untuk diuji
```

### 13.4.3 AI untuk Code Writing dan Debugging

Ini adalah salah satu kekuatan utama AI — menulis kode Python dengan cepat dan membantu memperbaiki error.

```python
# Contoh: Minta AI menulis kode untuk Two-Way ANOVA
# Prompt: "Tulis kode Python untuk Two-Way ANOVA
# dengan variabel dependen 'tip' dan variabel independen
# 'time' dan 'smoker'. Cek asumsi, jalankan ANOVA,
# dan buat interaction plot."

# AI mungkin menghasilkan kode seperti ini:
import pandas as pd
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load data
tips = sns.load_dataset('tips')

# 1. Cek asumsi normalitas per kelompok
groups = tips.groupby(['time', 'smoker'])['tip']
print("=== Uji Normalitas (Shapiro-Wilk) ===")
for name, group in groups:
    stat, p = stats.shapiro(group)
    print(f"  {name}: W={stat:.4f}, p={p:.4f}")

# 2. Cek homogenitas varians (Levene's test)
stat, p = stats.levene(
    tips[tips['time']=='Lunch']['tip'],
    tips[tips['time']=='Dinner']['tip']
)
print(f"\nLevene's test: F={stat:.4f}, p={p:.4f}")

# 3. Two-Way ANOVA
model = ols('tip ~ C(time) * C(smoker)', data=tips).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("\n=== Two-Way ANOVA ===")
print(anova_table)

# CHECKLIST EVALUASI KODE AI:
# [?] Apakah kode mengecek asumsi normalitas?  --> Ya
# [?] Apakah kode mengecek homogenitas varians? --> Ya
# [?] Apakah interaksi dimasukkan dalam model?  --> Ya (*)
# [?] Apakah ada post-hoc test?                 --> TIDAK (perlu ditambah)
# [?] Apakah ada effect size?                   --> TIDAK (perlu ditambah)
```

> **Perhatikan:** Kode yang dihasilkan AI seringkali **hampir benar** tetapi **tidak lengkap**. Dalam contoh di atas, AI tidak menyertakan post-hoc test dan effect size. Inilah mengapa **review oleh manusia** sangat penting.

### 13.4.4 AI untuk Interpretasi Hasil

AI sangat baik dalam menjelaskan output statistik dalam bahasa yang mudah dipahami. Namun, waspadalah terhadap **over-interpretation** dan **klaim kausalitas** yang tidak didukung desain penelitian.

**Contoh prompt interpretasi:**
```
Berikut output Two-Way ANOVA saya:

                    sum_sq     df        F    PR(>F)
C(time)            2.3456    1.0    2.145    0.1448
C(smoker)          0.8912    1.0    0.815    0.3677
C(time):C(smoker)  3.7621    1.0    3.441    0.0649
Residual         264.1234  241.0      NaN       NaN

Interpretasikan hasil ini. Apakah ada efek signifikan?
Apakah ada interaksi? Apa artinya dalam konteks restoran?
Jangan membuat klaim kausal — ini bukan data eksperimen.
```

---

## 13.5 Validasi dan Verifikasi Output AI

### 13.5.1 Mengapa Validasi Kritis Sangat Penting?

AI bisa salah — dan sering salah secara **meyakinkan**. Berikut adalah kesalahan-kesalahan yang **sering** dilakukan AI dalam konteks analisis statistik:

| Jenis Kesalahan | Contoh | Cara Mendeteksi |
|-----------------|--------|-----------------|
| **Hallucinated statistics** | "Menurut studi Smith (2023), p-value-nya 0.003..." (studi tidak ada) | Verifikasi referensi, hitung sendiri |
| **Wrong test recommendation** | Merekomendasikan t-test padahal data tidak normal dan sampel kecil | Cek asumsi sendiri sebelum mengikuti saran AI |
| **Incorrect interpretation** | "p > 0.05 berarti H0 terbukti benar" (salah! seharusnya "gagal menolak H0") | Bandingkan dengan materi kuliah dan textbook |
| **Fabricated output** | Generate output Python yang "terlihat benar" tapi sebenarnya dibuat-buat | Selalu jalankan kode sendiri |
| **Overclaiming causation** | "X menyebabkan Y" padahal hanya menunjukkan korelasi | Terapkan critical thinking tentang desain studi |
| **Ignoring assumptions** | Langsung menjalankan ANOVA tanpa cek normalitas dan homogenitas varians | Selalu cek asumsi terlebih dahulu |

### 13.5.2 Red Flags: Kapan Harus Waspada

Waspadalah ketika AI:
- Memberikan angka yang **terlalu presisi** tanpa menjalankan kode (misal: "p-value = 0.00342")
- Menyatakan sesuatu dengan **sangat yakin** tanpa menyebutkan asumsi atau keterbatasan
- Merekomendasikan metode **tanpa menjelaskan** mengapa metode itu dipilih
- Mengutip **referensi** yang tidak bisa kalian temukan di Google Scholar
- Memberikan interpretasi yang **bertentangan** dengan materi kuliah kalian

### 13.5.3 Checklist Verifikasi Output AI

Gunakan checklist berikut setiap kali menerima output dari AI:

```
CHECKLIST VERIFIKASI OUTPUT AI
──────────────────────────────

KODE:
[ ] Apakah saya memahami setiap baris kode?
[ ] Apakah library yang diimpor sudah tersedia?
[ ] Apakah kode berjalan tanpa error?
[ ] Apakah output sesuai dengan yang diharapkan?
[ ] Apakah ada silent error (kode jalan tapi hasil salah)?

METODE STATISTIK:
[ ] Apakah metode yang dipilih sesuai dengan tipe data?
[ ] Apakah asumsi metode diperiksa terlebih dahulu?
[ ] Apakah ada metode alternatif yang lebih tepat?
[ ] Apakah post-hoc test dilakukan (jika diperlukan)?
[ ] Apakah effect size dihitung?

INTERPRETASI:
[ ] Apakah interpretasi p-value benar?
[ ] Apakah ada klaim kausal yang tidak didukung data?
[ ] Apakah keterbatasan disebutkan?
[ ] Apakah interpretasi masuk akal secara domain knowledge?
[ ] Apakah referensi yang dikutip AI benar-benar ada?
```

### 13.5.4 Contoh Praktis: Mengevaluasi Klaim AI

Berikut adalah empat "jawaban AI" terhadap pertanyaan statistik. Identifikasi mana yang **benar** dan mana yang **salah**:

**Klaim 1 — AI bilang:** "P-value 0.03 berarti ada 3% probabilitas bahwa H0 benar."

> **Evaluasi:** SALAH. P-value bukan probabilitas H0 benar. P-value adalah probabilitas mendapatkan hasil seextrem atau lebih ekstrem dari yang diamati, **jika H0 benar**. Ini adalah salah satu miskonsepsi paling umum, dan AI sering memperparahnya.

**Klaim 2 — AI bilang:** "Karena R-squared = 0.95, maka model regresi ini sangat bagus dan tidak perlu perbaikan."

> **Evaluasi:** PERLU KOREKSI. R-squared tinggi tidak selalu berarti model baik. Perlu diperiksa: residual plot (apakah ada pola?), multikolinearitas, overfitting, dan apakah hubungan memang linear. R-squared 0.95 bisa jadi terlalu tinggi dan mengindikasikan masalah.

**Klaim 3 — AI bilang:** "k-NN tidak memerlukan data yang di-standardisasi."

> **Evaluasi:** SALAH. k-NN menggunakan jarak (distance) untuk klasifikasi. Jika fitur memiliki skala yang berbeda (misalnya usia dalam tahun vs pendapatan dalam jutaan), fitur dengan skala besar akan mendominasi perhitungan jarak. Standardisasi sangat diperlukan.

**Klaim 4 — AI bilang:** "Untuk membandingkan 2 kelompok, gunakan ANOVA."

> **Evaluasi:** TIDAK SALAH, tapi KURANG TEPAT. ANOVA memang bisa membandingkan 2 kelompok (hasilnya setara dengan t-test), tetapi **t-test** lebih tepat dan lebih umum digunakan untuk 2 kelompok. ANOVA dirancang untuk 3 kelompok atau lebih.

---

## 13.6 Etika AI dalam Analisis Data

### 13.6.1 Prinsip Etika AI dalam Konteks Akademik

| Prinsip | Penjelasan | Implementasi |
|---------|------------|-------------|
| **Transparansi** | Jujur tentang penggunaan AI | Dokumentasi lengkap di setiap tugas |
| **Accountability** | Bertanggung jawab atas hasil akhir | Anda yang menandatangani, Anda yang bertanggung jawab |
| **Competence** | Mampu menjelaskan apa yang dikerjakan | Jika tidak bisa menjelaskan, jangan klaim sebagai pekerjaan Anda |
| **Integrity** | Tidak menyesatkan tentang kontribusi AI | Bedakan mana pemikiran Anda, mana bantuan AI |
| **Fairness** | Tidak menggunakan AI untuk keuntungan yang tidak adil | Ikuti kebijakan AI yang berlaku |

### 13.6.2 Bias dalam AI dan Implikasinya

AI dilatih dari data yang dibuat oleh manusia, sehingga bisa mewarisi dan memperkuat bias yang ada. Dalam konteks analisis data, bias AI dapat muncul dalam bentuk:

```
SUMBER BIAS DALAM AI
─────────────────────

1. TRAINING DATA BIAS
   Data pelatihan AI didominasi oleh konteks Barat/Amerika
   --> AI mungkin menyarankan metode yang kurang relevan
       untuk konteks Indonesia

2. CONFIRMATION BIAS
   AI cenderung mengkonfirmasi asumsi yang diberikan dalam prompt
   --> Jika Anda bilang "data saya normal", AI mungkin
       tidak menyarankan pengecekan

3. POPULARITY BIAS
   AI cenderung merekomendasikan metode yang populer
   --> Metode yang lebih tepat tapi kurang dikenal bisa terlewat
       (contoh: merekomendasikan Pearson padahal Spearman lebih tepat)

4. SURVIVORSHIP BIAS
   AI belajar dari contoh-contoh "sukses"
   --> Mungkin tidak memperingatkan tentang kegagalan umum
```

### 13.6.3 Tanggung Jawab Pengguna AI

Sebagai pengguna AI dalam analisis data, tanggung jawab Anda meliputi:

1. **Memvalidasi setiap output** — Jangan pernah mempercayai output AI tanpa verifikasi
2. **Memahami metode yang digunakan** — Jika AI menyarankan metode yang tidak Anda pahami, pelajari dulu sebelum menggunakannya
3. **Menjaga kerahasiaan data** — Jangan mengunggah data sensitif atau rahasia ke AI tools publik
4. **Mengakui keterbatasan** — Jika AI membantu, nyatakan secara transparan dalam laporan
5. **Bertanggung jawab atas kesimpulan** — AI bisa membantu analisis, tetapi kesimpulan akhir adalah tanggung jawab Anda

---

## 13.7 Responsible AI Framework dan Nilai-Nilai Islami

### 13.7.1 Perspektif Islam tentang Etika Penggunaan AI

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

> **Hadits relevan:** *"Sesungguhnya Allah menyukai jika seseorang mengerjakan sesuatu pekerjaan, ia mengerjakannya dengan itqan (sempurna/sungguh-sungguh)."* (HR. Thabrani)
>
> Menggunakan AI tools dengan bijak, bertanggung jawab, dan jujur adalah bentuk **itqan** dalam era digital.

### 13.7.2 Framework Responsible AI untuk Mahasiswa

Berikut framework praktis yang mengintegrasikan prinsip etika umum dan nilai Islami:

```
RESPONSIBLE AI FRAMEWORK UNTUK ANALISIS DATA
─────────────────────────────────────────────

         ┌─────────────────────┐
         │   AMANAH            │
         │   (Tanggung jawab   │
         │    atas pemahaman)  │
         └────────┬────────────┘
                  │
    ┌─────────────┼─────────────┐
    │             │             │
    v             v             v
┌────────┐  ┌─────────┐  ┌──────────┐
│KEADILAN│  │ IHSAN   │  │TRANSPARANSI│
│(Adil   │  │(Kualitas│  │(Dokumentasi│
│ dalam  │  │ terbaik)│  │ lengkap)  │
│penggunaan) │         │  │           │
└────┬───┘  └────┬────┘  └─────┬────┘
     │           │             │
     └─────────┬─┘─────────────┘
               │
               v
      ┌────────────────┐
      │   ANALISIS     │
      │   YANG VALID,  │
      │   ETIS, DAN    │
      │   BERMANFAAT   │
      └────────────────┘
```

### 13.7.3 Kapan AI Boleh dan Tidak Boleh Digunakan

| Situasi | Boleh Menggunakan AI? | Alasan |
|---------|----------------------|--------|
| Tugas mingguan | Ya, dengan dokumentasi | AI sebagai alat belajar |
| Proyek akhir | Ya, dengan AI Usage Log | Mencerminkan praktik industri |
| Kuis di kelas | Tidak | Menguji pemahaman individu |
| UTS/UAS | Tidak | Evaluasi kemampuan mandiri |
| Skripsi/penelitian | Ya, dengan disclosure | Standar akademik kontemporer |
| Presentasi | Boleh untuk persiapan | Presentasi harus refleksi pemahaman sendiri |

---

## 13.8 AI Usage Documentation: Best Practices

### 13.8.1 Mengapa Dokumentasi Penting?

Dalam sains dan analisis data, **reproducibility** (kemampuan orang lain untuk mereproduksi hasil Anda) adalah prinsip fundamental. Ketika AI digunakan sebagai bagian dari proses analisis, dokumentasi AI usage menjadi **sama pentingnya** dengan dokumentasi kode dan data.

### 13.8.2 Template Dokumentasi AI

Gunakan template berikut di setiap tugas dan proyek:

```markdown
## Dokumentasi Penggunaan AI

### Informasi Umum
- **AI Tool:** [Claude / ChatGPT / Copilot / lainnya]
- **Versi/Model:** [Claude 3.5 Sonnet / GPT-4o / dll.]
- **Tanggal penggunaan:** [DD/MM/YYYY]
- **Tujuan penggunaan:** [Brainstorming / Coding / Debugging / Interpretasi]

### Log Interaksi

#### Interaksi 1
- **Prompt:** [Copy-paste prompt yang digunakan]
- **Ringkasan output AI:** [Apa yang AI jawab]
- **Apa yang diambil:** [Bagian mana dari output AI yang digunakan]
- **Modifikasi:** [Apa yang diubah dari output AI dan mengapa]
- **Evaluasi:** [Apakah output AI akurat? Ada masalah?]

#### Interaksi 2
- ...

### Refleksi
- **Apa yang AI bantu percepat?** [...]
- **Apa yang AI salah atau kurang tepat?** [...]
- **Apa yang saya pelajari dari interaksi ini?** [...]
- **Apakah saya bisa menjelaskan semua kode/analisis tanpa AI?**
  [Ya/Tidak -- jika tidak, bagian mana?]
```

### 13.8.3 Contoh Dokumentasi yang Baik vs Buruk

**Dokumentasi BURUK:**
> "Menggunakan ChatGPT untuk membantu tugas."

**Dokumentasi BAIK:**
> **Interaksi 1:** Saya bertanya ke Claude cara melakukan Shapiro-Wilk test di Python. Claude memberikan kode menggunakan `scipy.stats.shapiro()`. Saya menggunakan kode tersebut langsung karena sudah sesuai. Output menunjukkan p-value = 0.234, yang saya interpretasikan sendiri sebagai data tidak menyimpang signifikan dari normalitas (gagal menolak H0 pada alpha = 0.05).
>
> **Interaksi 2:** Saya meminta Claude membantu memvisualisasikan residual plot. Kode yang diberikan menggunakan `plt.scatter()` tetapi saya modifikasi menjadi `sns.residplot()` karena hasilnya lebih informatif dan saya sudah familiar dengan seaborn dari Bab 3.

### 13.8.4 Citing AI dalam Karya Akademik

Saat ini belum ada standar universal untuk mengutip AI, tetapi berikut panduan yang bisa diikuti:

**Dalam teks:**
```
"Analisis kode Python untuk visualisasi ini dikembangkan dengan bantuan
Claude (Anthropic, 2025), yang kemudian dimodifikasi oleh penulis untuk
menyesuaikan dengan konteks dataset Indonesia."
```

**Dalam daftar pustaka (gaya APA):**
```
Anthropic. (2025). Claude [Large language model]. https://claude.ai
OpenAI. (2025). ChatGPT [Large language model]. https://chat.openai.com
```

---

## 13.9 Studi Kasus: Analisis End-to-End dengan AI sebagai Co-Analyst

### 13.9.1 Skenario

Seorang mahasiswa Informatika UAI ingin menganalisis dataset `tips` (data restoran) untuk menjawab dua pertanyaan:

1. **Apakah ada perbedaan rata-rata tip antara waktu Lunch dan Dinner?**
2. **Faktor-faktor apa yang mempengaruhi besarnya tip?**

Berikut adalah catatan langkah demi langkah bagaimana ia menggunakan AI sebagai co-analyst.

### 13.9.2 Langkah 1: Persiapan dan Eksplorasi Awal (Manusia)

```python
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats

# Load dataset
tips = sns.load_dataset('tips')

# Eksplorasi awal -- LAKUKAN SENDIRI sebelum bertanya ke AI
print("=== Info Dataset ===")
print(f"Jumlah baris: {len(tips)}")
print(f"Jumlah kolom: {len(tips.columns)}")
print(f"Kolom: {tips.columns.tolist()}")
print()
print("=== Statistik Deskriptif ===")
print(tips.describe())
print()
print("=== Nilai Unik (variabel kategorikal) ===")
for col in tips.select_dtypes(include='object').columns:
    print(f"  {col}: {tips[col].unique().tolist()}")
```

### 13.9.3 Langkah 2: Merumuskan Pertanyaan (Manusia, Tanpa AI)

Pertanyaan penelitian dirumuskan sendiri berdasarkan eksplorasi data. Ini adalah keterampilan yang **tidak boleh didelegasikan ke AI**.

### 13.9.4 Langkah 3: Meminta AI Menyusun Rencana Analisis

```
PROMPT KE AI:
Saya memiliki dataset restoran dengan kolom:
- total_bill (float), tip (float), sex (Male/Female),
  smoker (Yes/No), day (Thur/Fri/Sat/Sun), time (Lunch/Dinner),
  size (int)

Pertanyaan 1: Apakah ada perbedaan rata-rata tip Lunch vs Dinner?
Pertanyaan 2: Faktor apa yang memprediksi besarnya tip?

Susun rencana analisis step-by-step. Untuk setiap langkah,
jelaskan metode, asumsi, dan alasan pemilihan metode.
```

### 13.9.5 Langkah 4-5: Eksekusi dan Verifikasi

```python
# Kode ini di-generate oleh AI, kemudian di-review dan dimodifikasi
# oleh mahasiswa

# --- Pertanyaan 1: t-test Lunch vs Dinner ---

# Pisahkan data
lunch_tips = tips[tips['time'] == 'Lunch']['tip']
dinner_tips = tips[tips['time'] == 'Dinner']['tip']

# Cek asumsi normalitas (DITAMBAHKAN oleh mahasiswa -- AI tidak menyarankan)
print("=== Uji Normalitas (Shapiro-Wilk) ===")
stat_l, p_l = stats.shapiro(lunch_tips)
stat_d, p_d = stats.shapiro(dinner_tips)
print(f"  Lunch:  W={stat_l:.4f}, p={p_l:.4f}")
print(f"  Dinner: W={stat_d:.4f}, p={p_d:.4f}")

# Cek homogenitas varians
stat_lev, p_lev = stats.levene(lunch_tips, dinner_tips)
print(f"\nLevene's test: F={stat_lev:.4f}, p={p_lev:.4f}")

# Karena normalitas terpenuhi --> Independent t-test
t_stat, p_val = stats.ttest_ind(lunch_tips, dinner_tips)
print(f"\nt-test: t={t_stat:.4f}, p={p_val:.4f}")

# Effect size (Cohen's d) -- DITAMBAHKAN oleh mahasiswa
pooled_std = np.sqrt(
    ((len(lunch_tips)-1)*lunch_tips.std()**2 +
     (len(dinner_tips)-1)*dinner_tips.std()**2) /
    (len(lunch_tips)+len(dinner_tips)-2)
)
cohens_d = (dinner_tips.mean() - lunch_tips.mean()) / pooled_std
print(f"Cohen's d: {cohens_d:.4f}")

# --- Pertanyaan 2: Multiple Regression ---
import statsmodels.api as sm
from statsmodels.formula.api import ols

model = ols('tip ~ total_bill + size + C(time) + C(sex) + C(smoker)',
            data=tips).fit()
print("\n=== Regresi Linear Berganda ===")
print(model.summary())
```

### 13.9.6 Langkah 6: Kesimpulan (Ditulis Manusia)

Kesimpulan akhir **harus** ditulis oleh mahasiswa, bukan copy-paste dari AI. AI boleh membantu menjelaskan output, tetapi interpretasi dalam konteks harus asli.

### 13.9.7 Dokumentasi AI Usage

```
AI Usage Log:
- Tool: Claude (Anthropic, 2025)
- Interaksi 1: Minta rencana analisis (digunakan dengan modifikasi)
- Interaksi 2: Minta kode t-test (dimodifikasi: tambah Shapiro-Wilk, effect size)
- Interaksi 3: Minta kode regresi (digunakan, tambah interpretasi sendiri)
- Interaksi 4: Minta bantuan interpretasi output regresi (digunakan sebagian,
  koreksi klaim kausal menjadi korelasional)
```

---

## 13.10 Masa Depan: AI dan Analisis Data

### 13.10.1 Tren yang Sedang Berkembang

| Tren | Penjelasan | Relevansi untuk Mahasiswa |
|------|------------|--------------------------|
| **Agentic AI** | AI yang bisa menjalankan langkah-langkah analisis secara otonom | Analisis data semi-otomatis akan semakin umum |
| **AutoML** | Automated Machine Learning — AI memilih model terbaik secara otomatis | Fondasi statistik tetap perlu untuk mengevaluasi hasil |
| **AI Code Assistants** | GitHub Copilot, Cursor — AI membantu menulis kode real-time | Bisa mempercepat coding, tapi perlu pemahaman untuk mengevaluasi |
| **Multimodal AI** | AI yang memahami teks, gambar, tabel, grafik | Upload grafik dan minta AI menginterpretasi |
| **AI in Scientific Research** | AI membantu literature review, hypothesis generation | Memahami statistik menjadi **lebih** penting, bukan kurang |

### 13.10.2 Keterampilan yang Tetap Relevan di Era AI

```
YANG AI BISA                    YANG MANUSIA TETAP PERLU
TAPI MANUSIA SULIT              DAN AI TIDAK BISA (BELUM)
─────────────────               ──────────────────────────
Menulis kode dalam detik        Memahami KONTEKS:
                                mengapa analisis ini penting?
Mengingat ratusan fungsi        Untuk siapa hasilnya?
dan parameter library
                                Merumuskan PERTANYAAN bermakna:
Menjelaskan konsep dengan       AI menjawab pertanyaan,
berbagai analogi                bukan membuat pertanyaan

Bekerja 24/7 tanpa lelah       JUDGMENT ETIS:
                                apakah analisis ini bisa
Memproses informasi dari        merugikan seseorang?
ribuan textbook
                                KREATIVITAS SEJATI:
                                menghubungkan temuan data
                                dengan pengetahuan dunia nyata

                                TANGGUNG JAWAB:
                                AI tidak bisa "disalahkan"

                                EMPATI DAN KOMUNIKASI:
                                menyampaikan temuan sensitif
                                kepada stakeholder
```

> **Pesan penting:** Perkembangan AI **tidak** membuat statistik menjadi kurang penting. Justru sebaliknya — semakin mudah analisis dilakukan oleh AI, semakin penting kemampuan manusia untuk:
>
> 1. **Merumuskan pertanyaan yang tepat**
> 2. **Mengevaluasi apakah metode yang digunakan AI benar**
> 3. **Menginterpretasi hasil dalam konteks yang bermakna**
> 4. **Mengkomunikasikan temuan kepada stakeholder**
>
> Ini semua membutuhkan **fondasi statistik yang kuat** — yang kalian telah bangun selama 13 bab ini.

> **Kesimpulan paradigma:** AI adalah co-pilot terbaik yang bisa Anda miliki. Tetapi **pilot-nya tetap Anda**.

---

## AI Corner: Meta — Menggunakan AI untuk Belajar tentang AI

### AI Corner 13.1: Prompt untuk Memahami Kemampuan AI

Ironisnya, salah satu cara terbaik untuk memahami kemampuan dan keterbatasan AI adalah dengan **bertanya langsung ke AI** tentang hal tersebut. Cobalah prompt-prompt berikut:

**Prompt 1: Memahami Keterbatasan**
```
Saya sedang belajar menggunakan AI untuk analisis data statistik.
Berikan 5 contoh spesifik di mana kamu (sebagai AI) kemungkinan
besar akan memberikan jawaban yang salah atau menyesatkan dalam
konteks statistik. Untuk setiap contoh, jelaskan mengapa kamu
bisa salah dan bagaimana pengguna bisa mendeteksinya.
```

**Prompt 2: Self-Evaluation**
```
Saya akan memberikan sebuah output statistik. Tolong interpretasikan,
tetapi setelah selesai, evaluasi jawabanmu sendiri. Berikan rating
confidence (1-10) untuk setiap bagian interpretasimu. Bagian mana
yang paling mungkin salah?
```

**Prompt 3: Adversarial Testing**
```
Saya ingin menguji kemampuanmu. Saya akan mengklaim bahwa data saya
normal berdasarkan histogram, meskipun sebenarnya saya belum menjalankan
uji normalitas. Apakah kamu akan langsung mengikuti asumsi saya,
atau kamu akan menyarankan pengecekan formal?
```

### AI Corner 13.2: Eksperimen Perbandingan AI Tools

| Aspek | Eksperimen yang Bisa Dicoba |
|-------|----------------------------|
| **Konsistensi** | Berikan prompt yang sama ke AI tool yang sama, tiga kali. Apakah hasilnya konsisten? |
| **Perbandingan** | Berikan prompt yang sama ke ChatGPT dan Claude. Bandingkan kualitas jawabannya |
| **Adversarial** | Sengaja berikan informasi yang salah ke AI. Apakah AI mengoreksi atau mengikuti? |
| **Reproducibility** | Minta teman menggunakan prompt yang sama. Apakah hasilnya identik? |

### AI Corner 13.3: Refleksi Metakognitif

Setelah menggunakan AI untuk analisis data, tanyakan pada diri sendiri:

1. **Apakah saya benar-benar memahami** kode yang dihasilkan AI, atau hanya copy-paste?
2. **Apakah saya bisa menjelaskan** setiap langkah analisis kepada teman yang tidak menggunakan AI?
3. **Apakah saya belajar sesuatu** dari interaksi ini, atau saya hanya "menyelesaikan tugas"?
4. **Jika AI tidak tersedia**, apakah saya tetap bisa menyelesaikan analisis ini (mungkin lebih lambat, tetapi tetap bisa)?

Jika jawaban pertanyaan 1-3 adalah "tidak", maka Anda perlu memperdalam pemahaman. Jika jawaban pertanyaan 4 adalah "tidak", maka Anda terlalu bergantung pada AI.

---

## Rangkuman Bab 13

1. **AI sebagai co-analyst** adalah paradigma baru dalam analisis data di mana AI (khususnya LLM) membantu mempercepat proses coding, interpretasi, dan brainstorming — tetapi **tidak menggantikan** pemahaman statistik, critical thinking, dan judgment manusia.

2. **Prompt engineering** yang efektif menggunakan framework **CRIDE** (Context, Role, Instruction, Data, Expectation). Prompt yang spesifik dan terstruktur menghasilkan output AI yang jauh lebih akurat dibandingkan prompt yang generik.

3. **Workflow Human-AI** terdiri dari 6 langkah: Human defines question, AI drafts plan, Human reviews, AI generates code, Human verifies and interprets, kemudian Iterate. Langkah 1 dan 5 adalah **tanggung jawab eksklusif manusia**.

4. **Validasi output AI** sangat penting karena AI sering melakukan kesalahan seperti hallucination, wrong test recommendation, overclaiming causation, dan mengabaikan asumsi. Gunakan checklist verifikasi untuk setiap output AI.

5. **Dokumentasi penggunaan AI** (AI Usage Log) adalah prinsip fundamental untuk menjaga transparansi, reproducibility, dan integritas akademik. Dokumentasi yang baik mencatat prompt, output, modifikasi, dan refleksi.

6. **Etika AI** dalam konteks akademik mencakup transparansi, accountability, competence, integrity, dan fairness. Nilai-nilai Islami — **amanah** (kepercayaan), **keadilan** (al-'adl), dan **ihsan** (keunggulan) — memberikan landasan moral yang kuat untuk penggunaan AI yang bertanggung jawab.

7. **Fondasi statistik menjadi lebih penting** di era AI, bukan kurang penting. Kemampuan merumuskan pertanyaan, mengevaluasi metode, menginterpretasi hasil, dan mengkomunikasikan temuan adalah keterampilan manusia yang tidak bisa digantikan oleh AI.

8. **AI adalah co-pilot, bukan pilot.** Keputusan akhir, tanggung jawab, dan integritas hasil analisis selalu berada di tangan analis manusia.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan antara menggunakan AI sebagai "pengganti" dan menggunakan AI sebagai "co-analyst" dalam analisis data. Berikan masing-masing satu contoh skenario.

**Soal 2.** Sebutkan dan jelaskan lima komponen framework CRIDE untuk menyusun prompt yang efektif. Berikan contoh masing-masing komponen untuk skenario berikut: Anda ingin AI membantu memilih uji statistik yang tepat untuk membandingkan rata-rata IPK antara mahasiswa yang bekerja part-time dan yang tidak.

**Soal 3.** Identifikasi tiga keterbatasan utama AI (LLM) dalam analisis data statistik. Untuk setiap keterbatasan, jelaskan mengapa keterbatasan tersebut berbahaya jika tidak disadari oleh pengguna.

**Soal 4.** Dalam workflow Human-AI 6 langkah, langkah mana saja yang menjadi tanggung jawab **eksklusif manusia** dan mengapa? Jelaskan konsekuensinya jika langkah-langkah tersebut didelegasikan sepenuhnya ke AI.

### Tingkat Menengah (C2-C3)

**Soal 5.** Perhatikan prompt berikut yang diberikan ke AI:

```
Analisis data saya dan beri tahu hasilnya.
```

- a) Identifikasi kelemahan prompt ini berdasarkan framework CRIDE
- b) Tulis ulang prompt ini menjadi prompt yang efektif, dengan asumsi data Anda adalah survei kepuasan 200 pelanggan e-commerce Indonesia (skala 1-5) terhadap 4 aspek layanan: pengiriman, harga, kualitas produk, dan customer service

**Soal 6.** AI menghasilkan kode Python berikut untuk analisis Anda:

```python
from scipy import stats

# Membandingkan rata-rata gaji 3 departemen
f_stat, p_value = stats.f_oneway(dept_a, dept_b, dept_c)
print(f"P-value: {p_value:.4f}")
if p_value < 0.05:
    print("Ada perbedaan signifikan antar departemen")
```

Evaluasi kode ini menggunakan checklist verifikasi output AI. Sebutkan minimal 4 hal yang **kurang** atau **perlu ditambahkan** dalam kode tersebut.

**Soal 7.** Berikut adalah dua dokumentasi penggunaan AI. Tentukan mana yang baik dan mana yang buruk, kemudian perbaiki dokumentasi yang buruk.

**Dokumentasi A:**
> "Saya menggunakan AI untuk mengerjakan tugas regresi."

**Dokumentasi B:**
> "Interaksi 1: Saya bertanya ke Claude tentang cara mendeteksi outlier menggunakan IQR method. Claude memberikan kode menggunakan pandas. Saya modifikasi threshold dari 1.5 menjadi 3.0 karena domain saya (harga rumah) wajar memiliki sebaran luas. Output: 12 outlier terdeteksi dari 500 data."

**Soal 8.** Tuliskan tiga prompt menggunakan framework CRIDE untuk masing-masing tugas analisis data berikut:
- a) Minta AI membantu EDA untuk dataset penjualan toko online Indonesia
- b) Minta AI menjelaskan kapan menggunakan parametrik vs non-parametrik test
- c) Minta AI membantu menginterpretasi output regresi logistik

### Tingkat Mahir (C5-C6)

**Soal 9.** Seorang teman mengirimkan laporan analisis data berikut ke dosen:

> "Berdasarkan analisis menggunakan ChatGPT, terdapat hubungan kausal antara jumlah jam belajar dan IPK mahasiswa (r = 0.72, p < 0.001). ChatGPT menyimpulkan bahwa meningkatkan jam belajar akan meningkatkan IPK. Model regresi menunjukkan R-squared = 0.52."

- a) Identifikasi minimal 3 masalah dalam laporan ini
- b) Tulis ulang laporan tersebut secara benar dan etis, termasuk dokumentasi penggunaan AI
- c) Dari perspektif nilai amanah dalam Islam, evaluasi apakah laporan ini memenuhi prinsip amanah. Jelaskan.

**Soal 10.** Rancang sebuah **workflow analisis data end-to-end** untuk skenario berikut:

Anda diminta menganalisis data kinerja mahasiswa UAI (500 mahasiswa, 12 variabel termasuk IPK, jumlah kehadiran, aktivitas ekstrakurikuler, status beasiswa, asal sekolah, dll.) untuk memprediksi mahasiswa yang berisiko drop out.

Untuk setiap langkah dalam workflow:
- Tentukan apakah langkah tersebut dilakukan oleh manusia, AI, atau kolaborasi
- Tulis prompt spesifik yang akan diberikan ke AI (jika ada)
- Jelaskan bagaimana Anda akan memvalidasi output AI
- Identifikasi potensi bias atau kesalahan AI di langkah tersebut

**Soal 11.** Lakukan **adversarial testing** terhadap AI dengan skenario berikut:

Anda sengaja memberikan informasi yang salah dalam prompt:
```
Data saya terdistribusi normal (saya yakin dari histogram saja,
belum uji formal). Sampel saya 15 orang. Saya ingin membandingkan
rata-rata 3 kelompok. Tolong langsung jalankan ANOVA one-way.
```

- a) Prediksi bagaimana AI kemungkinan akan merespons
- b) Apa yang **seharusnya** dilakukan AI jika ia sempurna?
- c) Apa risiko jika pengguna langsung mengikuti saran AI tanpa berpikir kritis?
- d) Uji statistik apa yang **sebenarnya** lebih tepat untuk skenario ini, dan mengapa?

**Soal 12.** Tulis esai reflektif (400-500 kata) tentang topik berikut:

*"Dalam 10 tahun ke depan, apakah kemampuan analisis data statistik masih relevan bagi lulusan informatika, mengingat AI semakin canggih? Bagaimana mahasiswa seharusnya mempersiapkan diri?"*

Esai harus mencakup:
- Argumen mengapa fondasi statistik tetap penting
- Contoh konkret keterampilan yang tidak bisa digantikan AI
- Perspektif etis (termasuk nilai-nilai Islami jika relevan)
- Rekomendasi praktis untuk mempersiapkan diri

**Soal 13.** Anda diminta menjadi reviewer untuk laporan analisis data seorang rekan. Rekan Anda menggunakan AI untuk seluruh proses analisis tetapi hanya menulis: "Dibantu oleh ChatGPT." Rancang rubrik penilaian (minimal 5 kriteria) untuk mengevaluasi:
- Kualitas dokumentasi AI usage
- Kedalaman pemahaman konsep statistik
- Ketepatan interpretasi hasil
- Kemandirian dalam merumuskan pertanyaan dan kesimpulan
- Kepatuhan terhadap prinsip etika

**Soal 14.** Perhatikan skenario berikut:

Sebuah startup fintech di Jakarta menggunakan model AI untuk memprediksi kelayakan pinjaman. Model dilatih menggunakan data historis yang kebanyakan berasal dari peminjam di Jakarta dan Surabaya. Ketika model diterapkan untuk mengevaluasi peminjam dari kota-kota kecil di luar Jawa, banyak pengajuan yang ditolak.

- a) Identifikasi jenis bias yang mungkin terjadi
- b) Bagaimana fondasi statistik dapat membantu mendeteksi bias ini?
- c) Apa rekomendasi Anda untuk memperbaiki situasi ini?
- d) Dari perspektif keadilan (al-'adl) dalam Islam, evaluasi etika penggunaan model ini

---

## Referensi

### Referensi Utama
1. Mollick, E. (2024). *Co-Intelligence: Living and Working with AI*. Portfolio/Penguin.
2. UNESCO. (2021). *Recommendation on the Ethics of Artificial Intelligence*. UNESCO Digital Library.
3. ACM. (2018). *ACM Code of Ethics and Professional Conduct*. Association for Computing Machinery.

### Referensi Pendukung
4. Crawford, K. (2021). *Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence*. Yale University Press.
5. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson.
6. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.

### Referensi Islam dan Etika
7. Abdallah, S. & Mohtar, S. (2023). "Artificial Intelligence in Islamic Ethics: Challenges and Opportunities." *Journal of Islamic Ethics*, 7(1), 1-28.

### Bacaan Lanjutan
8. Google AI Principles — [ai.google/principles](https://ai.google/principles)
9. Anthropic Usage Policy — [anthropic.com/usage-policy](https://www.anthropic.com/usage-policy)
10. White, J. et al. (2023). "A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT." *arXiv preprint arXiv:2302.11382*.

---

*Bab berikutnya: **Proyek Akhir — Analisis Data End-to-End dengan AI sebagai Co-Analyst***
