# ANALISIS STRATEGIS MATA KULIAH
## Probabilitas dan Statistik (IF52510033)

**Program Studi Informatika — Universitas Al Azhar Indonesia**
**Semester Ganjil 2026/2027 · Kurikulum Informatika 2025 Revisi 2026**
**Penyusun:** Tri Aji Nugroho, S.T., M.T.

---

## 1. POSISI STRATEGIS MATA KULIAH

### 1.1 Letak dalam Arsitektur Kurikulum

Probabilitas dan Statistik menempati posisi yang tidak biasa: ia adalah mata kuliah **semester pertama** yang menjadi **prasyarat konseptual bagi hampir seluruh jalur lanjutan** Prodi Informatika UAI.

| Dimensi | Posisi |
|---------|--------|
| Semester | 1 (Ganjil) — bersama Dasar Pemrograman, Kalkulus, Pengenalan Ilmu Komputer |
| Bobot | 3 SKS — salah satu MK terbesar di semester 1 |
| Rumpun | Matematika & Fondasi Komputasi (R02) |
| Bahan Kajian | BK08 — *Mathematical and Statistical Foundations* (CS2023: 55 CS Core Hours, 145 KA Core Hours — **KA terbesar dalam CS2023**) |
| CPL | CPL08 (Keterampilan Khusus — algoritma) dan CPL10 (Keterampilan Khusus — data) |
| CPMK | CPMK081 dan CPMK102 |
| Tahap AI | **F (Foundation)** · Mode **K (Kontekstual)** · Pilar **DS–AI** |

### 1.2 Peran dalam Visi Keilmuan 2025

Visi Prodi Informatika UAI 2025 menetapkan tiga domain keilmuan resmi: **Software Engineering, Data Science, dan Artificial Intelligence** — berlandaskan nilai spiritual, moral, dan etika Islami.

Probabilitas dan Statistik adalah **titik masuk paling awal** ke dua dari tiga domain itu. AI Curriculum Infusion Matrix menyatakan perannya secara eksplisit:

> *Fondasi uncertainty, inference dan ML. Tidak perlu AI Sub-CPMK khusus; pastikan probabilitas, distribusi, inference menjadi foundation ML.*

Dan menegaskan prinsip yang menjadi jangkar mata kuliah ini:

> *Mahasiswa tidak boleh menjadi sekadar pengguna model/API.*

Inilah alasan strategis keberadaan mata kuliah ini pada semester 1, bukan semester 3 atau 5: **kemampuan menilai apakah keluaran sebuah model masuk akal harus tumbuh sebelum mahasiswa pertama kali menyentuh model.**

### 1.3 Rantai Ketergantungan Hilir

| Mata Kuliah Hilir | Semester | Apa yang Dipakai dari MK Ini |
|-------------------|----------|------------------------------|
| Analisis Data Statistik (IF52520025) | 2 | Seluruh fondasi inferensi; mengampu CPMK102 yang sama |
| Matematika Diskrit (IF52520003) | 2 | Kaidah pencacahan |
| Sains Data (IF52520026) | 4 | Distribusi, sampling, uji hipotesis |
| Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (IF52510031) | 5 | Distribusi sebagai asumsi model; metrik sebagai statistik; *train/test split* sebagai sampling |
| Jaringan Syaraf Tiruan dan Pembelajaran Mendalam (IF52510032) | 5 | Mengampu CPMK081 yang sama; probabilitas sebagai dasar *loss function* |
| Pengolahan Bahasa Alami (IF52510024) | 7 | Model probabilistik bahasa |
| Keamanan Komputer (IF52510018) | 5 | Analisis risiko probabilistik |
| Komputasi Paralel dan Terdistribusi (IF52510022) | 7 | Analisis kinerja dan variabilitas |
| Metodologi Penelitian (IF52510021) | 7 | Uji hipotesis sebagai validasi temuan |
| Tugas Akhir (IF52520022) | 8 | Seluruh kerangka validasi empiris |

**Sepuluh mata kuliah hilir.** Kegagalan pada mata kuliah ini berdampak berantai sampai Tugas Akhir.

---

## 2. ANALISIS SWOT

### 2.1 Kekuatan (Strengths)

