# BAB 1: PENGANTAR ALGORITMA DAN COMPUTATIONAL THINKING

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| CPMK-1.1 | Mendefinisikan konsep algoritma dan sejarahnya | C1 (Mengingat) |
| CPMK-1.2 | Menjelaskan 4 pilar computational thinking | C2 (Memahami) |
| CPMK-1.3 | Membuat flowchart dan pseudocode sederhana | C3 (Menerapkan) |
| CPMK-1.4 | Menjelaskan peran pemrograman di era AI | C2 (Memahami) |

**Estimasi Waktu:** 3 × 50 menit (3 SKS)

**Prasyarat:** Tidak ada (bab pembuka).

---

## 1.1 Apa Itu Algoritma?

### 1.1.1 Definisi dan Sejarah

Kata **"algoritma"** berasal dari nama seorang ilmuwan Muslim yang sangat berpengaruh: **Muhammad ibn Musa al-Khwarizmi** (±780–850 M). Beliau adalah seorang matematikawan, astronomer, dan geograf dari Persia yang bekerja di **Bayt al-Hikmah** (House of Wisdom) di Baghdad pada masa Kekhalifahan Abbasiyah.

> **Warisan Al-Khwarizmi:**
> - Karya beliau *"Kitab al-Jabr wal-Muqabala"* melahirkan kata **"aljabar"** (algebra).
> - Nama beliau, "al-Khwarizmi", dilatinkan menjadi "Algoritmi" dan kemudian menjadi kata **"algoritma"** (algorithm).
> - Beliau memperkenalkan sistem angka Hindu-Arab ke dunia Barat melalui karyanya *"Liber Algorismi"*.
> - Ini adalah warisan peradaban Islam yang luar biasa dalam dunia ilmu pengetahuan dan teknologi.

Secara formal, **algoritma** adalah:

> Urutan langkah-langkah **terbatas**, **terdefinisi dengan jelas**, dan **efektif** untuk menyelesaikan suatu masalah atau mencapai tujuan tertentu.

Definisi ini dapat dipecah menjadi beberapa kata kunci:

| Kata Kunci | Penjelasan |
|-----------|------------|
| **Urutan langkah** | Ada langkah 1, langkah 2, dan seterusnya — bukan acak |
| **Terbatas** | Algoritma harus berhenti setelah sejumlah langkah tertentu (finiteness) |
| **Terdefinisi jelas** | Setiap langkah harus tidak ambigu (definiteness) |
| **Efektif** | Setiap langkah harus bisa dilaksanakan (effectiveness) |

### 1.1.2 Karakteristik Algoritma

Donald Knuth, salah satu ilmuwan komputer terbesar, mendefinisikan lima karakteristik utama algoritma:

```
┌─────────────────────────────────────────────────────┐
│              5 KARAKTERISTIK ALGORITMA               │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. FINITENESS (Keterbatasan)                       │
│     → Algoritma harus berhenti setelah              │
│       sejumlah langkah yang terbatas                │
│                                                     │
│  2. DEFINITENESS (Ketegasan)                        │
│     → Setiap langkah harus didefinisikan            │
│       secara tepat dan tidak ambigu                 │
│                                                     │
│  3. INPUT (Masukan)                                 │
│     → Algoritma menerima nol atau lebih             │
│       nilai masukan dari luar                       │
│                                                     │
│  4. OUTPUT (Keluaran)                               │
│     → Algoritma menghasilkan satu atau              │
│       lebih nilai keluaran                          │
│                                                     │
│  5. EFFECTIVENESS (Efektivitas)                     │
│     → Setiap langkah harus cukup sederhana          │
│       untuk bisa dilaksanakan                       │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 1.1.3 Contoh Algoritma dalam Kehidupan Sehari-hari

Algoritma bukan hanya konsep komputer — kita menggunakan algoritma setiap hari tanpa menyadarinya.

**Contoh 1: Resep Rendang**

```
ALGORITMA: Memasak Rendang Sederhana
========================================
1. MULAI
2. Siapkan bahan: daging sapi 1 kg, santan 1 liter, bumbu halus
3. Panaskan santan dalam wajan besar hingga mendidih
4. Masukkan bumbu halus, aduk rata
5. Masukkan daging sapi
6. Masak dengan api sedang sambil sesekali diaduk
7. SELAMA santan belum menyusut:
   7.1 Aduk perlahan setiap 10 menit
   7.2 Periksa kematangan daging
8. JIKA daging sudah empuk DAN santan sudah meresap:
   8.1 Kecilkan api
   8.2 Aduk terus hingga bumbu kering dan daging berwarna cokelat gelap
