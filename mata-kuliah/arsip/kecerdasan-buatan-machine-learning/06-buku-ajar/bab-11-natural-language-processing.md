# BAB 11: NATURAL LANGUAGE PROCESSING DASAR

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| Sub-CPMK 12.1 | Menerapkan teknik preprocessing teks dan representasi teks (BoW, TF-IDF) untuk membangun pipeline NLP | C3 |
| Sub-CPMK 12.2 | Menganalisis dan mengevaluasi model klasifikasi teks serta sentiment analysis pada data teks Indonesia | C4 |

**CPMK-6:** Menerapkan teknik NLP dan Computer Vision dasar untuk data teks dan gambar.

---

## Estimasi Waktu

| Komponen | Durasi |
|----------|--------|
| Membaca materi | 90 menit |
| Praktik kode Python | 75 menit |
| Latihan soal | 45 menit |
| **Total** | **210 menit** |

---

## Prasyarat

- Pemahaman dasar Python: string, list, dictionary (Bab 2)
- Konsep supervised learning: klasifikasi, evaluasi (Bab 5-7)
- Dasar-dasar preprocessing data (Bab 4)
- Pengenalan scikit-learn pipeline (Bab 5)

---

## 11.1 NLP Overview

### 11.1.1 Apa itu Natural Language Processing?

**Natural Language Processing (NLP)** adalah cabang AI yang memungkinkan komputer **memahami**, **menginterpretasi**, dan **menghasilkan** bahasa manusia (bahasa alami).

> "NLP is the bridge between human communication and computer understanding."

### 11.1.2 Mengapa NLP Penting?

Data teks ada di mana-mana:
- **80%** data dunia adalah data tidak terstruktur, sebagian besar berupa teks
- Ulasan produk, media sosial, dokumen hukum, jurnal medis, email — semua adalah teks

### 11.1.3 Aplikasi NLP

| Aplikasi | Contoh di Indonesia | Teknik |
|----------|---------------------|--------|
| **Sentiment analysis** | Analisis sentimen ulasan Tokopedia/Shopee | Klasifikasi teks |
| **Chatbot** | CS otomatis bank BCA, Telkomsel | NLU + response generation |
| **Machine translation** | Google Translate Indonesia-Inggris | Seq2Seq, Transformer |
| **Spam detection** | Filter spam Gmail/WhatsApp | Klasifikasi teks |
| **Text summarization** | Ringkasan berita Kompas | Extractive/Abstractive |
| **Named Entity Recognition** | Ekstraksi nama orang, tempat, organisasi dari berita | Sequence labeling |
| **Voice assistant** | Google Assistant dalam Bahasa Indonesia | ASR + NLU + TTS |

### 11.1.4 Pipeline NLP Umum

```
Teks Mentah → Preprocessing → Representasi Numerik → Model ML → Prediksi/Output
  "Produk     Tokenize,       BoW, TF-IDF,           Naive Bayes,  "Positif"
   bagus!"    Stopword,       Word2Vec               SVM, NN
              Stemming
```

---

## 11.2 Text Preprocessing

Teks mentah tidak bisa langsung diproses oleh model ML. Kita perlu **membersihkan** dan **menormalisasi** teks terlebih dahulu.

### 11.2.1 Tokenization

**Tokenization** adalah proses memecah teks menjadi unit-unit kecil (*tokens*): kata, kalimat, atau subword.

```python
# Tokenization dasar
teks = "Saya membeli laptop di Tokopedia dengan harga Rp 8.500.000"

# Tokenization sederhana (split by space)
tokens_sederhana = teks.split()
print(f"Split sederhana: {tokens_sederhana}")

# Tokenization dengan NLTK
import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
from nltk.tokenize import word_tokenize, sent_tokenize

# Word tokenization
tokens_nltk = word_tokenize(teks)
print(f"NLTK word tokenize: {tokens_nltk}")

# Sentence tokenization
teks_panjang = "Produk ini sangat bagus. Pengiriman cepat. Akan beli lagi."
kalimat = sent_tokenize(teks_panjang)
print(f"Sentence tokenize: {kalimat}")
```

### 11.2.2 Lowercasing dan Punctuation Removal

```python
import re

teks = "Produk BAGUS!!! Pengiriman cepat... Terima kasih Tokopedia :)"

# Lowercasing
teks_lower = teks.lower()
print(f"Lowercase: {teks_lower}")

# Hapus tanda baca dan karakter khusus
teks_clean = re.sub(r'[^\w\s]', '', teks_lower)
print(f"Clean: {teks_clean}")

# Hapus angka (opsional)
teks_no_num = re.sub(r'\d+', '', teks_clean)
print(f"No numbers: {teks_no_num}")

# Hapus whitespace berlebih
teks_final = ' '.join(teks_no_num.split())
print(f"Final: {teks_final}")
```

### 11.2.3 Stopword Removal

**Stopwords** adalah kata-kata umum yang tidak membawa banyak makna (contoh: "yang", "dan", "di", "ke", "dari").

