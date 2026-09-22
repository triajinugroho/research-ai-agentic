# BAB 2: STATISTIKA DESKRIPTIF

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK102-1` | Menghitung ukuran pemusatan dan menentukan mana yang tepat untuk sebuah sebaran | C3–C4 |
| `PS-Sub-CPMK102-1` | Menghitung ukuran penyebaran dan menjelaskan koreksi Bessel | C3 |
| `PS-Sub-CPMK102-1` | Menghitung ukuran posisi dan mendeteksi pencilan secara kritis | C3–C4 |

---

## 2.1 Mengapa Satu Angka Tidak Pernah Cukup

Sebuah tim melaporkan: *"Rata-rata waktu respons API kami 495 ms."*

Terdengar wajar. Tetapi lihat datanya:

```
  95, 98, 102, 88, 105, 97, 101, 93, 99, 8200   (dalam ms)
```

Sembilan dari sepuluh permintaan selesai di bawah 110 ms. Satu permintaan memakan 8,2 detik. Rata-ratanya 497,8 ms — sebuah angka yang **tidak menggambarkan pengalaman siapa pun**.

Tidak ada pengguna yang mengalami 497 ms. Sembilan mengalami sekitar 100 ms; satu mengalami bencana.

> Statistika deskriptif adalah seni memilih angka mana yang **jujur** menggambarkan data. Dan pilihan itu bergantung pada bentuk datanya.

---

## 2.2 Ukuran Pemusatan

### 2.2.1 Mean (Rata-Rata Aritmetik)

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i \qquad \mu = \frac{1}{N}\sum_{i=1}^{N} x_i$$

Mean adalah **titik keseimbangan** sebuah sebaran. Bayangkan data sebagai beban di atas penggaris; mean adalah titik tumpu agar seimbang.

```
   Data: 2, 3, 3, 4, 8          Mean = 20/5 = 4

   2   3 3   4       8
   ●   ● ●   ●       ●
   ├───┼─┼───┼───────┤
   0   2 3   4   6   8
             ▲
            mean = 4
```

**Sifat penting:** mean memakai **seluruh** nilai, sehingga ia sangat peka terhadap nilai ekstrem. Ubah 8 menjadi 80, dan mean melompat dari 4 ke 18,4 — padahal empat nilai lainnya tidak berubah sedikit pun.

### 2.2.2 Median

Median adalah nilai yang membagi data terurut menjadi dua bagian sama banyak.

```python
def median_manual(data):
    """Menghitung median secara manual untuk menunjukkan prosedurnya."""
    d = sorted(data)
    n = len(d)
    tengah = n // 2
    if n % 2 == 1:                       # ganjil
        return d[tengah]
    return (d[tengah - 1] + d[tengah]) / 2   # genap

print(median_manual([2, 3, 3, 4, 8]))       # 3
print(median_manual([2, 3, 3, 4, 80]))      # 3  ← tidak berubah
```

Mengubah 8 menjadi 80 **sama sekali tidak menggeser median**. Sifat ini disebut ***robust*** — tahan terhadap nilai ekstrem.

### 2.2.3 Modus

Nilai yang paling sering muncul. Satu-satunya ukuran pemusatan yang sah untuk data **nominal**.

```python
import pandas as pd

bahasa = pd.Series(["Python", "Java", "Python", "C++", "Python", "Java"])
print(bahasa.mode().tolist())        # ['Python']
print(bahasa.value_counts())
```

Sebuah sebaran dapat **tidak bermodus**, **bermodus satu**, atau **bermodus dua atau lebih**. Sebaran bermodus dua sering menandakan **ada dua kelompok berbeda yang tercampur** dalam satu data — temuan yang penting dan mudah terlewat bila hanya melihat mean.

### 2.2.4 Memilih Ukuran Pemusatan

| Situasi | Ukuran yang Tepat | Alasan |
|---------|-------------------|--------|
| Data simetris tanpa pencilan | Mean | Memakai seluruh informasi |
| Data menceng atau ada pencilan | **Median** | Tidak terseret nilai ekstrem |
| Data nominal | Modus | Satu-satunya yang bermakna |
| Data ordinal | Median atau modus | Mean tidak sah |
| Waktu respons sistem | **Median + p95 + p99** | Sebaran hampir selalu menceng kanan |

### 2.2.5 Mengapa Industri Tidak Memakai Rata-Rata untuk Kinerja

```python
import numpy as np

