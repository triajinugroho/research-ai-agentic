# Minggu 2: Proses dan Model Pengembangan Perangkat Lunak

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 2 dari 16 |
| **Topik** | Proses dan Model Pengembangan Perangkat Lunak |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK-1 |
| **Sub-CPMK** | 1.3 (Membedakan model proses), 1.4 (Menjelaskan Scrum & Agile) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Ceramah interaktif, simulasi Scrum mini, studi kasus |

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menjelaskan** 4 aktivitas fundamental dalam proses perangkat lunak (C2)
2. **Membedakan** model proses tradisional (Waterfall, V-Model, Spiral) dan modern (Agile, DevOps) (C2)
3. **Menjelaskan** Agile Manifesto (4 values, 12 principles) dan sejarahnya (C2)
4. **Mendeskripsikan** framework Scrum: roles, events, dan artifacts secara lengkap (C2)
5. **Memilih** model proses yang sesuai untuk skenario proyek tertentu (C3)

## Materi Pembelajaran

### 2.1 Konsep Proses Perangkat Lunak

Proses software (*software process*) adalah sekumpulan aktivitas dan hasil yang terkait untuk menghasilkan produk perangkat lunak. Sommerville mendefinisikan 4 aktivitas fundamental:

```
┌──────────────────────────────────────────────────────────────┐
│          4 AKTIVITAS FUNDAMENTAL PROSES SOFTWARE             │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐    ┌──────────────┐                       │
│  │ SPECIFICATION│───▶│ DEVELOPMENT  │                       │
│  │ Apa yang     │    │ Merancang &  │                       │
│  │ harus dibuat │    │ implementasi │                       │
│  └──────────────┘    └──────┬───────┘                       │
│                             │                                │
│  ┌──────────────┐    ┌──────▼───────┐                       │
│  │  EVOLUTION   │◀───│ VALIDATION   │                       │
│  │ Mengubah     │    │ Memastikan   │                       │
│  │ sesuai       │    │ sesuai       │                       │
│  │ kebutuhan    │    │ kebutuhan    │                       │
│  └──────────────┘    └──────────────┘                       │
│                                                              │
│  Setiap model proses mengatur URUTAN dan ITERASI             │
│  dari keempat aktivitas ini secara berbeda.                  │
└──────────────────────────────────────────────────────────────┘
```

### 2.2 Model Proses Tradisional

#### 2.2.1 Waterfall Model (Model Air Terjun)

Diciptakan oleh Winston Royce (1970). Setiap fase harus selesai sebelum masuk ke fase berikutnya — seperti air terjun yang mengalir ke bawah.

```
┌─────────────────┐
│   Requirements   │  ← Semua kebutuhan dikumpulkan di awal
└────────┬────────┘
         ▼
┌─────────────────┐
│     Design       │  ← Desain lengkap sebelum coding
└────────┬────────┘
         ▼
┌─────────────────┐
│ Implementation   │  ← Coding berdasarkan desain
└────────┬────────┘
         ▼
┌─────────────────┐
│    Testing       │  ← Testing setelah semua kode selesai
└────────┬────────┘
         ▼
┌─────────────────┐
│   Deployment     │  ← Deploy ke production
└────────┬────────┘
         ▼
┌─────────────────┐
│  Maintenance     │  ← Bug fix, update (ongoing)
└─────────────────┘
```

```python
# Simulasi Waterfall: setiap fase harus selesai sebelum lanjut

class WaterfallProject:
    """Simulasi proyek dengan model Waterfall."""

    def __init__(self, nama_proyek):
        self.nama = nama_proyek
        self.fase_sekarang = 0
        self.fases = [
            "Requirements", "Design", "Implementation",
            "Testing", "Deployment", "Maintenance"
        ]
        self.selesai = {fase: False for fase in self.fases}

    def selesaikan_fase(self):
        """Selesaikan fase saat ini dan lanjut ke berikutnya."""
        fase = self.fases[self.fase_sekarang]
        self.selesai[fase] = True
        print(f"[OK] {fase} selesai")

        if self.fase_sekarang < len(self.fases) - 1:
            self.fase_sekarang += 1
            print(f"     Lanjut ke: {self.fases[self.fase_sekarang]}")
        else:
            print("     Proyek selesai!")

    def kembali_ke_fase(self, nama_fase):
        """Di Waterfall, kembali ke fase sebelumnya itu MAHAL."""
        idx = self.fases.index(nama_fase)
        biaya = (self.fase_sekarang - idx) * 100  # semakin jauh, semakin mahal
        print(f"[!!] Kembali ke {nama_fase}: biaya estimasi ${biaya}K")


proyek = WaterfallProject("Sistem Akademik UAI")
proyek.selesaikan_fase()  # Requirements selesai
proyek.selesaikan_fase()  # Design selesai
proyek.selesaikan_fase()  # Implementation selesai
# Oops, ternyata requirements berubah!
proyek.kembali_ke_fase("Requirements")
# Output: [!!] Kembali ke Requirements: biaya estimasi $300K
```

