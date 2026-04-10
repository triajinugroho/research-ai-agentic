# BAB 2: PROSES DAN MODEL PENGEMBANGAN PERANGKAT LUNAK

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 1.3 | Membedakan model proses tradisional (Waterfall, V-Model, Spiral) dan modern (Agile, DevOps) | C2 (Memahami) |
| 1.4 | Menjelaskan framework Scrum (roles, events, artifacts) dan Agile Manifesto | C2 (Memahami) |

---

## 2.1 Konsep Proses Perangkat Lunak

Setiap pengembangan software mengikuti serangkaian aktivitas terstruktur yang disebut **proses perangkat lunak** (*software process*).

### 2.1.1 Empat Aktivitas Fundamental

1. **Specification** — mendefinisikan apa yang harus dilakukan sistem
2. **Development** — merancang dan mengimplementasikan sistem
3. **Validation** — memastikan sistem sesuai kebutuhan pelanggan
4. **Evolution** — mengubah sistem sesuai kebutuhan baru

Setiap model proses mengatur keempat aktivitas ini dengan cara yang berbeda.

## 2.2 Model Tradisional

### 2.2.1 Waterfall Model

Model paling awal dan paling sederhana — setiap fase harus selesai sebelum fase berikutnya dimulai:

```
Requirements → Design → Implementation → Testing → Deployment → Maintenance
     ↓            ↓          ↓              ↓          ↓            ↓
  (Selesai     (Selesai   (Selesai      (Selesai   (Selesai    (Ongoing)
   dulu)        dulu)      dulu)         dulu)      dulu)
```

**Kelebihan:**
- Sederhana dan mudah dikelola
- Dokumentasi lengkap di setiap fase
- Cocok jika requirements stabil dan jelas

**Kekurangan:**
- Tidak fleksibel terhadap perubahan
- Pelanggan baru melihat produk di akhir
- Risiko besar jika requirements salah

**Cocok untuk:** Embedded systems, proyek regulasi ketat, proyek kecil dengan requirements pasti.

### 2.2.2 V-Model

Ekstensi dari Waterfall yang menambahkan **fase testing** paralel untuk setiap fase development:

```
Requirements ────────────────── Acceptance Testing
    Design ──────────────── System Testing
        Detailed Design ── Integration Testing
            Coding ──── Unit Testing
```

Setiap fase development memiliki pasangan testing yang memvalidasinya.

### 2.2.3 Spiral Model (Boehm, 1986)

Menambahkan **risk analysis** di setiap iterasi. Proses bergerak dalam spiral:

```
       Planning
      /        \
  Risk          Development
  Analysis      & Testing
      \        /
       Evaluation
```

Cocok untuk proyek besar, berisiko tinggi, dan inovatif.

## 2.3 Agile Software Development

### 2.3.1 Agile Manifesto (2001)

**4 Values:**

| Kami menghargai... | Lebih dari... |
|-------------------|---------------|
| **Individuals and interactions** | Processes and tools |
| **Working software** | Comprehensive documentation |
| **Customer collaboration** | Contract negotiation |
| **Responding to change** | Following a plan |

*"Walaupun item di sebelah kanan bernilai, kami lebih menghargai item di sebelah kiri."*

### 2.3.2 12 Principles of Agile

1. Kepuasan pelanggan melalui delivery yang cepat dan berkelanjutan
2. Menyambut perubahan requirements, bahkan di tahap akhir
3. Deliver working software secara berkala (minggu-bulan)
4. Kolaborasi harian antara bisnis dan developer
5. Bangun proyek di sekitar individu yang termotivasi
6. Face-to-face conversation sebagai komunikasi paling efektif
7. Working software adalah ukuran utama kemajuan
8. Sustainable development — pace yang bisa dipertahankan
9. Perhatian berkelanjutan pada technical excellence
10. Kesederhanaan — memaksimalkan pekerjaan yang TIDAK dilakukan
11. Tim yang self-organizing menghasilkan arsitektur terbaik
12. Refleksi berkala untuk menjadi lebih efektif

### 2.3.3 Scrum Framework

Scrum adalah framework Agile paling populer, dengan struktur:

```
Product     Sprint        Daily         Sprint      Sprint
Backlog  →  Planning  →   Standup   →   Review  →  Retrospective
   ↑           ↓          (15 min)      (Demo)     (Improve)
   │      Sprint Backlog     ↓
   │           ↓          Working
   └─── Feedback ←──── Increment (2-4 minggu)
```

**Scrum Roles:**

| Role | Tanggung Jawab |
|------|----------------|
| **Product Owner** | Mengelola Product Backlog, mewakili stakeholder, memutuskan prioritas |
| **Scrum Master** | Memfasilitasi proses Scrum, menghilangkan hambatan, melindungi tim |
| **Development Team** | 3-9 orang, self-organizing, cross-functional, deliver increment |

**Scrum Events:**

| Event | Durasi | Tujuan |
|-------|--------|--------|
| Sprint Planning | Maks 8 jam (sprint 4 minggu) | Memilih backlog item, merencanakan sprint |
| Daily Standup | 15 menit | Sinkronisasi: apa yang dikerjakan, hambatan |
| Sprint Review | Maks 4 jam | Demo increment ke stakeholder |
| Sprint Retrospective | Maks 3 jam | Refleksi: apa yang diperbaiki |

**Scrum Artifacts:**

| Artifact | Deskripsi |
|----------|-----------|
| Product Backlog | Daftar semua yang dibutuhkan produk, diurutkan prioritas |
| Sprint Backlog | Subset Product Backlog yang dikerjakan dalam sprint ini |
| Increment | Produk yang bisa digunakan di akhir sprint |

