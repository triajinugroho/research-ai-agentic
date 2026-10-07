# Lab 12: NLP — Text Classification

**Mata Kuliah:** Kecerdasan Buatan dan Machine Learning
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Minggu:** 12
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

- Melakukan preprocessing teks: tokenisasi, lowercasing, penghapusan tanda baca
- Menggunakan library Sastrawi untuk stemming dan stopword removal Bahasa Indonesia
- Membuat dataset teks Bahasa Indonesia untuk klasifikasi sentimen
- Menerapkan TF-IDF vectorization untuk mengubah teks menjadi fitur numerik
- Melatih model klasifikasi teks dengan Naive Bayes dan SVM
- Mengevaluasi model klasifikasi teks dengan confusion matrix dan classification report
- Membandingkan performa classifier untuk teks Bahasa Indonesia

---

## Persiapan

1. Buka Google Colab notebook baru
2. Nama file: `Lab12_NamaAnda_NIM.ipynb`
3. Pastikan library `scikit-learn`, `pandas`, dan `matplotlib` sudah bisa diimpor
4. Install library tambahan: `pip install Sastrawi`

---

## Langkah-langkah

### Langkah 1: Text Preprocessing Dasar

```python
# =============================================
# LANGKAH 1: Text Preprocessing Dasar
# =============================================

import re
import string
import numpy as np
import pandas as pd

# --- Contoh teks ulasan produk e-commerce Indonesia ---
teks_contoh = "Produk ini SANGAT bagus!!! Pengiriman cepat & packaging rapi. 5/5 bintang ⭐⭐⭐"

print("=== TEXT PREPROCESSING DASAR ===\n")
print(f"Teks asli: {teks_contoh}")

# 1. Lowercasing (ubah ke huruf kecil)
teks_lower = teks_contoh.lower()
print(f"\n1. Lowercase: {teks_lower}")

# 2. Hapus tanda baca dan karakter khusus
teks_clean = re.sub(r'[^\w\s]', '', teks_lower)
print(f"2. Hapus tanda baca: {teks_clean}")

# 3. Hapus angka
teks_no_num = re.sub(r'\d+', '', teks_clean)
print(f"3. Hapus angka: {teks_no_num}")

# 4. Hapus spasi berlebih
teks_stripped = re.sub(r'\s+', ' ', teks_no_num).strip()
print(f"4. Hapus spasi lebih: {teks_stripped}")

# 5. Tokenisasi (pecah menjadi kata-kata)
tokens = teks_stripped.split()
print(f"5. Tokenisasi: {tokens}")
print(f"   Jumlah token: {len(tokens)}")

# --- Fungsi preprocessing lengkap ---
def preprocess_teks(teks):
    """Preprocessing teks dasar: lowercase, hapus tanda baca, angka, spasi."""
    teks = teks.lower()
    teks = re.sub(r'[^\w\s]', '', teks)
    teks = re.sub(r'\d+', '', teks)
    teks = re.sub(r'\s+', ' ', teks).strip()
    return teks

# Uji fungsi
print(f"\n--- Test fungsi ---")
test_texts = [
    "Barang JELEK, pecah saat sampai!!! 😡",
    "Lumayan, harga sesuai kualitas.",
    "RECOMMENDED SELLER! cepat & ramah 👍"
]
for t in test_texts:
    print(f"  Asli  : {t}")
    print(f"  Bersih: {preprocess_teks(t)}\n")
```

### Langkah 2: Stemming dan Stopword Removal Bahasa Indonesia

```python
# =============================================
# LANGKAH 2: Sastrawi — Stemming & Stopwords
# =============================================

# Install Sastrawi (library NLP Bahasa Indonesia)
!pip install Sastrawi -q

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# --- Stemming ---
factory_stemmer = StemmerFactory()
stemmer = factory_stemmer.createStemmer()

print("=== STEMMING BAHASA INDONESIA (Sastrawi) ===\n")
kata_uji = ['pengiriman', 'membelikan', 'berlarian',
            'pembelajaran', 'mengesankan', 'terpercaya']
for kata in kata_uji:
    print(f"  {kata:20s} -> {stemmer.stem(kata)}")

# --- Stopword Removal ---
factory_stopword = StopWordRemoverFactory()
stopword_remover = factory_stopword.createStopWordRemover()

print("\n=== STOPWORD REMOVAL ===\n")
kalimat_contoh = "ini adalah contoh kalimat yang akan dihilangkan kata-kata tidak pentingnya"
kalimat_bersih = stopword_remover.remove(kalimat_contoh)
print(f"  Asli  : {kalimat_contoh}")
print(f"  Bersih: {kalimat_bersih}")

# Daftar stopword Indonesia
stopwords_id = factory_stopword.getStopWords()
print(f"\n  Jumlah stopword: {len(stopwords_id)}")
print(f"  Contoh: {stopwords_id[:20]}")

# --- Fungsi preprocessing lengkap (dengan stemming dan stopword) ---
def preprocess_indonesia(teks):
    """Preprocessing teks Bahasa Indonesia: clean, stopword, stemming."""
    # Bersihkan teks
    teks = preprocess_teks(teks)
    # Hapus stopword
    teks = stopword_remover.remove(teks)
    # Stemming
    teks = stemmer.stem(teks)
    return teks

# Test
print("\n--- Test preprocessing lengkap ---")
test = "Pengiriman sangat cepat dan pelayanan yang memuaskan sekali"
print(f"  Asli  : {test}")
print(f"  Proses: {preprocess_indonesia(test)}")
```

