# Minggu 4: Dasar Probabilitas

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 4 |
| **Topik** | Ruang sampel, aksioma Kolmogorov, aturan penjumlahan dan perkalian, probabilitas bersyarat, kaidah pencacahan |
| **CPL / CPMK** | CPL08 / CPMK081 |
| **Sub-CPMK** | `PS-Sub-CPMK081-1` |
| **Indikator Mingguan** | Menerapkan aksioma probabilitas, aturan penjumlahan/perkalian, dan probabilitas bersyarat |
| **Level Bloom** | C3 (Menerapkan) |
| **Durasi** | 150 menit tatap muka |
| **Metode** | Kuliah, latihan terbimbing, simulasi Monte Carlo |

---

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menentukan** (C3) ruang sampel dan kejadian dari sebuah eksperimen acak dalam konteks computing.
2. **Menerapkan** (C3) tiga aksioma Kolmogorov dan menurunkan aturan komplemen serta aturan penjumlahan darinya.
3. **Menghitung** (C3) probabilitas gabungan dan irisan dengan aturan penjumlahan dan perkalian.
4. **Menghitung** (C3) probabilitas bersyarat dan menjelaskan maknanya secara kontekstual.
5. **Menerapkan** (C3) kaidah pencacahan (aturan perkalian, permutasi, kombinasi) untuk menghitung probabilitas.

---

## Materi Pembelajaran

### 1. Dari Statistika ke Probabilitas

Tiga minggu pertama kita **menggambarkan data yang sudah ada**. Mulai minggu ini arahnya berbalik: kita membangun **model matematis tentang ketidakpastian**, agar kelak bisa menyimpulkan tentang data yang *belum* kita amati.

```
  Minggu 1–3            Minggu 4–7           Minggu 9–14
  ──────────            ──────────           ───────────
  DESKRIPTIF     →      PROBABILITAS   →     INFERENSIAL
  "apa yang               "apa yang            "apa yang
   terjadi"                mungkin terjadi"     berlaku umum"

  data → ringkasan      model → peluang      sampel → populasi
```

> **Mengapa ini penting bagi Informatika.** Ketika Anda kelak membangun model *machine learning*, keluarannya bukan "kucing" melainkan "probabilitas 0,87 bahwa ini kucing". Tanpa memahami apa arti angka 0,87 itu — dan apa yang **tidak** dikatakannya — Anda tidak bisa menilai apakah model Anda layak dipercaya.

---

### 2. Eksperimen Acak, Ruang Sampel, dan Kejadian

#### 2.1 Definisi

| Istilah | Lambang | Definisi | Contoh Informatika |
|---------|---------|----------|--------------------|
| **Eksperimen acak** | — | Proses yang hasilnya tidak dapat dipastikan sebelumnya | Mengirim satu permintaan HTTP |
| **Ruang sampel** | S atau Ω | Himpunan semua hasil yang mungkin | S = {200, 301, 404, 500} |
| **Titik sampel** | — | Satu anggota ruang sampel | 404 |
| **Kejadian** | A, B, … | Himpunan bagian dari ruang sampel | A = {404, 500} ("permintaan gagal") |

#### 2.2 Contoh dalam Konteks Computing

**Contoh 1 — Pengujian perangkat lunak.**
Tiga modul diuji, masing-masing lulus (L) atau gagal (G).

```
S = { LLL, LLG, LGL, LGG, GLL, GLG, GGL, GGG }      |S| = 2³ = 8
```

Kejadian A = "tepat satu modul gagal" = {LLG, LGL, GLL}, sehingga |A| = 3.

**Contoh 2 — Penjadwalan proses.**
Tiga proses (P1, P2, P3) dijadwalkan dalam suatu urutan.

```
S = { P1P2P3, P1P3P2, P2P1P3, P2P3P1, P3P1P2, P3P2P1 }      |S| = 3! = 6
```

```python
from itertools import product, permutations

# Contoh 1: hasil pengujian tiga modul
ruang_uji = list(product(["L", "G"], repeat=3))
print(f"Ukuran ruang sampel: {len(ruang_uji)}")
print(["".join(h) for h in ruang_uji])

# Kejadian: tepat satu modul gagal
tepat_satu_gagal = [h for h in ruang_uji if h.count("G") == 1]
print(f"\nTepat satu gagal: {['' .join(h) for h in tepat_satu_gagal]}")
print(f"P(tepat satu gagal) = {len(tepat_satu_gagal)}/{len(ruang_uji)} "
      f"= {len(tepat_satu_gagal)/len(ruang_uji):.4f}")

# Contoh 2: urutan penjadwalan proses
ruang_jadwal = list(permutations(["P1", "P2", "P3"]))
print(f"\nJumlah urutan penjadwalan: {len(ruang_jadwal)}")
```