waktu = np.array([95, 98, 102, 88, 105, 97, 101, 93, 99, 8200])

print(f"Mean   : {waktu.mean():8.1f} ms  ← terseret satu nilai ekstrem")
print(f"Median : {np.median(waktu):8.1f} ms  ← menggambarkan pengalaman tipikal")
print(f"p95    : {np.percentile(waktu, 95):8.1f} ms")
print(f"p99    : {np.percentile(waktu, 99):8.1f} ms  ← menggambarkan pengalaman terburuk")
```

Laporan kinerja profesional menyebut **p50 (median), p95, dan p99** — bukan rata-rata. Alasannya:

- **p50** menjawab: "bagaimana pengalaman pengguna tipikal?"
- **p95** menjawab: "seberapa buruk pengalaman 1 dari 20 pengguna?"
- **p99** menjawab: "seberapa buruk pengalaman 1 dari 100 pengguna?"

Rata-rata tidak menjawab satu pun dari ketiganya.

> **Perjanjian tingkat layanan (SLA)** hampir selalu dinyatakan dalam persentil, misalnya *"99% permintaan selesai di bawah 300 ms"*. Tidak pernah dalam rata-rata — karena rata-rata dapat dipenuhi sambil membiarkan sebagian pengguna menderita.

---

## 2.3 Ukuran Penyebaran

Dua kelompok dapat memiliki mean yang sama persis tetapi karakter yang sama sekali berbeda:

```
  Server A: 49, 50, 50, 51, 50        mean = 50, konsisten
  Server B: 10, 90, 50, 20, 80        mean = 50, kacau
```

Server mana yang Anda pilih untuk melayani pengguna? Mean tidak dapat menjawab. **Penyebaran-lah yang menjawab.**

### 2.3.1 Range

$$\text{Range} = x_{\max} - x_{\min}$$

Paling sederhana, tetapi hanya memakai dua nilai dan sangat peka pencilan.

### 2.3.2 Varians dan Simpangan Baku

$$s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1} \qquad \sigma^2 = \frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N}$$

$$s = \sqrt{s^2} \qquad \sigma = \sqrt{\sigma^2}$$

**Mengapa dikuadratkan?**

Jumlah simpangan biasa selalu nol — simpangan positif dan negatif saling meniadakan:

$$\sum (x_i - \bar{x}) = 0 \quad \text{selalu}$$

Mengkuadratkan membuat semuanya positif, sekaligus memberi **bobot lebih besar pada simpangan besar**. Inilah alasan varians peka terhadap pencilan.

**Mengapa penyebut n−1 untuk sampel? (Koreksi Bessel)**

Karena x̄ dihitung dari data yang sama, simpangan terhadap x̄ cenderung **sedikit lebih kecil** daripada simpangan terhadap μ yang sebenarnya. Membagi dengan n−1 mengoreksi kecenderungan meremehkan itu, sehingga s² menjadi **penduga tak bias** bagi σ².

```python
import numpy as np

rng = np.random.default_rng(42)
MU, SIGMA = 100, 15

# Membuktikan bias penyebut n
n = 5
var_n, var_n1 = [], []
for _ in range(50_000):
    s = rng.normal(MU, SIGMA, n)
    var_n.append(s.var(ddof=0))     # penyebut n
    var_n1.append(s.var(ddof=1))    # penyebut n−1

print(f"Varians populasi sebenarnya : {SIGMA**2}")
print(f"Rata-rata s² dengan n       : {np.mean(var_n):.2f}  ← meremehkan")
print(f"Rata-rata s² dengan n−1     : {np.mean(var_n1):.2f}  ← tepat")
```

> **Jebakan yang sering menjatuhkan mahasiswa.**
>
> - `numpy.var()` memakai `ddof=0` (rumus populasi)
> - `pandas.Series.var()` memakai `ddof=1` (rumus sampel)
>
> Keduanya "benar" untuk konteksnya masing-masing, dan tidak ada galat yang muncul. Selalu tanyakan: **data ini populasi atau sampel?**

### 2.3.3 Koefisien Variasi

$$CV = \frac{s}{\bar{x}} \times 100\%$$

Ukuran penyebaran **relatif** — memungkinkan membandingkan variabilitas dua kelompok dengan satuan atau skala berbeda.

```python
import numpy as np

api_a = np.array([100, 105, 98, 102, 95])       # milidetik
api_b = np.array([2.1, 2.3, 1.9, 2.2, 2.0])     # detik

