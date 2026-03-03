# Minggu 6: Decision Tree dan Random Forest

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 6 |
| **Topik** | Decision Tree dan Random Forest |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-3: Menerapkan dan menganalisis algoritma supervised learning |
| **Sub-CPMK** | 6.1 Menganalisis algoritma Decision Tree termasuk entropy, information gain, dan Gini impurity |
| | 6.2 Menganalisis ensemble method Random Forest dan membandingkan performanya dengan single Decision Tree |
| **Bloom's Taxonomy** | C4 (Menganalisis / *Analyze*) |
| **Durasi** | 2 x 100 menit (Teori 100 min + Praktikum 100 min) |
| **Platform** | Google Colab |
| **Metode** | Ceramah interaktif, live coding, hands-on praktikum |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menganalisis** prinsip kerja Decision Tree termasuk konsep entropy, information gain, dan Gini impurity sebagai kriteria pemisahan (*splitting*).
2. **Menjelaskan** proses pembangunan Decision Tree: pemilihan fitur terbaik, *splitting*, dan *pruning*.
3. **Memvisualisasikan** struktur Decision Tree menggunakan scikit-learn dan menginterpretasikan aturan keputusan.
4. **Mengidentifikasi** masalah *overfitting* pada Decision Tree dan strategi penanganannya.
5. **Menganalisis** konsep *ensemble methods* khususnya *bagging* sebagai dasar Random Forest.
6. **Membandingkan** performa Decision Tree tunggal dengan Random Forest pada dataset nyata.
7. **Menerapkan** teknik *hyperparameter tuning* untuk mengoptimalkan performa model berbasis pohon.

---

## Materi Pembelajaran

### 1. Decision Tree: Konsep Dasar

#### Apa Itu Decision Tree?

Decision Tree (Pohon Keputusan) adalah algoritma supervised learning yang membuat keputusan dengan memecah data menjadi subset-subset berdasarkan pertanyaan ya/tidak pada fitur-fiturnya. Hasilnya menyerupai struktur pohon terbalik.

#### Analogi Kehidupan Sehari-hari

Bayangkan seorang petugas bank di Indonesia menentukan persetujuan kredit:

```
                  [Pendapatan > 10 juta/bulan?]
                  /                            \
               Ya                               Tidak
              /                                    \
   [Skor BI Checking ≤ 2?]               [Punya Jaminan?]
    /                \                     /            \
  Ya                 Tidak               Ya             Tidak
   |                   |                  |               |
DISETUJUI          [Rasio Utang < 0.5?]  REVIEW         DITOLAK
                    /          \
                  Ya           Tidak
                   |              |
               DISETUJUI       DITOLAK
```

Setiap simpul (*node*) berisi pertanyaan, setiap cabang (*branch*) berisi jawaban, dan setiap daun (*leaf*) berisi keputusan akhir.

#### Terminologi Penting

| Istilah | Penjelasan |
|---|---|
| **Root Node** | Simpul paling atas; pertanyaan pertama |
| **Internal Node** | Simpul di tengah; pertanyaan lanjutan |
| **Leaf Node** | Simpul paling bawah; keputusan akhir |
| **Branch** | Cabang yang menghubungkan simpul |
| **Depth** | Jarak dari root ke leaf terdalam |
| **Splitting** | Proses membagi data berdasarkan fitur |
| **Pruning** | Proses memangkas pohon untuk mengurangi overfitting |

---

### 2. Kriteria Pemisahan: Entropy dan Information Gain

#### Entropy

Entropy mengukur **ketidakpastian** atau **keacakan** dalam data. Semakin campuran datanya, semakin tinggi entropy-nya.

```
Entropy(S) = -Σ pᵢ × log₂(pᵢ)

Di mana pᵢ = proporsi kelas ke-i
```

Contoh:
- Dataset dengan 50% Disetujui, 50% Ditolak → Entropy = 1.0 (ketidakpastian maksimal)
- Dataset dengan 100% Disetujui → Entropy = 0.0 (pasti, tidak ada ketidakpastian)
- Dataset dengan 90% Disetujui, 10% Ditolak → Entropy = 0.47 (cukup pasti)

```
Entropy
  1.0 |      *
      |    *   *
      |   *     *
  0.5 |  *       *
      | *         *
  0.0 |*           *
      +--+--+--+--+--
      0  .25 .5 .75 1
      Proporsi kelas positif
```