```python
import nltk
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

# Stopwords Bahasa Indonesia
stopwords_id = set(stopwords.words('indonesian'))
print(f"Jumlah stopwords Indonesia: {len(stopwords_id)}")
print(f"Contoh: {list(stopwords_id)[:15]}")

# Hapus stopwords
teks = "saya sangat suka dengan produk ini karena kualitasnya bagus"
tokens = teks.split()
tokens_filtered = [t for t in tokens if t not in stopwords_id]

print(f"\nSebelum: {tokens}")
print(f"Sesudah: {tokens_filtered}")

# Tambahkan stopwords kustom (kata-kata informal Indonesia)
stopwords_kustom = stopwords_id.union({
    'nya', 'yg', 'nih', 'sih', 'dong', 'deh', 'lho', 'kok',
    'banget', 'bgt', 'gak', 'ga', 'udah', 'udh', 'aja',
    'emang', 'gw', 'gue', 'lo', 'lu'
})
print(f"\nJumlah stopwords + kustom: {len(stopwords_kustom)}")
```

### 11.2.4 Stemming vs Lemmatization

**Stemming** menghilangkan imbuhan untuk mendapatkan kata dasar. **Lemmatization** mengubah kata ke bentuk dasarnya (*lemma*) menggunakan kamus.

| Aspek | Stemming | Lemmatization |
|-------|----------|---------------|
| **Pendekatan** | Rule-based (potong imbuhan) | Dictionary-based |
| **Kecepatan** | Cepat | Lebih lambat |
| **Akurasi** | Kadang menghasilkan non-word | Selalu menghasilkan kata valid |
| **Contoh (EN)** | "running" → "run", "better" → "bet" | "running" → "run", "better" → "good" |
| **Contoh (ID)** | "membelikan" → "beli" | "membelikan" → "beli" |

```python
# Stemming untuk Bahasa Indonesia menggunakan Sastrawi
# !pip install Sastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.createStemmer()

# Contoh stemming kata-kata Indonesia
kata_kata = [
    'membelikan', 'pembelajaran', 'berlari', 'penjualan',
    'memperbaiki', 'permasalahan', 'ketidakadilan', 'mengerjakan'
]

print("=== STEMMING BAHASA INDONESIA (Sastrawi) ===")
for kata in kata_kata:
    stem = stemmer.stem(kata)
    print(f"  {kata:20s} → {stem}")

# Stemming kalimat lengkap
kalimat = "Mahasiswa sedang mempelajari pemrograman untuk mengembangkan aplikasi"
kalimat_stem = stemmer.stem(kalimat)
print(f"\nKalimat asli:  {kalimat}")
print(f"Setelah stem:  {kalimat_stem}")
```

---

## 11.3 Indonesian NLP

### 11.3.1 Sastrawi Stemmer untuk Bahasa Indonesia

**Sastrawi** adalah library stemming Bahasa Indonesia yang paling populer. Algoritma-nya berdasarkan aturan morfologi Bahasa Indonesia (awalan, sisipan, akhiran, konfiks).

```python
# Preprocessing lengkap untuk teks Indonesia
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords

def preprocess_indonesia(teks, stem=True):
    """
    Pipeline preprocessing teks Bahasa Indonesia.

    Parameter:
    - teks: string input
    - stem: boolean, apakah melakukan stemming

    Return:
    - string teks yang sudah dipreprocess
    """
    # 1. Lowercase
    teks = teks.lower()

    # 2. Hapus URL
    teks = re.sub(r'http\S+|www\S+', '', teks)

    # 3. Hapus mention dan hashtag
    teks = re.sub(r'@\w+|#\w+', '', teks)

    # 4. Hapus angka
    teks = re.sub(r'\d+', '', teks)

    # 5. Hapus tanda baca dan karakter khusus
    teks = re.sub(r'[^\w\s]', '', teks)

    # 6. Tokenisasi
    tokens = teks.split()

    # 7. Hapus stopwords
    stop_words = set(stopwords.words('indonesian'))
    stop_words.update(['nya', 'yg', 'nih', 'sih', 'dong', 'deh',
                       'banget', 'bgt', 'gak', 'ga', 'gue', 'gw'])
    tokens = [t for t in tokens if t not in stop_words and len(t) > 1]

    # 8. Stemming (opsional, bisa lambat untuk teks panjang)
    if stem:
        factory = StemmerFactory()
        stemmer = factory.createStemmer()
        tokens = [stemmer.stem(t) for t in tokens]

    # 9. Gabungkan kembali
    return ' '.join(tokens)

# Contoh penggunaan
contoh_teks = [
    "Produk ini sangat bagus!!! Pengiriman cepat banget dari Jakarta ke Surabaya",
    "Kecewa bgt, barangnya gak sesuai deskripsi. Sudah komplain tapi belum direspon",
    "Laptop ini cocok untuk mahasiswa, harganya terjangkau @tokopedia #BeliBijak"
]

print("=== HASIL PREPROCESSING ===")
for teks in contoh_teks:
    hasil = preprocess_indonesia(teks, stem=True)
    print(f"Asli:   {teks}")
    print(f"Proses: {hasil}\n")
```

### 11.3.2 Indonesian Stopwords List

