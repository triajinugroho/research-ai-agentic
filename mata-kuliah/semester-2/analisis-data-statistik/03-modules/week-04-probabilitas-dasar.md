# MODUL MINGGU 4: PROBABILITAS DASAR DAN BAYES' THEOREM

## UNIVERSITAS AL AZHAR INDONESIA
### Fakultas Sains dan Teknologi — Program Studi Informatika
### Mata Kuliah: Analisis Data Statistik (IF2XXX)

---

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Minggu** | 4 |
| **Topik** | Probabilitas Dasar dan Bayes' Theorem |
| **CPMK** | CPMK-3: Menerapkan konsep probabilitas dan distribusi probabilitas untuk memodelkan ketidakpastian dalam data |
| **Sub-CPMK** | 4.1: Menghitung probabilitas dasar, conditional probability, dan menerapkan Bayes' theorem |
| | 4.2: Mensimulasikan eksperimen probabilitas menggunakan Python |
| **Bloom's Taxonomy** | C3 (Apply) |
| **Durasi** | 100 menit (50 menit teori + 50 menit praktikum) |
| **Tools** | Google Colab, Python 3.x, random, numpy, matplotlib |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Mengingat kembali** konsep probabilitas dasar dari Semester 1 (sample space, event, complement)
2. **Menerapkan** aturan penjumlahan (addition rule) dan aturan perkalian (multiplication rule) untuk menghitung probabilitas
3. **Menghitung** conditional probability P(A|B) dan menentukan apakah dua event independen
4. **Menerapkan** Bayes' Theorem untuk memperbarui probabilitas berdasarkan bukti baru
5. **Membangun** simulasi probabilitas sederhana menggunakan Python (coin flip, dice roll, Monte Carlo)
6. **Menganalisis** aplikasi Bayes' Theorem dalam konteks nyata (spam filter, diagnostic testing)

---

## Materi Pembelajaran

### 1. Review Probabilitas Dasar (dari Semester 1)

Sebelum masuk ke materi baru, mari kita review konsep-konsep dasar probabilitas yang sudah dipelajari di Semester 1.

#### 1.1 Sample Space dan Event

**Sample Space (S)** adalah himpunan semua kemungkinan hasil dari suatu eksperimen.

| Eksperimen | Sample Space (S) | Jumlah Elemen |
|-----------|------------------|---------------|
| Lempar koin 1x | {H, T} | 2 |
| Lempar dadu 1x | {1, 2, 3, 4, 5, 6} | 6 |
| Lempar 2 koin | {HH, HT, TH, TT} | 4 |

**Event (A)** adalah subset dari sample space — yaitu hasil-hasil yang kita minati.

Contoh: Jika melempar dadu, event "mendapat angka genap" adalah A = {2, 4, 6}.

#### 1.2 Probabilitas Suatu Event

Untuk sample space dengan hasil yang **equally likely** (sama kemungkinannya):

```
P(A) = |A| / |S| = Jumlah hasil yang diinginkan / Jumlah total hasil
```

**Contoh:** P(dadu genap) = |{2, 4, 6}| / |{1,2,3,4,5,6}| = 3/6 = 0.5

#### 1.3 Sifat-sifat Dasar Probabilitas

