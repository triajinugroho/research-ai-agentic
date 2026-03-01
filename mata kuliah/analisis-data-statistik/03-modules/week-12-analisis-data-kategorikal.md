# Minggu 12: Analisis Data Kategorikal

## Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

**Semester:** Genap 2025/2026
**CPMK:** CPMK-6 — Menganalisis data menggunakan ANOVA, uji non-parametrik, dan analisis data kategorikal sesuai karakteristik data
**Sub-CPMK:** 12.1 (Chi-square dan contingency table), 12.2 (Logistic regression)
**Bloom's Taxonomy:** C4 (Analyze)
**Durasi:** 100 menit (50 menit teori + 50 menit praktikum)

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Membedakan** data kategorikal dan numerik serta memilih teknik analisis yang sesuai (Sub-CPMK 12.1)
2. **Membuat dan membaca** contingency table (tabel kontingensi) untuk data kategorikal (Sub-CPMK 12.1)
3. **Melaksanakan** chi-square test of independence dan menginterpretasi hasilnya (Sub-CPMK 12.1)
4. **Menghitung dan menginterpretasi** odds ratio dan relative risk (Sub-CPMK 12.1)
5. **Menjelaskan** konsep logistic regression dan fungsi sigmoid (Sub-CPMK 12.2)
6. **Membangun** model logistic regression sederhana dan menginterpretasi odds ratio dari koefisien (Sub-CPMK 12.2)
7. **Memutuskan** kapan menggunakan chi-square test vs logistic regression (Sub-CPMK 12.1-12.2)

---

## Materi

### 12.1 Data Kategorikal: Review dan Pengantar

#### 12.1.1 Mengapa Data Kategorikal Butuh Teknik Khusus?

Sepanjang Minggu 9-11, kita menganalisis variabel **numerik** (pengeluaran, harga rumah, IPM). Sekarang kita beralih ke variabel **kategorikal** — yaitu variabel yang nilainya berupa kategori atau label, bukan angka kontinu.

**Contoh variabel kategorikal:**
- Gender (Laki-laki / Perempuan)
- Platform e-learning yang disukai (Google Classroom / Moodle / Edmodo)
- Status kelulusan (Lulus / Tidak Lulus)
- Tingkat kepuasan (Sangat Puas / Puas / Tidak Puas)

**Mengapa teknik berbeda?** Kita tidak bisa menghitung "rata-rata" dari kategori. Tidak masuk akal mengatakan "rata-rata gender mahasiswa adalah 1.47." Untuk data kategorikal, kita bekerja dengan **frekuensi** dan **proporsi**.

| Jenis Data | Contoh | Teknik Analisis |
|-----------|--------|----------------|
| Numerik vs Numerik | IPM vs Pendapatan | Korelasi, Regresi (Minggu 9-10) |
| Numerik vs Kategorikal | Pengeluaran per Wilayah | ANOVA, Kruskal-Wallis (Minggu 11) |
| **Kategorikal vs Kategorikal** | **Platform vs Gender** | **Chi-square (Minggu 12)** |
| **Kategorikal (outcome) vs Numerik/Kategorikal** | **Lulus vs IPK** | **Logistic Regression (Minggu 12)** |

---

### 12.2 Chi-Square Test of Independence

#### 12.2.1 Konsep Dasar

Chi-square test of independence menguji apakah dua variabel kategorikal **berhubungan** (dependen) atau **tidak berhubungan** (independen).

**Contoh pertanyaan:**
- Apakah preferensi platform e-learning berbeda antara mahasiswa laki-laki dan perempuan?
- Apakah ada hubungan antara jenis kelamin dan pilihan program studi?

**Hipotesis:**
- **H₀:** Kedua variabel independen (tidak berhubungan)
- **H₁:** Kedua variabel dependen (ada hubungan)

#### 12.2.2 Contingency Table (Tabel Kontingensi)

Langkah pertama adalah menyusun data ke dalam **contingency table** — tabel silang yang menunjukkan frekuensi kombinasi dua variabel kategorikal.

**Contoh:** Survei preferensi platform e-learning berdasarkan gender

|  | Google Classroom | Moodle | Edmodo | **Total** |
|--|:---:|:---:|:---:|:---:|
| **Laki-laki** | 35 | 20 | 15 | **70** |
| **Perempuan** | 25 | 30 | 25 | **80** |
| **Total** | **60** | **50** | **40** | **150** |