### Langkah 3: Membuat Dataset Ulasan Produk Indonesia

```python
# =============================================
# LANGKAH 3: Dataset Ulasan Produk Indonesia
# =============================================

# Dataset simulasi ulasan produk e-commerce Indonesia
data_ulasan = {
    'ulasan': [
        # Positif (label 1)
        "Produk sangat bagus, pengiriman cepat dan rapi",
        "Kualitas bahan premium, jahitan rapi, recommended seller",
        "Barang sesuai deskripsi, penjual ramah dan responsif",
        "Sangat puas dengan pembelian ini, akan beli lagi",
        "Packaging aman, barang sampai dengan selamat, terima kasih",
        "Harga terjangkau tapi kualitas mantap, tidak mengecewakan",
        "Warna sesuai gambar, ukuran pas, bahan nyaman dipakai",
        "Respon penjual cepat, pengiriman tepat waktu, top seller",
        "Sudah beli berkali-kali di toko ini, selalu puas",
        "Produk original dan berkualitas, layanan pelanggan bagus",
        "Desain keren dan modern, bahan tebal dan tidak mudah rusak",
        "Pengiriman dari Jakarta hanya 2 hari, luar biasa cepat",
        "Anak saya suka sekali dengan produk ini, terima kasih",
        "Murah meriah tapi barangnya oke punya, bintang lima",
        "Toko terpercaya, sudah langganan sejak tahun lalu",
        # Negatif (label 0)
        "Barang tidak sesuai deskripsi, warna beda jauh",
        "Kualitas buruk, bahan tipis dan mudah robek",
        "Pengiriman sangat lambat, sudah 2 minggu belum sampai",
        "Barang cacat, ada goresan dan penyok saat diterima",
        "Penjual tidak responsif, chat dibaca tapi tidak dibalas",
        "Ukuran tidak sesuai, terlalu kecil dari yang diharapkan",
        "Packaging asal-asalan, barang rusak saat sampai",
        "Sangat kecewa, produk murahan tapi harga mahal",
        "Barang palsu, bukan original seperti yang dijanjikan",
        "Warna luntur setelah dicuci pertama kali, mengecewakan",
        "Bau bahan kimia menyengat, tidak layak dipakai",
        "Sudah komplain tapi tidak ada penyelesaian dari toko",
        "Jahitan berantakan dan benang keluar dimana-mana",
        "Tidak rekomendasi toko ini, pelayanan sangat buruk",
        "Menyesal beli di sini, buang-buang uang saja",
    ],
    'sentimen': [1]*15 + [0]*15  # 1 = positif, 0 = negatif
}

df = pd.DataFrame(data_ulasan)

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

print("=== DATASET ULASAN PRODUK E-COMMERCE INDONESIA ===")
print(f"Jumlah ulasan: {len(df)}")
print(f"Distribusi sentimen:")
print(df['sentimen'].value_counts().rename({1: 'Positif', 0: 'Negatif'}))

# Terapkan preprocessing
print("\n--- Menerapkan preprocessing ---")
df['ulasan_bersih'] = df['ulasan'].apply(preprocess_indonesia)

# Tampilkan sampel
print("\nSampel data:")
for _, row in df.head(5).iterrows():
    label = "Positif" if row['sentimen'] == 1 else "Negatif"
    print(f"  [{label}]")
    print(f"    Asli  : {row['ulasan']}")
    print(f"    Bersih: {row['ulasan_bersih']}\n")
```

### Langkah 4: TF-IDF Vectorization

