# Minggu 12: Natural Language Processing Dasar

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 12 |
| **Topik** | Natural Language Processing (NLP) Dasar |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-6: Menerapkan dan menganalisis teknik NLP dasar untuk pemrosesan teks |
| **Sub-CPMK** | 12.1 Menerapkan pipeline NLP (preprocessing, vektorisasi, klasifikasi) pada teks bahasa Indonesia |
| | 12.2 Menganalisis hasil sentiment analysis dan mengevaluasi performa model klasifikasi teks |
| **Bloom's Taxonomy** | C3-C4 (Menerapkan-Menganalisis / *Apply-Analyze*) |
| **Durasi** | 2 x 100 menit (Teori 100 min + Praktikum 100 min) |
| **Platform** | Google Colab |
| **Metode** | Ceramah interaktif, demonstrasi, hands-on coding, diskusi kelompok |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** apa itu NLP, mengapa penting, dan bagaimana penerapannya di kehidupan nyata.
2. **Menerapkan** teknik text preprocessing: tokenization, lowercasing, stopword removal, dan stemming.
3. **Mengimplementasikan** preprocessing khusus bahasa Indonesia menggunakan Sastrawi dan Indonesian stopwords.
4. **Menjelaskan** dan menerapkan teknik text representation: Bag of Words dan TF-IDF.
5. **Membangun** pipeline klasifikasi teks lengkap: preprocessing, vektorisasi, training model, evaluasi.
6. **Menganalisis** hasil sentiment analysis pada teks bahasa Indonesia dan mengevaluasi performa model.
7. **Menjelaskan** konsep dasar word embeddings (Word2Vec).

---

## Materi Pembelajaran

### 1. NLP Overview: Apa, Mengapa, dan Aplikasi

#### Apa Itu NLP?

**Natural Language Processing (NLP)** adalah cabang AI yang berhubungan dengan interaksi antara komputer dan bahasa manusia. NLP memungkinkan komputer untuk **memahami**, **menginterpretasi**, dan **menghasilkan** bahasa alami.

```
Teks Manusia → [NLP System] → Pemahaman/Aksi

Contoh:
"Produk ini sangat bagus!" → [Sentiment Analysis] → Positif (95%)
"Apa ibukota Indonesia?" → [Question Answering] → "Jakarta"
"Terjemahkan ke Inggris" → [Machine Translation] → "Translate to English"
```

#### Mengapa NLP Penting?

- **80% data dunia** adalah data tidak terstruktur, sebagian besar berupa teks
- Bahasa manusia sangat kompleks: ambigu, informal, kontekstual
- Permintaan industri sangat tinggi: chatbot, analisis sentimen, pencarian cerdas

#### Aplikasi NLP di Dunia Nyata

| Aplikasi | Contoh | Contoh di Indonesia |
|---|---|---|
| **Sentiment Analysis** | Analisis opini produk/politik | Review Tokopedia/Shopee, opini publik di Twitter |
| **Chatbot** | Asisten virtual | CS otomatis Bank BCA, Telkomsel Virtual Assistant |
| **Machine Translation** | Terjemahan bahasa | Google Translate Indonesia-Inggris |
| **Text Summarization** | Ringkasan otomatis | Rangkuman berita Kompas, Detik |
| **Named Entity Recognition** | Ekstraksi nama, lokasi, organisasi | Ekstraksi entitas dari berita hukum |
| **Spam Detection** | Deteksi email/SMS spam | Filter spam SMS penipuan |
| **Speech Recognition** | Teks dari suara | Google Assistant berbahasa Indonesia |
| **Question Answering** | Menjawab pertanyaan | ChatGPT, Claude |

> **Konteks Indonesia:** NLP untuk bahasa Indonesia memiliki tantangan unik: bahasa informal (slang), campuran bahasa (code-switching Indonesia-Inggris), dan keterbatasan resource dibandingkan NLP bahasa Inggris.

---

### 2. Text Preprocessing: Langkah-langkah Persiapan Teks

#### Mengapa Preprocessing Penting?

Teks mentah penuh dengan "noise" yang tidak berguna untuk analisis. Preprocessing membersihkan dan menstandarkan teks sebelum diproses model ML.

#### Pipeline Preprocessing Teks

```
Teks Mentah
    │
    ▼
1. Lowercasing (huruf kecil)
    │
    ▼
2. Pembersihan (hapus HTML, URL, angka, tanda baca)
    │
    ▼
3. Tokenization (pecah menjadi kata-kata)
    │
    ▼
4. Stopword Removal (hapus kata umum)
    │
    ▼
5. Stemming / Lemmatization (kembalikan ke bentuk dasar)
    │
    ▼
Teks Bersih
```

#### Penjelasan Setiap Langkah