for nama, d in [("API A (ms)", api_a), ("API B (s)", api_b)]:
    cv = d.std(ddof=1) / d.mean() * 100
    print(f"{nama:12s} mean={d.mean():8.3f}  s={d.std(ddof=1):7.4f}  CV={cv:5.2f}%")
```

Simpangan baku API A jauh lebih besar secara angka (3,7 vs 0,158), tetapi CV menunjukkan **konsistensi relatif keduanya hampir sama**. Tanpa CV, perbandingan itu menyesatkan.

---

## 2.4 Ukuran Posisi

### 2.4.1 Kuartil, Persentil, dan IQR

```
  Data terurut:
  │←── 25% ──→│←── 25% ──→│←── 25% ──→│←── 25% ──→│
  min         Q1          Q2          Q3         max
                       (median)
              │←──────── IQR ────────→│
```

| Ukuran | Makna |
|--------|-------|
| Q1 (persentil 25) | 25% data di bawah nilai ini |
| Q2 (persentil 50) | Median |
| Q3 (persentil 75) | 75% data di bawah nilai ini |
| **IQR = Q3 − Q1** | Rentang 50% data di tengah — ukuran penyebaran yang ***robust*** |

### 2.4.2 Deteksi Pencilan: Aturan 1,5×IQR

$$\text{Batas bawah} = Q_1 - 1{,}5 \times IQR \qquad \text{Batas atas} = Q_3 + 1{,}5 \times IQR$$

```python
import numpy as np

def deteksi_pencilan(data):
    """Mendeteksi kandidat pencilan dengan aturan 1,5 × IQR."""
    data = np.asarray(data)
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    bb, ba = q1 - 1.5*iqr, q3 + 1.5*iqr
    return bb, ba, data[(data < bb) | (data > ba)]

waktu = np.array([88, 93, 95, 97, 98, 99, 101, 102, 105, 8200])
bb, ba, pencilan = deteksi_pencilan(waktu)
print(f"Batas wajar : [{bb:.2f} , {ba:.2f}]")
print(f"Pencilan    : {pencilan}")
```

### 2.4.3 Etika Pencilan

Ini bagian yang paling sering disalahgunakan — dan paling menentukan integritas sebuah analisis.

> **Kata "pencilan" BUKAN izin untuk membuang data.**

Nilai 8.200 ms itu mungkin justru **temuan paling berharga** dalam dataset. Barangkali ada *query* yang tidak terindeks, atau *timeout* jaringan yang nyata dialami pengguna. Membuangnya berarti membuang satu-satunya petunjuk tentang masalah yang paling merugikan.

**Kapan pencilan boleh dibuang:**

| Situasi | Boleh dibuang? |
|---------|----------------|
| Terbukti kesalahan pencatatan (umur 250 tahun) | **Ya**, dengan catatan |
| Alat ukur terbukti rusak pada waktu itu | **Ya**, dengan catatan |
| Di luar populasi yang dipelajari (data server uji masuk ke data produksi) | **Ya**, dengan catatan |
| "Hasilnya jadi lebih rapi" | **Tidak** |
| "Grafiknya jadi lebih bagus" | **Tidak** |
| "Kalau dibuang jadi signifikan" | **Tidak — ini pelanggaran berat** |

**Yang harus dilakukan ketika menemukan pencilan:**

1. **Telaah konteksnya.** Lihat seluruh baris datanya, bukan hanya satu kolom.
2. **Cari penjelasan substantif.** Apakah ada alasan nyata nilai ini ekstrem?
3. **Laporkan apa adanya.** Bila dipertahankan, gunakan median dan IQR.
4. **Bila dibuang, catat alasannya** dalam laporan, beserta dampaknya terhadap kesimpulan.
5. **Sajikan kedua versi** bila dampaknya besar: dengan dan tanpa pencilan.

---

## 2.5 Bentuk Sebaran: Kemencengan

```
   MENCENG KIRI          SIMETRIS           MENCENG KANAN
   (negatif)                                (positif)

        ▄▄█                 ▄█▄                █▄▄
      ▄███│               ▄███▄                │███▄
    ▄█████│             ▄█████▄                │█████▄
   ───────┼──         ──────┼──────          ──┼───────
   mean < median       mean = median         median < mean
                       = modus

   contoh: nilai ujian  contoh: tinggi        contoh: waktu respons,
   yang mudah           badan                 gaji, ukuran berkas
