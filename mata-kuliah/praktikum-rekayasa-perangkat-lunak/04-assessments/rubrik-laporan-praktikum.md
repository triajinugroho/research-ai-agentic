# Rubrik Penilaian Laporan Praktikum (L1-L13) — IF2206

| Informasi | Detail |
|-----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Komponen** | Laporan Praktikum (25% dari nilai akhir) |
| **Jumlah Laporan** | 13 laporan (L1-L13), satu per sesi praktikum |
| **Format** | Markdown di repository GitHub |
| **Pengumpulan** | Pull Request ke repository praktikum |

---

## A. Daftar Laporan Praktikum

| Laporan | Minggu | Topik | CPMK |
|---------|--------|-------|------|
| L1 | 1 | Setup Dev Environment & GitHub Codespaces | CPMK-1 |
| L2 | 2 | Git Branching & Pull Request Workflow | CPMK-2 |
| L3 | 3 | Requirements Documentation (SRS) | CPMK-3 |
| L4 | 4 | User Story & Sprint Planning | CPMK-3 |
| L5 | 5 | Frontend Development (HTML/CSS/JS) | CPMK-4 |
| L6 | 6 | Backend Development (Flask API) | CPMK-4 |
| L7 | 7 | Database Integration & ORM | CPMK-4 |
| — | 8 | *Responsi Tengah Semester (RTS) — tidak ada laporan* | — |
| L8 | 9 | Unit Testing (pytest & Jest) | CPMK-5 |
| L9 | 10 | Integration & API Testing | CPMK-5 |
| L10 | 11 | CI/CD dengan GitHub Actions | CPMK-6 |
| L11 | 12 | Docker & Deployment | CPMK-6 |
| L12 | 13 | AI Pair Programming & Code Review | CPMK-7 |
| L13 | 14 | Sprint Review & Retrospective | CPMK-7 |

**Nilai Laporan = Rata-rata (L1 + L2 + ... + L13)**

---

## B. Template Struktur Laporan Standar

Setiap laporan praktikum **wajib** mengikuti struktur berikut:

### B.1 Header Laporan

```markdown
# Laporan Praktikum [NN] — [Topik]

| Informasi | Detail |
|-----------|--------|
| **Nama** | [Nama Lengkap] |
| **NIM** | [NIM] |
| **Kelompok** | [Nomor Kelompok] |
| **Praktikum ke-** | [1-14] |
| **Tanggal** | [DD Bulan YYYY] |
```

### B.2 Tujuan Praktikum

Salin tujuan praktikum dari modul lab. Mahasiswa boleh menambahkan tujuan personal learning.

```markdown
## Tujuan Praktikum

1. [Tujuan 1 dari modul lab]
2. [Tujuan 2 dari modul lab]
3. [Tujuan tambahan personal — opsional]
```

### B.3 Langkah-langkah yang Dikerjakan

Bagian utama laporan. Dokumentasikan **setiap langkah** yang dikerjakan dengan:
- Kode yang ditulis/dimodifikasi (dalam code block dengan syntax highlighting)
- Screenshot hasil/output
- Penjelasan singkat apa yang dilakukan dan mengapa

```markdown
## Langkah-langkah

### Langkah 1: [Judul Langkah]

[Penjelasan apa yang dilakukan]

```python
# Kode yang ditulis
```

**Output:**

![Screenshot output](images/lab-NN-step1.png)

[Penjelasan output — apa yang terjadi dan mengapa]
```

### B.4 Tantangan Tambahan

Jika mengerjakan tantangan tambahan dari modul lab (bonus).

```markdown
## Tantangan Tambahan

### Tantangan 1: [Judul]
[Dokumentasi pengerjaan tantangan]
```

### B.5 Analisis & Refleksi

Bagian **kritis** yang menunjukkan pemahaman konsep.

```markdown
## Analisis & Refleksi

### Apa yang Dipelajari
[Penjelasan konsep yang dipahami dari praktikum ini]

### Kesulitan dan Solusi
[Apa kesulitan yang dihadapi dan bagaimana mengatasinya]

### Hubungan dengan Materi Teori IF2205
[Bagaimana praktikum ini terhubung dengan materi teori minggu ini]
```

### B.6 AI Usage Log

