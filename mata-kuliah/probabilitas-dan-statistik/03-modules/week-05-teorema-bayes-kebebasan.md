# Minggu 5: Teorema Bayes dan Kebebasan

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 5 |
| **Topik** | Hukum probabilitas total, Teorema Bayes, kebebasan, *base rate fallacy* |
| **CPL / CPMK** | CPL08 / CPMK081 |
| **Sub-CPMK** | `PS-Sub-CPMK081-1` |
| **Indikator Mingguan** | Menerapkan Teorema Bayes dan menganalisis kebebasan kejadian pada kasus computing |
| **Level Bloom** | C3–C4 (Menerapkan–Menganalisis) |
| **Durasi** | 150 menit tatap muka |
| **Metode** | Kuliah, studi kasus, simulasi |

---

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menerapkan** (C3) hukum probabilitas total untuk menghitung probabilitas kejadian yang bergantung pada beberapa keadaan.
2. **Menerapkan** (C3) Teorema Bayes untuk memperbarui keyakinan berdasarkan bukti baru.
3. **Menganalisis** (C4) *base rate fallacy* dan menjelaskan mengapa tes yang akurat dapat menghasilkan banyak alarm palsu.
4. **Menentukan** (C4) apakah dua kejadian saling bebas berdasarkan definisi formal.
5. **Menjelaskan** (C2) cara kerja penyaring spam Naive Bayes sebagai penerapan langsung Teorema Bayes.

---

## Materi Pembelajaran

### 1. Hukum Probabilitas Total

#### 1.1 Gagasan Dasar

Kadang kita tidak bisa menghitung P(A) secara langsung, tetapi kita tahu P(A) dalam beberapa **keadaan** yang berbeda. Hukum probabilitas total menggabungkannya.

Bila B₁, B₂, …, Bₖ adalah **partisi** ruang sampel (saling lepas dan gabungannya seluruh S):

$$P(A) = \sum_{i=1}^{k} P(B_i) \cdot P(A \mid B_i)$$

```
            S dipartisi menjadi B₁, B₂, B₃
   ┌──────────┬──────────┬──────────┐
   │   B₁     │   B₂     │   B₃     │
   │  ▓▓▓     │   ▓▓▓▓▓  │  ▓       │  ▓ = bagian yang juga A
   └──────────┴──────────┴──────────┘

   P(A) = P(B₁)P(A|B₁) + P(B₂)P(A|B₂) + P(B₃)P(A|B₃)
```

#### 1.2 Contoh: Tingkat Kegagalan Deployment

> Sebuah tim melakukan *deployment* dari tiga jalur: 50% lewat pipeline CI otomatis, 30% lewat *manual deploy* terjadwal, 20% lewat *hotfix* darurat.
> Tingkat kegagalan masing-masing: 2%, 8%, dan 25%.
>
> Berapa probabilitas sebuah *deployment* acak gagal?

$$P(\text{gagal}) = 0{,}50(0{,}02) + 0{,}30(0{,}08) + 0{,}20(0{,}25) = 0{,}01 + 0{,}024 + 0{,}05 = 0{,}084$$

```python
jalur = {
    "CI otomatis":      {"proporsi": 0.50, "p_gagal": 0.02},
    "Manual terjadwal": {"proporsi": 0.30, "p_gagal": 0.08},
    "Hotfix darurat":   {"proporsi": 0.20, "p_gagal": 0.25},
}

p_gagal_total = sum(d["proporsi"] * d["p_gagal"] for d in jalur.values())
print(f"P(deployment gagal) = {p_gagal_total:.4f}  ({p_gagal_total*100:.2f}%)")

print("\nKontribusi tiap jalur terhadap total kegagalan:")
for nama, d in jalur.items():
    kontribusi = d["proporsi"] * d["p_gagal"]
    print(f"  {nama:18s}: {kontribusi:.4f}  "
          f"({kontribusi/p_gagal_total*100:5.1f}% dari semua kegagalan)")
```

> Perhatikan hasilnya: **hotfix darurat hanya 20% dari deployment, tetapi menyumbang 59,5% dari seluruh kegagalan.** Inilah jenis wawasan yang tidak terlihat dari angka kasar, dan yang membuat probabilitas berguna dalam rekayasa perangkat lunak.