```

**Aturan praktis:**

| Kondisi | Bentuk |
|---------|--------|
| mean ≈ median | Simetris |
| mean > median | Menceng kanan |
| mean < median | Menceng kiri |

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)
waktu = rng.exponential(scale=120, size=1000)

print(f"Mean        : {waktu.mean():8.2f}")
print(f"Median      : {np.median(waktu):8.2f}")
print(f"Kemencengan : {stats.skew(waktu):8.4f}")

sk = stats.skew(waktu)
if sk > 0.5:
    print("→ Menceng kanan. Gunakan MEDIAN sebagai ukuran pemusatan.")
elif sk < -0.5:
    print("→ Menceng kiri. Gunakan MEDIAN.")
else:
    print("→ Cukup simetris. Mean dapat dipakai.")
```

### Mengapa Data Informatika Hampir Selalu Menceng Kanan

Waktu respons, ukuran berkas, jumlah pengikut, penghasilan — semuanya menceng kanan. Bukan kebetulan.

> **Penyebabnya struktural:** besaran-besaran itu memiliki **batas bawah yang tegas** (tidak mungkin negatif, dan ada nilai minimum yang wajar) tetapi **tidak punya batas atas**. Sebuah permintaan bisa saja tertahan 30 detik; tidak ada yang mencegahnya. Tetapi tidak ada permintaan yang selesai dalam −5 ms.
>
> Sebaran dengan batas bawah tegas dan ekor atas bebas **selalu** menceng kanan.

Konsekuensinya praktis: untuk data semacam ini, **mean hampir selalu menyesatkan**, dan median hampir selalu pilihan yang lebih jujur.

---

## 2.6 Analisis Deskriptif Lengkap

```python
import pandas as pd
import numpy as np
from scipy import stats

def ringkasan_deskriptif(seri, nama):
    """Ringkasan deskriptif lengkap beserta rekomendasi."""
    seri = seri.dropna()
    q1, q3 = seri.quantile([0.25, 0.75])
    iqr = q3 - q1
    sk = stats.skew(seri)

    print(f"\n{'='*54}\n  {nama}\n{'='*54}")
    print(f"  n              : {seri.count()}")
    print(f"  Mean           : {seri.mean():.4f}")
    print(f"  Median         : {seri.median():.4f}")
    print(f"  Modus          : {seri.mode().tolist()[:3]}")
    print(f"  Simpangan baku : {seri.std():.4f}   (ddof=1)")
    print(f"  Koef. variasi  : {seri.std()/seri.mean()*100:.2f}%")
    print(f"  Min–Q1–Q2–Q3–Max: {seri.min():.2f} – {q1:.2f} – "
          f"{seri.median():.2f} – {q3:.2f} – {seri.max():.2f}")
    print(f"  IQR            : {iqr:.4f}")
    print(f"  p95 / p99      : {seri.quantile(0.95):.2f} / {seri.quantile(0.99):.2f}")
    print(f"  Kemencengan    : {sk:.4f}")

    if abs(sk) < 0.5:
        print("  → Simetris; MEAN layak dipakai.")
    else:
        print(f"  → Menceng {'kanan' if sk > 0 else 'kiri'}; gunakan MEDIAN dan IQR.")

    pencilan = seri[(seri < q1 - 1.5*iqr) | (seri > q3 + 1.5*iqr)]
    print(f"  Kandidat pencilan: {len(pencilan)} "
          f"({len(pencilan)/len(seri)*100:.1f}%)")
    if len(pencilan) > 0:
        print("     JANGAN dibuang tanpa alasan substantif.")

df = pd.read_csv("nilai_mahasiswa_if.csv")
for kolom in ["nilai_uts", "nilai_uas", "jam_belajar"]:
    ringkasan_deskriptif(df[kolom], kolom)
```

### Analisis per Kelompok

```python
print(df.groupby("kelas")[["nilai_uas", "jam_belajar"]].agg(
    ["count", "mean", "median", "std"]
).round(2))
```

> **Pertanyaan yang harus muncul di benak Anda:** bila rata-rata IF26A lebih tinggi dari IF26H, apakah kelas IF26A "lebih baik"?
>
> **Belum tentu.** Selisih itu bisa saja kebetulan sampel. Menjawabnya memerlukan **uji hipotesis dua sampel** — Bab 11.
>
> Statistika deskriptif **menggambarkan, tidak menyimpulkan**. Batas ini penting dipegang.