#### 2.3 Operasi Himpunan pada Kejadian

```
   GABUNGAN  A ∪ B          IRISAN  A ∩ B         KOMPLEMEN  A'
   "A atau B"               "A dan B"             "bukan A"

   ┌─────────────┐          ┌─────────────┐       ┌─────────────┐
   │ ▓▓▓▓▓┌───┐  │          │     ┌───┐   │       │░░░░░┌───┐░░░│
   │ ▓▓A▓▓│▓▓▓│B │          │  A  │▓▓▓│ B │       │░░A░░│   │░B░│
   │ ▓▓▓▓▓└───┘  │          │     └───┘   │       │░░░░░└───┘░░░│
   └─────────────┘          └─────────────┘       └─────────────┘
```

| Istilah | Makna | Contoh |
|---------|-------|--------|
| A ∪ B | A atau B (atau keduanya) terjadi | "permintaan gagal ATAU lambat" |
| A ∩ B | A dan B terjadi bersamaan | "permintaan gagal DAN lambat" |
| A′ | A tidak terjadi | "permintaan tidak gagal" |
| A ∩ B = ∅ | A dan B **saling lepas** (mustahil bersamaan) | "status 200" dan "status 404" |

---

### 3. Aksioma Kolmogorov

Seluruh teori probabilitas dibangun dari **tiga aksioma** saja. Semua aturan lain diturunkan dari ketiganya.

> **Aksioma 1 (Non-negatif).** Untuk setiap kejadian A: P(A) ≥ 0
>
> **Aksioma 2 (Normalisasi).** P(S) = 1
>
> **Aksioma 3 (Penjumlahan).** Bila A dan B saling lepas, maka P(A ∪ B) = P(A) + P(B)

#### 3.1 Aturan yang Diturunkan

**Aturan komplemen.** Karena A dan A′ saling lepas dan A ∪ A′ = S:

$$P(A) + P(A') = P(S) = 1 \quad\Longrightarrow\quad P(A') = 1 - P(A)$$

**Aturan penjumlahan umum.** Untuk kejadian yang **tidak** saling lepas:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

Irisannya dikurangkan karena terhitung dua kali.

**Batas atas.** Dari Aksioma 1 dan 2: 0 ≤ P(A) ≤ 1 untuk setiap A.

#### 3.2 Contoh Terapan

> **Soal.** Dari 500 permintaan API yang dicatat, 60 berstatus galat (kejadian G) dan 85 memakan waktu lebih dari 1 detik (kejadian L). Sebanyak 25 permintaan mengalami keduanya.
>
> Berapa probabilitas sebuah permintaan mengalami galat **atau** lambat?

$$P(G) = \frac{60}{500} = 0{,}12 \qquad P(L) = \frac{85}{500} = 0{,}17 \qquad P(G \cap L) = \frac{25}{500} = 0{,}05$$

$$P(G \cup L) = 0{,}12 + 0{,}17 - 0{,}05 = 0{,}24$$

**Dan berapa probabilitas permintaan berjalan normal** (tidak galat dan tidak lambat)?

$$P(G' \cap L') = P\big((G \cup L)'\big) = 1 - 0{,}24 = 0{,}76$$

```python
total = 500
n_galat, n_lambat, n_keduanya = 60, 85, 25

p_galat   = n_galat / total
p_lambat  = n_lambat / total
p_irisan  = n_keduanya / total

p_gabungan = p_galat + p_lambat - p_irisan
p_normal   = 1 - p_gabungan

print(f"P(galat)                = {p_galat:.4f}")
print(f"P(lambat)               = {p_lambat:.4f}")
print(f"P(galat DAN lambat)     = {p_irisan:.4f}")
print(f"P(galat ATAU lambat)    = {p_gabungan:.4f}")
print(f"P(normal)               = {p_normal:.4f}")

# Pemeriksaan: keempat wilayah harus berjumlah 1
hanya_galat  = p_galat - p_irisan
hanya_lambat = p_lambat - p_irisan
print(f"\nPemeriksaan total: "
      f"{hanya_galat + hanya_lambat + p_irisan + p_normal:.4f}")
```

---

### 4. Probabilitas Bersyarat

#### 4.1 Definisi

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} \qquad \text{dengan } P(B) > 0$$

Dibaca: "probabilitas A **bila diketahui** B telah terjadi".

