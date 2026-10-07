# BAB 4: DASAR PROBABILITAS

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK081-1` | Menentukan ruang sampel dan kejadian dari eksperimen acak | C3 |
| `PS-Sub-CPMK081-1` | Menerapkan aksioma Kolmogorov dan menurunkan aturan probabilitas darinya | C3 |
| `PS-Sub-CPMK081-1` | Menghitung probabilitas bersyarat dan menerapkan kaidah pencacahan | C3 |

---

## 4.1 Mengapa Arah Berbalik di Sini

Tiga bab pertama menggambarkan **data yang sudah ada**. Mulai bab ini arahnya berbalik: kita membangun **model matematis tentang ketidakpastian**, agar kelak dapat menyimpulkan tentang data yang *belum* kita amati.

```
  Bab 1–3              Bab 4–7              Bab 8–13
  ───────              ───────              ────────
  DESKRIPTIF     →     PROBABILITAS   →     INFERENSIAL
  "apa yang            "apa yang            "apa yang
   terjadi"             mungkin terjadi"     berlaku umum"

  data → ringkasan     model → peluang      sampel → populasi
```

> **Mengapa ini penting bagi Informatika.** Ketika Anda kelak membangun model *machine learning*, keluarannya bukan "kucing" melainkan "probabilitas 0,87 bahwa ini kucing". Tanpa memahami apa arti angka 0,87 itu — dan apa yang **tidak** dikatakannya — Anda tidak dapat menilai apakah model Anda layak dipercaya.

---

## 4.2 Eksperimen Acak, Ruang Sampel, dan Kejadian

### 4.2.1 Definisi

| Istilah | Lambang | Definisi | Contoh Informatika |
|---------|---------|----------|--------------------|
| **Eksperimen acak** | — | Proses yang hasilnya tidak dapat dipastikan sebelumnya | Mengirim satu permintaan HTTP |
| **Ruang sampel** | S atau Ω | Himpunan semua hasil yang mungkin | S = {200, 301, 404, 500} |
| **Titik sampel** | — | Satu anggota ruang sampel | 404 |
| **Kejadian** | A, B, … | Himpunan bagian dari ruang sampel | A = {404, 500} ("gagal") |

### 4.2.2 Contoh dalam Konteks Computing

**Contoh 1 — Pengujian tiga modul.** Setiap modul lulus (L) atau gagal (G).

$$S = \{LLL,\ LLG,\ LGL,\ LGG,\ GLL,\ GLG,\ GGL,\ GGG\}, \quad |S| = 2^3 = 8$$

Kejadian A = "tepat satu modul gagal" = {LLG, LGL, GLL}, |A| = 3.

**Contoh 2 — Penjadwalan tiga proses.**

$$S = \{P_1P_2P_3,\ P_1P_3P_2,\ P_2P_1P_3,\ P_2P_3P_1,\ P_3P_1P_2,\ P_3P_2P_1\}, \quad |S| = 3! = 6$$

```python
from itertools import product, permutations

# Contoh 1
ruang_uji = list(product(["L", "G"], repeat=3))
A = [h for h in ruang_uji if h.count("G") == 1]
print(f"|S| = {len(ruang_uji)}, |A| = {len(A)}")
print(f"P(A) = {len(A)}/{len(ruang_uji)} = {len(A)/len(ruang_uji):.4f}")

# Contoh 2
ruang_jadwal = list(permutations(["P1", "P2", "P3"]))
print(f"\nJumlah urutan penjadwalan: {len(ruang_jadwal)}")
```

> **Asumsi tersembunyi yang sering dilupakan.** Perhitungan P(A) = 3/8 di atas mengandaikan **kedelapan hasil berpeluang sama** — yaitu setiap modul gagal dengan probabilitas 0,5. Bila probabilitas gagal sebenarnya 0,2, perhitungannya berbeda sama sekali.
>
> Menghitung probabilitas sebagai "jumlah hasil menguntungkan dibagi jumlah hasil total" **hanya sah bila seluruh hasil berpeluang sama**. Ini asumsi, bukan aturan umum.

### 4.2.3 Operasi Himpunan pada Kejadian

```
   GABUNGAN  A ∪ B          IRISAN  A ∩ B         KOMPLEMEN  A'
   "A atau B"               "A dan B"             "bukan A"

   ┌─────────────┐          ┌─────────────┐       ┌─────────────┐
   │ ▓▓▓▓▓┌───┐  │          │     ┌───┐   │       │░░░░░┌───┐░░░│
   │ ▓▓A▓▓│▓▓▓│B │          │  A  │▓▓▓│ B │       │░░A░░│   │░B░│
   │ ▓▓▓▓▓└───┘  │          │     └───┘   │       │░░░░░└───┘░░░│
   └─────────────┘          └─────────────┘       └─────────────┘