Dari tabel ini, kita bisa bertanya: apakah distribusi preferensi platform berbeda antara laki-laki dan perempuan?

#### 12.2.3 Expected Frequencies (Frekuensi Harapan)

Jika kedua variabel **benar-benar independen**, berapa frekuensi yang kita *harapkan* di setiap sel?

```
Expected frequency (Eᵢⱼ) = (Row total x Column total) / Grand total
```

**Contoh:** Expected frequency laki-laki yang memilih Google Classroom:

```
E = (70 x 60) / 150 = 28
```

Jika frekuensi **observasi** sangat berbeda dari frekuensi **harapan**, maka ada indikasi hubungan antar variabel.

#### 12.2.4 Formula Chi-Square

```
chi-square = Sigma [(Oij - Eij)^2 / Eij]
```

Di mana:
- **Oij** = frekuensi observasi di sel (i, j)
- **Eij** = frekuensi harapan di sel (i, j)
- Penjumlahan dilakukan untuk **semua sel** dalam tabel

**Derajat kebebasan (df):**
```
df = (jumlah baris - 1) x (jumlah kolom - 1)
```

Untuk tabel 2x3: df = (2-1)(3-1) = 2

**Keputusan:** Bandingkan p-value dengan alpha (biasanya 0.05):
- p-value < alpha: Tolak H₀ -- Ada hubungan
- p-value >= alpha: Gagal tolak H₀ -- Tidak cukup bukti

**Syarat chi-square test:**
- Setiap expected frequency >= 5 (aturan umum)
- Jika ada sel dengan expected < 5, pertimbangkan menggabungkan kategori atau gunakan Fisher's exact test

---

### 12.3 Odds Ratio dan Relative Risk

#### 12.3.1 Odds Ratio (OR)

**Odds** adalah rasio probabilitas suatu kejadian terjadi versus tidak terjadi:

```
Odds = P(event) / P(not event) = P(event) / (1 - P(event))
```

**Odds Ratio (OR)** membandingkan odds antara dua kelompok:

```
            Odds kelompok 1
OR = ─────────────────────────
            Odds kelompok 2
```

**Interpretasi OR:**

| Nilai OR | Interpretasi |
|----------|-------------|
| OR = 1 | Tidak ada perbedaan (odds sama di kedua kelompok) |
| OR > 1 | Kelompok 1 memiliki odds lebih tinggi |
| OR < 1 | Kelompok 1 memiliki odds lebih rendah |

**Contoh:** Jika OR = 2.5 untuk "mahasiswa laki-laki memilih Google Classroom vs Moodle, dibandingkan perempuan":
- "Odds mahasiswa laki-laki memilih Google Classroom (vs Moodle) adalah **2.5 kali** odds mahasiswa perempuan."

#### 12.3.2 Relative Risk (RR)

Relative Risk (risiko relatif) membandingkan **probabilitas** (bukan odds) antara dua kelompok:

```
            P(event | kelompok 1)
RR = ─────────────────────────────
            P(event | kelompok 2)
```

**Perbedaan OR dan RR:**

| Aspek | Odds Ratio | Relative Risk |
|-------|-----------|---------------|
| Mengukur | Rasio odds | Rasio probabilitas |
| Kapan digunakan | Case-control studies, logistic regression | Cohort studies, RCT |
| Selalu mendekati | RR jika event langka | RR (tapi berbeda jika event umum) |
| Lebih intuitif? | Kurang | Lebih |

> **Catatan:** Untuk mahasiswa semester 2, OR lebih penting karena akan digunakan dalam logistic regression.

---

### 12.4 Pengantar Logistic Regression

#### 12.4.1 Dari Linear ke Logistic

Pada Minggu 9-10, kita mempelajari **linear regression** untuk variabel dependen numerik (kontinu). Bagaimana jika variabel dependen kita **biner** (ya/tidak, lulus/gagal, klik/tidak klik)?

**Masalah linear regression untuk outcome biner:**
- Prediksi bisa < 0 atau > 1 (tidak masuk akal untuk probabilitas)
- Asumsi residual normal dilanggar
- Hubungannya biasanya non-linear

**Solusi: Logistic Regression** — menggunakan fungsi **sigmoid** untuk memastikan output selalu antara 0 dan 1.