**Kapan Waterfall cocok:**
- Requirements sudah stabil dan sangat jelas
- Proyek regulasi ketat (embedded systems, medis, militer)
- Tim sudah berpengalaman dengan domain
- Kontrak fixed-price dengan scope yang jelas

#### 2.2.2 V-Model (Verification & Validation)

Setiap fase development dipasangkan dengan fase testing yang sesuai:

```
Requirements ─────────────────────────────── Acceptance Testing
     │                                              ▲
     ▼                                              │
 System Design ─────────────────────── System Testing
      │                                        ▲
      ▼                                        │
  Detailed Design ─────────────── Integration Testing
       │                                  ▲
       ▼                                  │
    Coding ──────────────────── Unit Testing
```

**Keunggulan V-Model:** Testing direncanakan sejak awal, bukan *afterthought*.

#### 2.2.3 Spiral Model (Boehm, 1986)

Model spiral menambahkan **risk analysis** di setiap iterasi, cocok untuk proyek berisiko tinggi.

```
          Planning
         ╱        ╲
        ╱          ╲
  Evaluation    Risk Analysis
        ╲          ╱
         ╲        ╱
        Engineering

  Setiap putaran spiral = 1 iterasi
  Iterasi 1: Proof of concept
  Iterasi 2: Prototype
  Iterasi 3: MVP
  Iterasi 4: Product
```

#### 2.2.4 Iterative & Incremental

```
┌────────────────────────────────────────────────────────┐
│  ITERATIVE & INCREMENTAL MODEL                         │
│                                                        │
│  Iterasi 1:  [Login]                                   │
│  Iterasi 2:  [Login] + [Pencarian Buku]                │
│  Iterasi 3:  [Login] + [Pencarian] + [Peminjaman]      │
│  Iterasi 4:  [Login] + [Pencarian] + [Peminjaman]      │
│              + [Pengembalian] + [Notifikasi]            │
│                                                        │
│  Setiap iterasi menghasilkan software yang berjalan!   │
└────────────────────────────────────────────────────────┘
```

### 2.3 Agile Software Development

#### 2.3.1 Sejarah Agile Manifesto

Pada Februari 2001, 17 praktisi software berkumpul di Snowbird, Utah, dan menulis **Manifesto for Agile Software Development**.

#### 2.3.2 Agile Manifesto — 4 Values

```
┌──────────────────────────────────────────────────────────┐
│              AGILE MANIFESTO — 4 VALUES                   │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Kami menghargai:                LEBIH DARI:              │
│                                                          │
│  Individuals & interactions  >  Processes & tools        │
│  Working software            >  Comprehensive docs       │
│  Customer collaboration      >  Contract negotiation     │
│  Responding to change        >  Following a plan         │
│                                                          │
│  ⚠ Item di kanan TETAP penting, hanya saja item         │
│    di kiri LEBIH diprioritaskan.                         │
└──────────────────────────────────────────────────────────┘
```

#### 2.3.3 Agile Manifesto — 12 Principles

```python
# 12 Prinsip Agile Manifesto

agile_principles = [
    "1.  Prioritas utama: memuaskan pelanggan melalui delivery software yang bernilai secara dini dan berkelanjutan",
    "2.  Menyambut perubahan requirements, bahkan di akhir development",
    "3.  Deliver working software secara berkala (minggu-bulan, prefer yang lebih pendek)",
    "4.  Pebisnis dan developer harus bekerja BERSAMA setiap hari",
    "5.  Bangun proyek di sekitar individu yang termotivasi, beri lingkungan dan dukungan",
    "6.  Komunikasi tatap muka (face-to-face) adalah cara paling efisien",
    "7.  Working software adalah ukuran utama progres",
    "8.  Proses agile mendorong sustainable development — pace yang konstan",
    "9.  Perhatian berkelanjutan pada technical excellence dan good design",
    "10. Kesederhanaan — seni memaksimalkan pekerjaan yang TIDAK dilakukan",
    "11. Arsitektur, requirements, dan desain terbaik muncul dari self-organizing teams",
    "12. Secara berkala, tim merefleksikan cara menjadi lebih efektif, lalu menyesuaikan perilaku",
]

for p in agile_principles:
    print(p)
```

