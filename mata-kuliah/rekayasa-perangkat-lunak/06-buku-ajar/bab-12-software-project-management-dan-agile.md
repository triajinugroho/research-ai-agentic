# BAB 12: SOFTWARE PROJECT MANAGEMENT DAN AGILE

**Oleh: Tri Aji Nugroho, S.T., M.T.**
**Mata Kuliah:** IF2205 Rekayasa Perangkat Lunak
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Semester:** Genap 2025/2026

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 4.3 | Menerapkan teknik estimasi (Planning Poker, T-shirt sizing, story points) dan risk management dalam proyek perangkat lunak | C3 (Menerapkan) | 75 menit |
| 4.4 | Mengelola proyek Agile/Scrum dengan sprint management, velocity tracking, burndown/burnup charts, Kanban metrics, dan team dynamics | C4-C5 (Menganalisis-Mengevaluasi) | 75 menit |

**Setelah mempelajari bab ini, mahasiswa mampu:**

1. Menjelaskan *project management triangle* (scope, time, cost) dan dampak trade-off antar constraint
2. Menerapkan minimal 3 teknik estimasi (Planning Poker, T-shirt sizing, story points) untuk user stories
3. Menganalisis velocity tim dan membuat burndown/burnup chart untuk tracking sprint progress
4. Menjelaskan dan mempraktikkan 4 Scrum ceremonies secara mendalam
5. Menerapkan Kanban metrics (WIP limits, lead/cycle time) untuk optimasi flow
6. Menganalisis team dynamics menggunakan Tuckman's model dan memfasilitasi retrospective
7. Menyusun risk management matrix dan strategi mitigasi untuk proyek tim
8. Mengevaluasi project management tools (GitHub Projects, Jira) untuk kolaborasi tim

---

## Peta Konsep Bab 12

```
                    ┌──────────────────────────────────────┐
                    │  SOFTWARE PROJECT MANAGEMENT & AGILE │
                    └──────────────────┬───────────────────┘
                                       │
        ┌──────────────┬───────────────┼───────────────┬──────────────┐
        │              │               │               │              │
        ▼              ▼               ▼               ▼              ▼
  ┌───────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌───────────┐
  │ PM        │ │ Estimation │ │ Scrum      │ │ Kanban &   │ │ Team &    │
  │ Triangle  │ │ Techniques │ │ Ceremonies │ │ Metrics    │ │ Risk Mgmt │
  └─────┬─────┘ └─────┬──────┘ └─────┬──────┘ └─────┬──────┘ └─────┬─────┘
        │              │              │              │              │
  ┌─────┴─────┐  ┌─────┴──────┐ ┌────┴───────┐ ┌────┴──────┐ ┌────┴──────┐
  │Scope/Time │  │Story Points│ │Sprint Plan │ │WIP Limits │ │Tuckman's  │
  │/Cost/     │  │Planning    │ │Daily Stand │ │Lead/Cycle │ │Model      │
  │Quality    │  │Poker       │ │Review      │ │Time       │ │           │
  │WBS        │  │T-shirt     │ │Retro       │ │CFD        │ │Risk       │
  │           │  │Sizing      │ │            │ │           │ │Matrix     │
  └───────────┘  └────────────┘ └────────────┘ └───────────┘ └───────────┘
```

---

## 12.1 Project Management Fundamentals

### 12.1.1 Apa Itu Software Project Management?

**Software Project Management** adalah disiplin perencanaan, pengorganisasian, pemantauan, dan pengendalian sumber daya untuk mencapai tujuan proyek perangkat lunak dalam batasan scope, waktu, dan biaya. Berbeda dengan manajemen proyek konstruksi atau manufaktur, proyek perangkat lunak memiliki karakteristik unik:

| Karakteristik | Penjelasan | Implikasi |
|---------------|------------|-----------|
| **Intangible** | Produk tidak terlihat secara fisik | Sulit mengukur progress secara visual |
| **Malleable** | Mudah diubah (kode bisa di-edit) | Rentan scope creep |
| **Kompleksitas tinggi** | Interaksi antar komponen eksponensial | Bug muncul dari interaksi tak terduga |
| **Human-intensive** | Bergantung pada kreativitas manusia | Produktivitas bervariasi 10x antar developer |
| **Evolusi cepat** | Teknologi berubah dalam hitungan bulan | Keputusan arsitektur bisa usang |

### 12.1.2 Triple Constraint (Project Management Triangle)

Setiap proyek perangkat lunak dibatasi oleh tiga constraint utama yang saling memengaruhi, dengan kualitas (*quality*) sebagai resultan di tengahnya:

```
                      ┌─────────┐
                      │  SCOPE  │
                      │(Fitur & │
                      │ Fungsi) │
                      └────┬────┘
                          / \
                         /   \
                        /     \
                       / QUALITY\
                      /  (Mutu)  \
                     /             \
              ┌─────┴──┐      ┌────┴─────┐
              │  TIME  │──────│   COST   │
              │(Waktu) │      │ (Biaya)  │
              └────────┘      └──────────┘

  Hukum Iron Triangle:
  "Anda bisa mendapatkan 2 dari 3, tapi tidak ketiganya."
  
  Ubah satu → yang lain menyesuaikan:
  ┌─────────────────────────────────────────────────┐
  │ + Scope (tambah fitur)  → + Time ATAU + Cost    │
  │ - Time  (deadline maju) → - Scope ATAU + Cost   │
  │ - Cost  (budget dipotong) → - Scope ATAU + Time │
  └─────────────────────────────────────────────────┘
```

**Contoh di Indonesia:**

Bayangkan proyek "Sistem Informasi Akademik Universitas" (seperti SIAK UAI):

| Skenario | Scope | Time | Cost | Quality | Strategi |
|----------|-------|------|------|---------|----------|
| **Ideal** | 30 fitur, semua jurusan | 8 bulan | Rp 500 juta | Tinggi | — |
| **Budget dipotong 50%** | 15 fitur, 3 jurusan dulu | 8 bulan | Rp 250 juta | Sedang | Phased rollout |
| **Deadline dimajukan** | 20 fitur, fitur inti saja | 4 bulan | Rp 500 juta | Sedang | MVP approach |
| **Scope bertambah** | 40 fitur + mobile app | 12 bulan | Rp 800 juta | Tinggi | Negosiasi ulang |

> **Tips:** Dalam Agile, scope menjadi variable yang paling fleksibel. Time dan cost biasanya *fixed* (sprint duration dan ukuran tim tetap), sementara scope di-adjust setiap sprint berdasarkan prioritas.

### 12.1.3 Work Breakdown Structure (WBS)

WBS memecah proyek besar menjadi komponen-komponen yang lebih kecil dan terkelola (*manageable*). Setiap level menambah detail:

```
Sistem Perpustakaan UAI v1.0 (Proyek Akhir IF2205)
├── 1. Discovery & Planning (Sprint 0)
│   ├── 1.1 Stakeholder interview
│   ├── 1.2 Requirements elicitation
│   ├── 1.3 User story writing (15+ stories)
│   ├── 1.4 Product backlog creation
│   └── 1.5 Sprint planning session
├── 2. Design (Sprint 0-1)
│   ├── 2.1 UML Diagrams
│   │   ├── 2.1.1 Use Case Diagram
│   │   ├── 2.1.2 Class Diagram
│   │   ├── 2.1.3 Sequence Diagram
│   │   └── 2.1.4 Activity Diagram
│   ├── 2.2 Database Design (ERD + Normalisasi)
│   ├── 2.3 API Design (REST endpoints)
│   └── 2.4 UI/UX Wireframes
├── 3. Implementation (Sprint 1-3)
│   ├── 3.1 Backend (Flask)
│   │   ├── 3.1.1 App factory & config
│   │   ├── 3.1.2 SQLAlchemy models
│   │   ├── 3.1.3 API routes (CRUD)
│   │   ├── 3.1.4 Authentication (login/register)
│   │   └── 3.1.5 Business logic (services)
│   ├── 3.2 Frontend (HTML/CSS/JS)
│   │   ├── 3.2.1 Login & Register pages
│   │   ├── 3.2.2 Dashboard
│   │   ├── 3.2.3 Katalog & Pencarian buku
│   │   └── 3.2.4 Halaman peminjaman
│   └── 3.3 Database (SQLite + Migrations)
├── 4. Quality Assurance (Sprint 2-3)
│   ├── 4.1 Unit Tests (pytest)
│   ├── 4.2 Integration Tests
│   ├── 4.3 E2E Tests (jika waktu memungkinkan)
│   └── 4.4 Code Review
└── 5. Deployment & Delivery (Sprint 3-4)
    ├── 5.1 CI/CD Pipeline (GitHub Actions)
    ├── 5.2 Docker Setup (Dockerfile + compose)
    ├── 5.3 Cloud Deploy (Railway/Render)
    ├── 5.4 Documentation (README, API docs)
    └── 5.5 Presentasi & Demo
```

> **Best Practice:** Setiap item WBS di level terbawah (*work package*) harus bisa diestimasikan waktunya dan ditugaskan ke satu orang. Jika terlalu besar, pecahkan lagi.

### 12.1.4 Peran Kunci dalam Proyek Agile

| Peran | Tanggung Jawab | Dalam Konteks Tim Mahasiswa |
|-------|----------------|---------------------------|
| **Product Owner (PO)** | Mengelola Product Backlog, prioritas fitur, mewakili stakeholder | 1 anggota tim yang memahami kebutuhan pengguna |
| **Scrum Master (SM)** | Fasilitator proses Scrum, hapus hambatan, lindungi tim | 1 anggota tim secara bergilir per sprint |
| **Development Team** | Menulis kode, testing, deployment — self-organizing | Seluruh anggota tim (3-4 orang) |

**Contoh pembagian peran di proyek akhir IF2205:**

```python
# Contoh: Pembagian peran tim proyek akhir
tim_proyek = {
    "nama_tim": "Tim Pustaka Digital",
    "anggota": [
        {
            "nama": "Aisyah",
            "peran_utama": "Product Owner",
            "tanggung_jawab": [
                "Mengelola product backlog",
                "Menulis user stories",
                "Prioritas fitur (MoSCoW)",
                "Juga: Frontend development"
            ]
        },
        {
            "nama": "Budi",
            "peran_utama": "Scrum Master (Sprint 1-2)",
            "tanggung_jawab": [
                "Fasilitasi daily standup",
                "Tracking velocity & burndown",
                "Hapus hambatan",
                "Juga: Backend development"
            ]
        },
        {
            "nama": "Citra",
            "peran_utama": "Lead Developer",
            "tanggung_jawab": [
                "Arsitektur & database design",
                "Code review",
                "Backend API development",
                "Scrum Master (Sprint 3-4)"
            ]
        },
        {
            "nama": "Dimas",
            "peran_utama": "QA & DevOps",
            "tanggung_jawab": [
                "Testing strategy & execution",
                "CI/CD pipeline setup",
                "Docker & deployment",
                "Juga: Frontend development"
            ]
        }
    ]
}
```

---

## 12.2 Estimation Techniques

### 12.2.1 Mengapa Estimasi Penting?

Estimasi adalah fondasi perencanaan sprint. Tanpa estimasi yang baik, tim tidak bisa:
- Menentukan berapa banyak pekerjaan yang masuk dalam satu sprint
- Memprediksi kapan semua fitur selesai (release planning)
- Mengidentifikasi user stories yang terlalu besar dan perlu dipecah

> **Prinsip penting:** Estimasi adalah *perkiraan* (estimate), bukan *komitmen* (commitment). Estimasi yang tepat 100% adalah ilusi. Yang penting adalah *konsistensi relatif* — apakah story 5 poin memang ~2.5x lebih effort dari story 2 poin?

### 12.2.2 Story Points

Story points mengukur **effort relatif** — bukan jam kerja absolut. Mereka menggabungkan tiga faktor:

```
Story Points = f(Kompleksitas, Effort, Ketidakpastian)

┌─────────────────────────────────────────────────────┐
│                 STORY POINTS                         │
│                                                      │
│  Kompleksitas  ─── Seberapa rumit secara teknis?     │
│  Effort        ─── Seberapa banyak pekerjaan?        │
│  Uncertainty   ─── Seberapa banyak yang belum jelas? │
│                                                      │
│  Skala Fibonacci: 1, 2, 3, 5, 8, 13, 21             │
│                                                      │
│  Mengapa Fibonacci? Semakin besar story, semakin     │
│  tidak presisi estimasinya → gap antar angka membesar│
└─────────────────────────────────────────────────────┘
```

**Contoh kalibrasi story points untuk Sistem Perpustakaan:**

| Story Points | Contoh User Story | Alasan |
|-------------|-------------------|--------|
| **1** | "Ubah label tombol dari 'Submit' ke 'Pinjam Buku'" | Trivial, 1 file, 1 baris |
| **2** | "Tampilkan jumlah buku tersedia di halaman katalog" | Query sederhana + tampilan |
| **3** | "Tambah field 'Tahun Terbit' di form input buku" | DB migration + form + validasi |
| **5** | "Implementasi fitur pencarian buku by judul/pengarang" | API endpoint + frontend + query |
| **8** | "CRUD lengkap untuk manajemen anggota perpustakaan" | Multiple endpoints + pages + validasi |
| **13** | "Sistem peminjaman buku dengan pengecekan ketersediaan" | Business logic kompleks + state |
| **21** | "Laporan statistik peminjaman per bulan dengan chart" | Backend + frontend + chart library |

### 12.2.3 Planning Poker

Planning Poker adalah teknik estimasi kolaboratif di mana setiap anggota tim mengestimasi secara independen:

```
┌────────────────────────────────────────────────────────────┐
│                    PLANNING POKER                           │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  Langkah 1: PO membacakan user story                       │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ "Sebagai anggota, saya ingin bisa mencari buku      │   │
│  │  berdasarkan judul agar bisa menemukan buku cepat"  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Langkah 2: Diskusi singkat (2-3 menit)                    │
│  - "Perlu search endpoint di backend?"                      │
│  - "Pakai full-text search atau LIKE query?"                │
│  - "Autocomplete atau search biasa?"                        │
│                                                             │
│  Langkah 3: Semua REVEAL kartu bersamaan                   │
│  ┌───┐ ┌───┐ ┌───┐ ┌───┐                                  │
│  │ 5 │ │ 3 │ │ 5 │ │ 8 │   ← Aisyah, Budi, Citra, Dimas │
│  └───┘ └───┘ └───┘ └───┘                                  │
│                                                             │
│  Langkah 4: Diskusikan outlier                              │
│  Dimas (8): "Saya pikir perlu autocomplete + debounce"     │
│  Budi (3):  "Kalau search biasa, cuma LIKE query"          │
│  Tim sepakat: search biasa dulu → 5 points                 │
│                                                             │
│  Langkah 5: Catat: "Search buku" = 5 story points          │
└────────────────────────────────────────────────────────────┘
```

**Implementasi sederhana Planning Poker di Python:**

```python
import random

def planning_poker(story, team_members):
    """Simulasi Planning Poker session."""
    fibonacci = [1, 2, 3, 5, 8, 13, 21]
    
    print(f"\n📋 User Story: {story}")
    print("=" * 50)
    
    # Setiap anggota memilih estimasi
    estimates = {}
    for member in team_members:
        estimate = random.choice(fibonacci[:5])  # Simulasi
        estimates[member] = estimate
    
    # Reveal bersamaan
    print("\n🃏 Reveal kartu:")
    for member, est in estimates.items():
        print(f"  {member}: {est} points")
    
    # Analisis
    values = list(estimates.values())
    spread = max(values) - min(values)
    
    if spread <= 2:
        consensus = round(sum(values) / len(values))
        print(f"\n✅ Konsensus tercapai: ~{consensus} points")
    else:
        print(f"\n⚠️  Spread terlalu besar ({spread}). Diskusi ulang!")
        print(f"  Tertinggi: {max(values)} — alasan?")
        print(f"  Terendah: {min(values)} — alasan?")
    
    return estimates

# Contoh penggunaan
tim = ["Aisyah", "Budi", "Citra", "Dimas"]
stories = [
    "Halaman pencarian buku",
    "Login dan registrasi anggota",
    "Proses peminjaman buku online",
    "Dashboard admin dengan statistik"
]

for story in stories:
    planning_poker(story, tim)
```

### 12.2.4 T-Shirt Sizing

T-shirt sizing cocok untuk estimasi cepat di tahap awal (*rough estimation*) ketika detail belum jelas:

| Size | Relative Effort | Story Points (mapping) | Contoh Proyek Perpustakaan |
|------|----------------|----------------------|---------------------------|
| **XS** | Trivial, < 1 jam | 1 | Ubah warna tombol, fix typo |
| **S** | Kecil, setengah hari | 2-3 | Tambah field di form, validasi input |
| **M** | Medium, 1-2 hari | 5 | Endpoint baru dengan CRUD sederhana |
| **L** | Besar, 3-5 hari | 8 | Fitur lengkap (API + UI + tests) |
| **XL** | Sangat besar, 1+ minggu | 13+ | Modul baru, perlu dipecah! |

> **Tips:** Jika story berukuran XL atau lebih, **pecah** menjadi beberapa stories yang lebih kecil. Story yang terlalu besar sulit diestimasikan dan berisiko tidak selesai dalam 1 sprint.

### 12.2.5 Teknik Estimasi Lainnya

```
┌─────────────────────────────────────────────────────────────────────┐
│                   PERBANDINGAN TEKNIK ESTIMASI                       │
├──────────────────┬──────────────┬──────────────┬───────────────────┤
│ Teknik           │ Kapan Pakai  │ Akurasi      │ Waktu Dibutuhkan  │
├──────────────────┼──────────────┼──────────────┼───────────────────┤
│ Planning Poker   │ Sprint       │ Tinggi       │ 30-60 menit       │
│                  │ Planning     │ (konsensus)  │ untuk 10 stories  │
├──────────────────┼──────────────┼──────────────┼───────────────────┤
│ T-shirt Sizing   │ Release      │ Sedang       │ 15-30 menit       │
│                  │ Planning     │ (rough)      │ untuk 20 stories  │
├──────────────────┼──────────────┼──────────────┼───────────────────┤
│ Dot Voting       │ Prioritas,   │ Rendah-      │ 5-10 menit        │
│                  │ quick sort   │ Sedang       │                   │
├──────────────────┼──────────────┼──────────────┼───────────────────┤
│ Affinity         │ Grouping     │ Sedang       │ 20-40 menit       │
│ Mapping          │ banyak items │              │                   │
├──────────────────┼──────────────┼──────────────┼───────────────────┤
│ Three-Point      │ Estimasi     │ Tinggi       │ Lama per item     │
│ (O+M+P)/3       │ formal       │ (statistik)  │                   │
└──────────────────┴──────────────┴──────────────┴───────────────────┘
```

---

## 12.3 Velocity dan Sprint Tracking

### 12.3.1 Velocity

**Velocity** adalah jumlah story points yang berhasil diselesaikan (DONE) dalam satu sprint. Velocity hanya menghitung story yang sepenuhnya *done* — sesuai Definition of Done (DoD).

```python
# Contoh tracking velocity
sprints = {
    "Sprint 1": {"planned": 20, "completed": 15, "carried_over": 5},
    "Sprint 2": {"planned": 18, "completed": 19, "carried_over": 0},
    "Sprint 3": {"planned": 20, "completed": 21, "carried_over": 0},
    "Sprint 4": {"planned": 20, "completed": 20, "carried_over": 0},
}

velocities = [s["completed"] for s in sprints.values()]
avg_velocity = sum(velocities) / len(velocities)

print("Velocity per Sprint:")
for name, data in sprints.items():
    status = "✅" if data["completed"] >= data["planned"] else "⚠️"
    print(f"  {name}: {data['completed']} pts {status}")

print(f"\nAverage Velocity: {avg_velocity:.1f} pts/sprint")
print(f"Range: {min(velocities)}-{max(velocities)} pts")

# Prediksi: sisa backlog 40 pts
remaining = 40
sprints_needed = remaining / avg_velocity
print(f"\nSisa backlog: {remaining} pts")
print(f"Estimasi selesai: {sprints_needed:.1f} sprint lagi")
```

Output:
```
Velocity per Sprint:
  Sprint 1: 15 pts ⚠️
  Sprint 2: 19 pts ✅
  Sprint 3: 21 pts ✅
  Sprint 4: 20 pts ✅

Average Velocity: 18.8 pts/sprint
Range: 15-21 pts

Sisa backlog: 40 pts
Estimasi selesai: 2.1 sprint lagi
```

### 12.3.2 Burndown Chart

Burndown chart menunjukkan sisa pekerjaan vs waktu dalam satu sprint:

```
Story Points Remaining
  25 │●
     │ ╲  ← Ideal Line (garis lurus)
  20 │  ╲.....●
     │   ╲     ╲
  15 │    ╲     ●───● ← Stagnasi (hari 4-5: tidak ada story selesai)
     │     ╲         ╲
  10 │      ╲         ●
     │       ╲         ╲
   5 │        ╲         ●
     │         ╲       ╱  ← Scope ditambah!
   3 │          ╲     ●
     │           ╲   ╱
   0 │────────────╲─●────────────
     Day 1  2  3  4  5  6  7  8  9  10
     
  Interpretasi:
  ● ─── Actual progress
  ╲ ─── Ideal burndown
  
  Hari 4-5: Flat line = tidak ada progress (blocked?)
  Hari 7:   Garis naik = scope ditambah mid-sprint (red flag!)
  Hari 10:  Masih sisa 3 pts = tidak semua selesai
```

### 12.3.3 Burnup Chart

Burnup chart menunjukkan pekerjaan yang sudah selesai dan total scope — lebih informatif ketika scope berubah:

```
Story Points
  30 │                          ........● ← Total Scope (naik!)
     │                    ......          
  25 │              ●─────●               ← Scope awal = 25 pts
     │             ╱                      
  20 │           ●╱         ● ← Work Completed
     │          ╱          ╱
  15 │        ●           ╱
     │       ╱          ╱
  10 │     ●          ╱
     │    ╱         ╱
   5 │  ●         ╱
     │ ╱        ╱
   0 │●──────────────────────────────────
     Day 1  2  3  4  5  6  7  8  9  10
     
  Keunggulan burnup vs burndown:
  - Terlihat jelas ketika scope bertambah (garis atas naik)
  - Gap antara scope dan completed = sisa pekerjaan
  - Lebih mudah memprediksi kapan selesai
```

### 12.3.4 Cumulative Flow Diagram (CFD)

CFD menunjukkan distribusi pekerjaan di setiap status seiring waktu:

```
Items
  30 │████████████████████████████████████
     │████████████████████████████ Done ██
  25 │█████████████████████████████████
     │███████████████████████████████
  20 │░░░░░░░░░░░░░░░░░░░████████████
     │░░░░░░░░░░░░░░░░░░░ In Progress░
  15 │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
     │▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░
  10 │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     │▒▒▒▒▒▒▒▒▒▒▒▒▒ To Do ▒▒▒▒▒▒▒▒
   5 │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
   0 │──────────────────────────────────
     Day 1    3    5    7    9    10

  ▒ = To Do    ░ = In Progress    █ = Done
  
  Lebar band "In Progress" = WIP (Work in Progress)
  - Band WIP terlalu lebar → terlalu banyak pekerjaan paralel
  - Band WIP stabil dan tipis → flow yang sehat
```

---

## 12.4 Scrum Ceremonies Deep Dive

### 12.4.1 Sprint Planning

Sprint Planning adalah ceremony untuk menentukan **apa** yang akan dikerjakan dan **bagaimana** mengerjakannya.

```
┌─────────────────────────────────────────────────────────────┐
│                     SPRINT PLANNING                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Durasi: Max 2 jam untuk sprint 2 minggu                     │
│  Peserta: PO + SM + Dev Team                                 │
│                                                              │
│  PART 1: WHAT (60 menit)                                     │
│  ┌────────────────────────────────────────────────────┐      │
│  │ 1. PO presentasi Sprint Goal                       │      │
│  │ 2. PO jelaskan top-priority Product Backlog items   │      │
│  │ 3. Tim tanya jawab: acceptance criteria, edge cases │      │
│  │ 4. Tim estimasi dan select items → Sprint Backlog   │      │
│  │    (berdasarkan velocity sprint sebelumnya)          │      │
│  └────────────────────────────────────────────────────┘      │
│                                                              │
│  PART 2: HOW (60 menit)                                      │
│  ┌────────────────────────────────────────────────────┐      │
│  │ 1. Breakdown setiap story → technical tasks          │      │
│  │ 2. Identifikasi dependencies antar task              │      │
│  │ 3. Tim members volunteer untuk tasks                 │      │
│  │ 4. Estimasi tasks (jam/hari)                         │      │
│  │ 5. Update Sprint Board                               │      │
│  └────────────────────────────────────────────────────┘      │
│                                                              │
│  OUTPUT:                                                     │
│  ✅ Sprint Goal yang jelas                                   │
│  ✅ Sprint Backlog (stories + tasks)                         │
│  ✅ Komitmen tim terhadap Sprint Goal                        │
└─────────────────────────────────────────────────────────────┘
```

**Contoh Sprint Backlog:**

```
Sprint 2 Goal: "Anggota bisa mencari dan meminjam buku online"

Sprint Backlog:
┌──────┬───────────────────────────────────┬────────┬──────────┐
│ ID   │ User Story                        │ Points │ Assignee │
├──────┼───────────────────────────────────┼────────┼──────────┤
│ US-7 │ Pencarian buku by judul/pengarang │ 5      │ Citra    │
│ US-8 │ Detail buku & ketersediaan        │ 3      │ Dimas    │
│ US-9 │ Proses peminjaman buku            │ 8      │ Budi     │
│ US-10│ Notifikasi peminjaman berhasil    │ 3      │ Aisyah   │
├──────┼───────────────────────────────────┼────────┼──────────┤
│      │ TOTAL                             │ 19     │          │
│      │ Velocity Sprint 1                 │ 15     │          │
│      │ Target: stretch +4 pts            │        │          │
└──────┴───────────────────────────────────┴────────┴──────────┘
```

### 12.4.2 Daily Standup (Daily Scrum)

Daily Standup adalah meeting singkat (maks 15 menit) setiap hari kerja untuk sinkronisasi tim:

```
┌──────────────────────────────────────────────────────┐
│              DAILY STANDUP FORMAT                      │
│                                                       │
│  Setiap anggota menjawab 3 pertanyaan:                │
│                                                       │
│  1. Kemarin saya mengerjakan apa?                     │
│  2. Hari ini saya akan mengerjakan apa?               │
│  3. Apakah ada hambatan (blocker)?                    │
│                                                       │
│  ⏱️  Maks 2 menit per orang                           │
│  📍 Di depan Sprint Board (fisik/digital)             │
│  🚫 BUKAN meeting untuk diskusi detail                │
│     (diskusi lanjutan setelah standup selesai)         │
└──────────────────────────────────────────────────────┘
```

**Contoh Daily Standup di tim mahasiswa (via WhatsApp/Discord):**

```
# Daily Standup - Rabu, 2 April 2026

## Budi:
- Kemarin: Selesai API endpoint POST /api/peminjaman
- Hari ini: Integrasi dengan frontend form peminjaman
- Blocker: Belum ada endpoint GET /api/buku/:id dari Citra

## Citra:
- Kemarin: Selesai search endpoint GET /api/buku?q=keyword
- Hari ini: Buat GET /api/buku/:id (detail + ketersediaan)
  → Unblock Budi siang ini
- Blocker: Tidak ada

## Aisyah:
- Kemarin: Wireframe halaman peminjaman (Figma)
- Hari ini: Implement halaman pencarian buku (HTML/CSS/JS)
- Blocker: Perlu contoh response JSON dari search API

## Dimas:
- Kemarin: Setup pytest fixtures & test database
- Hari ini: Tulis unit tests untuk model Buku & Peminjaman
- Blocker: Tidak ada
```

### 12.4.3 Sprint Review