9. Angkat dan sajikan
10. SELESAI
```

Perhatikan bahwa resep di atas memiliki kelima karakteristik algoritma: ada urutan langkah yang jelas, terbatas (akan selesai), setiap langkah terdefinisi, ada input (bahan), dan ada output (rendang).

**Contoh 2: Navigasi dari Kampus UAI ke Stasiun MRT**

```
ALGORITMA: Rute Kampus UAI → Stasiun MRT Blok M
=================================================
1. MULAI
2. Keluar dari gedung kampus UAI
3. Belok kiri ke Jl. Sisingamangaraja
4. Jalan lurus ± 500 meter ke arah selatan
5. JIKA ada lampu merah:
   5.1 Tunggu hingga lampu hijau
   5.2 Seberangi jalan dengan hati-hati
6. Masuk ke kompleks Blok M Plaza
7. Ikuti penunjuk arah menuju Stasiun MRT
8. Sampai di Stasiun MRT Blok M
9. SELESAI
```

**Contoh 3: Antrian di Puskesmas**

```
ALGORITMA: Sistem Antrian Puskesmas
=====================================
1. MULAI
2. Pasien datang dan mengambil nomor antrian
3. Pasien menunggu di ruang tunggu
4. SELAMA nomor pasien belum dipanggil:
   4.1 Tunggu panggilan dari petugas
5. Nomor pasien dipanggil
6. Pasien masuk ke ruang periksa
7. Dokter memeriksa pasien
8. JIKA pasien perlu obat:
   8.1 Dokter menulis resep
   8.2 Pasien ke apotek untuk mengambil obat
9. JIKA TIDAK:
   9.1 Pasien langsung pulang
10. SELESAI
```

> **Refleksi:** Perhatikan pola yang muncul di semua contoh: ada langkah berurutan, ada pengambilan keputusan (JIKA), dan ada pengulangan (SELAMA). Ketiga pola ini — **urutan (sequence)**, **seleksi (selection/branching)**, dan **perulangan (iteration/loop)** — adalah tiga struktur dasar yang dapat membangun SEMUA algoritma. Kita akan mempelajari ini secara mendalam di Bab 3 dan Bab 4.

---

## 1.2 Computational Thinking: Berpikir Seperti Programmer

**Computational thinking** (pemikiran komputasional) adalah kemampuan berpikir secara sistematis untuk menyelesaikan masalah — dengan atau tanpa komputer. Ini bukan hanya tentang "coding", melainkan tentang **cara berpikir**.

> "Computational thinking is the thought processes involved in formulating a problem and expressing its solution(s) in such a way that a computer — human or machine — can effectively carry out."
> — Jeannette M. Wing (2006)

Computational thinking terdiri dari **4 pilar** utama:

```
┌─────────────────────────────────────────────────────────────┐
│                   4 PILAR COMPUTATIONAL THINKING             │
├──────────────┬──────────────┬──────────────┬────────────────┤
│              │              │              │                │
│ DECOMPOSITION│   PATTERN    │  ABSTRACTION │   ALGORITHM    │
│              │ RECOGNITION  │              │    DESIGN      │
│              │              │              │                │
│  Memecah     │  Mengenali   │  Fokus pada  │  Merancang     │
│  masalah     │  pola yang   │  hal penting,│  langkah-      │
│  besar       │  berulang    │  abaikan     │  langkah       │
│  menjadi     │              │  detail yang │  penyelesaian  │
│  bagian      │              │  tidak       │                │
│  kecil       │              │  relevan     │                │
│              │              │              │                │
└──────────────┴──────────────┴──────────────┴────────────────┘
```

### 1.2.1 Decomposition (Dekomposisi)

**Dekomposisi** adalah proses memecah masalah yang besar dan kompleks menjadi bagian-bagian yang lebih kecil dan mudah dikelola.

**Analogi:** Bayangkan Anda harus memasak nasi goreng lengkap untuk 50 orang. Tugas ini terasa besar! Tetapi jika Anda memecahnya:

```
Memasak Nasi Goreng 50 Porsi
├── 1. Persiapan bahan (tim 1)
│   ├── Cuci dan potong sayuran
│   ├── Siapkan protein (ayam/telur)
│   └── Siapkan bumbu
├── 2. Memasak nasi (tim 2)
│   ├── Cuci beras
│   ├── Masak nasi (perlu dingin/semalam)
│   └── Dinginkan nasi
├── 3. Memasak nasi goreng (tim 3)
│   ├── Tumis bumbu
│   ├── Masukkan protein
│   ├── Masukkan nasi dan aduk rata
│   └── Tambahkan kecap dan penyedap
└── 4. Penyajian (tim 4)
    ├── Siapkan piring
    ├── Beri garnish (kerupuk, acar)
    └── Sajikan