#### Information Gain

Information Gain mengukur **pengurangan entropy** setelah melakukan *splitting* berdasarkan suatu fitur:

```
IG(S, A) = Entropy(S) - Σ (|Sᵥ|/|S|) × Entropy(Sᵥ)

Di mana:
- S = dataset sebelum split
- A = fitur yang digunakan untuk split
- Sᵥ = subset setelah split berdasarkan nilai v dari fitur A
```

Fitur dengan **Information Gain tertinggi** dipilih sebagai simpul (*node*) berikutnya.

#### Gini Impurity

Alternatif dari entropy yang lebih cepat dihitung:

```
Gini(S) = 1 - Σ pᵢ²
```

- Gini = 0: semua data satu kelas (murni)
- Gini = 0.5: campuran seimbang dua kelas (tidak murni maksimal)

Scikit-learn menggunakan Gini sebagai default karena lebih efisien secara komputasi.

---

### 3. Membangun Decision Tree

#### Proses Pembangunan

1. **Pilih fitur terbaik** untuk root node (information gain atau Gini tertinggi)
2. **Split data** berdasarkan fitur tersebut
3. **Ulangi** secara rekursif untuk setiap subset
4. **Berhenti** jika memenuhi kriteria: semua data satu kelas, kedalaman maksimal tercapai, atau jumlah sampel terlalu kecil

#### Pruning (Pemangkasan)

Pruning mencegah pohon tumbuh terlalu kompleks:

| Jenis Pruning | Penjelasan |
|---|---|
| **Pre-pruning** | Membatasi pertumbuhan pohon sejak awal (max_depth, min_samples_split, min_samples_leaf) |
| **Post-pruning** | Membangun pohon penuh lalu memangkas cabang yang tidak signifikan |

#### Hyperparameter Penting

| Parameter | Fungsi | Efek |
|---|---|---|
| `max_depth` | Kedalaman maksimal pohon | Semakin kecil → lebih sederhana, kurang overfit |
| `min_samples_split` | Minimal sampel untuk split | Semakin besar → lebih konservatif |
| `min_samples_leaf` | Minimal sampel di leaf | Mencegah leaf dengan sangat sedikit data |
| `max_features` | Jumlah fitur yang dipertimbangkan | Membantu generalisasi |

---

### 4. Overfitting pada Decision Tree

#### Masalah Overfitting

Decision Tree sangat rentan terhadap *overfitting* -- model terlalu menghafal data training sehingga gagal pada data baru.

```
Akurasi
  1.0 |  Training _______________
      |          /
      |         /   Testing
  0.8 |        / ____/\________
      |       /              \
  0.6 |      /                \_______
      |     /
      +----+----+----+----+----+----
           2    4    6    8   10  ∞
                max_depth
```

Tanda-tanda overfitting:
- Akurasi training **sangat tinggi** (mendekati 100%)
- Akurasi testing **jauh lebih rendah**
- Pohon terlalu dalam dengan banyak leaf

#### Strategi Mengatasi Overfitting

1. Batasi `max_depth` (misalnya 3-10)
2. Tingkatkan `min_samples_split` (misalnya 10-20)
3. Gunakan *cross-validation* untuk menemukan parameter optimal
4. **Gunakan ensemble methods** seperti Random Forest

---

### 5. Ensemble Methods: Konsep Bagging

#### Filosofi: "Wisdom of the Crowd"

Satu pohon bisa salah, tetapi **banyak pohon yang beragam** cenderung memberikan jawaban yang lebih baik. Ini mirip dengan musyawarah dalam Islam -- keputusan kolektif sering lebih baik dari keputusan individu.

#### Bagging (Bootstrap Aggregating)

Bagging bekerja dengan tiga langkah:

```
Dataset Asli (N sampel)
       |
       ├── Bootstrap Sample 1 → Tree 1 → Prediksi 1
       ├── Bootstrap Sample 2 → Tree 2 → Prediksi 2
       ├── Bootstrap Sample 3 → Tree 3 → Prediksi 3
       ├── ...
       └── Bootstrap Sample B → Tree B → Prediksi B
                                              |
                                         Voting / Rata-rata
                                              |
                                        Prediksi Akhir
```

- **Bootstrap sampling**: mengambil sampel acak **dengan pengembalian** dari dataset asli
- Setiap sampel berukuran sama dengan dataset asli, tetapi beberapa data mungkin terduplikasi
- Prediksi akhir ditentukan melalui **voting mayoritas** (klasifikasi) atau **rata-rata** (regresi)