Sprint Review dilakukan di akhir sprint untuk mendemonstrasikan hasil kerja kepada stakeholder:

```
┌──────────────────────────────────────────────────────┐
│               SPRINT REVIEW                           │
│                                                       │
│  Durasi: 1-2 jam (sprint 2 minggu)                    │
│  Peserta: PO + SM + Dev Team + Stakeholders           │
│                                                       │
│  Agenda:                                              │
│  1. PO recap Sprint Goal                              │
│  2. Tim DEMO fitur yang sudah selesai                 │
│     - Working software, bukan slides!                 │
│     - Demo di environment yang mendekati production   │
│  3. Stakeholder memberikan feedback                   │
│  4. PO update Product Backlog berdasarkan feedback    │
│  5. Diskusi prioritas untuk sprint berikutnya         │
│                                                       │
│  OUTPUT:                                              │
│  ✅ Increment yang sudah di-demo                      │
│  ✅ Feedback stakeholder tercatat                     │
│  ✅ Product Backlog updated                           │
└──────────────────────────────────────────────────────┘
```

**Dalam konteks proyek akhir IF2205:** Sprint Review dilakukan di hadapan dosen dan/atau tim lain. Setiap tim mendemonstrasikan fitur yang sudah berjalan — bukan presentasi PowerPoint, tapi **live demo**.

### 12.4.4 Sprint Retrospective

Retrospective adalah waktu bagi tim untuk refleksi dan perbaikan proses:

```
┌──────────────────────────────────────────────────────┐
│            SPRINT RETROSPECTIVE                       │
│                                                       │
│  Durasi: 45-90 menit                                  │
│  Peserta: SM + Dev Team (PO opsional)                 │
│  Fasilitator: Scrum Master                            │
│                                                       │
│  Prinsip: Safe space — tidak ada blame                │
│                                                       │
│  Format populer:                                      │
│  ┌─────────────────────────────────────────────┐      │
│  │ 1. Start-Stop-Continue                       │      │
│  │ 2. Mad-Sad-Glad                              │      │
│  │ 3. 4Ls: Liked-Learned-Lacked-Longed for      │      │
│  │ 4. Sailboat (wind=good, anchor=bad, rock=risk)│     │
│  └─────────────────────────────────────────────┘      │
│                                                       │
│  OUTPUT: 2-3 action items untuk sprint berikutnya     │
└──────────────────────────────────────────────────────┘
```

**Contoh Retrospective Sprint 2 — Tim Pustaka Digital:**

```
Format: Start-Stop-Continue

🟢 START (mulai lakukan):
  - Code review setiap PR sebelum merge (minimal 1 reviewer)
  - Unit test untuk setiap endpoint baru
  - Estimasi task dalam jam, bukan hanya story points

🔴 STOP (berhenti lakukan):
  - Push langsung ke branch main tanpa PR
  - Skip daily standup karena "tidak ada update"
  - Coding tanpa acceptance criteria yang jelas

🔵 CONTINUE (lanjutkan):
  - Daily standup di Discord jam 8 pagi
  - Pair programming untuk fitur yang kompleks
  - Menggunakan AI (Claude Code) untuk boilerplate code

ACTION ITEMS untuk Sprint 3:
  1. Setup branch protection rule di GitHub (Dimas)
  2. Buat template PR dengan checklist (Citra)
  3. Tambahkan test requirement di Definition of Done (Budi)
```

---

## 12.5 Kanban Metrics

### 12.5.1 WIP Limits (Work in Progress Limits)

WIP limits membatasi jumlah item yang boleh "In Progress" secara bersamaan. Ini mencegah multitasking berlebihan dan meningkatkan focus:

```
Kanban Board dengan WIP Limits:

┌─────────────┬──────────────────┬───────────────┬────────────┐
│  TO DO      │  IN PROGRESS     │  IN REVIEW    │   DONE     │
│  (no limit) │  (WIP: 4)        │  (WIP: 2)     │ (no limit) │
├─────────────┼──────────────────┼───────────────┼────────────┤
│ ▪ US-15     │ ▪ US-11 (Budi)   │ ▪ US-9 (Budi) │ ▪ US-7     │
│ ▪ US-16     │ ▪ US-12 (Citra)  │ ▪ US-10(Citra)│ ▪ US-8     │
│ ▪ US-17     │ ▪ US-13 (Aisyah) │               │ ▪ US-6     │
│ ▪ US-18     │ ▪ US-14 (Dimas)  │  ← Ada slot   │ ▪ US-5     │
│ ▪ US-19     │                  │    kosong!     │ ▪ US-4     │
│             │ ← PENUH! (4/4)   │    (1/2)       │            │
│             │   Harus selesai-  │               │            │
│             │   kan dulu sebelum│               │            │
│             │   ambil yang baru │               │            │
└─────────────┴──────────────────┴───────────────┴────────────┘

  Mengapa WIP limits penting?
  - Mengurangi context switching
  - Meningkatkan flow dan throughput
  - Membantu identifikasi bottleneck
  - Mendorong kolaborasi (saling bantu selesaikan)
```

### 12.5.2 Lead Time vs Cycle Time

```
                 ┌──── Lead Time ────────────────────────────────┐
                 │                                                │
  Customer       │  ┌──── Cycle Time ──────────────┐             │
  Request ───────┼──┤                               ├──── Done ──┤
                 │  │  In Progress → In Review      │             │
  (masuk backlog)│  │  → Testing → Deploy            │(delivered) │
                 │  └───────────────────────────────┘             │
                 │                                                │
                 └── (termasuk waktu menunggu di backlog) ────────┘

  Lead Time  = waktu dari request masuk sampai delivered
  Cycle Time = waktu dari mulai dikerjakan sampai selesai
  
  Contoh:
  - User story masuk backlog: 1 Maret
  - Mulai dikerjakan: 8 Maret  
  - Selesai (done): 12 Maret
  
  Lead Time  = 12 - 1 = 11 hari
  Cycle Time = 12 - 8 = 4 hari
  Wait Time  = 8 - 1 = 7 hari (menunggu di backlog)
```

**Tracking metrics dengan Python:**

```python
from datetime import datetime, timedelta

# Data story completion
stories = [
    {"id": "US-7",  "requested": "2026-03-01", "started": "2026-03-05", "done": "2026-03-07"},
    {"id": "US-8",  "requested": "2026-03-01", "started": "2026-03-07", "done": "2026-03-08"},
    {"id": "US-9",  "requested": "2026-03-02", "started": "2026-03-08", "done": "2026-03-12"},
    {"id": "US-10", "requested": "2026-03-03", "started": "2026-03-10", "done": "2026-03-11"},
    {"id": "US-11", "requested": "2026-03-05", "started": "2026-03-12", "done": "2026-03-14"},
]

def parse_date(s):
    return datetime.strptime(s, "%Y-%m-%d")

print("Kanban Metrics:")
print(f"{'Story':<8} {'Lead Time':>10} {'Cycle Time':>11} {'Wait Time':>10}")
print("-" * 45)

lead_times = []
cycle_times = []

for s in stories:
    req = parse_date(s["requested"])
    start = parse_date(s["started"])
    done = parse_date(s["done"])
    
    lead = (done - req).days
    cycle = (done - start).days
    wait = (start - req).days
    
    lead_times.append(lead)
    cycle_times.append(cycle)
    
    print(f"{s['id']:<8} {lead:>8} hr {cycle:>9} hr {wait:>8} hr")

print("-" * 45)
print(f"{'Average':<8} {sum(lead_times)/len(lead_times):>8.1f} hr "
      f"{sum(cycle_times)/len(cycle_times):>9.1f} hr")
```