| Langkah | Sebelum | Sesudah |
|---|---|---|
| **Lowercasing** | "Produk Ini BAGUS!!" | "produk ini bagus!!" |
| **Pembersihan** | "produk ini bagus!! 😊 #review" | "produk ini bagus review" |
| **Tokenization** | "produk ini bagus review" | ["produk", "ini", "bagus", "review"] |
| **Stopword Removal** | ["produk", "ini", "bagus", "review"] | ["produk", "bagus", "review"] |
| **Stemming** | ["produk", "bagus", "review"] | ["produk", "bagus", "review"] |

#### Contoh Lengkap

```
Input:  "Pengiriman sangat CEPAT!! Produknya berkualitas. Recommended! 👍"

Setelah preprocessing:
→ lowercasing:    "pengiriman sangat cepat!! produknya berkualitas. recommended! 👍"
→ pembersihan:    "pengiriman sangat cepat produknya berkualitas recommended"
→ tokenization:   ["pengiriman", "sangat", "cepat", "produknya", "berkualitas", "recommended"]
→ stopword:       ["pengiriman", "cepat", "produknya", "berkualitas", "recommended"]
→ stemming:       ["kirim", "cepat", "produk", "kualitas", "recommended"]
```

---

### 3. Indonesian NLP: Sastrawi Stemmer dan Indonesian Stopwords

#### Tantangan NLP Bahasa Indonesia

Bahasa Indonesia memiliki karakteristik unik yang membuat NLP lebih menantang:

| Karakteristik | Contoh | Tantangan |
|---|---|---|
| **Afiksasi** (imbuhan) | me-**lari** → berlari, pelari, larian | Stemming harus mengenali imbuhan |
| **Reduplikasi** | rumah-rumah, sayur-mayur | Perlu penanganan khusus |
| **Informal/slang** | gak, bgt, emg, ga, udh | Perlu normalisasi |
| **Code-switching** | "Produk ini good banget!" | Campuran Indonesia-Inggris |
| **Negasi** | "tidak bagus" vs "bagus" | Mempengaruhi sentimen |

#### Sastrawi: Indonesian Stemmer

**Sastrawi** adalah library stemming bahasa Indonesia yang mengubah kata berimbuhan ke bentuk dasarnya:

```
membelikan  → beli
pembelajaran → ajar
berkualitas  → kualitas
pengiriman  → kirim
```

#### Indonesian Stopwords

**Stopwords** adalah kata-kata umum yang tidak membawa makna penting untuk analisis:

```
Stopwords Indonesia: yang, dan, di, ini, itu, dengan, untuk, dari, pada,
                     tidak, adalah, ke, akan, sudah, juga, atau, ada,
                     saya, kamu, dia, mereka, kami, sangat, bisa, ...
```

---

### 4. Text Representation: Bag of Words dan TF-IDF

#### Masalah: Komputer Tidak Memahami Teks

Model ML hanya bisa memproses angka. Kita perlu mengubah teks menjadi representasi numerik (*feature vector*).

#### a) Bag of Words (BoW)

**Bag of Words** menghitung frekuensi kemunculan setiap kata dalam dokumen. Disebut "bag" karena **tidak memperhatikan urutan kata**.

```
Dokumen 1: "saya suka makan nasi goreng"
Dokumen 2: "dia suka makan mie goreng"
Dokumen 3: "saya tidak suka nasi"

Vocabulary: [saya, suka, makan, nasi, goreng, dia, mie, tidak]

BoW Matrix:
          saya suka makan nasi goreng dia mie tidak
Doc 1:    1    1    1     1    1       0   0   0
Doc 2:    0    1    1     0    1       1   1   0
Doc 3:    1    1    0     1    0       0   0   1
```

**Keterbatasan BoW:**
- Tidak memperhatikan urutan kata
- Tidak mempertimbangkan pentingnya kata
- Vocabulary bisa sangat besar

#### b) TF-IDF (Term Frequency — Inverse Document Frequency)

**TF-IDF** tidak hanya menghitung frekuensi, tapi juga mempertimbangkan **seberapa unik** kata tersebut di seluruh dokumen.

$$\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t)$$

Di mana:
- **TF (Term Frequency):** Frekuensi kata $t$ dalam dokumen $d$
- **IDF (Inverse Document Frequency):** $\log\frac{N}{df(t)}$, di mana $N$ = total dokumen, $df(t)$ = jumlah dokumen yang mengandung kata $t$

```
Kata "suka" muncul di semua dokumen → IDF rendah → kurang penting
Kata "goreng" muncul di 2 dari 3 dokumen → IDF sedang
Kata "mie" muncul di 1 dari 3 dokumen → IDF tinggi → lebih diskriminatif
```

| Metode | Kelebihan | Kekurangan |
|---|---|---|
| **Bag of Words** | Sederhana, mudah dipahami | Tidak ada bobot pentingnya kata |
| **TF-IDF** | Membobot kata berdasarkan kepentingan | Masih tidak menangkap urutan dan konteks |

---

### 5. Text Classification Pipeline

#### Pipeline Lengkap

