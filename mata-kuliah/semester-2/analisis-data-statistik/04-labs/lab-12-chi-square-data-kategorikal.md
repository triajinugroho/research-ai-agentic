# Lab 12: Chi-Square dan Data Kategorikal

**Mata Kuliah:** Statistika — Universitas Al Azhar Indonesia
**Minggu:** 12
**Platform:** Google Colab (Python)

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. Membuat tabel kontingensi (*contingency table*) menggunakan `pd.crosstab`
2. Melaksanakan uji Chi-Square dengan `scipy.stats.chi2_contingency`
3. Memvisualisasikan data kategorikal (stacked bar chart, mosaic plot)
4. Membangun model logistic regression sederhana dengan `sklearn`
5. Menginterpretasikan odds ratio dalam konteks data survei

---

## Persiapan

### Library yang Dibutuhkan

```python
# Jalankan cell ini terlebih dahulu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Pengaturan
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("Semua library berhasil dimuat!")
```

### Konsep Singkat

**Uji Chi-Square** digunakan untuk menganalisis hubungan antara dua variabel kategorikal.

- **Chi-Square Test of Independence**: Menguji apakah dua variabel kategorikal saling independen
- **H₀**: Tidak ada hubungan antara kedua variabel (independen)
- **H₁**: Terdapat hubungan antara kedua variabel (dependen)

$$\chi^2 = \sum \frac{(O - E)^2}{E}$$

Di mana O = frekuensi observasi, E = frekuensi ekspektasi.

---

## Langkah-langkah Praktikum

### Langkah 1: Membuat Dataset Survei

```python
# Studi kasus: Survei kepuasan mahasiswa UAI terhadap layanan kampus
np.random.seed(2024)
n = 300

# Variabel kategorikal
fakultas = np.random.choice(
    ['Teknik', 'Ekonomi', 'Hukum', 'FKIP', 'Sains'],
    size=n,
    p=[0.25, 0.25, 0.20, 0.15, 0.15]
)

# Kepuasan dipengaruhi oleh fakultas (simulasi hubungan)
kepuasan = []
for f in fakultas:
    if f == 'Teknik':
        k = np.random.choice(['Puas', 'Netral', 'Tidak Puas'], p=[0.5, 0.3, 0.2])
    elif f == 'Ekonomi':
        k = np.random.choice(['Puas', 'Netral', 'Tidak Puas'], p=[0.6, 0.25, 0.15])
    elif f == 'Hukum':
        k = np.random.choice(['Puas', 'Netral', 'Tidak Puas'], p=[0.35, 0.35, 0.3])
    elif f == 'FKIP':
        k = np.random.choice(['Puas', 'Netral', 'Tidak Puas'], p=[0.45, 0.30, 0.25])
    else:
        k = np.random.choice(['Puas', 'Netral', 'Tidak Puas'], p=[0.55, 0.25, 0.20])
    kepuasan.append(k)

# Variabel tambahan
gender = np.random.choice(['Laki-laki', 'Perempuan'], size=n, p=[0.45, 0.55])
semester = np.random.choice([2, 4, 6, 8], size=n, p=[0.3, 0.3, 0.25, 0.15])
ipk_kategori = np.random.choice(
    ['< 2.5', '2.5-3.0', '3.0-3.5', '> 3.5'],
    size=n, p=[0.10, 0.25, 0.40, 0.25]
)

data = pd.DataFrame({
    'fakultas': fakultas,
    'kepuasan': kepuasan,
    'gender': gender,
    'semester': semester,
    'ipk_kategori': ipk_kategori
})

print("=== Dataset Survei Kepuasan Mahasiswa ===")
print(f"Jumlah responden: {len(data)}")
print()
print("Distribusi variabel:")
for col in data.columns:
    print(f"\n  {col}:")
    print(f"  {data[col].value_counts().to_dict()}")
```

### Langkah 2: Membuat Tabel Kontingensi

```python
# Tabel kontingensi: Fakultas vs Kepuasan
tabel_kontingensi = pd.crosstab(
    data['fakultas'],
    data['kepuasan'],
    margins=True,
    margins_name='Total'
)

print("=== Tabel Kontingensi: Fakultas vs Kepuasan ===")
print(tabel_kontingensi)
```

```python
# Tabel kontingensi dengan persentase baris
tabel_persen = pd.crosstab(
    data['fakultas'],
    data['kepuasan'],
    normalize='index'  # persentase per baris
) * 100

print("=== Tabel Persentase (per baris) ===")
print(tabel_persen.round(1))
```

```python
# Tabel kontingensi: Gender vs Kepuasan
tabel_gender = pd.crosstab(
    data['gender'],
    data['kepuasan'],
    margins=True,
    margins_name='Total'
)

print("\n=== Tabel Kontingensi: Gender vs Kepuasan ===")
print(tabel_gender)
```

