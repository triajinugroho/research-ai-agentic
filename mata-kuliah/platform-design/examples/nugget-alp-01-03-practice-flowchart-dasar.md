---
id: "nugget-alp-01-09"
title: "Latihan: Membuat Flowchart Dasar"
course: "alp"
week: 1
sequence: 9
type: "practice"
topic_slug: "flowchart-dasar"

cpmk: ["CPMK-1"]
sub_cpmk: ["CPMK-1.3"]
bloom_level: "C3"
difficulty: 2
estimated_minutes: 10

prerequisites: ["nugget-alp-01-05", "nugget-alp-01-06"]
related: ["nugget-alp-01-01", "nugget-alp-01-02"]
cross_course: []

modality: ["text", "diagram", "code"]
has_interactive_code: true
has_quiz: true
quiz_count: 3

review_priority: "high"
key_concepts:
  - "Simbol-simbol flowchart"
  - "Menerjemahkan masalah ke flowchart"
  - "Dari flowchart ke pseudocode"

tags: ["flowchart", "representasi-algoritma", "pseudocode", "latihan"]
---

# Latihan: Membuat Flowchart Dasar

> **Tujuan:** Setelah menyelesaikan latihan ini, kamu mampu **menerapkan** simbol flowchart untuk merepresentasikan algoritma sederhana.

---

## Recall: Simbol Flowchart

Sebelum mulai, ingat kembali simbol-simbol utama:

```
  ╭──────────╮
  │ TERMINAL │  = Mulai / Selesai (oval)
  ╰──────────╯

  ┌──────────┐
  │ PROCESS  │  = Pemrosesan / Perhitungan (persegi panjang)
  └──────────┘

  ╱            ╲
 ╱  INPUT/OUT   ╲  = Masukan / Keluaran (jajar genjang)
 ╲              ╱
  ╲            ╱

      ◇
     ╱ ╲
    ╱   ╲         = Keputusan / Decision (belah ketupat)
    ╲   ╱
     ╲ ╱
```

---

## Tantangan 1: Ganjil atau Genap

**Masalah:** Buat flowchart untuk program yang membaca satu bilangan bulat, lalu menentukan apakah bilangan tersebut ganjil atau genap.

**Hints tersedia — coba dulu sebelum membuka!**

<details>
<summary>Hint 1: Langkah-langkah utama</summary>

1. Mulai
2. Baca bilangan
3. Cek: apakah bilangan habis dibagi 2?
4. Jika ya → tampilkan "Genap"
5. Jika tidak → tampilkan "Ganjil"
6. Selesai

</details>

<details>
<summary>Hint 2: Flowchart dalam ASCII</summary>

```
        ╭───────╮
        │ MULAI │
        ╰───┬───╯
            │
    ╱───────────────╲
   ╱ BACA bilangan   ╲
   ╲                  ╱
    ╲────────┬───────╱
             │
         ◇───────◇
        ╱         ╲
       ╱ bilangan  ╲
      ╱  % 2 == 0?  ╲
      ╲             ╱
       ╲    ╱──╲   ╱
        ╲──╱    ╲─╱
       Ya│       │Tidak
         │       │
   ╱─────────╲  ╱─────────╲
  ╱ TAMPILKAN ╲╱ TAMPILKAN  ╲
  ╲  "Genap"  ╱╲  "Ganjil"  ╱
   ╲─────────╱  ╲───────────╱
         │            │
         └──────┬─────┘
                │
        ╭───────────╮
        │  SELESAI  │
        ╰───────────╯
```

</details>

<details>
<summary>Hint 3: Pseudocode lengkap</summary>

```
MULAI
  BACA bilangan
  JIKA bilangan MOD 2 == 0 MAKA
    TAMPILKAN "Genap"
  SELAINNYA
    TAMPILKAN "Ganjil"
SELESAI
```

</details>

**Sekarang implementasikan dalam Python:**

```python
# Tantangan 1: Ganjil atau Genap
# Terjemahkan flowchart/pseudocode di atas ke kode Python

bilangan = int(input("Masukkan bilangan: "))

# Tulis kode kamu di sini:
# ...
```