```

Setiap sub-masalah kini lebih mudah ditangani dan bisa dikerjakan secara paralel oleh tim yang berbeda.

**Contoh dalam pemrograman:** Membuat aplikasi kasir warung:

```
Aplikasi Kasir Warung
├── Input: memasukkan data barang
├── Proses: menghitung total harga
│   ├── Hitung subtotal per barang
│   ├── Hitung diskon (jika ada)
│   └── Hitung total akhir
├── Output: menampilkan struk belanja
└── Penyimpanan: menyimpan transaksi
```

### 1.2.2 Pattern Recognition (Pengenalan Pola)

**Pengenalan pola** adalah kemampuan menemukan kesamaan, keteraturan, atau tren dalam data atau masalah.

**Contoh kehidupan nyata:**
- Seorang pedagang di Pasar Tanah Abang mengenali bahwa penjualan baju meningkat menjelang Lebaran → **pola musiman**
- Tarif TransJakarta sama untuk semua jarak → **pola tarif flat**
- Harga Indomie di berbagai warung relatif sama → **pola harga stabil**

**Contoh dalam pemrograman:**

Perhatikan perhitungan berikut:
```
Harga barang A: 15000, jumlah: 3 → subtotal: 45000
Harga barang B: 25000, jumlah: 2 → subtotal: 50000
Harga barang C: 8000,  jumlah: 5 → subtotal: 40000
```

Polanya jelas: `subtotal = harga × jumlah`. Dengan mengenali pola ini, kita cukup menulis **satu rumus** yang berlaku untuk semua barang, bukan menghitung satu per satu.

### 1.2.3 Abstraction (Abstraksi)

**Abstraksi** adalah proses menyaring informasi — fokus pada hal-hal yang penting dan mengabaikan detail yang tidak relevan untuk masalah yang sedang diselesaikan.

**Analogi Peta:** Peta Jakarta menunjukkan jalan dan landmark, tetapi tidak menunjukkan setiap pohon, setiap orang, atau setiap lubang di jalan. Peta adalah **abstraksi** dari dunia nyata — hanya menampilkan informasi yang relevan untuk navigasi.

**Contoh dalam pemrograman:**

Jika kita membuat sistem data mahasiswa, kita perlu memutuskan informasi apa yang **relevan**:

| Relevan (disimpan) | Tidak relevan (diabaikan) |
|---------------------|---------------------------|
| Nama | Warna baju favorit |
| NIM | Hobi |
| Program studi | Makanan kesukaan |
| IPK | Tinggi badan |
| Semester | Jumlah followers Instagram |

Abstraksi membantu kita **menyederhanakan** masalah agar lebih mudah dimodelkan dan dipecahkan.

### 1.2.4 Algorithm Design (Perancangan Algoritma)

Setelah masalah didekomposisi, pola dikenali, dan abstraksi dilakukan, langkah terakhir adalah **merancang algoritma** — yaitu langkah-langkah sistematis untuk menyelesaikan masalah.

**Contoh:** Algoritma menghitung rata-rata nilai mahasiswa:

```
ALGORITMA: Hitung Rata-rata Nilai
==================================
1. MULAI
2. Masukkan jumlah mahasiswa (n)
3. Set total_nilai = 0
4. UNTUK setiap mahasiswa ke-i dari 1 sampai n:
   4.1 Masukkan nilai mahasiswa ke-i
   4.2 Tambahkan nilai ke total_nilai
5. Hitung rata_rata = total_nilai / n
6. Tampilkan rata_rata
7. SELESAI
```

> **Keterkaitan 4 Pilar:**
> Keempat pilar ini tidak terpisah — mereka bekerja bersama. Ketika menghadapi masalah:
> 1. **Dekomposisi** dulu masalahnya
> 2. Cari **pola** di sub-masalah
> 3. Lakukan **abstraksi** untuk fokus pada inti masalah
> 4. **Rancang algoritma** untuk setiap bagian

---

## 1.3 Representasi Algoritma

Ada tiga cara umum merepresentasikan algoritma sebelum kita menulis kode program:

### 1.3.1 Bahasa Natural (Deskriptif)

Cara paling sederhana: menuliskan langkah-langkah dalam bahasa sehari-hari. Contohnya sudah kita lihat di bagian 1.1.3.

**Kelebihan:** Mudah dipahami siapa saja.
**Kekurangan:** Bisa ambigu dan tidak presisi.

### 1.3.2 Pseudocode

**Pseudocode** (kode semu) adalah representasi algoritma yang menggunakan campuran bahasa natural dan struktur yang menyerupai bahasa pemrograman, tetapi tidak terikat pada sintaks bahasa tertentu.

**Konvensi pseudocode yang kita gunakan:**

| Elemen | Konvensi | Contoh |
|--------|----------|--------|
| Kata kunci | HURUF KAPITAL | MULAI, SELESAI, JIKA, SELAMA |
| Variabel | huruf_kecil_dengan_underscore | total_nilai, jumlah_mahasiswa |
| Assignment | ← atau = | total ← 0 |
| Input | BACA / INPUT | BACA nama |
| Output | TULIS / TAMPILKAN | TULIS "Halo" |
| Seleksi | JIKA...MAKA...JIKA TIDAK | JIKA x > 0 MAKA ... |
| Perulangan | SELAMA / UNTUK | SELAMA i < n LAKUKAN ... |
| Komentar | // | // ini komentar |
| Indentasi | 2-4 spasi | Menunjukkan blok |

**Contoh Pseudocode — Menentukan Ganjil/Genap:**

```
ALGORITMA CekGanjilGenap
// Menentukan apakah bilangan ganjil atau genap