```python
# Daftar stopwords Indonesia yang diperluas
# Sumber: NLTK + custom untuk bahasa informal

stopwords_id_extended = {
    # Kata ganti
    'saya', 'aku', 'kamu', 'dia', 'kami', 'kita', 'mereka',
    'gue', 'gw', 'lo', 'lu', 'elo',

    # Kata hubung
    'dan', 'atau', 'tetapi', 'namun', 'serta', 'maupun',

    # Kata depan
    'di', 'ke', 'dari', 'pada', 'untuk', 'dengan', 'oleh',

    # Kata keterangan
    'sudah', 'belum', 'akan', 'sedang', 'telah', 'masih',
    'udah', 'udh', 'blm', 'mau', 'lagi',

    # Partikel informal
    'nih', 'sih', 'dong', 'deh', 'lho', 'kok', 'kan',
    'banget', 'bgt', 'aja', 'doang',

    # Kata negasi
    'tidak', 'bukan', 'jangan', 'gak', 'ga', 'nggak', 'ngga',

    # Lainnya
    'yang', 'ini', 'itu', 'ada', 'juga', 'hanya', 'nya',
    'bila', 'jika', 'kalau', 'karena', 'agar', 'supaya'
}

print(f"Total stopwords: {len(stopwords_id_extended)}")
```

### 11.3.3 Tantangan NLP Bahasa Indonesia

| Tantangan | Deskripsi | Contoh |
|-----------|-----------|--------|
| **Bahasa informal** | Banyak singkatan dan slang | "gw lg mkn" = "saya sedang makan" |
| **Alay/Lebay** | Ejaan kreatif | "4L4y" = "alay" |
| **Campuran bahasa** | Code-switching Indonesia-Inggris | "meeting-nya di-cancel ya" |
| **Negasi** | "tidak" bisa membalik makna | "tidak bagus" vs "bagus" |
| **Sarkasme** | Makna berlawanan | "Wah, bagus banget ya pelayanannya" (sarkas) |
| **Resource terbatas** | Lebih sedikit dataset & model dibanding Inggris | Pre-trained model terbatas |

```python
# Contoh normalisasi bahasa informal Indonesia
kamus_normalisasi = {
    'gak': 'tidak', 'ga': 'tidak', 'nggak': 'tidak', 'ngga': 'tidak',
    'gue': 'saya', 'gw': 'saya', 'lo': 'kamu', 'lu': 'kamu',
    'bgt': 'banget', 'bgtt': 'banget', 'bngtt': 'banget',
    'emg': 'memang', 'emang': 'memang',
    'blm': 'belum', 'udh': 'sudah', 'udah': 'sudah',
    'org': 'orang', 'trs': 'terus', 'krn': 'karena',
    'sm': 'sama', 'utk': 'untuk', 'dgn': 'dengan',
    'yg': 'yang', 'tp': 'tetapi', 'aja': 'saja',
    'bsk': 'besok', 'kmrn': 'kemarin', 'skrg': 'sekarang',
    'mkn': 'makan', 'mnt': 'minta', 'lg': 'lagi'
}

def normalisasi_informal(teks):
    """Normalisasi kata-kata informal Indonesia ke bentuk baku."""
    tokens = teks.lower().split()
    tokens_norm = [kamus_normalisasi.get(t, t) for t in tokens]
    return ' '.join(tokens_norm)

# Contoh
teks_informal = "gw lg mkn di warung tp makanannya gak enak bgt"
teks_normal = normalisasi_informal(teks_informal)
print(f"Informal: {teks_informal}")
print(f"Normal:   {teks_normal}")
```

---

## 11.4 Text Representation

Komputer tidak memahami teks — kita perlu mengubah teks menjadi **vektor numerik**.

### 11.4.1 Bag of Words (CountVectorizer)

**Bag of Words (BoW)** merepresentasikan teks sebagai vektor frekuensi kata, mengabaikan urutan.

```python
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Corpus contoh
corpus = [
    "saya suka makan nasi goreng",
    "dia suka makan mie goreng",
    "saya tidak suka mie goreng",
    "nasi goreng sangat enak"
]

# CountVectorizer
cv = CountVectorizer()
X_bow = cv.fit_transform(corpus)

# Tampilkan sebagai DataFrame
df_bow = pd.DataFrame(
    X_bow.toarray(),
    columns=cv.get_feature_names_out(),
    index=[f'Dok {i+1}' for i in range(len(corpus))]
)

print("=== BAG OF WORDS ===")
print(df_bow)
print(f"\nVocabulary size: {len(cv.get_feature_names_out())}")
print(f"Sparse matrix shape: {X_bow.shape}")
```

**Output:**

```
         dia  enak  goreng  makan  mie  nasi  sangat  saya  suka  tidak
Dok 1     0     0       1      1    0     1       0     1     1      0
Dok 2     1     0       1      1    1     0       0     0     1      0
Dok 3     0     0       1      0    1     0       0     1     1      1
Dok 4     0     1       1      0    0     1       1     0     0      0
```

### 11.4.2 TF-IDF (TfidfVectorizer)

**TF-IDF** (Term Frequency-Inverse Document Frequency) memberikan **bobot lebih tinggi** pada kata yang sering muncul di satu dokumen tetapi jarang di dokumen lain.

$$\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t)$$

- **TF** (Term Frequency): frekuensi kata t di dokumen d
- **IDF** (Inverse Document Frequency): $\log\frac{N}{df(t)}$ — semakin jarang kata, semakin tinggi IDF

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# TF-IDF
tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(corpus)

df_tfidf = pd.DataFrame(
    X_tfidf.toarray().round(3),
    columns=tfidf.get_feature_names_out(),
    index=[f'Dok {i+1}' for i in range(len(corpus))]
)

print("=== TF-IDF ===")
print(df_tfidf)