---

### 6. Random Forest

#### Dari Bagging ke Random Forest

Random Forest menambahkan **keacakan fitur** (*feature randomness*) di atas bagging:

- Pada setiap split, hanya **subset acak fitur** yang dipertimbangkan (bukan semua fitur)
- Ini membuat setiap pohon lebih berbeda (*diverse*) satu sama lain
- Menghasilkan prediksi ensemble yang lebih robust

#### Keunggulan Random Forest

| Keunggulan | Penjelasan |
|---|---|
| Akurasi tinggi | Menggabungkan banyak pohon mengurangi variansi |
| Robust terhadap overfitting | Jauh lebih stabil dibanding single Decision Tree |
| Feature importance | Otomatis menghitung pentingnya setiap fitur |
| Versatile | Bisa untuk klasifikasi dan regresi |
| Sedikit preprocessing | Tidak butuh normalisasi/standardisasi fitur |

#### Feature Importance

Random Forest menghitung pentingnya setiap fitur berdasarkan seberapa besar fitur tersebut mengurangi impurity di seluruh pohon:

```
Feature Importance (Contoh: Prediksi Churn Nasabah Bank)
  |
  |████████████████  Saldo Tabungan (0.35)
  |████████████      Frekuensi Transaksi (0.25)
  |████████          Lama Menjadi Nasabah (0.18)
  |██████            Jumlah Produk (0.12)
  |████              Usia (0.07)
  |██                Jenis Kelamin (0.03)
  +------------------------------------------
```

---

### 7. Hyperparameter Tuning untuk Model Berbasis Pohon

#### Parameter Utama Random Forest

| Parameter | Fungsi | Nilai Umum |
|---|---|---|
| `n_estimators` | Jumlah pohon dalam forest | 100-500 |
| `max_depth` | Kedalaman maksimal setiap pohon | 5-20, atau None |
| `min_samples_split` | Minimal sampel untuk split | 2-20 |
| `min_samples_leaf` | Minimal sampel di leaf | 1-10 |
| `max_features` | Fitur yang dipertimbangkan per split | 'sqrt', 'log2', atau angka |

#### Strategi Tuning

1. **Mulai dari default**: scikit-learn sudah memiliki default yang cukup baik
2. **Grid Search**: coba semua kombinasi parameter yang ditentukan
3. **Random Search**: lebih efisien untuk ruang pencarian yang besar
4. **Evaluasi dengan cross-validation**: hindari overfitting pada test set

---

## Aktivitas Kelas

### Sesi 1: Teori dan Diskusi (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Review & Pembukaan | Review regresi minggu 5, pengantar Decision Tree |
| 20 menit | Ceramah Interaktif | Decision Tree: entropy, information gain, Gini impurity |
| 15 menit | Latihan Perhitungan | Menghitung entropy dan information gain secara manual (contoh tabel keputusan kredit) |
| 15 menit | Ceramah Interaktif | Overfitting, pruning, dan pengantar ensemble methods |
| 15 menit | Ceramah Interaktif | Random Forest: bagging, feature randomness, feature importance |
| 15 menit | Diskusi Kelompok | Studi kasus: mengapa bank menggunakan Random Forest untuk credit scoring? |
| 10 menit | Tanya Jawab | Klarifikasi konsep sebelum masuk praktikum |

### Sesi 2: Praktikum Hands-on (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Setup & Data Loading | Buka Google Colab, import library, buat dataset churn |
| 25 menit | Hands-on Decision Tree | Bangun, latih, dan visualisasikan Decision Tree |
| 10 menit | Analisis Overfitting | Bandingkan akurasi training vs testing pada berbagai max_depth |
| 25 menit | Hands-on Random Forest | Bangun Random Forest, bandingkan dengan single tree |
| 20 menit | Feature Importance & Tuning | Analisis feature importance, coba GridSearchCV |
| 10 menit | Wrap-up & Preview | Rangkuman, pengenalan SVM dan KNN minggu depan |

---

## Hands-on: Klasifikasi Churn Nasabah Bank Indonesia

### Langkah 1: Import Library

```python
# Import library yang dibutuhkan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (classification_report, confusion_matrix,
                             accuracy_score)
from sklearn.preprocessing import LabelEncoder

print("Semua library berhasil di-import!")
```

