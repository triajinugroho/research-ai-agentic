# BAB 3: REQUIREMENTS ENGINEERING

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 2.1 | Menerapkan teknik elicitation (interview, observation, prototyping) untuk mengumpulkan kebutuhan | C3 (Menerapkan) |
| 2.2 | Menyusun dokumen SRS sesuai standar IEEE 830/ISO 29148 | C3 (Menerapkan) |

---

## 3.1 Pengantar Requirements Engineering

### 3.1.1 Mengapa Requirements Penting?

> **60% kegagalan proyek software disebabkan oleh requirements yang buruk** — Standish Group

Requirements engineering (RE) adalah proses sistematik untuk menemukan, mendokumentasikan, dan memelihara kebutuhan perangkat lunak. RE adalah fondasi dari seluruh proses SE — jika fondasi salah, seluruh bangunan akan runtuh.

### 3.1.2 Proses Requirements Engineering

```
Elicitation → Analysis → Specification → Validation → Management
(Kumpulkan)   (Analisis)  (Dokumentasi)  (Validasi)   (Kelola perubahan)
```

## 3.2 Teknik Elicitation

Elicitation adalah proses **mengumpulkan kebutuhan** dari stakeholder. Tidak semua kebutuhan bisa langsung ditanyakan — beberapa perlu digali.

| Teknik | Deskripsi | Kapan Digunakan | Kelebihan | Kekurangan |
|--------|-----------|-----------------|-----------|------------|
| **Interview** | Tanya jawab langsung | Awal proyek, kebutuhan inti | Mendalam, bisa follow-up | Memakan waktu, bias interviewer |
| **Questionnaire** | Survey tertulis | Banyak stakeholder | Skala besar, kuantitatif | Tidak bisa follow-up langsung |
| **Observation** | Mengamati pengguna bekerja | Proses bisnis kompleks | Menemukan kebutuhan tersembunyi | Hawthorne effect |
| **Prototyping** | Mock-up untuk feedback | UI/UX, requirements tidak jelas | Visual, feedback cepat | Bisa salah ekspektasi |
| **Brainstorming** | Diskusi terbuka | Fase awal, inovasi | Kreatif, kolaboratif | Bisa tidak fokus |
| **Document Analysis** | Pelajari dokumen existing | Sistem pengganti | Objektif, detil | Bisa outdated |

### 3.2.1 Contoh Interview Script

```
Konteks: Interview dengan pustakawan untuk Sistem Perpustakaan Kampus

P: Bagaimana proses peminjaman buku saat ini?
J: Mahasiswa datang, cari buku di rak, bawa ke meja sirkulasi, 
   saya catat di buku log manual.

P: Apa masalah utama dengan proses saat ini?
J: Sering kehilangan data, mahasiswa tidak tahu buku sudah dipinjam 
   atau belum, dan sulit tracking keterlambatan.

P: Jika ada sistem baru, apa yang paling Anda butuhkan?
J: Pencarian buku online, notifikasi otomatis untuk keterlambatan, 
   dan laporan statistik peminjaman.
```

## 3.3 Jenis Requirements

### 3.3.1 Functional Requirements (FR)

Apa yang sistem **harus lakukan** — fungsi dan fitur:

- FR-01: Sistem harus memungkinkan mahasiswa mendaftar dengan NIM dan email kampus
- FR-02: Sistem harus menampilkan katalog buku dengan pencarian berdasarkan judul, penulis, atau ISBN
- FR-03: Sistem harus memproses peminjaman buku maksimal 3 buku per mahasiswa
- FR-04: Sistem harus mengirim notifikasi 3 hari sebelum batas pengembalian

### 3.3.2 Non-Functional Requirements (NFR)

**Bagaimana** sistem harus bekerja — kualitas dan batasan:

| Kategori | Contoh | Metrik |
|----------|--------|--------|
| **Performance** | Halaman pencarian loading < 3 detik | Response time |
| **Scalability** | Mendukung 1000 pengguna bersamaan | Concurrent users |
| **Security** | Data personal dienkripsi AES-256 | Encryption standard |
| **Availability** | Uptime 99.5% (8.76 jam downtime/tahun) | SLA |
| **Usability** | Mahasiswa bisa meminjam buku dalam < 5 klik | Task completion |
| **Compatibility** | Berjalan di Chrome, Firefox, Safari terbaru | Browser support |

## 3.4 Software Requirements Specification (SRS)

### 3.4.1 Struktur SRS (IEEE 830)

```
1. Pendahuluan
   1.1 Tujuan
   1.2 Ruang Lingkup
   1.3 Definisi, Akronim, dan Singkatan
   1.4 Referensi
   1.5 Overview Dokumen

2. Deskripsi Umum
   2.1 Perspektif Produk
   2.2 Fungsi Produk (ringkasan)
   2.3 Karakteristik Pengguna
   2.4 Batasan
   2.5 Asumsi dan Dependensi

3. Kebutuhan Spesifik
   3.1 External Interface Requirements
       3.1.1 User Interface
       3.1.2 Hardware Interface
       3.1.3 Software Interface
       3.1.4 Communications Interface
   3.2 Functional Requirements
   3.3 Non-Functional Requirements
   3.4 Design Constraints
```