# Perhatikan: kata "goreng" (muncul di semua dokumen) memiliki bobot rendah
# Kata "enak", "sangat" (unik) memiliki bobot tinggi
```

**Perbandingan BoW vs TF-IDF:**

| Aspek | Bag of Words | TF-IDF |
|-------|-------------|--------|
| **Nilai** | Frekuensi integer | Float terbobot |
| **Kata umum** | Bobot sama | Bobot rendah |
| **Kata unik** | Bobot sama | Bobot tinggi |
| **Kapan digunakan** | Baseline sederhana | Umumnya lebih baik |

### 11.4.3 Word Embeddings (Pengantar)

**Word embeddings** merepresentasikan kata sebagai vektor berdimensi rendah yang menangkap **makna semantik**.

```
Bag of Words:      "raja" = [0, 0, 0, 1, 0, 0, 0, ...]  (sparse, tinggi dimensi)
Word Embedding:    "raja" = [0.23, -0.41, 0.85, 0.12]    (dense, dimensi rendah)

Properti ajaib:
  vektor("raja") - vektor("pria") + vektor("wanita") ≈ vektor("ratu")
```

| Model | Pendekatan | Catatan |
|-------|-----------|---------|
| **Word2Vec** | Skip-gram / CBOW | Google, 2013. Efisien untuk vocab besar |
| **GloVe** | Global matrix factorization | Stanford. Menangkap statistik global |
| **FastText** | Subword (karakter n-gram) | Facebook. Baik untuk bahasa Indonesia (morfologi kaya) |

> **Catatan:** Untuk bab ini kita fokus pada BoW dan TF-IDF. Word embeddings dan model modern (BERT, GPT) dibahas secara konseptual di Bagian 11.7.

---

## 11.5 Text Classification Pipeline

### 11.5.1 Pipeline Lengkap

```
[Teks Mentah] → [Preprocessing] → [Vektorisasi] → [Model] → [Evaluasi]
  "Bagus!"       lowercase,         TF-IDF          NB/SVM     Accuracy,
                  hapus tanda baca,                              F1-score,
                  stopwords,                                     Confusion
                  stemming                                       Matrix
```

### 11.5.2 Naive Bayes untuk Teks

**Naive Bayes** adalah algoritma klasik untuk klasifikasi teks yang bekerja sangat baik meskipun sederhana.

```python
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset ulasan produk Indonesia (simulasi)
np.random.seed(42)

ulasan_positif = [
    "produk bagus kualitas mantap",
    "pengiriman cepat barang sesuai deskripsi",
    "sangat puas dengan pembelian ini",
    "recommended seller pelayanan ramah",
    "barang original harga terjangkau",
    "kualitas premium pengiriman aman",
    "produk sesuai foto penjual responsif",
    "barang sampai cepat packaging rapi",
    "sangat memuaskan akan beli lagi",
    "harga murah kualitas bagus banget",
    "toko terpercaya barang asli",
    "pengiriman kilat barang utuh",
    "puas banget produk melebihi ekspektasi",
    "seller ramah fast response",
    "barang bagus sesuai pesanan",
    "kualitas oke punya harga bersahabat",
    "produk mantap jiwa recommended",
    "cepat sampai packing aman rapi",
    "terima kasih seller barang sesuai",
    "produk keren kualitas terjamin"
]

ulasan_negatif = [
    "produk jelek kualitas buruk",
    "pengiriman lama barang rusak",
    "sangat kecewa tidak sesuai deskripsi",
    "seller tidak responsif pelayanan buruk",
    "barang palsu harga kemahalan",
    "kualitas murahan produk cacat",
    "barang tidak sesuai foto penjual bohong",
    "packaging asal asalan barang penyok",
    "sangat mengecewakan tidak akan beli lagi",
    "harga mahal kualitas jelek",
    "toko penipu barang palsu",
    "pengiriman lambat barang hilang",
    "kecewa berat produk jauh dari ekspektasi",
    "seller cuek slow response",
    "barang rusak tidak sesuai pesanan",
    "kualitas payah harga tidak sebanding",
    "produk abal abal tidak recommended",
    "lama sampai packing berantakan",
    "komplain tidak ditanggapi seller",
    "produk cacat minta tukar susah"
]

# Gabungkan data
teks = ulasan_positif + ulasan_negatif
label = [1] * len(ulasan_positif) + [0] * len(ulasan_negatif)  # 1=positif, 0=negatif

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    teks, label, test_size=0.25, random_state=42, stratify=label
)

print(f"Training: {len(X_train)} data")
print(f"Testing: {len(X_test)} data")

# Vektorisasi dengan TF-IDF
tfidf = TfidfVectorizer(max_features=1000)
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Latih Naive Bayes
nb = MultinomialNB()
nb.fit(X_train_tfidf, y_train)

# Evaluasi
y_pred = nb.predict(X_test_tfidf)
print(f"\n=== NAIVE BAYES — KLASIFIKASI ULASAN ===")
print(classification_report(y_test, y_pred, target_names=['Negatif', 'Positif']))
```

### 11.5.3 SVM untuk Klasifikasi Teks

```python
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

# Pipeline SVM (preprocessing + model dalam satu objek)
pipeline_svm = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=1000, ngram_range=(1, 2))),
    ('svm', LinearSVC(random_state=42))
])

# Training dan evaluasi
pipeline_svm.fit(X_train, y_train)
y_pred_svm = pipeline_svm.predict(X_test)

print("=== SVM — KLASIFIKASI ULASAN ===")
print(classification_report(y_test, y_pred_svm, target_names=['Negatif', 'Positif']))