**Intuisinya:** mengetahui B telah terjadi berarti **mempersempit ruang sampel** menjadi hanya B. Kita menghitung seberapa besar bagian B yang juga mengandung A.

```
  SEBELUM tahu B           SESUDAH tahu B terjadi
  ┌─────────────────┐       ┌───────┐
  │      ┌───┐      │       │▓▓▓┌───┤  ruang sampel menyempit
  │  A   │▓▓▓│  B   │  →    │▓▓▓│   │  menjadi B saja
  │      └───┘      │       │A∩B│   │
  └─────────────────┘       └───────┘
   P(A) = A / S              P(A|B) = (A∩B) / B
```

#### 4.2 Contoh Terapan

Melanjutkan kasus API di atas:

> **Bila diketahui sebuah permintaan lambat, berapa probabilitas ia juga galat?**

$$P(G \mid L) = \frac{P(G \cap L)}{P(L)} = \frac{0{,}05}{0{,}17} = 0{,}294$$

> **Dan sebaliknya — bila diketahui galat, berapa probabilitas ia lambat?**

$$P(L \mid G) = \frac{P(G \cap L)}{P(G)} = \frac{0{,}05}{0{,}12} = 0{,}417$$

```python
p_galat_bila_lambat = p_irisan / p_lambat
p_lambat_bila_galat = p_irisan / p_galat

print(f"P(galat | lambat) = {p_galat_bila_lambat:.4f}")
print(f"P(lambat | galat) = {p_lambat_bila_galat:.4f}")
print(f"\nPerhatikan: P(G|L) ≠ P(L|G). Keduanya menjawab pertanyaan berbeda.")
```

> **Kesalahan paling umum dalam probabilitas: menukar P(A|B) dengan P(B|A).** Keduanya sangat berbeda. "Probabilitas seseorang sakit bila hasil tesnya positif" sama sekali berbeda dari "probabilitas hasil tes positif bila orangnya sakit". Kekeliruan ini disebut *confusion of the inverse*, dan akan kita bedah tuntas pada Minggu 5.

#### 4.3 Aturan Perkalian

Dari definisi probabilitas bersyarat:

$$P(A \cap B) = P(B) \cdot P(A \mid B) = P(A) \cdot P(B \mid A)$$

Untuk tiga kejadian:

$$P(A \cap B \cap C) = P(A) \cdot P(B \mid A) \cdot P(C \mid A \cap B)$$

**Contoh.** Dari 20 tiket bug di papan kerja, 6 bersifat kritis. Dua tiket diambil berturut-turut tanpa pengembalian. Berapa probabilitas keduanya kritis?

$$P(\text{kedua kritis}) = \frac{6}{20} \times \frac{5}{19} = \frac{30}{380} = 0{,}0789$$

```python
# Tanpa pengembalian: probabilitas kedua berubah setelah yang pertama diambil
p_pertama_kritis = 6 / 20
p_kedua_kritis_bila_pertama_kritis = 5 / 19

p_keduanya = p_pertama_kritis * p_kedua_kritis_bila_pertama_kritis
print(f"P(kedua tiket kritis) = {p_keduanya:.4f}")

# Bandingkan DENGAN pengembalian (kejadian menjadi bebas)
p_dengan_pengembalian = (6/20) * (6/20)
print(f"Bila dengan pengembalian = {p_dengan_pengembalian:.4f}")
```

---

### 5. Kaidah Pencacahan

Ketika seluruh titik sampel berpeluang sama, probabilitas dihitung dengan:

$$P(A) = \frac{\text{banyaknya hasil dalam } A}{\text{banyaknya hasil dalam } S}$$

Karena itu kita perlu cara **mencacah** tanpa mendaftar satu per satu.

#### 5.1 Aturan Perkalian

Bila tahap 1 punya n₁ pilihan, tahap 2 punya n₂ pilihan, dan seterusnya, maka total = n₁ × n₂ × … × nₖ.

**Contoh — kekuatan kata sandi.** Sandi 8 karakter dari 26 huruf kecil, 26 huruf besar, 10 angka, dan 10 simbol (total 72 karakter):

$$72^8 = 722{.}204{.}136{.}308{.}736 \approx 7{,}2 \times 10^{14}$$