| No | Kekuatan | Implikasi Strategis |
|----|----------|---------------------|
| S1 | **Posisi semester 1 dengan 3 SKS** memberi waktu memadai untuk membangun fondasi sebelum tekanan MK lanjutan | Dapat menuntaskan konsep secara perlahan tanpa mengejar materi |
| S2 | **Dosen pengampu juga mengampu Analisis Data Statistik dan Dasar AI/ML** | Kesinambungan materi terjaga; tidak ada celah atau tumpang tindih antar MK |
| S3 | **Dosen adalah koordinator rumpun Kecerdasan Buatan & Sains Data** | Arah materi dapat langsung diselaraskan dengan kebutuhan jalur AI/DS |
| S4 | **Bahan Kajian BK08 adalah KA terbesar CS2023** (145 KA core hours) — legitimasi kuat | Mudah dipertanggungjawabkan pada akreditasi dan benchmarking internasional |
| S5 | **Python dan Colab sudah menjadi standar repositori** materi Prodi | Tidak perlu membangun infrastruktur baru; mahasiswa cukup browser |
| S6 | **Konteks Indonesia tersedia melimpah** — BPS, Satu Data Indonesia, data kampus | Relevansi tinggi, mudah memotivasi mahasiswa |
| S7 | **Mode Kontekstual (K) pada AI Infusion Matrix** memberi kebebasan merancang tanpa beban Sub-CPMK AI | Fokus penuh pada fondasi, tanpa mengorbankan cakupan |

### 2.2 Kelemahan (Weaknesses)

| No | Kelemahan | Mitigasi yang Dirancang |
|----|-----------|-------------------------|
| W1 | **Mahasiswa semester 1 belum bisa memprogram** — Dasar Pemrograman berjalan paralel, bukan prasyarat | Lab dirancang *scaffolded*: Minggu 1–3 memakai kode yang tinggal dijalankan; kemandirian koding naik bertahap |
| W2 | **Hanya 2 Sub-CPMK** untuk 14 minggu materi — granularitas penilaian kasar | Dibuat lapisan **indikator capaian mingguan** yang menelusuri ke Sub-CPMK (Bagian F RPS) |
| W3 | **Statistika sering dipersepsi sebagai "matematika yang membosankan"** | Setiap konsep dibuka dengan persoalan computing nyata, bukan dengan rumus |
| W4 | **Beban hitung manual vs komputasi** — risiko mahasiswa hanya bisa memanggil fungsi | Kuis dan ujian *closed book* menuntut hitung manual; lab menuntut interpretasi, bukan sekadar keluaran |
| W5 | **Latar belakang matematika SMA yang beragam** (IPA vs IPS vs SMK) | Minggu 1–2 menyediakan penyegaran; tersedia materi pengayaan mandiri di lampiran buku ajar |
| W6 | **Dua kelas paralel (IF26A, IF26H)** berisiko tidak seragam | Modul, lab, dan kisi-kisi dibakukan dalam repositori ini |

### 2.3 Peluang (Opportunities)

| No | Peluang | Rencana Pemanfaatan |
|----|---------|---------------------|
| O1 | **Ledakan kebutuhan talenta data dan AI di Indonesia** | Dijadikan pembuka Minggu 1 untuk membangun motivasi |
| O2 | **Ketersediaan data terbuka pemerintah** yang makin baik (Satu Data Indonesia) | Seluruh contoh dan proyek memakai data nyata Indonesia |
| O3 | **Google Colab gratis** dengan pustaka statistik lengkap | Nol biaya perangkat lunak bagi mahasiswa |
| O4 | **AI generatif sebagai tutor 24 jam** untuk penjelasan alternatif | Diizinkan untuk memahami konsep, dengan batas tegas untuk penilaian |
| O5 | **Literasi statistik menjadi isu publik** (hoaks berbasis angka, survei politik) | Bahan diskusi etika yang sangat kontekstual dan menarik |
| O6 | **Keterhubungan dengan Analisis Data Statistik di semester 2** | Dapat dirancang sebagai satu kesatuan dua semester |

### 2.4 Ancaman (Threats)

