# BAB 4: PROBABILITAS DASAR DAN TEOREMA BAYES

**Tri Aji Nugroho, S.T., M.T.**
Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-3.1 | Menjelaskan konsep ruang sampel, kejadian, dan aksioma probabilitas Kolmogorov | C2 |
| CPMK-3.2 | Menerapkan aturan penjumlahan dan aturan perkalian untuk menghitung probabilitas | C3 |
| CPMK-3.3 | Menghitung probabilitas bersyarat dan menentukan independensi dua kejadian | C3 |
| CPMK-3.4 | Menerapkan Teorema Bayes untuk memperbarui probabilitas berdasarkan bukti baru | C3 |
| CPMK-3.5 | Membangun simulasi probabilitas menggunakan Python (Monte Carlo, random module) | C3 |

---

## 4.1 Konsep Dasar Probabilitas

### 4.1.1 Mengapa Probabilitas Penting bagi Informatika?

Probabilitas adalah bahasa matematis untuk mendeskripsikan **ketidakpastian**. Dalam dunia informatika, ketidakpastian ada di mana-mana:

| Bidang Informatika | Contoh Ketidakpastian | Peran Probabilitas |
|--------------------|----------------------|-------------------|
| **Machine Learning** | Apakah email ini spam? | P(Spam \| kata "gratis") = ? |
| **Cybersecurity** | Apakah transaksi ini fraud? | P(Fraud \| pola anomali) = ? |
| **Networking** | Apakah paket data akan hilang? | P(packet loss) = ? |
| **Software Testing** | Apakah bug masih ada setelah testing? | P(bug remaining \| 1000 test passed) = ? |
| **Recommendation System** | Apakah user akan suka film ini? | P(suka \| riwayat tontonan) = ? |

> "Probability is the language of uncertainty, and uncertainty is the language of real-world data."
> — Adapted from *Think Bayes*, Allen B. Downey

### 4.1.2 Eksperimen, Ruang Sampel, dan Kejadian

**Eksperimen (Percobaan)** adalah proses yang menghasilkan hasil yang tidak pasti. **Ruang sampel** (sample space, **S**) adalah himpunan semua kemungkinan hasil dari suatu eksperimen. **Kejadian** (event, **A**) adalah himpunan bagian (subset) dari ruang sampel.

| Eksperimen | Ruang Sampel (S) | |S| | Contoh Kejadian |
|-----------|------------------|-----|-----------------|
| Lempar koin 1x | {H, T} | 2 | A = {H} "muncul Head" |
| Lempar dadu 1x | {1, 2, 3, 4, 5, 6} | 6 | B = {2, 4, 6} "angka genap" |
| Lempar 2 koin | {HH, HT, TH, TT} | 4 | C = {HH} "keduanya Head" |
| Lempar 2 dadu | {(1,1), (1,2), ..., (6,6)} | 36 | D = {(a,b) : a+b=7} "jumlah = 7" |

```
                    EKSPERIMEN
                        |
            +-----------+-----------+
            |                       |
      RUANG SAMPEL (S)         KEJADIAN (A)
      Semua kemungkinan        Subset dari S
            |                       |
      +-----+-----+          +-----+-----+
      |           |           |           |
   Diskret    Kontinu     Sederhana  Gabungan
  (terhitung) (tak         (1 hasil)  (>1 hasil)
              terhitung)
```

### 4.1.3 Aksioma Probabilitas Kolmogorov

Probabilitas didefinisikan secara formal melalui tiga aksioma yang dikemukakan oleh Andrey Kolmogorov (1933):

**Aksioma 1 — Non-negativitas:**
$$P(A) \geq 0 \quad \text{untuk setiap kejadian A}$$

**Aksioma 2 — Normalisasi:**
$$P(S) = 1$$

**Aksioma 3 — Additivitas (untuk kejadian saling lepas):**
$$\text{Jika } A \cap B = \emptyset, \text{ maka } P(A \cup B) = P(A) + P(B)$$

Dari tiga aksioma ini, kita dapat menurunkan sifat-sifat penting:

| Sifat | Formula | Contoh |
|-------|---------|--------|
| Komplemen | P(A') = 1 - P(A) | P(bukan genap) = 1 - P(genap) = 1 - 0.5 = 0.5 |
| Kejadian mustahil | P(emptyset) = 0 | P(dadu = 7) = 0 |
| Range | 0 <= P(A) <= 1 | Probabilitas selalu antara 0 dan 1 |
| Penjumlahan umum | P(A union B) = P(A) + P(B) - P(A intersect B) | Lihat Bagian 4.2 |

### 4.1.4 Pendekatan Probabilitas

Ada tiga cara memandang probabilitas:

**1. Pendekatan Klasik (A Priori):**
Jika semua hasil dalam ruang sampel sama kemungkinannya (*equally likely*):

$$P(A) = \frac{|A|}{|S|} = \frac{\text{jumlah hasil yang diinginkan}}{\text{jumlah total hasil}}$$

Contoh: P(dadu genap) = |{2,4,6}| / |{1,2,3,4,5,6}| = 3/6 = 0.5

**2. Pendekatan Frekuensi Relatif (Empiris):**
Probabilitas diestimasi dari data pengamatan berulang:

$$P(A) \approx \frac{\text{jumlah kemunculan A}}{n} \quad \text{(untuk n yang besar)}$$

Contoh: Dari 10.000 pengiriman JNE, 850 terlambat. Maka P(terlambat) = 850/10.000 = 0.085.

**3. Pendekatan Subjektif (Bayesian):**
Probabilitas mencerminkan *degree of belief* (derajat keyakinan) seseorang berdasarkan informasi yang dimiliki.

Contoh: Seorang data scientist memperkirakan P(proyek selesai tepat waktu) = 0.70 berdasarkan pengalaman dan kondisi tim.

### 4.1.5 Menghitung Probabilitas Dasar dengan Python

```python
import numpy as np
import random

# === Pendekatan Klasik ===
# Lempar dadu 1x: P(genap)
S_dadu = {1, 2, 3, 4, 5, 6}
A_genap = {2, 4, 6}
P_genap = len(A_genap) / len(S_dadu)
print(f"P(dadu genap) = {len(A_genap)}/{len(S_dadu)} = {P_genap:.4f}")

# Lempar 2 koin: P(tepat 1 Head)
S_2koin = {'HH', 'HT', 'TH', 'TT'}
A_1head = {'HT', 'TH'}
P_1head = len(A_1head) / len(S_2koin)
print(f"P(tepat 1 Head dari 2 koin) = {len(A_1head)}/{len(S_2koin)} = {P_1head:.4f}")

# === Pendekatan Frekuensi Relatif ===
# Simulasi lempar dadu 100.000 kali
np.random.seed(42)
n = 100_000
hasil_dadu = np.random.randint(1, 7, size=n)
freq_genap = np.sum(hasil_dadu % 2 == 0)
P_genap_sim = freq_genap / n
print(f"\nSimulasi {n:,} lemparan dadu:")
print(f"P(genap) = {freq_genap:,}/{n:,} = {P_genap_sim:.4f}")
print(f"Error dari teori: {abs(P_genap_sim - 0.5):.4f}")
```

---

## 4.2 Aturan Probabilitas

### 4.2.1 Aturan Penjumlahan (Addition Rule)

Aturan penjumlahan digunakan untuk menghitung probabilitas **A ATAU B** (setidaknya salah satu terjadi):

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

```
DIAGRAM VENN: A UNION B

+---------------------------------------+
|              S (Ruang Sampel)          |
|                                        |
|    +----------+   +----------+         |
|    |          |   |          |         |
|    |    A     | X |    B     |         |
|    |          |   |          |         |
|    +----------+   +----------+         |
|                 ^                       |
|              A n B                      |
|         (irisan/intersection)          |
+---------------------------------------+

P(A u B) = P(A) + P(B) - P(A n B)
```

**Kasus khusus — Kejadian Saling Lepas (Mutually Exclusive):**

Jika A dan B tidak bisa terjadi bersamaan (A intersect B = emptyset):

$$P(A \cup B) = P(A) + P(B)$$

```
DIAGRAM VENN: MUTUALLY EXCLUSIVE

+---------------------------------------+
|              S (Ruang Sampel)          |
|                                        |
|    +----------+    +----------+        |
|    |          |    |          |        |
|    |    A     |    |    B     |        |
|    |          |    |          |        |
|    +----------+    +----------+        |
|                                        |
|       Tidak ada irisan (disjoint)      |
+---------------------------------------+
```

**Contoh 1 — Mutually Exclusive:**

Lempar dadu 1x. P(mendapat 2 ATAU 5)?

- P(2) = 1/6, P(5) = 1/6
- Kejadian "2" dan "5" saling lepas (tidak bisa terjadi bersamaan)
- P(2 atau 5) = 1/6 + 1/6 = 2/6 = **1/3**

**Contoh 2 — Not Mutually Exclusive:**

Dari 52 kartu standar, diambil 1 kartu. P(kartu merah ATAU kartu King)?

- P(merah) = 26/52, P(King) = 4/52, P(merah DAN King) = 2/52
- P(merah atau King) = 26/52 + 4/52 - 2/52 = 28/52 = **7/13**

**Contoh 3 — Konteks Indonesia:**

Sebuah perusahaan e-commerce mengirim 1.000 paket per hari. Dari data historis:
- P(paket terlambat) = 0.08
- P(paket rusak) = 0.05
- P(terlambat DAN rusak) = 0.02

P(terlambat ATAU rusak) = 0.08 + 0.05 - 0.02 = **0.11** (11% paket bermasalah)

### 4.2.2 Aturan Perkalian (Multiplication Rule)

Aturan perkalian digunakan untuk menghitung probabilitas **A DAN B** (keduanya terjadi):

$$P(A \cap B) = P(A) \times P(B|A)$$

**Kasus khusus — Kejadian Independen:**

Jika A dan B saling bebas (independen):

$$P(A \cap B) = P(A) \times P(B)$$

**Contoh 1 — Kejadian Independen:**

Lempar koin 2x. P(Head pertama DAN Head kedua)?
- P(H1) = 1/2, P(H2) = 1/2 (independen)
- P(H1 dan H2) = 1/2 x 1/2 = **1/4**

**Contoh 2 — Kejadian Dependen:**

Dari kantong berisi 5 bola merah dan 3 bola biru, diambil 2 bola **tanpa pengembalian**. P(keduanya merah)?
- P(merah pertama) = 5/8
- P(merah kedua | merah pertama) = 4/7 (sisa 4 merah dari 7 bola)
- P(keduanya merah) = 5/8 x 4/7 = 20/56 = **5/14**

### 4.2.3 Implementasi Python: Aturan Probabilitas

```python
import numpy as np

# === Aturan Penjumlahan ===
# Konteks: Mahasiswa UAI yang mengambil mata kuliah
n_mahasiswa = 200
n_statistik = 80    # mengambil Statistika
n_algoritma = 90    # mengambil Algoritma
n_keduanya = 30     # mengambil keduanya

P_stat = n_statistik / n_mahasiswa
P_algo = n_algoritma / n_mahasiswa
P_keduanya = n_keduanya / n_mahasiswa

# P(Statistika ATAU Algoritma)
P_stat_atau_algo = P_stat + P_algo - P_keduanya

print("=== ATURAN PENJUMLAHAN ===")
print(f"P(Statistika)                = {P_stat:.4f}")
print(f"P(Algoritma)                 = {P_algo:.4f}")
print(f"P(Statistika DAN Algoritma)  = {P_keduanya:.4f}")
print(f"P(Statistika ATAU Algoritma) = {P_stat_atau_algo:.4f}")
print(f"Artinya: {P_stat_atau_algo*100:.0f}% mahasiswa mengambil "
      f"setidaknya salah satu dari kedua mata kuliah.\n")

# === Aturan Perkalian ===
# Konteks: Password 4 digit (0-9), setiap digit independen
P_digit_benar = 1/10
P_password_benar = P_digit_benar ** 4

print("=== ATURAN PERKALIAN ===")
print(f"P(tebak 1 digit benar)   = {P_digit_benar:.4f}")
print(f"P(tebak 4 digit benar)   = {P_password_benar:.6f}")
print(f"Artinya: 1 dari {int(1/P_password_benar):,} percobaan untuk menebak password.")
```

---

## 4.3 Permutasi dan Kombinasi

Untuk menghitung probabilitas, kita sering perlu menghitung **berapa banyak cara** suatu kejadian dapat terjadi. Di sinilah permutasi dan kombinasi berperan.

### 4.3.1 Prinsip Pencacahan

**Aturan Perkalian (Counting):** Jika ada *m* cara melakukan langkah pertama dan *n* cara melakukan langkah kedua, maka total cara = m x n.

Contoh: Plat nomor kendaraan di Indonesia terdiri dari 1-2 huruf + 1-4 angka + 1-3 huruf. Jika kita sederhanakan menjadi 2 huruf (26 pilihan) + 4 angka (10 pilihan) + 3 huruf (26 pilihan):

Total kombinasi = 26^2 x 10^4 x 26^3 = 676 x 10.000 x 17.576 = 118.813.760.000

### 4.3.2 Permutasi

**Permutasi** adalah susunan terurut dari sejumlah objek. Urutan **penting**.

$$P(n, r) = \frac{n!}{(n-r)!}$$

Contoh: Dari 10 finalis lomba coding, berapa cara memilih juara 1, 2, dan 3?

$$P(10, 3) = \frac{10!}{7!} = 10 \times 9 \times 8 = 720 \text{ cara}$$

### 4.3.3 Kombinasi

**Kombinasi** adalah pemilihan sejumlah objek tanpa memperhatikan urutan. Urutan **tidak penting**.

$$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

Contoh: Dari 10 mahasiswa, berapa cara memilih 3 orang untuk tim proyek?

$$C(10, 3) = \frac{10!}{3! \cdot 7!} = \frac{720}{6} = 120 \text{ cara}$$

### 4.3.4 Permutasi vs Kombinasi

| Aspek | Permutasi | Kombinasi |
|-------|-----------|-----------|
| Urutan | Penting | Tidak penting |
| Formula | n! / (n-r)! | n! / (r!(n-r)!) |
| Contoh | Kode PIN, ranking | Memilih tim, panitia |
| Jumlah | Selalu >= kombinasi | Selalu <= permutasi |

### 4.3.5 Perhitungan dengan Python

```python
import math
from itertools import permutations, combinations

# === Permutasi ===
n, r = 10, 3
perm = math.perm(n, r)   # Python 3.8+
print(f"P({n},{r}) = {perm}")
print(f"Dari {n} finalis, ada {perm} cara memilih juara 1, 2, 3.\n")

# === Kombinasi ===
comb = math.comb(n, r)   # Python 3.8+
print(f"C({n},{r}) = {comb}")
print(f"Dari {n} mahasiswa, ada {comb} cara memilih tim 3 orang.\n")

# === Aplikasi: Probabilitas Lotre ===
# Lotre 6/45: pilih 6 angka dari 45 angka (urutan tidak penting)
total_kombinasi = math.comb(45, 6)
P_jackpot = 1 / total_kombinasi
print(f"=== LOTRE 6/45 ===")
print(f"Total kombinasi: {total_kombinasi:,}")
print(f"P(jackpot) = 1/{total_kombinasi:,} = {P_jackpot:.10f}")
print(f"Artinya: peluang menang jackpot = {P_jackpot*100:.8f}%")

# === Aplikasi: Birthday Problem (Teoritis) ===
# P(setidaknya 2 dari n orang memiliki ulang tahun yang sama)
def birthday_prob(n_orang):
    """Hitung P(match) menggunakan kombinatorik."""
    if n_orang > 365:
        return 1.0
    p_no_match = 1.0
    for i in range(n_orang):
        p_no_match *= (365 - i) / 365
    return 1 - p_no_match

print(f"\n=== BIRTHDAY PROBLEM ===")
for n in [10, 20, 23, 30, 50, 70]:
    p = birthday_prob(n)
    print(f"n = {n:>3} orang: P(match) = {p:.4f} ({p*100:.1f}%)")
```

---

## 4.4 Probabilitas Bersyarat dan Independensi

### 4.4.1 Definisi Probabilitas Bersyarat

**Probabilitas bersyarat** (*conditional probability*) adalah probabilitas A terjadi **dengan syarat** B sudah diketahui terjadi.

$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad \text{asalkan } P(B) > 0$$

Dibaca: "Probabilitas A *given* B" atau "Probabilitas A jika diketahui B terjadi."

**Intuisi:** Ketika kita mengetahui B terjadi, ruang sampel "mengecil" dari S menjadi B saja. Kita hanya memperhatikan hasil-hasil yang ada di dalam B.

```
PROBABILITAS BERSYARAT: P(A|B)

Sebelum tahu B:                Sesudah tahu B:
+--------------------+         +----------+
|         S          |         |    B     |
|   +----+  +----+   |  --->   |  +----+  |
|   | A  |XX| B  |   |         |  | AnB|  |
|   +----+  +----+   |         |  +----+  |
+--------------------+         +----------+
P(A) = |A|/|S|                 P(A|B) = |AnB|/|B|
```

**Contoh:**

Di kelas Informatika UAI, 60% mahasiswa lulus Statistika (L), dan 40% lulus Statistika DAN aktif mengerjakan latihan soal (L intersect A). Jika diketahui seorang mahasiswa lulus, berapa probabilitas dia aktif mengerjakan latihan?

- P(L) = 0.60, P(L intersect A) = 0.40
- P(A|L) = P(L intersect A) / P(L) = 0.40 / 0.60 = 2/3 = **0.667**

Artinya: 66.7% mahasiswa yang lulus ternyata aktif mengerjakan latihan soal.

### 4.4.2 Independensi Dua Kejadian

Dua kejadian A dan B dikatakan **independen** jika mengetahui bahwa B terjadi **tidak mengubah** probabilitas A:

$$P(A|B) = P(A) \quad \Leftrightarrow \quad P(A \cap B) = P(A) \times P(B)$$

**Cara menguji independensi:**

Periksa apakah P(A intersect B) = P(A) x P(B). Jika ya, maka A dan B independen.

**Contoh independen:**

Lempar dadu 2x. Kejadian D1 = "dadu pertama = 6" dan D2 = "dadu kedua = 3":
- P(D1=6) = 1/6
- P(D1=6 | D2=3) = 1/6 (hasil dadu kedua tidak mempengaruhi dadu pertama)
- Karena P(D1=6 | D2=3) = P(D1=6), maka kedua kejadian **independen**.

**Contoh tidak independen:**

Mengambil 2 kartu dari deck **tanpa pengembalian**:
- P(kartu 1 = As) = 4/52
- P(kartu 2 = As | kartu 1 = As) = 3/51 (bukan 4/52)
- Karena P(kartu 2 = As | kartu 1 = As) != P(kartu 2 = As), kedua kejadian **tidak independen**.

### 4.4.3 Tabel Kontingensi untuk Probabilitas Bersyarat

Tabel kontingensi sangat membantu untuk menghitung probabilitas bersyarat secara sistematis.

**Contoh:** Survei 500 mahasiswa UAI tentang kepemilikan laptop dan tablet:

|  | Punya Tablet | Tidak Punya Tablet | Total |
|--|-------------|-------------------|-------|
| **Punya Laptop** | 120 | 230 | 350 |
| **Tidak Punya Laptop** | 80 | 70 | 150 |
| **Total** | 200 | 300 | 500 |

```python
import numpy as np

# Tabel kontingensi
laptop_tablet = 120
laptop_no_tablet = 230
no_laptop_tablet = 80
no_laptop_no_tablet = 70
total = 500

# P(Laptop)
P_laptop = (laptop_tablet + laptop_no_tablet) / total
print(f"P(Laptop) = {P_laptop:.4f}")

# P(Tablet)
P_tablet = (laptop_tablet + no_laptop_tablet) / total
print(f"P(Tablet) = {P_tablet:.4f}")

# P(Laptop DAN Tablet)
P_laptop_dan_tablet = laptop_tablet / total
print(f"P(Laptop DAN Tablet) = {P_laptop_dan_tablet:.4f}")

# P(Tablet | Laptop)
P_tablet_given_laptop = laptop_tablet / (laptop_tablet + laptop_no_tablet)
print(f"P(Tablet | Laptop) = {P_tablet_given_laptop:.4f}")

# P(Laptop | Tablet)
P_laptop_given_tablet = laptop_tablet / (laptop_tablet + no_laptop_tablet)
print(f"P(Laptop | Tablet) = {P_laptop_given_tablet:.4f}")

# Uji independensi
P_laptop_x_tablet = P_laptop * P_tablet
print(f"\nUji Independensi:")
print(f"P(Laptop) x P(Tablet) = {P_laptop_x_tablet:.4f}")
print(f"P(Laptop DAN Tablet)  = {P_laptop_dan_tablet:.4f}")
if abs(P_laptop_x_tablet - P_laptop_dan_tablet) < 0.01:
    print("Kesimpulan: Mendekati independen")
else:
    print("Kesimpulan: TIDAK independen")
```

---

## 4.5 Teorema Bayes

### 4.5.1 Formula dan Intuisi

Teorema Bayes adalah salah satu rumus paling penting dalam statistika dan ilmu komputer. Teorema ini memungkinkan kita **memperbarui keyakinan (belief)** berdasarkan bukti baru.

$$P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$$

Di mana:
- **P(A)** = **Prior** — keyakinan awal tentang A sebelum melihat bukti
- **P(B|A)** = **Likelihood** — probabilitas mengamati bukti B jika A benar
- **P(B)** = **Evidence** — probabilitas total mengamati bukti B
- **P(A|B)** = **Posterior** — keyakinan tentang A setelah melihat bukti B

```
INTUISI TEOREMA BAYES

[Keyakinan Awal]  +  [Bukti Baru]  -->  [Keyakinan Diperbarui]
     PRIOR         x   LIKELIHOOD   =        POSTERIOR
                       ----------
                        EVIDENCE

Contoh intuitif:
  Prior:     "Mungkin hujan hari ini" (30%)
  Evidence:  Langit mendung gelap
  Posterior: "Kemungkinan besar hujan" (80%)
```

### 4.5.2 Hukum Probabilitas Total

Seringkali P(B) tidak langsung diketahui. Kita gunakan **Hukum Probabilitas Total** (*Law of Total Probability*):

$$P(B) = P(B|A) \times P(A) + P(B|A') \times P(A')$$

Sehingga Teorema Bayes menjadi:

$$P(A|B) = \frac{P(B|A) \times P(A)}{P(B|A) \times P(A) + P(B|A') \times P(A')}$$

### 4.5.3 Tree Diagram untuk Teorema Bayes

Tree diagram (diagram pohon) sangat membantu untuk memvisualisasikan dan menghitung Teorema Bayes secara sistematis.

```
TREE DIAGRAM

                              P(B|A)
                       +---- B (bukti ada) .... P(A n B) = P(A) x P(B|A)
          P(A)        |
    +--- A ----------+
    |                 |
    |                 +---- B' (bukti tidak ada) . P(A n B') = P(A) x P(B'|A)
    |                       P(B'|A)
----+
    |                       P(B|A')
    |                 +---- B (bukti ada) .... P(A' n B) = P(A') x P(B|A')
    |    P(A')        |
    +--- A' ----------+
                      |
                      +---- B' (bukti tidak ada) . P(A' n B') = P(A') x P(B'|A')
                            P(B'|A')

Langkah:
1. Tuliskan P(A) dan P(A') di cabang pertama
2. Tuliskan P(B|A) dan P(B|A') di cabang kedua
3. Kalikan sepanjang cabang: P(A n B) = P(A) x P(B|A)
4. P(B) = P(A n B) + P(A' n B)
5. P(A|B) = P(A n B) / P(B)
```

### 4.5.4 Implementasi Teorema Bayes dengan Python

```python
def bayes_theorem(prior, likelihood, false_positive_rate):
    """
    Menghitung posterior probability menggunakan Teorema Bayes.

    Parameters:
    -----------
    prior : float
        P(A) - probabilitas awal hipotesis
    likelihood : float
        P(B|A) - probabilitas bukti jika hipotesis benar
    false_positive_rate : float
        P(B|A') - probabilitas bukti jika hipotesis salah

    Returns:
    --------
    posterior : float
        P(A|B) - probabilitas hipotesis setelah melihat bukti
    """
    # P(B) = P(B|A)*P(A) + P(B|A')*P(A')
    p_evidence = likelihood * prior + false_positive_rate * (1 - prior)

    # P(A|B) = P(B|A)*P(A) / P(B)
    posterior = (likelihood * prior) / p_evidence

    return posterior

# Test fungsi
posterior = bayes_theorem(prior=0.30, likelihood=0.80, false_positive_rate=0.10)
print(f"Posterior = {posterior:.4f}")
```

---

## 4.6 Studi Kasus Teorema Bayes

### 4.6.1 Studi Kasus 1: Spam Filter (Naive Bayes)

Email spam filter adalah salah satu aplikasi paling sukses dari Teorema Bayes di informatika. Gmail, Yahoo Mail, dan layanan email lainnya menggunakan prinsip ini.

**Skenario:**
- P(Spam) = 0.30 (30% email di inbox adalah spam)
- P(mengandung kata "gratis" | Spam) = 0.80
- P(mengandung kata "gratis" | Bukan Spam) = 0.10

**Pertanyaan:** Jika email mengandung kata "gratis", berapa P(Spam)?

```
TREE DIAGRAM: SPAM FILTER

                         P("gratis"|Spam)=0.80
                  +---- "gratis" .... 0.30 x 0.80 = 0.24
    P(Spam)=0.30  |
    +--- Spam ----+
    |              +---- bukan "gratis" . 0.30 x 0.20 = 0.06
    |                    0.20
----+
    |                    P("gratis"|~Spam)=0.10
    |              +---- "gratis" .... 0.70 x 0.10 = 0.07
    | P(~Spam)=0.70|
    +--- ~Spam ----+
                   +---- bukan "gratis" . 0.70 x 0.90 = 0.63
                         0.90

P("gratis") = 0.24 + 0.07 = 0.31
P(Spam|"gratis") = 0.24 / 0.31 = 0.774
```

```python
# === SPAM FILTER ===
print("=" * 55)
print("STUDI KASUS 1: SPAM FILTER")
print("=" * 55)

prior_spam = 0.30
likelihood_spam = 0.80
fp_rate_spam = 0.10

posterior_spam = bayes_theorem(prior_spam, likelihood_spam, fp_rate_spam)

print(f"Prior P(Spam)                    = {prior_spam:.2f}")
print(f"Likelihood P('gratis'|Spam)      = {likelihood_spam:.2f}")
print(f"False Positive P('gratis'|~Spam) = {fp_rate_spam:.2f}")
print(f"Posterior P(Spam|'gratis')        = {posterior_spam:.4f}")
print(f"\nInterpretasi: Email dengan kata 'gratis' memiliki")
print(f"probabilitas {posterior_spam*100:.1f}% adalah spam.")
print(f"Prior 30% meningkat menjadi {posterior_spam*100:.1f}% setelah melihat bukti!")
```

### 4.6.2 Studi Kasus 2: Diagnosis Medis

Teorema Bayes menjelaskan mengapa **test positif bukan berarti pasti sakit** — konsep yang sangat penting untuk dipahami.

**Istilah penting:**

| Istilah | Definisi | Formula |
|---------|----------|---------|
| Sensitivity | Kemampuan test mendeteksi orang sakit | P(Test+ \| Sakit) |
| Specificity | Kemampuan test mengidentifikasi orang sehat | P(Test- \| Sehat) |
| PPV | Positive Predictive Value | P(Sakit \| Test+) |
| NPV | Negative Predictive Value | P(Sehat \| Test-) |
| Prevalence | Proporsi populasi yang sakit | P(Sakit) |

```
CONFUSION MATRIX

                  Kondisi Sebenarnya
                  Sakit        Sehat
              +------------+------------+
Test Positif  |     TP      |     FP     |
              | (True Pos)  | (False Pos)|
              +------------+------------+
Test Negatif  |     FN      |     TN     |
              | (False Neg) | (True Neg) |
              +------------+------------+

Sensitivity = TP / (TP + FN)
Specificity = TN / (TN + FP)
PPV         = TP / (TP + FP)   <-- ini yang dihitung Bayes!
```

**Skenario:** Rapid test COVID-19
- Sensitivity = 85% -- P(Test+ | Terinfeksi) = 0.85
- Specificity = 97% -- P(Test- | Tidak Terinfeksi) = 0.97
- Kita bandingkan dua skenario prevalence

```python
print("=" * 60)
print("STUDI KASUS 2: DIAGNOSIS MEDIS (COVID-19 RAPID TEST)")
print("=" * 60)

sensitivity = 0.85
specificity = 0.97
false_pos_rate = 1 - specificity  # 0.03

skenario = {
    'Prevalence Rendah (1%)': 0.01,
    'Prevalence Tinggi (20%)': 0.20,
}

for nama, prevalence in skenario.items():
    ppv = bayes_theorem(prevalence, sensitivity, false_pos_rate)

    print(f"\n--- Skenario: {nama} ---")
    print(f"Prevalence = {prevalence*100:.0f}%")

    # Hitung untuk populasi 10.000 orang
    pop = 10_000
    sakit = int(pop * prevalence)
    sehat = pop - sakit
    tp = int(sakit * sensitivity)
    fn = sakit - tp
    fp = int(sehat * false_pos_rate)
    tn = sehat - fp

    print(f"\nDari {pop:,} orang yang di-test:")
    print(f"  Terinfeksi    : {sakit:,}")
    print(f"    Test (+)    : {tp:,} (True Positive)")
    print(f"    Test (-)    : {fn:,} (False Negative)")
    print(f"  Tidak Infeksi : {sehat:,}")
    print(f"    Test (+)    : {fp:,} (False Positive)")
    print(f"    Test (-)    : {tn:,} (True Negative)")
    print(f"  Total Test (+): {tp + fp:,}")
    print(f"  PPV = P(Sakit|Test+) = {tp}/{tp+fp} = {tp/(tp+fp):.4f} ({tp/(tp+fp)*100:.1f}%)")

print("\n" + "=" * 60)
print("INSIGHT PENTING:")
print("Prevalence 1%  -> PPV hanya ~22% (4 dari 5 positif = FALSE positive!)")
print("Prevalence 20% -> PPV naik ~88% (test jauh lebih bermakna)")
print("Jangan interpretasi hasil test tanpa mempertimbangkan BASE RATE!")
print("=" * 60)
```

### 4.6.3 Studi Kasus 3: Recommendation System

Aplikasi Teorema Bayes juga digunakan dalam sistem rekomendasi.

**Skenario:** Sebuah platform streaming video di Indonesia ingin merekomendasikan film. Dari data historis:
- P(suka film action) = 0.40
- P(menonton trailer | suka) = 0.75
- P(menonton trailer | tidak suka) = 0.20

**Pertanyaan:** Jika user menonton trailer, berapa probabilitas user akan suka film tersebut?

```python
print("=" * 55)
print("STUDI KASUS 3: RECOMMENDATION SYSTEM")
print("=" * 55)

prior_suka = 0.40
likelihood_trailer = 0.75
fp_trailer = 0.20

posterior_suka = bayes_theorem(prior_suka, likelihood_trailer, fp_trailer)

print(f"Prior P(Suka)                       = {prior_suka:.2f}")
print(f"P(Tonton Trailer | Suka)            = {likelihood_trailer:.2f}")
print(f"P(Tonton Trailer | Tidak Suka)      = {fp_trailer:.2f}")
print(f"Posterior P(Suka | Tonton Trailer)   = {posterior_suka:.4f}")
print(f"\nInterpretasi: Setelah user menonton trailer,")
print(f"keyakinan bahwa user suka naik dari {prior_suka*100:.0f}% menjadi {posterior_suka*100:.1f}%.")
print(f"Sistem bisa merekomendasikan film ini lebih tinggi.")
```

---

## 4.7 Simulasi Probabilitas dengan Python

Simulasi memungkinkan kita **memverifikasi perhitungan teoretis** dan membangun intuisi tentang probabilitas. Prinsip yang mendasarinya adalah **Hukum Bilangan Besar** (*Law of Large Numbers*): semakin banyak percobaan, semakin dekat frekuensi relatif ke probabilitas teoretis.

### 4.7.1 Simulasi Pelemparan Koin

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def simulasi_koin(n_lemparan):
    """Simulasi pelemparan koin sebanyak n kali."""
    hasil = np.random.choice(['Head', 'Tail'], size=n_lemparan)
    n_head = np.sum(hasil == 'Head')
    proporsi_head = n_head / n_lemparan
    return hasil, n_head, proporsi_head

# Simulasi dengan berbagai jumlah lemparan
jumlah_lemparan = [10, 100, 1_000, 10_000, 100_000, 1_000_000]

print("=" * 55)
print(f"{'N Lemparan':>12} | {'Head':>8} | {'P(Head)':>10} | {'Error':>10}")
print("=" * 55)

for n in jumlah_lemparan:
    _, n_head, p_head = simulasi_koin(n)
    error = abs(p_head - 0.5)
    print(f"{n:>12,} | {n_head:>8,} | {p_head:>10.6f} | {error:>10.6f}")

print("\nTeori: P(Head) = 0.5")
print("Semakin banyak lemparan -> semakin dekat ke 0.5")
print("Ini adalah Hukum Bilangan Besar (Law of Large Numbers)!")
```

### 4.7.2 Visualisasi Hukum Bilangan Besar

```python
n_max = 5000
lemparan = np.random.choice([0, 1], size=n_max)  # 0=Tail, 1=Head

# Proporsi kumulatif
proporsi_kumulatif = np.cumsum(lemparan) / np.arange(1, n_max + 1)

plt.figure(figsize=(12, 5))
plt.plot(range(1, n_max + 1), proporsi_kumulatif, color='steelblue',
         linewidth=0.8, alpha=0.8)
plt.axhline(y=0.5, color='red', linestyle='--', linewidth=2,
            label='P(Head) = 0.5 (teoritis)')
plt.xlabel('Jumlah Lemparan', fontsize=12)
plt.ylabel('Proporsi Head', fontsize=12)
plt.title('Law of Large Numbers: Konvergensi P(Head) ke 0.5',
          fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.ylim(0.3, 0.7)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Setelah {n_max} lemparan: P(Head) = {proporsi_kumulatif[-1]:.4f}")
```

### 4.7.3 Simulasi Pelemparan Dadu

```python
n_lempar = 60_000
dadu = np.random.randint(1, 7, size=n_lempar)

# Distribusi frekuensi
nilai_unik, frekuensi = np.unique(dadu, return_counts=True)
proporsi = frekuensi / n_lempar
teoritis = 1/6

print("=== SIMULASI PELEMPARAN DADU ===")
print(f"Jumlah lemparan: {n_lempar:,}\n")
print(f"{'Sisi':>6} | {'Frekuensi':>10} | {'Proporsi':>10} | {'Teoritis':>10} | {'Error':>10}")
print("-" * 60)
for s, f, p in zip(nilai_unik, frekuensi, proporsi):
    print(f"{s:>6} | {f:>10,} | {p:>10.4f} | {teoritis:>10.4f} | {abs(p-teoritis):>10.4f}")

# Visualisasi distribusi jumlah dua dadu
dadu1 = np.random.randint(1, 7, size=n_lempar)
dadu2 = np.random.randint(1, 7, size=n_lempar)
jumlah_dua_dadu = dadu1 + dadu2

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart: satu dadu
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c']
axes[0].bar(nilai_unik, proporsi, color=colors, edgecolor='white')
axes[0].axhline(y=1/6, color='red', linestyle='--',
                label=f'Teoritis: {1/6:.4f}')
axes[0].set_title(f'Proporsi Hasil 1 Dadu ({n_lempar:,} lemparan)',
                  fontsize=12, fontweight='bold')
axes[0].set_xlabel('Sisi Dadu')
axes[0].set_ylabel('Proporsi')
axes[0].legend()

# Histogram: jumlah dua dadu
axes[1].hist(jumlah_dua_dadu, bins=np.arange(1.5, 13.5, 1),
             color='steelblue', edgecolor='white', density=True, alpha=0.8)
jumlah_teoritis = range(2, 13)
prob_teoritis = [sum(1 for a in range(1,7) for b in range(1,7)
                     if a+b==s)/36 for s in jumlah_teoritis]
axes[1].plot(jumlah_teoritis, prob_teoritis, 'ro-', linewidth=2,
             markersize=6, label='Teoritis')
axes[1].set_title('Distribusi Jumlah Dua Dadu', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Jumlah')
axes[1].set_ylabel('Probabilitas')
axes[1].set_xticks(range(2, 13))
axes[1].legend()

plt.tight_layout()
plt.show()
```

### 4.7.4 Simulasi Monty Hall Problem

Monty Hall Problem adalah salah satu masalah probabilitas paling terkenal yang hasilnya sering **kontra-intuitif**.

**Aturan permainan:**
1. Ada 3 pintu. Di balik 1 pintu ada mobil, 2 pintu lainnya ada kambing.
2. Anda memilih 1 pintu.
3. Host (yang tahu lokasi mobil) membuka 1 pintu lain yang berisi kambing.
4. Anda diberi pilihan: **tetap** dengan pilihan awal atau **pindah** ke pintu tersisa.

**Analisis probabilitas:**
- Strategi TETAP: menang jika pilihan awal benar, P = **1/3**
- Strategi PINDAH: menang jika pilihan awal salah (karena pasti pindah ke mobil), P = **2/3**

```python
def monty_hall_simulasi(n_simulasi, strategi='switch'):
    """
    Simulasi Monty Hall Problem.
    strategi: 'switch' (pindah) atau 'stay' (tetap)
    """
    menang = 0

    for _ in range(n_simulasi):
        pintu_mobil = np.random.randint(0, 3)
        pilihan_pemain = np.random.randint(0, 3)

        # Host membuka pintu bukan pilihan pemain DAN bukan pintu mobil
        pintu_tersedia = [p for p in range(3)
                         if p != pilihan_pemain and p != pintu_mobil]
        pintu_dibuka = np.random.choice(pintu_tersedia)

        if strategi == 'switch':
            pilihan_akhir = [p for p in range(3)
                            if p != pilihan_pemain and p != pintu_dibuka][0]
        else:
            pilihan_akhir = pilihan_pemain

        if pilihan_akhir == pintu_mobil:
            menang += 1

    return menang / n_simulasi

# Jalankan simulasi
n_sim = 100_000
p_stay = monty_hall_simulasi(n_sim, 'stay')
p_switch = monty_hall_simulasi(n_sim, 'switch')

print("=" * 50)
print("MONTY HALL PROBLEM - SIMULASI")
print("=" * 50)
print(f"Jumlah simulasi: {n_sim:,}")
print(f"Strategi TETAP  : P(menang) = {p_stay:.4f}  (Teoritis: 1/3 = 0.3333)")
print(f"Strategi PINDAH : P(menang) = {p_switch:.4f}  (Teoritis: 2/3 = 0.6667)")
print(f"\nKesimpulan: Strategi PINDAH ~2x lebih baik daripada TETAP!")

# Visualisasi konvergensi
n_max = 5000
menang_stay = np.zeros(n_max)
menang_switch = np.zeros(n_max)

for i in range(n_max):
    pintu_mobil = np.random.randint(0, 3)
    pilihan = np.random.randint(0, 3)
    menang_stay[i] = 1 if pilihan == pintu_mobil else 0
    menang_switch[i] = 1 if pilihan != pintu_mobil else 0

kum_stay = np.cumsum(menang_stay) / np.arange(1, n_max + 1)
kum_switch = np.cumsum(menang_switch) / np.arange(1, n_max + 1)

plt.figure(figsize=(12, 6))
plt.plot(range(1, n_max + 1), kum_stay, label='Tetap (Stay)',
         color='#e74c3c', alpha=0.8)
plt.plot(range(1, n_max + 1), kum_switch, label='Pindah (Switch)',
         color='#2ecc71', alpha=0.8)
plt.axhline(y=1/3, color='#e74c3c', linestyle='--', alpha=0.5,
            label='Teori: 1/3')
plt.axhline(y=2/3, color='#2ecc71', linestyle='--', alpha=0.5,
            label='Teori: 2/3')
plt.xlabel('Jumlah Simulasi', fontsize=12)
plt.ylabel('Proporsi Kemenangan', fontsize=12)
plt.title('Monty Hall Problem: Konvergensi ke Probabilitas Teoritis',
          fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.ylim(0, 1)
plt.tight_layout()
plt.show()
```

### 4.7.5 Simulasi Monte Carlo: Estimasi Pi

Metode **Monte Carlo** menggunakan bilangan acak untuk mengestimasi nilai-nilai yang sulit dihitung secara analitis. Contoh klasik: estimasi nilai pi.

**Ide:** Bayangkan sebuah lingkaran dengan jari-jari 1 di dalam kotak 2x2. Jika kita melempar "dart" secara acak ke kotak, rasio yang jatuh di dalam lingkaran terhadap total lemparan akan mendekati pi/4.

```
ESTIMASI PI DENGAN MONTE CARLO

+-------------------+
|    .   .  *  .    |    Kotak: sisi = 2, luas = 4
|  .  * /----\ .    |    Lingkaran: r = 1, luas = pi
| .  * |  *   |  .  |
|  . * | *  * |*    |    P(dalam lingkaran) = pi/4
| .  * |  * * | .   |
|   .   \----/  *   |    Maka: pi = 4 x P(dalam lingkaran)
|    .    .  .   .  |
+-------------------+    * = di dalam lingkaran
                         . = di luar lingkaran
```

```python
def estimasi_pi_monte_carlo(n_titik):
    """Estimasi pi menggunakan metode Monte Carlo."""
    # Generate titik acak di kotak [-1, 1] x [-1, 1]
    x = np.random.uniform(-1, 1, n_titik)
    y = np.random.uniform(-1, 1, n_titik)

    # Hitung jarak dari pusat (0, 0)
    jarak = x**2 + y**2

    # Titik di dalam lingkaran jika jarak <= 1
    dalam_lingkaran = jarak <= 1
    n_dalam = np.sum(dalam_lingkaran)

    # Estimasi pi
    pi_estimasi = 4 * n_dalam / n_titik
    return pi_estimasi, x, y, dalam_lingkaran

# Estimasi pi dengan berbagai jumlah titik
print("=== ESTIMASI PI DENGAN MONTE CARLO ===\n")
print(f"{'N Titik':>12} | {'Pi Estimasi':>12} | {'Error':>12}")
print("-" * 42)

for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
    pi_est, _, _, _ = estimasi_pi_monte_carlo(n)
    error = abs(pi_est - np.pi)
    print(f"{n:>12,} | {pi_est:>12.6f} | {error:>12.6f}")

print(f"\nNilai pi sebenarnya: {np.pi:.10f}")

# Visualisasi
n_visual = 5000
pi_est, x, y, dalam = estimasi_pi_monte_carlo(n_visual)

plt.figure(figsize=(7, 7))
plt.scatter(x[dalam], y[dalam], s=1, c='blue', alpha=0.5, label='Dalam lingkaran')
plt.scatter(x[~dalam], y[~dalam], s=1, c='red', alpha=0.5, label='Luar lingkaran')

# Gambar lingkaran
theta = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(theta), np.sin(theta), 'k-', linewidth=2)

plt.axis('equal')
plt.title(f'Estimasi Pi dengan Monte Carlo (n={n_visual:,})\n'
          f'Pi estimasi = {pi_est:.4f}', fontsize=13, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### 4.7.6 Simulasi Birthday Problem

Birthday Problem adalah contoh probabilitas yang hasilnya mengejutkan: dalam sebuah kelompok **23 orang**, probabilitas setidaknya 2 orang memiliki ulang tahun yang sama sudah lebih dari **50%**!

```python
def simulasi_birthday(n_orang, n_simulasi=10_000):
    """Simulasi Birthday Problem."""
    cocok = 0
    for _ in range(n_simulasi):
        ulang_tahun = np.random.randint(1, 366, size=n_orang)
        if len(ulang_tahun) != len(set(ulang_tahun)):
            cocok += 1
    return cocok / n_simulasi

def birthday_teoritis(n):
    """Hitung P(match) secara teoritis."""
    p_no_match = 1.0
    for i in range(n):
        p_no_match *= (365 - i) / 365
    return 1 - p_no_match

# Simulasi dan hitung teoritis
ukuran = list(range(2, 61))
prob_sim = [simulasi_birthday(n, 10_000) for n in ukuran]
prob_teori = [birthday_teoritis(n) for n in ukuran]

plt.figure(figsize=(10, 6))
plt.plot(ukuran, prob_sim, 'o', markersize=3, alpha=0.6,
         label='Simulasi (10,000x)')
plt.plot(ukuran, prob_teori, '-', color='red', linewidth=2,
         label='Teoritis')
plt.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
plt.axvline(x=23, color='green', linestyle='--', alpha=0.5)
plt.annotate('23 orang -> P > 50%', xy=(23, 0.5), xytext=(30, 0.35),
             arrowprops=dict(arrowstyle='->', color='green'),
             fontsize=11, color='green', fontweight='bold')

plt.xlabel('Jumlah Orang', fontsize=12)
plt.ylabel('P(setidaknya 2 orang ulang tahun sama)', fontsize=12)
plt.title('Birthday Problem: Simulasi vs Teoritis',
          fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print("Fakta mengejutkan: Hanya butuh 23 orang agar probabilitas")
print("setidaknya 2 orang memiliki ulang tahun yang sama > 50%!")
```

### 4.7.7 Simulasi Teorema Bayes

Kita juga dapat memverifikasi Teorema Bayes melalui simulasi, dengan membuat populasi virtual dan mensimulasikan proses testing.

```python
# === Simulasi Teorema Bayes: Diagnosis Medis ===
n_populasi = 1_000_000
P_sakit = 0.01
P_pos_sakit = 0.95    # sensitivity
P_pos_sehat = 0.10    # false positive rate

# Simulasi populasi
np.random.seed(42)
sakit = np.random.choice([True, False], size=n_populasi,
                         p=[P_sakit, 1-P_sakit])

# Simulasi hasil test
hasil_tes = np.zeros(n_populasi, dtype=bool)
for i in range(n_populasi):
    if sakit[i]:
        hasil_tes[i] = np.random.random() < P_pos_sakit
    else:
        hasil_tes[i] = np.random.random() < P_pos_sehat

# Hitung confusion matrix
tp = np.sum(sakit & hasil_tes)
fp = np.sum(~sakit & hasil_tes)
fn = np.sum(sakit & ~hasil_tes)
tn = np.sum(~sakit & ~hasil_tes)

P_sakit_given_pos_sim = tp / (tp + fp)
P_sakit_given_pos_teori = bayes_theorem(P_sakit, P_pos_sakit, P_pos_sehat)

print("=" * 55)
print("SIMULASI TEOREMA BAYES (n = 1,000,000)")
print("=" * 55)
print(f"\nConfusion Matrix:")
print(f"{'':>20} {'Sakit':>12} {'Sehat':>12} {'Total':>12}")
print("-" * 60)
print(f"{'Tes Positif':>20} {tp:>12,} {fp:>12,} {tp+fp:>12,}")
print(f"{'Tes Negatif':>20} {fn:>12,} {tn:>12,} {fn+tn:>12,}")
print(f"{'Total':>20} {tp+fn:>12,} {fp+tn:>12,} {n_populasi:>12,}")
print(f"\nP(Sakit|Positif) simulasi = {P_sakit_given_pos_sim:.4f} "
      f"({P_sakit_given_pos_sim*100:.1f}%)")
print(f"P(Sakit|Positif) teoritis = {P_sakit_given_pos_teori:.4f} "
      f"({P_sakit_given_pos_teori*100:.1f}%)")
print(f"\nSimulasi mendekati nilai teoritis!")
```

---

## 4.8 AI Corner: Menggunakan AI untuk Masalah Probabilitas

### 4.8.1 Apa yang Bisa AI Bantu?

| AI Bisa Membantu | AI Tidak Bisa Menggantikan |
|-------------------|---------------------------|
| Mengecek perhitungan probabilitas Anda | Memahami makna hasil dalam konteks nyata |
| Menjelaskan intuisi di balik rumus | Menentukan apakah model probabilitas sudah tepat |
| Memvisualisasikan tree diagram | Menjamin jawaban benar 100% (sering salah hitung!) |
| Membuat soal latihan sesuai level | Menggantikan proses berpikir kritis Anda |
| Menulis kode simulasi Python | Menginterpretasi implikasi etis dari hasil |

### 4.8.2 Contoh Prompt yang Efektif

**Prompt 1 — Mengecek perhitungan:**

```
Saya menghitung soal Teorema Bayes:
- Prior P(Fraud) = 0.02
- Sensitivity P(Alert|Fraud) = 0.95
- False Positive P(Alert|~Fraud) = 0.10
- Jawaban saya: P(Fraud|Alert) = 0.162

Apakah jawaban saya benar? Tunjukkan langkah-langkahnya
dan gambarkan tree diagram.
```

**Prompt 2 — Membangun intuisi:**

```
Jelaskan mengapa pada Monty Hall Problem probabilitas menang
menjadi 2/3 jika kita pindah pintu. Gunakan analogi sederhana
yang mudah dipahami. Jangan gunakan rumus, jelaskan secara intuitif.
```

**Prompt 3 — Generate kode simulasi:**

```
Buatkan kode Python untuk mensimulasikan Birthday Problem.
- Simulasi untuk n = 5, 10, 15, 20, 23, 30, 40, 50
- Bandingkan hasil simulasi (10.000 iterasi) dengan rumus teoritis
- Tampilkan dalam tabel dan plot grafik
- Gunakan numpy dan matplotlib
- Tambahkan komentar dalam Bahasa Indonesia
```

### 4.8.3 Peringatan Penting

1. **AI sering salah hitung probabilitas** — terutama pada soal multi-langkah. Selalu verifikasi dengan perhitungan manual atau Python.
2. **Jangan gunakan AI untuk mengerjakan tugas** tanpa memahami prosesnya. Pahami dulu konsepnya, baru minta AI membantu.
3. **Gunakan AI sebagai tutor** — minta penjelasan langkah demi langkah, bukan hanya jawaban akhir.
4. **Dokumentasikan penggunaan AI** sesuai kebijakan mata kuliah (lihat template AI Usage Log di Bab 1).

### 4.8.4 Latihan: Evaluasi Output AI

Berikut adalah contoh output AI yang perlu Anda evaluasi:

> **Prompt:** "Jika P(Sakit) = 0.001, P(Test+|Sakit) = 0.99, P(Test+|Sehat) = 0.05, berapa P(Sakit|Test+)?"
>
> **Jawaban AI:** "P(Sakit|Test+) = 0.99 x 0.001 / (0.99 x 0.001 + 0.05 x 0.999) = 0.00099 / 0.05094 = 0.0194. Jadi probabilitasnya sekitar 1.94%."

**Tugas:** Verifikasi apakah jawaban AI di atas benar. Jika salah, di mana letak kesalahannya? (Petunjuk: hitung manual dan bandingkan.)

---

## Rangkuman Bab 4

1. **Probabilitas** mengukur ketidakpastian secara kuantitatif. Tiga aksioma Kolmogorov menjadi fondasi: non-negativitas (P(A) >= 0), normalisasi (P(S) = 1), dan additivitas untuk kejadian saling lepas.

2. **Aturan penjumlahan** P(A union B) = P(A) + P(B) - P(A intersect B) menghitung probabilitas "A atau B", sedangkan **aturan perkalian** P(A intersect B) = P(A) x P(B|A) menghitung probabilitas "A dan B".

3. **Probabilitas bersyarat** P(A|B) mengecilkan ruang sampel ke kejadian B saja. Dua kejadian independen jika P(A|B) = P(A), artinya mengetahui B tidak mengubah keyakinan tentang A.

4. **Teorema Bayes** (Posterior = Likelihood x Prior / Evidence) memungkinkan kita memperbarui keyakinan berdasarkan bukti baru. Ini adalah fondasi dari Naive Bayes classifier, diagnosis medis, dan banyak aplikasi AI.

5. **Base rate fallacy** terjadi ketika kita mengabaikan prevalence (prior probability). Contoh: test positif dengan sensitivity 95% tetap bermakna rendah jika prevalence penyakit sangat kecil.

6. **Simulasi Monte Carlo** menggunakan bilangan acak untuk memverifikasi perhitungan teoretis. Hukum Bilangan Besar menjamin bahwa frekuensi relatif konvergen ke probabilitas sejati seiring bertambahnya jumlah percobaan.

7. **Permutasi** (urutan penting) dan **kombinasi** (urutan tidak penting) adalah alat penting untuk menghitung jumlah cara suatu kejadian dapat terjadi dalam pendekatan klasik probabilitas.

8. Probabilitas memiliki aplikasi luas di informatika: dari **spam filtering**, **fraud detection**, **medical diagnosis**, hingga **recommendation system**. Mahasiswa informatika wajib menguasai konsep ini sebagai fondasi machine learning.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Sebuah dadu seimbang dilempar satu kali. Tentukan:
- a) Ruang sampel S
- b) P(angka prima)
- c) P(angka > 4)
- d) P(angka genap ATAU angka > 4)

