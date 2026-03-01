# BAB 13: AI-AUGMENTED PROGRAMMING DAN CODE QUALITY

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| CPMK-7.5 | Mengevaluasi penggunaan AI sebagai coding partner secara bertanggung jawab | C5 (Mengevaluasi) |
| CPMK-7.6 | Menerapkan framework CRIDE untuk prompt engineering kode | C3 (Menerapkan) |
| CPMK-7.7 | Merancang workflow AI pair programming yang efektif | C6 (Mencipta) |
| CPMK-7.8 | Mengevaluasi dan memvalidasi kode yang dihasilkan AI | C5 (Mengevaluasi) |

**Estimasi Waktu:** 3 × 50 menit (3 SKS)

**Prasyarat:** Mahasiswa telah memahami seluruh fondasi pemrograman (Bab 1–12): variabel, kontrol, fungsi, string, koleksi, searching, sorting, rekursi, dan Big-O.

---

## 13.1 Landscape AI Coding Assistants (2025-2026)

### 13.1.1 Era Baru Pemrograman

Tahun 2025-2026 menandai titik balik dalam sejarah pemrograman. AI coding assistants telah berkembang dari fitur autocomplete sederhana menjadi **partner programming** yang mampu memahami konteks, menulis kode lengkap, dan bahkan melakukan debugging.

| AI Coding Assistant | Perusahaan | Tahun Rilis | Keunggulan Utama |
|---------------------|------------|-------------|------------------|
| **GitHub Copilot** | GitHub/Microsoft | 2021 | Terintegrasi di IDE, autocomplete kontekstual |
| **Claude** | Anthropic | 2023 | Penalaran mendalam, penjelasan kode terperinci |
| **ChatGPT** | OpenAI | 2022 | General purpose, community besar |
| **Cursor** | Cursor Inc. | 2023 | IDE berbasis AI, multi-file editing |
| **Windsurf** | Codeium | 2024 | Flow state coding, konteks proyek penuh |
| **Claude Code** | Anthropic | 2025 | Agentic coding, terminal integration |

### 13.1.2 Bagaimana AI Coding Assistants Bekerja

AI coding assistants ditenagai oleh **Large Language Models (LLM)** — model AI yang dilatih pada miliaran baris kode dan teks:

```
┌─────────────────────────────────────────────────────────────┐
│              CARA KERJA AI CODING ASSISTANT                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. TRAINING (Pelatihan)                                    │
│     ┌──────────────┐                                        │
│     │ Miliaran     │──→ Model belajar pola kode,            │
│     │ baris kode   │    sintaks, best practices,            │
│     │ + dokumentasi│    dan hubungan konsep                  │
│     └──────────────┘                                        │
│                                                             │
│  2. INFERENCE (Penggunaan)                                  │
│     ┌──────────────┐    ┌──────────────┐                    │
│     │ Prompt/      │──→ │   Model AI   │──→ Kode/           │
│     │ Konteks Anda │    │   (LLM)      │   Penjelasan       │
│     └──────────────┘    └──────────────┘                    │
│                                                             │
│  3. CONTEXT WINDOW                                          │
│     Model melihat kode sekitar (file saat ini,              │
│     file terkait) untuk menghasilkan respons relevan        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 13.1.3 Apa yang AI Bisa dan Tidak Bisa Lakukan

| Kemampuan | AI Bisa ✓ | AI Tidak Bisa ✗ |
|-----------|-----------|-----------------|
| **Menulis kode** | Generate kode dari deskripsi | Memahami konteks bisnis sepenuhnya |
| **Debugging** | Mengidentifikasi banyak jenis bug | Memahami bug yang bergantung pada infrastruktur spesifik |
| **Menjelaskan** | Menjelaskan kode baris per baris | Menjelaskan mengapa keputusan bisnis diambil |
| **Refactoring** | Menyarankan perbaikan struktur | Memahami dampak perubahan pada seluruh sistem |
| **Testing** | Menulis unit test | Menentukan skenario testing bisnis |
| **Dokumentasi** | Menulis docstrings dan komentar | Menulis spesifikasi kebutuhan pengguna |

> **Pesan Penting:** AI adalah **alat yang sangat kuat**, tetapi **bukan pengganti pemikiran kritis**. AI bisa menghasilkan kode yang *terlihat benar* tetapi *secara logika salah*. Tanpa pemahaman algoritma dan computational thinking (yang telah Anda pelajari di Bab 1-12), Anda tidak akan mampu menilai apakah output AI itu benar.

### 13.1.4 Perubahan Peran Programmer

```
EVOLUSI PERAN PROGRAMMER
═══════════════════════════════════════════════

Era 1 (1950-1990): HARDWARE FOCUSED
┌─────────────────────────────────────────┐
│ Programmer = "penerjemah mesin"          │
│ Menulis kode assembly/C, fokus pada     │
│ efisiensi memori dan prosesor           │
└─────────────────────────────────────────┘
         │
         ▼
Era 2 (1990-2020): SOFTWARE FOCUSED
┌─────────────────────────────────────────┐
│ Programmer = "penulis kode"              │
│ Menulis kode high-level, framework,     │
│ Stack Overflow sebagai referensi         │
└─────────────────────────────────────────┘
         │
         ▼