---

## AI Corner — Tingkat Dasar

### Apa yang AI Lakukan dengan Baik dan Buruk di Bab Ini

| AI biasanya **baik** dalam | AI sering **keliru** dalam |
|----------------------------|----------------------------|
| Menjelaskan rumus varians dan mengapa dikuadratkan | Menyadari bahwa data Anda menceng dan median lebih tepat |
| Menuliskan kode pandas untuk menghitung ringkasan | Mengetahui bahwa kolom tertentu berskala ordinal |
| Menjelaskan koreksi Bessel | Memutuskan apakah pencilan boleh dibuang |
| Memberi contoh tambahan | Menilai apakah sampel Anda representatif |

Pola yang terlihat: **AI kuat pada hal yang bersifat umum, lemah pada hal yang memerlukan konteks data Anda.** Dan hampir semua keputusan penting dalam statistika deskriptif bergantung pada konteks.

### Percobaan: Uji AI Anda

Ajukan pertanyaan ini:

> *"Saya punya data waktu respons server: 95, 98, 102, 88, 105, 97, 101, 93, 99, 8200 ms. Berapa rata-ratanya?"*

Sebagian besar AI akan menghitung 497,8 ms dengan benar. **Perhatikan apakah ia memperingatkan Anda** bahwa rata-rata tidak tepat untuk data ini.

Lalu ajukan pertanyaan lanjutan:

> *"Apakah rata-rata itu angka yang tepat untuk dilaporkan?"*

Sekarang hampir semua AI akan menjelaskan bahwa median lebih tepat. **Informasi itu ada dalam modelnya — tetapi ia tidak menyampaikannya sampai ditanya.**

> **Pelajarannya:** AI menjawab pertanyaan yang Anda ajukan. Kualitas jawabannya dibatasi oleh kualitas pertanyaan Anda. Dan yang mengetahui pertanyaan mana yang seharusnya diajukan — hanya Anda.

### Pemakaian yang Dianjurkan

```
PROMPT YANG BAIK:
"Saya menghitung mean = 497,8 dan median = 98,5 untuk data waktu respons.
 Saya menduga datanya menceng kanan. Apakah dugaan saya masuk akal, dan
 ukuran mana yang sebaiknya saya laporkan?"

Mengapa baik: Anda sudah menghitung sendiri, sudah punya dugaan,
dan meminta AI memeriksa penalaran Anda — bukan menggantikannya.
```

---

## Latihan Soal

### Tingkat Dasar

1. Data waktu kompilasi (detik): `42, 38, 45, 41, 39, 44, 40`. Hitung secara manual:
   (a) mean, (b) median, (c) range, (d) varians sampel, (e) simpangan baku sampel.

2. Untuk data yang sama, hitung Q1, Q3, dan IQR.

3. Jelaskan mengapa jumlah simpangan Σ(xᵢ − x̄) selalu bernilai nol, dan bagaimana masalah itu diatasi dalam rumus varians.

4. Manakah ukuran pemusatan yang tepat untuk setiap kasus?
   (a) Bahasa pemrograman favorit mahasiswa
   (b) Waktu respons API
   (c) Rating aplikasi 1–5 bintang
   (d) Nilai ujian yang sebarannya simetris

5. Sebuah data memiliki mean 72 dan median 85. Bagaimana bentuk sebarannya? Ukuran pemusatan mana yang sebaiknya dilaporkan?

### Tingkat Menengah

6. Data waktu kompilasi bertambah satu nilai: `42, 38, 45, 41, 39, 44, 40, 185`.
   (a) Hitung ulang mean dan median. Mana yang berubah lebih besar? Mengapa?
   (b) Hitung batas pencilan dengan aturan 1,5×IQR.
   (c) Apakah 185 tergolong pencilan?
   (d) Nilai 185 itu ternyata kompilasi pertama setelah *cache* dibersihkan. **Bolehkah dibuang?** Jelaskan dengan mengacu pada kriteria di §2.4.3.

7. Jelaskan mengapa `numpy.var()` dan `pandas.Series.var()` memberi hasil berbeda untuk data yang sama. Tuliskan kode yang membuktikannya dan jelaskan mana yang harus dipakai dalam situasi apa.