```

| Notasi | Makna | Contoh |
|--------|-------|--------|
| A ∪ B | A atau B (atau keduanya) | "permintaan gagal ATAU lambat" |
| A ∩ B | A dan B bersamaan | "permintaan gagal DAN lambat" |
| A′ | A tidak terjadi | "permintaan tidak gagal" |
| A ∩ B = ∅ | **Saling lepas** — mustahil bersamaan | "status 200" dan "status 404" |

---

## 4.3 Aksioma Kolmogorov

Seluruh teori probabilitas dibangun dari **tiga aksioma**. Semua aturan lain adalah turunannya — tidak perlu dihafal terpisah.

> **Aksioma 1 (Non-negatif).** Untuk setiap kejadian A: P(A) ≥ 0
>
> **Aksioma 2 (Normalisasi).** P(S) = 1
>
> **Aksioma 3 (Penjumlahan).** Bila A dan B saling lepas: P(A ∪ B) = P(A) + P(B)

### 4.3.1 Menurunkan Aturan Komplemen

Karena A dan A′ saling lepas dan A ∪ A′ = S:

$$P(A) + P(A') = P(A \cup A') = P(S) = 1$$

$$\boxed{P(A') = 1 - P(A)}$$

### 4.3.2 Menurunkan Aturan Penjumlahan Umum

Untuk kejadian yang **tidak** saling lepas, irisannya terhitung dua kali sehingga harus dikurangkan:

$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$$

Untuk tiga kejadian (prinsip inklusi-eksklusi):

$$P(A \cup B \cup C) = P(A)+P(B)+P(C) - P(A\cap B) - P(A\cap C) - P(B\cap C) + P(A\cap B\cap C)$$

### 4.3.3 Batas Probabilitas

Dari Aksioma 1 dan 2: **0 ≤ P(A) ≤ 1** untuk setiap A.

> Bila perhitungan Anda menghasilkan probabilitas negatif atau lebih dari 1, **ada kesalahan** — bukan temuan menarik. Ini pemeriksaan pertama yang harus selalu Anda lakukan.

### 4.3.4 Contoh Terapan

> Dari 500 permintaan API yang dicatat: 60 berstatus galat (G), 85 memakan waktu lebih dari 1 detik (L), dan 25 mengalami keduanya.

$$P(G) = \tfrac{60}{500} = 0{,}12 \qquad P(L) = \tfrac{85}{500} = 0{,}17 \qquad P(G \cap L) = \tfrac{25}{500} = 0{,}05$$

$$P(G \cup L) = 0{,}12 + 0{,}17 - 0{,}05 = 0{,}24$$

$$P(\text{normal}) = P\big((G \cup L)'\big) = 1 - 0{,}24 = 0{,}76$$

```python
total = 500
p_galat = 60 / total
p_lambat = 85 / total
p_irisan = 25 / total

p_gabungan = p_galat + p_lambat - p_irisan
p_normal = 1 - p_gabungan

print(f"P(galat)             = {p_galat:.4f}")
print(f"P(lambat)            = {p_lambat:.4f}")
print(f"P(galat DAN lambat)  = {p_irisan:.4f}")
print(f"P(galat ATAU lambat) = {p_gabungan:.4f}")
print(f"P(normal)            = {p_normal:.4f}")