### 2.4 Scrum Framework — Detail Lengkap

Scrum adalah **framework Agile paling populer** (digunakan oleh 58% tim Agile menurut State of Agile Report 2023).

#### 2.4.1 Scrum Overview

```
┌──────────────────────────────────────────────────────────────┐
│                    SCRUM FRAMEWORK                            │
│                                                              │
│  Product         Sprint        Sprint Backlog                │
│  Backlog         Planning      ┌──────────┐                  │
│  ┌────────┐     ┌────────┐    │ Story A  │                  │
│  │ Story 1│────▶│ SELECT │───▶│ Story B  │───┐              │
│  │ Story 2│     │ items  │    │ Story C  │   │              │
│  │ Story 3│     └────────┘    └──────────┘   │              │
│  │ Story 4│                                   │              │
│  │  ...   │         ┌─────────────────────────┘              │
│  └────────┘         │                                        │
│       ▲             ▼                                        │
│       │      ┌──────────────┐                                │
│       │      │   SPRINT     │  2-4 minggu                    │
│       │      │  (timeboxed) │                                │
│       │      │              │  Daily Standup                 │
│       │      │  ┌────────┐  │  (15 min/hari)                │
│       │      │  │ Build  │  │                                │
│       │      │  │ Test   │  │                                │
│       │      │  │ Review │  │                                │
│       │      │  └────────┘  │                                │
│       │      └──────┬───────┘                                │
│       │             │                                        │
│       │             ▼                                        │
│       │      ┌──────────────┐    ┌──────────────┐           │
│       │      │   Sprint     │───▶│    Sprint     │           │
│       └──────│   Review     │    │ Retrospective │           │
│   feedback   │  (demo)      │    │ (improve)     │           │
│              └──────────────┘    └──────────────┘           │
│                     │                                        │
│                     ▼                                        │
│              ┌──────────────┐                                │
│              │  Increment   │  (potentially shippable)       │
│              │  (working    │                                │
│              │   software)  │                                │
│              └──────────────┘                                │
└──────────────────────────────────────────────────────────────┘
```

#### 2.4.2 Scrum Roles (3 Peran)

```
┌──────────────────────────────────────────────────────────────┐
│                    SCRUM ROLES                                │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  PRODUCT OWNER (1 orang)                                     │
│  ├── Mewakili stakeholder dan pengguna                       │
│  ├── Mengelola Product Backlog (prioritas, isi, urutan)      │
│  ├── Memutuskan APA yang dibangun                            │
│  └── Contoh: Kepala Perpustakaan UAI                         │
│                                                              │
│  SCRUM MASTER (1 orang)                                      │
│  ├── Memfasilitasi proses Scrum                              │
│  ├── Menghilangkan hambatan (impediments)                    │
│  ├── BUKAN manajer, tapi servant-leader                      │
│  └── Contoh: Senior developer yang paham Scrum               │
│                                                              │
│  DEVELOPMENT TEAM (3-9 orang)                                │
│  ├── Cross-functional (developer, tester, designer)          │
│  ├── Self-organizing (tim menentukan BAGAIMANA)              │
│  ├── Bertanggung jawab membuat Increment                     │
│  └── Contoh: Programmer, QA engineer, UI designer            │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

#### 2.4.3 Scrum Events (5 Event)

```python
# Detail 5 Scrum Events