<details>
<summary>Solusi Python</summary>

```python
bilangan = int(input("Masukkan bilangan: "))

if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan GENAP")
else:
    print(f"{bilangan} adalah bilangan GANJIL")
```

</details>

---

## Tantangan 2: Hitung Ongkos Ojol

**Masalah:** Buat pseudocode untuk menghitung ongkos ojek online dengan aturan:
- Tarif dasar: Rp10.000 (untuk 4 km pertama)
- Tarif per km setelah 4 km: Rp2.500/km
- Jika jarak > 20 km, tambah surcharge Rp5.000

**Contoh:**
- Jarak 3 km → Rp10.000
- Jarak 10 km → Rp10.000 + (6 × Rp2.500) = Rp25.000
- Jarak 25 km → Rp10.000 + (21 × Rp2.500) + Rp5.000 = Rp67.500

<details>
<summary>Hint 1: Identifikasi variabel</summary>

- Input: `jarak` (km)
- Proses: hitung tarif berdasarkan kondisi
- Output: `total_tarif` (Rupiah)

</details>

<details>
<summary>Hint 2: Pseudocode</summary>

```
MULAI
  BACA jarak
  tarif_dasar = 10000

  JIKA jarak <= 4 MAKA
    total = tarif_dasar
  SELAINNYA
    km_lebih = jarak - 4
    total = tarif_dasar + (km_lebih * 2500)
    JIKA jarak > 20 MAKA
      total = total + 5000

  TAMPILKAN "Total ongkos: Rp" + total
SELESAI
```

</details>

```python
# Tantangan 2: Hitung Ongkos Ojol
# Implementasikan algoritma di atas

jarak = float(input("Masukkan jarak (km): "))

# Tulis kode kamu di sini:
# ...
```

<details>
<summary>Solusi Python</summary>

```python
jarak = float(input("Masukkan jarak (km): "))

tarif_dasar = 10000

if jarak <= 4:
    total = tarif_dasar
else:
    km_lebih = jarak - 4
    total = tarif_dasar + (km_lebih * 2500)
    if jarak > 20:
        total += 5000

print(f"Jarak: {jarak} km")
print(f"Total ongkos: Rp{total:,.0f}")
```

</details>

---

## Cek Pemahaman

**Soal 1** (C2 — Understand):
Simbol belah ketupat (diamond) dalam flowchart digunakan untuk:

- A) Menandakan awal/akhir program
- B) Operasi input/output
- C) Pengambilan keputusan (decision) ✓
- D) Pemrosesan/perhitungan

**Soal 2** (C3 — Apply):
Jika `jarak = 15` km dalam algoritma ongkos ojol, berapa total tarifnya?

- A) Rp10.000
- B) Rp25.000
- C) Rp37.500 ✓
- D) Rp42.500

> **Penjelasan:** jarak > 4 km, jadi: 10.000 + (11 × 2.500) = 10.000 + 27.500 = **Rp37.500**. Jarak ≤ 20 km, jadi tidak ada surcharge.

**Soal 3** (C3 — Apply):
Tulis pseudocode untuk menentukan apakah sebuah tahun adalah **tahun kabisat**. Aturan: habis dibagi 4, KECUALI habis dibagi 100 (bukan kabisat), KECUALI habis dibagi 400 (kabisat).

> **Ini soal terbuka.** Kerjakan di kertas/notebook, lalu bandingkan dengan solusi.

<details>
<summary>Contoh Jawaban</summary>

```
MULAI
  BACA tahun
  JIKA tahun MOD 400 == 0 MAKA
    TAMPILKAN "Kabisat"
  SELAINNYA JIKA tahun MOD 100 == 0 MAKA
    TAMPILKAN "Bukan Kabisat"
  SELAINNYA JIKA tahun MOD 4 == 0 MAKA
    TAMPILKAN "Kabisat"
  SELAINNYA
    TAMPILKAN "Bukan Kabisat"
SELESAI
```

</details>

---

## Refleksi

Sebelum lanjut, jawab dalam 1-2 kalimat:

> *"Menurut kamu, mengapa penting membuat flowchart/pseudocode SEBELUM menulis kode Python?"*

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