1. **Range:** 0 ≤ P(A) ≤ 1
2. **Kepastian:** P(S) = 1
3. **Kemustahilan:** P(∅) = 0
4. **Complement:** P(A') = 1 - P(A)
   - P(dadu BUKAN genap) = 1 - 0.5 = 0.5

---

### 2. Aturan Probabilitas

#### 2.1 Addition Rule (Aturan Penjumlahan)

Untuk menghitung probabilitas **A ATAU B** terjadi:

**Rumus Umum:**
```
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
```

**Kasus Khusus — Mutually Exclusive Events** (A dan B tidak bisa terjadi bersamaan):
```
Jika A ∩ B = ∅, maka: P(A ∪ B) = P(A) + P(B)
```

**Contoh 1 — Mutually Exclusive:**

Melempar dadu sekali. Berapa P(mendapat 2 ATAU 5)?

- P(2) = 1/6, P(5) = 1/6
- Event "mendapat 2" dan "mendapat 5" tidak bisa terjadi bersamaan
- P(2 atau 5) = 1/6 + 1/6 = 2/6 = 1/3

**Contoh 2 — Not Mutually Exclusive:**

Dari satu set kartu standar (52 kartu), diambil 1 kartu. Berapa P(kartu merah ATAU kartu King)?

- P(merah) = 26/52, P(King) = 4/52, P(merah DAN King) = 2/52
- P(merah atau King) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13

#### 2.2 Multiplication Rule (Aturan Perkalian)

Untuk menghitung probabilitas **A DAN B** keduanya terjadi:

**Rumus Umum:**
```
P(A ∩ B) = P(A) × P(B|A)
```

**Kasus Khusus — Independent Events** (kejadian A tidak mempengaruhi B):
```
Jika A dan B independen: P(A ∩ B) = P(A) × P(B)
```

**Contoh 1 — Independent:**

Melempar koin 2x. Berapa P(H pada lemparan pertama DAN H pada lemparan kedua)?

- P(H1) = 1/2, P(H2) = 1/2 (independen)
- P(H1 dan H2) = 1/2 × 1/2 = 1/4

**Contoh 2 — Dependent:**

Dari kantong berisi 5 bola merah dan 3 bola biru, diambil 2 bola **tanpa pengembalian**. Berapa P(keduanya merah)?

- P(merah pertama) = 5/8
- P(merah kedua | merah pertama) = 4/7 (sisa 4 merah dari 7 bola)
- P(keduanya merah) = 5/8 × 4/7 = 20/56 = 5/14

---

### 3. Conditional Probability

#### 3.1 Definisi P(A|B)

**Conditional probability** adalah probabilitas A terjadi **dengan syarat** B sudah terjadi.

```
P(A|B) = P(A ∩ B) / P(B),    asalkan P(B) > 0
```

Dibaca: "Probabilitas A given B" atau "Probabilitas A jika diketahui B".

**Contoh:**

Di sebuah kelas, 60% mahasiswa lulus mata kuliah Statistika (L), dan 40% mahasiswa lulus Statistika DAN aktif di kelas (L ∩ A). Jika seorang mahasiswa diketahui lulus, berapa probabilitas dia aktif di kelas?

- P(L) = 0.60, P(L ∩ A) = 0.40
- P(A|L) = P(L ∩ A) / P(L) = 0.40 / 0.60 = 2/3 ≈ 0.667

Artinya: 66.7% mahasiswa yang lulus ternyata aktif di kelas.

#### 3.2 Independence (Kebebasan)

Dua event A dan B dikatakan **independen** jika dan hanya jika:

```
P(A|B) = P(A)    atau equivalen:    P(A ∩ B) = P(A) × P(B)
```

Artinya: mengetahui bahwa B terjadi **tidak mengubah** probabilitas A.

**Contoh:**

Lempar dadu 2x. Apakah event "dadu pertama = 6" dan "dadu kedua = 3" independen?

- P(D1=6) = 1/6
- P(D1=6 | D2=3) = 1/6 (hasil dadu kedua tidak mempengaruhi dadu pertama)
- Karena P(D1=6 | D2=3) = P(D1=6), maka kedua event **independen**.

**Contoh non-independen:**

Mengambil kartu dari deck **tanpa pengembalian**. Event "kartu pertama = Ace" dan "kartu kedua = Ace" **tidak independen**, karena pengambilan pertama mempengaruhi komposisi deck.

---

### 4. Bayes' Theorem

#### 4.1 Formula

Bayes' Theorem memungkinkan kita **memperbarui kepercayaan (belief)** berdasarkan bukti baru.

```
P(A|B) = P(B|A) × P(A) / P(B)
```

Di mana:
- **P(A)** = **Prior** — probabilitas awal A sebelum ada bukti
- **P(B|A)** = **Likelihood** — probabilitas mengamati bukti B jika A benar
- **P(B)** = **Evidence** — probabilitas total mengamati bukti B
- **P(A|B)** = **Posterior** — probabilitas A setelah memperhitungkan bukti B

#### 4.2 Intuisi: Prior → Evidence → Posterior

Bayangkan Bayes' Theorem sebagai proses **belajar dari data**:

```
[Keyakinan Awal]  +  [Bukti Baru]  →  [Keyakinan yang Diperbarui]
     Prior         ×   Likelihood   =        Posterior
```

**Analogi sederhana:** Anda menduga kemungkinan hujan hari ini 30% (prior). Lalu Anda melihat langit mendung gelap (evidence). Sekarang Anda memperbarui keyakinan menjadi 80% (posterior). Itulah esensi Bayes!

#### 4.3 Menghitung P(B) dengan Total Probability

Seringkali P(B) tidak langsung diketahui. Kita gunakan **Law of Total Probability**:

```
P(B) = P(B|A) × P(A) + P(B|A') × P(A')
```

Sehingga Bayes' Theorem lengkapnya:

```
P(A|B) = P(B|A) × P(A) / [P(B|A) × P(A) + P(B|A') × P(A')]
```

#### 4.4 Tree Diagram

Tree diagram sangat membantu untuk memvisualisasikan Bayes' Theorem.

```
                         P(B|A)
                  ┌──── B (bukti ada)
         P(A)    │
    ┌─── A ──────┤
    │            │
    │            └──── B' (bukti tidak ada)
    │                    P(B'|A)
────┤
    │                    P(B|A')
    │            ┌──── B (bukti ada)
    │   P(A')    │
    └─── A' ─────┤
                 │
                 └──── B' (bukti tidak ada)
                         P(B'|A')
```

**Langkah menghitung dengan tree diagram:**
1. Tuliskan P(A) dan P(A') di cabang pertama
2. Tuliskan P(B|A) dan P(B|A') di cabang kedua
3. Kalikan sepanjang cabang untuk mendapat P(A ∩ B) dan P(A' ∩ B)
4. P(B) = jumlah semua cabang yang berakhir di B
5. P(A|B) = P(A ∩ B) / P(B)

---

### 5. Aplikasi Bayes' Theorem

#### 5.1 Spam Filter

Email spam filter menggunakan **Naive Bayes classifier** untuk menentukan apakah email baru adalah spam.

**Skenario:**
- P(Spam) = 0.30 (30% email di inbox Anda adalah spam — prior)
- P(mengandung kata "gratis" | Spam) = 0.80 (likelihood)
- P(mengandung kata "gratis" | Bukan Spam) = 0.10

**Pertanyaan:** Jika sebuah email mengandung kata "gratis", berapa probabilitas email tersebut spam?

**Penyelesaian:**

```
P(Spam | "gratis") = P("gratis"|Spam) × P(Spam) / P("gratis")

P("gratis") = P("gratis"|Spam) × P(Spam) + P("gratis"|Bukan Spam) × P(Bukan Spam)
            = 0.80 × 0.30 + 0.10 × 0.70
            = 0.24 + 0.07
            = 0.31

P(Spam | "gratis") = (0.80 × 0.30) / 0.31 = 0.24 / 0.31 ≈ 0.774
```

**Interpretasi:** Jika email mengandung kata "gratis", ada probabilitas ~77.4% bahwa email tersebut spam. Prior 30% meningkat menjadi 77.4% setelah melihat bukti!

#### 5.2 Medical Diagnostic Testing

Aplikasi penting lainnya adalah dalam **uji diagnostik medis**. Di sini kita berkenalan dengan dua istilah penting:

**Sensitivity (True Positive Rate):** P(Test Positif | Sakit)
- Kemampuan test mendeteksi orang yang benar-benar sakit

**Specificity (True Negative Rate):** P(Test Negatif | Sehat)
- Kemampuan test mengidentifikasi orang yang benar-benar sehat

| | Benar-benar Sakit | Benar-benar Sehat |
|---|---|---|
| **Test Positif** | True Positive (TP) | False Positive (FP) |
| **Test Negatif** | False Negative (FN) | True Negative (TN) |

```
Sensitivity = TP / (TP + FN)
Specificity = TN / (TN + FP)
```

**Pertanyaan kritis:** Jika test positif, berapa probabilitas benar-benar sakit? Ini disebut **Positive Predictive Value (PPV)**, dan dihitung dengan Bayes' Theorem.

---

### 6. Simulasi Probabilitas dengan Python

Simulasi memungkinkan kita **memverifikasi perhitungan teoretis** dan membangun intuisi tentang probabilitas.

#### 6.1 Setup

```python
import random
import numpy as np
import matplotlib.pyplot as plt

# Set seed untuk reprodusibilitas
random.seed(42)
np.random.seed(42)
```

#### 6.2 Simulasi Coin Flip

```python
def simulasi_koin(n_flips, n_simulasi=10000):
    """
    Simulasikan melempar koin n_flips kali, hitung proporsi Heads.
    Ulangi simulasi n_simulasi kali.
    """
    hasil = []
    for _ in range(n_simulasi):
        flips = [random.choice(['H', 'T']) for _ in range(n_flips)]
        proporsi_heads = flips.count('H') / n_flips
        hasil.append(proporsi_heads)
    return hasil

# Simulasi: lempar koin 10x, ulangi 10.000 kali
proporsi = simulasi_koin(n_flips=10)

plt.figure(figsize=(10, 6))
plt.hist(proporsi, bins=11, edgecolor='white', color='#36A2EB', alpha=0.8, density=True)
plt.axvline(0.5, color='red', linestyle='--', linewidth=2, label='Nilai Teoritis = 0.5')
plt.axvline(np.mean(proporsi), color='green', linestyle='-.',
            linewidth=2, label=f'Mean Simulasi = {np.mean(proporsi):.4f}')
plt.title('Distribusi Proporsi Heads dari 10 Lemparan Koin\n(10.000 simulasi)',
          fontsize=14, fontweight='bold')
plt.xlabel('Proporsi Heads', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()

print(f"Mean proporsi Heads: {np.mean(proporsi):.4f}")
print(f"Std proporsi Heads:  {np.std(proporsi):.4f}")
```

#### 6.3 Simulasi Dice Roll

```python
def simulasi_dadu(n_rolls, n_simulasi=10000):
    """
    Simulasikan melempar dadu n_rolls kali, hitung rata-rata nilai.
    """
    hasil = []
    for _ in range(n_simulasi):
        rolls = [random.randint(1, 6) for _ in range(n_rolls)]
        rata_rata = sum(rolls) / n_rolls
        hasil.append(rata_rata)
    return hasil

# Simulasi: lempar dadu 1x, ulangi 10.000 kali
hasil_1 = simulasi_dadu(n_rolls=1)

# Distribusi frekuensi
plt.figure(figsize=(10, 6))
values, counts = np.unique(hasil_1, return_counts=True)
plt.bar(values, counts / len(hasil_1), color='#FF6384', edgecolor='white', width=0.6)
plt.axhline(y=1/6, color='blue', linestyle='--', linewidth=2,
            label=f'Probabilitas Teoritis = {1/6:.4f}')
plt.title('Distribusi Hasil Lempar Dadu 1x (10.000 simulasi)',
          fontsize=14, fontweight='bold')
plt.xlabel('Nilai Dadu', fontsize=12)
plt.ylabel('Proporsi', fontsize=12)
plt.xticks([1, 2, 3, 4, 5, 6])
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()

# Verifikasi: Apakah semua nilai memiliki probabilitas ~1/6?
for val, cnt in zip(values, counts):
    print(f"Dadu = {val:.0f}: Proporsi = {cnt/len(hasil_1):.4f} (Teoritis: {1/6:.4f})")
```

#### 6.4 Simulasi Monty Hall Problem

Monty Hall Problem adalah salah satu masalah probabilitas paling terkenal yang sering kali kontra-intuitif.

**Aturan permainan:**
1. Ada 3 pintu. Di balik 1 pintu ada mobil, 2 pintu lainnya ada kambing.
2. Anda memilih 1 pintu.
3. Host (yang tahu di mana mobilnya) membuka 1 pintu lain yang berisi kambing.
4. Anda diberi pilihan: **tetap** dengan pilihan awal atau **pindah** ke pintu yang tersisa.

**Pertanyaan:** Apakah lebih baik tetap atau pindah?

```python
def monty_hall_simulasi(n_simulasi=100000, strategi='pindah'):
    """
    Simulasikan Monty Hall Problem.
    strategi: 'pindah' atau 'tetap'
    """
    menang = 0

    for _ in range(n_simulasi):
        # Setup: mobil di balik salah satu pintu (0, 1, atau 2)
        pintu_mobil = random.randint(0, 2)

        # Pemain memilih salah satu pintu
        pilihan_awal = random.randint(0, 2)

        # Host membuka pintu yang BUKAN pilihan pemain dan BUKAN pintu mobil
        pintu_tersedia = [p for p in range(3) if p != pilihan_awal and p != pintu_mobil]
        pintu_dibuka = random.choice(pintu_tersedia)

        if strategi == 'tetap':
            pilihan_final = pilihan_awal
        elif strategi == 'pindah':
            # Pindah ke pintu yang tersisa (bukan pilihan awal, bukan yang dibuka)
            pilihan_final = [p for p in range(3)
                           if p != pilihan_awal and p != pintu_dibuka][0]

        if pilihan_final == pintu_mobil:
            menang += 1

    return menang / n_simulasi

# Jalankan simulasi
n_sim = 100000
prob_tetap = monty_hall_simulasi(n_sim, 'tetap')
prob_pindah = monty_hall_simulasi(n_sim, 'pindah')

print("=" * 50)
print("SIMULASI MONTY HALL PROBLEM")
print("=" * 50)
print(f"Jumlah simulasi: {n_sim:,}")
print(f"Strategi TETAP:  P(menang) = {prob_tetap:.4f}  (Teoritis: 1/3 = 0.3333)")
print(f"Strategi PINDAH: P(menang) = {prob_pindah:.4f}  (Teoritis: 2/3 = 0.6667)")
print(f"\nKesimpulan: Strategi PINDAH ~2x lebih baik dari TETAP!")

# Visualisasi
plt.figure(figsize=(8, 5))
strategi_label = ['Tetap', 'Pindah']
prob_values = [prob_tetap, prob_pindah]
colors = ['#FF6384', '#36A2EB']
bars = plt.bar(strategi_label, prob_values, color=colors, edgecolor='white', width=0.5)

# Tambahkan garis teoritis
plt.axhline(y=1/3, color='#FF6384', linestyle='--', alpha=0.7, label='Teoritis: 1/3')
plt.axhline(y=2/3, color='#36A2EB', linestyle='--', alpha=0.7, label='Teoritis: 2/3')

for bar, val in zip(bars, prob_values):
    plt.text(bar.get_x() + bar.get_width()/2, val + 0.02,
             f'{val:.4f}', ha='center', fontsize=14, fontweight='bold')

plt.title('Monty Hall Problem: Tetap vs Pindah', fontsize=14, fontweight='bold')
plt.ylabel('Probabilitas Menang', fontsize=12)
plt.ylim(0, 0.85)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()
```

#### 6.5 Implementasi Bayes' Theorem dengan Python

```python
def bayes_theorem(prior, likelihood, false_positive_rate):
    """
    Menghitung posterior probability menggunakan Bayes' Theorem.

    Parameters:
    -----------
    prior : float
        P(A) - probabilitas awal hypothesis
    likelihood : float
        P(B|A) - probabilitas evidence jika hypothesis benar
    false_positive_rate : float
        P(B|A') - probabilitas evidence jika hypothesis salah

    Returns:
    --------
    posterior : float
        P(A|B) - probabilitas hypothesis setelah melihat evidence
    """
    # P(B) = P(B|A)*P(A) + P(B|A')*P(A')
    p_evidence = likelihood * prior + false_positive_rate * (1 - prior)

    # P(A|B) = P(B|A)*P(A) / P(B)
    posterior = (likelihood * prior) / p_evidence

    return posterior

# === Contoh 1: Spam Filter ===
print("=" * 55)
print("CONTOH 1: SPAM FILTER")
print("=" * 55)

prior_spam = 0.30          # P(Spam)
likelihood_spam = 0.80     # P("gratis" | Spam)
fp_rate_spam = 0.10        # P("gratis" | Bukan Spam)

posterior_spam = bayes_theorem(prior_spam, likelihood_spam, fp_rate_spam)

print(f"Prior P(Spam)                    = {prior_spam:.2f}")
print(f"Likelihood P('gratis'|Spam)      = {likelihood_spam:.2f}")
print(f"False Positive P('gratis'|~Spam) = {fp_rate_spam:.2f}")
print(f"Posterior P(Spam|'gratis')        = {posterior_spam:.4f}")
print(f"\nInterpretasi: Email dengan kata 'gratis' memiliki")
print(f"probabilitas {posterior_spam*100:.1f}% adalah spam.")

# === Contoh 2: Medical Test ===
print("\n" + "=" * 55)
print("CONTOH 2: MEDICAL DIAGNOSTIC TEST")
print("=" * 55)

prevalence = 0.01          # P(Sakit) - 1% populasi terinfeksi
sensitivity = 0.95         # P(Test+|Sakit)
false_pos = 0.05           # P(Test+|Sehat) = 1 - Specificity

posterior_sakit = bayes_theorem(prevalence, sensitivity, false_pos)

print(f"Prevalence P(Sakit)          = {prevalence:.4f} ({prevalence*100:.1f}%)")
print(f"Sensitivity P(Test+|Sakit)   = {sensitivity:.2f}")
print(f"False Positive P(Test+|Sehat)= {false_pos:.2f}")
print(f"PPV P(Sakit|Test+)           = {posterior_sakit:.4f} ({posterior_sakit*100:.1f}%)")
print(f"\nInterpretasi: Meskipun test positif, probabilitas")
print(f"benar-benar sakit hanya {posterior_sakit*100:.1f}%!")
print(f"Ini karena prevalence penyakit sangat rendah (base rate fallacy).")
```

#### 6.6 Visualisasi Dampak Prevalence terhadap PPV

```python
def plot_prevalence_vs_ppv():
    """
    Visualisasi bagaimana prevalence mempengaruhi PPV
    untuk test dengan sensitivity dan specificity tertentu.
    """
    prevalences = np.linspace(0.001, 0.50, 200)
    sensitivity = 0.95
    specificity = 0.95
    false_pos = 1 - specificity

    ppv_values = []
    npv_values = []

    for prev in prevalences:
        ppv = bayes_theorem(prev, sensitivity, false_pos)
        ppv_values.append(ppv)

    plt.figure(figsize=(10, 6))
    plt.plot(prevalences * 100, ppv_values, color='#FF6384',
             linewidth=2.5, label='PPV (Positive Predictive Value)')
    plt.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5, label='50% threshold')

    # Highlight area di mana PPV < 50%
    threshold_idx = next(i for i, v in enumerate(ppv_values) if v >= 0.5)
    threshold_prev = prevalences[threshold_idx] * 100
    plt.axvline(x=threshold_prev, color='orange', linestyle=':',
                linewidth=2, label=f'PPV=50% saat prevalence={threshold_prev:.1f}%')

    plt.fill_between(prevalences[:threshold_idx] * 100, ppv_values[:threshold_idx],
                     alpha=0.15, color='red', label='PPV < 50% (lebih banyak false positive)')

    plt.title(f'Dampak Prevalence terhadap PPV\n(Sensitivity={sensitivity:.0%}, '
              f'Specificity={specificity:.0%})', fontsize=14, fontweight='bold')
    plt.xlabel('Prevalence (%)', fontsize=12)
    plt.ylabel('Positive Predictive Value (PPV)', fontsize=12)
    plt.legend(fontsize=10, loc='lower right')
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 50)
    plt.ylim(0, 1.05)
    plt.tight_layout()
    plt.show()

plot_prevalence_vs_ppv()
```

---

## Studi Kasus: Diagnostic Testing — "Jika Test COVID Positif, Berapa Probabilitas Benar-benar Terinfeksi?"

### Konteks Masalah

Pada masa pandemi COVID-19, jutaan orang menjalani rapid test dan PCR test. Namun, banyak yang tidak memahami: **test positif BUKAN berarti pasti sakit**. Mari kita analisis dengan Bayes' Theorem.

### Data

Misalkan sebuah rapid antigen test memiliki:
- **Sensitivity** = 85% — P(Test Positif | Terinfeksi) = 0.85
- **Specificity** = 97% — P(Test Negatif | Tidak Terinfeksi) = 0.97
- **False Positive Rate** = 3% — P(Test Positif | Tidak Terinfeksi) = 0.03

Kita akan analisis dua skenario:
- **Skenario A:** Prevalence rendah = 1% (situasi normal, tanpa gelombang)
- **Skenario B:** Prevalence tinggi = 20% (saat puncak gelombang)

### Perhitungan dengan Python

```python
print("=" * 60)
print("STUDI KASUS: COVID-19 DIAGNOSTIC TESTING")
print("=" * 60)

sensitivity = 0.85
specificity = 0.97
false_pos_rate = 1 - specificity  # 0.03

skenario = {
    'A: Prevalence Rendah (1%)': 0.01,
    'B: Prevalence Tinggi (20%)': 0.20,
}

results = {}

for nama, prevalence in skenario.items():
    ppv = bayes_theorem(prevalence, sensitivity, false_pos_rate)
    results[nama] = ppv

    print(f"\n--- {nama} ---")
    print(f"Prevalence: {prevalence*100:.0f}%")
    print(f"P(Terinfeksi | Test Positif) = {ppv:.4f} ({ppv*100:.1f}%)")

    # Tree diagram numerik
    pop = 10000
    sakit = int(pop * prevalence)
    sehat = pop - sakit

    tp = int(sakit * sensitivity)       # True Positive
    fn = sakit - tp                      # False Negative
    fp = int(sehat * false_pos_rate)     # False Positive
    tn = sehat - fp                      # True Negative

    print(f"\nDari {pop:,} orang yang di-test:")
    print(f"  Terinfeksi   : {sakit:,}")
    print(f"    Test (+)   : {tp:,} (True Positive)")
    print(f"    Test (-)   : {fn:,} (False Negative)")
    print(f"  Tidak Infeksi: {sehat:,}")
    print(f"    Test (+)   : {fp:,} (False Positive)")
    print(f"    Test (-)   : {tn:,} (True Negative)")
    print(f"  Total Test (+): {tp + fp:,}")
    print(f"  PPV = {tp}/{tp+fp} = {tp/(tp+fp):.4f}")
```

### Visualisasi Perbandingan

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

for idx, (nama, prevalence) in enumerate(skenario.items()):
    pop = 10000
    sakit = int(pop * prevalence)
    sehat = pop - sakit

    tp = int(sakit * sensitivity)
    fn = sakit - tp
    fp = int(sehat * false_pos_rate)
    tn = sehat - fp

    # Stacked bar chart
    labels = ['Sakit', 'Sehat']
    test_pos = [tp, fp]
    test_neg = [fn, tn]

    x = np.arange(len(labels))
    width = 0.35

    axes[idx].bar(x - width/2, test_pos, width, label='Test Positif',
                  color=['#4CAF50', '#FF5252'])
    axes[idx].bar(x + width/2, test_neg, width, label='Test Negatif',
                  color=['#FFB74D', '#64B5F6'])

    # Label di atas bar
    for i, (tp_v, tn_v) in enumerate(zip(test_pos, test_neg)):
        axes[idx].text(i - width/2, tp_v + 50, f'{tp_v:,}',
                       ha='center', fontweight='bold', fontsize=10)
        axes[idx].text(i + width/2, tn_v + 50, f'{tn_v:,}',
                       ha='center', fontweight='bold', fontsize=10)

    ppv = tp / (tp + fp)
    axes[idx].set_title(f'{nama}\nPPV = {ppv:.1%}',
                        fontsize=12, fontweight='bold')
    axes[idx].set_xticks(x)
    axes[idx].set_xticklabels(['Benar-benar\nSakit', 'Benar-benar\nSehat'])
    axes[idx].legend(['Test (+)', 'Test (-)'])
    axes[idx].set_ylabel('Jumlah Orang')

plt.suptitle('Dampak Prevalence terhadap Nilai Prediktif Test COVID-19\n(Sensitivity=85%, Specificity=97%)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Insight Penting

> **Pada prevalence 1%:** Meskipun test Anda positif, probabilitas benar-benar terinfeksi hanya sekitar **22%**. Artinya, dari setiap 5 orang yang test-nya positif, hampir 4 di antaranya sebenarnya **tidak terinfeksi** (false positive).

> **Pada prevalence 20%:** Test positif menjadi jauh lebih bermakna — probabilitas terinfeksi meningkat menjadi sekitar **88%**.

> **Pelajaran:** Jangan pernah menginterpretasikan hasil test tanpa mempertimbangkan **base rate** (prevalence). Ini adalah salah satu contoh paling penting dari **base rate fallacy** yang sering terjadi di kehidupan nyata.

---

## AI Corner: Gunakan AI untuk Mengecek Perhitungan Probabilitas Anda

### Cara Memanfaatkan AI

AI dapat membantu Anda dalam:

1. **Mengecek perhitungan** — Pastikan jawaban Anda benar sebelum mengumpulkan tugas
2. **Memvisualisasikan tree diagram** — Minta AI menggambarkan tree diagram dari soal probabilitas
3. **Menjelaskan intuisi** — Jika konsep terasa abstrak, minta AI menjelaskan dengan analogi
4. **Membuat soal latihan** — Minta AI membuat soal dengan tingkat kesulitan yang Anda inginkan

### Contoh Prompt

**Prompt 1 — Mengecek perhitungan:**
```
Saya menghitung soal Bayes' Theorem berikut:
- Prior P(Sakit) = 0.05
- Sensitivity P(Test+|Sakit) = 0.90
- Specificity P(Test-|Sehat) = 0.95
- Jawaban saya: P(Sakit|Test+) = 0.486

Apakah jawaban saya benar? Tunjukkan langkah-langkahnya.
```

**Prompt 2 — Memahami intuisi:**
```
Jelaskan mengapa pada Monty Hall Problem, probabilitas menang
menjadi 2/3 jika kita pindah pintu. Gunakan analogi sederhana
yang mudah dipahami mahasiswa semester 2.
```

**Prompt 3 — Membuat soal latihan:**
```
Buatkan 3 soal Bayes' Theorem dengan konteks yang relevan
untuk mahasiswa Indonesia (misalnya: e-commerce, ojek online,
atau kesehatan). Sertakan kunci jawaban dan langkah penyelesaian.
```

### Batasan dan Peringatan

- **Selalu verifikasi** jawaban AI dengan perhitungan manual atau Python
- AI kadang **salah menghitung** — terutama pada soal probabilitas yang melibatkan banyak langkah
- Jangan gunakan AI untuk **mengerjakan tugas** tanpa memahami prosesnya
- Gunakan AI sebagai **tutor**, bukan **pengganti belajar**

---

## Latihan Mandiri

### Latihan 1: Aturan Probabilitas (Sub-CPMK 4.1)

**Soal 1a.** Dari satu set kartu standar (52 kartu), diambil 1 kartu secara acak. Hitung:
- P(Kartu As atau Kartu Hati)
- P(Kartu wajah atau Kartu hitam)

**Soal 1b.** Sebuah perusahaan e-commerce mengirim 1000 paket. Dari data historis:
- P(paket terlambat) = 0.08
- P(paket rusak) = 0.05
- P(paket terlambat DAN rusak) = 0.02

Hitung P(paket terlambat ATAU rusak).

### Latihan 2: Conditional Probability (Sub-CPMK 4.1)

Sebuah survei di kampus menunjukkan:
- 70% mahasiswa memiliki laptop
- 40% mahasiswa memiliki laptop DAN tablet
- 50% mahasiswa memiliki tablet

Hitung:
1. P(Tablet | Laptop)
2. Apakah memiliki laptop dan tablet independen?
3. P(Laptop atau Tablet)

### Latihan 3: Bayes' Theorem (Sub-CPMK 4.1)

Sebuah sistem deteksi fraud pada transaksi e-commerce memiliki:
- P(Fraud) = 0.02 (2% transaksi adalah fraud)
- P(Alert | Fraud) = 0.95 (sensitivity)
- P(Alert | Bukan Fraud) = 0.10 (false positive rate)

1. Jika sistem memberikan alert, berapa probabilitas transaksi tersebut benar-benar fraud?
2. Gambarkan tree diagram untuk masalah ini.
3. Jika prevalence fraud naik menjadi 10%, bagaimana perubahannya?

### Latihan 4: Simulasi Python (Sub-CPMK 4.2)

**Soal 4a.** Buat simulasi Python (10.000 iterasi) untuk memverifikasi jawaban Latihan 3. Bandingkan hasil simulasi dengan perhitungan teoritis.

**Soal 4b.** **Birthday Problem:** Dalam sebuah kelas berisi n orang, berapa probabilitas bahwa setidaknya 2 orang memiliki ulang tahun yang sama? Buat simulasi untuk n = 5, 10, 15, 20, 23, 30, 40, 50 dan bandingkan dengan rumus teoritis:

```python
# Hint: Rumus teoritis
# P(setidaknya 2 orang sama) = 1 - P(semua berbeda)
# P(semua berbeda) = (365/365) × (364/365) × (363/365) × ... × ((365-n+1)/365)
```

Plot hasilnya dalam satu grafik (simulasi vs teoritis).

**Soal 4c.** Modifikasi simulasi Monty Hall untuk kasus **100 pintu** (1 mobil, 99 kambing). Host membuka 98 pintu yang berisi kambing. Apakah kesimpulannya sama?

---

## Referensi

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson. — Chapter 2: Probability.
2. Downey, A. B. (2021). *Think Bayes: Bayesian Statistics in Python* (2nd ed.). O'Reilly Media. https://allendowney.github.io/ThinkBayes2/
3. 3Blue1Brown. (2019). "Bayes theorem, the geometry of changing beliefs." YouTube. https://www.youtube.com/watch?v=HZGCoVF3YvM
4. Gigerenzer, G. (2002). *Calculated Risks: How to Know When Numbers Deceive You*. Simon & Schuster. — Bab tentang base rate fallacy.
5. McGrayne, S. B. (2011). *The Theory That Would Not Die: How Bayes' Rule Cracked the Enigma Code*. Yale University Press.
6. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media. — Chapter 3: NumPy.
7. Python `random` module documentation. https://docs.python.org/3/library/random.html

---

*Modul ini adalah bagian dari mata kuliah Analisis Data Statistik, Program Studi Informatika, Universitas Al Azhar Indonesia. Semester Genap 2025/2026.*