| No | Ancaman | Strategi Penanganan |
|----|---------|---------------------|
| T1 | **AI generatif dapat menyelesaikan hampir semua soal statistika standar** | Ujian *closed book*; penilaian menekankan pemeriksaan asumsi dan interpretasi — bagian yang paling sering salah dijawab AI |
| T2 | **Mahasiswa menyerahkan penalaran kepada AI sejak awal** | Kebijakan AI eksplisit (RPS Bagian K.1) + AI Usage Log wajib |
| T3 | **Fenomena "bisa memanggil `scipy` tapi tidak paham"** | Porsi hitung manual dipertahankan pada kuis dan ujian |
| T4 | **Tingkat kegagalan MK matematis di semester 1 cenderung tinggi** | Asesmen berfrekuensi tinggi dan berbobot kecil (13 lab + 4 kuis) agar mahasiswa terdeteksi dini |
| T5 | **Persepsi "statistika bukan Informatika"** | Setiap bab dibuka dengan kasus computing; keterkaitan hilir dijelaskan sejak Minggu 1 |
| T6 | **Kesenjangan akses perangkat** pada sebagian mahasiswa | Colab berjalan di ponsel dan komputer kampus; tidak ada instalasi lokal wajib |

---

## 3. ANALISIS LIMA KEKUATAN PORTER (ADAPTASI PENDIDIKAN)

Kerangka Porter diadaptasi untuk menilai posisi kompetitif lulusan yang menguasai mata kuliah ini.

### 3.1 Ancaman Pendatang Baru — **TINGGI**

Bootcamp data science 3–6 bulan mencetak lulusan yang bisa memakai pustaka statistik dengan cepat.

**Diferensiasi mata kuliah ini:** bootcamp mengajarkan *cara memanggil fungsi*; mata kuliah ini mengajarkan *kapan fungsi itu tidak boleh dipakai*. Pemeriksaan asumsi, pemahaman galat Tipe I/II, dan kesadaran akan batas inferensi adalah pembeda yang tidak dapat dipadatkan menjadi tiga bulan.

### 3.2 Daya Tawar Pemasok (Sumber Pengetahuan) — **RENDAH**

Materi statistika tersedia melimpah dan gratis: buku terbuka, kursus daring, dokumentasi pustaka.

**Implikasi:** nilai tambah dosen bukan pada penyampaian materi, melainkan pada **kurasi, umpan balik atas pekerjaan mahasiswa, dan pembentukan kebiasaan berpikir kritis**. Karena itu porsi terbesar penilaian formatif ada pada 13 laporan lab yang diberi umpan balik, bukan pada ceramah.

### 3.3 Daya Tawar Pembeli (Industri dan Pemberi Kerja) — **TINGGI**

Pemberi kerja dapat memilih dari banyak pelamar dan kini menguji kemampuan secara langsung.

**Respons:** proyek akhir menghasilkan artefak nyata (notebook + laporan) yang dapat masuk portofolio GitHub mahasiswa sejak semester 1.

### 3.4 Ancaman Produk Substitusi — **SEDANG-TINGGI**

AutoML dan asisten AI dapat menjalankan analisis statistik tanpa pemahaman pengguna.

**Respons:** justru inilah yang membuat mata kuliah ini makin relevan. Ketika eksekusi menjadi murah, **penilaian atas kelayakan eksekusi** menjadi mahal. Fokus penilaian digeser ke arah itu.

### 3.5 Persaingan Antar Program Studi — **TINGGI**

Hampir seluruh prodi Informatika di Indonesia memiliki mata kuliah setara.

**Diferensiasi UAI:**
1. **Integrasi nilai Islami dalam etika data** — amanah dalam pelaporan hasil, larangan memanipulasi data agar signifikan.
2. **Konteks Indonesia yang konsisten** pada seluruh contoh dan proyek.
3. **Keterhubungan eksplisit ke jalur AI** melalui AI Curriculum Infusion Matrix.
4. **Kesinambungan pengampu** dengan Analisis Data Statistik dan Dasar AI/ML.

---

## 4. ANALISIS TREN: STATISTIKA DI ERA AI (2026)

### 4.1 Tren yang Membentuk Materi