#### 12.4.2 Fungsi Sigmoid

```
              1
P(Y=1) = ─────────────
          1 + e^(-z)

di mana z = b0 + b1*x1 + b2*x2 + ...
```

Fungsi sigmoid mengubah nilai z (yang bisa dari negatif tak hingga sampai positif tak hingga) menjadi probabilitas (antara 0 dan 1).

**Sifat sigmoid:**
- z = 0 maka P = 0.5 (titik tengah)
- z sangat besar (positif) maka P mendekati 1
- z sangat kecil (negatif) maka P mendekati 0
- Kurva berbentuk S (itulah mengapa disebut sigmoid)

#### 12.4.3 Interpretasi Koefisien: Odds Ratio

Dalam logistic regression, koefisien **tidak** diinterpretasi langsung seperti linear regression. Kita menggunakan **odds ratio** dari koefisien:

```
OR = e^(bi)
```

**Interpretasi:** "Setiap kenaikan 1 unit xi, **odds** dari Y=1 berubah sebesar faktor e^(bi), ceteris paribus."

**Contoh:** Jika b1 = 0.8 untuk variabel "jam belajar" dalam model prediksi kelulusan:
- OR = e^(0.8) = 2.23
- "Setiap tambahan 1 jam belajar, odds kelulusan meningkat **2.23 kali lipat**."

#### 12.4.4 Kapan Chi-Square vs Logistic Regression?

| Aspek | Chi-Square Test | Logistic Regression |
|-------|----------------|-------------------|
| **Tujuan** | Menguji hubungan 2 variabel kategorikal | Memprediksi outcome biner dari satu/banyak prediktor |
| **Variabel** | Kedua variabel kategorikal | Dependen biner, independen bisa numerik/kategorikal |
| **Output** | p-value (ada/tidak hubungan) | Koefisien, odds ratio, prediksi probabilitas |
| **Kekuatan** | Sederhana, cepat | Bisa mengontrol banyak variabel, prediktif |
| **Kelemahan** | Tidak bisa mengontrol confounders | Lebih kompleks, butuh sampel lebih besar |
| **Kapan pakai** | Analisis eksplorasi awal | Analisis mendalam, prediksi |

**Aturan praktis:**
- Ingin tahu "apakah ada hubungan?" maka gunakan Chi-square
- Ingin "memprediksi" atau "mengontrol variabel lain" maka gunakan Logistic regression
- Idealnya, gunakan keduanya: chi-square untuk eksplorasi, logistic regression untuk pemodelan

---

## Contoh Kode Python

### Persiapan Data: Survei Preferensi Platform E-Learning

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Simulasi data survei mahasiswa
np.random.seed(2025)
n = 200

# Generate data survei
gender = np.random.choice(['Laki-laki', 'Perempuan'], n, p=[0.45, 0.55])

# Preferensi platform (beri sedikit hubungan dengan gender)
platform = []
for g in gender:
    if g == 'Laki-laki':
        p = np.random.choice(
            ['Google Classroom', 'Moodle', 'Edmodo'],
            p=[0.50, 0.25, 0.25]
        )
    else:
        p = np.random.choice(
            ['Google Classroom', 'Moodle', 'Edmodo'],
            p=[0.30, 0.40, 0.30]
        )
    platform.append(p)

# Variabel tambahan untuk logistic regression
ipk = np.random.normal(3.2, 0.4, n).clip(2.0, 4.0).round(2)
jam_belajar = np.random.uniform(1, 8, n).round(1)

# Outcome biner: kepuasan tinggi (1) vs rendah (0)
z = -3 + 1.2 * ipk + 0.3 * jam_belajar + np.random.normal(0, 0.5, n)
prob_puas = 1 / (1 + np.exp(-z))
puas = (np.random.random(n) < prob_puas).astype(int)

survei = pd.DataFrame({
    'gender': gender,
    'platform': platform,
    'ipk': ipk,
    'jam_belajar': jam_belajar,
    'puas': puas  # 1 = puas, 0 = tidak puas
})

print("=== Preview Data Survei ===")
print(survei.head(10))
print(f"\nDistribusi Gender: \n{survei['gender'].value_counts()}")
print(f"\nDistribusi Platform: \n{survei['platform'].value_counts()}")
print(f"\nDistribusi Kepuasan: \n{survei['puas'].value_counts()}")
```

### Membuat Contingency Table

```python
# ============================================================
# CONTINGENCY TABLE: Gender vs Platform
# ============================================================