Era 3 (2020-sekarang): AI-AUGMENTED
┌─────────────────────────────────────────┐
│ Programmer = "pengarah AI"               │
│ Mengarahkan AI, memvalidasi output,     │
│ fokus pada arsitektur dan logika        │
└─────────────────────────────────────────┘
```

Peran programmer kini lebih fokus pada:
1. **Problem Analysis** — Memahami dan merumuskan masalah
2. **Solution Architecture** — Merancang solusi tingkat tinggi
3. **AI Direction** — Memberikan instruksi yang tepat ke AI
4. **Quality Assurance** — Memvalidasi dan menguji output AI
5. **Ethical Judgment** — Memastikan kode aman, adil, dan bertanggung jawab

---

## 13.2 Framework CRIDE untuk Prompt Engineering Kode

Salah satu keterampilan terpenting di era AI adalah **prompt engineering** — kemampuan memberikan instruksi yang efektif kepada AI. Untuk pemrograman, kita menggunakan framework **CRIDE**:

```
┌─────────────────────────────────────────────────┐
│              FRAMEWORK CRIDE                     │
├─────────────────────────────────────────────────┤
│                                                 │
│   C ─── Context      (Konteks masalah)          │
│   R ─── Requirements  (Kebutuhan spesifik)      │
│   I ─── Input/Output  (Masukan/Keluaran)        │
│   D ─── Design        (Batasan desain)          │
│   E ─── Examples      (Contoh)                  │
│                                                 │
└─────────────────────────────────────────────────┘
```

### 13.2.1 C — Context (Konteks)

Berikan latar belakang masalah agar AI memahami situasinya.

**Contoh buruk:**
```
"Buatkan fungsi sorting"
```

**Contoh baik:**
```
"Saya sedang membuat sistem informasi perpustakaan kampus
menggunakan Python. Saya perlu mengurutkan daftar buku."
```

### 13.2.2 R — Requirements (Kebutuhan)

Spesifikasikan apa yang harus dicapai oleh kode.

```
"Fungsi harus bisa:
1. Mengurutkan berdasarkan judul (A-Z)
2. Mengurutkan berdasarkan tahun terbit (terbaru dulu)
3. Mengurutkan berdasarkan nama pengarang
4. User bisa memilih kriteria pengurutan"
```

### 13.2.3 I — Input/Output

Definisikan format data masukan dan keluaran yang diharapkan.

```
"Input: list of dictionaries, contoh:
[
    {'judul': 'Laskar Pelangi', 'pengarang': 'Andrea Hirata', 'tahun': 2005},
    {'judul': 'Bumi Manusia', 'pengarang': 'Pramoedya A.T.', 'tahun': 1980}
]

Output: list yang sama tetapi sudah terurut sesuai kriteria"
```

### 13.2.4 D — Design Constraints (Batasan Desain)

Tentukan batasan teknis dan arsitektur.

```
"Batasan:
- Gunakan Python built-in sort (bukan library eksternal)
- Fungsi harus modular (satu fungsi per kriteria)
- Kode harus Google Colab-compatible
- Komentar dalam Bahasa Indonesia
- Ikuti PEP 8 style guide"
```

### 13.2.5 E — Examples (Contoh)

Berikan contoh input-output konkret.

```
"Contoh penggunaan:
>>> daftar_buku = [
...     {'judul': 'Laskar Pelangi', 'pengarang': 'Andrea Hirata', 'tahun': 2005},
...     {'judul': 'Bumi Manusia', 'pengarang': 'Pramoedya A.T.', 'tahun': 1980},
...     {'judul': 'Ayat-Ayat Cinta', 'pengarang': 'Habiburrahman', 'tahun': 2004}
... ]
>>> urutkan_buku(daftar_buku, 'tahun')
# Harus mengembalikan: Bumi Manusia (1980) → Ayat-Ayat Cinta (2004) → Laskar Pelangi (2005)"
```

### Prompt CRIDE Lengkap

Menggabungkan semua elemen menjadi satu prompt:

```
Konteks: Saya membuat sistem informasi perpustakaan kampus
menggunakan Python untuk tugas kuliah Algoritma dan Pemrograman.

Kebutuhan: Buatkan fungsi untuk mengurutkan daftar buku
berdasarkan judul (A-Z), tahun terbit (terbaru dulu), atau
nama pengarang. User bisa memilih kriteria.

Input: List of dictionaries dengan key 'judul', 'pengarang', 'tahun'.
Output: List yang sama, terurut sesuai kriteria pilihan.

Batasan: Gunakan Python built-in sort, kode modular, Google
Colab-compatible, komentar Bahasa Indonesia, PEP 8.

Contoh:
daftar = [
    {'judul': 'Laskar Pelangi', 'pengarang': 'Andrea Hirata', 'tahun': 2005},
    {'judul': 'Bumi Manusia', 'pengarang': 'Pramoedya A.T.', 'tahun': 1980}
]
urutkan_buku(daftar, 'tahun')
# → [{'judul': 'Bumi Manusia', ...}, {'judul': 'Laskar Pelangi', ...}]
```

---

## 13.3 AI Pair Programming Workflow

### 13.3.1 Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│              AI PAIR PROGRAMMING WORKFLOW                         │
└─────────────────────────────────────────────────────────────────┘

  ╭──────────────╮     ╭──────────────╮     ╭──────────────╮
  │  1. ANALISIS │────→│  2. DESAIN   │────→│ 3. IMPLEMENT │
  │  MASALAH     │     │  SOLUSI      │     │    ASI       │
  │  [MANUSIA]   │     │ [MANUSIA+AI] │     │  [AI+MANUSIA]│
  ╰──────────────╯     ╰──────────────╯     ╰──────┬───────╯
                                                    │
                                                    ▼
  ╭──────────────╮     ╭──────────────╮     ╭──────────────╮
  │ 6. ITERASI   │←────│ 5. OPTIMASI  │←────│ 4. TESTING   │
  │ (jika perlu) │     │ & DOKUMENTASI│     │ & DEBUGGING  │
  │ [MANUSIA+AI] │     │  [AI+MANUSIA]│     │[MANUSIA+AI]  │
  ╰──────────────╯     ╰──────────────╯     ╰──────────────╯
```

### 13.3.2 Step 1: Analisis Masalah (Peran Utama: MANUSIA)

Langkah pertama **selalu** dilakukan oleh manusia. AI tidak memahami konteks bisnis atau kebutuhan pengguna.

**Yang harus Anda lakukan:**
- Pahami masalah secara mendalam
- Identifikasi input, output, dan constraint
- Terapkan computational thinking (Bab 1)
- Dekomposisi masalah menjadi sub-masalah

**Contoh:**
```
Masalah: Membuat sistem antrian Puskesmas
├── Sub-masalah 1: Pendaftaran pasien baru
├── Sub-masalah 2: Pengelolaan antrian (FIFO)
├── Sub-masalah 3: Prioritas (darurat, lansia)
├── Sub-masalah 4: Estimasi waktu tunggu
└── Sub-masalah 5: Riwayat kunjungan
```

### 13.3.3 Step 2: Desain Solusi (Kolaborasi: MANUSIA + AI)

Setelah analisis, Anda bisa mulai berkolaborasi dengan AI.