### 12.5.3 Throughput

**Throughput** = jumlah item yang selesai per satuan waktu. Berbeda dengan velocity (yang berbasis story points), throughput menghitung jumlah *items*.

```
Throughput per Minggu:
Minggu 1: ████████ 8 items
Minggu 2: ██████████ 10 items
Minggu 3: ████████████ 12 items
Minggu 4: ██████████ 10 items

Average Throughput: 10 items/minggu
Sisa backlog: 25 items
Estimasi selesai: 2.5 minggu
```

---

## 12.6 Team Dynamics dan Komunikasi

### 12.6.1 Tuckman's Model

Bruce Tuckman (1965) mendeskripsikan 4 tahap perkembangan tim (ditambah tahap ke-5 oleh Tuckman & Jensen, 1977):

```
Performance
     │
High │                              ●─────── Performing
     │                           ╱ ╱
     │                         ●╱   Norming
     │                       ╱
     │                    ╱
Mid  │            ●─────●   ← Storming (bisa lama!)
     │          ╱
     │        ╱
Low  │  ●───●   Forming
     │
     └──────────────────────────────────── Waktu
           W1   W3   W5   W7   W9   W11
```

| Tahap | Ciri-ciri | Yang Terjadi di Tim Mahasiswa | Tips untuk SM |
|-------|-----------|------------------------------|---------------|
| **Forming** | Sopan, hati-hati, optimis | Perkenalan, bagi peran, setup repo | Atur ekspektasi, buat team agreement |
| **Storming** | Konflik, frustrasi, ego | "Kok kamu push langsung ke main?", perbedaan gaya coding | Fasilitasi dialog, coding standards |
| **Norming** | Aturan terbentuk, kepercayaan tumbuh | PR review jalan, coding standards dipatuhi | Pertahankan momentum, jaga konsistensi |
| **Performing** | Produktif, kolaboratif, saling bantu | Tim flow, pair programming natural, saling backup | Berikan tantangan, celebrate wins |
| **Adjourning** | Proyek selesai, refleksi | Sprint terakhir, retrospective final, presentasi | Retrospective menyeluruh, apresiasi |

**Contoh Team Agreement (kontrak tim):**

```python
# Team Agreement — Tim Pustaka Digital
team_agreement = {
    "komunikasi": {
        "channel_utama": "Discord (text + voice)",
        "response_time": "Maks 4 jam pada hari kerja",
        "daily_standup": "Discord voice, setiap hari jam 08:00, maks 15 menit"
    },
    "git_workflow": {
        "branching": "feature/nama-fitur dari branch develop",
        "commit_message": "Conventional commits (feat:, fix:, docs:, test:)",
        "pull_request": "Minimal 1 reviewer, harus passing CI",
        "merge_strategy": "Squash merge ke develop, merge ke main saat release"
    },
    "coding_standards": {
        "backend": "PEP 8 (enforced by flake8)",
        "frontend": "ESLint + Prettier",
        "testing": "Minimal 1 test per endpoint baru"
    },
    "scrum": {
        "sprint_duration": "2 minggu",
        "sprint_planning": "Senin minggu 1, 60 menit",
        "sprint_review": "Jumat minggu 2, 30 menit",
        "retrospective": "Jumat minggu 2, setelah review, 30 menit"
    },
    "konflik": {
        "prinsip": "Diskusi terbuka, fokus pada masalah bukan orangnya",
        "eskalasi": "Jika tidak bisa diselesaikan → minta bantuan dosen"
    }
}
```

### 12.6.2 Komunikasi Tim Terdistribusi

Di era remote/hybrid, komunikasi dalam tim yang tersebar secara geografis memerlukan strategi khusus:

| Tantangan | Solusi | Tools |
|-----------|--------|-------|
| **Timezone berbeda** | Overlap hours, async standup | Discord, Slack |
| **Miskomunikasi teks** | Video call untuk diskusi kompleks | Google Meet, Zoom |
| **Knowledge silos** | Dokumentasi di README, wiki | GitHub Wiki, Notion |
| **Kurang visibility** | Sprint board selalu updated | GitHub Projects, Trello |
| **Social isolation** | Virtual coffee, ice breakers | Discord voice channel |

**Contoh di Gojek/GoTo Engineering:**

GoTo Engineering mengelola ratusan tim yang tersebar di Jakarta, Bangalore, Singapore, dan kota lainnya. Praktik mereka:
- **Asynchronous standup** via Slack bots (karena timezone berbeda)
- **RFC (Request for Comments)** document untuk keputusan arsitektur besar
- **Confluence wiki** sebagai single source of truth untuk dokumentasi
- **Sprint demo** via video call dengan recording untuk yang tidak bisa hadir
- **Quarterly planning** secara tatap muka (hybrid) untuk alignment

---

## 12.7 Risk Management

### 12.7.1 Risk Management Matrix

Setiap proyek memiliki risiko. Manajemen risiko yang baik berarti **mengidentifikasi risiko sebelum terjadi** dan menyiapkan strategi respons.

```
Risk Matrix:

              I M P A C T
              Low        Medium      High
         ┌──────────┬──────────┬──────────┐
  High   │ MONITOR  │ MITIGATE │ ⚠ URGENT │
P        │ (kuning) │ (oranye) │ (merah)  │
r        ├──────────┼──────────┼──────────┤
o Medium │ ACCEPT   │ MONITOR  │ MITIGATE │
b        │ (hijau)  │ (kuning) │ (oranye) │
         ├──────────┼──────────┼──────────┤
  Low    │ ACCEPT   │ ACCEPT   │ MONITOR  │
         │ (hijau)  │ (hijau)  │ (kuning) │
         └──────────┴──────────┴──────────┘
         
  Strategi Response:
  ┌──────────┬─────────────────────────────────────┐
  │ ACCEPT   │ Terima risiko, tidak ada aksi khusus │
  │ MONITOR  │ Pantau secara berkala                 │
  │ MITIGATE │ Kurangi probability atau impact       │
  │ URGENT   │ Tangani SEGERA, rencana kontingensi   │
  └──────────┴─────────────────────────────────────┘
```

### 12.7.2 Risk Register untuk Proyek Mahasiswa