---

### 2. Teorema Bayes

#### 2.1 Rumus

$$P(B_i \mid A) = \frac{P(B_i) \cdot P(A \mid B_i)}{P(A)} = \frac{P(B_i) \cdot P(A \mid B_i)}{\sum_{j} P(B_j) \cdot P(A \mid B_j)}$$

Dalam bentuk paling sederhana:

$$P(H \mid E) = \frac{P(H) \cdot P(E \mid H)}{P(E)}$$

| Istilah | Lambang | Makna |
|---------|---------|-------|
| **Prior** | P(H) | Keyakinan **sebelum** melihat bukti |
| **Likelihood** | P(E\|H) | Seberapa mungkin bukti muncul bila hipotesis benar |
| **Evidence** | P(E) | Probabilitas bukti muncul secara keseluruhan |
| **Posterior** | P(H\|E) | Keyakinan **setelah** melihat bukti |

> **Inti gagasannya:** Teorema Bayes adalah mesin untuk **memperbarui keyakinan secara rasional ketika bukti baru datang**. Prior masuk, bukti diproses, posterior keluar. Posterior hari ini menjadi prior esok hari.

#### 2.2 Membalik Arah Persyaratan

Teorema Bayes pada dasarnya menjawab satu kebutuhan: kita **punya** P(E|H) tetapi **butuh** P(H|E).

```
   Yang kita TAHU (dari uji laboratorium):
     P(tes positif | benar-benar sakit) = 0,99     ← likelihood

   Yang kita BUTUHKAN (sebagai pasien):
     P(benar-benar sakit | tes positif) = ?        ← posterior

   Keduanya SANGAT BERBEDA. Teorema Bayes menjembataninya.
```

#### 2.3 Contoh Lengkap: Deteksi Penipuan Transaksi

> Sistem deteksi penipuan sebuah bank memiliki spesifikasi:
> - **Sensitivitas:** 98% transaksi penipuan berhasil ditandai.
> - **Spesifisitas:** 97% transaksi normal tidak ditandai (alarm palsu 3%).
> - **Prevalensi:** 0,4% dari seluruh transaksi adalah penipuan.
>
> Sebuah transaksi ditandai sistem. **Berapa probabilitas transaksi itu benar-benar penipuan?**

Banyak orang menjawab "sekitar 98%". Mari kita hitung.

$$P(\text{tandai}) = \underbrace{0{,}004 \times 0{,}98}_{\text{penipuan ditandai}} + \underbrace{0{,}996 \times 0{,}03}_{\text{alarm palsu}} = 0{,}00392 + 0{,}02988 = 0{,}0338$$

$$P(\text{penipuan} \mid \text{tandai}) = \frac{0{,}00392}{0{,}0338} = 0{,}116$$

**Hanya 11,6%.** Hampir sembilan dari sepuluh alarm adalah alarm palsu.

```python
def bayes_diagnostik(prevalensi, sensitivitas, spesifisitas, nama="kondisi"):
    """Menghitung nilai prediktif positif dan negatif dari sebuah tes.

    prevalensi   : P(kondisi) sebelum tes  — prior
    sensitivitas : P(tes positif | kondisi ada)
    spesifisitas : P(tes negatif | kondisi tidak ada)
    """
    p_ada = prevalensi
    p_tidak = 1 - prevalensi

    # Empat kemungkinan
    benar_positif  = p_ada * sensitivitas
    salah_negatif  = p_ada * (1 - sensitivitas)
    salah_positif  = p_tidak * (1 - spesifisitas)
    benar_negatif  = p_tidak * spesifisitas

    p_positif = benar_positif + salah_positif
    p_negatif = salah_negatif + benar_negatif

    ppv = benar_positif / p_positif      # nilai prediktif positif
    npv = benar_negatif / p_negatif      # nilai prediktif negatif

    print(f"=== {nama.upper()} ===")
    print(f"Prevalensi (prior)        : {prevalensi:.4f}")
    print(f"Sensitivitas              : {sensitivitas:.4f}")
    print(f"Spesifisitas              : {spesifisitas:.4f}")
    print(f"\nDari 100.000 kasus:")
    print(f"  Benar positif  : {benar_positif*100000:>8.0f}")
    print(f"  Salah positif  : {salah_positif*100000:>8.0f}  ← alarm palsu")
    print(f"  Salah negatif  : {salah_negatif*100000:>8.0f}  ← terlewat")
    print(f"  Benar negatif  : {benar_negatif*100000:>8.0f}")
    print(f"\nP({nama} | tes POSITIF) = {ppv:.4f}  ({ppv*100:.2f}%)")
    print(f"P(bukan | tes NEGATIF)  = {npv:.4f}  ({npv*100:.2f}%)")
    return ppv, npv

bayes_diagnostik(0.004, 0.98, 0.97, nama="penipuan")
```