# Pemeriksaan: keempat wilayah harus berjumlah 1
hanya_galat = p_galat - p_irisan
hanya_lambat = p_lambat - p_irisan
total_cek = hanya_galat + hanya_lambat + p_irisan + p_normal
print(f"\nPemeriksaan total: {total_cek:.6f}  (harus 1)")
```

---

## 4.4 Probabilitas Bersyarat

### 4.4.1 Definisi dan Intuisi

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0$$

Dibaca: "probabilitas A **bila diketahui** B telah terjadi".

**Intuisinya:** mengetahui B telah terjadi berarti **mempersempit ruang sampel** menjadi hanya B. Kita menghitung seberapa besar bagian B yang juga mengandung A.

```
  SEBELUM tahu B           SESUDAH tahu B terjadi
  ┌─────────────────┐       ┌───────┐
  │      ┌───┐      │       │▓▓▓┌───┤  ruang sampel MENYEMPIT
  │  A   │▓▓▓│  B   │  →    │▓▓▓│   │  menjadi B saja
  │      └───┘      │       │A∩B│   │
  └─────────────────┘       └───────┘
   P(A) = A / S              P(A|B) = (A∩B) / B
```

### 4.4.2 Kesalahan Paling Umum dalam Probabilitas Terapan

Melanjutkan kasus API di atas:

$$P(G \mid L) = \frac{0{,}05}{0{,}17} = 0{,}294 \qquad\qquad P(L \mid G) = \frac{0{,}05}{0{,}12} = 0{,}417$$

Kedua angka ini **berbeda**, dan menjawab **pertanyaan yang berbeda**:

- P(G|L) = 0,294 → "dari permintaan yang lambat, 29,4% juga galat"
- P(L|G) = 0,417 → "dari permintaan yang galat, 41,7% juga lambat"

> **Menukar P(A|B) dengan P(B|A) adalah kesalahan paling umum dalam probabilitas terapan**, dan konsekuensinya bisa sangat serius.
>
> "Probabilitas seseorang sakit **bila** hasil tesnya positif" sama sekali berbeda dari "probabilitas hasil tes positif **bila** orangnya sakit". Kekeliruan ini disebut ***confusion of the inverse***, dan dibahas tuntas pada Bab 5.
>
> **Kebiasaan yang menolong:** sebelum menghitung, tuliskan dalam notasi apa yang **diketahui** dan apa yang **ditanya**. Yang diketahui selalu berada di belakang garis vertikal.

### 4.4.3 Aturan Perkalian

Dari definisi probabilitas bersyarat:

$$\boxed{P(A \cap B) = P(B) \cdot P(A \mid B) = P(A) \cdot P(B \mid A)}$$

Untuk tiga kejadian:

$$P(A \cap B \cap C) = P(A) \cdot P(B \mid A) \cdot P(C \mid A \cap B)$$

**Contoh.** Dari 20 tiket bug, 6 bersifat kritis. Dua tiket diambil berturut-turut **tanpa pengembalian**.

$$P(\text{kedua kritis}) = \frac{6}{20} \times \frac{5}{19} = \frac{30}{380} = 0{,}0789$$

```python
# Tanpa pengembalian: probabilitas kedua BERUBAH setelah yang pertama diambil
p_tanpa = (6/20) * (5/19)

# Dengan pengembalian: kejadian menjadi BEBAS
p_dengan = (6/20) * (6/20)

print(f"Tanpa pengembalian : {p_tanpa:.6f}")
print(f"Dengan pengembalian: {p_dengan:.6f}")
print(f"Selisih            : {abs(p_tanpa - p_dengan):.6f}")
```

> Perhatikan mengapa selisihnya ada: pada pengambilan tanpa pengembalian, tiket pertama yang terambil **mengubah komposisi** sisa tiket. Pada pengambilan dengan pengembalian, komposisi kembali seperti semula.

---

## 4.5 Kaidah Pencacahan

Ketika seluruh titik sampel berpeluang sama:

$$P(A) = \frac{|A|}{|S|}$$

Karena itu kita perlu cara **mencacah** tanpa mendaftar satu per satu.

### 4.5.1 Aturan Perkalian

Bila tahap 1 punya n₁ pilihan, tahap 2 punya n₂ pilihan, dan seterusnya, maka total = n₁ × n₂ × … × n_k.

**Contoh — kekuatan kata sandi.** Sandi 8 karakter dari 72 karakter berbeda (26 huruf kecil + 26 huruf besar + 10 angka + 10 simbol):

$$72^8 \approx 7{,}22 \times 10^{14}$$

```python
jumlah_karakter = 26 + 26 + 10 + 10
percobaan_per_detik = 10_000_000_000      # 10 miliar per detik

