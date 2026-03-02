# Minggu 14: AI-Augmented Programming dan Code Quality

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Algoritma dan Pemrograman (3 SKS) |
| **Minggu** | 14 dari 16 |
| **Topik** | AI-Augmented Programming dan Code Quality |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python |
| **CPMK** | CPMK-7 |
| **Sub-CPMK** | CPMK-7.5, CPMK-7.6, CPMK-7.7, CPMK-7.8 |
| **Durasi** | 150 menit (Teori: 75 menit, Praktik: 75 menit) |
| **Metode** | Ceramah interaktif, Demo langsung, Praktik AI pair programming, Code review |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Mengidentifikasi** berbagai AI coding assistant dan menjelaskan perannya sebagai alat bantu dalam pemrograman, bukan pengganti pemahaman fundamental (CPMK-7.5)
2. **Menerapkan** framework CRIDE untuk menyusun prompt yang efektif kepada AI coding assistant dan memvalidasi output yang dihasilkan (CPMK-7.6)
3. **Menganalisis** kualitas kode berdasarkan prinsip clean code (PEP 8, penamaan, fungsi, DRY, KISS) dan melakukan code review secara sistematis (CPMK-7.7)
4. **Mengevaluasi** aspek etika penggunaan AI dalam pemrograman dan mendokumentasikan penggunaan AI secara transparan melalui AI Usage Log (CPMK-7.8)

---

## Materi Pembelajaran

### 1. Lanskap AI Coding Assistants (CPMK-7.5)

AI coding assistant adalah alat berbasis kecerdasan buatan yang membantu programmer menulis, memahami, dan memperbaiki kode. Berikut perbandingan beberapa tools utama:

| Tool | Pengembang | Keunggulan | Keterbatasan |
|------|-----------|------------|--------------|
| **GitHub Copilot** | GitHub/OpenAI | Integrasi langsung di IDE, autocomplete real-time | Berbayar, kadang menyarankan kode tidak aman |
| **Claude** | Anthropic | Penalaran mendalam, penjelasan detail, konteks panjang | Berbasis chat, perlu copy-paste kode |
| **ChatGPT** | OpenAI | Serbaguna, banyak bahasa pemrograman | Output kadang terlihat benar tapi salah secara logika |
| **Cursor** | Cursor Inc. | IDE lengkap dengan AI terintegrasi, edit kode langsung | Kurva belajar untuk fitur lanjutan |

**Prinsip utama:** AI adalah *co-pilot*, bukan *auto-pilot*. Mahasiswa harus **memahami** kode yang dihasilkan AI, bukan sekadar menyalin.

### 2. Framework CRIDE untuk Prompt Engineering (CPMK-7.6)

CRIDE adalah kerangka kerja untuk menyusun prompt yang efektif:

| Komponen | Deskripsi | Contoh |
|----------|-----------|--------|
| **C** -- Context | Berikan konteks tentang proyek dan situasi | "Saya sedang membuat program manajemen perpustakaan dalam Python" |
| **R** -- Role | Tentukan peran yang diharapkan dari AI | "Bertindak sebagai tutor Python yang menjelaskan langkah demi langkah" |
| **I** -- Instruction | Instruksi spesifik tentang apa yang diinginkan | "Buatkan fungsi untuk mengurutkan buku berdasarkan judul menggunakan merge sort" |
| **D** -- Details | Detail tambahan: batasan, format output, dll. | "Gunakan type hints, tambahkan docstring, dan sertakan contoh penggunaan" |
| **E** -- Examples | Berikan contoh input/output yang diharapkan | "Input: [('Python', 2020), ('Java', 2019)] -> Output: [('Java', 2019), ('Python', 2020)]" |

**Contoh prompt CRIDE lengkap:**

```
Context: Saya mengerjakan tugas Algoritma dan Pemrograman tentang stack.
Role: Bertindak sebagai tutor yang menjelaskan konsep, bukan hanya memberikan jawaban.
Instruction: Jelaskan cara mengimplementasikan fungsi is_balanced() yang mengecek
apakah tanda kurung dalam sebuah ekspresi seimbang menggunakan stack.
Details: Gunakan list Python sebagai stack, tangani 3 jenis kurung: (), [], {}.
Sertakan komentar penjelasan di setiap bagian penting.
Examples: is_balanced("({[]})") -> True, is_balanced("([)]") -> False
```