```
Teks Mentah → Preprocessing → Vektorisasi → Model ML → Prediksi

    "Produk bagus!"                              "Positif"
    "Barang rusak"    → [clean] → [TF-IDF] → [Classifier] → "Negatif"
    "Biasa saja"                                 "Netral"
```

#### Model yang Cocok untuk Text Classification

| Model | Kelebihan | Cocok Untuk |
|---|---|---|
| **Naive Bayes** | Cepat, bekerja baik dengan TF-IDF | Baseline, dataset kecil-sedang |
| **SVM** | Akurasi tinggi di dimensi tinggi | Dataset sedang, teks formal |
| **Logistic Regression** | Cepat, interpretable | Baseline kuat |
| **Random Forest** | Robust, feature importance | Dataset menengah |
| **Deep Learning** | Akurasi terbaik | Dataset besar, teks kompleks |

> **Rekomendasi:** Untuk text classification dasar, mulai dengan **Naive Bayes** atau **SVM** sebagai baseline. Jika akurasi belum cukup, coba model yang lebih kompleks.

---

### 6. Sentiment Analysis pada Teks Indonesia

#### Apa Itu Sentiment Analysis?

**Sentiment analysis** (*opinion mining*) adalah tugas NLP yang menentukan sentimen atau opini dari sebuah teks — apakah **positif**, **negatif**, atau **netral**.

#### Contoh Penerapan di Indonesia

| Platform | Contoh Teks | Sentimen |
|---|---|---|
| **Tokopedia** | "Barang sesuai deskripsi, pengiriman cepat!" | Positif |
| **Shopee** | "Kualitas jelek, bahan tipis, menyesal beli" | Negatif |
| **Google Maps** | "Hotel bersih tapi AC kurang dingin" | Mixed |
| **Twitter/X** | "Kebijakan ini merugikan rakyat kecil" | Negatif |
| **App Store** | "Aplikasi sering crash, tolong diperbaiki" | Negatif |

#### Tantangan Sentiment Analysis Bahasa Indonesia

- **Sarkasme:** "Bagus ya, paket 3 minggu baru sampai" (negatif!)
- **Implisit:** "Ukurannya lebih kecil dari yang diharapkan" (negatif?)
- **Negasi:** "Tidak jelek" (positif atau netral?)
- **Slang:** "barangnya jelek bgt, ga worth it" (perlu normalisasi)

---

### 7. Evaluation Metrics untuk Text Classification

#### Metrik Evaluasi

Untuk evaluasi text classification, kita menggunakan metrik yang sama dengan classification umumnya:

| Metrik | Formula | Interpretasi |
|---|---|---|
| **Accuracy** | $\frac{TP+TN}{Total}$ | Proporsi prediksi benar secara keseluruhan |
| **Precision** | $\frac{TP}{TP+FP}$ | Dari yang diprediksi positif, berapa yang benar positif? |
| **Recall** | $\frac{TP}{TP+FN}$ | Dari yang sebenarnya positif, berapa yang terdeteksi? |
| **F1-Score** | $\frac{2 \times P \times R}{P + R}$ | Harmonic mean precision dan recall |

#### Kapan Mana yang Lebih Penting?

| Skenario | Metrik Utama | Alasan |
|---|---|---|
| Deteksi spam SMS | **Precision** | Jangan sampai SMS penting masuk spam |
| Deteksi konten berbahaya | **Recall** | Lebih baik false alarm daripada konten lolos |
| Sentiment analysis umum | **F1-Score** | Keseimbangan precision dan recall |

---

### 8. Pengantar Word Embeddings (Word2Vec)

#### Keterbatasan BoW dan TF-IDF

Bag of Words dan TF-IDF memperlakukan setiap kata sebagai entitas independen. Mereka tidak menangkap **hubungan semantik** antar kata:

```
BoW/TF-IDF:    "kucing" dan "anjing" → tidak ada hubungan
Word2Vec:      "kucing" dan "anjing" → vektor yang berdekatan (keduanya hewan)
```

#### Konsep Word2Vec

**Word2Vec** (Google, 2013) merepresentasikan setiap kata sebagai vektor berdimensi rendah (biasanya 100-300 dimensi) yang menangkap hubungan semantik:

```
king - man + woman ≈ queen
jakarta - indonesia + japan ≈ tokyo

Ruang Vektor (2D simplified):
    ↑
    | ● raja     ● ratu
    |
    | ● pria     ● wanita
    |
    | ● kucing
    | ● anjing
    |    ● mobil
    +──────────────────→
```

#### Dua Arsitektur Word2Vec

| Model | Deskripsi |
|---|---|
| **CBOW** (Continuous Bag of Words) | Memprediksi kata target dari kata-kata konteks |
| **Skip-Gram** | Memprediksi kata-kata konteks dari kata target |

```
CBOW:     [saya, ke, hari, ini] → prediksi → "pergi"
Skip-Gram: "pergi" → prediksi → [saya, ke, hari, ini]
```