8. Tiga layanan memiliki waktu respons dengan satuan berbeda:

   | Layanan | Data |
   |---------|------|
   | Autentikasi (ms) | 45, 48, 43, 47, 44, 46, 49, 45 |
   | Query DB (ms) | 210, 350, 180, 420, 195, 380, 205, 390 |
   | Render (detik) | 3,1 · 3,4 · 2,9 · 3,2 · 3,0 · 3,3 · 3,1 · 3,5 |

   (a) Hitung mean, simpangan baku, dan koefisien variasi masing-masing.
   (b) Layanan mana yang paling konsisten?
   (c) Jelaskan mengapa simpangan baku saja tidak cukup untuk menjawab (b).

9. Sebuah laporan menyatakan: *"Rata-rata waktu respons kami 200 ms, memenuhi SLA 500 ms."* Data sebenarnya: p50 = 90 ms, p95 = 850 ms, p99 = 3.200 ms.
   (a) Apakah pernyataan itu berbohong?
   (b) Apakah pernyataan itu menyesatkan? Jelaskan perbedaannya.
   (c) Tuliskan ulang laporan itu secara jujur.

### Tingkat Mahir

10. Buktikan secara aljabar bahwa Σ(xᵢ − x̄) = 0 untuk sembarang data.

11. Jelaskan secara konseptual mengapa penyebut n−1 menghasilkan penduga tak bias bagi σ².
    (a) Jelaskan intuisinya dalam 3–4 kalimat.
    (b) Rancang simulasi Python untuk mendemonstrasikannya pada n = 3, 5, 10, 30.
    (c) Apa yang terjadi pada besarnya bias seiring n bertambah? Mengapa?

12. Seorang analis diminta melaporkan "waktu respons tipikal" sistem. Ia menemukan sebaran **bermodus dua**: satu gundukan di sekitar 80 ms dan satu di sekitar 900 ms.
    (a) Mengapa mean, median, dan modus **ketiganya** gagal menggambarkan data ini dengan jujur?
    (b) Apa dugaan Anda tentang penyebab bimodalitas itu?
    (c) Apa yang seharusnya dilakukan analis tersebut?
    (d) Rancang cara penyajian yang jujur untuk laporan kepada manajemen.

13. Tulislah pedoman satu halaman berjudul *"Etika Menangani Pencilan"* untuk tim data di sebuah perusahaan. Sertakan: definisi, prosedur yang harus dilalui, kriteria kapan boleh dibuang, dan format pencatatan keputusannya.

---

## Rangkuman

1. **Mean** memakai seluruh data tetapi peka pencilan; **median** *robust*; **modus** satu-satunya yang sah untuk data nominal.
2. Untuk data menceng — dan data Informatika hampir selalu menceng kanan — **gunakan median**.
3. Industri melaporkan **p50, p95, p99** untuk kinerja sistem. SLA dinyatakan dalam persentil, bukan rata-rata.
4. **Varians dan simpangan baku** mengukur penyebaran. Simpangan dikuadratkan karena jumlah simpangan biasa selalu nol.
5. **Koreksi Bessel** (penyebut n−1) membuat s² menjadi penduga tak bias bagi σ².
6. `numpy.var()` memakai `ddof=0`; `pandas.var()` memakai `ddof=1`. Selalu periksa: populasi atau sampel?
7. **Koefisien variasi** memungkinkan membandingkan variabilitas lintas satuan.
8. **IQR** adalah ukuran penyebaran yang *robust*. Aturan 1,5×IQR **menandai** kandidat pencilan — tidak memerintahkan membuangnya.
9. **Pencilan hanya boleh dibuang dengan alasan substantif**, dan keputusan itu wajib dicatat.
10. Data Informatika menceng kanan karena punya **batas bawah tegas dan ekor atas bebas**.
11. Statistika deskriptif **menggambarkan, tidak menyimpulkan**.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 1.3–1.6. Pearson.
2. Bhattacharyya, G. K., & Johnson, R. A. (2019). *Statistics: Principles and Methods* (8th ed.), Bab 2. Wiley.
3. Downey, A. B. (2014). *Think Stats* (2nd ed.), Bab 2–3. O'Reilly Media.
4. Dean, J., & Barroso, L. A. (2013). The Tail at Scale. *Communications of the ACM*, 56(2), 74–80.
5. Aggarwal, C. C. (2017). *Outlier Analysis* (2nd ed.), Bab 1. Springer.
6. Dokumentasi pandas — *Descriptive statistics*. <https://pandas.pydata.org/docs/user_guide/basics.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