scrum_events = {
    "Sprint": {
        "durasi": "1-4 minggu (biasanya 2 minggu)",
        "tujuan": "Menghasilkan Increment yang potentially shippable",
        "aturan": [
            "Tidak boleh mengubah Sprint Goal",
            "Kualitas tidak boleh dikurangi",
            "Scope bisa dinegosiasi dengan Product Owner",
        ],
    },
    "Sprint Planning": {
        "durasi": "Maks 8 jam untuk Sprint 1 bulan, proporsional untuk lebih pendek",
        "tujuan": "Menentukan APA dan BAGAIMANA Sprint ini",
        "output": "Sprint Goal + Sprint Backlog",
        "peserta": "Seluruh Scrum Team",
    },
    "Daily Standup": {
        "durasi": "Maks 15 menit",
        "tujuan": "Sinkronisasi tim dan identifikasi hambatan",
        "format": [
            "Apa yang saya kerjakan kemarin?",
            "Apa yang akan saya kerjakan hari ini?",
            "Apakah ada hambatan (impediment)?",
        ],
        "peserta": "Development Team (PO & SM opsional)",
    },
    "Sprint Review": {
        "durasi": "Maks 4 jam untuk Sprint 1 bulan",
        "tujuan": "Demo Increment ke stakeholder, kumpulkan feedback",
        "output": "Updated Product Backlog berdasarkan feedback",
        "peserta": "Scrum Team + Stakeholders",
    },
    "Sprint Retrospective": {
        "durasi": "Maks 3 jam untuk Sprint 1 bulan",
        "tujuan": "Refleksi proses, identifikasi improvement",
        "format": [
            "Apa yang berjalan baik?",
            "Apa yang perlu diperbaiki?",
            "Action items untuk Sprint berikutnya",
        ],
        "peserta": "Scrum Team (tanpa stakeholder)",
    },
}

for event, detail in scrum_events.items():
    print(f"\n{'='*50}")
    print(f"  {event}")
    print(f"{'='*50}")
    for key, val in detail.items():
        if isinstance(val, list):
            print(f"  {key}:")
            for item in val:
                print(f"    - {item}")
        else:
            print(f"  {key}: {val}")
```

#### 2.4.4 Scrum Artifacts (3 Artefak)

| Artifact | Deskripsi | Pemilik | Commitment |
|----------|-----------|---------|------------|
| **Product Backlog** | Daftar semua yang dibutuhkan produk, terurut prioritas | Product Owner | Product Goal |
| **Sprint Backlog** | Item yang dipilih untuk Sprint + rencana delivery | Dev Team | Sprint Goal |
| **Increment** | Hasil kerja Sprint yang memenuhi Definition of Done | Dev Team | Definition of Done |

#### 2.4.5 Simulasi Sprint — Sistem Perpustakaan Kampus

```python
# Simulasi Sprint untuk proyek Sistem Perpustakaan

class SprintSimulation:
    def __init__(self, sprint_number, duration_weeks=2):
        self.sprint = sprint_number
        self.duration = duration_weeks
        self.sprint_backlog = []
        self.done = []
        self.impediments = []

    def sprint_planning(self, product_backlog):
        """Sprint Planning: pilih item dari Product Backlog."""
        print(f"\n--- SPRINT {self.sprint} PLANNING ---")
        # Tim memilih berdasarkan kapasitas (velocity)
        velocity = 20  # story points per sprint
        total_points = 0
        for item in product_backlog:
            if total_points + item["points"] <= velocity:
                self.sprint_backlog.append(item)
                total_points += item["points"]
        print(f"Sprint Goal: {self.sprint_backlog[0]['story'][:30]}...")
        print(f"Items selected: {len(self.sprint_backlog)}, Total SP: {total_points}")

    def daily_standup(self, hari):
        """Daily Standup: 15 menit setiap hari."""
        print(f"\n  Daily Standup Hari {hari}:")
        print(f"  - Kemarin: Implementasi {self.sprint_backlog[0]['story'][:25]}...")
        print(f"  - Hari ini: Lanjut + testing")
        if hari == 3:
            self.impediments.append("Database migration gagal")
            print(f"  - Impediment: {self.impediments[-1]}")

    def sprint_review(self):
        """Sprint Review: demo ke stakeholder."""
        self.done = self.sprint_backlog.copy()
        print(f"\n--- SPRINT {self.sprint} REVIEW ---")
        print(f"Demo: {len(self.done)} item selesai")
        for item in self.done:
            print(f"  [DONE] {item['story']}")

    def sprint_retrospective(self):
        """Sprint Retrospective: perbaikan proses."""
        print(f"\n--- SPRINT {self.sprint} RETROSPECTIVE ---")
        print("  Baik  : Pair programming efektif")
        print("  Perbaiki: Perlu otomatisasi testing")
        print("  Action : Setup pytest + CI pipeline di Sprint berikut")


