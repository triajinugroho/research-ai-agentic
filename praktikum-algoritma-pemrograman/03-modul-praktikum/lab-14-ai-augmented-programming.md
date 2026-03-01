# Lab 14: AI-Augmented Programming

## Informasi Praktikum

| Komponen | Keterangan |
|----------|------------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Kode MK** | INF-101 |
| **Semester** | Genap 2025/2026 |
| **Praktikum** | Lab 14 — AI-Augmented Programming |
| **Durasi** | 75 menit |
| **Prasyarat** | Seluruh Lab sebelumnya (Lab 01-13), Modul Minggu 14 |
| **Platform** | Google Colab + AI Assistant (ChatGPT / Claude / Gemini) |
| **Pengajar** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. **Menulis** prompt CRIDE (Context, Role, Instruction, Details, Examples) yang efektif untuk menghasilkan kode Python dari AI
2. **Mengevaluasi** secara kritis output kode yang dihasilkan AI — mengidentifikasi kebenaran, efisiensi, dan potensi masalah
3. **Memanfaatkan** AI sebagai partner debugging, refactoring, dan code review
4. **Mendokumentasikan** setiap interaksi dengan AI secara transparan melalui AI Usage Log

---

## Persiapan

- Buka Google Colab di browser: [colab.research.google.com](https://colab.research.google.com)
- Buat notebook baru dengan nama: `Lab14_NIM_NamaLengkap.ipynb`
- Siapkan akses ke salah satu AI assistant:
  - ChatGPT: [chat.openai.com](https://chat.openai.com)
  - Claude: [claude.ai](https://claude.ai)
  - Gemini: [gemini.google.com](https://gemini.google.com)
- **Penting:** Setiap interaksi dengan AI harus didokumentasikan dalam AI Usage Log

---

## Template AI Usage Log

Salin template berikut ke cell pertama notebook Anda. Isi setiap kali Anda berinteraksi dengan AI.

```python
# === AI USAGE LOG ===
# Lab 14: AI-Augmented Programming
# Nama  : [Nama Lengkap]
# NIM   : [NIM]
# Tanggal: [Tanggal Praktikum]
# AI Tool: [ChatGPT / Claude / Gemini / Lainnya]

"""
=== ENTRI LOG ===

--- Interaksi #1 ---
Waktu       : [HH:MM]
Exercise    : [Nomor exercise]
Prompt      : [Prompt yang diberikan ke AI]
Tujuan      : [Mengapa Anda meminta bantuan AI]
Ringkasan   : [Ringkasan respons AI dalam 2-3 kalimat]
Evaluasi    : [Benar/Salah/Sebagian — jelaskan]
Modifikasi  : [Perubahan yang Anda lakukan pada output AI]
Pelajaran   : [Apa yang Anda pelajari dari interaksi ini]

--- Interaksi #2 ---
...

"""
```

---

## Langkah-langkah Praktikum

### Exercise 1: Prompt CRIDE untuk Generate Fungsi (15 menit)

Tulis prompt menggunakan framework **CRIDE** untuk meminta AI menghasilkan sebuah fungsi Python.

**Tugas:** Minta AI membuat fungsi `hitung_statistik(data)` yang menerima list angka dan mengembalikan dictionary berisi: jumlah, rata-rata, median, modus, nilai minimum, dan nilai maksimum.

```python
# === EXERCISE 1: PROMPT CRIDE ===

# Langkah 1: Tulis prompt CRIDE Anda di bawah ini
prompt_cride = """
Context : Saya mahasiswa Informatika semester 1 yang sedang belajar
          Python dasar. Saya belum pernah menggunakan library statistik.

Role    : Bertindaklah sebagai tutor pemrograman Python yang
          menjelaskan kode dengan bahasa Indonesia sederhana.

Instruction: Buatkan fungsi Python bernama hitung_statistik(data)
             yang menerima parameter list berisi angka (integer/float).

Details : - Fungsi mengembalikan dictionary dengan key: 'jumlah',
            'rata_rata', 'median', 'modus', 'minimum', 'maksimum'
          - TIDAK boleh menggunakan library eksternal (hanya Python murni)
          - Tangani edge case: list kosong (return dictionary dengan
            semua value None)
          - Sertakan docstring dan komentar penjelasan
          - Modus: jika ada beberapa nilai dengan frekuensi sama,
            kembalikan yang terkecil

Examples: hitung_statistik([4, 2, 7, 2, 9, 4, 2])
          → {'jumlah': 7, 'rata_rata': 4.29, 'median': 4,
             'modus': 2, 'minimum': 2, 'maksimum': 9}
"""

print("=== PROMPT CRIDE ===")
print(prompt_cride)

# Langkah 2: Kirim prompt ke AI, lalu paste hasilnya di bawah ini
# [PASTE KODE DARI AI DI SINI]

# Langkah 3: Evaluasi — jalankan test case berikut
# Setelah Anda paste fungsi dari AI, jalankan pengujian ini:

def test_hitung_statistik():
    """Test case untuk memvalidasi output AI."""

    # Test 1: Data normal
    hasil = hitung_statistik([4, 2, 7, 2, 9, 4, 2])
    assert hasil['jumlah'] == 7, f"Jumlah salah: {hasil['jumlah']}"
    assert abs(hasil['rata_rata'] - 4.29) < 0.01, f"Rata-rata salah: {hasil['rata_rata']}"
    assert hasil['median'] == 4, f"Median salah: {hasil['median']}"
    assert hasil['modus'] == 2, f"Modus salah: {hasil['modus']}"
    assert hasil['minimum'] == 2, f"Minimum salah: {hasil['minimum']}"
    assert hasil['maksimum'] == 9, f"Maksimum salah: {hasil['maksimum']}"
    print("  Test 1 (data normal): LULUS")

    # Test 2: Satu elemen
    hasil = hitung_statistik([42])
    assert hasil['jumlah'] == 1, f"Jumlah salah: {hasil['jumlah']}"
    assert hasil['rata_rata'] == 42.0, f"Rata-rata salah: {hasil['rata_rata']}"
    print("  Test 2 (satu elemen): LULUS")

    # Test 3: List kosong
    hasil = hitung_statistik([])
    assert hasil['jumlah'] is None or hasil['jumlah'] == 0
    print("  Test 3 (list kosong): LULUS")

    # Test 4: Data genap
    hasil = hitung_statistik([1, 3, 5, 7])
    assert hasil['median'] == 4.0, f"Median genap salah: {hasil['median']}"
    print("  Test 4 (median genap): LULUS")

    print("\n  Semua test LULUS!")

# Uncomment setelah paste fungsi dari AI:
# test_hitung_statistik()

print("\nCatatan: Paste fungsi dari AI, lalu jalankan test.")
print("Catat di AI Usage Log: apakah kode AI lolos semua test?")
```

### Exercise 2: AI sebagai Debugger (15 menit)

Berikan kode yang mengandung bug ke AI, minta AI untuk menemukan dan memperbaikinya.

```python
# === EXERCISE 2: DEBUGGING DENGAN AI ===

# Kode berikut mengandung BEBERAPA BUG. Jangan perbaiki sendiri dulu!
# Kirim ke AI dan minta AI menemukan semua bug-nya.

kode_bermasalah = """
def cari_kata_terpanjang(kalimat):
    '''Mencari kata terpanjang dalam sebuah kalimat.'''
    kata_list = kalimat.split(' ')
    terpanjang = kata_list[0]
    panjang_max = 0

    for kata in kata_list:
        if len(kata) > panjang_max:
            terpanjang = kata

    return terpanjang, panjang_max

# Bug 1: panjang_max tidak pernah diupdate
# Bug 2: Tidak menangani kalimat kosong
# Bug 3: Tanda baca ikut dihitung sebagai bagian kata
"""

print("=== KODE BERMASALAH ===")
print(kode_bermasalah)

# Langkah 1: Kirim kode di atas ke AI dengan prompt:
# "Temukan semua bug dalam kode Python berikut dan jelaskan perbaikannya."

# Langkah 2: Paste kode perbaikan dari AI di bawah ini
# [PASTE KODE PERBAIKAN DARI AI DI SINI]

# Langkah 3: Validasi perbaikan AI dengan test berikut
def test_cari_kata_terpanjang():
    """Test case untuk validasi perbaikan."""
    # Test 1: Kalimat normal
    kata, panjang = cari_kata_terpanjang("Saya belajar pemrograman Python")
    assert kata == "pemrograman", f"Kata salah: {kata}"
    assert panjang == 11, f"Panjang salah: {panjang}"
    print("  Test 1 (normal): LULUS")

    # Test 2: Kalimat dengan tanda baca
    kata, panjang = cari_kata_terpanjang("Halo, selamat datang!")
    assert kata == "selamat", f"Kata salah: {kata}"
    print("  Test 2 (tanda baca): LULUS")

    # Test 3: Kalimat kosong
    kata, panjang = cari_kata_terpanjang("")
    assert kata == "" or kata is None
    print("  Test 3 (kosong): LULUS")

    print("\n  Semua test LULUS!")

# Uncomment setelah paste perbaikan dari AI:
# test_cari_kata_terpanjang()

# Langkah 4: Evaluasi — Apakah AI menemukan SEMUA bug?
# Catat di AI Usage Log.
print("\nPertanyaan refleksi:")
print("  1. Apakah AI menemukan semua 3 bug?")
print("  2. Apakah ada bug tambahan yang AI temukan?")
print("  3. Apakah penjelasan AI mudah dipahami?")
```

### Exercise 3: AI untuk Refactoring (10 menit)

Berikan kode yang bekerja tapi "berantakan" ke AI, minta AI merapikan.

```python
# === EXERCISE 3: REFACTORING DENGAN AI ===

# Kode berikut BERFUNGSI tapi kualitasnya buruk.
# Kirim ke AI untuk di-refactor.

kode_berantakan = """
def f(x):
    r=[]
    for i in range(len(x)):
        if x[i]%2==0:
            r.append(x[i]**2)
    s=0
    for j in r:
        s=s+j
    return s,r,len(r)
"""

print("=== KODE BERANTAKAN ===")
print(kode_berantakan)

# Langkah 1: Kirim ke AI dengan prompt:
# "Refactor kode Python berikut agar lebih readable:
#  - Gunakan nama variabel deskriptif dalam bahasa Indonesia
#  - Tambahkan docstring dan komentar
#  - Gunakan Python idiomatik (list comprehension jika sesuai)
#  - Jangan ubah fungsionalitas"

# Langkah 2: Paste kode hasil refactoring dari AI
# [PASTE KODE REFACTORED DARI AI DI SINI]

# Langkah 3: Bandingkan output — harus sama
data_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Jalankan kode asli
def f(x):
    r=[]
    for i in range(len(x)):
        if x[i]%2==0:
            r.append(x[i]**2)
    s=0
    for j in r:
        s=s+j
    return s,r,len(r)

hasil_asli = f(data_test)
print(f"Hasil kode asli      : {hasil_asli}")

# Uncomment setelah paste kode refactored:
# hasil_refactored = [nama_fungsi_baru](data_test)
# print(f"Hasil kode refactored: {hasil_refactored}")
# assert hasil_asli == hasil_refactored, "Output berbeda!"
# print("Output SAMA — refactoring berhasil!")

print("\nPertanyaan evaluasi:")
print("  1. Apakah kode AI lebih readable?")
print("  2. Apakah AI menggunakan list comprehension?")
print("  3. Apakah nama variabel sudah deskriptif?")
```

### Exercise 4: AI untuk Code Review (10 menit)

Tulis kode sendiri, lalu minta AI melakukan code review.

```python
# === EXERCISE 4: CODE REVIEW OLEH AI ===

# Langkah 1: Tulis fungsi berikut SENDIRI (tanpa bantuan AI)
# Fungsi: konversi_suhu(nilai, dari, ke)
# - Konversi suhu antara Celsius, Fahrenheit, dan Kelvin
# - Parameter 'dari' dan 'ke' bisa berupa: 'C', 'F', atau 'K'

# Tulis kode Anda di sini:
def konversi_suhu(nilai, dari, ke):
    """Konversi suhu antara Celsius (C), Fahrenheit (F), dan Kelvin (K)."""
    # [TULIS IMPLEMENTASI ANDA SENDIRI]
    pass

# Langkah 2: Kirim kode Anda ke AI dengan prompt:
# "Review kode Python saya berikut. Berikan feedback tentang:
#  1. Kebenaran logika
#  2. Penanganan error
#  3. Kelengkapan kasus
#  4. Kualitas kode (readability, naming, documentation)
#  5. Saran perbaikan"

# Langkah 3: Test kode Anda
def test_konversi_suhu():
    """Test case untuk konversi suhu."""
    # Celsius ke Fahrenheit: C * 9/5 + 32
    assert abs(konversi_suhu(100, 'C', 'F') - 212.0) < 0.01
    print("  C→F (100°C = 212°F): LULUS")

    # Fahrenheit ke Celsius: (F - 32) * 5/9
    assert abs(konversi_suhu(32, 'F', 'C') - 0.0) < 0.01
    print("  F→C (32°F = 0°C)  : LULUS")

    # Celsius ke Kelvin: C + 273.15
    assert abs(konversi_suhu(0, 'C', 'K') - 273.15) < 0.01
    print("  C→K (0°C = 273.15K): LULUS")

    # Konversi ke diri sendiri
    assert abs(konversi_suhu(50, 'C', 'C') - 50.0) < 0.01
    print("  C→C (50 = 50)     : LULUS")

    print("\n  Semua test LULUS!")

# Uncomment setelah implementasi:
# test_konversi_suhu()

# Langkah 4: Catat feedback AI di AI Usage Log
# Apakah ada saran yang membantu? Perbaiki kode Anda berdasarkan feedback.
```

### Exercise 5: AI Pair Programming Session (25 menit)

Bangun program kecil bersama AI. Dokumentasikan setiap interaksi.

```python
# === EXERCISE 5: AI PAIR PROGRAMMING ===
# Bangun program: Kalkulator IPK Mahasiswa

# Fitur yang harus dibuat:
# 1. Input daftar mata kuliah (nama, SKS, nilai huruf)
# 2. Konversi nilai huruf ke angka (A=4.0, A-=3.7, B+=3.3, B=3.0, dll)
# 3. Hitung IPK = Σ(SKS × nilai_angka) / Σ(SKS)
# 4. Tampilkan transkrip dalam format tabel
# 5. Kategorisasi: Cumlaude (≥3.5), Sangat Memuaskan (≥3.0), Memuaskan (≥2.5)

# === ATURAN PAIR PROGRAMMING ===
# 1. Anda HARUS menulis pseudocode/rencana DULU sebelum meminta AI
# 2. Minta AI membantu SATU bagian pada satu waktu, bukan seluruh program
# 3. EVALUASI setiap output AI sebelum melanjutkan ke bagian berikutnya
# 4. CATAT setiap interaksi di AI Usage Log

# === RENCANA PROGRAM (tulis sendiri) ===
print("=== RENCANA PROGRAM KALKULATOR IPK ===\n")
rencana = """
1. Buat dictionary konversi nilai huruf → angka
2. Buat fungsi input_matkul() untuk memasukkan data mata kuliah
3. Buat fungsi hitung_ipk() untuk menghitung IPK
4. Buat fungsi tampilkan_transkrip() untuk menampilkan tabel
5. Buat fungsi kategorisasi_ipk() untuk menentukan predikat
6. Buat program utama yang mengintegrasikan semua fungsi
"""
print(rencana)

# === CONTOH IMPLEMENTASI AWAL (tulis sendiri) ===
# Mulai dengan bagian yang Anda bisa, lalu minta AI membantu sisanya

# Bagian 1: Konversi nilai (bisa Anda tulis sendiri)
KONVERSI_NILAI = {
    'A': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D': 1.0,
    'E': 0.0
}

# Bagian 2-6: Lanjutkan dengan bantuan AI
# Contoh prompt untuk setiap bagian:
contoh_prompt = """
Bagian 2 — Prompt ke AI:
"Buatkan fungsi input_matkul() yang meminta user memasukkan
data mata kuliah satu per satu. Setiap mata kuliah berisi
nama (string), SKS (int), dan nilai huruf (string).
Gunakan list of dictionaries. Berhenti input jika user
mengetik 'selesai'. Validasi nilai huruf terhadap dictionary
konversi yang sudah saya buat."
"""
print("Contoh prompt untuk AI:", contoh_prompt)

# [LENGKAPI PROGRAM DI SINI DENGAN BANTUAN AI]
# Pastikan Anda memahami SETIAP baris kode yang dihasilkan AI

# === CONTOH OUTPUT YANG DIHARAPKAN ===
print("\n=== CONTOH OUTPUT PROGRAM ===\n")
contoh_output = """
╔══════════════════════════════════════════════════╗
║         TRANSKRIP NILAI MAHASISWA               ║
║  Nama : Ahmad Fauzi                             ║
║  NIM  : 2025001                                 ║
╠══════════════════════════════════════════════════╣
║ No  Mata Kuliah              SKS  Nilai  Angka  ║
║ 1   Algoritma & Pemrograman   3    A      4.0   ║
║ 2   Kalkulus I                3    B+     3.3   ║
║ 3   Fisika Dasar              2    A-     3.7   ║
║ 4   Bahasa Inggris            2    B      3.0   ║
╠══════════════════════════════════════════════════╣
║ Total SKS: 10    IPK: 3.53                      ║
║ Predikat : Cumlaude                             ║
╚══════════════════════════════════════════════════╝
"""
print(contoh_output)
```

---

## Refleksi Akhir

Jawab pertanyaan berikut di cell terakhir notebook Anda.

```python
# === REFLEKSI AI-AUGMENTED PROGRAMMING ===
print("=" * 50)
print("  REFLEKSI AKHIR")
print("=" * 50)

refleksi = """
Jawab pertanyaan berikut berdasarkan pengalaman Anda hari ini:

1. Apa yang AI lakukan dengan BAIK dalam sesi ini?
   Jawaban: [...]

2. Apa yang AI lakukan dengan KURANG BAIK atau SALAH?
   Jawaban: [...]

3. Kapan Anda merasa PERLU bantuan AI? Kapan TIDAK perlu?
   Jawaban: [...]

4. Apakah Anda memahami SEMUA kode yang dihasilkan AI?
   Jika tidak, bagian mana yang belum paham?
   Jawaban: [...]

5. Bagaimana AI mengubah cara Anda belajar programming?
   Apakah positif atau negatif? Mengapa?
   Jawaban: [...]

6. Sebagai Muslim yang menjunjung kejujuran, bagaimana Anda
   akan menggunakan AI secara etis dalam tugas kuliah?
   Jawaban: [...]
"""
print(refleksi)

# === RANGKUMAN PENGGUNAAN AI ===
print("\n=== RANGKUMAN PENGGUNAAN AI ===")
print(f"Total interaksi dengan AI  : [isi jumlah]")
print(f"AI tool yang digunakan     : [ChatGPT/Claude/Gemini]")
print(f"Output AI yang benar       : [jumlah] dari [total]")
print(f"Output AI yang perlu edit  : [jumlah] dari [total]")
print(f"Output AI yang salah       : [jumlah] dari [total]")
print(f"Pelajaran terpenting       : [isi]")
```

---

## Tantangan Tambahan

1. **Prompt Engineering Battle:** Tulis 3 versi prompt berbeda untuk tugas yang sama. Bandingkan kualitas output AI. Mana prompt terbaik dan mengapa?
2. **AI Limitation Test:** Temukan kasus di mana AI memberikan jawaban yang salah atau menyesatkan. Dokumentasikan mengapa AI gagal.
3. **Teach-Back Method:** Minta AI menjelaskan konsep rekursi. Evaluasi penjelasan AI: apakah akurat? Apakah ada yang kurang? Tulis versi penjelasan yang lebih baik.

---

## Checklist Penyelesaian

- [ ] Menulis prompt CRIDE dan mengevaluasi output AI (Exercise 1)
- [ ] Memberikan kode buggy ke AI dan memvalidasi perbaikan (Exercise 2)
- [ ] Meminta AI melakukan refactoring dan memverifikasi kesamaan output (Exercise 3)
- [ ] Menulis kode sendiri dan meminta AI melakukan code review (Exercise 4)
- [ ] Menyelesaikan sesi pair programming dengan AI (Exercise 5)
- [ ] Mengisi AI Usage Log untuk SETIAP interaksi dengan AI
- [ ] Menjawab pertanyaan refleksi akhir
- [ ] Notebook disimpan dengan nama `Lab14_NIM_NamaLengkap.ipynb`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