**Wajib** diisi jika menggunakan AI tools. Kosongkan jika tidak menggunakan AI.

```markdown
## AI Usage Log

| No | Tanggal | Tool | Prompt (ringkas) | Output (ringkas) | Modifikasi | Pemahaman |
|----|---------|------|------------------|------------------|------------|-----------|
| 1 | ... | ... | ... | ... | ... | Y/N |

*Jika tidak menggunakan AI, tuliskan: "Tidak menggunakan AI tools pada praktikum ini."*
```

### B.7 Referensi

```markdown
## Referensi

1. [Modul Lab NN — IF2206]
2. [Sumber tambahan jika ada]
```

---

## C. Rubrik Penilaian Detail

### Skala Penilaian

| Level | Skor | Deskripsi |
|-------|------|-----------|
| **Excellent** | 4 | Melebihi ekspektasi |
| **Good** | 3 | Memenuhi semua kriteria |
| **Adequate** | 2 | Memenuhi kriteria minimum |
| **Inadequate** | 1 | Tidak memenuhi kriteria |

### Tabel Rubrik: 4 Dimensi x 4 Level

| Dimensi | Bobot | 4 (Excellent) | 3 (Good) | 2 (Adequate) | 1 (Inadequate) |
|---------|-------|---------------|----------|---------------|-----------------|
| **Kelengkapan** | 25% | Semua langkah lab selesai **dan** tantangan tambahan dikerjakan. Setiap langkah didokumentasikan dengan kode, screenshot, dan penjelasan. | Semua langkah lab selesai dan didokumentasikan. Tantangan tambahan tidak dikerjakan. | Sebagian besar langkah selesai (75%+). Beberapa langkah kurang dokumentasi. | Kurang dari 50% langkah selesai. Banyak langkah tidak didokumentasikan. |
| **Kebenaran Implementasi** | 30% | Semua kode berjalan sempurna tanpa error. Output sesuai expected output di modul. Clean code, naming convention konsisten. | Kode berjalan dengan benar. Ada minor issues (warning, style inconsistency) tapi tidak memengaruhi fungsionalitas. | Kode berjalan sebagian. Ada error minor yang tidak di-handle. Output sebagian sesuai expected. | Kode tidak berjalan. Banyak error. Output tidak sesuai atau tidak ada output. |
| **Pemahaman Konsep** | 25% | Analisis mendalam yang menunjukkan pemahaman konsep. Refleksi menghubungkan praktikum dengan teori IF2205. Mengidentifikasi trade-offs dan alternatif pendekatan. | Analisis memadai yang menunjukkan pemahaman. Ada refleksi tentang apa yang dipelajari dan kesulitan yang dihadapi. | Analisis dangkal — hanya mendeskripsikan apa yang dilakukan tanpa menjelaskan mengapa. Refleksi minimal. | Tidak ada analisis atau refleksi. Laporan hanya berisi kode dan screenshot tanpa penjelasan. |
| **Dokumentasi & AI Log** | 20% | Format Markdown rapi dan profesional. Screenshot jelas dan relevan. AI Usage Log lengkap dan detail (jika menggunakan AI). Referensi dicantumkan. | Format baik dan mudah dibaca. Screenshot ada. AI Usage Log ada (jika menggunakan AI). | Format cukup tapi ada inkonsistensi. Screenshot kurang jelas atau tidak lengkap. AI Usage Log tidak lengkap. | Format berantakan, sulit dibaca. Tidak ada screenshot. AI Usage Log tidak ada padahal menggunakan AI. |

### Rumus Perhitungan Nilai Laporan

```
Skor Total = (Kelengkapan × 0.25) + (Kebenaran × 0.30) + (Pemahaman × 0.25) + (Dokumentasi × 0.20)

Nilai Laporan = (Skor Total / 4) × 100
```

**Contoh perhitungan:**

| Dimensi | Bobot | Skor | Kontribusi |
|---------|-------|------|------------|
| Kelengkapan | 25% | 3 | 0.75 |
| Kebenaran Implementasi | 30% | 4 | 1.20 |
| Pemahaman Konsep | 25% | 3 | 0.75 |
| Dokumentasi & AI Log | 20% | 3 | 0.60 |
| **Total** | | | **3.30** |

```
Nilai = (3.30 / 4) × 100 = 82.5 → A
```