### Langkah 2: Membuat Dataset Churn Nasabah Bank Indonesia

```python
# Dataset churn nasabah bank Indonesia (simulasi)
np.random.seed(42)
n = 500

usia = np.random.randint(18, 65, n)
saldo_juta = np.random.exponential(50, n).round(1)
frekuensi_transaksi = np.random.poisson(15, n)
lama_nasabah_tahun = np.random.randint(1, 20, n)
jumlah_produk = np.random.randint(1, 5, n)
punya_kartu_kredit = np.random.choice([0, 1], n, p=[0.4, 0.6])
punya_mobile_banking = np.random.choice([0, 1], n, p=[0.3, 0.7])

# Logika churn: nasabah dengan saldo rendah, transaksi sedikit,
# dan tidak aktif cenderung churn
skor = (-0.02 * saldo_juta + 0.05 * usia - 0.1 * frekuensi_transaksi
        - 0.08 * lama_nasabah_tahun - 0.3 * jumlah_produk
        - 0.5 * punya_mobile_banking + np.random.normal(0, 1, n))
churn = (skor > np.percentile(skor, 70)).astype(int)

df_churn = pd.DataFrame({
    'usia': usia,
    'saldo_juta': saldo_juta,
    'frekuensi_transaksi': frekuensi_transaksi,
    'lama_nasabah_tahun': lama_nasabah_tahun,
    'jumlah_produk': jumlah_produk,
    'punya_kartu_kredit': punya_kartu_kredit,
    'punya_mobile_banking': punya_mobile_banking,
    'churn': churn
})

print("Dataset Churn Nasabah Bank Indonesia:")
print(df_churn.head(10))
print(f"\nJumlah data: {len(df_churn)}")
print(f"\nDistribusi churn:")
print(df_churn['churn'].value_counts())
print(f"\nChurn rate: {df_churn['churn'].mean()*100:.1f}%")
```

### Langkah 3: Persiapan Data

```python
# Fitur dan target
X = df_churn.drop('churn', axis=1)
y = df_churn['churn']

# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Data training: {len(X_train)} sampel")
print(f"Data testing : {len(X_test)} sampel")
print(f"\nDistribusi churn di training:")
print(y_train.value_counts(normalize=True).round(3))
```

### Langkah 4: Melatih Decision Tree

```python
# Decision Tree dengan max_depth terbatas (untuk menghindari overfitting)
dt_model = DecisionTreeClassifier(max_depth=4, random_state=42)
dt_model.fit(X_train, y_train)

# Prediksi
y_pred_dt = dt_model.predict(X_test)

# Evaluasi
print("=== Decision Tree (max_depth=4) ===")
print(f"Akurasi Training: {dt_model.score(X_train, y_train)*100:.1f}%")
print(f"Akurasi Testing : {accuracy_score(y_test, y_pred_dt)*100:.1f}%")
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred_dt,
      target_names=['Tidak Churn', 'Churn']))
```

### Langkah 5: Visualisasi Decision Tree

```python
# Visualisasi pohon keputusan
plt.figure(figsize=(20, 10))
plot_tree(dt_model,
          feature_names=X.columns,
          class_names=['Tidak Churn', 'Churn'],
          filled=True,
          rounded=True,
          fontsize=10,
          proportion=True)
plt.title('Decision Tree - Prediksi Churn Nasabah Bank', fontsize=16)
plt.tight_layout()
plt.show()

# Cetak aturan keputusan penting
print("=== Aturan Keputusan Utama ===")
feature_importance_dt = pd.Series(
    dt_model.feature_importances_, index=X.columns
).sort_values(ascending=False)
print(feature_importance_dt.round(4))
```

### Langkah 6: Analisis Overfitting

```python
# Bandingkan akurasi training vs testing pada berbagai max_depth
depths = range(1, 21)
train_scores = []
test_scores = []

for depth in depths:
    dt_temp = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt_temp.fit(X_train, y_train)
    train_scores.append(dt_temp.score(X_train, y_train))
    test_scores.append(dt_temp.score(X_test, y_test))

# Visualisasi
plt.figure(figsize=(10, 6))
plt.plot(depths, train_scores, 'b-o', label='Training Accuracy', markersize=4)
plt.plot(depths, test_scores, 'r-o', label='Testing Accuracy', markersize=4)
plt.xlabel('Max Depth')
plt.ylabel('Accuracy')
plt.title('Decision Tree: Training vs Testing Accuracy')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axvline(x=depths[np.argmax(test_scores)], color='green',
            linestyle='--', label=f'Best depth={depths[np.argmax(test_scores)]}')
plt.legend()
plt.tight_layout()
plt.show()

print(f"Best max_depth: {depths[np.argmax(test_scores)]}")
print(f"Best testing accuracy: {max(test_scores)*100:.1f}%")
print(f"Training accuracy at best depth: {train_scores[np.argmax(test_scores)]*100:.1f}%")
```