# Membuat tabel kontingensi
ct = pd.crosstab(survei['gender'], survei['platform'], margins=True)
print("=== Contingency Table: Gender vs Platform ===")
print(ct)

# Tabel proporsi (persentase per baris)
ct_pct = pd.crosstab(survei['gender'], survei['platform'], normalize='index')
print(f"\n=== Proporsi per Gender ===")
print(ct_pct.round(3))

# Visualisasi
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Stacked bar chart
ct_pct.plot(kind='bar', stacked=True, ax=axes[0], colormap='Set2',
            edgecolor='white')
axes[0].set_xlabel('Gender', fontsize=11)
axes[0].set_ylabel('Proporsi', fontsize=11)
axes[0].set_title('Proporsi Preferensi Platform per Gender', fontsize=13)
axes[0].legend(title='Platform', bbox_to_anchor=(1.02, 1))
axes[0].tick_params(axis='x', rotation=0)
axes[0].grid(True, alpha=0.3, axis='y')

# Grouped bar chart
ct_no_margins = pd.crosstab(survei['gender'], survei['platform'])
ct_no_margins.plot(kind='bar', ax=axes[1], colormap='Set2', edgecolor='white')
axes[1].set_xlabel('Gender', fontsize=11)
axes[1].set_ylabel('Frekuensi', fontsize=11)
axes[1].set_title('Frekuensi Preferensi Platform per Gender', fontsize=13)
axes[1].legend(title='Platform')
axes[1].tick_params(axis='x', rotation=0)
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()
```

### Chi-Square Test of Independence

```python
# ============================================================
# CHI-SQUARE TEST OF INDEPENDENCE
# ============================================================

# Membuat contingency table (tanpa margins)
ct_chi = pd.crosstab(survei['gender'], survei['platform'])

# Chi-square test
chi2, p_value, dof, expected = stats.chi2_contingency(ct_chi)

print("=== Chi-Square Test of Independence ===")
print(f"Chi-square statistic: {chi2:.4f}")
print(f"Degrees of freedom (df): {dof}")
print(f"P-value: {p_value:.6f}")

print(f"\n=== Expected Frequencies (jika H0 benar) ===")
expected_df = pd.DataFrame(
    expected,
    index=ct_chi.index,
    columns=ct_chi.columns
)
print(expected_df.round(1))

# Cek syarat: semua expected >= 5?
print(f"\nSemua expected >= 5? {'Ya' if expected.min() >= 5 else 'TIDAK - syarat tidak terpenuhi!'}")

# Perbandingan observed vs expected
print(f"\n=== Observed vs Expected ===")
for gender in ct_chi.index:
    for plat in ct_chi.columns:
        obs = ct_chi.loc[gender, plat]
        exp = expected_df.loc[gender, plat]
        print(f"  {gender} - {plat}: Observed = {obs}, Expected = {exp:.1f}, "
              f"Diff = {obs - exp:.1f}")

# Keputusan
print(f"\n=== Keputusan (alpha = 0.05) ===")
if p_value < 0.05:
    print(f"p-value ({p_value:.6f}) < 0.05 -> TOLAK H0")
    print("Kesimpulan: Ada hubungan signifikan antara gender dan preferensi platform.")
else:
    print(f"p-value ({p_value:.6f}) >= 0.05 -> GAGAL TOLAK H0")
    print("Kesimpulan: Tidak cukup bukti adanya hubungan antara gender dan preferensi platform.")
```

### Menghitung Odds Ratio

```python
# ============================================================
# ODDS RATIO: Contoh 2x2
# ============================================================

# Sederhanakan: Google Classroom vs Lainnya, antara Laki-laki vs Perempuan
survei['gc'] = (survei['platform'] == 'Google Classroom').astype(int)

# Tabel 2x2
ct_2x2 = pd.crosstab(survei['gender'], survei['gc'])
ct_2x2.columns = ['Bukan GC', 'Google Classroom']
print("=== Tabel 2x2: Gender vs Google Classroom ===")
print(ct_2x2)