print(f"{'Panjang':>9}  {'Kemungkinan':>22}  {'Waktu menebak semua':>22}")
for panjang in [6, 8, 10, 12, 16]:
    total = jumlah_karakter ** panjang
    detik = total / percobaan_per_detik
    if detik < 3600:
        waktu = f"{detik:.1f} detik"
    elif detik < 86400 * 365:
        waktu = f"{detik/86400:.1f} hari"
    else:
        waktu = f"{detik/86400/365:.3e} tahun"
    print(f"{panjang:>9}  {total:>22,}  {waktu:>22}")
```

> **Pelajaran keamanan:** setiap karakter tambahan mengalikan ruang pencarian dengan 72. Menambah panjang sandi dari 8 ke 12 karakter menaikkan waktu penebakan sekitar **27 juta kali lipat**. Inilah alasan panjang sandi lebih berpengaruh daripada kerumitannya.

### 4.5.2 Permutasi — Urutan Diperhatikan

$$P(n, r) = \frac{n!}{(n-r)!}$$

**Contoh.** Dari 10 tugas, berapa cara memilih 3 dan menyusunnya ke urutan prioritas pertama, kedua, ketiga?

$$P(10,3) = 10 \times 9 \times 8 = 720$$

### 4.5.3 Kombinasi — Urutan Tidak Diperhatikan

$$C(n, r) = \binom{n}{r} = \frac{n!}{r!\,(n-r)!}$$

**Contoh.** Dari 10 tugas, berapa cara memilih 3 untuk dikerjakan sprint ini?

$$C(10,3) = 120$$

```python
from math import factorial, perm, comb

n, r = 10, 3
print(f"Permutasi P({n},{r}) = {perm(n, r)}    ← urutan penting")
print(f"Kombinasi C({n},{r}) = {comb(n, r)}    ← urutan tidak penting")
print(f"Rasio P/C = {perm(n,r)//comb(n,r)} = {r}! = {factorial(r)}")
```

> **Cara cepat membedakan:** tanyakan *"apakah menukar posisi mengubah hasilnya?"*
>
> - Panitia Ali–Budi–Citra **sama saja** dengan Citra–Budi–Ali → **kombinasi**
> - Ketua Ali/sekretaris Budi **berbeda** dari ketua Budi/sekretaris Ali → **permutasi**

### 4.5.4 Contoh Gabungan

> Sebuah tim terdiri dari 8 pengembang *backend* dan 5 *frontend*. Dipilih 4 orang secara acak. Berapa probabilitas terpilih tepat 2 *backend* dan 2 *frontend*?

$$P = \frac{\binom{8}{2}\binom{5}{2}}{\binom{13}{4}} = \frac{28 \times 10}{715} = 0{,}3916$$

```python
from math import comb

menguntungkan = comb(8, 2) * comb(5, 2)
total = comb(13, 4)
print(f"C(8,2) × C(5,2) = {comb(8,2)} × {comb(5,2)} = {menguntungkan}")
print(f"C(13,4)         = {total}")
print(f"P               = {menguntungkan/total:.6f}")
```

---

## 4.6 Simulasi Monte Carlo

Ketika ragu pada hasil hitungan — atau ketika hitungan analitisnya terlalu rumit — **simulasikan**.

```python
import numpy as np
from math import comb

rng = np.random.default_rng(42)

def simulasi_pilih_tim(n_backend=8, n_frontend=5, n_pilih=4,
                       target=2, ulangan=200_000):
    """Verifikasi hasil analitis dengan simulasi."""
    tim = np.array([1]*n_backend + [0]*n_frontend)
    berhasil = sum(
        rng.choice(tim, size=n_pilih, replace=False).sum() == target
        for _ in range(ulangan)
    )
    return berhasil / ulangan

analitis = comb(8,2) * comb(5,2) / comb(13,4)
simulasi = simulasi_pilih_tim()