---

## D. Contoh Laporan Baik vs Kurang Baik

### D.1 Contoh Bagian "Analisis & Refleksi" yang BAIK (Skor 4)

```markdown
## Analisis & Refleksi

### Apa yang Dipelajari

Pada praktikum ini saya mempelajari bagaimana Flask routing bekerja di balik layar.
Flask menggunakan decorator `@app.route()` yang mendaftarkan fungsi Python sebagai
handler untuk URL tertentu. Konsep ini mirip dengan *observer pattern* yang dibahas
di materi teori IF2205 minggu 5 tentang design patterns.

Saya juga memahami perbedaan antara HTTP methods:
- **GET** untuk mengambil data (idempotent — tidak mengubah state)
- **POST** untuk membuat data baru (non-idempotent)
- **PUT** untuk update data keseluruhan
- **DELETE** untuk menghapus data

### Kesulitan dan Solusi

Kesulitan utama: route `/books/<int:book_id>` mengembalikan 500 Internal Server
Error ketika `book_id` tidak ditemukan. Awalnya saya hanya menggunakan
`books[book_id]` yang menyebabkan KeyError.

**Solusi:** Menggunakan `get_or_404()` dari Flask-SQLAlchemy atau manual check
dengan `if not book: return jsonify({"error": "Not found"}), 404`.

### Hubungan dengan Teori IF2205

Praktikum ini mengimplementasikan konsep *software construction* (Bab 7 IF2205),
khususnya tentang coding standards dan error handling. REST API yang dibuat juga
merupakan implementasi dari arsitektur client-server yang dibahas di Bab 5.
```

### D.2 Contoh Bagian "Analisis & Refleksi" yang KURANG BAIK (Skor 1-2)

```markdown
## Analisis & Refleksi

Saya belajar membuat API dengan Flask. Ada kesulitan tapi bisa diatasi.
Praktikum ini berhubungan dengan materi di kelas.
```

**Mengapa kurang baik:**
- Tidak spesifik tentang apa yang dipelajari
- Tidak menjelaskan kesulitan apa dan bagaimana mengatasinya
- Tidak menghubungkan dengan materi teori secara konkret
- Tidak menunjukkan pemahaman konsep

---

## E. Ketentuan AI Usage Log

### E.1 Kapan AI Usage Log Wajib

- AI Usage Log **wajib** dilampirkan di setiap laporan yang menggunakan AI tools.
- Jika **tidak** menggunakan AI, tulis: *"Tidak menggunakan AI tools pada praktikum ini."*
- **L1 dan L2** (yang bersamaan dengan TP1-TP2 yang melarang AI): AI tetap boleh untuk *memahami konsep* (bertanya penjelasan), tapi **tidak boleh** untuk *generate kode*.

### E.2 Apa yang Harus Didokumentasikan

| Kolom | Penjelasan | Contoh Baik | Contoh Buruk |
|-------|------------|-------------|-------------|
| **Tool** | AI tool yang digunakan | "Claude 3.5 Sonnet" | "AI" |
| **Prompt** | Ringkasan pertanyaan/instruksi | "Jelaskan cara membuat migration di Flask-Migrate untuk model Book dengan field title dan isbn" | "bantu kode" |
| **Output** | Ringkasan jawaban AI | "Langkah-langkah migration: flask db init, flask db migrate -m 'add book', flask db upgrade" | "kode migration" |
| **Modifikasi** | Perubahan yang dilakukan mahasiswa | "Menambahkan field `year` dan `author_id` foreign key yang tidak ada di output AI" | "tidak ada" |
| **Pemahaman** | Apakah mahasiswa memahami output | "Y — saya memahami bahwa migration membuat versi database seperti Git untuk schema" | "Y" |

### E.3 Contoh AI Usage Log yang Lengkap

```markdown
## AI Usage Log

| No | Tanggal | Tool | Prompt (ringkas) | Output (ringkas) | Modifikasi | Pemahaman |
|----|---------|------|------------------|------------------|------------|-----------|
| 1 | 2026-04-01 | Claude | "Bagaimana cara setup Flask-Migrate?" | Langkah install + konfigurasi + contoh migration | Menyesuaikan dengan model Book saya, menambahkan field isbn | Y |
| 2 | 2026-04-01 | Copilot | Auto-complete untuk query filter | Suggestion: `Book.query.filter_by(author_id=id).all()` | Menambahkan `.order_by(Book.title)` dan pagination | Y |
| 3 | 2026-04-02 | ChatGPT | "Kenapa migration error 'Target database is not up to date'?" | Penjelasan: perlu `flask db stamp head` lalu `flask db migrate` ulang | Mengikuti langkah yang disarankan, berhasil | Y |
```