# Hitung Odds Ratio manual
a = ct_2x2.loc['Laki-laki', 'Google Classroom']
b = ct_2x2.loc['Laki-laki', 'Bukan GC']
c = ct_2x2.loc['Perempuan', 'Google Classroom']
d = ct_2x2.loc['Perempuan', 'Bukan GC']

odds_laki = a / b
odds_perempuan = c / d
odds_ratio = odds_laki / odds_perempuan

print(f"\nOdds laki-laki memilih GC: {a}/{b} = {odds_laki:.3f}")
print(f"Odds perempuan memilih GC: {c}/{d} = {odds_perempuan:.3f}")
print(f"Odds Ratio: {odds_ratio:.3f}")

if odds_ratio > 1:
    print(f"\nInterpretasi: Laki-laki {odds_ratio:.1f}x lebih mungkin (dalam hal odds) "
          f"memilih Google Classroom dibandingkan perempuan.")
elif odds_ratio < 1:
    print(f"\nInterpretasi: Laki-laki {1/odds_ratio:.1f}x kurang mungkin (dalam hal odds) "
          f"memilih Google Classroom dibandingkan perempuan.")
else:
    print(f"\nInterpretasi: Tidak ada perbedaan odds antara kedua gender.")

# Relative Risk
rr = (a / (a + b)) / (c / (c + d))
print(f"\nRelative Risk: {rr:.3f}")
```

### Logistic Regression

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# ============================================================
# LOGISTIC REGRESSION: Prediksi Kepuasan Mahasiswa
# ============================================================

# Variabel: IPK dan Jam Belajar -> Kepuasan (0/1)
X = survei[['ipk', 'jam_belajar']]
y = survei['puas']

# Fit model
log_model = LogisticRegression(random_state=42)
log_model.fit(X, y)

print("=== Logistic Regression (sklearn) ===")
print(f"Intercept: {log_model.intercept_[0]:.4f}")
print(f"Koefisien:")
for nama, koef in zip(X.columns, log_model.coef_[0]):
    or_val = np.exp(koef)
    print(f"  {nama}: beta = {koef:.4f}, OR = e^beta = {or_val:.4f}")

print(f"\n=== Interpretasi Odds Ratio ===")
or_ipk = np.exp(log_model.coef_[0][0])
or_jam = np.exp(log_model.coef_[0][1])
print(f"IPK: OR = {or_ipk:.2f}")
print(f"  -> Setiap kenaikan 1 poin IPK, odds kepuasan meningkat {or_ipk:.2f} kali lipat.")
print(f"Jam Belajar: OR = {or_jam:.2f}")
print(f"  -> Setiap tambahan 1 jam belajar, odds kepuasan meningkat {or_jam:.2f} kali lipat.")

# Akurasi prediksi
y_pred = log_model.predict(X)
print(f"\n=== Evaluasi Model ===")
print(f"Akurasi: {log_model.score(X, y):.4f}")
print(f"\nConfusion Matrix:")
print(confusion_matrix(y, y_pred))
```

### Logistic Regression dengan statsmodels (Output Lengkap)

```python
import statsmodels.api as sm

# statsmodels untuk output lengkap
X_sm = sm.add_constant(survei[['ipk', 'jam_belajar']])
y_sm = survei['puas']

logit_model = sm.Logit(y_sm, X_sm).fit()
print(logit_model.summary())

# Odds ratio dengan confidence interval
print("\n=== Odds Ratio dengan 95% CI ===")
params = logit_model.params
conf = logit_model.conf_int()
odds_ratios = pd.DataFrame({
    'OR': np.exp(params),
    'CI Lower': np.exp(conf[0]),
    'CI Upper': np.exp(conf[1]),
    'p-value': logit_model.pvalues
})
print(odds_ratios.round(4))
```

### Visualisasi Fungsi Sigmoid

