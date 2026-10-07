# Minggu 2: Statistika Deskriptif — Pemusatan, Penyebaran, dan Posisi

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 2 |
| **Topik** | Ukuran pemusatan, penyebaran, dan posisi; deteksi pencilan; kemencengan |
| **CPL / CPMK** | CPL10 / CPMK102 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Indikator Mingguan** | Menghitung dan menafsirkan ukuran pemusatan, penyebaran, dan posisi pada data nyata |
| **Level Bloom** | C3 (Menerapkan) |
| **Durasi** | 150 menit tatap muka |
| **Metode** | Kuliah, latihan terbimbing, komputasi dengan pandas |

---

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menghitung** (C3) mean, median, dan modus secara manual maupun dengan pandas, serta **menentukan** (C4) mana yang tepat untuk sebuah sebaran data.
2. **Menghitung** (C3) range, varians, simpangan baku, dan koefisien variasi, serta **menjelaskan** (C2) perbedaan rumus populasi dan sampel.
3. **Menghitung** (C3) kuartil, persentil, dan IQR, serta **mengidentifikasi** (C3) pencilan dengan aturan 1,5×IQR.
4. **Menafsirkan** (C4) kemencengan sebuah sebaran dan kaitannya dengan pemilihan ukuran pemusatan.
5. **Menerapkan** (C3) seluruh ukuran tersebut pada dataset nyata berkonteks Informatika.

---

## Materi Pembelajaran

### 1. Ukuran Pemusatan

#### 1.1 Mean (Rata-Rata Aritmetik)

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i \qquad \mu = \frac{1}{N}\sum_{i=1}^{N} x_i$$

Mean adalah **titik keseimbangan** sebuah sebaran. Bayangkan data sebagai beban di atas penggaris: mean adalah titik tumpu agar penggaris seimbang.

```
   Data: 2, 3, 3, 4, 8        Mean = 20/5 = 4

   2   3 3   4       8
   ●   ● ●   ●       ●
   ├───┼─┼───┼───────┤
   0   2 3   4   6   8
             ▲
             mean = 4
```

Sifat penting: **mean sangat peka terhadap nilai ekstrem**. Ubah nilai 8 menjadi 80, dan mean melompat dari 4 ke 18,4 — padahal empat nilai lainnya tidak berubah sama sekali.

#### 1.2 Median (Nilai Tengah)

Median adalah nilai yang membagi data terurut menjadi dua bagian sama banyak.

```python
def median_manual(data):
    """Menghitung median secara manual untuk menunjukkan prosedurnya."""
    d = sorted(data)
    n = len(d)
    tengah = n // 2
    if n % 2 == 1:                      # ganjil: ambil yang di tengah
        return d[tengah]
    else:                               # genap: rata-rata dua nilai tengah
        return (d[tengah - 1] + d[tengah]) / 2

print(median_manual([2, 3, 3, 4, 8]))    # 3
print(median_manual([2, 3, 3, 4, 8, 80]))  # 3.5
```

Perhatikan: mengubah 8 menjadi 80 hanya menggeser median dari 3 ke 3,5. **Median tahan terhadap nilai ekstrem** — sifat yang disebut *robust*.

#### 1.3 Modus

Nilai yang paling sering muncul. Satu-satunya ukuran pemusatan yang sah untuk data **nominal**.

```python
import pandas as pd

bahasa = pd.Series(["Python", "Java", "Python", "C++", "Python", "Java"])
print(bahasa.mode())        # Python
print(bahasa.value_counts())
```

Sebaran bisa **tidak bermodus** (semua nilai muncul sekali), **bermodus satu**, atau **bermodus dua/lebih** — yang terakhir sering menandakan ada dua kelompok berbeda tercampur dalam satu data.

#### 1.4 Memilih Ukuran Pemusatan

| Situasi | Ukuran yang Tepat | Alasan |
|---------|-------------------|--------|
| Data simetris tanpa pencilan | Mean | Memakai seluruh informasi |
| Data menceng atau ada pencilan | **Median** | Tidak terseret nilai ekstrem |
| Data nominal | Modus | Satu-satunya yang bermakna |
| Data ordinal | Median atau modus | Mean tidak sah |
| Waktu respons sistem | **Median dan persentil ke-95** | Sebaran hampir selalu menceng kanan |