# Product Backlog untuk Sistem Perpustakaan
product_backlog = [
    {"story": "Login mahasiswa dengan NIM", "points": 5},
    {"story": "Pencarian buku berdasarkan judul", "points": 8},
    {"story": "Peminjaman buku (maks 3 buku)", "points": 5},
    {"story": "Notifikasi keterlambatan via email", "points": 8},
    {"story": "Dashboard statistik peminjaman", "points": 13},
]

# Jalankan simulasi Sprint 1
sprint1 = SprintSimulation(sprint_number=1)
sprint1.sprint_planning(product_backlog)
sprint1.daily_standup(1)
sprint1.daily_standup(3)
sprint1.sprint_review()
sprint1.sprint_retrospective()
```

### 2.5 Kanban

Kanban berasal dari Toyota Production System (Jepang). Fokus pada **visualisasi kerja** dan **membatasi Work-in-Progress (WIP)**.

```
┌──────────────────────────────────────────────────────────────┐
│                    KANBAN BOARD                               │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│ Backlog  │ To Do    │ In Prog  │ Review   │ Done            │
│          │ (WIP: 3) │ (WIP: 2) │ (WIP: 2) │                 │
├──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ [Search] │ [Login]  │ [Auth]   │ [DB     │ [Project Setup] │
│ [Report] │ [API]    │ [UI]     │  Schema] │ [README]        │
│ [Export] │ [Tests]  │          │          │ [Wireframe]     │
│ [Notif]  │          │          │          │                 │
└──────────┴──────────┴──────────┴──────────┴─────────────────┘
         WIP Limit mencegah tim mengambil terlalu banyak task
```

**Prinsip Kanban:**
1. Visualisasikan alur kerja (Kanban Board)
2. Batasi Work-in-Progress (WIP Limits)
3. Kelola alur (*manage flow*)
4. Buat kebijakan proses eksplisit
5. Implementasikan feedback loop
6. Tingkatkan secara kolaboratif, evolusikan secara eksperimental

### 2.6 Extreme Programming (XP)

XP menekankan **technical practices** untuk menghasilkan kode berkualitas tinggi:

```
┌──────────────────────────────────────────────────────────┐
│              EXTREME PROGRAMMING (XP) PRACTICES          │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌─── Technical ────────────┐  ┌─── Process ─────────┐ │
│  │ Pair Programming         │  │ Small Releases       │ │
│  │ Test-Driven Development  │  │ Planning Game        │ │
│  │ Continuous Integration   │  │ On-site Customer     │ │
│  │ Refactoring             │  │ Sustainable Pace     │ │
│  │ Simple Design           │  │ Collective Ownership │ │
│  │ Coding Standards        │  │ Metaphor             │ │
│  └──────────────────────────┘  └──────────────────────┘ │
│                                                          │
│  XP Motto: "Embrace Change"                             │
└──────────────────────────────────────────────────────────┘
```

### 2.7 DevOps Culture

DevOps = **Development + Operations** — sebuah budaya kolaborasi untuk deliver software lebih cepat dan reliable.

```
┌──────────────────────────────────────────────────────────────┐
│                    DEVOPS INFINITY LOOP                       │
│                                                              │
│           Plan ──▶ Code ──▶ Build ──▶ Test                  │
│          ╱                                    ╲              │
│         ╱                                      ╲             │
│  DEVELOPMENT                              OPERATIONS         │
│         ╲                                      ╱             │
│          ╲                                    ╱              │
│           Monitor ◀── Operate ◀── Deploy ◀── Release        │
│                                                              │
│  Prinsip CAMS:                                               │
│  C = Culture (budaya kolaborasi)                             │
│  A = Automation (otomatisasi CI/CD)                          │
│  M = Measurement (metrics & monitoring)                      │
│  S = Sharing (knowledge sharing)                             │
└──────────────────────────────────────────────────────────────┘
```

```python
# DevOps pipeline sederhana (konseptual)

class DevOpsPipeline:
    """Simulasi CI/CD pipeline sederhana."""

    def __init__(self):
        self.stages = []

    def add_stage(self, name, action):
        self.stages.append({"name": name, "action": action})

    def run(self):
        print("--- CI/CD Pipeline Running ---")
        for i, stage in enumerate(self.stages, 1):
            status = stage["action"]()
            emoji = "PASS" if status else "FAIL"
            print(f"  Stage {i}: {stage['name']} [{emoji}]")
            if not status:
                print("  Pipeline GAGAL! Fix dan push ulang.")
                return False
        print("  Pipeline SUKSES! Deploy ke production.")
        return True