```python
# Visualisasi fungsi sigmoid dan decision boundary
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Fungsi sigmoid
z_range = np.linspace(-6, 6, 200)
sigmoid = 1 / (1 + np.exp(-z_range))

axes[0].plot(z_range, sigmoid, 'b-', linewidth=2)
axes[0].axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label='P = 0.5')
axes[0].axvline(x=0, color='gray', linestyle='--', alpha=0.3)
axes[0].set_xlabel('z = b0 + b1*x1 + b2*x2 + ...', fontsize=11)
axes[0].set_ylabel('P(Y = 1)', fontsize=11)
axes[0].set_title('Fungsi Sigmoid\n(Logistic Function)', fontsize=13)
axes[0].legend(fontsize=10)
axes[0].grid(True, alpha=0.3)
axes[0].set_ylim(-0.05, 1.05)

# Plot 2: Scatter plot IPK vs Kepuasan + probability curve
ipk_sorted = np.sort(survei['ipk'].values)
# Prediksi probabilitas untuk berbagai IPK (jam belajar = rata-rata)
ipk_pred = np.column_stack([
    ipk_sorted,
    np.full(len(ipk_sorted), survei['jam_belajar'].mean())
])
prob_pred = log_model.predict_proba(ipk_pred)[:, 1]

axes[1].scatter(survei['ipk'], survei['puas'], alpha=0.3, color='steelblue',
                label='Data observasi')
axes[1].plot(ipk_sorted, prob_pred, 'r-', linewidth=2,
             label='P(Puas) predicted')
axes[1].axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
axes[1].set_xlabel('IPK', fontsize=11)
axes[1].set_ylabel('Kepuasan (0/1) atau P(Puas)', fontsize=11)
axes[1].set_title('Logistic Regression: IPK vs Kepuasan\n(jam_belajar = rata-rata)',
                  fontsize=13)
axes[1].legend(fontsize=10)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## Studi Kasus: Analisis Survei Preferensi Platform E-Learning Mahasiswa

### Konteks

Sebuah universitas ingin mengevaluasi platform e-learning yang digunakan. Survei dilakukan terhadap 200 mahasiswa untuk mengetahui: (1) Apakah preferensi platform berbeda berdasarkan gender? (2) Faktor apa yang mempengaruhi kepuasan mahasiswa terhadap e-learning?

### Analisis Lengkap

```python
# ============================================================
# STUDI KASUS LENGKAP: Survei Platform E-Learning
# ============================================================

print("=" * 60)
print("STUDI KASUS: Preferensi Platform E-Learning Mahasiswa")
print("=" * 60)

# BAGIAN A: Chi-Square -- Gender vs Platform
print("\n" + "-" * 60)
print("BAGIAN A: Hubungan Gender dan Preferensi Platform")
print("-" * 60)

# A1. Deskriptif
print("\n1. Tabel Kontingensi:")
ct = pd.crosstab(survei['gender'], survei['platform'], margins=True)
print(ct)

ct_pct = pd.crosstab(survei['gender'], survei['platform'], normalize='index')
print(f"\n   Proporsi per Gender:")
print(ct_pct.round(3))

# A2. Chi-square test
chi2, p, dof, exp = stats.chi2_contingency(
    pd.crosstab(survei['gender'], survei['platform'])
)
print(f"\n2. Chi-Square Test:")
print(f"   chi2 = {chi2:.4f}, df = {dof}, p = {p:.6f}")
if p < 0.05:
    print(f"   Keputusan: Tolak H0 -- ada hubungan signifikan")
else:
    print(f"   Keputusan: Gagal tolak H0 -- tidak ada hubungan signifikan")

# BAGIAN B: Logistic Regression -- Prediksi Kepuasan
print("\n" + "-" * 60)
print("BAGIAN B: Faktor yang Mempengaruhi Kepuasan E-Learning")
print("-" * 60)

# B1. Deskriptif
print(f"\n1. Distribusi kepuasan:")
print(f"   Puas (1): {survei['puas'].sum()} ({survei['puas'].mean()*100:.1f}%)")
print(f"   Tidak Puas (0): {(1-survei['puas']).sum()} ({(1-survei['puas'].mean())*100:.1f}%)")

# B2. Logistic regression
X_case = sm.add_constant(survei[['ipk', 'jam_belajar']])
logit_case = sm.Logit(survei['puas'], X_case).fit(disp=0)

print(f"\n2. Model Logistic Regression:")
print(f"   Log-Likelihood: {logit_case.llf:.2f}")
print(f"   Pseudo R-squared: {logit_case.prsquared:.4f}")