### Langkah 3: Uji Chi-Square Test of Independence

```python
# Uji Chi-Square: Fakultas vs Kepuasan
print("=== Uji Chi-Square: Fakultas vs Kepuasan ===")
print("H₀: Tidak ada hubungan antara fakultas dan tingkat kepuasan")
print("H₁: Terdapat hubungan antara fakultas dan tingkat kepuasan")
print()

# Buat tabel tanpa margins
tabel = pd.crosstab(data['fakultas'], data['kepuasan'])
chi2, p_value, dof, expected = stats.chi2_contingency(tabel)

print(f"Chi-Square statistic (χ²) = {chi2:.4f}")
print(f"Degrees of freedom (df)   = {dof}")
print(f"p-value                   = {p_value:.4f}")
print()

if p_value < 0.05:
    print("Kesimpulan: Tolak H₀ (p < 0.05)")
    print("Terdapat hubungan signifikan antara fakultas dan tingkat kepuasan.")
else:
    print("Kesimpulan: Gagal tolak H₀ (p ≥ 0.05)")
    print("Tidak ada hubungan signifikan antara fakultas dan tingkat kepuasan.")
```

```python
# Tampilkan frekuensi ekspektasi (expected frequency)
print("=== Frekuensi Ekspektasi (Expected Frequency) ===")
expected_df = pd.DataFrame(
    expected,
    index=tabel.index,
    columns=tabel.columns
).round(2)
print(expected_df)
print()

# Cek asumsi: semua expected frequency ≥ 5
min_expected = expected.min()
print(f"Frekuensi ekspektasi minimum: {min_expected:.2f}")
if min_expected >= 5:
    print("Asumsi terpenuhi: Semua frekuensi ekspektasi ≥ 5")
else:
    print("PERINGATAN: Ada frekuensi ekspektasi < 5. Pertimbangkan Fisher's Exact Test.")
```

```python
# Effect size: Cramér's V
def cramers_v(chi2, n, min_dim):
    """Menghitung Cramér's V sebagai effect size untuk Chi-Square."""
    return np.sqrt(chi2 / (n * (min_dim - 1)))

n_obs = len(data)
min_dim = min(tabel.shape)
v = cramers_v(chi2, n_obs, min_dim)

print(f"\n=== Effect Size: Cramér's V ===")
print(f"Cramér's V = {v:.4f}")

if v < 0.1:
    print("Interpretasi: Hubungan sangat lemah (negligible)")
elif v < 0.3:
    print("Interpretasi: Hubungan lemah")
elif v < 0.5:
    print("Interpretasi: Hubungan sedang")
else:
    print("Interpretasi: Hubungan kuat")
```

### Langkah 4: Uji Chi-Square untuk Variabel Lain

```python
# Uji Chi-Square: Gender vs Kepuasan
print("=== Uji Chi-Square: Gender vs Kepuasan ===")

tabel_gk = pd.crosstab(data['gender'], data['kepuasan'])
chi2_gk, p_gk, dof_gk, exp_gk = stats.chi2_contingency(tabel_gk)

print(f"χ² = {chi2_gk:.4f}, df = {dof_gk}, p = {p_gk:.4f}")
if p_gk < 0.05:
    print("→ Terdapat hubungan signifikan antara gender dan kepuasan.")
else:
    print("→ Tidak ada hubungan signifikan antara gender dan kepuasan.")
```

```python
# Uji Chi-Square: IPK Kategori vs Kepuasan
print("=== Uji Chi-Square: IPK Kategori vs Kepuasan ===")

tabel_ik = pd.crosstab(data['ipk_kategori'], data['kepuasan'])
chi2_ik, p_ik, dof_ik, exp_ik = stats.chi2_contingency(tabel_ik)

print(f"χ² = {chi2_ik:.4f}, df = {dof_ik}, p = {p_ik:.4f}")
if p_ik < 0.05:
    print("→ Terdapat hubungan signifikan antara kategori IPK dan kepuasan.")
else:
    print("→ Tidak ada hubungan signifikan antara kategori IPK dan kepuasan.")
```

### Langkah 5: Visualisasi Data Kategorikal