# Prediksi ulasan baru
ulasan_baru = [
    "produk bagus sekali sangat puas",
    "barang jelek rusak kecewa",
    "lumayan lah untuk harga segini",
    "mantap jiwa recommended banget"
]

prediksi = pipeline_svm.predict(ulasan_baru)
label_map = {0: 'Negatif', 1: 'Positif'}

print("\n=== PREDIKSI ULASAN BARU ===")
for teks, pred in zip(ulasan_baru, prediksi):
    print(f"  '{teks}' → {label_map[pred]}")
```

---

## 11.6 Sentiment Analysis

### 11.6.1 Indonesian Sentiment Analysis pada Ulasan Produk

**Sentiment analysis** adalah tugas NLP untuk menentukan **opini** atau **sentimen** (positif, negatif, netral) dari sebuah teks.

```python
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline

# Dataset lebih besar (simulasi ulasan e-commerce Indonesia)
np.random.seed(42)

# Template ulasan
template_positif = [
    "produk {} {} sangat {}",
    "{} banget {} ini {}",
    "recommended {} {} {}",
    "puas {} {} seller {}",
    "{} cepat {} {} mantap"
]

kata_positif_1 = ['bagus', 'keren', 'mantap', 'oke', 'top']
kata_positif_2 = ['kualitas', 'pengiriman', 'packaging', 'pelayanan', 'harga']
kata_positif_3 = ['memuaskan', 'terjangkau', 'aman', 'rapi', 'responsif']

template_negatif = [
    "produk {} {} sangat {}",
    "{} banget {} ini {}",
    "tidak {} {} {} kecewa",
    "{} {} seller {} mengecewakan",
    "{} lama {} {} buruk"
]

kata_negatif_1 = ['jelek', 'buruk', 'payah', 'abal', 'rusak']
kata_negatif_2 = ['kualitas', 'pengiriman', 'packaging', 'pelayanan', 'harga']
kata_negatif_3 = ['mengecewakan', 'kemahalan', 'berantakan', 'kasar', 'lambat']

# Generate data
data_ulasan = []
for _ in range(200):
    tmpl = np.random.choice(template_positif)
    k1 = np.random.choice(kata_positif_1)
    k2 = np.random.choice(kata_positif_2)
    k3 = np.random.choice(kata_positif_3)
    data_ulasan.append({'teks': tmpl.format(k1, k2, k3), 'sentimen': 'positif'})

for _ in range(200):
    tmpl = np.random.choice(template_negatif)
    k1 = np.random.choice(kata_negatif_1)
    k2 = np.random.choice(kata_negatif_2)
    k3 = np.random.choice(kata_negatif_3)
    data_ulasan.append({'teks': tmpl.format(k1, k2, k3), 'sentimen': 'negatif'})

df_ulasan = pd.DataFrame(data_ulasan)
df_ulasan = df_ulasan.sample(frac=1, random_state=42).reset_index(drop=True)

print(f"=== DATASET SENTIMENT ===")
print(f"Total data: {len(df_ulasan)}")
print(f"Distribusi:\n{df_ulasan['sentimen'].value_counts()}")
print(f"\nContoh data:")
print(df_ulasan.head(5).to_string(index=False))
```

### 11.6.2 Pipeline Lengkap Sentiment Analysis

```python
from sklearn.model_selection import train_test_split

# Encode label
df_ulasan['label'] = (df_ulasan['sentimen'] == 'positif').astype(int)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    df_ulasan['teks'], df_ulasan['label'],
    test_size=0.2, random_state=42, stratify=df_ulasan['label']
)

# Bandingkan 3 model
models = {
    'Naive Bayes': Pipeline([
        ('tfidf', TfidfVectorizer(max_features=2000, ngram_range=(1, 2))),
        ('clf', MultinomialNB())
    ]),
    'SVM': Pipeline([
        ('tfidf', TfidfVectorizer(max_features=2000, ngram_range=(1, 2))),
        ('clf', LinearSVC(random_state=42))
    ]),
    'Random Forest': Pipeline([
        ('tfidf', TfidfVectorizer(max_features=2000, ngram_range=(1, 2))),
        ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
}

# Evaluasi dengan cross-validation
print("=== PERBANDINGAN MODEL SENTIMENT ANALYSIS ===")
hasil = []
for nama, model in models.items():
    skor = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    hasil.append({
        'Model': nama,
        'Accuracy (CV)': f"{skor.mean():.4f} ± {skor.std():.4f}"
    })
    print(f"{nama:15s}: {skor.mean():.4f} ± {skor.std():.4f}")

# Latih model terbaik pada semua training data
best_model = models['SVM']
best_model.fit(X_train, y_train)

# Evaluasi pada test set
from sklearn.metrics import classification_report, confusion_matrix

y_pred_final = best_model.predict(X_test)
print(f"\n=== EVALUASI PADA TEST SET (SVM) ===")
print(classification_report(y_test, y_pred_final, target_names=['Negatif', 'Positif']))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred_final)
fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Negatif', 'Positif'],
            yticklabels=['Negatif', 'Positif'], ax=ax)
ax.set_xlabel('Prediksi')
ax.set_ylabel('Aktual')
ax.set_title('Confusion Matrix — Sentiment Analysis Ulasan')
plt.tight_layout()
plt.savefig('sentiment_confusion_matrix.png', dpi=150, bbox_inches='tight')
plt.show()