> **Catatan:** Kita hanya membahas konsep dasar Word2Vec di minggu ini. Implementasi mendalam dengan word embeddings akan dibahas di mata kuliah lanjutan (NLP/Deep Learning).

---

## Aktivitas Kelas

### Sesi 1: Teori dan Diskusi (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Pembukaan & Review | Review neural networks, transisi ke NLP |
| 15 menit | Ceramah: NLP Overview | Apa itu NLP, aplikasi, contoh Indonesia |
| 20 menit | Ceramah: Text Preprocessing | Tokenization, stopwords, stemming, demo Indonesian NLP |
| 15 menit | Ceramah: BoW dan TF-IDF | Representasi teks, perbedaan, kapan digunakan |
| 15 menit | Ceramah: Sentiment Analysis & Evaluation | Pipeline klasifikasi teks, metrik evaluasi |
| 10 menit | Ceramah: Word Embeddings | Konsep Word2Vec (pengantar singkat) |
| 5 menit | Pengumuman | **K3 Kuis: Advanced ML (Minggu 9-12) — diumumkan** |
| 10 menit | Rangkuman & Transisi | Key takeaways, persiapan hands-on |

### Sesi 2: Hands-on Praktikum (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Setup & Install | Install Sastrawi, import libraries, load dataset |
| 20 menit | Text Preprocessing | Implementasi preprocessing teks Indonesia |
| 25 menit | TF-IDF + Model Training | Vektorisasi, training Naive Bayes & SVM |
| 20 menit | Evaluasi & Analisis | Classification report, confusion matrix, analisis error |
| 15 menit | Eksperimen | Variasi model, parameter, preprocessing |
| 10 menit | Wrap-up & Preview | Rangkuman, info kuis, preview minggu depan |

---

## Hands-on: Sentiment Analysis pada Review Produk Indonesia

### Langkah 1: Install Library dan Import

```python
# Install library NLP untuk bahasa Indonesia
!pip install Sastrawi -q
!pip install nltk -q

# Import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords

# Download NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

# Import Sastrawi untuk stemming bahasa Indonesia
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Import scikit-learn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (classification_report, confusion_matrix,
                              accuracy_score, f1_score)
from sklearn.pipeline import Pipeline

import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8')
print("Library berhasil di-import!")
```

### Langkah 2: Membuat Dataset Review Produk Indonesia

```python
# Dataset review produk e-commerce Indonesia
reviews_data = {
    'review': [
        # Review Positif
        "Produk sangat bagus, kualitas premium, recommended banget!",
        "Pengiriman cepat, packaging rapi, barang sesuai deskripsi",
        "Saya sangat puas dengan pembelian ini, akan beli lagi",
        "Kualitas bahan bagus, jahitan rapi, ukuran pas",
        "Seller ramah dan responsif, barang dikirim cepat",
        "Harga terjangkau dengan kualitas yang sangat baik",
        "Produk original, sudah beli berkali-kali tidak pernah mengecewakan",
        "Mantap! Barang sesuai foto, kualitas oke punya",
        "Terima kasih seller, barang sampai dengan selamat dan cepat",
        "Beli untuk hadiah, penerima sangat senang, kualitas premium",
        "Warnanya sesuai gambar, bahannya tebal dan nyaman",
        "Sudah pakai sebulan masih awet, kualitas terjamin",
        "Respon seller cepat, dikasih bonus juga, senang belanja disini",
        "Produk sangat membantu pekerjaan saya, worth every rupiah",
        "Alhamdulillah barang sampai dengan baik, kualitas bagus",
        "Desainnya keren, banyak yang memuji setelah saya pakai",
        "Harga murah tapi kualitas tidak murahan, puas sekali",
        "Barang oke, sesuai ekspektasi, packing aman",
        "Ini belanja online terbaik saya, produk luar biasa",
        "Sudah langganan disini, selalu memuaskan",
        "Pengiriman aman sampai tujuan, bubble wrap tebal",
        "Bahan adem dipakai seharian, cocok untuk cuaca Indonesia",
        "Pesan sore hari besoknya sudah sampai, super cepat!",
        "Kualitas setara brand terkenal tapi harga jauh lebih murah",
        "Anak saya suka banget, kualitas mainannya bagus dan aman",

        # Review Negatif
        "Barang tidak sesuai deskripsi, kualitas jelek dan murahan",
        "Pengiriman lama sekali, sudah 2 minggu belum sampai",
        "Kecewa berat, produk rusak saat diterima, packaging buruk",
        "Ukuran tidak sesuai, kain tipis dan mudah robek",
        "Seller tidak responsif, komplain diabaikan, kapok belanja disini",
        "Harga mahal tapi kualitas mengecewakan, tidak worth it",
        "Barang palsu, bukan original seperti yang diklaim seller",
        "Warna tidak sesuai foto, bahan kasar dan tidak nyaman",
        "Sudah pakai sekali langsung rusak, kualitas sampah",
        "Menyesal beli produk ini, buang-buang uang saja",
        "Produk cacat, ada goresan dan penyok, QC dimana?",
        "Pengiriman sangat lambat dan barang datang dalam kondisi rusak",
        "Tidak akan beli lagi, pelayanan buruk dan produk mengecewakan",
        "Bahan tipis banget, bisa tembus pandang, malu pakainya",
        "Seller bohong soal stok, sudah bayar tapi dibatalkan sepihak",
        "Kemasan penyok, isi bocor kemana-mana, parah banget",
        "Beli 3 yang datang cuma 2, seller tidak mau tanggung jawab",
        "Foto dan barang beda jauh, ini penipuan namanya",
        "Garansi katanya 1 tahun tapi klaim ditolak terus",
        "Harga sudah dinaikkan sebelum diskon, tipu-tipu promo",
        "Barang bekas dikemas ulang dijual seperti baru, kecewa!",
        "Tidak recommended, banyak review palsu di toko ini",
        "Pesanan salah kirim, minta retur prosesnya ribet banget",
        "Kualitas jauh di bawah ekspektasi, mending beli yang lain",
        "Orderan hilang di ekspedisi, seller lepas tangan"
    ],
    'sentiment': (['positif'] * 25) + (['negatif'] * 25)
}

df = pd.DataFrame(reviews_data)

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

print(f"=== Dataset Review Produk Indonesia ===")
print(f"Total review: {len(df)}")
print(f"Distribusi sentimen:\n{df['sentiment'].value_counts()}")
print(f"\n--- Contoh Review ---")
for _, row in df.head(5).iterrows():
    print(f"[{row['sentiment']:8s}] {row['review'][:80]}...")
```