MULAI
    TULIS "Masukkan bilangan: "
    BACA bilangan

    JIKA bilangan MOD 2 = 0 MAKA
        TULIS bilangan, " adalah bilangan GENAP"
    JIKA TIDAK
        TULIS bilangan, " adalah bilangan GANJIL"
    AKHIR JIKA
SELESAI
```

**Contoh Pseudocode — Mencari Nilai Terbesar:**

```
ALGORITMA CariNilaiTerbesar
// Mencari nilai tertinggi dari sekumpulan nilai mahasiswa

MULAI
    TULIS "Masukkan jumlah mahasiswa: "
    BACA n

    TULIS "Masukkan nilai mahasiswa ke-1: "
    BACA nilai
    maks ← nilai

    UNTUK i ← 2 SAMPAI n LAKUKAN
        TULIS "Masukkan nilai mahasiswa ke-", i, ": "
        BACA nilai
        JIKA nilai > maks MAKA
            maks ← nilai
        AKHIR JIKA
    AKHIR UNTUK

    TULIS "Nilai tertinggi adalah: ", maks
SELESAI
```

### 1.3.3 Flowchart (Diagram Alir)

**Flowchart** adalah representasi visual algoritma menggunakan simbol-simbol standar yang dihubungkan oleh anak panah (arrow) untuk menunjukkan alur eksekusi.

**Simbol-simbol Flowchart Standar:**

```
┌──────────────┬─────────────────┬──────────────────────────────┐
│   Simbol     │  Bentuk         │  Fungsi                      │
├──────────────┼─────────────────┼──────────────────────────────┤
│              │  ╭──────────╮   │                              │
│  Terminator  │  │          │   │  Awal (MULAI) atau           │
│              │  ╰──────────╯   │  Akhir (SELESAI) program     │
├──────────────┼─────────────────┼──────────────────────────────┤
│              │  ┌──────────┐   │                              │
│  Proses      │  │          │   │  Pemrosesan / perhitungan    │
│              │  └──────────┘   │  (assignment, operasi)       │
├──────────────┼─────────────────┼──────────────────────────────┤
│              │  ╱╲             │                              │
│  Keputusan   │ ╱  ╲            │  Percabangan (Ya/Tidak)      │
│  (Decision)  │ ╲  ╱            │  berdasarkan kondisi         │
│              │  ╲╱             │                              │
├──────────────┼─────────────────┼──────────────────────────────┤
│              │  ╱──────────╱   │                              │
│  Input/      │ ╱          ╱    │  Memasukkan atau             │
│  Output      │╱──────────╱     │  menampilkan data            │
├──────────────┼─────────────────┼──────────────────────────────┤
│              │       │         │                              │
│  Anak Panah  │       ▼         │  Arah alur eksekusi          │
│  (Arrow)     │                 │                              │
└──────────────┴─────────────────┴──────────────────────────────┘
```

**Contoh Flowchart — Menentukan Kelulusan:**

```
        ╭──────────╮
        │  MULAI   │
        ╰────┬─────╯
             │
             ▼
     ╱───────────────╱
    ╱  Input: nilai  ╱
   ╱───────────────╱
             │
             ▼
          ╱╲
         ╱  ╲
        ╱nilai╲──── Ya ──→ ┌──────────────────┐
        ╲>=60 ╱             │ status = "LULUS" │
         ╲  ╱              └────────┬─────────┘
          ╲╱                        │
           │ Tidak                  │
           ▼                        │
   ┌────────────────────┐           │
   │status = "TIDAK     │           │
   │         LULUS"     │           │
   └────────┬───────────┘           │
            │                       │
            └──────────┬────────────┘
                       │
                       ▼
            ╱────────────────╱
           ╱ Output: status  ╱
          ╱────────────────╱
                       │
                       ▼
              ╭──────────╮
              │  SELESAI │
              ╰──────────╯
```

**Contoh Flowchart — Menghitung Total Belanja:**

```
         ╭──────────╮
         │  MULAI   │
         ╰────┬─────╯
              │
              ▼
      ┌───────────────┐
      │  total = 0    │
      └───────┬───────┘
              │
              ▼
          ╱╲
         ╱  ╲
        ╱ada  ╲── Tidak ──→ ╱──────────────────╱
        ╲barang╱             ╱ Output: total     ╱
         ╲lagi╱             ╱──────────────────╱
          ╲╱                        │
           │ Ya                     ▼
           ▼                ╭──────────╮
   ╱───────────────╱        │  SELESAI │
  ╱  Input: harga, ╱        ╰──────────╯
 ╱   jumlah       ╱