# Demo prediksi real-time
ulasan_test = [
    "bagus banget produknya, pengiriman cepat aman",
    "jelek banget, barang tidak sesuai foto",
    "biasa aja sih, standar lah",
    "seller responsif, barang original mantap",
    "kecewa berat, mau refund tapi susah"
]

print("\n=== DEMO PREDIKSI SENTIMEN ===")
prediksi_demo = best_model.predict(ulasan_test)
for teks, pred in zip(ulasan_test, prediksi_demo):
    sentimen = "POSITIF" if pred == 1 else "NEGATIF"
    print(f"  [{sentimen:8s}] {teks}")
```

---

## 11.7 Pengantar NLP Modern: Transformers, BERT, GPT

### 11.7.1 Mekanisme Attention (Intuisi)

Sebelum Transformers, model NLP (RNN/LSTM) memproses teks **secara sekuensial** — kata per kata. Ini lambat dan sulit menangkap hubungan jarak jauh.

**Attention mechanism** memungkinkan model "memperhatikan" semua kata sekaligus dan memberikan **bobot berbeda** untuk setiap kata berdasarkan relevansi.

```
Kalimat: "Kucing itu duduk di atas tikar karena dia lelah"

Tanpa attention (RNN):
  Kucing → itu → duduk → di → atas → tikar → karena → dia → lelah
  (informasi "kucing" menghilang saat memproses "dia")

Dengan attention:
  "dia" → melihat ke semua kata →
    Kucing (0.6)  itu (0.05)  duduk (0.1)  tikar (0.05)  karena (0.1)  lelah (0.1)
    → "dia" merujuk ke "Kucing" (bobot tertinggi)
```

### 11.7.2 Bagaimana LLM Bekerja (Tingkat Tinggi)

**Large Language Models** (LLM) seperti GPT dan BERT dibangun di atas arsitektur **Transformer**:

```
Arsitektur Transformer (2017):
┌──────────────┐
│   Self-      │ ← Setiap kata memperhatikan semua kata lain
│   Attention  │
├──────────────┤
│   Feed-      │ ← Transformasi non-linear
│   Forward    │
├──────────────┤
│   Layer      │ ← Normalisasi dan residual connection
│   Norm       │
└──────────────┘
    × N layers (GPT-3: 96 layers, BERT: 12-24 layers)
```

| Model | Pendekatan | Kegunaan |
|-------|-----------|----------|
| **BERT** | Bidirectional (melihat kiri dan kanan) | Klasifikasi, NER, QA |
| **GPT** | Autoregressive (melihat kiri saja) | Generasi teks, chatbot |
| **T5** | Encoder-decoder | Terjemahan, summarization |

**Ukuran model:**

| Model | Parameter | Tahun |
|-------|-----------|-------|
| BERT-base | 110 juta | 2018 |
| GPT-2 | 1.5 miliar | 2019 |
| GPT-3 | 175 miliar | 2020 |
| GPT-4 | ~1.8 triliun (estimasi) | 2023 |
| Claude 3 Opus | — (tidak dipublikasi) | 2024 |

> **Untuk mahasiswa:** Anda tidak perlu membangun LLM dari awal — fokus pada **menggunakan** model pre-trained melalui API dan **memahami** konsep dasarnya. Kemampuan prompting yang baik (Bab 1) lebih praktis daripada melatih model sendiri.

---

## 11.8 Studi Kasus: NLP untuk Analisis Ulasan E-Commerce Indonesia

### 11.8.1 Konteks

Platform e-commerce seperti Tokopedia dan Shopee memiliki jutaan ulasan produk. Analisis otomatis ulasan ini membantu:
- **Penjual:** Memahami keluhan pelanggan, meningkatkan produk
- **Pembeli:** Mendapat ringkasan sentimen tanpa membaca semua ulasan
- **Platform:** Mendeteksi ulasan palsu, meningkatkan kualitas marketplace

### 11.8.2 End-to-End Pipeline

```python
import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Simulasi dataset yang lebih realistis
np.random.seed(42)

ulasan_data = {
    'teks': [
        # Positif - elektronik
        "laptop bagus performa kencang layar jernih",
        "headset suara jernih bass mantap harga murah",
        "charger fast charging beneran cepat original",
        "mouse wireless nyaman dipakai baterai awet",
        "speaker bluetooth suara bening desain keren",
        "powerbank kapasitas besar awet tahan lama",
        "kabel data original pengisian cepat tahan lama",
        "keyboard mechanical enak diketik responsif",
        "webcam jernih resolusi tinggi bagus untuk meeting",
        "earbuds nyaman dipakai suara oke bass nendang",
        # Positif - fashion
        "baju kualitas bagus jahitan rapi nyaman dipakai",
        "sepatu nyaman dipakai bahan berkualitas",
        "tas bagus desain elegan bahan tebal kuat",
        "jaket bagus hangat nyaman modelnya keren",
        "celana jeans bahan tebal nyaman jahitan rapi",
        # Negatif - elektronik
        "laptop lemot cepat panas baterai boros",
        "headset suara pecah kualitas murahan cepat rusak",
        "charger palsu lambat pengisian panas berbahaya",
        "mouse cepat rusak klik tidak responsif murahan",
        "speaker suara jelek bass bocor desain murahan",
        "powerbank palsu kapasitas tidak sesuai cepat habis",
        "kabel data cepat putus kualitas abal tidak original",
        "keyboard berisik tombol macet tidak nyaman",
        "webcam blur gelap resolusi rendah mengecewakan",
        "earbuds suara jelek cepat rusak tidak nyaman",
        # Negatif - fashion
        "baju tipis jahitan berantakan mudah robek",
        "sepatu sempit tidak nyaman cepat rusak sol tipis",
        "tas murahan bahan tipis cepat sobek mengecewakan",
        "jaket tipis tidak hangat jahitan jelek abal",
        "celana mudah luntur bahan tipis jahitan amburadul",
    ],
    'sentimen': ['positif']*15 + ['negatif']*15
}