```python
# =============================================
# LANGKAH 4: TF-IDF Vectorization
# =============================================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Split data: 80% train, 20% test
X_train_text, X_test_text, y_train, y_test = train_test_split(
    df['ulasan_bersih'], df['sentimen'],
    test_size=0.2, random_state=42, stratify=df['sentimen']
)

print(f"Training set: {len(X_train_text)} ulasan")
print(f"Test set: {len(X_test_text)} ulasan")

# TF-IDF Vectorizer
tfidf = TfidfVectorizer(
    max_features=1000,      # Maksimal 1000 kata
    ngram_range=(1, 2),     # Unigram dan bigram
    min_df=1,               # Minimal muncul di 1 dokumen
    max_df=0.95             # Maksimal muncul di 95% dokumen
)

# Fit dan transform pada data training
X_train_tfidf = tfidf.fit_transform(X_train_text)
X_test_tfidf = tfidf.transform(X_test_text)

print(f"\nShape TF-IDF matrix (train): {X_train_tfidf.shape}")
print(f"Shape TF-IDF matrix (test) : {X_test_tfidf.shape}")

# Tampilkan kosakata (vocabulary)
vocab = tfidf.get_feature_names_out()
print(f"\nJumlah fitur (kosakata): {len(vocab)}")
print(f"Contoh fitur: {list(vocab[:15])}")

# Tampilkan TF-IDF tertinggi untuk satu dokumen
first_doc = X_train_tfidf[0].toarray().flatten()
top_indices = first_doc.argsort()[-10:][::-1]
print(f"\nTop 10 kata dengan TF-IDF tertinggi (dokumen pertama):")
for idx in top_indices:
    if first_doc[idx] > 0:
        print(f"  {vocab[idx]:20s} : {first_doc[idx]:.4f}")
```

### Langkah 5: Klasifikasi dengan Naive Bayes

```python
# =============================================
# LANGKAH 5: Klasifikasi — Naive Bayes
# =============================================

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Latih model Multinomial Naive Bayes
model_nb = MultinomialNB(alpha=1.0)  # alpha = Laplace smoothing
model_nb.fit(X_train_tfidf, y_train)

# Prediksi
y_pred_nb = model_nb.predict(X_test_tfidf)

# Akurasi
acc_nb = accuracy_score(y_test, y_pred_nb)
print("=== NAIVE BAYES (MultinomialNB) ===")
print(f"Akurasi: {acc_nb:.4f} ({acc_nb*100:.1f}%)")

# Prediksi pada contoh baru
contoh_baru = [
    "Produk ini sangat bagus dan pengiriman cepat",
    "Barangnya rusak dan penjual tidak mau tanggung jawab",
    "Lumayan lah untuk harga segitu"
]

print("\n--- Prediksi Ulasan Baru ---")
for teks in contoh_baru:
    teks_bersih = preprocess_indonesia(teks)
    teks_tfidf = tfidf.transform([teks_bersih])
    pred = model_nb.predict(teks_tfidf)[0]
    prob = model_nb.predict_proba(teks_tfidf)[0]
    label = "Positif" if pred == 1 else "Negatif"
    print(f"  Ulasan : {teks}")
    print(f"  Prediksi: {label} (prob positif: {prob[1]:.3f})\n")
```

### Langkah 6: Klasifikasi dengan SVM

```python
# =============================================
# LANGKAH 6: Klasifikasi — SVM
# =============================================

from sklearn.svm import SVC

# Latih model SVM
model_svm = SVC(kernel='linear', probability=True, random_state=42)
model_svm.fit(X_train_tfidf, y_train)

# Prediksi
y_pred_svm = model_svm.predict(X_test_tfidf)

# Akurasi
acc_svm = accuracy_score(y_test, y_pred_svm)
print("=== SVM (Linear Kernel) ===")
print(f"Akurasi: {acc_svm:.4f} ({acc_svm*100:.1f}%)")

# Prediksi ulasan baru dengan SVM
print("\n--- Prediksi Ulasan Baru (SVM) ---")
for teks in contoh_baru:
    teks_bersih = preprocess_indonesia(teks)
    teks_tfidf = tfidf.transform([teks_bersih])
    pred = model_svm.predict(teks_tfidf)[0]
    prob = model_svm.predict_proba(teks_tfidf)[0]
    label = "Positif" if pred == 1 else "Negatif"
    print(f"  Ulasan : {teks}")
    print(f"  Prediksi: {label} (prob positif: {prob[1]:.3f})\n")
```

### Langkah 7: Evaluasi — Confusion Matrix dan Classification Report

```python
# =============================================
# LANGKAH 7: Evaluasi Lengkap
# =============================================

from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Confusion Matrix — Naive Bayes
cm_nb = confusion_matrix(y_test, y_pred_nb)
sns.heatmap(cm_nb, annot=True, fmt='d', cmap='Blues', ax=axes[0],
            xticklabels=['Negatif', 'Positif'],
            yticklabels=['Negatif', 'Positif'])
axes[0].set_xlabel('Prediksi')
axes[0].set_ylabel('Aktual')
axes[0].set_title(f'Naive Bayes (Akurasi: {acc_nb:.2f})')

# Confusion Matrix — SVM
cm_svm = confusion_matrix(y_test, y_pred_svm)
sns.heatmap(cm_svm, annot=True, fmt='d', cmap='Oranges', ax=axes[1],
            xticklabels=['Negatif', 'Positif'],
            yticklabels=['Negatif', 'Positif'])
axes[1].set_xlabel('Prediksi')
axes[1].set_ylabel('Aktual')
axes[1].set_title(f'SVM Linear (Akurasi: {acc_svm:.2f})')

plt.suptitle('Confusion Matrix — Klasifikasi Sentimen Ulasan', fontsize=14)
plt.tight_layout()
plt.show()

# Classification Report
print("=== CLASSIFICATION REPORT — NAIVE BAYES ===")
print(classification_report(y_test, y_pred_nb,
                            target_names=['Negatif', 'Positif']))

print("=== CLASSIFICATION REPORT — SVM ===")
print(classification_report(y_test, y_pred_svm,
                            target_names=['Negatif', 'Positif']))
```

