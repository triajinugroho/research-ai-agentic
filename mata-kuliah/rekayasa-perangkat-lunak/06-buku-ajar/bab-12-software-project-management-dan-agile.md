# BAB 12: SOFTWARE PROJECT MANAGEMENT DAN AGILE

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 4.3 | Menerapkan teknik estimasi (Planning Poker, T-shirt sizing) dan risk management | C3 (Menerapkan) |
| 4.4 | Mengelola proyek Agile/Scrum dengan sprint management, velocity, dan burndown chart | C4-C5 |

---

## 12.1 Project Management Fundamentals

### 12.1.1 Triple Constraint

```
        Scope
       /     \
      /       \
    Time ─── Cost
         Quality
```

Perubahan di satu constraint mempengaruhi yang lain: menambah scope → tambah time/cost atau kurangi quality.

### 12.1.2 Work Breakdown Structure (WBS)

```
Sistem Perpustakaan v1.0
├── 1. Requirements & Planning
│   ├── 1.1 Elicitation
│   ├── 1.2 SRS Document
│   └── 1.3 Sprint Planning
├── 2. Design
│   ├── 2.1 UML Diagrams
│   ├── 2.2 Database Design
│   └── 2.3 API Design
├── 3. Implementation
│   ├── 3.1 Backend (Flask)
│   ├── 3.2 Frontend (HTML/CSS/JS)
│   └── 3.3 Database (SQLAlchemy)
├── 4. Testing
│   ├── 4.1 Unit Tests
│   ├── 4.2 Integration Tests
│   └── 4.3 E2E Tests
└── 5. Deployment
    ├── 5.1 CI/CD Pipeline
    ├── 5.2 Docker Setup
    └── 5.3 Cloud Deploy
```

## 12.2 Estimation Techniques

### 12.2.1 Planning Poker

Setiap anggota tim mengestimasi secara independen menggunakan kartu Fibonacci:

```
Kartu: 1, 2, 3, 5, 8, 13, 21, ?

Proses:
1. PO membacakan user story
2. Tim berdiskusi singkat
3. Semua reveal kartu bersamaan
4. Jika ada perbedaan besar → diskusi → re-vote
5. Kesepakatan dicatat sebagai story points
```

### 12.2.2 T-Shirt Sizing

| Size | Effort | Story Points | Contoh |
|------|--------|-------------|--------|
| XS | Trivial | 1 | Ubah teks tombol |
| S | Kecil | 2-3 | Tambah field di form |
| M | Medium | 5 | CRUD endpoint baru |
| L | Besar | 8 | Fitur dengan API + UI |
| XL | Sangat besar | 13+ | Modul baru lengkap |

## 12.3 Risk Management

### 12.3.1 Risk Matrix

```
Probability
  High   │ Monitor  │ Mitigate │ URGENT  │
  Medium │ Accept   │ Monitor  │ Mitigate│
  Low    │ Accept   │ Accept   │ Monitor │
         └──────────┴──────────┴─────────┘
           Low       Medium     High
                    Impact
```

### 12.3.2 Contoh Risk Register

| # | Risiko | Probability | Impact | Mitigasi |
|---|--------|-------------|--------|----------|
| R1 | Anggota tim drop out | Medium | High | Cross-training, dokumentasi |
| R2 | Scope creep | High | Medium | MoSCoW prioritization, sprint boundary |
| R3 | Technology baru gagal | Low | High | Prototyping awal, fallback plan |
| R4 | Deadline terlalu ketat | Medium | High | Buffer sprint, MVP approach |

## 12.4 Sprint Management

### 12.4.1 Sprint Planning

**Input:** Product Backlog (prioritized)
**Output:** Sprint Backlog + Sprint Goal

```
Sprint Goal: "User bisa search dan meminjam buku online"

Sprint Backlog:
- [5 pts] Halaman pencarian buku
- [3 pts] API endpoint search
- [8 pts] Proses peminjaman online
- [3 pts] Notifikasi peminjaman berhasil
─────────────────────────────────
Total: 19 story points (sesuai velocity)
```