> **Kasus nyata Informatika.** Laporan kinerja API yang hanya menyebut rata-rata waktu respons menyembunyikan penderitaan pengguna. Bila 95% permintaan selesai dalam 100 ms tetapi 5% memakan 8 detik, rata-ratanya mungkin hanya 495 ms — terdengar baik-baik saja. Karena itu industri melaporkan **p50, p95, dan p99**, bukan mean.

```python
import numpy as np

# Waktu respons API dalam milidetik (menceng kanan, seperti kenyataan)
waktu = np.array([95, 98, 102, 88, 105, 97, 101, 93, 99, 8200])

print(f"Mean   : {waktu.mean():.1f} ms")          # terseret nilai 8200
print(f"Median : {np.median(waktu):.1f} ms")      # tahan
print(f"p95    : {np.percentile(waktu, 95):.1f} ms")
print(f"p99    : {np.percentile(waktu, 99):.1f} ms")
```

---

### 2. Ukuran Penyebaran

Dua kelompok data bisa punya mean yang sama persis tetapi karakter yang sama sekali berbeda.

```
  Kelompok A: 49, 50, 50, 51, 50        mean = 50, konsisten
  Kelompok B: 10, 90, 50, 20, 80        mean = 50, kacau
```

Kalau kelompok A dan B adalah waktu respons dua server, server mana yang Anda pilih? Mean tidak bisa menjawab. **Penyebaran-lah yang menjawab.**

#### 2.1 Range

$$\text{Range} = x_{\max} - x_{\min}$$

Paling sederhana, tetapi hanya memakai dua nilai dan sangat peka pencilan.

#### 2.2 Varians dan Simpangan Baku

$$s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1} \qquad \sigma^2 = \frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N}$$

$$s = \sqrt{s^2} \qquad \sigma = \sqrt{\sigma^2}$$

**Mengapa dikuadratkan?** Karena jumlah simpangan biasa selalu nol — simpangan positif dan negatif saling meniadakan. Mengkuadratkan membuat semuanya positif sekaligus memberi bobot lebih pada simpangan besar.

**Mengapa penyebut sampel adalah n−1, bukan n?** Ini disebut **koreksi Bessel**. Karena x̄ dihitung dari data yang sama, simpangan terhadap x̄ cenderung sedikit lebih kecil daripada simpangan terhadap μ yang sebenarnya. Membagi dengan n−1 (bukan n) mengoreksi kecenderungan meremehkan itu, sehingga s² menjadi **penduga tak bias** bagi σ².

```python
import numpy as np

data = np.array([49, 50, 50, 51, 50])

# PENTING: NumPy default ddof=0 (rumus populasi)
print(f"Varians populasi (ddof=0) : {data.var():.4f}")
print(f"Varians sampel   (ddof=1) : {data.var(ddof=1):.4f}")

# pandas default ddof=1 (rumus sampel) — KEBALIKAN dari NumPy
import pandas as pd
s = pd.Series(data)
print(f"pandas .var()  (ddof=1)   : {s.var():.4f}")
```

> **Jebakan yang sering menjatuhkan mahasiswa.** `numpy.var()` memakai `ddof=0`, sedangkan `pandas.Series.var()` memakai `ddof=1`. Hasilnya berbeda, dan keduanya "benar" untuk konteksnya masing-masing. Selalu tanyakan: **data ini populasi atau sampel?**

#### 2.3 Koefisien Variasi

$$CV = \frac{s}{\bar{x}} \times 100\%$$

Ukuran penyebaran **relatif** — berguna membandingkan variabilitas dua kelompok dengan satuan atau skala berbeda.

```python
# Membandingkan konsistensi dua layanan dengan skala berbeda
api_a = np.array([100, 105, 98, 102, 95])       # milidetik
api_b = np.array([2.1, 2.3, 1.9, 2.2, 2.0])     # detik

for nama, d in [("API A (ms)", api_a), ("API B (s)", api_b)]:
    cv = d.std(ddof=1) / d.mean() * 100
    print(f"{nama:12s} mean={d.mean():7.2f}  s={d.std(ddof=1):6.3f}  CV={cv:5.2f}%")
```