╱───────────────╱
           │
           ▼
   ┌───────────────────────┐
   │ subtotal = harga ×    │
   │            jumlah     │
   │ total = total +       │
   │         subtotal      │
   └───────────┬───────────┘
               │
               └──── (kembali ke cek "ada barang lagi?")
```

> **Tips Membuat Flowchart yang Baik:**
> 1. Selalu mulai dengan **MULAI** dan akhiri dengan **SELESAI**
> 2. Gunakan simbol yang tepat untuk setiap jenis operasi
> 3. Alur panah harus jelas — jangan ada alur yang "menggantung"
> 4. Setiap simbol keputusan (diamond) harus memiliki **dua cabang** (Ya/Tidak)
> 5. Jaga agar flowchart tetap rapi dan mudah dibaca dari atas ke bawah

---

## 1.4 Mengapa Python?

### 1.4.1 Perbandingan Bahasa Pemrograman

Di dunia pemrograman ada ratusan bahasa. Mengapa kita memilih Python?

| Kriteria | Python | C | Java | JavaScript |
|----------|--------|---|------|------------|
| **Kesulitan belajar** | Mudah | Sulit | Menengah | Menengah |
| **Sintaks** | Sangat ringkas | Verbose | Verbose | Menengah |
| **Tipe data** | Dynamic typing | Static typing | Static typing | Dynamic typing |
| **Penggunaan utama** | AI/ML, Data Science, Web, Scripting | Sistem operasi, embedded | Enterprise, Android | Web frontend/backend |
| **Hello World** | 1 baris | 5+ baris | 5+ baris | 1 baris |
| **Popularitas (2025)** | #1 (TIOBE) | #2 | #3 | #6 |
| **Kebutuhan industri AI** | Sangat tinggi | Rendah | Menengah | Menengah |

**Perbandingan "Hello World":**

```python
# Python - 1 baris!
print("Hello, World!")
```

```c
// C - 5 baris
#include <stdio.h>
int main() {
    printf("Hello, World!\n");
    return 0;
}
```

```java
// Java - 5 baris
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Python dirancang dengan filosofi **keterbacaan** (readability). Penciptanya, **Guido van Rossum**, menginginkan bahasa yang "mudah dibaca dan ditulis, seperti menulis dalam bahasa Inggris". Ini membuat Python sangat cocok untuk pemula.

### 1.4.2 Python di Era AI dan Industri

Python bukan hanya bahasa untuk pemula — Python adalah bahasa yang paling banyak digunakan di industri AI dan data science:

- **TensorFlow, PyTorch, scikit-learn** — framework AI/ML utama berbasis Python
- **NumPy, Pandas** — library analisis data standar industri
- **Django, Flask, FastAPI** — framework web Python populer
- **Google, Netflix, Instagram, Spotify** — menggunakan Python secara ekstensif

Di Indonesia:
- **Tokopedia, Gojek, Traveloka** — menggunakan Python untuk data engineering dan ML
- **Bootcamp coding** di Indonesia (Hacktiv8, Purwadhika) mengajarkan Python
- Permintaan kerja **Python developer** di Indonesia terus meningkat

### 1.4.3 Program Python Pertama

Mari kita tulis program Python pertama di Google Colab:

```python
# Program pertama kita!
# Menampilkan sapaan dalam Bahasa Indonesia

print("Assalamu'alaikum!")
print("Selamat datang di mata kuliah Algoritma dan Pemrograman")
print("Program Studi Informatika - Universitas Al Azhar Indonesia")
print()

# Menampilkan identitas
nama = "Ahmad"
nim = "2025001"
prodi = "Informatika"

print(f"Nama  : {nama}")
print(f"NIM   : {nim}")
print(f"Prodi : {prodi}")
print()

# Perhitungan sederhana
tahun_masuk = 2025
tahun_sekarang = 2026
semester = (tahun_sekarang - tahun_masuk) * 2  # semester genap
print(f"Semester saat ini: {semester}")
```

**Output:**
```
Assalamu'alaikum!
Selamat datang di mata kuliah Algoritma dan Pemrograman
Program Studi Informatika - Universitas Al Azhar Indonesia

Nama  : Ahmad
NIM   : 2025001
Prodi : Informatika

Semester saat ini: 2
```

> **Perhatikan:** Python mengeksekusi kode **baris per baris dari atas ke bawah**. Ini disebut **sequential execution** (eksekusi berurutan) — struktur dasar pertama dari tiga struktur kontrol.

---

## 1.5 Pemrograman di Era AI

### 1.5.1 Landscape AI Coding Assistants

Tahun 2025-2026 menandai era baru dalam pemrograman. AI coding assistants telah menjadi alat bantu yang sangat powerful:

| AI Coding Assistant | Perusahaan | Keunggulan |
|--------------------|------------|------------|
| **GitHub Copilot** | GitHub/Microsoft | Terintegrasi di VS Code, autocomplete cerdas |
| **Claude** | Anthropic | Penalaran mendalam, menjelaskan kode dengan baik |
| **ChatGPT** | OpenAI | General purpose, bisa membuat dan menjelaskan kode |
| **Cursor** | Cursor Inc. | IDE berbasis AI, editing kode langsung |
| **Windsurf** | Codeium | IDE AI dengan flow state coding |

### 1.5.2 Computational Thinking vs Coding: Mana yang Lebih Penting?

Dengan adanya AI yang bisa menulis kode, muncul pertanyaan: **apakah belajar coding masih relevan?**

Jawabannya: **Ya, tetapi fokusnya bergeser.**

```
DULU (sebelum AI):
┌─────────────────────────────────────────────────┐
│  Hafal sintaks 40% │ Logika 30% │ Debug 30%    │
└─────────────────────────────────────────────────┘

SEKARANG (era AI):
┌─────────────────────────────────────────────────┐
│ CT & Logika 50% │ AI Skills 25% │ Coding 25%   │
└─────────────────────────────────────────────────┘

CT = Computational Thinking
```

Yang berubah bukan **kebutuhan** akan pemahaman pemrograman, tetapi **cara** kita memprogram:

| Aspek | Dulu | Sekarang (Era AI) |
|-------|------|-------------------|
| Menulis kode | Semua manual, ketik baris per baris | AI membantu generate, manusia review |
| Debugging | Baca error, cari di Stack Overflow | AI bantu analisis error, manusia validasi |
| Belajar | Buku, tutorial, trial-and-error | AI sebagai tutor personal + sumber tradisional |
| **Yang tetap penting** | Computational thinking, logika, desain algoritma | **Sama — SEMAKIN penting!** |

> **Pesan Penting:** AI adalah **alat**, bukan pengganti. Seorang programmer yang memahami algoritma dan computational thinking akan mampu **mengarahkan AI** dengan baik. Tanpa pemahaman dasar, Anda tidak akan tahu apakah kode dari AI itu benar, efisien, atau aman.

### 1.5.3 Peran Programmer Masa Depan

Peran programmer berevolusi dari "penulis kode" menjadi:

1. **Problem Analyst** — Memahami dan merumuskan masalah
2. **Solution Architect** — Merancang solusi dan arsitektur
3. **AI Director** — Mengarahkan AI untuk menghasilkan kode
4. **Quality Guardian** — Memvalidasi, menguji, dan memastikan kualitas
5. **Ethical Decision Maker** — Memastikan teknologi digunakan secara bertanggung jawab

Inilah mengapa mata kuliah ini berfokus pada **computational thinking** dan **pemahaman algoritma**, bukan sekadar menghafal sintaks Python.

---

## 1.6 Google Colab: Platform Praktik Kita

### 1.6.1 Mengapa Google Colab?

**Google Colaboratory** (Google Colab) adalah platform notebook interaktif berbasis cloud yang gratis. Kita menggunakannya karena:

| Keuntungan | Penjelasan |
|-----------|------------|
| **Gratis** | Tidak perlu bayar — hanya butuh akun Google |
| **Tanpa instalasi** | Tidak perlu menginstal Python di laptop |
| **Cloud-based** | Bisa diakses dari mana saja (laptop, tablet, bahkan HP) |
| **Kolaboratif** | Bisa berbagi notebook dan bekerja bersama (seperti Google Docs) |
| **GPU gratis** | Untuk yang nanti belajar AI/ML (bonus!) |
| **Mendukung Markdown** | Bisa menulis catatan berformat di antara kode |

### 1.6.2 Cara Mengakses Google Colab

1. Buka browser dan akses: **colab.research.google.com**
2. Login dengan akun Google Anda
3. Klik **"New Notebook"** untuk membuat notebook baru
4. Anda akan melihat **cell** (kotak) tempat menulis kode
5. Ketik kode Python di cell, lalu tekan **Shift+Enter** untuk menjalankan

### 1.6.3 Struktur Notebook Colab

```
┌─────────────────────────────────────────────┐
│  📓 Notebook Saya.ipynb                     │
├─────────────────────────────────────────────┤
│                                             │
│  [Text Cell]                                │
│  # Latihan Bab 1                            │
│  Nama: Ahmad | NIM: 2025001                 │
│                                             │
├─────────────────────────────────────────────┤
│                                             │
│  [Code Cell]                                │
│  print("Hello, World!")                     │
│  ─────────────────────────                  │
│  Output: Hello, World!                      │
│                                             │
├─────────────────────────────────────────────┤
│                                             │
│  [Code Cell]                                │
│  x = 10                                     │
│  y = 20                                     │
│  print(x + y)                               │
│  ─────────────────────────                  │
│  Output: 30                                 │
│                                             │
└─────────────────────────────────────────────┘
```