```python
jumlah_karakter = 26 + 26 + 10 + 10
panjang = 8
total_kombinasi = jumlah_karakter ** panjang

print(f"Jumlah kemungkinan sandi : {total_kombinasi:,}")

# Berapa lama menebak seluruhnya dengan 10 miliar percobaan per detik?
percobaan_per_detik = 10_000_000_000
detik = total_kombinasi / percobaan_per_detik
print(f"Waktu menebak seluruhnya : {detik/3600:.2f} jam")

# Bandingkan dengan sandi 12 karakter
total_12 = jumlah_karakter ** 12
print(f"\nSandi 12 karakter        : {total_12:,}")
print(f"Waktu menebak            : {total_12/percobaan_per_detik/3600/24/365:.0f} tahun")
```

#### 5.2 Permutasi — Urutan Diperhatikan

$$P(n, r) = \frac{n!}{(n-r)!}$$

**Contoh.** Dari 10 tugas, berapa cara memilih 3 tugas dan menyusunnya ke dalam urutan prioritas pertama, kedua, ketiga?

$$P(10, 3) = \frac{10!}{7!} = 10 \times 9 \times 8 = 720$$

#### 5.3 Kombinasi — Urutan Tidak Diperhatikan

$$C(n, r) = \binom{n}{r} = \frac{n!}{r!\,(n-r)!}$$

**Contoh.** Dari 10 tugas, berapa cara memilih 3 tugas untuk dikerjakan sprint ini (tanpa urutan)?

$$C(10, 3) = \frac{10!}{3!\,7!} = 120$$

```python
from math import factorial, perm, comb

n, r = 10, 3

print(f"Permutasi P({n},{r}) = {perm(n, r)}")       # 720 — urutan penting
print(f"Kombinasi C({n},{r}) = {comb(n, r)}")       # 120 — urutan tidak penting
print(f"Rasio: P/C = {perm(n,r)/comb(n,r)} = {r}! = {factorial(r)}")
```

> **Cara cepat membedakan:** tanyakan "apakah menukar posisi mengubah hasilnya?" Panitia yang terdiri dari Ali, Budi, Citra sama saja dengan Citra, Budi, Ali → **kombinasi**. Tetapi ketua Ali–sekretaris Budi berbeda dari ketua Budi–sekretaris Ali → **permutasi**.

#### 5.4 Contoh Gabungan

> **Soal.** Sebuah tim beranggotakan 8 pengembang backend dan 5 pengembang frontend. Dipilih 4 orang secara acak untuk sebuah proyek. Berapa probabilitas terpilih tepat 2 backend dan 2 frontend?

$$P = \frac{\binom{8}{2} \times \binom{5}{2}}{\binom{13}{4}} = \frac{28 \times 10}{715} = \frac{280}{715} = 0{,}3916$$

```python
from math import comb

n_backend, n_frontend, n_pilih = 8, 5, 4

cara_menguntungkan = comb(n_backend, 2) * comb(n_frontend, 2)
cara_total = comb(n_backend + n_frontend, n_pilih)

print(f"Cara memilih 2 backend  : {comb(n_backend, 2)}")
print(f"Cara memilih 2 frontend : {comb(n_frontend, 2)}")
print(f"Cara menguntungkan      : {cara_menguntungkan}")
print(f"Cara total              : {cara_total}")
print(f"P(2 backend, 2 frontend)= {cara_menguntungkan/cara_total:.4f}")
```

---

### 6. Simulasi Monte Carlo: Memeriksa Jawaban Secara Empiris

Ketika ragu pada hasil hitungan, **simulasikan**. Bila simulasi dengan banyak ulangan mendekati hitungan analitis, keduanya saling menguatkan.

```python
import numpy as np

def simulasi_pilih_tim(n_backend=8, n_frontend=5, n_pilih=4,
                       target_backend=2, ulangan=200_000, seed=42):
    """Memeriksa hasil analitis dengan simulasi Monte Carlo."""
    rng = np.random.default_rng(seed)
    # 1 menandai backend, 0 menandai frontend
    tim = np.array([1] * n_backend + [0] * n_frontend)

    berhasil = 0
    for _ in range(ulangan):
        terpilih = rng.choice(tim, size=n_pilih, replace=False)
        if terpilih.sum() == target_backend:
            berhasil += 1

    return berhasil / ulangan

hasil_simulasi = simulasi_pilih_tim()
hasil_analitis = comb(8, 2) * comb(5, 2) / comb(13, 4)

print(f"Hasil simulasi  : {hasil_simulasi:.4f}")
print(f"Hasil analitis  : {hasil_analitis:.4f}")
print(f"Selisih         : {abs(hasil_simulasi - hasil_analitis):.5f}")
```

> **Hukum Bilangan Besar** menjamin bahwa proporsi hasil simulasi akan mendekati probabilitas sebenarnya seiring bertambahnya ulangan. Ini bukan kebetulan — ini teorema, dan akan kita perdalam pada Minggu 9.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (Mandiri — 60 menit)