### 12.4.2 Velocity Tracking

Velocity = jumlah story points yang berhasil diselesaikan per sprint.

```
Sprint 1: 15 points (masih belajar)
Sprint 2: 19 points (mulai stabil)
Sprint 3: 21 points (improved)
Sprint 4: 20 points (consistent)
─────────────────────────────
Average velocity: ~19 points/sprint
```

### 12.4.3 Burndown Chart

```
Story Points
  30 │\
     │ \
  20 │  \  Ideal ─ ─ ─
     │   \        \
  10 │    \___     \
     │        \___  \
   0 │____________\__\___
     Day1  3   5  7  10
```

- **Ideal line**: garis lurus dari total points ke 0
- **Actual line**: progress sebenarnya
- Jika actual di atas ideal → behind schedule
- Jika actual di bawah ideal → ahead of schedule

## 12.5 Team Dynamics

### 12.5.1 Tuckman's Stages

| Stage | Deskripsi | Apa yang Terjadi |
|-------|-----------|------------------|
| **Forming** | Tim baru terbentuk | Perkenalan, exploration |
| **Storming** | Konflik dan negosiasi | Perbedaan pendapat, role clarity |
| **Norming** | Aturan terbentuk | Coding standards, workflow agreed |
| **Performing** | Produktif | Tim bekerja efektif |

### 12.5.2 Retrospective Techniques

**Start-Stop-Continue:**
- **Start:** Mulai code review setiap PR
- **Stop:** Berhenti push langsung ke main
- **Continue:** Lanjutkan daily standup 15 menit

**Mad-Sad-Glad:**
- **Mad:** CI pipeline terlalu lambat
- **Sad:** Tidak sempat implementasi dark mode
- **Glad:** Deployment sukses tanpa downtime

---

## AI Corner: AI untuk Project Management (Level: Expert)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| Risk analysis | "Identifikasi 10 risiko untuk proyek web app tim 4 mahasiswa, deadline 2 bulan" | Sesuaikan dengan konteks tim |
| Sprint planning | "Bantu breakdown user stories ini ke tasks dengan estimasi: [stories]" | AI sebagai starting point, tim yang memutuskan |
| Retrospective | "Buatkan template sprint retrospective untuk tim Agile 4 orang" | Customisasi untuk kebutuhan tim |

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Jelaskan triple constraint dalam project management.
2. Apa itu velocity dan bagaimana mengukurnya?
3. Sebutkan 4 tahap Tuckman's team development.

### Level Menengah (C3-C4)
4. Buatlah WBS untuk proyek Sistem Antrian Puskesmas.
5. Lakukan Planning Poker untuk 5 user stories berikut dan jelaskan alasan estimasi Anda.
6. Buatlah risk register dengan 5 risiko untuk proyek tim Anda.

### Level Mahir (C5-C6)
7. Evaluasi sprint performance tim berdasarkan burndown chart berikut — apa yang bisa diperbaiki?
8. Rancang sprint retrospective process yang efektif untuk tim 4 mahasiswa yang baru pertama kali menggunakan Scrum.

---

## Rangkuman

1. **Project management** mengelola triple constraint: scope, time, cost — dengan quality di tengah.
2. **Estimation** menggunakan Planning Poker (story points) atau T-shirt sizing untuk relative effort.
3. **Risk management** mengidentifikasi, menganalisis, dan memitigasi risiko proyek.
4. **Sprint management** meliputi planning, execution, tracking (velocity, burndown chart).
5. **Team dynamics** (Tuckman's stages) mempengaruhi produktivitas — fasilitasi dengan retrospectives.
6. **Retrospective** (Start-Stop-Continue, Mad-Sad-Glad) mendorong continuous improvement.

---

## Referensi

1. Schwaber, K. & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org.
2. Cohn, M. (2005). *Agile Estimating and Planning*. Prentice Hall.
3. Stellman, A. & Greene, J. (2014). *Learning Agile*. O'Reilly.
4. Rubin, K. S. (2012). *Essential Scrum*. Addison-Wesley.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