**Tips menggunakan Google Colab:**
- **Shift+Enter**: Jalankan cell dan pindah ke cell berikutnya
- **Ctrl+Enter**: Jalankan cell tanpa pindah
- **Ctrl+M B**: Tambah cell baru di bawah
- **Ctrl+M D**: Hapus cell
- Gunakan **text cell** untuk catatan (mendukung Markdown)
- Simpan secara otomatis ke Google Drive Anda

```python
# Coba jalankan di Google Colab!
# Program ini menghitung luas dan keliling persegi panjang

# Input
panjang = float(input("Masukkan panjang (cm): "))
lebar = float(input("Masukkan lebar (cm): "))

# Proses
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Output
print(f"\n--- Hasil Perhitungan ---")
print(f"Panjang  : {panjang} cm")
print(f"Lebar    : {lebar} cm")
print(f"Luas     : {luas} cm²")
print(f"Keliling : {keliling} cm")
```

---

## AI Corner: Memulai dengan AI

**Level: Dasar**

Di setiap bab buku ini, kita akan memiliki bagian **AI Corner** yang membahas cara menggunakan AI sebagai alat bantu belajar. Di bab pertama ini, kita mulai dari dasar.

### Apa Itu AI Coding Assistant?

AI coding assistant adalah program AI yang bisa membantu Anda:
- Menjelaskan konsep pemrograman
- Menulis kode berdasarkan deskripsi Anda
- Menemukan dan memperbaiki bug (error) dalam kode
- Menjawab pertanyaan tentang bahasa pemrograman

### Cara Bertanya pada AI tentang Konsep Algoritma

**Contoh prompt yang BAIK:**

```
"Jelaskan apa itu computational thinking menggunakan analogi
kehidupan sehari-hari di Indonesia. Saya mahasiswa semester 2
yang baru belajar pemrograman."
```

**Contoh prompt yang KURANG BAIK:**

```
"Apa itu computational thinking?"
```

Perbedaannya: prompt yang baik memberikan **konteks** (siapa Anda, apa yang Anda butuhkan) sehingga AI bisa memberikan jawaban yang lebih relevan.

### Batasan dan Tanggung Jawab

> **⚠ Penting untuk diingat:**
> - AI bisa **salah** — selalu verifikasi jawaban AI
> - AI **tidak menggantikan** pemahaman Anda sendiri
> - Menggunakan AI tanpa memahami hasilnya = **bukan belajar**
> - Di ujian (UTS/UAS), AI **tidak diperbolehkan** — closed book!
> - Jika menggunakan AI untuk tugas, **wajib didokumentasikan** dalam AI Usage Log

### Contoh Penggunaan AI untuk Bab 1

**Prompt 1 — Belajar konsep:**
```
"Buatkan analogi computational thinking menggunakan
contoh memasak nasi goreng. Jelaskan keempat pilarnya."
```

**Prompt 2 — Verifikasi pemahaman:**
```
"Saya membuat pseudocode berikut untuk menghitung rata-rata
nilai. Apakah sudah benar? [tempel pseudocode Anda]"
```

**Prompt 3 — Explorasi:**
```
"Berikan 3 contoh algoritma dalam kehidupan sehari-hari
di Indonesia yang melibatkan pengambilan keputusan (seleksi)."
```

### Progresi AI Literacy

| Bab | Level AI | Fokus |
|-----|----------|-------|
| **1-4** | **Dasar** | Bertanya konsep, verifikasi pemahaman |
| 5-7 | Menengah | AI bantu debug, refactoring |
| 8-11 | Lanjut | AI bantu analisis algoritma |
| 12-14 | Mahir | AI pair programming, prompt engineering |

Anda sekarang di level **Dasar**. Fokuslah pada memahami konsep terlebih dahulu, dan gunakan AI hanya sebagai **tutor tambahan**, bukan sebagai pengganti berpikir.

---

## Latihan Soal

### Tingkat Dasar

1. **Definisi:** Jelaskan dengan kata-kata Anda sendiri apa yang dimaksud dengan algoritma. Sebutkan 5 karakteristik algoritma menurut Donald Knuth.

2. **Sejarah:** Siapakah Al-Khwarizmi? Jelaskan kontribusinya terhadap dunia ilmu komputer dan mengapa namanya diabadikan dalam kata "algoritma".

3. **Contoh Sehari-hari:** Tuliskan algoritma dalam bahasa natural (deskriptif) untuk mengirim pesan WhatsApp kepada seseorang. Pastikan algoritma Anda memiliki langkah MULAI dan SELESAI.

4. **Flowchart Symbols:** Gambarkan kelima simbol flowchart standar dan jelaskan fungsi masing-masing.

5. **Identifikasi:** Dari contoh berikut, identifikasi mana yang merupakan algoritma dan mana yang bukan. Jelaskan alasannya:
   a. Resep membuat teh manis
   b. "Pikirkanlah sesuatu yang kreatif"
   c. Instruksi merakit lemari IKEA
   d. "Lakukan yang terbaik"

### Tingkat Menengah