**Prompt ke AI:**
```
Saya merancang sistem antrian Puskesmas dengan Python.
Sub-masalah yang sudah saya identifikasi:
1. Pendaftaran pasien baru
2. Pengelolaan antrian FIFO
3. Prioritas darurat dan lansia
4. Estimasi waktu tunggu
5. Riwayat kunjungan

Bantu saya merancang struktur data yang tepat untuk
masing-masing sub-masalah. Jelaskan alasannya.
```

**Yang ANDA evaluasi dari respons AI:**
- Apakah struktur data yang disarankan masuk akal?
- Apakah sesuai dengan yang Anda pelajari di Bab 7-8?
- Apakah ada alternatif yang lebih sederhana?

### 13.3.4 Step 3: Implementasi (Peran Utama: AI + Review MANUSIA)

Di tahap ini, AI membantu menulis kode, tetapi Anda **harus review setiap baris**.

**Prompt ke AI (menggunakan CRIDE):**
```
Implementasikan fungsi pendaftaran_pasien() dengan spesifikasi:

Context: Sistem antrian Puskesmas di Indonesia
Requirements:
- Input: nama, umur, keluhan, status (darurat/reguler)
- Simpan data dalam dictionary
- Tambahkan ke antrian (list)
- Return nomor antrian

Input/Output:
- Input: "Ahmad", 45, "Demam tinggi", "darurat"
- Output: {"nomor": 1, "nama": "Ahmad", "umur": 45, ...}

Design: Gunakan dict + list, komentar Bahasa Indonesia
```

**Review Anda setelah AI generate kode:**

```python
# Kode dari AI - SELALU review sebelum menggunakan!

antrian = []  # list untuk menyimpan antrian
nomor_terakhir = 0  # counter nomor antrian

def pendaftaran_pasien(nama, umur, keluhan, status="reguler"):
    """
    Mendaftarkan pasien baru ke sistem antrian.

    Parameters:
        nama (str): Nama lengkap pasien
        umur (int): Umur pasien dalam tahun
        keluhan (str): Keluhan utama pasien
        status (str): 'darurat' atau 'reguler'

    Returns:
        dict: Data pasien yang terdaftar
    """
    global nomor_terakhir
    nomor_terakhir += 1

    pasien = {
        'nomor': nomor_terakhir,
        'nama': nama,
        'umur': umur,
        'keluhan': keluhan,
        'status': status,
        'prioritas': tentukan_prioritas(umur, status)
    }

    # Sisipkan berdasarkan prioritas
    if pasien['prioritas'] == 1:  # darurat → paling depan
        antrian.insert(0, pasien)
    elif pasien['prioritas'] == 2:  # lansia → setelah darurat
        posisi = sum(1 for p in antrian if p['prioritas'] == 1)
        antrian.insert(posisi, pasien)
    else:  # reguler → paling belakang
        antrian.append(pasien)

    return pasien

def tentukan_prioritas(umur, status):
    """Menentukan level prioritas pasien."""
    if status == "darurat":
        return 1  # prioritas tertinggi
    elif umur >= 60:
        return 2  # lansia
    else:
        return 3  # reguler
```

**Checklist review Anda:**
- [x] Logika prioritas benar? → Ya, darurat > lansia > reguler
- [x] Edge cases: apa jika umur negatif? → Perlu ditambahkan validasi
- [x] Global variable → Sebaiknya gunakan class/parameter, tapi OK untuk tugas sederhana
- [x] Docstring ada → Baik
- [x] Kode bisa jalan di Colab? → Ya

### 13.3.5 Step 4: Testing dan Debugging (Kolaborasi)

**Testing manual:**
```python
# Test 1: Pasien reguler
p1 = pendaftaran_pasien("Ahmad", 25, "Batuk", "reguler")
print(f"Test 1: {p1}")
# Expected: nomor=1, prioritas=3

# Test 2: Pasien darurat
p2 = pendaftaran_pasien("Siti", 35, "Kecelakaan", "darurat")
print(f"Test 2: {p2}")
# Expected: nomor=2, prioritas=1, posisi pertama di antrian

# Test 3: Pasien lansia
p3 = pendaftaran_pasien("Haji Usman", 70, "Cek rutin", "reguler")
print(f"Test 3: {p3}")
# Expected: nomor=3, prioritas=2, posisi setelah darurat

# Cek urutan antrian
print("\nUrutan antrian:")
for i, p in enumerate(antrian, 1):
    print(f"  {i}. {p['nama']} (prioritas: {p['prioritas']})")
# Expected: Siti → Haji Usman → Ahmad
```

**Jika ada bug, minta AI membantu debug:**
```
Kode saya menghasilkan output berikut [tempel output].
Expected output adalah [tempel expected].
Apa yang salah dan bagaimana memperbaikinya?
```

### 13.3.6 Step 5: Optimasi dan Dokumentasi

Setelah kode berfungsi, minta AI membantu:
- Optimasi performa (jika perlu)
- Menambahkan error handling
- Menulis dokumentasi yang lebih lengkap
- Membuat README proyek

---

## 13.4 Memvalidasi Kode dari AI

### 13.4.1 Checklist Validasi

Setiap kali Anda menerima kode dari AI, gunakan checklist berikut:

```
┌─────────────────────────────────────────────────────────────┐
│           CHECKLIST VALIDASI KODE AI                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  □ CORRECTNESS (Kebenaran)                                  │
│    - Apakah logika sesuai dengan yang diminta?              │
│    - Apakah output benar untuk input yang diberikan?        │
│    - Trace kode secara manual untuk input sederhana         │
│                                                             │
│  □ EDGE CASES (Kasus Batas)                                 │
│    - Apa yang terjadi jika input kosong?                    │
│    - Apa yang terjadi jika input sangat besar?              │
│    - Apa yang terjadi jika tipe data salah?                 │
│                                                             │
│  □ READABILITY (Keterbacaan)                                │
│    - Apakah nama variabel bermakna?                         │
│    - Apakah ada komentar yang cukup?                        │
│    - Apakah struktur kode logis?                            │
│                                                             │
│  □ EFFICIENCY (Efisiensi)                                   │
│    - Apakah kompleksitas waktu masuk akal? (Bab 12)        │
│    - Ada loop yang tidak perlu?                             │
│    - Ada operasi yang bisa disederhanakan?                  │
│                                                             │
│  □ SECURITY (Keamanan)                                      │
│    - Ada eval() atau exec()? (BAHAYA!)                      │
│    - Ada input yang tidak divalidasi?                       │
│    - Ada data sensitif yang ter-hardcode?                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 13.4.2 Common AI Mistakes (Kesalahan Umum AI)

AI coding assistants sering membuat kesalahan berikut:

| Jenis Kesalahan | Contoh | Cara Mendeteksi |
|----------------|--------|-----------------|
| **Hallucination** | Menggunakan library/fungsi yang tidak ada | Cek apakah import berhasil |
| **Outdated API** | Menggunakan sintaks lama yang sudah deprecated | Cek dokumentasi resmi |
| **Wrong assumption** | Mengasumsikan data selalu valid | Test dengan data invalid |
| **Off-by-one** | Loop `range(1, n)` harusnya `range(1, n+1)` | Manual trace |
| **Logic error** | Kondisi if terbalik | Test boundary values |
| **Overcomplication** | Solusi 50 baris untuk masalah 5 baris | Tanya: bisa lebih sederhana? |

### 13.4.3 Teknik Testing: Manual Trace, Unit Test, Boundary Testing

**Manual Trace — Teknik dari Bab 4:**

```python
# Fungsi dari AI: mencari elemen terbesar kedua
def second_largest(data):
    if len(data) < 2:
        return None
    first = second = float('-inf')
    for num in data:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None
```

**Trace manual:**
```
data = [5, 3, 8, 1, 8]

Iterasi 1: num=5, first=-inf → second=-inf, first=5
Iterasi 2: num=3, 3>5? No, 3>-inf AND 3≠5? Yes → second=3
Iterasi 3: num=8, 8>5? Yes → second=5, first=8
Iterasi 4: num=1, 1>8? No, 1>5? No → no change
Iterasi 5: num=8, 8>8? No, 8>5 AND 8≠8? No (8==8) → no change

Result: second = 5 ✓ (benar! elemen terbesar kedua dari [5,3,8,1,8] adalah 5)
```

**Boundary testing:**
```python
# Test normal
assert second_largest([5, 3, 8, 1]) == 5

# Test semua sama
assert second_largest([7, 7, 7]) is None

# Test hanya 2 elemen
assert second_largest([1, 2]) == 1

# Test satu elemen
assert second_largest([5]) is None

# Test list kosong
assert second_largest([]) is None

# Test negatif
assert second_largest([-1, -5, -3]) == -3

print("Semua test passed!")
```

### 13.4.4 Contoh: Kode AI yang Terlihat Benar Tapi Ada Bug

**Prompt ke AI:** "Buatkan fungsi untuk menghitung rata-rata dari list bilangan."

**Kode dari AI:**
```python
def hitung_rata_rata(data):
    total = 0
    for angka in data:
        total += angka
    rata_rata = total / len(data)
    return rata_rata
```

**Pertanyaan:** Apakah kode ini benar?

**Analisis:**
- Untuk input normal `[10, 20, 30]` → benar, menghasilkan 20.0
- Untuk input `[]` (list kosong) → **ERROR!** `ZeroDivisionError: division by zero`

**Perbaikan:**
```python
def hitung_rata_rata(data):
    """Menghitung rata-rata dari list bilangan."""
    if not data:  # cek apakah list kosong
        return 0  # atau bisa return None
    total = sum(data)
    return total / len(data)