| Tren | Dampak pada Materi |
|------|--------------------|
| **Krisis reproduksibilitas** di berbagai bidang ilmu | Penekanan pada praregistrasi rencana analisis (proposal Minggu 6) dan notebook yang dapat dijalankan ulang |
| **Kritik atas *p-value*** (pernyataan ASA 2016) | Minggu 11 membahas salah tafsir *p-value* secara eksplisit, bukan sekadar mengajarkan prosedurnya |
| **Pergeseran ke ukuran efek dan interval kepercayaan** | Interval kepercayaan diberi porsi penuh satu minggu (Minggu 10), bukan sekadar pelengkap |
| **AI generatif menjadi antarmuka analisis data** | Kebijakan AI yang tegas; penilaian digeser ke pemeriksaan asumsi dan interpretasi |
| **Data terbuka pemerintah Indonesia makin matang** | Seluruh dataset proyek berasal dari sumber nyata |
| **Statistika Bayesian makin diadopsi industri** | Teorema Bayes diberi porsi satu minggu penuh (Minggu 5) dengan kasus penyaring spam dan diagnosis |
| **Kebutuhan literasi *fairness* pada model** | Dasar konseptualnya — *base rate*, probabilitas bersyarat — ditanam di Minggu 5 |

### 4.2 Yang Dipertahankan, Ditambah, dan Dikurangi

**Dipertahankan (fondasi yang tidak lekang):**
- Aksioma probabilitas dan penurunan aturan dari aksioma.
- Distribusi klasik dan pemilihan distribusi yang tepat.
- Teorema Limit Pusat.
- Hitung manual pada kuis dan ujian.

**Ditambah dibanding kurikulum sebelumnya:**
- Satu minggu penuh untuk Teorema Bayes dan *base rate fallacy* (Minggu 5).
- Pembahasan eksplisit salah tafsir *p-value* (Minggu 11).
- Simulasi cakupan interval kepercayaan (Lab 10) — mengajarkan tafsir "95%" secara empiris.
- Studi kasus A/B testing sebagai jembatan ke praktik industri (Minggu 12).
- Kebijakan dan log penggunaan AI.

**Dikurangi:**
- Pembacaan tabel distribusi secara manual dipersingkat — cukup untuk ujian, selebihnya komputasi.
- Penurunan rumus yang panjang diganti dengan pemahaman intuitif dan simulasi.
- Distribusi yang jarang dipakai di computing (hipergeometrik lanjut, distribusi khusus) dijadikan pengayaan mandiri.

---

## 5. STRATEGI PEMBELAJARAN

### 5.1 Prinsip Perancangan

1. **Konteks dulu, rumus kemudian.** Setiap topik dibuka dengan persoalan computing yang belum bisa dijawab, baru diperkenalkan alatnya.
2. **Hitung manual dan komputasi berjalan beriringan.** Manual membangun pemahaman; komputasi membangun kemampuan kerja. Keduanya dinilai.
3. **Interpretasi adalah inti penilaian.** Angka yang benar tanpa tafsir bernilai separuh.
4. **Asumsi diperiksa, bukan diasumsikan.** Ini pembeda utama dari pengguna pustaka yang tidak paham.
5. **Kejujuran hasil dilindungi.** Hasil tidak signifikan tidak mengurangi nilai.

### 5.2 Penanganan Keberagaman Latar Belakang

| Kelompok | Ciri | Penanganan |
|----------|------|------------|
| Kuat matematika, lemah koding | Umumnya dari SMA IPA | Lab bertahap; kode contoh lengkap pada Minggu 1–3 |
| Kuat koding, lemah matematika | Umumnya dari SMK | Penyegaran konsep pada Minggu 1–2; penekanan intuisi sebelum rumus |
| Lemah keduanya | Perlu perhatian khusus | Asesmen berfrekuensi tinggi untuk deteksi dini; jam konsultasi mingguan |
| Kuat keduanya | Perlu tantangan | Bagian **Tantangan Tambahan** pada setiap lab; soal tingkat Mahir pada latihan bab |

### 5.3 Indikator Keberhasilan Mata Kuliah