**Soal 2.** Jelaskan perbedaan antara:
- a) Kejadian saling lepas (mutually exclusive) dan kejadian independen
- b) P(A|B) dan P(B|A)
- c) Permutasi dan kombinasi

**Soal 3.** Dari 52 kartu standar, diambil 1 kartu secara acak. Hitung:
- a) P(kartu As)
- b) P(kartu hati)
- c) P(kartu As ATAU kartu hati)
- d) P(kartu As DAN kartu hati)

**Soal 4.** Sebutkan dan jelaskan tiga aksioma probabilitas Kolmogorov. Berikan contoh untuk masing-masing aksioma.

### Tingkat Menengah (C2-C3)

**Soal 5.** Sebuah perusahaan e-commerce Indonesia mengirim paket melalui dua kurir:
- 60% paket dikirim via Kurir A (P(terlambat) = 0.05)
- 40% paket dikirim via Kurir B (P(terlambat) = 0.12)

Hitung:
- a) P(paket terlambat) menggunakan Hukum Probabilitas Total
- b) Jika sebuah paket terlambat, berapa P(dikirim via Kurir B)? Gunakan Teorema Bayes.
- c) Gambarkan tree diagram untuk masalah ini.

**Soal 6.** Survei terhadap 400 mahasiswa menunjukkan:
- 250 mahasiswa menggunakan Android
- 120 mahasiswa menggunakan iPhone
- 30 mahasiswa menggunakan keduanya (dual SIM)