#### 2.4 Mengapa Hasilnya Mengejutkan: *Base Rate Fallacy*

Kunci jawabannya ada pada **prevalensi yang sangat rendah**. Bayangkan 100.000 transaksi:

```
  100.000 transaksi
  ├── 400 penipuan (0,4%)
  │    ├── 392 ditandai   ✓ benar positif
  │    └──   8 lolos      ✗ salah negatif
  └── 99.600 normal (99,6%)
       ├── 2.988 ditandai ✗ ALARM PALSU
       └── 96.612 lolos   ✓ benar negatif

  Total yang ditandai = 392 + 2.988 = 3.380
  Yang benar-benar penipuan = 392 / 3.380 = 11,6%
```

Meskipun tingkat alarm palsu hanya 3%, **3% dari kelompok yang sangat besar** menghasilkan lebih banyak alarm palsu daripada seluruh kasus penipuan yang ada.

> ***Base rate fallacy*** adalah kecenderungan mengabaikan prevalensi (*base rate*) dan hanya memperhatikan akurasi tes. Ini bukan sekadar kuriositas akademis — ini adalah kesalahan penalaran yang menyebabkan diagnosis medis salah, penangkapan keliru berbasis pengenalan wajah, dan sistem keamanan yang diabaikan karena terlalu sering berteriak serigala.

#### 2.5 Pengaruh Prevalensi

```python
import numpy as np
import matplotlib.pyplot as plt

sensitivitas, spesifisitas = 0.98, 0.97
prevalensi = np.linspace(0.0005, 0.5, 300)

bp = prevalensi * sensitivitas
sp = (1 - prevalensi) * (1 - spesifisitas)
ppv = bp / (bp + sp)

plt.figure(figsize=(10, 5.5))
plt.plot(prevalensi * 100, ppv * 100, linewidth=2.2, color="steelblue")
plt.axhline(50, color="gray", linestyle=":", linewidth=1)
plt.axvline(0.4, color="#c0392b", linestyle="--", linewidth=1.5,
            label="Kasus penipuan (0,4%)")
plt.xlabel("Prevalensi kondisi (%)")
plt.ylabel("P(kondisi benar ada | tes positif)  (%)")
plt.title("Tes yang sama (sensitivitas 98%, spesifisitas 97%)\n"
          "menghasilkan kepercayaan yang sangat berbeda tergantung prevalensi")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

for p in [0.001, 0.004, 0.01, 0.05, 0.10, 0.30, 0.50]:
    bp_ = p * sensitivitas
    sp_ = (1 - p) * (1 - spesifisitas)
    print(f"Prevalensi {p*100:5.1f}%  →  PPV = {bp_/(bp_+sp_)*100:5.1f}%")
```

> **Pelajaran untuk perancang sistem:** menaikkan akurasi model saja tidak cukup bila kejadian yang dicari sangat langka. Anda juga harus menaikkan **spesifisitas** secara drastis, atau menerima bahwa sebagian besar alarm akan palsu dan merancang alur kerja manusia yang sanggup menanganinya. Ini akan Anda temui lagi di Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (Semester 5).

---

### 3. Kebebasan Dua Kejadian

#### 3.1 Definisi Formal

Dua kejadian A dan B disebut **saling bebas** (*independent*) bila:

$$P(A \cap B) = P(A) \cdot P(B)$$

Setara dengan: P(A|B) = P(A), artinya **mengetahui B tidak mengubah keyakinan kita tentang A**.

