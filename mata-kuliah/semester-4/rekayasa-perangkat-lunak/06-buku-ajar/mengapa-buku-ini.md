# Mengapa Buku Ini? — Positioning dan Keunggulan

**Tri Aji Nugroho, S.T., M.T.**
Rekayasa Perangkat Lunak — Prodi Informatika, Universitas Al Azhar Indonesia

---

## 1. Lanskap Buku Rekayasa Perangkat Lunak Saat Ini

Dunia pendidikan rekayasa perangkat lunak (*software engineering*) saat ini didominasi oleh buku-buku teks berbahasa Inggris yang telah menjadi standar global selama beberapa dekade. Buku-buku klasik seperti *Software Engineering* karya Ian Sommerville dan *Software Engineering: A Practitioner's Approach* karya Roger Pressman telah menjadi rujukan utama di perguruan tinggi di seluruh dunia, sementara buku-buku seperti *Clean Code* karya Robert C. Martin dan *The Pragmatic Programmer* karya Hunt & Thomas menawarkan perspektif praktis dari sisi industri. Di sisi lain, bootcamp online dan MOOC seperti Coursera, Udemy, dan freeCodeCamp menyediakan pelatihan yang lebih langsung tetapi seringkali fragmentaris.

Namun, terdapat beberapa kesenjangan mendasar yang belum dijawab oleh sumber-sumber tersebut:

- **Bahasa.** Seluruh buku SE berkualitas ditulis dalam bahasa Inggris, menciptakan hambatan kognitif tambahan bagi mahasiswa Indonesia yang harus memahami konsep arsitektur, design patterns, dan proses pengembangan yang sudah kompleks sekaligus menerjemahkan bahasa pengantar.
- **Konteks.** Studi kasus dan proyek hampir seluruhnya berasal dari konteks perusahaan teknologi Barat — Netflix, Amazon, Google — yang terasa jauh dari realitas pengembangan perangkat lunak di Indonesia.
- **Cakupan SDLC.** Banyak buku fokus pada aspek tertentu saja — Sommerville pada proses dan manajemen, Clean Code pada kualitas kode, bootcamp pada coding skills — tanpa memberikan pandangan end-to-end dari requirements hingga maintenance.
- **Kurikulum.** Tidak ada buku internasional yang dirancang berdasarkan kerangka OBE (*Outcome-Based Education*) dan KKNI yang menjadi standar pendidikan tinggi di Indonesia.
- **AI dalam SE.** Meskipun era AI-augmented development (Copilot, Claude Code, Cursor) telah mengubah cara software dibangun, belum ada buku SE yang secara sistematis mengintegrasikan AI tools ke dalam setiap tahap SDLC.
- **Multi-language.** Dunia industri menggunakan banyak bahasa pemrograman secara bersamaan, namun kebanyakan buku akademik hanya menggunakan satu bahasa.
- **DevOps & CI/CD.** Banyak buku SE yang masih berhenti di level teori tanpa memberikan pengalaman hands-on dengan tools DevOps modern seperti Docker, GitHub Actions, dan cloud deployment.

Buku **"Rekayasa Perangkat Lunak: Proses, Desain, dan Praktik Modern dengan AI"** hadir untuk menjawab kesenjangan tersebut.

---

## 2. Tabel Perbandingan Komprehensif

Tabel berikut membandingkan buku ini dengan sumber-sumber utama yang banyak digunakan dalam pendidikan rekayasa perangkat lunak:

| Kriteria | Sommerville (*SE*, 10th Ed) | Pressman (*SE: Practitioner's*) | Clean Code (Martin) | Bootcamp Online | MOOC (Coursera/Udemy) | **Buku Ini** |
|----------|:---------------------------:|:-------------------------------:|:--------------------:|:----------------:|:---------------------:|:------------:|
| **Bahasa** | English | English | English | English/Mixed | English | **Indonesia** |
| **Target audiens** | CS Undergrad / Grad | CS Undergrad / Practitioners | Developers | Career changers | Self-learners | **Informatika S1** |
| **Cakupan SDLC** | Requirements → Management | Requirements → Quality | Coding only | Coding → Deployment | Varies | **Requirements → Maintenance (full SDLC)** |
| **Bahasa pemrograman** | Tidak spesifik | Java-oriented | Java/C# examples | JS/Python (1 bahasa) | Varies | **Python + JavaScript (multi-language)** |
| **Integrasi AI tools** | Tidak | Tidak | Tidak | Minim | Minim | **Ya — setiap bab, setiap tahap SDLC** |
| **Cloud IDE** | Tidak | Tidak | Tidak | Varies | Varies | **GitHub Codespaces** |
| **DevOps & CI/CD hands-on** | Teori saja | Teori saja | Tidak | Varies | Varies | **Ya — Docker, GitHub Actions, Cloud Deploy** |
| **Konteks studi kasus** | UK / Global | American | American | American / Global | American / Global | **Indonesia (UMKM, layanan publik, kampus)** |
| **Berbasis OBE/KKNI** | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya — dengan pemetaan CPMK** |
| **Nilai-nilai Islami** | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya — terintegrasi** |
| **AI Corner / AI Literacy** | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya — progresif per bab** |
| **Latihan soal bertingkat** | Ya (satu level) | Ya (satu level) | Tidak ada | Project-based | Quizzes | **Ya — 3 tingkat (dasar, menengah, mahir)** |
| **Tim proyek Agile/Scrum** | Teori Agile | Teori Agile | Tidak | Individual | Individual | **Ya — proyek tim dengan Scrum** |
| **SWEBOK v4 (2024) aligned** | SWEBOK v3 | SWEBOK v3 | Tidak | Tidak | Tidak | **Ya — SWEBOK v4** |
| **Harga / Akses** | Komersial | Komersial | Komersial | Berbayar | Freemium | **Gratis (institusional)** |

> **Catatan:** Tabel ini bukan untuk mendiskreditkan buku-buku lain yang telah terbukti berkualitas tinggi. Setiap buku memiliki keunggulan dan konteks penggunaannya masing-masing. Perbandingan ini bertujuan untuk menunjukkan posisi unik buku ini dalam ekosistem buku rekayasa perangkat lunak yang tersedia.

---

## 3. Keunggulan Unik — 10 Diferensiator Utama

### 3.1 Pertama di Indonesia: Buku SE Berbahasa Indonesia dengan OBE + AI-Augmented

Buku ini adalah buku rekayasa perangkat lunak pertama di Indonesia yang dirancang secara eksplisit berdasarkan kerangka OBE (*Outcome-Based Education*) dan KKNI, sekaligus mengintegrasikan AI tools sebagai bagian integral dari proses belajar. Setiap bab memiliki pemetaan **CPMK** (*Capaian Pembelajaran Mata Kuliah*) yang jelas, tujuan pembelajaran ditulis menggunakan taksonomi **Bloom** yang terukur (C2–C6), dan asesmen dirancang untuk mengukur ketercapaian CPMK.

Tidak ada buku SE internasional yang menyediakan pemetaan kurikulum semacam ini untuk konteks pendidikan tinggi Indonesia. Buku ini dirancang agar langsung selaras dengan **RPS** (*Rencana Pembelajaran Semester*) standar 16 minggu, sehingga dosen dapat langsung mengadopsinya tanpa adaptasi kurikulum yang rumit.

### 3.2 Multi-Language: Python + JavaScript — Praktik Industri Nyata

Berbeda dari kebanyakan buku akademik yang hanya menggunakan satu bahasa pemrograman, buku ini menggunakan **dua bahasa**: Python untuk backend dan scripting, serta JavaScript/TypeScript untuk frontend dan full-stack development. Pendekatan ini mencerminkan realitas industri di mana software engineer bekerja dengan multiple technology stacks secara bersamaan.

Mahasiswa belajar bahwa rekayasa perangkat lunak bukan tentang menguasai satu bahasa — melainkan tentang menguasai **prinsip-prinsip** yang berlaku di semua bahasa: clean code, design patterns, testing, dan kolaborasi tim.

### 3.3 Full SDLC Coverage — Dari Requirements hingga Maintenance

Buku ini mencakup **seluruh siklus hidup pengembangan perangkat lunak** secara end-to-end:

| Tahap SDLC | Bab | Kompetensi |
|-------------|-----|-----------|
| **Requirements** | 3, 4 | Elicitation, SRS, use case, user story, backlog |
| **Design** | 5, 6 | Arsitektur, design patterns, UML, database design, API design |
| **Construction** | 7 | Clean code, refactoring, Git flow, code review |
| **Testing** | 8, 9 | Unit, integration, E2E, TDD, AI-assisted testing |
| **Deployment** | 10 | CI/CD, Docker, GitHub Actions, cloud deployment |
| **Maintenance** | 11 | Technical debt, metrics, versioning, evolution |
| **Management** | 12 | Agile/Scrum, sprint planning, estimation |

Tidak ada buku tunggal di pasar yang memberikan cakupan selengkap ini dengan pendekatan hands-on di setiap tahap.

### 3.4 GitHub Codespaces — Cloud IDE Profesional

Seluruh kode dalam buku ini dirancang untuk berjalan di **GitHub Codespaces**, cloud IDE profesional yang digunakan oleh developer di industri. Keuntungan pendekatan ini:

- Mahasiswa langsung terbiasa dengan environment profesional, bukan toy environments
- **Konsistensi environment** — tidak ada masalah "works on my machine"
- Akses ke terminal, debugger, extensions, dan Git integration yang lengkap
- Mendukung Python dan JavaScript/TypeScript secara bersamaan
- **Gratis untuk mahasiswa** melalui GitHub Education

Ini menjadi solusi yang jauh lebih realistis dibandingkan setup lokal yang problematis atau environment sederhana yang tidak mencerminkan praktik industri.

### 3.5 AI sebagai Co-Developer — Copilot, Claude Code, Cursor

Buku ini adalah buku SE pertama yang mengintegrasikan penggunaan **AI development tools** secara sistematis di setiap tahap SDLC. Fitur **"AI Corner"** di setiap bab mengajarkan mahasiswa cara:

- Menggunakan **GitHub Copilot** untuk code completion dan pair programming
- Memanfaatkan **Claude Code** untuk code review, debugging, dan refactoring
- Menggunakan **Cursor** untuk AI-native development workflow
- Memvalidasi output AI dan mengidentifikasi potensi *hallucination*
- Menulis *prompt* yang efektif untuk setiap tahap SDLC — dari requirements analysis hingga test generation
- Menerapkan **agentic development** — di mana AI mengeksekusi multi-step tasks secara otonom

Pada akhir buku, mahasiswa memiliki **AI literacy** yang relevan untuk dunia kerja modern di mana AI-augmented development sudah menjadi standar industri.

### 3.6 100% Konteks Indonesia — Studi Kasus dan Proyek Lokal

Seluruh studi kasus dan proyek dalam buku ini berasal dari konteks Indonesia:

| Domain | Contoh Studi Kasus |
|--------|-------------------|
| **UMKM Indonesia** | Sistem manajemen toko online untuk UMKM batik, sistem POS warung kopi |
| **Layanan Publik** | Aplikasi antrian puskesmas, sistem informasi RT/RW digital |
| **Kampus** | Sistem manajemen tugas mahasiswa, portal informasi akademik |
| **Transportasi** | Aplikasi pemesanan tiket bus antar kota, tracking pengiriman paket |
| **E-commerce** | Marketplace produk UMKM lokal, sistem review dan rating |
| **Sosial** | Aplikasi donasi dan zakat online, platform volunteer komunitas |

Mahasiswa membangun perangkat lunak untuk masalah yang mereka pahami konteksnya — bukan clone Netflix atau Twitter, melainkan solusi nyata untuk kebutuhan masyarakat Indonesia.

### 3.7 Nilai-Nilai Islami Terintegrasi Secara Natural

Sebagai buku ajar di **Universitas Al Azhar Indonesia**, buku ini menanamkan nilai-nilai Islami secara natural dalam konteks rekayasa perangkat lunak:

- **Amanah** (*trustworthiness*) — Menulis kode yang jujur dan dapat dipercaya; tidak menyembunyikan bug; transparent reporting dalam sprint review
- **Keadilan** (*al-'adl*) — Distribusi tugas yang adil dalam tim Scrum; memastikan aksesibilitas aplikasi untuk semua pengguna
- **Ihsan** (*excellence*) — Mengejar kualitas kode terbaik (*clean code*); tidak berhenti di "sekadar berjalan" tetapi menulis software yang maintainable dan scalable
- **Itqan** (*precision, mastery*) — Ketelitian dalam testing; thoroughness dalam code review; presisi dalam dokumentasi
- **Syura** (*consultation*) — Kolaborasi tim yang demokratis; code review sebagai budaya saling menasihati; retrospective yang konstruktif

Nilai-nilai ini bukan sekadar sisipan, melainkan terintegrasi dalam praktik SE sehari-hari — dari cara mahasiswa melakukan code review hingga cara mereka mengelola proyek tim.

### 3.8 SWEBOK v4 (2024) Aligned — Standar Terbaru SE Body of Knowledge

Buku ini diselaraskan dengan **SWEBOK v4** (*Software Engineering Body of Knowledge*, edisi 2024), standar terbaru dari IEEE Computer Society yang mendefinisikan area-area pengetahuan dalam rekayasa perangkat lunak. Kebanyakan buku SE yang beredar masih merujuk pada SWEBOK v3 (2014) yang sudah berusia satu dekade.

Pembaruan penting di SWEBOK v4 yang dicakup buku ini meliputi:
- **Software Construction** yang diperluas dengan DevOps dan CI/CD
- **Software Engineering Models and Methods** yang mencakup AI-assisted development
- **Software Engineering Professional Practice** yang memperbarui standar etika profesi
- Penekanan pada **security by design** dan **sustainability** dalam pengembangan perangkat lunak

### 3.9 Proyek Tim dengan Agile/Scrum — Metodologi Industri Nyata

Buku ini tidak hanya mengajarkan Agile/Scrum secara teori (seperti Sommerville dan Pressman), tetapi mahasiswa **mempraktikkannya secara langsung** dalam proyek akhir:

- Membentuk **Scrum team** dengan peran Product Owner, Scrum Master, dan Developers
- Menjalankan **sprint** nyata dengan sprint planning, daily standup (asynchronous), sprint review, dan retrospective
- Mengelola **product backlog** dan **sprint backlog** di GitHub Projects
- Melakukan **code review** melalui pull request dengan standar kualitas yang jelas
- Menyelesaikan proyek web app end-to-end dalam 3–4 sprint

Pengalaman kolaborasi tim ini mempersiapkan mahasiswa untuk realitas kerja di industri, di mana software tidak pernah dibangun sendirian.

### 3.10 DevOps & CI/CD Hands-On — Bukan Sekadar Teori

Banyak buku SE yang membahas DevOps dan CI/CD hanya sebagai konsep. Buku ini memberikan **pengalaman hands-on** yang nyata:

- Menulis **Dockerfile** untuk containerization aplikasi
- Membuat **GitHub Actions workflow** untuk automated testing dan deployment
- Men-*deploy* aplikasi ke **cloud platform** (Vercel/Railway)
- Menerapkan **semantic versioning** dan release management
- Memahami **monitoring** dan **logging** dasar di lingkungan produksi

Pada akhir buku, mahasiswa tidak hanya tahu apa itu CI/CD — mereka telah membangun pipeline CI/CD yang berfungsi untuk proyek mereka sendiri.

---

## 4. Progressive AI Literacy

AI Corner dalam buku ini dirancang secara **progresif** — kemampuan interaksi dengan AI dibangun secara bertahap dari bab ke bab:

| Bab | Level AI Literacy | Contoh Aktivitas |
|-----|-------------------|------------------|
| 1–4 | **Basic** | Menulis prompt sederhana untuk memahami konsep SE; meminta AI menjelaskan perbedaan Waterfall vs Agile; menggunakan AI untuk menyusun draf user story |
| 5–7 | **Intermediate** | Menggunakan Copilot untuk pair programming; meminta AI membantu merancang arsitektur MVC; AI-assisted UML generation; code review dengan Claude Code |
| 8–11 | **Advanced** | AI-generated unit tests; menggunakan AI untuk menulis Dockerfile dan CI/CD pipeline; AI-assisted debugging dan refactoring; security analysis dengan AI |
| 12–14 | **Expert** | AI-augmented Agile workflow; end-to-end development dengan AI sebagai co-developer; agentic development; evaluasi kritis dan responsible use of AI dalam tim |

Pada akhir buku, mahasiswa memiliki kompetensi untuk menggunakan AI secara produktif, kritis, dan bertanggung jawab dalam seluruh siklus pengembangan perangkat lunak profesional.

---

## 5. Siapa yang Cocok Menggunakan Buku Ini?

| Kategori | Profil Pembaca | Manfaat Utama |
|----------|----------------|---------------|
| **Primer** | Mahasiswa S1 Informatika semester 4, terutama di Universitas Al Azhar Indonesia | Buku utama mata kuliah Rekayasa Perangkat Lunak (IF2205), selaras dengan RPS dan CPMK |
| **Sekunder** | Mahasiswa IT lainnya (Sistem Informasi, Teknik Komputer) yang membutuhkan fondasi SE | Pendekatan hands-on dengan cakupan SDLC lengkap |
| **Tersier** | Dosen yang ingin mengadopsi pendekatan *AI-augmented teaching* dalam mata kuliah SE | Kerangka kerja lengkap untuk mengintegrasikan AI dalam pembelajaran SE |
| **Tambahan** | Junior developer yang ingin memperkuat fondasi SE dan mempelajari praktik modern | Belajar mandiri dengan materi terstruktur, proyek realistis, dan kode yang siap dijalankan |

> **Untuk dosen di luar UAI:** Buku ini dapat diadaptasi untuk mata kuliah Rekayasa Perangkat Lunak di program studi lain. Pemetaan CPMK dapat disesuaikan dengan kurikulum masing-masing institusi, sementara konten dan studi kasus tetap relevan untuk konteks pendidikan tinggi Indonesia secara umum.

---

## 6. Apa yang Buku Ini *Bukan*

Transparansi tentang cakupan buku sama pentingnya dengan menjelaskan keunggulannya. Buku ini **bukan**:

| Buku Ini Bukan... | Untuk Itu, Rujuk... |
|--------------------|---------------------|
| Buku teori SE mendalam (formal methods, model checking, software reliability engineering) | Sommerville — *Software Engineering* (10th Ed); Ghezzi et al. — *Fundamentals of SE* |
| Buku arsitektur enterprise (microservices at scale, distributed systems, cloud-native architecture) | Richards & Ford — *Fundamentals of Software Architecture*; Newman — *Building Microservices* |
| Buku pemrograman Python atau JavaScript murni (OOP, data structures, algorithms) | Lutz — *Learning Python*; Eloquent JavaScript; MDN Web Docs |
| Buku DevOps lanjutan (Kubernetes, infrastructure as code, observability at scale) | Humble & Farley — *Continuous Delivery*; Morris — *Infrastructure as Code* |
| Buku manajemen proyek IT (portfolio management, PMO, enterprise governance) | PMI — *PMBOK Guide*; Kerzner — *Project Management* |
| Pengganti bimbingan dosen dan diskusi kelas | Interaksi langsung di kelas tetap merupakan komponen esensial pembelajaran |

Buku ini berada di **irisan** antara fondasi rekayasa perangkat lunak, praktik modern (DevOps, CI/CD, Agile), dan AI-augmented development — dirancang khusus untuk mahasiswa informatika yang membutuhkan ketiga kompetensi tersebut secara terpadu untuk menjadi software engineer yang siap kerja.

---

## 7. Testimoni

> *Bagian ini akan diisi dengan testimoni dari mahasiswa, kolega dosen, dan pengguna buku setelah buku digunakan dalam perkuliahan.*

---

> "Akhirnya ada buku RPL yang tidak berhenti di teori Waterfall dan UML saja. Saya belajar membangun web app dari requirements sampai deploy, lengkap dengan CI/CD dan Docker — persis seperti yang dilakukan di industri."
>
> — *[Nama Mahasiswa], Mahasiswa Informatika UAI Angkatan 2024*

---

> "AI Corner di setiap bab mengubah cara saya coding. Sekarang saya tahu kapan harus pakai Copilot, kapan harus pakai Claude Code, dan yang paling penting — kapan harus berpikir sendiri."
>
> — *[Nama Mahasiswa], Mahasiswa Informatika UAI Angkatan 2024*

---

> "Sebagai dosen RPL di program studi lain, saya melihat buku ini sebagai contoh bagaimana buku ajar SE modern seharusnya ditulis — hands-on, multi-language, dan mengintegrasikan AI sebagai bagian dari workflow, bukan sekadar appendix."
>
> — *[Nama Dosen], Dosen Rekayasa Perangkat Lunak, [Universitas]*

---

## Penutup

Buku ini tidak bermaksud menggantikan buku-buku SE klasik yang telah teruji. Sommerville dan Pressman tetap menjadi referensi penting dalam fondasi teori rekayasa perangkat lunak. Clean Code dan The Pragmatic Programmer tetap menjadi panduan esensial untuk kualitas kode. MOOC dan bootcamp tetap menjadi sumber belajar yang baik untuk keterampilan spesifik.

Yang buku ini tawarkan adalah sesuatu yang belum tersedia di pasar: **sebuah buku rekayasa perangkat lunak yang berbicara dalam bahasa mahasiswa Indonesia, menggunakan studi kasus yang mereka kenal, mengajarkan full SDLC dari requirements hingga maintenance, membekali mereka dengan AI tools modern, dan mempersiapkan mereka untuk era di mana membangun software berkualitas bukan hanya soal menulis kode — melainkan soal menguasai proses, desain, dan praktik yang membuat software itu dapat diandalkan, dipelihara, dan membawa manfaat bagi masyarakat.**

Itulah mengapa buku ini ditulis. Itulah mengapa buku ini perlu ada.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
— Program Studi Informatika, Universitas Al Azhar Indonesia