### 3. Validasi Kode dari AI (CPMK-7.6)

Kode dari AI **wajib divalidasi** sebelum digunakan. Langkah-langkah validasi:

1. **Baca dan pahami** -- Bisakah Anda menjelaskan setiap baris?
2. **Uji dengan contoh** -- Jalankan dengan input normal, edge case, dan input salah
3. **Periksa logika** -- Apakah algoritma yang digunakan sudah tepat?
4. **Cek keamanan** -- Apakah ada potensi error atau kerentanan?
5. **Sesuaikan** -- Modifikasi agar sesuai dengan kebutuhan spesifik

```python
# Contoh: AI menghasilkan fungsi ini -- apakah sudah benar?
def cari_maks(data):
    maks = 0  # Bug: bagaimana jika semua elemen negatif?
    for item in data:
        if item > maks:
            maks = item
    return maks

# Versi yang diperbaiki setelah validasi:
def cari_maks_fixed(data):
    if not data:
        raise ValueError("List tidak boleh kosong")
    maks = data[0]  # Inisialisasi dengan elemen pertama
    for item in data[1:]:
        if item > maks:
            maks = item
    return maks
```

### 4. Prinsip Clean Code (CPMK-7.7)

#### a. PEP 8 -- Style Guide Python

```python
# Buruk
def f(x,y):return x+y
L=[1,2,3,4,5]

# Baik (PEP 8)
def hitung_jumlah(bilangan_1, bilangan_2):
    """Mengembalikan jumlah dari dua bilangan."""
    return bilangan_1 + bilangan_2

daftar_nilai = [1, 2, 3, 4, 5]
```

#### b. Penamaan yang Bermakna

```python
# Buruk                         # Baik
x = 25                          usia_mahasiswa = 25
lst = [90, 85, 78]              daftar_nilai_ujian = [90, 85, 78]
def proc(d):                    def hitung_rata_rata(daftar_nilai):
    return sum(d) / len(d)          return sum(daftar_nilai) / len(daftar_nilai)
```

#### c. Prinsip DRY (Don't Repeat Yourself) dan KISS (Keep It Simple, Stupid)

```python
# Melanggar DRY -- kode berulang
print(f"Nilai Andi: {andi * 100 / total:.1f}%")
print(f"Nilai Budi: {budi * 100 / total:.1f}%")
print(f"Nilai Cici: {cici * 100 / total:.1f}%")

# Menerapkan DRY -- gunakan loop dan fungsi
def format_persentase(nama, nilai, total):
    return f"Nilai {nama}: {nilai * 100 / total:.1f}%"

for nama, nilai in data_mahasiswa.items():
    print(format_persentase(nama, nilai, total))
```

### 5. Code Review: Checklist Sistematis (CPMK-7.7)

| Aspek | Pertanyaan Kunci |
|-------|-----------------|
| **Kebenaran** | Apakah kode menghasilkan output yang benar untuk semua kasus? |
| **Keterbacaan** | Apakah programmer lain bisa memahami kode ini tanpa penjelasan tambahan? |
| **Efisiensi** | Apakah ada cara yang lebih efisien (Big-O lebih rendah)? |
| **Penamaan** | Apakah nama variabel dan fungsi menjelaskan tujuannya? |
| **Modularitas** | Apakah fungsi melakukan satu tugas saja (Single Responsibility)? |
| **Error Handling** | Apakah kode menangani input yang tidak valid? |
| **Dokumentasi** | Apakah ada docstring dan komentar yang diperlukan? |

### 6. AI Usage Log dan Etika AI (CPMK-7.8)

**AI Usage Log** adalah dokumen transparansi yang mencatat bagaimana AI digunakan dalam pengerjaan tugas:

```markdown
## AI Usage Log -- [Nama Tugas]

### Entri 1
- **Tanggal:** 2026-01-15
- **AI Tool:** Claude
- **Prompt:** "Jelaskan cara kerja binary search dan berikan implementasi Python"
- **Output AI:** [Ringkasan output yang diterima]
- **Modifikasi:** Mengubah nama variabel ke bahasa Indonesia, menambahkan validasi input
- **Pemahaman:** Saya memahami bahwa binary search membagi ruang pencarian menjadi
  setengah setiap iterasi sehingga kompleksitasnya O(log n)
```

**Etika penggunaan AI dalam pemrograman:**

- **Transparansi** -- Selalu catat dan laporkan penggunaan AI
- **Pemahaman** -- Jangan kirim kode AI yang tidak Anda pahami
- **Integritas akademik** -- Gunakan AI untuk belajar, bukan untuk menggantikan proses belajar
- **Tanggung jawab** -- Anda bertanggung jawab penuh atas kode yang Anda kirimkan
- **Pengembangan diri** -- Coba selesaikan dulu sendiri sebelum meminta bantuan AI

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)

1. Membaca panduan PEP 8 ringkas dan mencatat 5 aturan utama yang paling sering dilanggar (8 menit)
2. Membuat akun atau menyiapkan akses ke minimal satu AI coding assistant (Claude/ChatGPT) (7 menit)

### In-class (120 menit)

| Waktu | Kegiatan | Metode |
|-------|----------|--------|
| 0--20 menit | Ceramah: Lanskap AI coding assistants, peran AI sebagai co-pilot, bukan auto-pilot | Ceramah interaktif |
| 20--40 menit | Demo langsung: Framework CRIDE -- dosen menulis prompt secara live dan menganalisis output AI bersama mahasiswa | Live demo dan diskusi |
| 40--60 menit | Hands-on: AI pair programming session -- mahasiswa mencoba menggunakan CRIDE untuk menyelesaikan masalah pemrograman sederhana | Praktik terbimbing |
| 60--75 menit | Ceramah: Prinsip clean code (PEP 8, penamaan, DRY, KISS) dengan contoh buruk vs baik | Ceramah dengan contoh kode |
| 75--95 menit | Latihan: Code review exercise -- mahasiswa menerima kode yang sengaja ditulis buruk dan melakukan review serta refactoring | Praktik berpasangan |
| 95--110 menit | Diskusi: Etika penggunaan AI, integritas akademik, dan pentingnya AI Usage Log | Diskusi kelas |
| 110--120 menit | Workshop: Mengisi template AI Usage Log untuk satu entri berdasarkan sesi pair programming tadi | Praktik mandiri |

### Post-class (15 menit)

1. Menerapkan prinsip clean code pada salah satu tugas sebelumnya -- refactor minimal 1 file kode (8 menit)
2. Melengkapi AI Usage Log untuk semua penggunaan AI dalam Proyek Akhir hingga saat ini (7 menit)

---

## Penugasan

**Proyek Akhir -- Deadline Pengumpulan Final**

Pada minggu ini, mahasiswa mengumpulkan **Proyek Akhir** secara lengkap:

1. **Source code** -- kode Python yang bersih, terdokumentasi, dan berfungsi sesuai spesifikasi
2. **Dokumentasi proyek** -- deskripsi masalah, fitur, cara penggunaan, dan penjelasan arsitektur/desain
3. **AI Usage Log** -- catatan lengkap semua penggunaan AI selama pengerjaan proyek, mengikuti template yang diberikan

**Kriteria kualitas kode:**

- Mengikuti konvensi PEP 8
- Nama variabel dan fungsi bermakna (dalam bahasa Indonesia atau Inggris, konsisten)
- Setiap fungsi memiliki docstring
- Tidak ada kode duplikat yang tidak perlu (DRY)
- Error handling untuk input yang tidak valid

**Deadline:** Sebelum pertemuan Minggu 15 (hari presentasi)

---

## Referensi

1. Gaddis, T. (2021). *Starting Out with Python*, 5th Edition. Pearson. -- Bab tentang Software Development.
2. Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. -- Bab 1--3.
3. PEP 8 -- Style Guide for Python Code: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)
4. Anthropic Claude Documentation: [https://docs.anthropic.com/](https://docs.anthropic.com/)
5. GitHub Copilot Documentation: [https://docs.github.com/en/copilot](https://docs.github.com/en/copilot)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