Meski simpangan baku API A jauh lebih besar secara angka, CV menunjukkan **konsistensi relatif** keduanya dapat dibandingkan secara adil.

---

### 3. Ukuran Posisi

#### 3.1 Kuartil dan Persentil

```
  Data terurut:
  │←── 25% ──→│←── 25% ──→│←── 25% ──→│←── 25% ──→│
  min         Q1          Q2          Q3         max
                        (median)
              │←──────── IQR ────────→│
```

| Ukuran | Makna |
|--------|-------|
| Q1 (persentil 25) | 25% data berada di bawah nilai ini |
| Q2 (persentil 50) | Median |
| Q3 (persentil 75) | 75% data berada di bawah nilai ini |
| IQR = Q3 − Q1 | Rentang 50% data di tengah — ukuran penyebaran yang *robust* |

```python
import numpy as np

waktu = np.array([88, 93, 95, 97, 98, 99, 101, 102, 105, 8200])

q1, q2, q3 = np.percentile(waktu, [25, 50, 75])
iqr = q3 - q1

print(f"Q1  = {q1:.2f}")
print(f"Q2  = {q2:.2f}  (median)")
print(f"Q3  = {q3:.2f}")
print(f"IQR = {iqr:.2f}")
```

#### 3.2 Deteksi Pencilan dengan Aturan 1,5×IQR

$$\text{Batas bawah} = Q_1 - 1{,}5 \times IQR \qquad \text{Batas atas} = Q_3 + 1{,}5 \times IQR$$

Nilai di luar batas tersebut ditandai sebagai **kandidat pencilan**.

```python
def deteksi_pencilan(data):
    """Mendeteksi pencilan dengan aturan 1,5 x IQR.

    Mengembalikan batas bawah, batas atas, dan nilai-nilai pencilan.
    """
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    batas_bawah = q1 - 1.5 * iqr
    batas_atas = q3 + 1.5 * iqr
    pencilan = data[(data < batas_bawah) | (data > batas_atas)]
    return batas_bawah, batas_atas, pencilan

bb, ba, outlier = deteksi_pencilan(waktu)
print(f"Batas wajar : [{bb:.2f} , {ba:.2f}]")
print(f"Pencilan    : {outlier}")
```

> **Peringatan etis yang penting.** Kata "pencilan" **bukan** izin untuk membuang data. Nilai 8200 ms itu mungkin justru temuan paling berharga — barangkali ada *query* yang tidak terindeks, atau *timeout* jaringan yang nyata dialami pengguna. Membuang pencilan hanya sah bila ada **alasan substantif** (misalnya terbukti kesalahan pencatatan), bukan karena grafiknya jadi lebih rapi.
>
> Dalam mata kuliah ini, membuang pencilan tanpa penjelasan pada laporan proyek **mengurangi nilai** pada aspek validitas interpretasi.

---

### 4. Bentuk Sebaran: Kemencengan

**Kemencengan (*skewness*)** menggambarkan ketidaksimetrisan sebuah sebaran.

```
   MENCENG KIRI          SIMETRIS           MENCENG KANAN
   (negatif)                                (positif)

        ▄▄█                 ▄█▄                █▄▄
      ▄███│               ▄███▄                │███▄
    ▄█████│             ▄█████▄                │█████▄
   ───────┼──         ──────┼──────          ──┼───────
   mean median         mean=median=modus      median mean
   <median             berimpit               <mean

   contoh: nilai ujian  contoh: tinggi badan   contoh: waktu respons,
   yang mudah                                   gaji, ukuran berkas
```

**Aturan praktis hubungan mean–median:**

| Kondisi | Bentuk |
|---------|--------|
| mean ≈ median | Simetris |
| mean > median | Menceng kanan (ada ekor panjang ke kanan) |
| mean < median | Menceng kiri |