### Langkah 7: Random Forest

```python
# Random Forest
rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=8,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1  # Gunakan semua core CPU
)
rf_model.fit(X_train, y_train)

# Prediksi
y_pred_rf = rf_model.predict(X_test)

# Evaluasi
print("=== Random Forest (100 trees, max_depth=8) ===")
print(f"Akurasi Training: {rf_model.score(X_train, y_train)*100:.1f}%")
print(f"Akurasi Testing : {accuracy_score(y_test, y_pred_rf)*100:.1f}%")
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred_rf,
      target_names=['Tidak Churn', 'Churn']))

# Perbandingan dengan Decision Tree
print("\n=== Perbandingan ===")
print(f"Decision Tree Accuracy: {accuracy_score(y_test, y_pred_dt)*100:.1f}%")
print(f"Random Forest Accuracy: {accuracy_score(y_test, y_pred_rf)*100:.1f}%")
```

### Langkah 8: Feature Importance dari Random Forest

```python
# Feature importance
feature_imp = pd.Series(
    rf_model.feature_importances_, index=X.columns
).sort_values(ascending=True)

plt.figure(figsize=(10, 6))
feature_imp.plot(kind='barh', color='steelblue', edgecolor='black')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Random Forest: Feature Importance - Prediksi Churn')
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.show()

print("=== Feature Importance ===")
for feat, imp in feature_imp.sort_values(ascending=False).items():
    print(f"  {feat}: {imp:.4f} ({imp*100:.1f}%)")
```

### Langkah 9: Hyperparameter Tuning dengan GridSearchCV

```python
# GridSearchCV untuk Random Forest
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [4, 6, 8, 10],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X_train, y_train)

print(f"\n=== Hasil GridSearchCV ===")
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best F1-Score (CV): {grid_search.best_score_:.4f}")

# Evaluasi model terbaik
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test)
print(f"\nAkurasi Testing (Best Model): {accuracy_score(y_test, y_pred_best)*100:.1f}%")
print(f"\nClassification Report (Best Model):")
print(classification_report(y_test, y_pred_best,
      target_names=['Tidak Churn', 'Churn']))
```

### Langkah 10: Perbandingan Confusion Matrix

```python
# Perbandingan confusion matrix: Decision Tree vs Random Forest
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Decision Tree
cm_dt = confusion_matrix(y_test, y_pred_dt)
sns.heatmap(cm_dt, annot=True, fmt='d', cmap='Oranges', ax=axes[0],
            xticklabels=['Tidak Churn', 'Churn'],
            yticklabels=['Tidak Churn', 'Churn'])
axes[0].set_xlabel('Prediksi')
axes[0].set_ylabel('Aktual')
axes[0].set_title(f'Decision Tree\n(Accuracy: {accuracy_score(y_test, y_pred_dt)*100:.1f}%)')

# Random Forest
cm_rf = confusion_matrix(y_test, y_pred_rf)
sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Blues', ax=axes[1],
            xticklabels=['Tidak Churn', 'Churn'],
            yticklabels=['Tidak Churn', 'Churn'])
axes[1].set_xlabel('Prediksi')
axes[1].set_ylabel('Aktual')
axes[1].set_title(f'Random Forest\n(Accuracy: {accuracy_score(y_test, y_pred_rf)*100:.1f}%)')

plt.suptitle('Perbandingan Confusion Matrix: Decision Tree vs Random Forest', fontsize=14)
plt.tight_layout()
plt.show()
```

---

## AI Corner: Menggunakan AI untuk Menjelaskan Keputusan Pohon

> **Level: Intermediate** -- Menggunakan AI untuk memahami dan menjelaskan aturan keputusan yang dihasilkan model berbasis pohon.

### Cara AI Bisa Membantu