### Langkah 3: Text Preprocessing untuk Bahasa Indonesia

```python
# Inisialisasi stemmer Sastrawi
factory = StemmerFactory()
stemmer = factory.createStemmer()

# Daftar stopwords Indonesia (gabungan NLTK + custom)
indo_stopwords = set(stopwords.words('indonesian'))
# Tambahkan stopwords custom
custom_stopwords = {
    'yg', 'nya', 'utk', 'dgn', 'krn', 'tp', 'sm', 'dr', 'dlm',
    'sdh', 'udh', 'jg', 'tdk', 'gak', 'ga', 'gk', 'bgt', 'bngt',
    'bisa', 'lagi', 'aja', 'sih', 'dong', 'deh', 'nih', 'tuh',
    'banget', 'sekali', 'sudah', 'belum', 'lah', 'kah'
}
all_stopwords = indo_stopwords.union(custom_stopwords)

def preprocess_text(text):
    """
    Pipeline preprocessing teks Indonesia:
    1. Lowercase
    2. Hapus karakter non-alfabet
    3. Tokenisasi
    4. Hapus stopwords
    5. Stemming (Sastrawi)
    """
    # 1. Lowercase
    text = text.lower()

    # 2. Hapus karakter non-alfabet (kecuali spasi)
    text = re.sub(r'[^a-z\s]', '', text)

    # 3. Hapus spasi berlebih
    text = re.sub(r'\s+', ' ', text).strip()

    # 4. Tokenisasi (pecah menjadi kata)
    tokens = text.split()

    # 5. Hapus stopwords
    tokens = [t for t in tokens if t not in all_stopwords and len(t) > 2]

    # 6. Stemming dengan Sastrawi
    tokens = [stemmer.stem(t) for t in tokens]

    return ' '.join(tokens)

# Terapkan preprocessing
print("Memproses teks (stemming memerlukan waktu)...")
df['review_clean'] = df['review'].apply(preprocess_text)

# Tampilkan contoh sebelum dan sesudah
print("\n=== Contoh Preprocessing ===\n")
for i in range(5):
    print(f"ORIGINAL : {df['review'].iloc[i]}")
    print(f"CLEANED  : {df['review_clean'].iloc[i]}")
    print()
```

### Langkah 4: Eksplorasi Teks — Kata Paling Sering

```python
# Analisis kata paling sering muncul per sentimen
from collections import Counter

def get_top_words(texts, n=15):
    """Hitung kata paling sering muncul"""
    all_words = ' '.join(texts).split()
    return Counter(all_words).most_common(n)

# Top words untuk positif dan negatif
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

for idx, sentiment in enumerate(['positif', 'negatif']):
    subset = df[df['sentiment'] == sentiment]['review_clean']
    top_words = get_top_words(subset, 15)
    words, counts = zip(*top_words)

    axes[idx].barh(range(len(words)), counts,
                    color='green' if sentiment == 'positif' else 'red',
                    alpha=0.7, edgecolor='black')
    axes[idx].set_yticks(range(len(words)))
    axes[idx].set_yticklabels(words, fontsize=11)
    axes[idx].invert_yaxis()
    axes[idx].set_xlabel('Frekuensi', fontsize=12)
    axes[idx].set_title(f'Top 15 Kata — Review {sentiment.capitalize()}', fontsize=13)

plt.suptitle('Kata Paling Sering Muncul per Sentimen', fontsize=15, y=1.02)
plt.tight_layout()
plt.show()
```