pipeline = DevOpsPipeline()
pipeline.add_stage("Lint (PEP 8)", lambda: True)
pipeline.add_stage("Unit Tests", lambda: True)
pipeline.add_stage("Integration Tests", lambda: True)
pipeline.add_stage("Build Docker Image", lambda: True)
pipeline.add_stage("Deploy to Staging", lambda: True)
pipeline.run()
```

### 2.8 Perbandingan Komprehensif 8 Model Proses

| Aspek | Waterfall | V-Model | Spiral | Iterative | Scrum | Kanban | XP | DevOps |
|-------|-----------|---------|--------|-----------|-------|--------|----|----|
| **Iterasi** | Tidak | Tidak | Ya (risk-based) | Ya | Sprint 2-4 minggu | Continuous | 1-2 minggu | Continuous |
| **Requirements** | Fixed awal | Fixed awal | Evolving | Evolving | Evolving | Evolving | Evolving | Evolving |
| **Feedback** | Di akhir | Di akhir | Per iterasi | Per iterasi | Setiap sprint | Real-time | Per iterasi | Real-time |
| **Risk Mgmt** | Rendah | Medium | Tinggi | Medium | Medium | Rendah | Medium | Tinggi |
| **Tim** | Terpisah | Terpisah | Terpisah | Flexible | Cross-functional | Flexible | Cross-functional | Dev + Ops |
| **Cocok untuk** | Regulasi ketat | Sistem kritikal | Risiko tinggi | Proyek medium | Kebanyakan proyek | Maintenance | Startup kecil | Modern web |

### 2.9 Studi Kasus: Memilih Model untuk Proyek Indonesia

```python
# Tool sederhana untuk merekomendasikan model proses

def rekomendasikan_model(proyek):
    """
    Berdasarkan karakteristik proyek, rekomendasikan model proses.
    """
    skor = {
        "Waterfall": 0, "Scrum": 0, "Kanban": 0,
        "XP": 0, "DevOps": 0, "Spiral": 0,
    }

    # Requirements stability
    if proyek["req_stabil"]:
        skor["Waterfall"] += 3
    else:
        skor["Scrum"] += 3
        skor["XP"] += 2

    # Team size
    if proyek["tim"] <= 5:
        skor["XP"] += 2
        skor["Kanban"] += 2
    elif proyek["tim"] <= 9:
        skor["Scrum"] += 3
    else:
        skor["Scrum"] += 2  # scaled Scrum

    # Regulasi ketat
    if proyek["regulasi"]:
        skor["Waterfall"] += 3
        skor["Spiral"] += 2

    # Perlu continuous delivery
    if proyek["continuous_delivery"]:
        skor["DevOps"] += 3
        skor["Kanban"] += 2

    # Risiko tinggi
    if proyek["risiko_tinggi"]:
        skor["Spiral"] += 3

    best = max(skor, key=skor.get)
    return best, skor


# Kasus 1: Startup e-commerce di Jakarta
kasus_1 = {
    "nama": "Startup E-commerce Jakarta",
    "req_stabil": False,
    "tim": 6,
    "regulasi": False,
    "continuous_delivery": True,
    "risiko_tinggi": False,
}

# Kasus 2: Sistem keuangan daerah (SIPKD)
kasus_2 = {
    "nama": "SIPKD (Sistem Keuangan Daerah)",
    "req_stabil": True,
    "tim": 15,
    "regulasi": True,
    "continuous_delivery": False,
    "risiko_tinggi": True,
}

# Kasus 3: Maintenance app Ruangguru
kasus_3 = {
    "nama": "Ruangguru Feature Team",
    "req_stabil": False,
    "tim": 4,
    "regulasi": False,
    "continuous_delivery": True,
    "risiko_tinggi": False,
}

for kasus in [kasus_1, kasus_2, kasus_3]:
    model, skor = rekomendasikan_model(kasus)
    print(f"\nProyek: {kasus['nama']}")
    print(f"Rekomendasi: {model}")
    print(f"Skor: {dict(sorted(skor.items(), key=lambda x: -x[1]))}")