print(f"\n3. Koefisien dan Odds Ratio:")
print(f"   {'Variabel':<15} {'beta':<10} {'OR':<10} {'p-value':<10} {'Signifikan?'}")
print(f"   {'-'*55}")
for var in ['const', 'ipk', 'jam_belajar']:
    beta = logit_case.params[var]
    or_val = np.exp(beta)
    pval = logit_case.pvalues[var]
    sig = "Ya ***" if pval < 0.001 else "Ya **" if pval < 0.01 else "Ya *" if pval < 0.05 else "Tidak"
    print(f"   {var:<15} {beta:<10.4f} {or_val:<10.4f} {pval:<10.4f} {sig}")

# B3. Prediksi contoh
print(f"\n4. Prediksi Contoh:")
contoh = pd.DataFrame({
    'const': [1, 1, 1],
    'ipk': [2.5, 3.0, 3.7],
    'jam_belajar': [3.0, 5.0, 6.0]
})
for i, row in contoh.iterrows():
    prob = logit_case.predict(row)[0]
    label = 'Kemungkinan Puas' if prob > 0.5 else 'Kemungkinan Tidak Puas'
    print(f"   IPK {row['ipk']}, Belajar {row['jam_belajar']} jam "
          f"-> P(Puas) = {prob:.3f} ({label})")

# Kesimpulan
print(f"\n{'='*60}")
print("KESIMPULAN:")
print(f"{'='*60}")
print("1. Analisis chi-square menunjukkan bahwa preferensi platform e-learning")
if p < 0.05:
    print(f"   berhubungan dengan gender mahasiswa (p = {p:.4f}).")
else:
    print(f"   tidak berhubungan dengan gender mahasiswa (p = {p:.4f}).")