### Langkah 5: Vektorisasi Teks — BoW dan TF-IDF

```python
# Perbandingan Bag of Words vs TF-IDF

# Bag of Words
bow_vectorizer = CountVectorizer(max_features=500)
X_bow = bow_vectorizer.fit_transform(df['review_clean'])

# TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=500)
X_tfidf = tfidf_vectorizer.fit_transform(df['review_clean'])

print("=== Perbandingan Vektorisasi ===\n")
print(f"Bag of Words:")
print(f"  Shape: {X_bow.shape}")
print(f"  Vocabulary size: {len(bow_vectorizer.vocabulary_)}")
print(f"  Contoh fitur: {list(bow_vectorizer.vocabulary_.keys())[:10]}")

print(f"\nTF-IDF:")
print(f"  Shape: {X_tfidf.shape}")
print(f"  Vocabulary size: {len(tfidf_vectorizer.vocabulary_)}")

# Bandingkan representasi untuk satu dokumen
print(f"\n=== Representasi Dokumen Pertama ===")
print(f"Review: '{df['review_clean'].iloc[0]}'")
print(f"\nBoW (non-zero values):")
bow_row = X_bow[0].toarray()[0]
non_zero_bow = [(bow_vectorizer.get_feature_names_out()[i], bow_row[i])
                 for i in np.where(bow_row > 0)[0]]
print(f"  {non_zero_bow}")

print(f"\nTF-IDF (non-zero values):")
tfidf_row = X_tfidf[0].toarray()[0]
non_zero_tfidf = [(tfidf_vectorizer.get_feature_names_out()[i], round(tfidf_row[i], 3))
                   for i in np.where(tfidf_row > 0)[0]]
print(f"  {non_zero_tfidf}")
```

### Langkah 6: Training Model — Naive Bayes dan SVM

```python
# Encode label
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(df['sentiment'])  # negatif=0, positif=1

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['review_clean'], y, test_size=0.3, random_state=42, stratify=y
)

print(f"Training set: {len(X_train)} review")
print(f"Test set: {len(X_test)} review")
print(f"Distribusi training: positif={sum(y_train)}, negatif={len(y_train)-sum(y_train)}")

# Pipeline: TF-IDF + Model
pipelines = {
    'Naive Bayes': Pipeline([
        ('tfidf', TfidfVectorizer(max_features=500)),
        ('clf', MultinomialNB())
    ]),
    'SVM (Linear)': Pipeline([
        ('tfidf', TfidfVectorizer(max_features=500)),
        ('clf', LinearSVC(random_state=42, max_iter=5000))
    ]),
    'Logistic Regression': Pipeline([
        ('tfidf', TfidfVectorizer(max_features=500)),
        ('clf', LogisticRegression(random_state=42, max_iter=1000))
    ])
}

# Training dan evaluasi
print("\n=== Hasil Training ===\n")
results = {}
for name, pipe in pipelines.items():
    # Cross-validation pada training set
    cv_scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring='f1')
    # Fit pada full training set
    pipe.fit(X_train, y_train)
    # Evaluasi pada test set
    y_pred = pipe.predict(X_test)
    test_acc = accuracy_score(y_test, y_pred)
    test_f1 = f1_score(y_test, y_pred)

    results[name] = {
        'cv_f1': cv_scores.mean(),
        'test_acc': test_acc,
        'test_f1': test_f1
    }
    print(f"{name:25s}: CV F1={cv_scores.mean():.4f} | "
          f"Test Acc={test_acc:.4f} | Test F1={test_f1:.4f}")
```

### Langkah 7: Evaluasi Detail — Classification Report dan Confusion Matrix

```python
# Gunakan model terbaik untuk evaluasi detail
best_model_name = max(results, key=lambda x: results[x]['test_f1'])
best_pipeline = pipelines[best_model_name]

y_pred_best = best_pipeline.predict(X_test)

print(f"=== Evaluasi Detail: {best_model_name} ===\n")
print(classification_report(y_test, y_pred_best,
                             target_names=['negatif', 'positif']))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred_best)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Negatif', 'Positif'],
            yticklabels=['Negatif', 'Positif'])
plt.xlabel('Prediksi', fontsize=12)
plt.ylabel('Label Sebenarnya', fontsize=12)
plt.title(f'Confusion Matrix — {best_model_name}', fontsize=14)
plt.tight_layout()
plt.show()

# Analisis prediksi salah
print("\n=== Analisis Prediksi Salah ===\n")
wrong_mask = y_pred_best != y_test
X_test_arr = X_test.values
for i in np.where(wrong_mask)[0]:
    true_label = 'positif' if y_test[i] == 1 else 'negatif'
    pred_label = 'positif' if y_pred_best[i] == 1 else 'negatif'
    original = df.loc[df['review_clean'] == X_test_arr[i], 'review'].values
    if len(original) > 0:
        print(f"  Review  : {original[0][:100]}...")
        print(f"  True: {true_label}, Predicted: {pred_label}")
        print()
```