df_ecom = pd.DataFrame(ulasan_data)

# Preprocessing
def preprocess_sederhana(teks):
    """Preprocessing tanpa stemming (lebih cepat)."""
    teks = teks.lower()
    teks = re.sub(r'[^\w\s]', '', teks)
    return teks

df_ecom['teks_clean'] = df_ecom['teks'].apply(preprocess_sederhana)
df_ecom['label'] = (df_ecom['sentimen'] == 'positif').astype(int)

# Bangun pipeline
pipeline_ecom = Pipeline([
    ('tfidf', TfidfVectorizer(
        max_features=1000,
        ngram_range=(1, 2),    # Unigrams dan bigrams
        min_df=1,              # Minimum document frequency
        max_df=0.95            # Maksimum document frequency
    )),
    ('svm', LinearSVC(C=1.0, random_state=42))
])

# Cross-validation
skor_cv = cross_val_score(
    pipeline_ecom, df_ecom['teks_clean'], df_ecom['label'],
    cv=5, scoring='accuracy'
)
print(f"Cross-validation accuracy: {skor_cv.mean():.4f} ± {skor_cv.std():.4f}")

# Latih pada seluruh data (untuk demo)
pipeline_ecom.fit(df_ecom['teks_clean'], df_ecom['label'])

# Analisis fitur terpenting
tfidf_model = pipeline_ecom.named_steps['tfidf']
svm_model = pipeline_ecom.named_steps['svm']

fitur_names = tfidf_model.get_feature_names_out()
koef = svm_model.coef_[0]

# Top kata positif dan negatif
top_positif = pd.DataFrame({
    'kata': fitur_names[np.argsort(koef)[-10:]],
    'koefisien': np.sort(koef)[-10:]
}).sort_values('koefisien', ascending=False)

top_negatif = pd.DataFrame({
    'kata': fitur_names[np.argsort(koef)[:10]],
    'koefisien': np.sort(koef)[:10]
})

print("\n=== TOP 10 KATA POSITIF ===")
print(top_positif.to_string(index=False))

print("\n=== TOP 10 KATA NEGATIF ===")
print(top_negatif.to_string(index=False))

# Visualisasi
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].barh(top_positif['kata'], top_positif['koefisien'], color='green', alpha=0.7)
axes[0].set_title('Top 10 Kata Positif')
axes[0].set_xlabel('Koefisien SVM')

axes[1].barh(top_negatif['kata'], top_negatif['koefisien'], color='red', alpha=0.7)
axes[1].set_title('Top 10 Kata Negatif')
axes[1].set_xlabel('Koefisien SVM')

plt.tight_layout()
plt.savefig('top_words_sentiment.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## 11.9 AI Corner: AI untuk Analisis Teks

### Level: Advanced

| Kemampuan AI | Contoh Penggunaan |
|-------------|-------------------|
| Preprocessing teks | Meminta AI menyarankan pipeline preprocessing yang tepat |
| Analisis hasil | Meminta AI menginterpretasi kata-kata paling berpengaruh |
| Evaluasi kritis | Meminta AI mengidentifikasi kelemahan model NLP |
| Perbandingan metode | Meminta AI membandingkan BoW vs TF-IDF vs embeddings |

### Contoh Prompt yang Baik

```
Saya membangun sentiment analysis untuk ulasan produk e-commerce Indonesia.
Pipeline saya: preprocessing (lowercase, hapus tanda baca, stopwords Indonesia)
→ TF-IDF (max_features=2000, ngram_range=(1,2)) → LinearSVC.

Hasil: accuracy 87%, F1 positif: 0.89, F1 negatif: 0.85.

Masalah:
- Model salah mengklasifikasi sarkasme: "Wah bagus ya, sampai 2 minggu"
- Kesulitan dengan bahasa informal: "brgnya bgs bgt tp krm lma"

1. Bagaimana cara menangani sarkasme?
2. Bagaimana menangani singkatan bahasa informal Indonesia?
3. Apakah saya perlu word embeddings untuk masalah ini?
```

### Contoh Prompt yang Kurang Baik

```
Buatkan sentiment analysis bahasa Indonesia
```

### Yang Perlu Diingat

1. **AI sangat baik dalam teks Inggris**, tapi mungkin kurang akurat untuk teks Indonesia informal
2. **Verifikasi saran preprocessing** — coba empiris, jangan hanya percaya teori
3. **Data annotation tetap tugas manusia** — AI bisa membantu labeling tapi perlu verifikasi
4. **Privacy** — jangan mengirim data sensitif pelanggan ke AI eksternal

### Template AI Usage Log

```markdown
## AI Usage Documentation — Bab 11
### Tool: [Claude / ChatGPT / Copilot]
### Prompt: "Bagaimana menangani sarkasme dalam sentiment analysis Indonesia?"
### Output: [Saran: contextual embeddings, fitur punctuation, dataset sarkasme khusus]
### Modifikasi: [Menambahkan fitur panjang teks dan jumlah tanda seru]
### Refleksi: [Sarkasme masih sulit, perlu dataset khusus yang lebih besar]
```

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan apa itu NLP dan sebutkan 5 aplikasi NLP yang sering Anda gunakan sehari-hari.

**Soal 2.** Jelaskan perbedaan antara:
- a) Tokenization dan stemming
- b) Stopword removal dan lemmatization
- c) Bag of Words dan TF-IDF