Hitung:
- a) P(Android ATAU iPhone)
- b) P(iPhone | Android)
- c) Apakah menggunakan Android dan iPhone independen?

**Soal 7.** Dari 8 anggota tim proyek (5 programmer dan 3 designer), berapa cara:
- a) Memilih 1 ketua dan 1 wakil ketua? (Permutasi)
- b) Memilih 3 orang untuk presentasi? (Kombinasi)
- c) Memilih 3 orang yang terdiri dari 2 programmer dan 1 designer?

**Soal 8.** Tulis kode Python untuk mensimulasikan pelemparan 2 dadu sebanyak 100.000 kali.
- a) Hitung P(jumlah = 7) dari simulasi dan bandingkan dengan teori (6/36).
- b) Hitung P(jumlah >= 10) dari simulasi dan bandingkan dengan teori.
- c) Buat histogram distribusi jumlah dua dadu.

### Tingkat Mahir (C3-C4)

**Soal 9.** Sebuah sistem deteksi fraud pada platform GoPay memiliki:
- P(Fraud) = 0.02
- P(Alert | Fraud) = 0.95 (sensitivity)
- P(Alert | Bukan Fraud) = 0.10 (false positive rate)

- a) Hitung P(Fraud | Alert) menggunakan Teorema Bayes.
- b) Jika GoPay menerima alert, apakah langsung memblokir transaksi? Diskusikan trade-off antara false positive dan false negative.
- c) Tulis kode Python untuk mensimulasikan 1 juta transaksi dan verifikasi jawaban (a).
- d) Bagaimana PPV berubah jika prevalence fraud naik menjadi 10%? Plot grafik PPV vs prevalence.