print(f"Analitis : {analitis:.6f}")
print(f"Simulasi : {simulasi:.6f}")
print(f"Selisih  : {abs(analitis - simulasi):.6f}")
```

**Hukum Bilangan Besar** menjamin bahwa proporsi hasil simulasi mendekati probabilitas sebenarnya seiring bertambahnya ulangan. Ini bukan kebetulan — ini teorema, dan diperdalam pada Bab 8.

> **Kapan simulasi lebih praktis daripada hitungan analitis:**
> - Ruang sampel terlalu besar untuk dicacah.
> - Ada ketergantungan rumit antar kejadian.
> - Model melibatkan banyak tahap berurutan.
> - Anda ingin memeriksa hasil analitis yang meragukan.

---

## AI Corner — Tingkat Menengah

### Kesalahan Khas AI pada Soal Probabilitas

Model bahasa sangat sering keliru pada probabilitas. Tiga pola kesalahannya cukup dapat diprediksi:

#### (1) Membalik arah persyaratan

Diberi soal "berapa P(A|B)", sebagian model menghitung P(B|A). Kekeliruan ini bahkan sering terjadi pada model yang baik, terutama bila soalnya dirumuskan dengan bahasa sehari-hari.

**Cara memeriksa:** minta AI menuliskan secara eksplisit apa yang diketahui dan apa yang ditanya dalam notasi, sebelum menghitung.

#### (2) Mengandaikan hasil berpeluang sama tanpa memeriksanya

Diberi soal "tiga modul diuji, berapa probabilitas tepat satu gagal", sebagian model langsung menjawab 3/8 — **tanpa memeriksa apakah probabilitas gagal tiap modul memang 0,5**.

**Cara memeriksa:** tanyakan "asumsi apa yang kamu pakai untuk perhitungan itu?"

#### (3) Tertukar permutasi dan kombinasi

Terutama pada soal yang konteksnya tidak lazim.

**Cara memeriksa:** minta AI menjelaskan mengapa urutan penting atau tidak penting dalam soal tersebut.

### Percobaan yang Dianjurkan

Ajukan soal ini kepada sebuah asisten AI:

> *"Dari 500 permintaan API: 60 galat, 85 lambat, 25 keduanya. Jika sebuah permintaan lambat, berapa probabilitas ia juga galat?"*

Jawaban benar: 25/85 = 0,294.

Sebagian model akan menjawab 25/60 = 0,417 — membalik arah persyaratan. Sebagian lagi akan menjawab 25/500 = 0,05 — tidak menyadari bahwa ruang sampel menyempit.

> **Ini bukan alasan untuk tidak memakai AI.** Ini alasan untuk **tetap bisa memeriksanya**. Dan kemampuan memeriksa itu hanya tumbuh bila Anda sendiri menguasai konsepnya.

### Pemakaian yang Dianjurkan

```
PROMPT YANG BAIK:
"Saya menghitung P(galat | lambat) = 25/85 = 0,294 untuk soal ini: [soal].
 Tolong periksa: apakah saya sudah benar mengidentifikasi mana yang
 diketahui dan mana yang ditanya? Apa asumsi yang saya pakai?"