```python
from scipy import stats
import numpy as np

# Data waktu respons: hampir selalu menceng kanan
np.random.seed(42)
waktu = np.random.exponential(scale=120, size=1000)

print(f"Mean       : {waktu.mean():.2f}")
print(f"Median     : {np.median(waktu):.2f}")
print(f"Kemencengan: {stats.skew(waktu):.3f}")

if stats.skew(waktu) > 0.5:
    print("→ Menceng kanan. Gunakan MEDIAN sebagai ukuran pemusatan.")
elif stats.skew(waktu) < -0.5:
    print("→ Menceng kiri. Gunakan MEDIAN.")
else:
    print("→ Cukup simetris. Mean dapat dipakai.")
```

> **Mengapa waktu respons hampir selalu menceng kanan?** Karena ada batas bawah alami (tidak mungkin negatif, dan ada waktu minimum pemrosesan) tetapi tidak ada batas atas — permintaan bisa saja tertahan sangat lama. Sebaran dengan batas bawah tegas dan ekor atas bebas selalu menceng kanan. Pola yang sama berlaku untuk ukuran berkas, jumlah pengikut, dan penghasilan.

---

### 5. Menerapkan Semuanya: Analisis Deskriptif Lengkap

```python
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("nilai_mahasiswa_if.csv")

def ringkasan_deskriptif(seri, nama):
    """Menghasilkan ringkasan deskriptif lengkap beserta rekomendasi."""
    q1, q3 = seri.quantile([0.25, 0.75])
    iqr = q3 - q1
    kemencengan = stats.skew(seri.dropna())

    print(f"\n{'='*52}")
    print(f"  {nama}")
    print('='*52)
    print(f"  n              : {seri.count()}")
    print(f"  Mean           : {seri.mean():.2f}")
    print(f"  Median         : {seri.median():.2f}")
    print(f"  Modus          : {seri.mode().tolist()}")
    print(f"  Simpangan baku : {seri.std():.2f}   (ddof=1, rumus sampel)")
    print(f"  Koef. variasi  : {seri.std()/seri.mean()*100:.2f}%")
    print(f"  Min – Max      : {seri.min():.2f} – {seri.max():.2f}")
    print(f"  Q1 / Q3 / IQR  : {q1:.2f} / {q3:.2f} / {iqr:.2f}")
    print(f"  Kemencengan    : {kemencengan:.3f}")

    # Rekomendasi otomatis
    if abs(kemencengan) < 0.5:
        print("  → Sebaran cukup simetris; MEAN layak dipakai.")
    else:
        arah = "kanan" if kemencengan > 0 else "kiri"
        print(f"  → Menceng {arah}; gunakan MEDIAN dan IQR.")

    pencilan = seri[(seri < q1 - 1.5*iqr) | (seri > q3 + 1.5*iqr)]
    print(f"  Kandidat pencilan: {len(pencilan)} nilai")
    if len(pencilan) > 0:
        print(f"     → {sorted(pencilan.tolist())[:8]}")
        print("     JANGAN dibuang tanpa alasan substantif.")

for kolom in ["nilai_uts", "nilai_uas", "jam_belajar"]:
    ringkasan_deskriptif(df[kolom], kolom)
```

#### Analisis per Kelompok

```python
# Membandingkan dua kelas
print(df.groupby("kelas")[["nilai_uts", "nilai_uas", "jam_belajar"]].agg(
    ["count", "mean", "median", "std"]
).round(2))

# Membandingkan berdasarkan asal sekolah
print("\nJam belajar menurut asal sekolah:")
print(df.groupby("asal_sekolah")["jam_belajar"].describe().round(2))
```

> **Pertanyaan yang harus muncul di benak Anda:** bila rata-rata nilai IF26A lebih tinggi dari IF26H, apakah itu berarti kelas IF26A benar-benar lebih baik? **Belum tentu.** Selisih itu bisa saja kebetulan sampel. Menjawabnya memerlukan **uji hipotesis dua sampel** — dan itu materi Minggu 12. Untuk sekarang, cukup sadari bahwa statistika deskriptif **hanya menggambarkan, tidak menyimpulkan**.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (Mandiri — 60 menit)

1. Membaca [Bab 2 buku ajar](../06-buku-ajar/bab-02-statistika-deskriptif.md).
2. Menghitung secara manual (tanpa komputer) mean, median, dan simpangan baku dari data: `12, 15, 11, 14, 13, 45, 12`.
3. Menuliskan dugaan: mengapa nilai 45 mengubah mean jauh lebih besar daripada median?