**Soal 10.** Modifikasi simulasi Monty Hall Problem untuk kasus **5 pintu** (1 mobil, 4 kambing). Host membuka 3 pintu berisi kambing, menyisakan 2 pintu (pilihan awal Anda dan 1 pintu lain).
- a) Hitung secara teoretis P(menang | tetap) dan P(menang | pindah).
- b) Buat simulasi Python (100.000 iterasi) untuk memverifikasi.
- c) Generalisasi: untuk n pintu, berapa P(menang | pindah)?

**Soal 11.** (*Birthday Problem yang Diperluas*) Dalam sebuah kelas berisi n mahasiswa:
- a) Tulis fungsi Python yang menghitung P(match) secara teoritis.
- b) Tulis fungsi simulasi Birthday Problem (10.000 iterasi).
- c) Plot kedua hasil dalam satu grafik untuk n = 2 hingga 60.
- d) Berapa jumlah minimum orang agar P(match) > 99%?

**Soal 12.** Sebuah pabrik smartphone memiliki 3 lini produksi:
- Lini 1: memproduksi 50% unit, tingkat cacat 3%
- Lini 2: memproduksi 30% unit, tingkat cacat 5%
- Lini 3: memproduksi 20% unit, tingkat cacat 8%

- a) Berapa probabilitas smartphone yang dipilih secara acak ternyata cacat?
- b) Jika sebuah smartphone ternyata cacat, dari lini mana kemungkinan besar berasal?
- c) Tulis kode Python untuk menghitung jawaban (a) dan (b) serta memvisualisasikan prior vs posterior untuk setiap lini.