```python
# Stacked Bar Chart
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Stacked bar chart (frekuensi)
tabel_persen_plot = pd.crosstab(data['fakultas'], data['kepuasan'], normalize='index') * 100
tabel_persen_plot.plot(kind='bar', stacked=True, ax=axes[0],
                       color=['#e74c3c', '#f39c12', '#27ae60'])
axes[0].set_title('Kepuasan per Fakultas (Stacked Bar)')
axes[0].set_xlabel('Fakultas')
axes[0].set_ylabel('Persentase (%)')
axes[0].legend(title='Kepuasan')
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=45)

# Plot 2: Grouped bar chart
tabel_persen_plot.plot(kind='bar', stacked=False, ax=axes[1],
                       color=['#e74c3c', '#f39c12', '#27ae60'])
axes[1].set_title('Kepuasan per Fakultas (Grouped Bar)')
axes[1].set_xlabel('Fakultas')
axes[1].set_ylabel('Persentase (%)')
axes[1].legend(title='Kepuasan')
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45)

plt.tight_layout()
plt.show()
```

```python
# Heatmap tabel kontingensi
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Heatmap frekuensi
sns.heatmap(tabel, annot=True, fmt='d', cmap='YlOrRd', ax=axes[0])
axes[0].set_title('Tabel Kontingensi (Frekuensi)')

# Heatmap persentase
sns.heatmap(tabel_persen, annot=True, fmt='.1f', cmap='YlOrRd', ax=axes[1])
axes[1].set_title('Tabel Kontingensi (% per Baris)')

plt.tight_layout()
plt.show()
```

```python
# Konsep Mosaic Plot — visualisasi sederhana
# (mosaic plot bisa dibuat dengan statsmodels, tapi kita buat versi sederhana)
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(12, 6))

# Hitung proporsi
props = pd.crosstab(data['fakultas'], data['kepuasan'], normalize='all')
fak_props = data['fakultas'].value_counts(normalize=True).sort_index()

x_start = 0
colors = {'Puas': '#27ae60', 'Netral': '#f39c12', 'Tidak Puas': '#e74c3c'}

for fak in sorted(data['fakultas'].unique()):
    width = fak_props[fak]
    y_start = 0
    for kep in ['Puas', 'Netral', 'Tidak Puas']:
        height = props.loc[fak, kep] / fak_props[fak] if fak_props[fak] > 0 else 0
        rect = Rectangle((x_start, y_start), width, height,
                         facecolor=colors[kep], edgecolor='white', linewidth=2)
        ax.add_patch(rect)
        if height > 0.05:
            ax.text(x_start + width/2, y_start + height/2,
                    f'{height*100:.0f}%', ha='center', va='center',
                    fontsize=9, fontweight='bold')
        y_start += height
    ax.text(x_start + width/2, -0.05, fak, ha='center', va='top',
            fontsize=10, fontweight='bold')
    x_start += width

ax.set_xlim(0, 1)
ax.set_ylim(-0.1, 1.05)
ax.set_ylabel('Proporsi Kepuasan')
ax.set_title('Mosaic Plot: Fakultas vs Kepuasan')

# Legend manual
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=colors[k], label=k) for k in colors]
ax.legend(handles=legend_elements, loc='upper right')

ax.set_xticks([])
plt.tight_layout()
plt.show()
```

### Langkah 6: Pengantar Logistic Regression

```python
# Logistic Regression: Memprediksi kepuasan (Puas vs Tidak Puas)
# Untuk penyederhanaan, kita ubah menjadi binary classification

# Siapkan data
data_lr = data.copy()
data_lr = data_lr[data_lr['kepuasan'] != 'Netral']  # Hapus netral
data_lr['kepuasan_binary'] = (data_lr['kepuasan'] == 'Puas').astype(int)

print(f"Data setelah filter (tanpa Netral): {len(data_lr)} observasi")
print(f"Distribusi target: {data_lr['kepuasan_binary'].value_counts().to_dict()}")
print("  1 = Puas, 0 = Tidak Puas")
```

```python
# Encode variabel kategorikal
le_fakultas = LabelEncoder()
le_gender = LabelEncoder()

data_lr['fakultas_enc'] = le_fakultas.fit_transform(data_lr['fakultas'])
data_lr['gender_enc'] = le_gender.fit_transform(data_lr['gender'])

# Fitur dan target
X_lr = data_lr[['fakultas_enc', 'gender_enc', 'semester']]
y_lr = data_lr['kepuasan_binary']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_lr, y_lr, test_size=0.3, random_state=42
)

print(f"Data latih: {len(X_train)}, Data uji: {len(X_test)}")
```

```python
# Bangun model Logistic Regression
log_model = LogisticRegression(random_state=42)
log_model.fit(X_train, y_train)

# Evaluasi
y_pred_lr = log_model.predict(X_test)
accuracy = log_model.score(X_test, y_test)

print(f"=== Hasil Logistic Regression ===")
print(f"Akurasi: {accuracy:.4f}")
print()
print("Classification Report:")
print(classification_report(y_test, y_pred_lr, target_names=['Tidak Puas', 'Puas']))
```

### Langkah 7: Interpretasi Odds Ratio