Mengapa baik: Anda sudah mengerjakan, sudah punya jawaban, dan meminta
AI memeriksa PENALARAN — bukan memberi jawaban.
```

---

## Latihan Soal

### Tingkat Dasar

1. Sebuah sistem memiliki tiga server yang masing-masing dapat aktif (A) atau mati (M).
   (a) Tuliskan ruang sampelnya.
   (b) Berapa |S|?
   (c) Tuliskan kejadian "sedikitnya dua server aktif".
   (d) Hitung probabilitasnya, dengan menyebutkan asumsi yang Anda pakai.

2. Tuliskan tiga aksioma Kolmogorov, lalu turunkan aturan komplemen darinya.

3. Dari 1.000 sesi pengguna: 220 membuka halaman produk (A), 130 menambahkan ke keranjang (B), 80 melakukan keduanya. Hitung:
   (a) P(A), (b) P(B), (c) P(A ∩ B), (d) P(A ∪ B), (e) P(tidak melakukan keduanya).

4. Untuk data soal 3, hitung P(B|A) dan P(A|B). Jelaskan dalam kalimat apa arti masing-masing.

5. Hitung: (a) P(8,3), (b) C(8,3), (c) berapa kali lipat P(8,3) dibanding C(8,3), dan mengapa.

### Tingkat Menengah

6. PIN ATM terdiri dari 6 digit angka. Berapa banyak PIN yang mungkin bila:
   (a) digit boleh berulang;
   (b) digit tidak boleh berulang;
   (c) tidak boleh ada dua digit berurutan yang sama;
   (d) harus mengandung sekurang-kurangnya satu angka 0?

7. Sebuah *code review* memilih 3 penelaah dari 12 anggota tim.
   (a) Berapa cara memilih tim penelaah?
   (b) Berapa probabilitas seorang anggota tertentu terpilih?
   (c) Berapa probabilitas dua anggota tertentu terpilih bersama?
   (d) Bila urutan penelaah pertama, kedua, ketiga dibedakan, berapa jawaban (a)?

8. Dari 20 tiket bug, 6 kritis. Tiga tiket diambil berturut-turut tanpa pengembalian.
   (a) Hitung P(ketiganya kritis).
   (b) Hitung P(tidak ada yang kritis).
   (c) Hitung P(sedikitnya satu kritis) dengan cara tercepat.
   (d) Bandingkan (a) dengan kasus pengambilan **dengan** pengembalian. Jelaskan selisihnya.

9. Jelaskan mengapa P(A|B) ≠ P(B|A) dengan satu contoh dari konteks Informatika yang **bukan** dari bab ini. Hitung kedua nilainya.

### Tingkat Mahir

10. Buktikan prinsip inklusi-eksklusi untuk tiga kejadian:
    P(A∪B∪C) = ΣP − ΣP(irisan berpasangan) + P(A∩B∩C)
    (a) Berikan bukti dengan diagram Venn.
    (b) Verifikasi dengan contoh numerik yang Anda buat sendiri.

11. Sebuah sistem pemeriksaan sandi menolak sandi yang mengandung kata dari kamus 10.000 kata, atau yang lebih pendek dari 10 karakter.
    (a) Berapa banyak sandi 10 karakter yang mungkin dari 72 karakter?
    (b) Perkirakan berapa banyak yang ditolak karena mengandung kata kamus. Nyatakan asumsi yang Anda pakai.
    (c) Berapa persen ruang sandi yang tersisa?
    (d) Apakah pembatasan ini secara praktis menurunkan keamanan? Jelaskan.

12. Rancang dan jalankan sebuah simulasi Monte Carlo untuk salah satu persoalan berikut, lalu bandingkan dengan hitungan analitis bila memungkinkan:
    (a) Probabilitas sedikitnya dua dari 30 mahasiswa berulang tahun sama.
    (b) Probabilitas sebuah *hash table* berukuran 1.000 mengalami tabrakan setelah 50 penyisipan.
    (c) Probabilitas semua dari 8 mikroservis hidup bersamaan, bila masing-masing andal 99,2% dan **saling bebas**.
    Laporkan: rumusan masalah, kode, hasil, dan estimasi ketidakpastian simulasi.

---

## Rangkuman

1. **Eksperimen acak** menghasilkan **ruang sampel** S; **kejadian** adalah himpunan bagian dari S.
2. Seluruh teori probabilitas berdiri di atas **tiga aksioma Kolmogorov**. Aturan komplemen dan penjumlahan adalah turunannya.
3. Rumus P(A) = |A|/|S| **hanya sah bila seluruh hasil berpeluang sama** — ini asumsi yang harus diperiksa.
4. **Aturan penjumlahan umum:** P(A∪B) = P(A) + P(B) − P(A∩B).
5. Probabilitas selalu berada antara 0 dan 1. Hasil di luar rentang itu berarti **ada kesalahan hitung**.
6. **Probabilitas bersyarat** P(A|B) mempersempit ruang sampel menjadi B saja.
7. **P(A|B) ≠ P(B|A).** Menukarnya adalah kesalahan paling umum dalam probabilitas terapan.
8. **Aturan perkalian:** P(A∩B) = P(A)·P(B|A). Pengambilan tanpa pengembalian mengubah probabilitas tahap berikutnya.
9. **Permutasi** memperhatikan urutan; **kombinasi** tidak. Tanyakan: "apakah menukar posisi mengubah hasilnya?"
10. **Simulasi Monte Carlo** memeriksa hitungan analitis secara empiris, dijamin oleh Hukum Bilangan Besar.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 2. Pearson.
2. Ross, S. M. (2019). *A First Course in Probability* (10th ed.), Bab 1–3. Pearson.
3. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 2. Wiley.
4. Kolmogorov, A. N. (1933). *Grundbegriffe der Wahrscheinlichkeitsrechnung*. Springer.
5. Dokumentasi Python `itertools` — <https://docs.python.org/3/library/itertools.html>
6. Dokumentasi Python `math` — <https://docs.python.org/3/library/math.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