## 2.4 Kanban

Kanban fokus pada **continuous flow** tanpa timeboxed sprints:

```
┌──────────┐  ┌──────────────┐  ┌──────────┐  ┌──────────┐
│  To Do   │→ │ In Progress  │→ │  Review  │→ │   Done   │
│          │  │  (WIP: 3)    │  │ (WIP: 2) │  │          │
└──────────┘  └──────────────┘  └──────────┘  └──────────┘
```

**Prinsip utama:**
- **Visualize workflow** — gunakan board (fisik atau digital)
- **Limit WIP** — batasi jumlah item in-progress
- **Manage flow** — ukur dan optimasi lead time
- **Continuous improvement** — perbaiki proses secara inkremental

## 2.5 DevOps Culture

```
     Plan → Code → Build → Test
       ↑                      ↓
    Monitor ← Operate ← Deploy ← Release
```

**DevOps = Development + Operations** — kultur kolaborasi untuk deliver software lebih cepat dan reliable. Prinsip CALMS:
- **C**ulture — kolaborasi Dev + Ops
- **A**utomation — CI/CD pipeline
- **L**ean — eliminasi waste
- **M**easurement — data-driven decisions
- **S**haring — knowledge sharing

## 2.6 Perbandingan Model

| Aspek | Waterfall | Scrum | Kanban | DevOps |
|-------|-----------|-------|--------|--------|
| Iterasi | Tidak | Sprint 2-4 minggu | Continuous | Continuous |
| Requirements | Fixed upfront | Evolving | Evolving | Evolving |
| Tim | Terpisah per fase | Cross-functional | Flexible | Dev + Ops |
| Feedback | Di akhir | Setiap sprint | Real-time | Real-time |
| Dokumentasi | Ekstensif | Minimal, working software | Minimal | As-needed |
| Cocok untuk | Regulasi ketat | Sebagian besar proyek | Maintenance, support | Modern web apps |

### 2.6.1 Memilih Model yang Tepat

Tidak ada satu model yang cocok untuk semua situasi. Pertimbangkan:
- **Stabilitas requirements**: Stabil → Waterfall; Berubah → Agile
- **Ukuran tim**: Kecil → Scrum/Kanban; Besar → Scaled Agile (SAFe)
- **Risiko**: Tinggi → Spiral; Normal → Scrum
- **Industri**: Regulasi ketat → V-Model; Startup → Kanban/Scrum
- **Timeline**: Deadline ketat → Agile (deliver incremental value)

---

## AI Corner: AI untuk Memahami Proses SE (Level: Basic)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| Bandingkan model | "Bandingkan Waterfall vs Scrum untuk proyek e-commerce startup dengan 5 developer" | Evaluasi apakah AI mempertimbangkan semua faktor |
| Simulasi Scrum | "Buatkan contoh Product Backlog untuk sistem antrian puskesmas" | Gunakan sebagai starting point, lalu sesuaikan |
| Pahami konsep | "Jelaskan 12 prinsip Agile dengan contoh praktis di konteks pengembangan mobile app" | Verifikasi dengan Agile Manifesto asli |

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Sebutkan 4 aktivitas fundamental dalam proses perangkat lunak.
2. Jelaskan 3 kelebihan dan 3 kekurangan model Waterfall.
3. Sebutkan 4 values dari Agile Manifesto.
4. Apa perbedaan antara Product Owner dan Scrum Master?

### Level Menengah (C3-C4)
5. Sebuah rumah sakit ingin membangun Sistem Informasi Rekam Medis. Requirements sudah fix oleh regulasi Kemenkes. Tim terdiri dari 10 developer, timeline 1 tahun. Model proses apa yang paling cocok? Jelaskan alasannya.
6. Analisis mengapa banyak perusahaan startup di Indonesia mengadopsi Scrum dibandingkan Waterfall.
7. Buatlah contoh Sprint Backlog untuk Sprint 1 dari proyek Sistem Perpustakaan Kampus.

### Level Mahir (C5-C6)
8. Evaluasi pendekatan hybrid (Waterfall untuk fase Requirements, Agile untuk Construction) — kapan ini cocok dan apa risikonya?
9. Rancang proses pengembangan software yang menggabungkan Scrum + DevOps untuk tim 6 orang yang membangun aplikasi UMKM.

---

## Rangkuman

1. **Proses perangkat lunak** terdiri dari 4 aktivitas fundamental: specification, development, validation, evolution.
2. **Model tradisional** (Waterfall, V-Model, Spiral) cocok untuk proyek dengan requirements stabil dan regulasi ketat.
3. **Agile Manifesto** (2001) mengubah paradigma — dari proses berat ke individu, working software, kolaborasi, dan adaptasi.
4. **Scrum** adalah framework Agile paling populer dengan 3 roles, 4 events, dan 3 artifacts.
5. **Kanban** fokus pada continuous flow dengan WIP limits.
6. **DevOps** menjembatani Development dan Operations untuk delivery yang lebih cepat.
7. **Tidak ada model terbaik** — pilih berdasarkan konteks proyek (requirements, tim, risiko, industri).

---

## Referensi

1. Schwaber, K. & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org.
2. Beck, K. et al. (2001). *Manifesto for Agile Software Development*. agilemanifesto.org.
3. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 2-3. Pearson.
4. Kim, G. et al. (2016). *The DevOps Handbook*. IT Revolution Press.
5. Boehm, B. W. (1988). "A Spiral Model of Software Development and Enhancement." *IEEE Computer*, 21(5).

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