```

> **Pelajaran:** AI sering menghasilkan kode yang bekerja untuk "happy path" tetapi gagal di edge cases. Selalu pikirkan: **apa yang bisa salah?**

---

## 13.5 Code Quality dan Clean Code

### 13.5.1 Prinsip Clean Code

Kode yang baik bukan hanya kode yang berfungsi — kode yang baik adalah kode yang **mudah dibaca, dipahami, dan dimodifikasi**.

**5 Prinsip Utama:**

```
┌─────────────────────────────────────────────────────────┐
│              5 PRINSIP CLEAN CODE                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. MEANINGFUL NAMES                                    │
│     Nama variabel/fungsi harus menjelaskan tujuannya   │
│     ✗ x, y, temp, data1, proses()                      │
│     ✓ jumlah_mahasiswa, rata_rata_ipk, hitung_total()  │
│                                                         │
│  2. SMALL FUNCTIONS                                     │
│     Satu fungsi = satu tugas                            │
│     Maksimal 20-30 baris per fungsi                     │
│                                                         │
│  3. DRY (Don't Repeat Yourself)                         │
│     Jangan copy-paste kode — buat fungsi                │
│                                                         │
│  4. KISS (Keep It Simple, Stupid)                       │
│     Solusi sesederhana mungkin                           │
│     Jangan over-engineering                             │
│                                                         │
│  5. COMMENTS THAT EXPLAIN WHY                           │
│     Komentar menjelaskan MENGAPA, bukan APA             │
│     ✗ # menambahkan 1 ke counter                        │
│     ✓ # counter dimulai dari 1 karena nomor antrian     │
│       # tidak boleh 0 (kebijakan Puskesmas)             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Contoh Before vs After Clean Code:**

**SEBELUM (kode "kotor"):**
```python
def p(d):
    t = 0
    for i in d:
        t = t + i['h'] * i['j']
    if t > 100000:
        t = t * 0.9
    return t
```

**SESUDAH (clean code):**
```python
def hitung_total_belanja(daftar_barang):
    """Menghitung total belanja dengan diskon 10% jika > Rp 100.000."""
    total = sum(
        barang['harga'] * barang['jumlah']
        for barang in daftar_barang
    )

    BATAS_DISKON = 100_000
    PERSENTASE_DISKON = 0.10

    if total > BATAS_DISKON:
        total *= (1 - PERSENTASE_DISKON)

    return total
```

### 13.5.2 PEP 8 Style Guide (Highlights)

**PEP 8** adalah panduan gaya resmi Python. Beberapa aturan penting:

| Aturan | Contoh Benar | Contoh Salah |
|--------|-------------|-------------|
| Nama variabel: snake_case | `jumlah_mahasiswa` | `jumlahMahasiswa`, `JumlahMahasiswa` |
| Nama fungsi: snake_case | `hitung_rata_rata()` | `HitungRataRata()`, `hitungRataRata()` |
| Nama konstanta: UPPER_CASE | `BATAS_MAKSIMAL = 100` | `batas_maksimal = 100` |
| Indentasi: 4 spasi | `    if True:` | `  if True:` (2 spasi) |
| Panjang baris: maks 79 karakter | — | — |
| Spasi di sekitar operator | `x = 1 + 2` | `x=1+2` |
| Spasi setelah koma | `fungsi(a, b, c)` | `fungsi(a,b,c)` |
| Blank line: 2 baris antar fungsi | — | — |

### 13.5.3 Code Review Checklist

Ketika melakukan code review (termasuk review kode dari AI):

```
CHECKLIST CODE REVIEW
═══════════════════════

Fungsionalitas:
□ Kode melakukan apa yang diminta?
□ Edge cases ditangani?
□ Error handling memadai?

Keterbacaan:
□ Nama variabel/fungsi bermakna?
□ Komentar menjelaskan "mengapa" (bukan "apa")?
□ Struktur kode logis (flow mudah diikuti)?

Efisiensi:
□ Tidak ada loop yang tidak perlu?
□ Struktur data tepat? (Bab 7-8)
□ Kompleksitas Big-O masuk akal? (Bab 12)

Best Practices:
□ Mengikuti PEP 8?
□ Fungsi tidak terlalu panjang?
□ Tidak ada kode yang di-copy-paste?
□ Tidak ada "magic number" (gunakan konstanta)?
```

### 13.5.4 Menggunakan AI untuk Code Review

**Prompt untuk code review:**
```
Review kode Python berikut. Identifikasi:
1. Bug atau potensi error
2. Pelanggaran PEP 8
3. Masalah readability
4. Potensi masalah efisiensi
5. Saran perbaikan

[tempel kode Anda di sini]
```

---

## 13.6 Etika AI dalam Pemrograman

### 13.6.1 Academic Integrity: Garis antara Bantuan dan Kecurangan

Di lingkungan akademik, penggunaan AI harus **transparan** dan **bertanggung jawab**. Berikut panduan di mata kuliah ini:

```
┌───────────────────────────────────────────────────────────────┐
│           GARIS BATAS AI DI MATA KULIAH INI                    │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  ✓ DIPERBOLEHKAN:                                             │
│    • Bertanya konsep ke AI untuk memahami materi              │
│    • Meminta AI menjelaskan error yang Anda tidak mengerti    │
│    • Menggunakan AI untuk brainstorm ide solusi               │
│    • Meminta AI review kode yang ANDA tulis                   │
│    • Menggunakan AI di tugas (WAJIB dokumentasi AI Log)       │
│                                                               │
│  ✗ TIDAK DIPERBOLEHKAN:                                       │
│    • Copy-paste kode AI tanpa memahami                        │
│    • Menggunakan AI saat UTS/UAS (closed book!)               │
│    • Tidak mendokumentasikan penggunaan AI                    │
│    • Mengklaim kode AI sebagai 100% karya sendiri             │
│                                                               │
│  ⚠ AREA ABU-ABU (diskusikan dengan dosen):                    │
│    • AI generate seluruh kode lalu Anda modifikasi sedikit   │
│    • Menggunakan AI untuk debugging tugas yang sangat rumit   │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### 13.6.2 AI Usage Log: Dokumentasi Penggunaan AI

Setiap tugas yang menggunakan bantuan AI **wajib** menyertakan AI Usage Log. Ini bukan hukuman — ini adalah **praktik profesional** yang juga diterapkan di industri.

### 13.6.3 Template AI Usage Log

```markdown
# AI Usage Log
## Identitas
- Nama: [Nama Anda]
- NIM: [NIM Anda]
- Tugas: [Nama Tugas]
- Tanggal: [Tanggal]

## Ringkasan Penggunaan AI
- AI yang digunakan: [Claude / ChatGPT / Copilot / dll.]
- Persentase kode yang di-generate AI: [estimasi %]
- Persentase kode yang ditulis sendiri: [estimasi %]
- Persentase kode AI yang dimodifikasi: [estimasi %]

## Detail Interaksi

### Interaksi 1
- **Prompt saya:** [tulis prompt Anda]
- **Respons AI:** [ringkasan respons AI]
- **Apa yang saya gunakan:** [bagian mana yang digunakan]
- **Modifikasi saya:** [apa yang Anda ubah dan mengapa]
- **Apa yang saya pelajari:** [insight baru]

### Interaksi 2
[dst.]

## Refleksi
- Apa yang tidak bisa saya lakukan tanpa AI?
- Apa yang saya pelajari dari proses ini?
- Apakah saya memahami seluruh kode yang dikumpulkan?

## Deklarasi Kejujuran
Saya menyatakan bahwa AI Usage Log ini adalah catatan
yang jujur dan lengkap dari penggunaan AI saya dalam
mengerjakan tugas ini.

Tanda tangan: [Nama]
Tanggal: [Tanggal]
```

### 13.6.4 Bias dan Keamanan dalam Kode AI

AI bisa menghasilkan kode yang mengandung:

| Risiko | Penjelasan | Contoh |
|--------|------------|--------|
| **Bias** | Kode mengandung asumsi yang tidak adil | Validasi nama yang tidak mendukung karakter Unicode/Arab |
| **Security vulnerability** | Kode tidak aman | SQL injection, tidak validasi input |
| **Outdated practice** | Menggunakan cara lama | MD5 untuk hashing password |
| **Copyright issue** | Kode mirip dengan kode open source berlisensi | Copy dari library GPL |

### 13.6.5 Perspektif Islam: Amanah, Kejujuran, dan Transparansi

Penggunaan AI dalam pemrograman harus dilandasi nilai-nilai yang sejalan dengan ajaran Islam:

> **Amanah (Kepercayaan):** Ketika dosen atau atasan mempercayakan tugas kepada Anda, menggunakan AI tanpa disclosure adalah melanggar amanah. Transparansi dalam dokumentasi AI Usage Log adalah wujud amanah.

> **Kejujuran (As-Sidq):** Rasulullah SAW bersabda: *"Hendaklah kalian berlaku jujur, karena kejujuran membawa kepada kebaikan."* (HR. Bukhari-Muslim). Mengklaim kode AI sebagai karya sendiri bertentangan dengan prinsip kejujuran.

> **Ihsan (Keunggulan):** Menggunakan AI seharusnya mendorong kita menghasilkan karya yang **lebih baik**, bukan sebagai jalan pintas untuk menghindari belajar. Ihsan berarti berusaha memberikan yang terbaik dalam setiap tugas.

> **Transparansi:** Dalam Islam, transparansi adalah bagian dari akuntabilitas (muhasabah). Mendokumentasikan proses kerja — termasuk bantuan AI — adalah bentuk transparansi dan profesionalisme.

---

## 13.7 Studi Kasus Lengkap: Membangun Sistem Antrian RS dengan AI

Mari kita praktikkan seluruh workflow AI pair programming untuk membangun sistem antrian sederhana.

### Step 1: Analisis Masalah (MANUSIA)

```
MASALAH: Sistem antrian Rumah Sakit/Puskesmas sederhana
FITUR:
1. Daftarkan pasien baru dengan nomor antrian otomatis
2. Prioritas: darurat > lansia (>= 60 tahun) > reguler
3. Panggil pasien berikutnya dari antrian
4. Tampilkan daftar antrian saat ini
5. Tampilkan statistik (total pasien, rata-rata waktu tunggu)

STRUKTUR DATA:
- Dictionary untuk data setiap pasien
- List untuk antrian (karena butuh insert di posisi tertentu)

ALGORITMA:
- Linear insertion berdasarkan prioritas
- FIFO untuk pasien dengan prioritas sama
```

### Step 2: Prompt CRIDE ke AI

```
Context: Sistem antrian Puskesmas sederhana untuk tugas kuliah
Algoritma dan Pemrograman, Python, Google Colab-compatible.

Requirements:
1. Menu interaktif: daftar, panggil, tampilkan antrian, statistik, keluar
2. Prioritas: darurat(1) > lansia >= 60 tahun(2) > reguler(3)
3. Nomor antrian otomatis
4. Estimasi waktu tunggu (rata-rata 10 menit per pasien)

Input: nama (str), umur (int), keluhan (str), status (str)
Output: menu-driven console interface

Design: Modular (minimal 5 fungsi), dict + list, komentar Indonesia, PEP 8

Examples:
- Daftar "Ahmad", 25, "Batuk", "reguler" → Nomor antrian: A-001
- Daftar "Siti", 35, "Kecelakaan", "darurat" → Nomor antrian: D-002
- Panggil → "Memanggil: D-002 Siti (DARURAT)"
```

### Step 3: Implementasi (Review dan modifikasi kode AI)

```python
# ============================================================
# SISTEM ANTRIAN PUSKESMAS SEDERHANA
# Mata Kuliah: Algoritma dan Pemrograman
# Universitas Al Azhar Indonesia
# ============================================================

# --- Data global ---
antrian = []          # list untuk menyimpan antrian pasien
riwayat = []          # list untuk menyimpan pasien yang sudah dilayani
nomor_counter = 0     # counter nomor antrian

# --- Konstanta ---
WAKTU_PER_PASIEN = 10  # estimasi menit per pasien
PRIORITAS_DARURAT = 1
PRIORITAS_LANSIA = 2
PRIORITAS_REGULER = 3

# --- Fungsi-fungsi ---

def tentukan_prioritas(umur, status):
    """Menentukan level prioritas pasien."""
    if status.lower() == "darurat":
        return PRIORITAS_DARURAT
    elif umur >= 60:
        return PRIORITAS_LANSIA
    else:
        return PRIORITAS_REGULER

def label_prioritas(prioritas):
    """Mengubah kode prioritas menjadi label teks."""
    labels = {1: "DARURAT", 2: "LANSIA", 3: "REGULER"}
    return labels.get(prioritas, "UNKNOWN")

def generate_nomor_antrian(prioritas):
    """Generate nomor antrian dengan prefix berdasarkan prioritas."""
    global nomor_counter
    nomor_counter += 1
    prefix = {1: "D", 2: "L", 3: "A"}  # Darurat, Lansia, Antrian reguler
    return f"{prefix.get(prioritas, 'X')}-{nomor_counter:03d}"

def daftarkan_pasien():
    """Mendaftarkan pasien baru ke antrian."""
    print("\n--- PENDAFTARAN PASIEN BARU ---")

    nama = input("Nama pasien  : ").strip()
    if not nama:
        print("Error: Nama tidak boleh kosong!")
        return

    try:
        umur = int(input("Umur (tahun) : "))
        if umur < 0 or umur > 150:
            print("Error: Umur tidak valid!")
            return
    except ValueError:
        print("Error: Umur harus berupa angka!")
        return

    keluhan = input("Keluhan utama: ").strip()

    print("Status: 1=Darurat, 2=Reguler")
    pilihan_status = input("Pilih (1/2)  : ").strip()
    status = "darurat" if pilihan_status == "1" else "reguler"

    # Tentukan prioritas dan nomor antrian
    prioritas = tentukan_prioritas(umur, status)
    nomor = generate_nomor_antrian(prioritas)

    pasien = {
        'nomor': nomor,
        'nama': nama,
        'umur': umur,
        'keluhan': keluhan,
        'status': status,
        'prioritas': prioritas
    }

    # Sisipkan berdasarkan prioritas (stabil — FIFO dalam prioritas sama)
    posisi = 0
    for i, p in enumerate(antrian):
        if p['prioritas'] <= prioritas:
            posisi = i + 1
        else:
            break
    antrian.insert(posisi, pasien)

    estimasi = (posisi + 1) * WAKTU_PER_PASIEN
    print(f"\nPasien terdaftar!")
    print(f"  Nomor Antrian : {nomor}")
    print(f"  Prioritas     : {label_prioritas(prioritas)}")
    print(f"  Estimasi tunggu: ~{estimasi} menit")

def panggil_pasien():
    """Memanggil pasien berikutnya dari antrian."""
    if not antrian:
        print("\nAntrian kosong — tidak ada pasien yang menunggu.")
        return

    pasien = antrian.pop(0)  # ambil dari depan antrian
    riwayat.append(pasien)

    print(f"\n{'='*50}")
    print(f"  MEMANGGIL: {pasien['nomor']} — {pasien['nama']}")
    print(f"  Status: {label_prioritas(pasien['prioritas'])}")
    print(f"  Keluhan: {pasien['keluhan']}")
    print(f"{'='*50}")

def tampilkan_antrian():
    """Menampilkan daftar antrian saat ini."""
    if not antrian:
        print("\nAntrian kosong.")
        return

    print(f"\n--- DAFTAR ANTRIAN ({len(antrian)} pasien) ---")
    print(f"{'No':>3} {'Nomor':<8} {'Nama':<20} {'Umur':>4} {'Prioritas':<10} {'Keluhan'}")
    print("-" * 75)

    for i, p in enumerate(antrian, 1):
        estimasi = i * WAKTU_PER_PASIEN
        print(f"{i:>3} {p['nomor']:<8} {p['nama']:<20} {p['umur']:>4} "
              f"{label_prioritas(p['prioritas']):<10} {p['keluhan']}")

    print(f"\nEstimasi waktu pasien terakhir: ~{len(antrian) * WAKTU_PER_PASIEN} menit")

def tampilkan_statistik():
    """Menampilkan statistik sistem antrian."""
    total_terdaftar = len(antrian) + len(riwayat)
    total_dilayani = len(riwayat)
    total_menunggu = len(antrian)

    print("\n--- STATISTIK SISTEM ---")
    print(f"  Total pasien terdaftar : {total_terdaftar}")
    print(f"  Sudah dilayani         : {total_dilayani}")
    print(f"  Masih menunggu         : {total_menunggu}")

    if antrian:
        darurat = sum(1 for p in antrian if p['prioritas'] == PRIORITAS_DARURAT)
        lansia = sum(1 for p in antrian if p['prioritas'] == PRIORITAS_LANSIA)
        reguler = sum(1 for p in antrian if p['prioritas'] == PRIORITAS_REGULER)
        print(f"  Darurat: {darurat} | Lansia: {lansia} | Reguler: {reguler}")

def menu_utama():
    """Menampilkan menu utama dan menjalankan loop program."""
    print("=" * 50)
    print("  SISTEM ANTRIAN PUSKESMAS SEHAT SEJAHTERA")
    print("  Algoritma dan Pemrograman — UAI 2026")
    print("=" * 50)

    while True:
        print("\n--- MENU UTAMA ---")
        print("1. Daftarkan Pasien Baru")
        print("2. Panggil Pasien Berikutnya")
        print("3. Tampilkan Daftar Antrian")
        print("4. Statistik")
        print("5. Keluar")

        pilihan = input("\nPilih menu (1-5): ").strip()

        if pilihan == "1":
            daftarkan_pasien()
        elif pilihan == "2":
            panggil_pasien()
        elif pilihan == "3":
            tampilkan_antrian()
        elif pilihan == "4":
            tampilkan_statistik()
        elif pilihan == "5":
            print("\nTerima kasih! Wassalamu'alaikum.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# --- Jalankan program ---
menu_utama()
```

### Step 4: Review dan AI Usage Log

```
AI Usage Log - Studi Kasus Bab 13
==================================
AI yang digunakan: Claude
Persentase kode AI: ~60%
Persentase kode sendiri: ~40%

Interaksi 1:
- Prompt: [CRIDE prompt di atas]
- AI generate: Struktur dasar program dengan 5 fungsi
- Modifikasi: Menambahkan validasi input, mengubah format nomor antrian

Interaksi 2:
- Prompt: "Perbaiki logika insert prioritas agar stabil (FIFO)"
- AI memperbaiki: logika posisi insert
- Saya belajar: pentingnya stable insertion

Refleksi: Saya memahami seluruh kode. AI membantu mempercepat
penulisan, tetapi desain dan validasi dilakukan sendiri.
```

---

## AI Corner: Mahir — Meta-AI Skills

**Level: Mahir**

Di bab terakhir sebelum proyek akhir, Anda telah mencapai level tertinggi dalam AI literacy:

### Menggunakan AI untuk Belajar tentang AI

```
Prompt: "Jelaskan bagaimana Large Language Model (LLM) bisa
menghasilkan kode Python. Gunakan analogi sederhana yang
bisa dipahami mahasiswa semester 2."
```

### Self-Assessment dengan AI

```
Prompt: "Berikan saya 5 soal tentang algoritma sorting
(bubble, selection, insertion sort) dengan tingkat kesulitan
C4 (Analisis) Bloom's taxonomy. Jangan berikan jawaban —
saya ingin mencoba sendiri dulu."
```

Setelah mengerjakan:
```
Prompt: "Ini jawaban saya untuk soal 1-5:
[tempel jawaban]
Evaluasi jawaban saya, berikan skor 1-10, dan jelaskan
apa yang perlu diperbaiki."
```

### Building a Personal AI Coding Workflow

Setiap programmer akan mengembangkan workflow AI yang unik. Berikut template untuk memulai:

```
MY AI CODING WORKFLOW
═════════════════════

1. SEBELUM coding:
   □ Analisis masalah sendiri (10 menit)
   □ Dekomposisi menjadi sub-masalah
   □ Pilih struktur data dan algoritma

2. SELAMA coding:
   □ Tulis kerangka kode sendiri dulu
   □ Gunakan AI untuk bagian repetitif
   □ Review SETIAP kode dari AI
   □ Test incrementally

3. SETELAH coding:
   □ Code review (sendiri + AI)
   □ Testing edge cases
   □ Dokumentasi
   □ AI Usage Log

4. REFLEKSI:
   □ Apa yang saya pelajari?
   □ Apa yang bisa saya lakukan lebih baik?
   □ Apakah saya terlalu bergantung pada AI?
```

---

## Latihan Soal

### Tingkat Dasar

1. **Identifikasi:** Sebutkan 5 AI coding assistant yang populer di tahun 2025-2026 dan jelaskan keunggulan masing-masing dalam 1-2 kalimat.

2. **CRIDE Framework:** Jelaskan apa singkatan dari CRIDE dan fungsi masing-masing elemen.

3. **Klasifikasi:** Dari aktivitas berikut, mana yang diperbolehkan dan mana yang tidak diperbolehkan dalam tugas kuliah ini?
   - a) Meminta AI menjelaskan error "IndexError"
   - b) Meminta AI menulis seluruh tugas lalu submit tanpa AI Log
   - c) Menggunakan AI saat UTS
   - d) Meminta AI review kode yang sudah Anda tulis
   - e) Meminta AI menulis kode, lalu Anda modifikasi dan dokumentasikan di AI Log

4. **Code Review:** Review kode berikut dan identifikasi 3 masalah (readability, naming, edge case):
   ```python
   def f(x):
       r = 0
       for i in x:
           r = r + i
       return r / len(x)
   ```

5. **PEP 8:** Perbaiki kode berikut agar sesuai PEP 8:
   ```python
   def HitungLuas(p,l):
       Hasil=p*l
       return(Hasil)
   x=HitungLuas(10,5)
   print(x)
   ```

### Tingkat Menengah

1. **Prompt Engineering:** Tulis prompt CRIDE lengkap untuk meminta AI membuat fungsi pencarian buku di perpustakaan berdasarkan judul, pengarang, atau tahun terbit. Gunakan konteks Indonesia.

2. **Validasi Kode AI:** AI menghasilkan kode berikut untuk binary search. Trace secara manual untuk data `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]` dengan target `23`. Apakah kode benar?
   ```python
   def binary_search(arr, target):
       low, high = 0, len(arr)
       while low < high:
           mid = (low + high) // 2
           if arr[mid] == target:
               return mid
           elif arr[mid] < target:
               low = mid + 1
           else:
               high = mid
       return -1
   ```

3. **AI Usage Log:** Tulis AI Usage Log lengkap untuk situasi berikut: Anda menggunakan Claude untuk membantu membuat fungsi sorting mahasiswa berdasarkan IPK. Anda memberikan 3 prompt, AI memberikan kode yang Anda modifikasi, dan Anda menemukan satu bug yang Anda perbaiki sendiri.

4. **Code Quality:** Refactor kode berikut menjadi clean code dengan fungsi-fungsi yang modular:
   ```python
   n = ["Ahmad", "Siti", "Budi", "Dewi"]
   v = [85, 92, 78, 95]
   for i in range(len(n)):
       if v[i] >= 90:
           print(n[i], "A")
       elif v[i] >= 80:
           print(n[i], "B")
       elif v[i] >= 70:
           print(n[i], "C")
       else:
           print(n[i], "D")
   t = 0
   for x in v:
       t = t + x
   print("Rata-rata:", t/len(v))
   ```

5. **Etika:** Tuliskan esai singkat (150-200 kata) tentang mengapa transparansi dalam penggunaan AI coding assistant penting dari perspektif akademik dan profesional. Hubungkan dengan nilai amanah dalam Islam.

### Tingkat Mahir

1. **Studi Kasus Lengkap:** Gunakan framework CRIDE untuk membangun sistem inventaris toko kecil (warung) menggunakan AI. Dokumentasikan:
   - Analisis masalah Anda (sebelum menggunakan AI)
   - Prompt CRIDE yang Anda tulis
   - Kode yang dihasilkan AI
   - Modifikasi yang Anda lakukan
   - Hasil testing
   - AI Usage Log lengkap

2. **Evaluasi Kritis:** Bandingkan dua kode dari dua AI berbeda untuk masalah yang sama (misalnya sorting). Evaluasi berdasarkan: correctness, readability, efficiency (Big-O), dan adherence to PEP 8. Mana yang lebih baik dan mengapa?

3. **Refleksi Mendalam:** Tulis refleksi 300-400 kata tentang perjalanan belajar Anda di mata kuliah ini dari Bab 1 hingga Bab 13. Bagaimana pemahaman Anda tentang peran AI dalam pemrograman berubah? Apa yang paling berharga yang Anda pelajari? Bagaimana Anda akan menggunakan AI secara bertanggung jawab di karir masa depan Anda?

---

## Rangkuman

- **AI Coding Assistants** (Copilot, Claude, ChatGPT, Cursor) telah mengubah cara programmer bekerja — dari menulis kode manual menjadi mengarahkan AI.
- AI ditenagai **LLM** yang dilatih pada miliaran baris kode, tetapi AI **bisa salah** dan tidak memahami konteks bisnis.
- **Framework CRIDE** (Context, Requirements, Input/Output, Design, Examples) membantu menulis prompt yang efektif untuk AI.
- **AI Pair Programming Workflow**: Analisis (manusia) → Desain (kolaborasi) → Implementasi (AI+review) → Testing (kolaborasi) → Optimasi → Iterasi.
- **Validasi kode AI** wajib dilakukan: cek correctness, edge cases, readability, efficiency, security.
- Kesalahan umum AI: **hallucination**, outdated API, wrong assumptions, off-by-one, logic errors.
- **Clean Code**: meaningful names, small functions, DRY, KISS, comments that explain why.
- **PEP 8**: snake_case, 4-spasi indentasi, 79 karakter per baris, spasi sebelum dan sesudah operator.
- **Etika AI**: transparansi, AI Usage Log wajib, membedakan bantuan vs kecurangan, sesuai nilai **amanah** dan **kejujuran** Islam.
- Programmer masa depan berfokus pada **problem analysis, solution architecture, AI direction, quality assurance, dan ethical judgment**.

---

## Referensi

1. Chen, M. et al. (2021). "Evaluating Large Language Models Trained on Code." *arXiv:2107.03374*. (Codex/Copilot paper)
2. Anthropic. (2026). Claude Documentation. https://docs.anthropic.com/
3. GitHub. (2026). GitHub Copilot Documentation. https://docs.github.com/copilot
4. van Rossum, G. et al. (2001). "PEP 8 — Style Guide for Python Code." Python Enhancement Proposals.
5. Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Pearson.
6. Denny, P. et al. (2024). "Computing Education in the Era of Generative AI." *Communications of the ACM*, 67(2).
7. UNESCO. (2023). "Guidance for Generative AI in Education and Research." United Nations.
8. Downey, A. B. (2024). *Think Python* (3rd ed.). O'Reilly Media.
9. Python Software Foundation. (2026). Python 3.x Documentation. https://docs.python.org/3/

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