```

### 2.10 Konteks Indonesia: Adopsi Agile di Industri

```
┌──────────────────────────────────────────────────────────────┐
│        ADOPSI AGILE DI PERUSAHAAN TEKNOLOGI INDONESIA        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  GOJEK/GOTO                                                  │
│  Model: Scrum + Spotify Model (tribes, squads, chapters)     │
│  Sprint: 2 minggu                                            │
│  Tantangan: Koordinasi antar 100+ squad                      │
│                                                              │
│  TOKOPEDIA                                                   │
│  Model: Scrum + Kanban hybrid                                │
│  Sprint: 2 minggu                                            │
│  Keunggulan: A/B testing terintegrasi di setiap sprint       │
│                                                              │
│  TRAVELOKA                                                   │
│  Model: Scrum                                                │
│  Sprint: 2 minggu                                            │
│  Fokus: Cross-functional team per product domain             │
│                                                              │
│  BUKALAPAK                                                   │
│  Model: Kanban + CI/CD                                       │
│  Fokus: Continuous deployment, feature flags                 │
│                                                              │
│  BANK MANDIRI (Digital)                                      │
│  Model: SAFe (Scaled Agile Framework)                        │
│  Tantangan: Regulasi OJK + transformasi digital              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Kegiatan Pembelajaran

### Pre-class (20 menit)
- Membaca Agile Manifesto di [agilemanifesto.org](https://agilemanifesto.org/)
- Membaca The Scrum Guide (ringkasan 2-3 halaman di [scrumguides.org](https://scrumguides.org/))
- Pikirkan: "Jika saya membangun app e-commerce, model proses apa yang akan saya pilih?"

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-25 menit | Model tradisional: Waterfall, V-Model, Spiral, Iterative | Ceramah interaktif |
| 25-50 menit | Agile Manifesto & Scrum Framework (roles, events, artifacts) | Ceramah + video |
| 50-75 menit | **Simulasi Scrum Mini**: Sprint Planning + Daily Standup + Review | Simulasi kelompok |
| 75-95 menit | Kanban, XP, DevOps: overview dan perbandingan | Ceramah + diskusi |
| 95-110 menit | Studi kasus: "Model mana yang cocok untuk proyek X?" | Diskusi kelompok |

### Post-class (20 menit)
- Refleksi tertulis: Bandingkan Waterfall vs Scrum dalam 5 aspek. Kapan masing-masing cocok?
- Preview: Requirements Engineering minggu depan
- Baca artikel tentang pengalaman Gojek mengadopsi Scrum

## Latihan dan Diskusi

### Soal 1 — Pemahaman Konsep (C2)
Jelaskan mengapa Agile Manifesto menyatakan "Working software over comprehensive documentation." Apakah ini berarti dokumentasi tidak penting? Berikan penjelasan Anda.

### Soal 2 — Analisis Skenario (C4)
Sebuah rumah sakit di Surabaya ingin membangun sistem rekam medis elektronik. Tim 10 developer, regulasi ketat dari Kemenkes, data sangat sensitif, deadline 18 bulan. Model proses apa yang paling cocok? Jelaskan alasan Anda dan gambarkan timeline kasar.

### Soal 3 — Scrum Mastery (C3)
Dalam sebuah Sprint, Development Team menemukan bahwa mereka tidak bisa menyelesaikan semua item di Sprint Backlog. Apa yang seharusnya mereka lakukan menurut Scrum Guide? Jelaskan langkah-langkahnya.

### Soal 4 — Perbandingan (C4)
Buatlah tabel perbandingan Scrum vs Kanban dalam 5 aspek: (a) iterasi, (b) roles, (c) WIP limits, (d) estimasi, (e) perubahan dalam iterasi. Berdasarkan perbandingan tersebut, kapan Anda akan memilih Kanban di atas Scrum?

### Soal 5 — Studi Kasus Indonesia (C5)
TransJakarta ingin membangun sistem tracking bus real-time. Requirements sering berubah karena rute baru, tim 8 developer, perlu update berkala ke penumpang via mobile app. Rekomendasikan model proses yang paling tepat beserta Sprint 0 plan-nya.

## Referensi

1. Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org.
2. Beck, K. et al. (2001). *Manifesto for Agile Software Development*. agilemanifesto.org.
3. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 2-3. Pearson.
4. Kim, G., Humble, J., Debois, P., & Willis, J. (2016). *The DevOps Handbook*. IT Revolution Press.
5. Beck, K. (2004). *Extreme Programming Explained* (2nd ed.). Addison-Wesley.
6. Anderson, D. J. (2010). *Kanban: Successful Evolutionary Change*. Blue Hole Press.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