| Indikator | Target | Cara Ukur |
|-----------|--------|-----------|
| Ketuntasan `PS-Sub-CPMK081-1` | ≥ 75% mahasiswa mencapai ≥ 60 | Rekap Kuis + Proyek + UAS |
| Ketuntasan `PS-Sub-CPMK102-1` | ≥ 75% mahasiswa mencapai ≥ 60 | Rekap Lab + Proyek + UTS |
| Tingkat kelulusan MK (≥ C) | ≥ 80% | Rekap nilai akhir |
| Penyerahan laporan lab tepat waktu | ≥ 85% | LMS |
| Proyek dengan uji inferensial yang tepat dan asumsi diperiksa | ≥ 70% kelompok | Rubrik proyek |
| Kelengkapan AI Usage Log | 100% laporan | Pemeriksaan berkas |

---

## 6. RISIKO PELAKSANAAN DAN MITIGASI

| Risiko | Kemungkinan | Dampak | Mitigasi |
|--------|-------------|--------|----------|
| Mahasiswa tertinggal pada Minggu 4–5 (lompatan ke probabilitas) | Tinggi | Tinggi | Kuis 2 di Minggu 5 sebagai deteksi dini; sesi konsultasi tambahan Minggu 6 |
| Proyek kelompok tidak merata bebannya | Tinggi | Sedang | Pembagian peran wajib di proposal; seluruh anggota diuji saat tanya jawab |
| Data proyek ternyata tidak memadai | Sedang | Tinggi | Persetujuan proposal di Minggu 6 memeriksa ketersediaan data lebih dulu |
| Ketergantungan AI tidak terdeteksi | Sedang | Tinggi | Tanya jawab lisan saat presentasi; ujian *closed book* berbobot 50% |
| Dua kelas paralel tidak seragam | Sedang | Sedang | Seluruh modul, lab, dan kisi-kisi dibakukan di repositori |
| Colab tidak dapat diakses saat lab | Rendah | Sedang | Notebook dapat diunduh dan dijalankan luring dengan Anaconda |

---

## 7. RENCANA PENINGKATAN BERKELANJUTAN

| Siklus | Kegiatan | Waktu |
|--------|----------|-------|
| Tengah semester | Evaluasi capaian Sub-CPMK dari UTS dan Kuis 1–2; penyesuaian kecepatan materi | Minggu 9 |
| Akhir semester | Rekap ketuntasan kedua Sub-CPMK; analisis butir soal UTS/UAS | Minggu 17 |
| Antar semester | Penyelarasan dengan Analisis Data Statistik (Sem 2) dan Dasar AI/ML (Sem 5) | Sebelum semester berikutnya |
| Tahunan | Pemutakhiran dataset dan kasus; peninjauan kebijakan AI | Sebelum tahun akademik baru |

---

## 8. SIMPULAN STRATEGIS

Probabilitas dan Statistik adalah **mata kuliah dengan daya ungkit tertinggi di semester 1** Prodi Informatika UAI: sepuluh mata kuliah hilir bergantung padanya, dan ia adalah pintu masuk paling awal ke dua dari tiga domain keilmuan dalam visi prodi.

Tantangan terbesarnya bukan cakupan materi, melainkan **godaan untuk melewati pemahaman**. Di era ketika AI dapat menjalankan uji statistik apa pun dalam hitungan detik, nilai seorang sarjana Informatika bergeser dari *kemampuan menjalankan analisis* ke *kemampuan menilai apakah analisis itu layak dijalankan dan layak dipercaya*.

Karena itu mata kuliah ini dirancang dengan satu keputusan yang disengaja: **AI diperlakukan sebagai alat bantu belajar, bukan sebagai mitra kerja.** Keputusan ini berbeda dari mata kuliah lain dalam repositori ini — dan memang seharusnya berbeda. Pada tahap Foundation, kemandirian intelektual adalah capaian pembelajaran itu sendiri.

Landasan nilai **amanah** menemukan bentuknya yang paling konkret di sini: melaporkan hasil apa adanya, tidak memaksakan signifikansi, dan mengakui keterbatasan. Seorang analis data yang jujur tentang ketidakpastian temuannya lebih berharga daripada yang selalu menemukan hasil yang "mengesankan".

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