#### 3.2 Bebas ≠ Saling Lepas

Ini dua hal yang sering tertukar.

| Sifat | Definisi | Makna Intuitif |
|-------|----------|----------------|
| **Saling lepas** (*mutually exclusive*) | P(A ∩ B) = 0 | Tidak mungkin terjadi bersamaan |
| **Saling bebas** (*independent*) | P(A ∩ B) = P(A)P(B) | Satu tidak memengaruhi yang lain |

> **Fakta yang penting:** dua kejadian dengan probabilitas tak nol yang **saling lepas** justru **tidak mungkin saling bebas**. Sebab bila A terjadi, kita jadi tahu pasti B tidak terjadi — itu jelas memengaruhi.

```python
# Contoh: kejadian saling lepas TIDAK bebas
p_status_200 = 0.90
p_status_404 = 0.06
# Saling lepas: satu permintaan tidak bisa berstatus 200 dan 404 sekaligus
p_irisan = 0.0

print("Saling lepas? ", p_irisan == 0)
print("Saling bebas? ", abs(p_irisan - p_status_200 * p_status_404) < 1e-12)
print(f"  P(A)P(B) = {p_status_200 * p_status_404:.4f}, tetapi P(A∩B) = {p_irisan}")
print("  → Saling lepas, TETAPI TIDAK bebas.")
```

#### 3.3 Menguji Kebebasan pada Data Nyata

```python
import pandas as pd

df = pd.read_csv("nilai_mahasiswa_if.csv")

# Apakah "kelas" dan "lulus UAS (≥60)" saling bebas?
df["lulus_uas"] = df["nilai_uas"] >= 60

tabel = pd.crosstab(df["kelas"], df["lulus_uas"])
print("Tabel kontingensi:")
print(tabel)

n = len(df)
p_if26a   = (df["kelas"] == "IF26A").mean()
p_lulus   = df["lulus_uas"].mean()
p_irisan  = ((df["kelas"] == "IF26A") & df["lulus_uas"]).mean()

print(f"\nP(IF26A)           = {p_if26a:.4f}")
print(f"P(lulus)           = {p_lulus:.4f}")
print(f"P(IF26A) × P(lulus)= {p_if26a * p_lulus:.4f}")
print(f"P(IF26A ∩ lulus)   = {p_irisan:.4f}")
print(f"Selisih            = {abs(p_irisan - p_if26a*p_lulus):.4f}")
```

> **Peringatan:** selisih kecil pada data sampel **tidak membuktikan** kebebasan. Selisih itu bisa saja kebetulan sampel. Menguji kebebasan secara formal memerlukan **uji chi-square kebebasan** — materi Minggu 13.

#### 3.4 Kebebasan Berganda dan Keandalan Sistem

Bila n komponen bekerja **secara bebas**, masing-masing dengan keandalan r:

$$P(\text{seluruhnya bekerja}) = r^n \qquad P(\text{sedikitnya satu bekerja}) = 1 - (1-r)^n$$

```python
def keandalan_sistem(r_komponen, n, susunan="seri"):
    """Menghitung keandalan sistem seri atau paralel dari komponen bebas."""
    if susunan == "seri":     # semua harus bekerja
        return r_komponen ** n
    else:                     # paralel: cukup satu bekerja
        return 1 - (1 - r_komponen) ** n

r = 0.99   # keandalan satu server: 99%

print("Susunan SERI (semua harus hidup — misalnya rantai layanan):")
for n in [1, 2, 3, 5, 10]:
    print(f"  {n:2d} komponen: {keandalan_sistem(r, n, 'seri')*100:.4f}%")

print("\nSusunan PARALEL (cukup satu hidup — misalnya replika):")
for n in [1, 2, 3, 5]:
    print(f"  {n:2d} komponen: {keandalan_sistem(r, n, 'paralel')*100:.6f}%")
```

> **Wawasan rekayasa:** menambah komponen pada susunan **seri menurunkan** keandalan (rantai sekuat mata rantai terlemah), sedangkan pada susunan **paralel menaikkannya** secara dramatis. Sepuluh layanan yang masing-masing andal 99% dan harus semuanya hidup hanya memberi keandalan 90,4%.
>
> **Catatan penting:** perhitungan ini mengandaikan komponen **benar-benar bebas**. Pada kenyataannya, replika yang berada di satu pusat data akan mati bersamaan bila listrik padam — *correlated failure*. Asumsi kebebasan yang keliru adalah penyebab banyak kegagalan sistem besar.