### Di Kelas (150 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10' | Pembahasan singkat Lab 01 dan kesulitan yang muncul |
| 10–40' | Kuliah: ukuran pemusatan dan kapan masing-masing menyesatkan |
| 40–60' | **Latihan terbimbing:** hitung manual mean/median/modus, lalu verifikasi dengan pandas |
| 60–70' | Istirahat |
| 70–100' | Kuliah: varians, simpangan baku, koreksi Bessel, koefisien variasi |
| 100–125' | Kuliah + latihan: kuartil, IQR, deteksi pencilan, diskusi etika membuang pencilan |
| 125–145' | Studio: analisis deskriptif dataset `waktu_respons_server.csv` bersama-sama |
| 145–150' | Penutup, penjelasan Lab 02 |

#### Latihan Terbimbing: Verifikasi Manual vs Komputasi

Data waktu kompilasi proyek (detik): `42, 38, 45, 41, 39, 44, 40, 185`

1. Hitung manual: mean, median, range.
2. Hitung manual: varians sampel dan simpangan baku sampel.
3. Hitung manual: Q1, Q3, IQR, dan batas pencilan.
4. Verifikasi seluruhnya dengan Python.
5. **Diskusikan:** nilai 185 detik itu apa? Kompilasi pertama setelah *cache* dibersihkan? Kalau ya, bolehkah dibuang?

### Setelah Kelas (Mandiri — 180 menit)

1. Mengerjakan [Lab 02](../04-labs/lab-02-statistika-deskriptif-pandas.md).
2. Mengerjakan Latihan Soal Bab 2 ketiga tingkat.
3. Mendiskusikan calon tema proyek dengan kelompok.

---

## Penugasan

| Kode | Tugas | Bobot | Batas Waktu |
|------|-------|-------|-------------|
| T-02 | Laporan Lab 02 — Statistika deskriptif dengan pandas | 1,92% | Sebelum kelas Minggu 3 |

**Catatan khusus:** pada Lab 02, setiap ukuran yang dihitung **wajib disertai kalimat yang menjelaskan apa artinya bagi konteks data**. Notebook yang hanya berisi angka dinilai tidak lengkap.

---

## Rangkuman

1. **Mean** memakai seluruh data tetapi peka pencilan; **median** tahan pencilan; **modus** satu-satunya yang sah untuk data nominal.
2. Untuk data menceng — dan waktu respons, ukuran berkas, serta penghasilan hampir selalu menceng — **gunakan median**, bukan mean.
3. Industri melaporkan **p50, p95, p99** untuk kinerja sistem, bukan rata-rata, karena rata-rata menyembunyikan pengalaman buruk sebagian pengguna.
4. **Varians dan simpangan baku** mengukur penyebaran. Penyebut n−1 pada rumus sampel (koreksi Bessel) membuat s² menjadi penduga tak bias bagi σ².
5. `numpy.var()` memakai `ddof=0`; `pandas.var()` memakai `ddof=1`. **Selalu periksa** apakah data Anda populasi atau sampel.
6. **IQR** adalah ukuran penyebaran yang *robust*. Aturan 1,5×IQR menandai kandidat pencilan — **menandai, bukan memerintahkan membuang**.
7. **Kemencengan** menentukan pilihan ukuran pemusatan. Hubungan mean–median adalah petunjuk cepat arah kemencengan.
8. Statistika deskriptif **menggambarkan**, tidak menyimpulkan. Selisih rata-rata antar kelompok belum tentu nyata — itu urusan uji hipotesis (Minggu 12).

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 1.3–1.6. Pearson.
2. Bhattacharyya, G. K., & Johnson, R. A. (2019). *Statistics: Principles and Methods* (8th ed.), Bab 2. Wiley.
3. Downey, A. B. (2014). *Think Stats* (2nd ed.), Bab 2–3. O'Reilly Media.
4. Dokumentasi pandas — *Descriptive statistics*. <https://pandas.pydata.org/docs/user_guide/basics.html#descriptive-statistics>
5. Dokumentasi NumPy — *Statistics*. <https://numpy.org/doc/stable/reference/routines.statistics.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