**Soal 13.** Estimasi nilai pi menggunakan metode Monte Carlo:
- a) Jelaskan prinsip di balik metode ini (mengapa rasio titik di dalam lingkaran mendekati pi/4?).
- b) Tulis kode Python yang mengestimasi pi untuk n = 100, 1.000, 10.000, 100.000, dan 1.000.000 titik.
- c) Plot grafik konvergensi: sumbu x = jumlah titik (log scale), sumbu y = estimasi pi.
- d) Berapa jumlah titik minimum agar error < 0.01?

---

## Referensi

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson. -- Chapter 2: Probability.
2. Downey, A. B. (2021). *Think Bayes: Bayesian Statistics in Python* (2nd ed.). O'Reilly Media. https://allendowney.github.io/ThinkBayes2/
3. Moore, D. S., McCabe, G. P., & Craig, B. A. (2021). *Introduction to the Practice of Statistics* (10th ed.). W. H. Freeman. -- Chapter 5: Probability.
4. 3Blue1Brown. (2019). "Bayes theorem, the geometry of changing beliefs." YouTube. https://www.youtube.com/watch?v=HZGCoVF3YvM
5. Gigerenzer, G. (2002). *Calculated Risks: How to Know When Numbers Deceive You*. Simon & Schuster.
6. McGrayne, S. B. (2011). *The Theory That Would Not Die: How Bayes' Rule Cracked the Enigma Code*. Yale University Press.
7. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
8. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media.
9. Python `random` module documentation. https://docs.python.org/3/library/random.html

---

*Bab berikutnya: **Bab 5 — Distribusi Probabilitas Diskret dan Kontinu***