1. **Pseudocode:** Tulis pseudocode untuk algoritma berikut: menentukan apakah sebuah tahun adalah tahun kabisat. (Petunjuk: tahun kabisat habis dibagi 4, kecuali yang habis dibagi 100 tapi tidak habis dibagi 400).

2. **Flowchart:** Buatlah flowchart untuk sistem penentuan tarif parkir di sebuah mal di Jakarta:
   - Tarif motor: Rp 3.000/jam pertama + Rp 2.000/jam berikutnya
   - Tarif mobil: Rp 5.000/jam pertama + Rp 3.000/jam berikutnya
   - Maksimal tarif per hari: motor Rp 15.000, mobil Rp 25.000

3. **Computational Thinking:** Anda diminta membangun sistem informasi sederhana untuk kantin kampus yang menjual 20 jenis makanan. Terapkan 4 pilar computational thinking untuk menganalisis masalah ini:
   - Bagaimana Anda mendekomposisi masalah?
   - Pola apa yang Anda temukan?
   - Abstraksi apa yang Anda lakukan?
   - Sketsa algoritma utamanya?

4. **Perbandingan Representasi:** Untuk masalah "menghitung total belanja di minimarket", buatkan representasinya dalam tiga bentuk: (a) bahasa natural, (b) pseudocode, (c) flowchart.

5. **Analisis:** Mengapa Python dipilih sebagai bahasa pemrograman untuk mata kuliah ini? Berikan minimal 5 alasan berdasarkan materi bab ini.

### Tingkat Mahir

1. **Desain Algoritma Kompleks:** Buatlah pseudocode lengkap untuk sistem antrian di Puskesmas dengan ketentuan:
   - Pasien dengan kondisi darurat mendapat prioritas utama
   - Lansia (usia ≥ 60) mendapat prioritas kedua
   - Pasien reguler dilayani berdasarkan nomor antrian
   - Sistem menampilkan estimasi waktu tunggu (rata-rata 10 menit per pasien)

2. **Refleksi AI:** Tuliskan esai singkat (200-300 kata) yang membahas: "Jika AI bisa menulis kode, mengapa mahasiswa Informatika masih perlu belajar algoritma dan pemrograman?" Gunakan perspektif computational thinking dan berikan contoh konkret.

3. **Proyek Mini:** Pilih satu aktivitas sehari-hari yang melibatkan pengambilan keputusan berulang (misalnya: memilih rute ojek online, memilih menu makan siang). Analisis menggunakan 4 pilar computational thinking, lalu buat (a) deskripsi bahasa natural, (b) pseudocode, dan (c) flowchart-nya. Diskusikan bagaimana AI bisa membantu menyelesaikan masalah ini.

---

## Rangkuman

- **Algoritma** adalah urutan langkah terbatas, terdefinisi jelas, dan efektif untuk menyelesaikan masalah.
- Kata "algoritma" berasal dari nama ilmuwan Muslim **Al-Khwarizmi** (±780-850 M), salah satu bapak matematika dan komputer.
- Lima karakteristik algoritma: **finiteness, definiteness, input, output, effectiveness**.
- **Computational thinking** memiliki 4 pilar: **decomposition, pattern recognition, abstraction, algorithm design**.
- Algoritma dapat direpresentasikan dalam tiga bentuk: **bahasa natural, pseudocode, dan flowchart**.
- Flowchart menggunakan simbol standar: **oval** (terminator), **persegi panjang** (proses), **belah ketupat** (keputusan), **jajar genjang** (I/O), dan **panah** (alur).
- **Python** dipilih karena sintaksnya ringkas, populer di industri AI, dan cocok untuk pemula.
- Di era AI, **computational thinking lebih penting dari sekadar hafal sintaks** — programmer masa depan adalah pengarah AI, bukan sekadar penulis kode.
- **Google Colab** adalah platform cloud gratis untuk praktik Python tanpa instalasi.
- AI coding assistant adalah **alat bantu**, bukan pengganti pemahaman dan pemikiran kritis.

---

## Referensi

1. Wing, J. M. (2006). "Computational Thinking." *Communications of the ACM*, 49(3), 33-35.
2. Knuth, D. E. (1997). *The Art of Computer Programming, Vol. 1: Fundamental Algorithms*. Addison-Wesley.
3. Al-Khwarizmi, M. (±830). *Kitab al-Jabr wal-Muqabala*. (Historical reference)
4. Downey, A. B. (2024). *Think Python: How to Think Like a Computer Scientist* (3rd ed.). O'Reilly Media.
5. Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.). MIT Press.
6. Python Software Foundation. (2026). Python 3.x Documentation. https://docs.python.org/3/
7. Google. (2026). Google Colaboratory. https://colab.research.google.com/
8. Denning, P. J., & Tedre, M. (2019). *Computational Thinking*. MIT Press.
9. Lutz, M. (2023). *Learning Python* (6th ed.). O'Reilly Media.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