---

### 4. Penerapan: Penyaring Spam Naive Bayes

#### 4.1 Gagasannya

Untuk sebuah pesan berisi kata-kata w₁, w₂, …, wₙ:

$$P(\text{spam} \mid w_1,\ldots,w_n) \propto P(\text{spam}) \times \prod_{i=1}^{n} P(w_i \mid \text{spam})$$

Disebut *naive* karena mengandaikan setiap kata **saling bebas** bila kelasnya diketahui — asumsi yang jelas tidak benar (kata "gratis" dan "hadiah" cenderung muncul bersama), tetapi ternyata bekerja sangat baik dalam praktik.

#### 4.2 Implementasi Sederhana

```python
from collections import Counter
import math

def latih_naive_bayes(dokumen, label):
    """Melatih penyaring Naive Bayes sederhana dengan penghalusan Laplace."""
    kelas = set(label)
    prior, likelihood, kosakata = {}, {}, set()

    for k in kelas:
        teks_kelas = [d for d, l in zip(dokumen, label) if l == k]
        prior[k] = len(teks_kelas) / len(dokumen)

        kata = [w for d in teks_kelas for w in d.lower().split()]
        kosakata.update(kata)
        likelihood[k] = Counter(kata)

    return prior, likelihood, kosakata

def klasifikasi(pesan, prior, likelihood, kosakata):
    """Mengklasifikasi pesan; memakai log agar tidak underflow."""
    skor = {}
    for k in prior:
        total_kata = sum(likelihood[k].values())
        log_p = math.log(prior[k])
        for w in pesan.lower().split():
            # Penghalusan Laplace: +1 agar kata baru tidak membuat probabilitas nol
            p_kata = (likelihood[k][w] + 1) / (total_kata + len(kosakata))
            log_p += math.log(p_kata)
        skor[k] = log_p
    return max(skor, key=skor.get), skor

# Data latih kecil berbahasa Indonesia
dokumen = [
    "selamat anda memenangkan hadiah gratis klik sekarang",
    "promo gratis diskon besar klik tautan ini sekarang",
    "menangkan hadiah undian gratis segera daftar",
    "rapat proyek besok pukul sembilan di ruang lab",
    "tolong kirim laporan praktikum sebelum jumat",
    "jadwal kuliah statistika pindah ke ruang 301",
]
label = ["spam", "spam", "spam", "ham", "ham", "ham"]

prior, likelihood, kosakata = latih_naive_bayes(dokumen, label)

uji = [
    "gratis hadiah klik sekarang",
    "laporan praktikum statistika besok",
]
for pesan in uji:
    hasil, skor = klasifikasi(pesan, prior, likelihood, kosakata)
    print(f"\nPesan  : \"{pesan}\"")
    print(f"Prediksi: {hasil.upper()}")
    print(f"  log P(spam) = {skor['spam']:.3f} | log P(ham) = {skor['ham']:.3f}")
```

> Pada Semester 5, mata kuliah **Dasar Kecerdasan Artifisial dan Pembelajaran Mesin** akan memakai `sklearn.naive_bayes.MultinomialNB` — yang di dalamnya persis menjalankan perhitungan ini. Memahami mekanismenya sekarang berarti Anda kelak memanggil fungsi itu dengan sadar, bukan sebagai kotak hitam.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (Mandiri — 60 menit)

1. Membaca [Bab 5 buku ajar](../06-buku-ajar/bab-05-probabilitas-bersyarat-bayes.md).
2. Menjawab dugaan awal (tanpa menghitung): *"Sebuah tes penyakit akurat 99%. Anda dites dan hasilnya positif. Menurut Anda, berapa persen kemungkinan Anda benar-benar sakit?"* Tuliskan jawabannya, nanti dibandingkan dengan hasil hitungan di kelas.