print("2. Logistic regression menunjukkan bahwa IPK dan jam belajar berpengaruh")
print("   terhadap kepuasan mahasiswa. Mahasiswa dengan IPK lebih tinggi dan")
print("   jam belajar lebih banyak cenderung lebih puas terhadap e-learning.")
```

### Diskusi Studi Kasus

1. **Chi-square vs logistic regression:** Chi-square cocok untuk menjawab "apakah ada hubungan," sementara logistic regression bisa memprediksi dan mengontrol variabel lain.
2. **Limitasi survei:** Self-reported data bisa memiliki bias (social desirability, recall bias). Jumlah sampel mungkin kurang besar untuk mendeteksi efek kecil.
3. **Implikasi praktis:** Jika ada perbedaan preferensi platform berdasarkan gender, universitas bisa menyediakan beberapa opsi platform atau menyesuaikan antarmuka.
4. **Langkah selanjutnya:** Tambahkan variabel lain (semester, program studi, koneksi internet) untuk model yang lebih komprehensif.

---

## AI Corner: AI untuk Analisis Data Kategorikal

### Prompt yang Efektif

> "Saya punya data survei dengan 200 responden. Variabel: gender (L/P), platform e-learning (3 pilihan), kepuasan (ya/tidak). Tolong bantu saya: (1) buat contingency table, (2) lakukan chi-square test, (3) interpretasikan hasilnya dalam konteks pendidikan."

> "Jelaskan fungsi sigmoid dalam logistic regression menggunakan analogi yang mudah dipahami untuk mahasiswa informatika semester 2."

### Kapan AI Membantu

- Menjelaskan perbedaan odds ratio vs relative risk dengan contoh nyata
- Membantu membaca dan menginterpretasi output statsmodels logistic regression
- Menyarankan cara memvisualisasikan data kategorikal
- Memeriksa apakah syarat chi-square terpenuhi

### Kapan Harus Kritis terhadap AI

- AI mungkin tidak mengingatkan bahwa expected frequency harus >= 5 untuk chi-square
- AI terkadang bingung antara odds dan probabilitas — pastikan interpretasi tepat
- AI mungkin mengabaikan konteks Indonesia (misalnya: pola penggunaan e-learning di kampus Indonesia berbeda dari kampus Barat)
- Selalu verifikasi perhitungan odds ratio secara manual

### Contoh Evaluasi Output AI

Jika AI mengatakan: *"OR = 2.5 berarti laki-laki 2.5 kali lebih mungkin memilih Google Classroom"* — ini **kurang tepat**. Yang benar: "**Odds** laki-laki memilih Google Classroom adalah 2.5 kali odds perempuan." Odds bukan probabilitas!

---

## Latihan Mandiri

### Latihan 1: Contingency Table dan Chi-Square (20 menit)

Sebuah survei terhadap 300 mahasiswa mencatat program studi dan metode belajar utama:

| | Buku Teks | Video Online | Diskusi Kelompok |
|--|:-:|:-:|:-:|
| **Informatika** | 30 | 50 | 20 |
| **Sistem Informasi** | 25 | 35 | 40 |
| **Teknik Komputer** | 40 | 25 | 35 |

a. Hitung expected frequencies untuk setiap sel
b. Lakukan chi-square test menggunakan `scipy.stats.chi2_contingency`
c. Apakah ada hubungan signifikan antara prodi dan metode belajar?
d. Visualisasikan data dengan stacked bar chart

### Latihan 2: Odds Ratio (15 menit)

Dari data berikut tentang penggunaan AI tool dan kelulusan:

| | Lulus | Tidak Lulus |
|--|:-:|:-:|
| **Menggunakan AI** | 80 | 20 |
| **Tidak Menggunakan AI** | 60 | 40 |

a. Hitung odds kelulusan untuk kelompok yang menggunakan AI
b. Hitung odds kelulusan untuk kelompok yang tidak menggunakan AI
c. Hitung Odds Ratio
d. Interpretasikan OR dalam konteks studi ini
e. Hitung juga Relative Risk dan bandingkan dengan OR

### Latihan 3: Logistic Regression (20 menit)

Gunakan data survei atau buat data simulasi dengan:
- Variabel dependen: lulus (1) / tidak lulus (0)
- Variabel independen: IPK, jam_belajar, kehadiran (%)

a. Fit model logistic regression menggunakan sklearn dan statsmodels
b. Hitung odds ratio untuk setiap prediktor
c. Interpretasikan: variabel mana yang paling berpengaruh?
d. Prediksi probabilitas kelulusan untuk mahasiswa dengan IPK 3.5, belajar 5 jam, kehadiran 90%

### Latihan 4: Perbandingan Metode (15 menit)

Untuk data Latihan 1:

a. Lakukan chi-square test (sudah dilakukan di Latihan 1)
b. Ubah menjadi masalah logistic regression: prediksi apakah mahasiswa memilih "Video Online" (1) atau tidak (0) berdasarkan prodi
c. Bandingkan kesimpulan kedua metode
d. Metode mana yang lebih informatif? Mengapa?

### Latihan 5: Studi Kasus Mandiri (20 menit)

Buatlah skenario survei sederhana yang relevan dengan kehidupan mahasiswa (misalnya: penggunaan transportasi online vs konvensional berdasarkan domisili). Lakukan:

1. Buat atau simulasikan data
2. Contingency table + visualisasi
3. Chi-square test
4. Jika relevan, logistic regression
5. Tulis kesimpulan dalam 3-4 kalimat

---

## Rangkuman

| Konsep | Poin Kunci |
|--------|-----------|
| Data Kategorikal | Variabel berupa label/kategori; dianalisis dengan frekuensi dan proporsi |
| Contingency Table | Tabel silang frekuensi dua variabel kategorikal; langkah pertama analisis |
| Chi-Square Test | Menguji independensi dua variabel kategorikal; syarat: expected >= 5 |
| Expected Frequency | E = (row total x col total) / grand total; digunakan dalam perhitungan chi-square |
| Odds Ratio | Membandingkan odds antar kelompok; OR = 1 berarti tidak ada perbedaan |
| Relative Risk | Membandingkan probabilitas antar kelompok; lebih intuitif dari OR |
| Logistic Regression | Memprediksi outcome biner; menggunakan fungsi sigmoid; koefisien diinterpretasi via OR |
| Fungsi Sigmoid | Mengubah z (linear) menjadi probabilitas (0-1); berbentuk S |
| Chi-square vs Logistic | Chi-square untuk eksplorasi hubungan; logistic untuk prediksi dan kontrol variabel |

---

## Referensi

1. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics* (4th ed.), Chapter 6: Inference for Categorical Data.
2. Agresti, A. (2018). *An Introduction to Categorical Data Analysis* (3rd ed.), Chapters 1-3.
3. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning (ISLP)*, Chapter 4: Classification (Logistic Regression).
4. scipy.stats Documentation: [chi2_contingency](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)
5. scikit-learn Documentation: [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
6. statsmodels Documentation: [Logit](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.Logit.html)

---

*Modul ini adalah bagian dari mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia. Semester Genap 2025/2026.*