**Soal 3.** Mengapa preprocessing teks penting sebelum membangun model NLP? Sebutkan minimal 5 langkah preprocessing dan tujuan masing-masing.

**Soal 4.** Diberikan corpus berikut:
```
D1: "saya suka makan nasi goreng"
D2: "dia suka makan mie goreng"
D3: "saya tidak suka mie"
```
Buatlah representasi Bag of Words (tabel frekuensi kata) secara manual.

**Soal 5.** Jelaskan secara intuitif (tanpa rumus) bagaimana TF-IDF memberikan bobot berbeda pada kata-kata. Mengapa kata "dan" mendapat bobot rendah?

### Tingkat Menengah (C3)

**Soal 6.** Tulis fungsi Python `preprocess_indonesia(teks)` yang melakukan:
- Lowercase
- Hapus URL, mention, hashtag
- Hapus tanda baca
- Normalisasi kata informal (gak → tidak, bgt → banget, dll.)
- Hapus stopwords Indonesia
- Stemming dengan Sastrawi

**Soal 7.** Bangun pipeline klasifikasi teks untuk mendeteksi **spam vs bukan spam** pada pesan singkat Indonesia. Gunakan data minimal 30 contoh (15 spam, 15 bukan spam). Bandingkan Naive Bayes dan SVM.

**Soal 8.** Jelaskan mengapa bigram (ngram_range=(1,2)) sering lebih baik daripada hanya unigram untuk klasifikasi teks. Berikan contoh kasus di mana bigram menangkap makna yang hilang dari unigram.

### Tingkat Mahir (C4)

**Soal 9.** Anda diminta membangun sistem sentiment analysis untuk ulasan aplikasi mobile Indonesia (dari Google Play Store). Implementasikan:
- a) Data collection: simulasikan 100 ulasan (50 positif, 50 negatif) yang realistis
- b) Preprocessing pipeline lengkap untuk teks Indonesia informal
- c) Bandingkan 3 metode: Naive Bayes, SVM, dan Random Forest
- d) Analisis error: contoh kasus yang salah diklasifikasi dan mengapa
- e) Saran perbaikan berdasarkan analisis error

**Soal 10.** Jelaskan secara kritis perbedaan pendekatan NLP klasik (BoW/TF-IDF + model tradisional) vs modern (BERT/GPT):
- a) Dari segi representasi teks
- b) Dari segi kemampuan menangkap konteks
- c) Dari segi kebutuhan data dan komputasi
- d) Kapan pendekatan klasik masih lebih tepat dari model Transformer?
- e) Bagaimana implikasi untuk NLP Bahasa Indonesia yang memiliki resource terbatas?

---

## Rangkuman

1. **NLP** memungkinkan komputer memproses bahasa manusia. Aplikasi utama: sentiment analysis, chatbot, machine translation, text classification.
2. **Preprocessing teks** meliputi tokenization, lowercasing, punctuation removal, stopword removal, dan stemming. Untuk Bahasa Indonesia, gunakan **Sastrawi** stemmer dan stopwords yang diperluas.
3. **Tantangan NLP Indonesia** meliputi bahasa informal, singkatan, code-switching, sarkasme, dan resource yang lebih terbatas dibanding Bahasa Inggris.
4. **Representasi teks** mengubah teks menjadi vektor numerik. **Bag of Words** menggunakan frekuensi kata; **TF-IDF** memberikan bobot berdasarkan keunikan kata. Word embeddings menangkap makna semantik.
5. **Pipeline NLP**: Preprocessing → Vektorisasi (TF-IDF) → Model (Naive Bayes/SVM) → Evaluasi. **SVM** sering menjadi baseline terkuat untuk klasifikasi teks.
6. **Sentiment analysis** menentukan sentimen (positif/negatif/netral) dari teks. Sangat berguna untuk analisis ulasan produk, media sosial, dan survei.
7. **NLP modern** (Transformers, BERT, GPT) menggunakan mekanisme **attention** untuk menangkap konteks secara lebih baik, tetapi membutuhkan komputasi dan data yang jauh lebih besar.

---

## Referensi

1. Jurafsky, D., & Martin, J. H. (2024). *Speech and Language Processing* (3rd ed. draft). Retrieved from https://web.stanford.edu/~jurafsky/slp3/
2. Bird, S., Klein, E., & Loper, E. (2009). *Natural Language Processing with Python*. O'Reilly Media.
3. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
4. Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.
5. Devlin, J., et al. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. *NAACL-HLT*.
6. Asian, J., et al. (2005). Stemming Indonesian. *Proceedings of the Australasian Language Technology Workshop*.
7. scikit-learn documentation. (2026). *Text Feature Extraction*. Retrieved from https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction

---

*Bab berikutnya: **Bab 12 — Computer Vision Dasar***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