| # | Risiko | Prob. | Impact | Skor | Strategi | Mitigasi |
|---|--------|-------|--------|------|----------|----------|
| R1 | Anggota tim drop atau tidak aktif | Medium | High | MITIGATE | Cross-training, dokumentasi kode | Pair programming agar semua paham semua modul |
| R2 | Scope creep (fitur terus bertambah) | High | Medium | MITIGATE | MoSCoW prioritization, sprint boundary | PO tegas menolak fitur di luar sprint backlog |
| R3 | Teknologi baru gagal/terlalu sulit | Low | High | MONITOR | Prototyping awal di Sprint 0 | Siapkan fallback ke teknologi yang dikuasai |
| R4 | Merge conflict parah | Medium | Medium | MONITOR | Branching strategy, PR kecil | Merge ke develop sering, hindari long-lived branches |
| R5 | Deadline bersamaan tugas MK lain | High | Medium | MITIGATE | Timeline buffer, prioritas | Komunikasi awal, bagi pekerjaan merata per minggu |
| R6 | Server/hosting down saat demo | Low | High | MONITOR | Backup lokal | Siapkan video recording demo sebagai backup |
| R7 | Data hilang (tidak ada backup) | Low | High | MONITOR | Git sebagai backup | Push ke remote setiap hari, jangan hanya commit lokal |

---

## 12.8 Project Management Tools

### 12.8.1 GitHub Projects

GitHub Projects terintegrasi langsung dengan repository dan ideal untuk tim mahasiswa:

```
GitHub Projects Board:

┌─────────────────────────────────────────────────────┐
│  🏗️ Sprint 2 Board — Tim Pustaka Digital             │
├──────────────┬──────────────┬──────────────┬────────┤
│ 📋 Backlog   │ 🔄 In Progress│ 👀 In Review │ ✅ Done │
├──────────────┼──────────────┼──────────────┼────────┤
│ #15 Laporan  │ #11 Search   │ #9 Pinjam   │ #7 CRUD│
│     pinjaman │     buku     │    buku     │   buku │
│              │     [Citra]  │    [Budi]   │        │
│ #16 Notif    │              │             │ #8 Auth│
│     overdue  │ #12 Detail   │             │        │
│              │     buku     │             │ #6 Home│
│ #17 Profil   │     [Dimas]  │             │   page │
│     anggota  │              │             │        │
│              │ #13 Form     │             │        │
│              │     pinjam   │             │        │
│              │     [Aisyah] │             │        │
└──────────────┴──────────────┴──────────────┴────────┘

Fitur GitHub Projects yang berguna:
- Automasi: issue otomatis pindah kolom saat PR di-merge
- Custom fields: story points, sprint, priority
- Views: Board, Table, Roadmap
- Gratis untuk repository publik dan privat
```

### 12.8.2 Perbandingan Tools

| Fitur | GitHub Projects | Jira | Trello | Linear |
|-------|----------------|------|--------|--------|
| **Harga** | Gratis | Gratis (10 user) | Gratis (limited) | Gratis (250 issues) |
| **Integrasi Git** | Native | Plugin | Plugin | Native |
| **Sprint Board** | Ya | Ya (lengkap) | Manual | Ya |
| **Burndown Chart** | Custom | Built-in | Plugin | Built-in |
| **Velocity Tracking** | Custom | Built-in | Tidak ada | Built-in |
| **Kompleksitas** | Sedang | Tinggi | Rendah | Sedang |
| **Cocok untuk** | Tim kecil, open source | Enterprise, tim besar | Kanban sederhana | Startup, tim medium |
| **Rekomendasi IF2205** | **Ya** | Opsional | Boleh | Boleh |

> **Rekomendasi untuk proyek akhir IF2205:** Gunakan **GitHub Projects** karena sudah terintegrasi dengan repository, issues, dan pull requests. Tidak perlu tools tambahan.

---

## Studi Kasus Komprehensif: Manajemen Proyek di Gojek Engineering

**Konteks:** Gojek (sekarang GoTo) adalah salah satu perusahaan teknologi terbesar di Indonesia. Pada tahun 2019, Gojek mengelola 20+ produk (GoRide, GoFood, GoPay, dll.) dengan ratusan tim engineering di 4 negara.

**Tantangan Project Management:**
1. Ratusan microservices yang saling terhubung
2. Tim tersebar di Jakarta, Bangalore, Singapore, Thailand
3. Setiap tim harus bisa deploy secara independen
4. Skalabilitas: dari 20 engineer (2015) ke 1000+ (2019)

**Solusi yang Diterapkan:**

| Aspek | Praktik | Alat |
|-------|---------|------|
| **Metodologi** | Scrum di level tim, SAFe (Scaled Agile) di level organisasi | Jira + Confluence |
| **Sprint** | 2 minggu, synchronized across teams | Sprint board per tim |
| **Estimasi** | Story points dengan Planning Poker | Jira estimation |
| **Komunikasi** | Async-first, RFC documents untuk keputusan besar | Slack + Google Docs |
| **Risk Management** | Blameless post-mortem setelah incidents | PagerDuty + Opsgenie |
| **Metrics** | Velocity, lead time, deployment frequency | Grafana dashboard |

**Pelajaran untuk Tim Mahasiswa:**
1. **Start small, iterate.** Gojek dimulai sebagai monolith sebelum pindah ke microservices.
2. **Dokumentasi adalah investasi.** RFC documents menghemat banyak meeting.
3. **Retrospective tanpa blame.** Post-mortem fokus pada *apa yang terjadi* bukan *siapa yang salah*.
4. **Tools mengikuti proses, bukan sebaliknya.** Pilih tools sederhana dulu (GitHub Projects), baru upgrade jika perlu.

---

## AI Corner: AI untuk Project Management (Level: Advanced/Expert)

### 1. AI untuk Sprint Planning

```
Prompt:
"Saya adalah Scrum Master tim 4 mahasiswa yang membangun 
Sistem Perpustakaan Online dengan Flask + SQLite. Sprint 
duration 2 minggu. Average velocity 18 story points.

Product Backlog items untuk sprint berikutnya:
- Fitur pencarian buku (search by judul, pengarang, ISBN)
- Halaman detail buku dengan ketersediaan
- Proses peminjaman online
- Notifikasi email peminjaman berhasil
- Laporan peminjaman per anggota
- Profil anggota (edit data diri)

Bantu saya:
1. Estimasi story points untuk setiap item
2. Rekomendasikan Sprint Backlog (sesuai velocity 18)
3. Identifikasi dependencies antar item
4. Suggest Sprint Goal"
```

### 2. AI untuk Risk Analysis

```
Prompt:
"Analisis risiko untuk proyek web app tim 4 mahasiswa semester 4 
dengan deadline 10 minggu. Tech stack: Flask, SQLite, vanilla JS, 
Docker, GitHub Actions.

Kondisi tim:
- 2 anggota berpengalaman Python, 2 pemula
- Semua baru pertama kali pakai Docker
- Ada 2 mata kuliah berat lain semester ini
- Repository di GitHub Codespaces

Buatkan Risk Register dengan format:
| Risiko | Probability | Impact | Strategi | Mitigasi Detail |

Minimal 8 risiko yang realistis untuk konteks ini."
```

### 3. AI untuk Retrospective Facilitation

```
Prompt:
"Saya SM yang akan memfasilitasi retrospective Sprint 2. 
Data sprint:
- Velocity: 14/18 target (4 story points carry over)
- 2 dari 6 stories tidak selesai 
- 3 bugs ditemukan saat sprint review
- 1 anggota tim sering telat daily standup
- CI pipeline gagal 5 kali karena test flaky

Buatkan:
1. Agenda retrospective 45 menit
2. Pertanyaan pemantik untuk setiap bagian
3. Template action items yang SMART"
```