### 3.4.2 Tips Menulis Requirements yang Baik

Setiap requirement harus:
- **Jelas** — tidak ambigu ("cepat" → "response time < 3 detik")
- **Testable** — bisa diverifikasi (ada kriteria pass/fail)
- **Consistent** — tidak bertentangan satu sama lain
- **Complete** — mencakup semua kebutuhan yang diketahui
- **Feasible** — bisa diimplementasikan dengan teknologi yang ada
- **Traceable** — bisa dilacak ke sumber (stakeholder, regulasi)

### 3.4.3 Contoh Requirement yang Buruk vs Baik

| Buruk | Baik |
|-------|------|
| "Sistem harus cepat" | "Halaman harus loading dalam < 3 detik pada koneksi 4G" |
| "Sistem harus user-friendly" | "Mahasiswa baru bisa menyelesaikan peminjaman dalam < 5 menit tanpa training" |
| "Sistem harus aman" | "Password harus minimal 8 karakter dengan kombinasi huruf, angka, dan simbol" |

## 3.5 Validasi Requirements

### 3.5.1 Checklist Validasi

- [ ] Apakah setiap requirement **jelas** dan tidak ambigu?
- [ ] Apakah setiap requirement **testable**?
- [ ] Apakah semua requirement **konsisten** (tidak bertentangan)?
- [ ] Apakah requirements **lengkap** (mencakup semua kebutuhan)?
- [ ] Apakah setiap requirement **feasible** (bisa diimplementasi)?
- [ ] Apakah setiap requirement **traceable** (ada sumbernya)?

### 3.5.2 Teknik Validasi

1. **Review** — stakeholder membaca dan memberikan feedback
2. **Prototyping** — buat mock-up untuk konfirmasi pemahaman
3. **Test case generation** — jika bisa dibuat test case, requirement cukup jelas
4. **Consistency checking** — periksa konflik antar requirement

## 3.6 Requirements Management

Requirements akan berubah sepanjang proyek. Requirements management mencakup:
- **Version control** — track perubahan di setiap versi requirement
- **Change request** — proses formal untuk mengajukan perubahan
- **Impact analysis** — analisis dampak perubahan terhadap sistem
- **Traceability** — lacak requirement dari sumber ke implementasi ke test

---

## AI Corner: AI untuk Requirements Engineering (Level: Basic)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| Generate requirements | "Buatkan 10 functional requirements untuk Sistem Antrian Puskesmas" | Review dan sesuaikan — AI bisa miss konteks lokal |
| Validasi requirement | "Apakah requirement ini testable: 'Sistem harus responsif'?" | AI bisa membantu identifikasi ambiguitas |
| Buat interview script | "Buatkan daftar pertanyaan interview untuk pustakawan dalam RE Sistem Perpustakaan" | Gunakan sebagai starting point |

**Peringatan:** AI bisa menghasilkan requirements yang terlihat bagus tapi tidak sesuai kebutuhan nyata stakeholder. Selalu validasi dengan stakeholder sebenarnya.

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Jelaskan 5 tahap proses requirements engineering.
2. Apa perbedaan functional dan non-functional requirements?
3. Sebutkan 6 teknik elicitation dan kapan masing-masing digunakan.
4. Sebutkan 6 kriteria requirement yang baik.

### Level Menengah (C3-C4)
5. Buatlah 10 functional requirements dan 5 non-functional requirements untuk Sistem Informasi Perpustakaan Kampus.
6. Tuliskan interview script untuk elicitation kebutuhan Sistem Antrian Puskesmas (minimal 10 pertanyaan).
7. Analisis mengapa requirement "Sistem harus memiliki performa yang baik" adalah requirement yang buruk, dan perbaiki menjadi requirement yang testable.

### Level Mahir (C5-C6)
8. Seorang klien startup e-commerce meminta fitur baru setiap minggu. Bagaimana Anda mengelola requirements yang terus berubah? Rancang proses requirements management yang cocok.
9. Evaluasi SRS berikut dan identifikasi 5 masalah (ambiguitas, inkonsistensi, atau gap).

---

## Rangkuman

1. **Requirements engineering** adalah proses sistematik untuk menemukan, mendokumentasikan, dan memelihara kebutuhan software.
2. **Elicitation** menggunakan berbagai teknik (interview, observation, prototyping) karena tidak semua kebutuhan bisa langsung ditanyakan.
3. **Functional requirements** mendefinisikan APA yang sistem lakukan, **non-functional** mendefinisikan BAGAIMANA.
4. **SRS (IEEE 830)** adalah format standar untuk dokumentasi requirements.
5. Requirements harus **jelas, testable, konsisten, lengkap, feasible, dan traceable**.
6. **Requirements management** penting karena kebutuhan akan berubah sepanjang proyek.

---

## Referensi

1. Wiegers, K. E. & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.
2. IEEE Std 830-1998. *Recommended Practice for Software Requirements Specifications*.
3. ISO/IEC/IEEE 29148:2018. *Systems and Software Engineering — Life Cycle Processes — Requirements Engineering*.
4. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 4-5. Pearson.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