### Di Kelas (150 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10' | Mengumpulkan dugaan awal mahasiswa, dicatat di papan |
| 10–35' | Kuliah: hukum probabilitas total; kasus tingkat kegagalan deployment |
| 35–65' | Kuliah: Teorema Bayes; prior–likelihood–posterior |
| 65–75' | Istirahat |
| 75–105' | **Studi kasus:** hitung bersama kasus tes penyakit, bandingkan dengan dugaan awal di papan |
| 105–125' | Kuliah: kebebasan vs saling lepas; keandalan sistem seri dan paralel |
| 125–145' | Demo: penyaring spam Naive Bayes sederhana |
| 145–150' | **Kuis 2** (Minggu 4–5) |

> **Catatan:** Kuis 2 dilaksanakan pada pertemuan ini, bobot 3,75%, menelusuri ke `PS-Sub-CPMK081-1`.

#### Studi Kasus Utama: Tes Penyakit Langka

> Sebuah penyakit menjangkiti 1 dari 1.000 orang. Tes diagnostiknya memiliki sensitivitas 99% dan spesifisitas 99%. Seseorang dites, hasilnya positif.

1. Hitung P(sakit | tes positif) dengan Teorema Bayes.
2. Bandingkan dengan dugaan awal yang dicatat di papan.
3. Gambarkan diagram pohon dari 100.000 orang.
4. **Diskusi:** apa implikasinya bila program skrining massal diterapkan pada seluruh penduduk?
5. **Diskusi lanjutan:** bagaimana bila tes hanya diberikan kepada orang yang sudah menunjukkan gejala? (Petunjuk: prevalensi pada kelompok bergejala jauh lebih tinggi.)

### Setelah Kelas (Mandiri — 180 menit)

1. Mengerjakan [Lab 05](../04-labs/lab-05-bayes-penyaring-spam.md).
2. Mengerjakan Latihan Soal Bab 5.
3. **Menyelesaikan proposal proyek — dikumpulkan Minggu 6.**

---

## Penugasan

| Kode | Tugas | Bobot | Batas Waktu |
|------|-------|-------|-------------|
| T-05 | Laporan Lab 05 — Teorema Bayes dan penyaring spam | 1,92% | Sebelum kelas Minggu 6 |
| K-02 | Kuis 2 — Minggu 4–5 | 3,75% | Di kelas Minggu 5 |
| P-00 | **Proposal proyek** | Syarat wajib | Sebelum kelas Minggu 6 |

---

## Rangkuman

1. **Hukum probabilitas total** menggabungkan probabilitas dari beberapa keadaan yang mempartisi ruang sampel.
2. **Teorema Bayes** membalik arah persyaratan: dari P(E|H) yang kita punya menjadi P(H|E) yang kita butuhkan.
3. Empat istilahnya: **prior** (keyakinan awal), **likelihood** (kecocokan bukti), **evidence** (normalisasi), dan **posterior** (keyakinan setelah bukti).
4. ***Base rate fallacy*** — mengabaikan prevalensi — menyebabkan tes yang akurat 98–99% tetap menghasilkan mayoritas alarm palsu bila kejadiannya langka.
5. Pada prevalensi rendah, **menaikkan spesifisitas jauh lebih berpengaruh** daripada menaikkan sensitivitas.
6. **Saling lepas ≠ saling bebas.** Dua kejadian berpeluang tak nol yang saling lepas justru pasti tidak bebas.
7. **Keandalan sistem seri menurun** seiring bertambahnya komponen; **paralel meningkat**. Asumsi kebebasan yang keliru (*correlated failure*) adalah penyebab umum kegagalan sistem besar.
8. **Naive Bayes** adalah penerapan langsung Teorema Bayes dengan asumsi kebebasan antar kata — asumsi yang salah tetapi berguna.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 2.7–2.8. Pearson.
2. Downey, A. B. (2013). *Think Bayes*. O'Reilly Media.
3. Kahneman, D., & Tversky, A. (1973). On the psychology of prediction. *Psychological Review*, 80(4), 237–251.
4. Gigerenzer, G. (2002). *Calculated Risks: How to Know When Numbers Deceive You*. Simon & Schuster.
5. Ross, S. M. (2019). *A First Course in Probability* (10th ed.), Bab 3. Pearson.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