### Langkah 8: Prediksi pada Review Baru

```python
# Prediksi sentimen pada review baru
new_reviews = [
    "Barang bagus, recommended untuk semua orang!",
    "Sampah! Barang rusak dan seller tidak mau bertanggung jawab",
    "Lumayan lah untuk harga segini, sesuai ekspektasi",
    "Pengiriman cepat tapi kualitas produk biasa saja",
    "Kecewa banget, sudah bayar mahal tapi kualitas murahan",
    "Alhamdulillah sesuai harapan, jazakallah seller",
    "Warnanya pudar setelah dicuci pertama kali",
    "Best seller! Sudah beli 3 kali tidak pernah kecewa"
]

# Preprocessing dan prediksi
print("=== Prediksi Sentimen Review Baru ===\n")
for review in new_reviews:
    prediction = best_pipeline.predict([preprocess_text(review)])[0]
    label = 'POSITIF' if prediction == 1 else 'NEGATIF'
    emoji = "(+)" if prediction == 1 else "(-)"
    print(f"  {emoji} [{label:8s}] {review}")
```

### Langkah 9: Perbandingan BoW vs TF-IDF

```python
# Perbandingan BoW vs TF-IDF dengan Naive Bayes
pipe_bow = Pipeline([
    ('vectorizer', CountVectorizer(max_features=500)),
    ('clf', MultinomialNB())
])

pipe_tfidf = Pipeline([
    ('vectorizer', TfidfVectorizer(max_features=500)),
    ('clf', MultinomialNB())
])

# Cross-validation
cv_bow = cross_val_score(pipe_bow, df['review_clean'], y, cv=5, scoring='f1')
cv_tfidf = cross_val_score(pipe_tfidf, df['review_clean'], y, cv=5, scoring='f1')

print("=== BoW vs TF-IDF (Naive Bayes, 5-Fold CV) ===\n")
print(f"Bag of Words: F1 = {cv_bow.mean():.4f} (+/- {cv_bow.std():.4f})")
print(f"TF-IDF:       F1 = {cv_tfidf.mean():.4f} (+/- {cv_tfidf.std():.4f})")

# Visualisasi perbandingan
plt.figure(figsize=(8, 5))
plt.boxplot([cv_bow, cv_tfidf], labels=['Bag of Words', 'TF-IDF'])
plt.ylabel('F1-Score', fontsize=12)
plt.title('Perbandingan BoW vs TF-IDF (Naive Bayes)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## AI Corner: Menggunakan AI untuk Tugas NLP — Kapabilitas dan Limitasi

> **Level: Advanced** — Pada minggu ini, kita memahami bagaimana Large Language Models (LLM) seperti ChatGPT dan Claude sebenarnya melakukan tugas NLP, serta memahami kapabilitas dan limitasinya.

### AI (LLM) untuk NLP: Apa yang Bisa dan Tidak Bisa

| Kapabilitas | Limitasi |
|---|---|
| Sentiment analysis tanpa training (zero-shot) | Tidak selalu konsisten untuk kasus ambigu |
| Summarization berkualitas tinggi | Bisa berhalusinasi atau menambah informasi |
| Translation bahasa Indonesia cukup baik | Slang dan dialek bisa salah diterjemahkan |
| Entity extraction dari teks | Akurasi bervariasi untuk entitas Indonesia |
| Text classification dengan few-shot examples | Biaya API tinggi untuk volume besar |
| Penjelasan hasil analisis NLP | Tidak transparan tentang reasoning internal |

### Skenario Penggunaan AI dalam NLP

| Skenario | Contoh Prompt ke AI |
|---|---|
| Zero-shot sentiment | *"Tentukan sentimen review berikut: 'Barang bagus tapi pengiriman lama'. Jawab: Positif/Negatif/Netral dan jelaskan."* |
| Bantu preprocessing | *"Buatkan fungsi Python untuk preprocessing teks bahasa Indonesia: lowercase, hapus tanda baca, tokenisasi, hapus stopwords, stemming Sastrawi."* |
| Analisis error | *"Model sentiment analysis saya salah mengklasifikasikan 'Tidak jelek sih' sebagai negatif. Bagaimana cara menangani negasi dalam NLP bahasa Indonesia?"* |
| Feature engineering | *"Selain TF-IDF, fitur apa saja yang bisa saya ekstrak dari teks review untuk meningkatkan akurasi sentiment analysis?"* |
| Evaluasi | *"Berikut classification report model saya [paste]. Interpretasikan hasilnya dan sarankan perbaikan."* |

### Contoh Prompt Minggu Ini

```
Saya membangun sentiment analysis untuk review produk e-commerce Indonesia.
Pipeline saya: preprocessing (Sastrawi) → TF-IDF → Naive Bayes.