### 4. AI untuk Velocity Prediction

```
Prompt:
"Data velocity tim 4 sprint terakhir: 12, 16, 18, 15.
Sisa Product Backlog: 45 story points.
Deadline: 3 sprint lagi.

Analisis:
1. Apakah deadline realistis?
2. Berapa confidence level-nya?
3. Jika tidak cukup, apa rekomendasinya?
4. Buat burnup chart projection (ASCII)"
```

### 5. AI untuk Team Conflict Resolution

```
Prompt:
"Dalam tim proyek software 4 orang, terjadi konflik: 
- Anggota A merasa kontribusinya lebih besar (15 commits vs 5)
- Anggota B berpendapat bahwa commit count bukan ukuran kontribusi
- Git log menunjukkan A banyak commit kecil, B lebih sedikit tapi 
  commit besar (arsitektur, testing)

Sebagai Scrum Master, bagaimana saya:
1. Memfasilitasi diskusi yang konstruktif?
2. Menentukan metrik kontribusi yang fair?
3. Menerapkan prinsip amanah dan keadilan Islam dalam konteks ini?"
```

> **Catatan Penting:** AI sangat berguna untuk brainstorming dan template, tetapi keputusan project management tetap harus melibatkan seluruh tim. Jangan gunakan AI untuk menggantikan diskusi tim yang sebenarnya.

---

## Latihan Soal

### Level Dasar (C1-C2)

1. Jelaskan *triple constraint* (scope, time, cost) dalam project management dan berikan contoh trade-off dari masing-masing.
2. Apa yang dimaksud dengan *velocity* dalam Scrum? Bagaimana cara mengukurnya?
3. Sebutkan dan jelaskan 4 tahap Tuckman's team development model.
4. Apa perbedaan antara *burndown chart* dan *burnup chart*? Kapan masing-masing lebih berguna?
5. Jelaskan perbedaan *lead time* dan *cycle time* dalam Kanban.

### Level Menengah (C3-C4)

6. Buatlah WBS (Work Breakdown Structure) untuk proyek "Sistem Antrian Puskesmas Online" dengan minimal 4 level dan 20 work packages.
7. Lakukan simulasi Planning Poker untuk 5 user stories berikut dan jelaskan alasan estimasi Anda:
   - "Sebagai pasien, saya ingin mendaftar antrian online"
   - "Sebagai petugas, saya ingin melihat daftar antrian hari ini"
   - "Sebagai dokter, saya ingin melihat riwayat pasien"
   - "Sebagai admin, saya ingin mengelola jadwal dokter"
   - "Sebagai pasien, saya ingin menerima notifikasi giliran"
8. Buatlah risk register dengan 6 risiko untuk proyek tim Anda, lengkap dengan probability, impact, skor, dan mitigasi detail.
9. Analisis burndown chart berikut: Sprint 2 minggu (10 hari kerja), total 20 story points. Data harian: 20, 18, 18, 16, 14, 14, 14, 12, 10, 8. Apa yang terjadi di hari 2-3 dan hari 5-7? Apa action item yang Anda sarankan?
10. Bandingkan penggunaan GitHub Projects vs Jira untuk proyek tim mahasiswa 4 orang. Berikan minimal 3 alasan rekomendasi Anda.

### Level Mahir (C5-C6)

11. Evaluasi sprint performance tim berikut dan berikan rekomendasi perbaikan:
    - Sprint 1: Planned 25 pts, Completed 12 pts (48%)
    - Sprint 2: Planned 20 pts, Completed 15 pts (75%)
    - Sprint 3: Planned 18 pts, Completed 19 pts (106%)
    - Sprint 4: Planned 18 pts, Completed 16 pts (89%)
12. Rancang *sprint retrospective process* yang efektif untuk tim 4 mahasiswa yang baru pertama kali menggunakan Scrum. Sertakan: format, agenda, pertanyaan pemantik, dan template action items.
13. Anda adalah Project Manager startup Indonesia yang membangun aplikasi e-commerce dengan tim 15 engineer. Saat ini sprint velocity menurun 3 sprint berturut-turut (40, 35, 28). Analisis kemungkinan penyebab dan rancang rencana pemulihan.
14. Desain Kanban board lengkap untuk proyek tim Anda: kolom, WIP limits per kolom, Definition of Done per transisi, dan metrik yang akan di-track. Jelaskan alasan setiap keputusan desain.
15. Refleksi: Bagaimana prinsip *amanah* (kepercayaan) dan *syura* (musyawarah) dalam Islam relevan dengan praktik Agile/Scrum? Berikan minimal 3 koneksi spesifik.

---

## Rangkuman

1. **Project Management Triangle** (scope, time, cost) mengharuskan trade-off — dalam Agile, scope biasanya menjadi variable yang fleksibel sementara time dan cost tetap.
2. **Estimation techniques** (Planning Poker, T-shirt sizing, story points) mengukur effort relatif, bukan jam absolut. Konsistensi lebih penting dari presisi.
3. **Velocity** mengukur kapasitas tim per sprint dan menjadi dasar prediksi. Butuh 2-3 sprint untuk stabil.
4. **Burndown/burnup charts** dan **CFD** memberikan visibilitas terhadap progress sprint dan mengidentifikasi masalah lebih awal.
5. **Scrum ceremonies** (Sprint Planning, Daily Standup, Sprint Review, Retrospective) masing-masing memiliki tujuan spesifik dan harus dilaksanakan secara disiplin.
6. **Kanban metrics** (WIP limits, lead time, cycle time, throughput) mengoptimasi flow pekerjaan dan mengidentifikasi bottleneck.
7. **Tuckman's model** (Forming → Storming → Norming → Performing) mengingatkan bahwa konflik tim adalah bagian alami dari pembentukan tim — kuncinya adalah fasilitasi yang baik.
8. **Risk management** yang proaktif (identifikasi, analisis, mitigasi) jauh lebih baik daripada reaktif (firefighting).
9. **Project management tools** (GitHub Projects, Jira) harus mengikuti proses, bukan sebaliknya — pilih yang sesuai dengan kebutuhan dan ukuran tim.
10. **Komunikasi** adalah kunci kesuksesan proyek — baik dalam tim yang co-located maupun distributed.

---

## Referensi

1. Schwaber, K. & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org.
2. Cohn, M. (2005). *Agile Estimating and Planning*. Prentice Hall.
3. Stellman, A. & Greene, J. (2014). *Learning Agile*. O'Reilly Media.
4. Rubin, K. S. (2012). *Essential Scrum: A Practical Guide to the Most Popular Agile Process*. Addison-Wesley.
5. Anderson, D. J. (2010). *Kanban: Successful Evolutionary Change for Your Technology Business*. Blue Hole Press.
6. Tuckman, B. W. (1965). "Developmental Sequence in Small Groups." *Psychological Bulletin*, 63(6), 384-399.
7. Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson. Chapter 22-23.
8. GoTo Engineering Blog. (2023). "How We Scale Engineering at GoTo." engineering.grab.com.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