1. Membaca [Bab 4 buku ajar](../06-buku-ajar/bab-04-dasar-probabilitas.md).
2. Menyegarkan kembali notasi himpunan: gabungan, irisan, komplemen.
3. Menuliskan ruang sampel untuk: "melempar dua dadu enam sisi dan mencatat jumlahnya".

### Di Kelas (150 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10' | Pembahasan Kuis 1 dan Lab 03 |
| 10–35' | Kuliah: eksperimen acak, ruang sampel, kejadian; contoh Informatika |
| 35–60' | Kuliah: tiga aksioma Kolmogorov; **menurunkan** aturan komplemen dan penjumlahan bersama-sama |
| 60–70' | Istirahat |
| 70–100' | Kuliah + latihan: probabilitas bersyarat dan aturan perkalian |
| 100–125' | Kuliah + latihan: kaidah pencacahan, permutasi vs kombinasi |
| 125–145' | Studio: kasus pemilihan tim — hitung analitis lalu verifikasi dengan simulasi |
| 145–150' | Penutup, penjelasan Lab 04 |

#### Latihan Kelas

1. Sebuah sistem memiliki tiga server. Setiap server dapat aktif (A) atau mati (M). Tuliskan ruang sampel, lalu hitung P(sedikitnya dua server aktif) bila semua hasil berpeluang sama.

2. Dari 1.000 sesi pengguna: 220 membuka halaman produk, 130 menambahkan ke keranjang, 80 melakukan keduanya. Hitung:
   (a) P(membuka produk atau menambah keranjang)
   (b) P(tidak melakukan keduanya)
   (c) P(menambah keranjang | membuka produk)
   (d) P(membuka produk | menambah keranjang)
   Jelaskan mengapa (c) dan (d) berbeda.

3. PIN ATM terdiri dari 6 digit angka. Berapa banyak PIN yang mungkin bila: (a) digit boleh berulang; (b) digit tidak boleh berulang; (c) tidak boleh ada dua digit berurutan yang sama?

4. Sebuah *code review* memilih 3 orang dari 12 anggota tim untuk menelaah satu *pull request*. Berapa probabilitas seorang anggota tertentu terpilih?

### Setelah Kelas (Mandiri — 180 menit)

1. Mengerjakan [Lab 04](../04-labs/lab-04-simulasi-probabilitas-monte-carlo.md).
2. Mengerjakan Latihan Soal Bab 4 ketiga tingkat.
3. Menyiapkan proposal proyek — **dikumpulkan Minggu 6**.

---

## Penugasan

| Kode | Tugas | Bobot | Batas Waktu |
|------|-------|-------|-------------|
| T-04 | Laporan Lab 04 — Simulasi probabilitas Monte Carlo | 1,92% | Sebelum kelas Minggu 5 |

---

## Rangkuman

1. **Eksperimen acak** menghasilkan **ruang sampel** S; **kejadian** adalah himpunan bagian dari S.
2. Seluruh teori probabilitas berdiri di atas **tiga aksioma Kolmogorov**. Aturan komplemen dan aturan penjumlahan adalah turunannya, bukan aturan terpisah yang harus dihafal.
3. **Aturan penjumlahan umum:** P(A ∪ B) = P(A) + P(B) − P(A ∩ B). Irisannya dikurangkan agar tidak terhitung dua kali.
4. **Probabilitas bersyarat** P(A|B) = P(A ∩ B)/P(B) mempersempit ruang sampel menjadi B saja.
5. **P(A|B) ≠ P(B|A).** Menukar keduanya adalah kesalahan paling umum dalam probabilitas terapan — dan akan dibahas tuntas Minggu 5.
6. **Aturan perkalian:** P(A ∩ B) = P(A)·P(B|A). Pengambilan tanpa pengembalian mengubah probabilitas tahap berikutnya.
7. **Permutasi** memperhatikan urutan; **kombinasi** tidak. Tanyakan: "apakah menukar posisi mengubah hasilnya?"
8. **Simulasi Monte Carlo** adalah cara memeriksa hitungan analitis secara empiris, dijamin oleh Hukum Bilangan Besar.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 2. Pearson.
2. Ross, S. M. (2019). *A First Course in Probability* (10th ed.), Bab 1–3. Pearson.
3. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 2. Wiley.
4. Dokumentasi Python `itertools` — <https://docs.python.org/3/library/itertools.html>
5. Dokumentasi Python `math` (`comb`, `perm`, `factorial`) — <https://docs.python.org/3/library/math.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