---

## F. Kesalahan Umum yang Harus Dihindari

### F.1 Kesalahan Format

| Kesalahan | Dampak | Solusi |
|-----------|--------|--------|
| Laporan dalam format Word/PDF, bukan Markdown | -10% penalti format | Gunakan Markdown di repository GitHub |
| Screenshot tidak ada atau tidak jelas | Mengurangi skor Dokumentasi | Gunakan screenshot yang jelas, crop bagian yang relevan |
| Kode tidak dalam code block | Sulit dibaca, mengurangi skor | Gunakan ` ```python ` untuk code blocks |
| Tidak ada header laporan | Mengurangi skor Kelengkapan | Ikuti template header di Section B.1 |
| File penamaan salah | Sulit ditemukan saat grading | Ikuti format: `laporan-lab-NN-NIM.md` |

### F.2 Kesalahan Konten

| Kesalahan | Dampak | Solusi |
|-----------|--------|--------|
| Copy-paste modul lab tanpa modifikasi | Skor Pemahaman = 1 | Tulis langkah dengan kata-kata sendiri |
| Tidak ada analisis/refleksi | Skor Pemahaman = 1 | Tulis minimal 100 kata analisis |
| Screenshot output orang lain | Pelanggaran akademik | Ambil screenshot sendiri |
| Menggunakan AI tanpa log | Pelanggaran AI policy | Selalu isi AI Usage Log |
| Analisis hanya "Saya belajar X" tanpa elaborasi | Skor Pemahaman = 2 | Jelaskan APA, MENGAPA, dan BAGAIMANA |

### F.3 Kesalahan Pengumpulan

| Kesalahan | Dampak | Solusi |
|-----------|--------|--------|
| Terlambat tanpa alasan | Late penalty berlaku | Kumpulkan tepat waktu |
| Tidak melalui pull request | Tidak dinilai | Selalu kumpulkan via PR |
| PR tanpa deskripsi | Mengurangi skor Dokumentasi | Tulis deskripsi PR yang jelas |
| Commit setelah deadline | Dihitung terlambat | Pastikan commit terakhir sebelum deadline |

---

## G. Alur Penilaian Laporan (Grading Workflow)

```
1. Mahasiswa submit PR sebelum deadline
       │
       ▼
2. Asisten/dosen memeriksa kelengkapan laporan
       │
       ▼
3. Penilaian per dimensi (4 dimensi × skor 1-4)
       │
       ▼
4. Perhitungan nilai sesuai rumus
       │
       ▼
5. Feedback diberikan via PR review comments
       │
       ▼
6. Nilai diinput ke rekap
       │
       ▼
7. Jika nilai < 56 → eligible remedial
       │                     │
       ▼                     ▼
8. Nilai final         Revisi & submit ulang
                       (nilai maks 70)
```

**Timeline penilaian:**
- Nilai laporan diumumkan **maksimal 2 minggu** setelah deadline pengumpulan.
- Feedback diberikan melalui **PR review comments** di GitHub.
- Mahasiswa dapat mengajukan klarifikasi melalui comment di PR.

---

## H. Kebijakan Khusus

### Laporan yang Menonjol

Laporan dengan skor Excellent (4) di semua dimensi **dan** mengerjakan tantangan tambahan dapat direkomendasikan sebagai **contoh laporan** untuk angkatan berikutnya (dengan izin mahasiswa).

### Laporan Terlambat

Late policy berlaku sesuai `assessment-framework-praktikum.md`:
- <= 1 hari: -10%
- 2-3 hari: -25%
- 4-7 hari: -50%
- > 7 hari: nilai 0

### Remedial Laporan

- Maksimal **3 laporan** dapat di-remedial per semester.
- Revisi harus mengikuti feedback spesifik dari dosen.
- Nilai remedial maksimal **70** (setara B).

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