### Langkah 8: Perbandingan Classifier

```python
# =============================================
# LANGKAH 8: Perbandingan Classifier
# =============================================

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

print("=" * 60)
print("PERBANDINGAN CLASSIFIER UNTUK TEKS BAHASA INDONESIA")
print("=" * 60)

# Gabungkan semua data untuk cross-validation
X_all_tfidf = tfidf.fit_transform(df['ulasan_bersih'])
y_all = df['sentimen'].values

classifiers = {
    'Naive Bayes (Multinomial)': MultinomialNB(alpha=1.0),
    'SVM (Linear)': SVC(kernel='linear', random_state=42),
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
}

results = {}
for name, clf in classifiers.items():
    scores = cross_val_score(clf, X_all_tfidf, y_all, cv=5, scoring='accuracy')
    results[name] = {'mean': scores.mean(), 'std': scores.std()}
    print(f"\n{name}:")
    print(f"  Akurasi (5-fold CV): {scores.mean():.4f} (+/- {scores.std():.4f})")
    print(f"  Skor per fold: {[f'{s:.3f}' for s in scores]}")

# Visualisasi perbandingan
plt.figure(figsize=(10, 5))
names = list(results.keys())
means = [r['mean'] for r in results.values()]
stds = [r['std'] for r in results.values()]

colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
bars = plt.bar(range(len(names)), means, yerr=stds, capsize=5,
               color=colors, edgecolor='white')
plt.xticks(range(len(names)), names, rotation=15, ha='right')
plt.ylabel('Akurasi (5-Fold CV)')
plt.title('Perbandingan Classifier — Sentimen Ulasan E-Commerce Indonesia')
plt.grid(axis='y', alpha=0.3)

for bar, mean in zip(bars, means):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
             f'{mean:.3f}', ha='center', fontsize=11)

plt.tight_layout()
plt.show()

print("\nKesimpulan:")
print("- Naive Bayes: cepat, baseline yang baik untuk text classification")
print("- SVM Linear: sering unggul untuk data teks berdimensi tinggi")
print("- Logistic Regression: interpretable, performa kompetitif")
print("- Random Forest: kurang optimal untuk fitur sparse (TF-IDF)")
print("\nCatatan: Dataset kecil (30 ulasan) — performa akan lebih baik")
print("dengan dataset yang lebih besar dan beragam.")
```

---

## Tantangan Tambahan

1. **Perbesar Dataset:** Tambahkan minimal 20 ulasan lagi (10 positif, 10 negatif) ke dataset. Apakah akurasi meningkat? Bandingkan performa sebelum dan sesudah penambahan data.

2. **Analisis Sentimen 3 Kelas:** Modifikasi dataset agar memiliki 3 kelas sentimen: positif, netral, dan negatif. Latih ulang model dan analisis bagaimana penambahan kelas netral mempengaruhi performa klasifikasi.

3. **Word Cloud Visualization:** Install library `wordcloud` dan buat word cloud terpisah untuk ulasan positif dan negatif. Kata apa saja yang paling sering muncul di masing-masing kategori?

---

## Checklist Penyelesaian

- [ ] Langkah 1: Text preprocessing dasar berhasil (lowercase, tanda baca, tokenisasi)
- [ ] Langkah 2: Sastrawi berhasil di-install, stemming dan stopword removal berfungsi
- [ ] Langkah 3: Dataset ulasan Indonesia berhasil dibuat dan di-preprocess
- [ ] Langkah 4: TF-IDF vectorization berhasil menghasilkan matriks fitur
- [ ] Langkah 5: Naive Bayes berhasil dilatih dan memprediksi sentimen
- [ ] Langkah 6: SVM berhasil dilatih dan memprediksi sentimen
- [ ] Langkah 7: Confusion matrix dan classification report berhasil dibuat
- [ ] Langkah 8: Perbandingan 4 classifier berhasil dilakukan dengan cross-validation
- [ ] Semua kode berjalan tanpa error di Google Colab
- [ ] Notebook disimpan dengan format `Lab12_NamaAnda_NIM.ipynb`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