Akurasi: 85%, F1: 0.84

Masalah yang saya temui:
1. Review sarkastik "Bagus ya, 3 minggu baru sampai" diprediksi positif
2. Review campuran "Barang oke tapi pengiriman lama" sulit diklasifikasikan
3. Slang seperti "bgt", "ga", "worth it" tidak tertangani dengan baik

Pertanyaan:
1. Bagaimana cara menangani sarkasme dalam NLP?
2. Bagaimana menangani review campuran (mixed sentiment)?
3. Apakah Anda bisa membantu membuat kamus normalisasi slang Indonesia?
4. Teknik apa yang bisa meningkatkan akurasi dari 85%?
```

### Tips Penting

1. **LLM bisa melakukan sentiment analysis langsung** (zero-shot), tapi tidak scalable untuk jutaan review.
2. **Untuk volume besar**, tetap butuh model ML tradisional (Naive Bayes, SVM) atau fine-tuned transformer.
3. **Gunakan AI untuk memahami konsep NLP**, bukan menggantikan proses belajar.
4. **Bahasa Indonesia masih underrepresented** di kebanyakan model NLP — ini peluang riset!

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **NLP dan Bahasa Indonesia:** Menurut Anda, mengapa NLP untuk bahasa Indonesia lebih menantang dibandingkan bahasa Inggris? Apa implikasinya bagi pengembangan teknologi AI di Indonesia?

2. **Sentiment Analysis dan Bisnis:** Bagaimana sebuah platform e-commerce Indonesia (Tokopedia, Shopee) bisa memanfaatkan sentiment analysis untuk meningkatkan layanan? Berikan contoh konkret.

3. **Etika NLP:** Sentiment analysis bisa digunakan untuk memantau opini publik. Dari perspektif amanah dan privasi, di mana batas etis penggunaan teknologi ini? Misalnya, apakah etis bagi pemerintah memantau sentimen di media sosial?

4. **Bias dalam NLP:** Model NLP bisa mengandung bias (gender, ras, agama) dari data pelatihannya. Bagaimana kita bisa mendeteksi dan mengurangi bias ini, terutama dalam konteks Indonesia yang majemuk?

5. **AI vs Traditional NLP:** Dengan adanya ChatGPT dan Claude yang bisa melakukan sentiment analysis secara langsung, apakah masih perlu belajar teknik NLP tradisional (BoW, TF-IDF, Naive Bayes)? Berikan argumentasi.

---

## Pengumuman

### K3 Kuis: Advanced ML (Minggu 9-12)

| Komponen | Keterangan |
|---|---|
| **Topik** | Materi Minggu 9-12 (Clustering, Dimensionality Reduction, Neural Networks, NLP) |
| **Jadwal** | Akan diumumkan pada Minggu 13 |
| **Format** | Pilihan ganda + isian singkat + kode pendek |
| **Durasi** | 60 menit |
| **Sifat** | Closed-book, tanpa AI |

**Materi yang perlu dikuasai:**
- Algoritma clustering (K-Means, Hierarchical, DBSCAN)
- PCA dan feature selection
- Arsitektur neural network, activation functions, backpropagation
- Preprocessing teks, TF-IDF, sentiment analysis

---

## Referensi

### Buku Teks

1. Jurafsky, D., & Martin, J. H. (2023). *Speech and Language Processing* (3rd ed. draft). — Chapter 2, 4, 6. Tersedia gratis di [web.stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/).
2. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media. — Chapter 16: Natural Language Processing.
3. Bird, S., Klein, E., & Loper, E. (2009). *Natural Language Processing with Python*. O'Reilly Media. Tersedia gratis di [nltk.org/book/](https://www.nltk.org/book/).

### Sumber Online

4. [scikit-learn: Text Feature Extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) — Dokumentasi TF-IDF dan CountVectorizer.
5. [Sastrawi GitHub](https://github.com/sastrawi/sastrawi) — Library stemming bahasa Indonesia.
6. [NLTK Indonesian Stopwords](https://www.nltk.org/) — Stopwords bahasa Indonesia di NLTK.

### Referensi NLP Indonesia

7. Wilie, B., et al. (2020). "IndoNLU: Benchmark and Resources for Evaluating Indonesian Natural Language Understanding." *Proceedings of AACL-IJCNLP 2020*. — Benchmark NLP bahasa Indonesia.
8. Koto, F., Rahimi, A., Lau, J. H., & Baldwin, T. (2020). "IndoLEM and IndoBERT: A Benchmark Dataset and Pre-trained Language Model for Indonesian NLP." *Proceedings of COLING 2020*.

---

> **Preview Minggu Depan:** Kita akan membahas topik lanjutan sesuai dengan rencana perkuliahan. Persiapkan diri untuk **K3 Kuis** yang akan mencakup materi Minggu 9-12.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