```python
# Odds Ratio dari koefisien logistic regression
print("=== Odds Ratio ===")
print()
print("Odds Ratio = exp(koefisien)")
print("- OR > 1: meningkatkan kemungkinan 'Puas'")
print("- OR < 1: menurunkan kemungkinan 'Puas'")
print("- OR = 1: tidak ada pengaruh")
print()

fitur_names = ['fakultas_enc', 'gender_enc', 'semester']
for nama, koef in zip(fitur_names, log_model.coef_[0]):
    or_val = np.exp(koef)
    print(f"  {nama:20s}: koef = {koef:.4f}, OR = {or_val:.4f}")

print(f"\n  Intercept: {log_model.intercept_[0]:.4f}")
```

```python
# Interpretasi dalam konteks
print("""
=== Cara Membaca Odds Ratio ===

Contoh: Jika OR untuk 'semester' = 1.15, artinya:
- Setiap kenaikan 1 unit semester, odds untuk 'Puas' meningkat 15%.
- Odds = probabilitas kejadian / probabilitas tidak kejadian.

Contoh: Jika OR untuk 'gender_enc' = 0.80, artinya:
- Kelompok gender tertentu memiliki odds 'Puas' 20% lebih rendah
  dibandingkan kelompok referensi.

Catatan: Interpretasi OR bergantung pada encoding variabel.
Selalu perhatikan mapping LabelEncoder sebelum menginterpretasikan.
""")

# Tampilkan mapping
print("Mapping LabelEncoder:")
print(f"  Fakultas: {dict(zip(le_fakultas.classes_, le_fakultas.transform(le_fakultas.classes_)))}")
print(f"  Gender  : {dict(zip(le_gender.classes_, le_gender.transform(le_gender.classes_)))}")
```

### Langkah 8: Ringkasan Analisis

```python
# Ringkasan semua uji Chi-Square yang dilakukan
print("=" * 60)
print("RINGKASAN ANALISIS CHI-SQUARE")
print("=" * 60)

uji_list = [
    ('Fakultas vs Kepuasan', chi2, p_value, dof),
    ('Gender vs Kepuasan', chi2_gk, p_gk, dof_gk),
    ('IPK Kategori vs Kepuasan', chi2_ik, p_ik, dof_ik),
]

for nama, c, p, d in uji_list:
    sig = "Signifikan" if p < 0.05 else "Tidak Signifikan"
    print(f"\n  {nama}:")
    print(f"    χ² = {c:.4f}, df = {d}, p = {p:.4f} → {sig}")

print()
print("=" * 60)
```

---

## Tugas yang Harus Dikumpulkan

Buat notebook Google Colab yang berisi:

1. **Dataset Survei** (15 poin)
   - Buat atau gunakan dataset survei dengan minimal 2 variabel kategorikal
   - Tampilkan distribusi frekuensi setiap variabel

2. **Tabel Kontingensi** (15 poin)
   - Buat tabel kontingensi menggunakan `pd.crosstab`
   - Tampilkan frekuensi dan persentase

3. **Uji Chi-Square** (25 poin)
   - Lakukan uji Chi-Square test of independence
   - Periksa asumsi (expected frequency ≥ 5)
   - Hitung dan interpretasikan Cramer's V

4. **Visualisasi** (20 poin)
   - Buat minimal 2 jenis visualisasi (stacked bar, heatmap, dll.)
   - Setiap visualisasi harus memiliki judul dan label yang jelas

5. **Logistic Regression** (25 poin)
   - Bangun model logistic regression sederhana
   - Tampilkan classification report
   - Interpretasikan minimal 1 odds ratio

**Format:** File `.ipynb` diunggah ke Google Classroom
**Deadline:** Satu minggu setelah pertemuan praktikum

---

## Challenge / Bonus

1. **Fisher's Exact Test**: Untuk tabel 2x2 dengan frekuensi ekspektasi kecil, gunakan `scipy.stats.fisher_exact`. Bandingkan hasilnya dengan Chi-Square.

2. **Logistic Regression dengan statsmodels**: Gunakan `statsmodels.api.Logit` untuk mendapatkan summary lengkap termasuk p-value per koefisien dan confidence interval untuk odds ratio.
   ```python
   import statsmodels.api as sm
   X_sm = sm.add_constant(X_train)
   logit_model = sm.Logit(y_train, X_sm).fit()
   print(logit_model.summary())
   # Odds ratio dengan CI
   print(np.exp(logit_model.params))
   print(np.exp(logit_model.conf_int()))
   ```

3. **Analisis survei nyata**: Gunakan data survei yang Anda kumpulkan sendiri (misalnya survei Google Forms di kelas) dan lakukan analisis Chi-Square lengkap.