| Skenario | Contoh Prompt ke AI |
|---|---|
| Interpretasi pohon | *"Decision tree saya memiliki root node 'saldo < 25 juta'. Jelaskan mengapa fitur ini paling penting untuk prediksi churn"* |
| Penjelasan ensemble | *"Jelaskan dengan analogi sederhana mengapa Random Forest lebih baik dari satu Decision Tree"* |
| Tuning advice | *"Random Forest saya overfitting (training acc 98%, test acc 75%). Parameter apa yang harus saya ubah?"* |
| Feature importance | *"Fitur 'punya_mobile_banking' memiliki importance 0.05. Apakah sebaiknya dihapus?"* |
| Business insight | *"Berdasarkan feature importance churn model, strategi retensi apa yang bisa bank terapkan?"* |

### Tips Penting

1. **Minta AI menjelaskan aturan pohon** dalam bahasa bisnis, bukan hanya teknis.
2. **Gunakan AI untuk brainstorming** fitur baru berdasarkan domain knowledge.
3. **Verifikasi saran tuning** AI dengan menjalankan eksperimen sendiri.
4. **Dokumentasikan** setiap penggunaan AI dalam AI Usage Log.

### Contoh Prompt Minggu Ini

Coba masukkan prompt berikut ke ChatGPT atau Claude:

```
Saya membangun model Random Forest untuk prediksi churn nasabah bank
di Indonesia. Feature importance menunjukkan:
- saldo_juta: 0.35
- frekuensi_transaksi: 0.25
- lama_nasabah_tahun: 0.18
- jumlah_produk: 0.12
- usia: 0.07
- punya_mobile_banking: 0.03

1. Interpretasikan feature importance ini dalam konteks bisnis perbankan Indonesia.
2. Strategi retensi apa yang bisa bank terapkan berdasarkan insight ini?
3. Fitur tambahan apa yang mungkin berguna untuk meningkatkan model?
```

Bandingkan jawaban AI dengan analisis Anda sendiri dari praktikum.

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **Interpretabilitas:** Mengapa Decision Tree sering disebut sebagai model yang *interpretable*? Dalam konteks regulasi perbankan Indonesia (OJK), mengapa interpretabilitas model penting?

2. **Overfitting:** Jelaskan dengan kata-kata sendiri mengapa Decision Tree tanpa batasan kedalaman rentan overfitting. Hubungkan dengan konsep bias-variance tradeoff.

3. **Ensemble vs Individual:** Dalam kehidupan sehari-hari, berikan contoh keputusan yang lebih baik diambil secara kolektif (seperti musyawarah) dibanding individual. Bagaimana ini berhubungan dengan konsep ensemble?

4. **Etika Feature Importance:** Jika model churn menunjukkan bahwa fitur "lokasi_cabang" sangat penting, dan ternyata ini berkorelasi dengan kelompok sosio-ekonomi tertentu, bagaimana prinsip keadilan (*Al-'Adl*) harus diterapkan?

5. **Trade-off:** Jika Anda harus memilih antara model yang sangat akurat tapi sulit dijelaskan (Random Forest 500 pohon) versus model yang kurang akurat tapi mudah dipahami (Decision Tree sederhana), mana yang Anda pilih untuk keputusan kredit? Jelaskan alasannya.

---

## Referensi

### Buku Teks

1. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer. -- Chapter 8: Tree-Based Methods.
2. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media. -- Chapter 6-7.
3. Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5-32.

### Sumber Online

4. [scikit-learn: Decision Trees](https://scikit-learn.org/stable/modules/tree.html) -- Dokumentasi resmi Decision Tree.
5. [scikit-learn: Ensemble Methods](https://scikit-learn.org/stable/modules/ensemble.html) -- Dokumentasi Random Forest dan ensemble lainnya.
6. [Visual Introduction to Decision Trees](https://www.r2d3.us/visual-intro-to-machine-learning-part-1/) -- Visualisasi interaktif yang sangat baik.

### Referensi Konteks Indonesia

7. Otoritas Jasa Keuangan (OJK). Peraturan tentang Manajemen Risiko Kredit dan Credit Scoring.
8. Bank Indonesia. Laporan Stabilitas Sistem Keuangan.

---

> **Preview Minggu Depan:** Kita akan membahas **Support Vector Machine (SVM) dan K-Nearest Neighbors (KNN)** -- dua algoritma supervised learning yang kuat untuk klasifikasi, termasuk konsep hyperplane, kernel trick, distance metrics, dan cross-validation.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
