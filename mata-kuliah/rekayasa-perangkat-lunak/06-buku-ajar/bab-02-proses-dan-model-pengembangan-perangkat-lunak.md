# BAB 2: PROSES DAN MODEL PENGEMBANGAN PERANGKAT LUNAK

**Oleh: Tri Aji Nugroho, S.T., M.T.**
**Mata Kuliah:** IF2205 Rekayasa Perangkat Lunak
**Program Studi Informatika — Universitas Al Azhar Indonesia**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 1.3 | Membedakan model proses pengembangan (Waterfall, V-Model, Iterative, Spiral, Agile, Kanban, XP, DevOps) dan memilih model yang sesuai untuk konteks tertentu | C2 (Memahami) | 90 menit |
| 1.4 | Menjelaskan framework Scrum (3 roles, 5 events, 3 artifacts) dan prinsip Agile Manifesto (4 values, 12 principles) | C2 (Memahami) | 60 menit |

---

## Peta Konsep Bab

```
                    ┌──────────────────────────────┐
                    │   PROSES PERANGKAT LUNAK      │
                    │ (Software Process)             │
                    └──────────────┬───────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                    ▼
    ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
    │  MODEL           │  │  MODEL           │  │  KULTUR &        │
    │  TRADISIONAL     │  │  AGILE           │  │  PRAKTIK         │
    ├─────────────────┤  ├─────────────────┤  ├─────────────────┤
    │ • Waterfall      │  │ • Agile Manifesto│  │ • DevOps (CAMS)  │
    │ • V-Model        │  │ • Scrum          │  │ • CI/CD          │
    │ • Iterative      │  │ • Kanban         │  │ • Continuous     │
    │ • Spiral         │  │ • XP             │  │   Improvement    │
    └────────┬────────┘  └────────┬────────┘  └────────┬────────┘
              │                    │                    │
              └────────────────────┼────────────────────┘
                                   ▼
                    ┌──────────────────────────────┐
                    │  PEMILIHAN MODEL              │
                    │  (Decision Tree)              │
                    │  → Requirements stability     │
                    │  → Team size & maturity       │
                    │  → Risk level                 │
                    │  → Regulatory constraints     │
                    └──────────────────────────────┘
```

---

## 2.1 Konsep Proses Perangkat Lunak

### 2.1.1 Definisi Proses Perangkat Lunak

**Proses perangkat lunak** (*software process*) adalah serangkaian aktivitas terstruktur yang diperlukan untuk menghasilkan produk perangkat lunak. Proses ini bukan sekadar langkah-langkah teknis, melainkan mencakup aktivitas manajemen, kolaborasi tim, dan pengelolaan perubahan.

Menurut Sommerville (2016), proses perangkat lunak adalah "a set of activities and associated results that produce a software product." Setiap organisasi memiliki proses yang berbeda, tetapi ada pola-pola umum yang menjadi fondasi berbagai model pengembangan.

### 2.1.2 Empat Aktivitas Fundamental

Terlepas dari model yang digunakan, setiap proses perangkat lunak mencakup empat aktivitas fundamental:

```
┌──────────────────────────────────────────────────────────────┐
│                FOUR FUNDAMENTAL ACTIVITIES                     │
├───────────────┬───────────────┬───────────────┬──────────────┤
│ SPECIFICATION │  DEVELOPMENT  │  VALIDATION   │  EVOLUTION   │
│               │               │               │              │
│ Apa yang      │ Merancang &   │ Memastikan    │ Mengubah     │
│ harus         │ mengimplemen- │ sistem sesuai │ sistem       │
│ dilakukan     │ tasikan       │ kebutuhan     │ sesuai       │
│ sistem?       │ sistem        │ pelanggan     │ kebutuhan    │
│               │               │               │ baru         │
│ Output:       │ Output:       │ Output:       │ Output:      │
│ SRS, User     │ Source code,  │ Test results, │ Updated      │
│ Stories       │ Database      │ UAT sign-off  │ system       │
└───────────────┴───────────────┴───────────────┴──────────────┘
```

### 2.1.3 Model Proses sebagai Abstraksi

**Model proses** (*process model*) adalah representasi abstrak dari suatu proses perangkat lunak. Model ini memberikan deskripsi tentang urutan dan hubungan antar aktivitas. Tidak ada model yang "benar" untuk semua situasi — pemilihan model bergantung pada konteks proyek.

```python
# Simulasi: Representasi aktivitas fundamental dalam Python
class SoftwareProcess:
    """Representasi sederhana proses perangkat lunak."""

    def __init__(self, project_name: str, model: str):
        self.project_name = project_name
        self.model = model
        self.phases = []
        self.current_phase = None

    def add_phase(self, name: str, activities: list):
        """Tambahkan fase ke proses."""
        phase = {
            "name": name,
            "activities": activities,
            "status": "belum_dimulai"
        }
        self.phases.append(phase)
        return phase

    def start_phase(self, phase_name: str):
        """Mulai fase tertentu."""
        for phase in self.phases:
            if phase["name"] == phase_name:
                phase["status"] = "sedang_berjalan"
                self.current_phase = phase
                print(f"[{self.model}] Fase '{phase_name}' dimulai")
                return
        print(f"Fase '{phase_name}' tidak ditemukan")


# Contoh penggunaan
project = SoftwareProcess("Sistem Perpustakaan UAI", "Waterfall")
project.add_phase("Specification", ["elicitation", "analisis", "dokumentasi SRS"])
project.add_phase("Development", ["desain arsitektur", "coding", "integrasi"])
project.add_phase("Validation", ["unit test", "integration test", "UAT"])
project.add_phase("Evolution", ["bug fix", "fitur baru", "maintenance"])

project.start_phase("Specification")
# Output: [Waterfall] Fase 'Specification' dimulai
```

### 2.1.4 Mengapa Proses Penting?

Tanpa proses yang jelas, pengembangan software akan mengalami:
- **Chaos** — tidak ada koordinasi antar anggota tim
- **Scope creep** — requirements terus bertambah tanpa kontrol
- **Technical debt** — kode berkualitas rendah menumpuk
- **Late delivery** — deadline terlewat karena tidak ada perencanaan

> **Tips:** Di Indonesia, banyak startup tahap awal yang mengabaikan proses formal karena menganggapnya "terlalu lambat." Namun, seiring pertumbuhan tim (misalnya dari 5 ke 50 engineer), ketiadaan proses justru menjadi penghambat utama. Gojek, misalnya, harus melakukan transformasi besar dalam proses engineering mereka saat tim berkembang dari puluhan menjadi ratusan engineer.

---

## 2.2 Model Proses Tradisional

### 2.2.1 Waterfall Model (Royce, 1970)

Model Waterfall adalah model proses paling awal dan paling mudah dipahami. Setiap fase harus diselesaikan sepenuhnya sebelum fase berikutnya dimulai — seperti air terjun yang mengalir satu arah.

```
┌─────────────────┐
│   Requirements   │
│   Analysis       │ ← Semua kebutuhan didefinisikan di awal
└────────┬────────┘
         ▼
┌─────────────────┐
│   System         │
│   Design         │ ← Arsitektur & desain detail
└────────┬────────┘
         ▼
┌─────────────────┐
│   Implementation │
│   (Coding)       │ ← Penulisan kode program
└────────┬────────┘
         ▼
┌─────────────────┐
│   Integration &  │
│   Testing        │ ← Pengujian seluruh sistem
└────────┬────────┘
         ▼
┌─────────────────┐
│   Deployment &   │
│   Maintenance    │ ← Instalasi dan perawatan
└─────────────────┘
```

**Kelebihan Waterfall:**
- Sederhana dan mudah dipahami oleh semua stakeholder
- Dokumentasi lengkap di setiap fase — penting untuk audit dan compliance
- Milestone yang jelas memudahkan tracking progress
- Cocok untuk proyek dengan requirements yang stabil dan well-defined

**Kekurangan Waterfall:**
- Tidak fleksibel terhadap perubahan requirements
- Pelanggan baru melihat produk yang berjalan di akhir siklus
- Risiko besar jika terjadi kesalahan di fase awal (biaya fix di fase akhir sangat mahal)
- Integrasi dilakukan di akhir — bug integrasi baru ditemukan terlambat

**Kapan menggunakan Waterfall:**
- Requirements sudah pasti dan tidak akan berubah (misal: regulasi pemerintah)
- Proyek kecil dengan timeline pendek (< 3 bulan)
- Proyek dengan kontrak fixed-price dan deliverables yang jelas
- Sistem embedded atau safety-critical (medis, aviasi)

```python
# Simulasi: Waterfall Process Tracker
class WaterfallTracker:
    """Melacak progress proyek Waterfall."""

    PHASES = [
        "Requirements", "Design", "Implementation",
        "Testing", "Deployment", "Maintenance"
    ]

    def __init__(self, project_name: str):
        self.project_name = project_name
        self.current_phase_idx = 0
        self.phase_completion = {phase: 0.0 for phase in self.PHASES}

    def update_progress(self, percentage: float):
        """Update progress fase saat ini."""
        phase = self.PHASES[self.current_phase_idx]
        self.phase_completion[phase] = min(percentage, 100.0)
        print(f"  [{phase}] Progress: {percentage:.0f}%")

    def complete_phase(self):
        """Selesaikan fase saat ini dan lanjut ke berikutnya."""
        phase = self.PHASES[self.current_phase_idx]
        self.phase_completion[phase] = 100.0
        print(f"  ✓ Fase '{phase}' selesai")

        if self.current_phase_idx < len(self.PHASES) - 1:
            self.current_phase_idx += 1
            next_phase = self.PHASES[self.current_phase_idx]
            print(f"  → Lanjut ke fase '{next_phase}'")
        else:
            print(f"  ★ Proyek '{self.project_name}' selesai!")

    def show_status(self):
        """Tampilkan status seluruh proyek."""
        print(f"\n=== Status Proyek: {self.project_name} ===")
        for i, phase in enumerate(self.PHASES):
            marker = "→" if i == self.current_phase_idx else " "
            bar = "█" * int(self.phase_completion[phase] / 10)
            print(f"  {marker} {phase:15s} [{bar:<10s}] {self.phase_completion[phase]:.0f}%")


# Contoh penggunaan
tracker = WaterfallTracker("Sistem SIPKD Keuangan Daerah")
tracker.update_progress(100)
tracker.complete_phase()
tracker.update_progress(75)
tracker.show_status()
```

### 2.2.2 V-Model (Verification & Validation Model)

V-Model adalah ekstensi dari Waterfall yang secara eksplisit menghubungkan setiap fase development dengan fase testing yang sesuai. Bentuknya menyerupai huruf "V":

```
  Requirements Analysis  ←─────────────→  Acceptance Testing
       ↓                                        ↑
    System Design        ←─────────────→  System Testing
       ↓                                        ↑
      Architectural Design ←───────────→  Integration Testing
       ↓                                        ↑
        Module Design    ←─────────────→  Unit Testing
              ↓                              ↑
              └────────→  Coding  ──────────┘

  ← Sisi kiri: Verification (apakah kita membangun produk dengan benar?)
  → Sisi kanan: Validation (apakah kita membangun produk yang benar?)
```

**Prinsip V-Model:**
- Setiap fase development memiliki pasangan testing yang memvalidasinya
- Test plan ditulis **bersamaan** dengan fase development, bukan setelahnya
- Deteksi defect lebih dini dibanding Waterfall murni

**Kelebihan V-Model:**
- Testing direncanakan sejak awal — bukan afterthought
- Traceability jelas antara requirements dan test cases
- Sangat cocok untuk sistem safety-critical

**Kekurangan V-Model:**
- Masih rigid dan sequential seperti Waterfall
- Tidak mengakomodasi perubahan requirements dengan baik
- Overhead dokumentasi sangat tinggi

**Kapan menggunakan V-Model:**
- Sistem medis (peralatan rumah sakit, rekam medis elektronik)
- Sistem aviasi dan otomotif
- Proyek pemerintah dengan regulasi ketat (misal: sistem e-KTP, SIPKD)

### 2.2.3 Iterative & Incremental Model

Model ini mengembangkan sistem secara bertahap melalui beberapa iterasi, di mana setiap iterasi menghasilkan versi yang semakin lengkap:

```
  Iterasi 1           Iterasi 2           Iterasi 3           Iterasi 4
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│ Plan → Code │   │ Plan → Code │   │ Plan → Code │   │ Plan → Code │
│ → Test →    │   │ → Test →    │   │ → Test →    │   │ → Test →    │
│ Evaluate    │   │ Evaluate    │   │ Evaluate    │   │ Release     │
└──────┬──────┘   └──────┬──────┘   └──────┬──────┘   └─────────────┘
       │                 │                 │
   Fitur Login      + Katalog Buku   + Peminjaman      + Laporan
   (v0.1)           (v0.2)           (v0.3)             (v1.0)
```

**Perbedaan Iterative vs Incremental:**
- **Iterative**: mengulang seluruh proses, memperbaiki dan memperdalam fitur di setiap iterasi
- **Incremental**: menambahkan fitur baru di setiap increment
- Dalam praktik, keduanya sering dikombinasikan

```python
# Simulasi: Iterative development tracker
def simulate_iterative_development():
    """Simulasi pengembangan iteratif sistem perpustakaan."""
    iterations = [
        {
            "name": "Iterasi 1",
            "features": ["Login mahasiswa", "Registrasi akun"],
            "feedback": "UI kurang intuitif, tambah fitur lupa password"
        },
        {
            "name": "Iterasi 2",
            "features": ["Katalog buku", "Pencarian buku", "Perbaikan UI login"],
            "feedback": "Pencarian perlu filter, tambah fitur peminjaman"
        },
        {
            "name": "Iterasi 3",
            "features": ["Peminjaman buku", "Pengembalian", "Filter pencarian"],
            "feedback": "Perlu notifikasi keterlambatan"
        },
        {
            "name": "Iterasi 4",
            "features": ["Notifikasi email", "Laporan peminjaman", "Dashboard admin"],
            "feedback": "Siap untuk release!"
        },
    ]

    total_features = 0
    for iteration in iterations:
        total_features += len(iteration["features"])
        print(f"\n{iteration['name']}:")
        print(f"  Fitur baru: {', '.join(iteration['features'])}")
        print(f"  Total fitur kumulatif: {total_features}")
        print(f"  Feedback: {iteration['feedback']}")


simulate_iterative_development()
```

### 2.2.4 Spiral Model (Boehm, 1986)

Spiral Model menggabungkan elemen iteratif dengan penekanan khusus pada **analisis risiko** di setiap iterasi. Model ini sangat cocok untuk proyek besar dan berisiko tinggi.

```
                          Planning
                        ╱          ╲
                      ╱              ╲
                    ╱                  ╲
           Risk Analysis      Engineering (Development)
                    ╲                  ╱
                      ╲              ╱
                        ╲          ╱
                        Evaluation
                             │
                    (Ulangi spiral berikutnya
                     dengan scope lebih besar)

  Spiral 1: Concept of operation → Prototype 1
  Spiral 2: Requirements → Prototype 2
  Spiral 3: Design → Prototype 3
  Spiral 4: Implementation → Operational system
```

**Empat Kuadran Spiral:**

| Kuadran | Aktivitas | Output |
|---------|-----------|--------|
| **Planning** | Tentukan objektif, alternatif, constraints | Project plan, scope definition |
| **Risk Analysis** | Identifikasi dan evaluasi risiko, buat prototype untuk mitigasi | Risk assessment, prototype |
| **Engineering** | Develop dan verifikasi produk | Working software increment |
| **Evaluation** | Review hasil, rencana iterasi berikutnya | Customer feedback, go/no-go decision |

**Kapan menggunakan Spiral:**
- Proyek besar dengan anggaran signifikan (> 5 miliar)
- Proyek dengan risiko teknis tinggi (teknologi baru, integrasi kompleks)
- Proyek R&D atau inovatif
- Contoh Indonesia: Pengembangan sistem pertahanan, sistem perbankan core

> **Tips:** Spiral Model jarang digunakan secara murni di industri karena overhead manajemen yang tinggi. Namun, konsep risk-driven development yang diperkenalkan Boehm sangat berpengaruh pada model-model modern.

---

## 2.3 Agile Software Development

### 2.3.1 Latar Belakang Munculnya Agile

Pada akhir 1990-an, industri software mengalami krisis kepercayaan terhadap model tradisional:
- **Standish Group CHAOS Report (1994)**: Hanya 16% proyek software yang berhasil sesuai rencana
- Requirements yang berubah menjadi norma, bukan pengecualian
- Pelanggan frustrasi karena baru melihat produk di akhir development cycle

Pada Februari 2001, 17 praktisi software berkumpul di Snowbird, Utah, dan merumuskan **Agile Manifesto** — sebuah deklarasi yang mengubah cara dunia mengembangkan software.

### 2.3.2 Agile Manifesto: 4 Values

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MANIFESTO FOR AGILE SOFTWARE DEVELOPMENT          │
│                                                                      │
│  Kami menemukan cara yang lebih baik untuk mengembangkan software    │
│  dengan melakukannya dan membantu orang lain melakukannya.           │
│                                                                      │
│  Melalui pekerjaan ini, kami menghargai:                             │
│                                                                      │
│  ► Individuals and interactions    OVER  Processes and tools         │
│  ► Working software                OVER  Comprehensive documentation │
│  ► Customer collaboration          OVER  Contract negotiation        │
│  ► Responding to change            OVER  Following a plan            │
│                                                                      │
│  Artinya, walaupun item di sebelah kanan bernilai,                   │
│  kami LEBIH menghargai item di sebelah kiri.                         │
└─────────────────────────────────────────────────────────────────────┘
```

**Deep Dive setiap Value:**

**Value 1: Individuals and Interactions over Processes and Tools**
- Tools dan proses membantu, tetapi tidak menggantikan kemampuan dan kolaborasi manusia
- Tim yang hebat dengan tools sederhana akan mengalahkan tim biasa dengan tools mahal
- Komunikasi langsung (face-to-face) lebih efektif daripada dokumen formal
- Contoh: Tim kecil Tokopedia di awal (5-10 orang) bisa deliver fitur dengan cepat karena komunikasi langsung, meskipun belum ada proses formal

**Value 2: Working Software over Comprehensive Documentation**
- Dokumentasi penting, tetapi software yang berjalan adalah ukuran utama kemajuan
- "No documentation" bukan berarti Agile — dokumentasi tetap ada, tapi secukupnya
- User lebih butuh melihat demo daripada membaca dokumen 200 halaman
- Contoh: MVP (Minimum Viable Product) Gojek awalnya hanya call center + spreadsheet — bukan sistem lengkap

**Value 3: Customer Collaboration over Contract Negotiation**
- Pelanggan adalah bagian dari tim, bukan pihak di seberang meja
- Feedback cepat dan berkelanjutan lebih baik daripada spesifikasi fixed di awal
- Kontrak tetap ada, tetapi hubungan kolaboratif lebih diutamakan
- Contoh: Startup Indonesia sering melibatkan user dalam beta testing — Ruangguru rutin melakukan user interview dengan guru dan siswa

**Value 4: Responding to Change over Following a Plan**
- Perubahan requirements adalah realita, bukan masalah yang harus dihindari
- Rencana tetap ada, tetapi harus adaptif (plan ≠ commitment yang rigid)
- Kemampuan beradaptasi adalah keunggulan kompetitif
- Contoh: Saat pandemi COVID-19, Halodoc harus mengubah prioritas development dalam hitungan hari untuk mengakomodasi lonjakan telekonsultasi

### 2.3.3 12 Principles of Agile

Dua belas prinsip Agile memberikan pedoman praktis untuk menerapkan keempat value:

| No | Prinsip | Penjelasan Praktis |
|----|---------|-------------------|
| 1 | Kepuasan pelanggan melalui early dan continuous delivery | Deliver fitur kecil yang berguna setiap 1-4 minggu |
| 2 | Sambut perubahan requirements, bahkan di tahap akhir | Perubahan = keunggulan kompetitif pelanggan |
| 3 | Deliver working software secara berkala (minggu-bulan) | Prefer rentang waktu lebih pendek |
| 4 | Bisnis dan developer harus bekerja sama setiap hari | Product Owner hadir di daily standup |
| 5 | Bangun proyek di sekitar individu yang termotivasi | Beri trust, environment, dan support |
| 6 | Face-to-face conversation adalah komunikasi paling efektif | Video call > chat > email |
| 7 | Working software adalah ukuran utama kemajuan | Bukan jumlah dokumen atau meeting |
| 8 | Sustainable development — pace yang bisa dipertahankan | Hindari crunch/lembur berlebihan |
| 9 | Perhatian berkelanjutan pada technical excellence | Clean code, refactoring, testing |
| 10 | Kesederhanaan — memaksimalkan pekerjaan yang TIDAK dilakukan | YAGNI (You Ain't Gonna Need It) |
| 11 | Tim self-organizing menghasilkan arsitektur terbaik | Tim memutuskan cara kerja sendiri |
| 12 | Refleksi berkala untuk menjadi lebih efektif | Retrospective setiap sprint |

```python
# Representasi 12 Agile Principles sebagai checklist tim
agile_health_check = {
    "early_delivery": "Apakah kita deliver fitur setiap sprint?",
    "welcome_change": "Apakah kita menyambut perubahan requirements?",
    "frequent_delivery": "Apakah interval delivery kita < 4 minggu?",
    "daily_collaboration": "Apakah PO hadir di daily standup?",
    "motivated_individuals": "Apakah tim diberi otonomi dan kepercayaan?",
    "face_to_face": "Apakah kita lebih sering tatap muka daripada email?",
    "working_software": "Apakah kita mengukur kemajuan dari software yang jalan?",
    "sustainable_pace": "Apakah tim bisa mempertahankan pace tanpa burnout?",
    "technical_excellence": "Apakah kita rutin refactoring dan menulis test?",
    "simplicity": "Apakah kita hanya membangun fitur yang benar-benar dibutuhkan?",
    "self_organizing": "Apakah tim memutuskan cara kerja sendiri?",
    "reflect_and_adjust": "Apakah kita rutin retrospective dan berubah?"
}

def run_agile_health_check(responses: dict) -> float:
    """Hitung skor kesehatan Agile tim (0-100)."""
    score = sum(1 for v in responses.values() if v) / len(responses) * 100
    if score >= 80:
        print(f"Skor: {score:.0f}% — Tim sangat Agile!")
    elif score >= 60:
        print(f"Skor: {score:.0f}% — Cukup baik, ada ruang perbaikan")
    else:
        print(f"Skor: {score:.0f}% — Perlu evaluasi serius terhadap praktik Agile")
    return score


# Contoh: Tim proyek mahasiswa mengevaluasi diri
team_responses = {
    "early_delivery": True,
    "welcome_change": True,
    "frequent_delivery": True,
    "daily_collaboration": False,  # PO jarang hadir
    "motivated_individuals": True,
    "face_to_face": False,  # Kebanyakan chat
    "working_software": True,
    "sustainable_pace": False,  # Sering begadang mendekati deadline
    "technical_excellence": False,  # Jarang refactoring
    "simplicity": True,
    "self_organizing": True,
    "reflect_and_adjust": False,  # Belum pernah retrospective
}

run_agile_health_check(team_responses)
# Output: Skor: 58% — Perlu evaluasi serius terhadap praktik Agile
```

---

## 2.4 Scrum Framework

### 2.4.1 Apa Itu Scrum?

Scrum adalah framework Agile paling populer di dunia. Menurut *The Scrum Guide* (Schwaber & Sutherland, 2020), Scrum adalah "a lightweight framework that helps people, teams and organizations generate value through adaptive solutions for complex problems."

Scrum **bukan** metodologi lengkap — Scrum adalah **framework** yang sengaja dibuat minimal agar tim bisa mengadaptasinya sesuai konteks.

```
┌─────────────────────────────────────────────────────────────┐
│                     SCRUM FRAMEWORK                          │
│                                                              │
│  Product    Sprint      Daily       Sprint     Sprint        │
│  Backlog → Planning → Standup  → Review  → Retrospective    │
│    ↑          ↓       (15 min)   (Demo)    (Improve)        │
│    │     Sprint Backlog   ↓                                  │
│    │          ↓        Working                               │
│    └── Feedback ←──── Increment  (Setiap 1-4 minggu)        │
│                                                              │
│  3 Roles │ 5 Events │ 3 Artifacts │ 5 Values               │
└─────────────────────────────────────────────────────────────┘
```

### 2.4.2 Scrum Roles (3 Roles)

| Role | Tanggung Jawab | Analogi Indonesia |
|------|----------------|-------------------|
| **Product Owner (PO)** | Mengelola Product Backlog, memutuskan prioritas, mewakili suara pelanggan dan stakeholder, memaksimalkan value produk | Seperti "kepala proyek" yang memutuskan fitur mana yang paling penting |
| **Scrum Master (SM)** | Memfasilitasi proses Scrum, menghilangkan hambatan (*impediments*), melindungi tim dari gangguan, coaching tim tentang Agile | Seperti "wasit" yang memastikan aturan main diikuti dan tim bisa bermain optimal |
| **Developers** | Tim 3-9 orang, self-organizing, cross-functional, bertanggung jawab membuat Increment yang "Done" setiap sprint | Para engineer yang melakukan design, code, test, dan deploy |

> **Penting:** Dalam Scrum Guide 2020, istilah "Development Team" diganti menjadi "Developers" untuk menghilangkan kesan sub-tim. Seluruh Scrum Team bertanggung jawab atas keberhasilan produk.

```python
# Contoh: Struktur Scrum Team dalam Python
class ScrumTeam:
    """Representasi Scrum Team."""

    def __init__(self, product_name: str):
        self.product_name = product_name
        self.product_owner = None
        self.scrum_master = None
        self.developers = []

    def set_product_owner(self, name: str, expertise: str):
        self.product_owner = {"name": name, "expertise": expertise}
        print(f"PO: {name} ({expertise})")

    def set_scrum_master(self, name: str):
        self.scrum_master = {"name": name}
        print(f"SM: {name}")

    def add_developer(self, name: str, skills: list):
        self.developers.append({"name": name, "skills": skills})
        print(f"Dev: {name} — {', '.join(skills)}")

    def is_valid(self) -> bool:
        """Cek apakah Scrum Team valid (3-9 developers)."""
        valid = (
            self.product_owner is not None
            and self.scrum_master is not None
            and 3 <= len(self.developers) <= 9
        )
        print(f"\nTim valid: {'Ya' if valid else 'Tidak'} "
              f"({len(self.developers)} developers)")
        return valid


# Contoh: Tim proyek UMKM App
team = ScrumTeam("Aplikasi Kasir UMKM")
team.set_product_owner("Rina", "domain UMKM & retail")
team.set_scrum_master("Budi")
team.add_developer("Andi", ["Python", "Flask", "PostgreSQL"])
team.add_developer("Sari", ["JavaScript", "React", "CSS"])
team.add_developer("Dimas", ["Python", "Testing", "Docker"])
team.add_developer("Putri", ["UI/UX", "HTML", "Figma"])
team.is_valid()
```

### 2.4.3 Scrum Events (5 Events)

Scrum memiliki 5 event formal yang menciptakan regularity dan meminimalkan kebutuhan meeting lain:

| Event | Time-box | Tujuan | Peserta |
|-------|----------|--------|---------|
| **Sprint** | 1-4 minggu (konsisten) | Container untuk semua event lainnya | Seluruh Scrum Team |
| **Sprint Planning** | Maks 8 jam (sprint 4 minggu) | Memilih item dari Product Backlog, merencanakan sprint | Seluruh Scrum Team |
| **Daily Scrum** | 15 menit | Inspeksi progress, adaptasi rencana harian | Developers (PO & SM opsional) |
| **Sprint Review** | Maks 4 jam (sprint 4 minggu) | Demo Increment, kumpulkan feedback stakeholder | Scrum Team + stakeholders |
| **Sprint Retrospective** | Maks 3 jam (sprint 4 minggu) | Refleksi proses, identifikasi improvement | Seluruh Scrum Team |

**Detail setiap Event:**

**Sprint** — Jantung Scrum. Durasi tetap (biasanya 2 minggu di Indonesia). Selama Sprint:
- Tidak ada perubahan yang membahayakan Sprint Goal
- Scope bisa dinegosiasi ulang antara PO dan Developers
- Kualitas tidak boleh dikurangi

**Sprint Planning** menjawab tiga pertanyaan:
1. **Mengapa Sprint ini berharga?** → Sprint Goal
2. **Apa yang bisa Done Sprint ini?** → Memilih item dari Product Backlog
3. **Bagaimana cara menyelesaikannya?** → Breakdown menjadi tasks

**Daily Scrum** (3 pertanyaan klasik):
- Apa yang saya kerjakan kemarin?
- Apa yang akan saya kerjakan hari ini?
- Apakah ada hambatan (*impediment*)?

```python
# Simulasi Daily Scrum
def daily_scrum(team_updates: list):
    """Simulasi daily scrum standup."""
    print("=" * 50)
    print("DAILY SCRUM — Senin, 14 April 2026, 09:00 WIB")
    print("=" * 50)

    for update in team_updates:
        print(f"\n👤 {update['name']}:")
        print(f"   Kemarin : {update['yesterday']}")
        print(f"   Hari ini: {update['today']}")
        if update.get("impediment"):
            print(f"   ⚠ Hambatan: {update['impediment']}")
        else:
            print(f"   ✓ Tidak ada hambatan")

    print("\n" + "=" * 50)
    print("Durasi: < 15 menit | Selesai!")


daily_scrum([
    {
        "name": "Andi (Backend)",
        "yesterday": "Selesai API endpoint GET /produk",
        "today": "Mulai API POST /transaksi",
        "impediment": "Perlu akses ke API payment gateway Midtrans"
    },
    {
        "name": "Sari (Frontend)",
        "yesterday": "Selesai halaman katalog produk",
        "today": "Integrasi halaman katalog dengan API backend",
        "impediment": None
    },
    {
        "name": "Dimas (QA/DevOps)",
        "yesterday": "Setup GitHub Actions CI pipeline",
        "today": "Tulis unit test untuk API produk",
        "impediment": None
    },
])
```

### 2.4.4 Scrum Artifacts (3 Artifacts)

| Artifact | Deskripsi | Commitment |
|----------|-----------|------------|
| **Product Backlog** | Daftar terurut (*ordered*) semua yang dibutuhkan produk — fitur, perbaikan, technical debt | **Product Goal** — tujuan jangka panjang produk |
| **Sprint Backlog** | Subset Product Backlog yang dipilih untuk Sprint ini + rencana delivery | **Sprint Goal** — tujuan yang ingin dicapai Sprint ini |
| **Increment** | Jumlah semua Product Backlog Items yang "Done" — kumulatif dari sprint-sprint sebelumnya | **Definition of Done** — standar kualitas minimum |

**Definition of Done (DoD)** — Contoh untuk proyek kuliah:
- Kode sudah di-review oleh minimal 1 anggota tim
- Semua unit test pass
- Tidak ada linting error (flake8/ESLint)
- Dokumentasi API diperbarui
- Fitur sudah di-deploy ke staging
- PO sudah melakukan acceptance testing

### 2.4.5 Sprint Simulation Walkthrough

Berikut simulasi lengkap satu Sprint (2 minggu) untuk proyek Aplikasi Kasir UMKM:

```
╔══════════════════════════════════════════════════════════════╗
║           SPRINT 1 — "Fondasi Produk UMKM"                  ║
║           Durasi: 2 minggu (14 hari)                         ║
║           Sprint Goal: User bisa login dan melihat produk    ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  HARI 1 (Senin): Sprint Planning (2 jam)                     ║
║  ─────────────────────────────────────────                   ║
║  • PO menjelaskan Sprint Goal                                ║
║  • Tim memilih 5 User Stories dari Product Backlog:          ║
║    US-01: Login dengan email [5 SP]                          ║
║    US-02: Registrasi akun pemilik UMKM [3 SP]               ║
║    US-03: Daftar produk (CRUD) [8 SP]                        ║
║    US-04: Halaman dashboard sederhana [3 SP]                 ║
║    US-05: Setup CI/CD pipeline [2 SP]                        ║
║  • Total: 21 Story Points (sesuai velocity perkiraan)        ║
║                                                              ║
║  HARI 2-9: Development (Daily Scrum setiap pagi, 15 min)     ║
║  ─────────────────────────────────────────                   ║
║  Hari 2-3: US-05 (CI/CD) + US-01 (Login backend)            ║
║  Hari 4-5: US-01 (Login frontend) + US-02 (Registrasi)      ║
║  Hari 6-7: US-03 (CRUD Produk backend + frontend)           ║
║  Hari 8-9: US-04 (Dashboard) + testing + bug fix             ║
║                                                              ║
║  HARI 10 (Jumat): Sprint Review (1 jam)                      ║
║  ─────────────────────────────────────────                   ║
║  • Demo ke stakeholder (dosen pembimbing, user pemilik UMKM) ║
║  • Feedback: "Tambah fitur search produk di Sprint 2"        ║
║  • 4 dari 5 US Done, US-03 sisa 80% (rollover ke Sprint 2)  ║
║                                                              ║
║  HARI 10 (Jumat): Sprint Retrospective (45 menit)            ║
║  ─────────────────────────────────────────                   ║
║  • What went well: CI/CD setup early, daily standup konsisten ║
║  • What to improve: Estimasi US-03 terlalu optimis           ║
║  • Action item: Breakdown story besar (>5 SP) jadi sub-tasks ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

```python
# Sprint Tracker — contoh implementasi sederhana
class SprintTracker:
    """Melacak progress Sprint."""

    def __init__(self, sprint_number: int, goal: str, duration_days: int = 14):
        self.sprint_number = sprint_number
        self.goal = goal
        self.duration_days = duration_days
        self.backlog_items = []
        self.velocity = 0

    def add_story(self, story_id: str, title: str, points: int):
        """Tambahkan User Story ke Sprint Backlog."""
        self.backlog_items.append({
            "id": story_id, "title": title,
            "points": points, "status": "To Do"
        })

    def update_status(self, story_id: str, new_status: str):
        """Update status User Story."""
        for item in self.backlog_items:
            if item["id"] == story_id:
                item["status"] = new_status
                break

    def calculate_velocity(self) -> int:
        """Hitung velocity (total SP yang Done)."""
        self.velocity = sum(
            item["points"] for item in self.backlog_items
            if item["status"] == "Done"
        )
        return self.velocity

    def burndown_report(self):
        """Tampilkan laporan sprint."""
        total_sp = sum(item["points"] for item in self.backlog_items)
        done_sp = self.calculate_velocity()
        remaining = total_sp - done_sp

        print(f"\n=== Sprint {self.sprint_number} Report ===")
        print(f"Goal: {self.goal}")
        print(f"Total SP: {total_sp} | Done: {done_sp} | Remaining: {remaining}")
        print(f"Velocity: {self.velocity} SP")
        print(f"\nBacklog Items:")
        for item in self.backlog_items:
            status_icon = {"To Do": "○", "In Progress": "◐", "Done": "●"}
            icon = status_icon.get(item["status"], "?")
            print(f"  {icon} [{item['id']}] {item['title']} "
                  f"({item['points']} SP) — {item['status']}")


# Jalankan simulasi Sprint 1
sprint = SprintTracker(1, "User bisa login dan melihat produk")
sprint.add_story("US-01", "Login dengan email", 5)
sprint.add_story("US-02", "Registrasi akun pemilik UMKM", 3)
sprint.add_story("US-03", "Daftar produk (CRUD)", 8)
sprint.add_story("US-04", "Dashboard sederhana", 3)
sprint.add_story("US-05", "Setup CI/CD pipeline", 2)

# Simulasi progress
sprint.update_status("US-01", "Done")
sprint.update_status("US-02", "Done")
sprint.update_status("US-03", "In Progress")  # Belum selesai
sprint.update_status("US-04", "Done")
sprint.update_status("US-05", "Done")

sprint.burndown_report()
```

### 2.4.6 Scrum Values

Lima values yang menjadi fondasi Scrum:

```
         ┌─────────────────┐
         │    COMMITMENT    │ → Tim berkomitmen pada Sprint Goal
         └────────┬────────┘
    ┌─────────────┼─────────────┐
    ▼             ▼             ▼
┌────────┐  ┌─────────┐  ┌─────────┐
│ FOCUS  │  │ OPENNESS│  │ RESPECT │
│        │  │         │  │         │
│ Fokus  │  │ Terbuka │  │ Hormati │
│ pada   │  │ tentang │  │ kemampu-│
│ Sprint │  │ progress│  │ an dan  │
│ Goal   │  │ & hamba-│  │ pendapat│
│        │  │ tan     │  │ rekan   │
└────────┘  └─────────┘  └─────────┘
                 │
           ┌─────┴─────┐
           │  COURAGE  │ → Berani mengambil keputusan sulit,
           │           │   berani bilang "tidak bisa"
           └───────────┘
```

---

## 2.5 Extreme Programming (XP)

### 2.5.1 Filosofi XP

**Extreme Programming** (Kent Beck, 1999) mengambil praktik-praktik engineering yang baik dan menjalankannya secara "extreme":
- Jika code review bagus → lakukan **pair programming** (review sepanjang waktu)
- Jika testing bagus → lakukan **TDD** (test dulu, baru code)
- Jika integrasi sering bagus → lakukan **continuous integration**
- Jika desain sederhana bagus → lakukan **refactoring** terus-menerus

### 2.5.2 Praktik-Praktik XP

| Praktik | Deskripsi | Tingkat Adopsi di Indonesia |
|---------|-----------|---------------------------|
| **Pair Programming** | 2 programmer, 1 komputer: driver (ketik) + navigator (review) | Sedang — lebih sering di perusahaan tech besar |
| **TDD (Test-Driven Development)** | Red → Green → Refactor: tulis test gagal, buat lulus, perbaiki | Rendah-sedang — mulai populer |
| **Continuous Integration** | Merge kode ke main branch berkali-kali sehari | Tinggi — hampir semua tim modern |
| **Refactoring** | Ubah struktur internal tanpa ubah perilaku | Sedang — sering dikorbankan saat deadline |
| **Simple Design** | YAGNI — hanya bangun yang dibutuhkan sekarang | Tinggi — terutama di startup |
| **Collective Code Ownership** | Semua developer bisa mengubah semua kode | Tinggi di tim kecil |
| **Coding Standards** | Tim sepakat aturan penulisan kode | Tinggi — PEP 8, ESLint, Prettier |
| **Planning Game** | Customer pilih scope, developer estimasi effort | Sedang — mirip Sprint Planning |
| **Small Releases** | Release kecil dan sering | Tinggi — terutama web apps |
| **On-Site Customer** | Customer (atau wakilnya) selalu available | Rendah — sulit dipraktikkan |
| **40-Hour Week** | Sustainable pace, no crunch | Rendah — masih banyak lembur di industri Indonesia |
| **Metaphor** | Tim punya bahasa bersama untuk menjelaskan sistem | Rendah |

```python
# Contoh TDD cycle di Python
# LANGKAH 1: RED — Tulis test yang gagal
def test_hitung_total_belanja():
    """Test: hitung total belanja dengan diskon."""
    assert hitung_total_belanja([
        {"nama": "Nasi Goreng", "harga": 25000, "qty": 2},
        {"nama": "Es Teh", "harga": 5000, "qty": 2},
    ], diskon_persen=10) == 54000  # (50000 + 10000) * 0.9


# LANGKAH 2: GREEN — Tulis kode minimal agar test lulus
def hitung_total_belanja(items: list, diskon_persen: float = 0) -> float:
    """Hitung total belanja dengan diskon."""
    subtotal = sum(item["harga"] * item["qty"] for item in items)
    diskon = subtotal * (diskon_persen / 100)
    return subtotal - diskon


# LANGKAH 3: REFACTOR — Perbaiki kode tanpa ubah perilaku
# (Dalam kasus ini, kode sudah cukup bersih)

# Verifikasi
result = hitung_total_belanja([
    {"nama": "Nasi Goreng", "harga": 25000, "qty": 2},
    {"nama": "Es Teh", "harga": 5000, "qty": 2},
], diskon_persen=10)
print(f"Total: Rp {result:,.0f}")  # Output: Total: Rp 54,000
assert result == 54000, "Test gagal!"
print("Test LULUS!")
```

---

## 2.6 Kanban

### 2.6.1 Asal-Usul dan Filosofi Kanban

Kanban berasal dari sistem produksi Toyota (Taiichi Ohno, 1953) — "kanban" dalam bahasa Jepang berarti "papan tanda" atau "kartu visual." Dalam konteks software, Kanban diadaptasi oleh David Anderson (2010) sebagai metode pengelolaan alur kerja (*workflow management*).

Berbeda dengan Scrum yang memiliki timeboxed sprints, Kanban fokus pada **continuous flow** — pekerjaan mengalir terus tanpa batch/sprint.

### 2.6.2 Kanban Board Visualization

```
┌──────────────┬───────────────┬───────────────┬──────────────┬──────────────┐
│   BACKLOG    │   TO DO       │ IN PROGRESS   │   REVIEW     │    DONE      │
│              │  (WIP: -)     │  (WIP: 3)     │  (WIP: 2)    │              │
├──────────────┼───────────────┼───────────────┼──────────────┼──────────────┤
│              │               │               │              │              │
│ ┌──────────┐ │ ┌───────────┐ │ ┌───────────┐ │ ┌──────────┐ │ ┌──────────┐ │
│ │ Laporan  │ │ │ Notifikasi│ │ │ API       │ │ │ Login    │ │ │ Setup    │ │
│ │ Penjual- │ │ │ WhatsApp  │ │ │ Transaksi │ │ │ Google   │ │ │ Database │ │
│ │ an       │ │ │           │ │ │ [Andi]    │ │ │ OAuth    │ │ │ [Done]   │ │
│ └──────────┘ │ └───────────┘ │ └───────────┘ │ │ [Sari]   │ │ └──────────┘ │
│              │               │               │ └──────────┘ │              │
│ ┌──────────┐ │ ┌───────────┐ │ ┌───────────┐ │              │ ┌──────────┐ │
│ │ Export   │ │ │ Dashboard │ │ │ UI Produk │ │ ┌──────────┐ │ │ CI/CD    │ │
│ │ CSV      │ │ │ Admin     │ │ │ [Sari]    │ │ │ Unit     │ │ │ Pipeline │ │
│ │          │ │ │           │ │ │           │ │ │ Test API │ │ │ [Done]   │ │
│ └──────────┘ │ └───────────┘ │ └───────────┘ │ │ [Dimas]  │ │ └──────────┘ │
│              │               │               │ └──────────┘ │              │
│ ┌──────────┐ │               │ ┌───────────┐ │              │              │
│ │ Multi-   │ │               │ │ Dockerfile│ │              │              │
│ │ bahasa   │ │               │ │ [Dimas]   │ │              │              │
│ │          │ │               │ │           │ │              │              │
│ └──────────┘ │               │ └───────────┘ │              │              │
│              │               │               │              │              │
└──────────────┴───────────────┴───────────────┴──────────────┴──────────────┘
                                 ↑ WIP = 3       ↑ WIP = 2
                              (maksimum!)      (maksimum!)
```

### 2.6.3 Prinsip Kanban

**4 Foundational Principles:**
1. **Start with what you do now** — tidak perlu revolusi, mulai dari proses yang ada
2. **Agree to pursue incremental, evolutionary change** — perubahan bertahap
3. **Respect the current process, roles, responsibilities, & titles** — tidak mengharuskan perubahan organisasi
4. **Encourage acts of leadership at all levels** — semua orang bisa memimpin improvement

**6 Core Practices:**
1. **Visualize workflow** — gunakan board (fisik atau digital: Trello, Jira)
2. **Limit Work in Progress (WIP)** — batasi jumlah item di setiap kolom
3. **Manage flow** — ukur dan optimasi lead time dan throughput
4. **Make process policies explicit** — tulis aturan yang jelas (misal: Definition of Done)
5. **Implement feedback loops** — review berkala
6. **Improve collaboratively, evolve experimentally** — perbaiki berdasarkan data

### 2.6.4 Kanban vs Scrum

| Aspek | Scrum | Kanban |
|-------|-------|--------|
| Cadence | Fixed sprint (1-4 minggu) | Continuous flow |
| Roles | PO, SM, Developers (wajib) | Tidak ada roles khusus (opsional) |
| WIP Limit | Sprint Backlog = implicit WIP | Explicit per kolom |
| Estimation | Story Points / T-shirt sizing | Tidak wajib |
| Board Reset | Board direset setiap sprint | Board mengalir terus |
| Perubahan | Tidak boleh ubah Sprint Backlog mid-sprint | Boleh ubah kapan saja |
| Metrics | Velocity (SP per sprint) | Lead time, throughput, cycle time |
| Best for | Pengembangan produk baru | Maintenance, support, ops |

```python
# Kanban Metrics Calculator
from datetime import datetime, timedelta

class KanbanMetrics:
    """Menghitung metrik Kanban."""

    def __init__(self):
        self.completed_items = []

    def add_completed_item(self, title: str, started: str, completed: str):
        """Catat item yang selesai."""
        start = datetime.strptime(started, "%Y-%m-%d")
        end = datetime.strptime(completed, "%Y-%m-%d")
        lead_time = (end - start).days
        self.completed_items.append({
            "title": title, "lead_time": lead_time,
            "started": start, "completed": end
        })

    def average_lead_time(self) -> float:
        """Rata-rata lead time (hari)."""
        if not self.completed_items:
            return 0
        return sum(i["lead_time"] for i in self.completed_items) / len(self.completed_items)

    def throughput(self, period_days: int = 7) -> float:
        """Throughput (items per periode)."""
        if not self.completed_items:
            return 0
        latest = max(i["completed"] for i in self.completed_items)
        earliest = min(i["started"] for i in self.completed_items)
        total_days = (latest - earliest).days or 1
        items_per_day = len(self.completed_items) / total_days
        return items_per_day * period_days

    def report(self):
        print(f"=== Kanban Metrics Report ===")
        print(f"Items selesai: {len(self.completed_items)}")
        print(f"Rata-rata Lead Time: {self.average_lead_time():.1f} hari")
        print(f"Throughput: {self.throughput(7):.1f} items/minggu")


# Contoh penggunaan — Tim maintenance aplikasi Kasir
metrics = KanbanMetrics()
metrics.add_completed_item("Fix bug login", "2026-04-01", "2026-04-02")
metrics.add_completed_item("Tambah filter produk", "2026-04-01", "2026-04-04")
metrics.add_completed_item("Perbaiki laporan PDF", "2026-04-03", "2026-04-07")
metrics.add_completed_item("Update API payment", "2026-04-05", "2026-04-09")
metrics.report()
```

---

## 2.7 DevOps Culture

### 2.7.1 Apa Itu DevOps?

**DevOps = Development + Operations** — sebuah kultur dan kumpulan praktik yang menjembatani pengembangan software (Dev) dengan operasi IT (Ops) untuk memperpendek siklus delivery dan meningkatkan kualitas.

```
      ┌────────────────────────────────────────────┐
      │           DEVOPS INFINITY LOOP              │
      │                                             │
      │    Plan → Code → Build → Test               │
      │      ↑                       ↓              │
      │   Monitor ← Operate ← Deploy ← Release     │
      │                                             │
      │   ◄──── DEV ────►◄──── OPS ────►           │
      │   (Continuous Integration)                  │
      │              (Continuous Delivery)           │
      │                    (Continuous Deployment)   │
      └────────────────────────────────────────────┘
```

### 2.7.2 CAMS Framework

CAMS (atau CALMS) adalah framework untuk mengevaluasi dan mengadopsi DevOps:

| Pilar | Deskripsi | Praktik Konkret |
|-------|-----------|-----------------|
| **C**ulture | Kolaborasi Dev + Ops, shared responsibility, no blame | Blameless postmortems, shared on-call |
| **A**utomation | Otomatisasi build, test, deploy, infrastructure | CI/CD pipeline, Infrastructure as Code |
| **M**easurement | Keputusan berbasis data, metrics | DORA metrics, monitoring, alerting |
| **S**haring | Knowledge sharing, transparansi | Tech talks, documentation, runbooks |

**DORA Metrics** (DevOps Research & Assessment — Google):

| Metrik | Apa yang Diukur | Target Elite |
|--------|-----------------|-------------|
| **Deployment Frequency** | Seberapa sering deploy ke production | On-demand (bisa berkali-kali per hari) |
| **Lead Time for Changes** | Dari commit sampai running di production | < 1 jam |
| **Change Failure Rate** | % deployment yang menyebabkan failure | < 5% |
| **Time to Restore Service** | Waktu recovery dari failure | < 1 jam |

> **Konteks Indonesia:** Tokopedia dan Gojek telah mengadopsi DevOps secara agresif. Tokopedia melaporkan melakukan ratusan deployment per minggu untuk berbagai microservice mereka. Sementara Bukalapak menggunakan CI/CD pipeline untuk memastikan kualitas setiap perubahan kode sebelum masuk ke production.

---

## 2.8 Perbandingan Komprehensif 8+ Model

### 2.8.1 Tabel Perbandingan Model Proses

| Aspek | Waterfall | V-Model | Iterative | Spiral | Scrum | Kanban | XP | DevOps |
|-------|-----------|---------|-----------|--------|-------|--------|----|----- ---|
| **Approach** | Sequential | Sequential + Testing | Iterative | Risk-driven | Agile/Iterative | Lean/Flow | Agile/Engineering | Culture/Practices |
| **Iterasi** | Tidak | Tidak | Ya | Ya (risk-based) | Sprint 1-4 minggu | Continuous | 1-2 minggu | Continuous |
| **Requirements** | Fixed upfront | Fixed upfront | Evolving | Evolving (per spiral) | Evolving | Evolving | Evolving | Evolving |
| **Feedback** | Di akhir | Di akhir (per V) | Per iterasi | Per spiral | Per sprint | Real-time | Per iterasi | Real-time |
| **Risk Mgmt** | Rendah | Rendah | Sedang | Tinggi | Sedang | Sedang | Sedang | Tinggi (automated) |
| **Dokumentasi** | Sangat ekstensif | Sangat ekstensif | Moderat | Moderat-tinggi | Secukupnya | Minimal | Minimal | As-needed |
| **Tim Size** | Any | Any | 5-20 | 5-50+ | 3-9 developers | Flexible | 5-12 | Cross-functional |
| **Customer Involvement** | Di awal & akhir | Di awal & akhir | Per iterasi | Per spiral | Setiap sprint | Real-time | Setiap iterasi | Continuous |

### 2.8.2 Decision Tree: Memilih Model yang Tepat

```
                        START: Memilih Model Proses
                                    │
                    ┌───────────────┴───────────────┐
                    │ Apakah requirements stabil     │
                    │ dan well-defined?              │
                    └───────┬───────────────┬───────┘
                       YA   │               │  TIDAK
                            ▼               ▼
                 ┌────────────────┐  ┌────────────────┐
                 │ Apakah proyek  │  │ Apakah tim      │
                 │ safety-critical│  │ berpengalaman   │
                 │ atau regulated?│  │ dengan Agile?   │
                 └──┬──────────┬─┘  └──┬──────────┬──┘
                 YA │          │ TIDAK  │ YA       │ TIDAK
                    ▼          ▼       ▼          ▼
              ┌──────────┐ ┌───────┐ ┌──────┐ ┌──────────┐
              │ V-Model  │ │Water- │ │Scrum │ │ Scrum +  │
              │          │ │fall   │ │atau  │ │ coaching │
              └──────────┘ └───────┘ │Kanban│ │ (mulai   │
                                     └──────┘ │ sederhana)│
                                              └──────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │ Apakah proyek besar            │
                    │ (> 50 orang) dengan risiko     │
                    │ teknis tinggi?                  │
                    └───────┬───────────────┬───────┘
                       YA   │               │  TIDAK
                            ▼               ▼
                     ┌───────────┐   ┌───────────────┐
                     │ Spiral    │   │ Apakah fokus  │
                     │ atau SAFe │   │ pada delivery │
                     │(Scaled    │   │ speed + ops?  │
                     │ Agile)    │   └──┬────────┬──┘
                     └───────────┘   YA │        │ TIDAK
                                       ▼        ▼
                                  ┌────────┐ ┌──────────┐
                                  │DevOps +│ │Scrum/XP  │
                                  │Scrum   │ │(pilih    │
                                  └────────┘ │sesuai    │
                                             │fokus)    │
                                             └──────────┘
```

> **Tips:** Dalam praktik, banyak organisasi menggunakan **hybrid model** — misalnya Scrum untuk pengembangan fitur baru, Kanban untuk maintenance dan support, dan DevOps practices (CI/CD) di semua tim. Tidak ada model yang murni satu — yang penting adalah menyesuaikan dengan konteks tim dan proyek.

---

## Studi Kasus Komprehensif: Memilih Model untuk Aplikasi UMKM Indonesia

### Konteks
Sebuah startup edtech di Jakarta mendapat kontrak dari Kementerian Koperasi dan UKM untuk membangun **"UMKM Digital"** — aplikasi mobile + web yang membantu pelaku UMKM mengelola inventori, penjualan, dan laporan keuangan sederhana.

### Karakteristik Proyek

| Aspek | Detail |
|-------|--------|
| Tim | 6 developer, 1 UI/UX designer, 1 QA |
| Timeline | 6 bulan |
| Budget | Rp 500 juta |
| Users | 10.000 UMKM di fase pilot |
| Requirements | Sebagian sudah jelas (dari riset user), sebagian akan berevolusi |
| Regulasi | Harus comply dengan regulasi data pribadi (UU PDP) |
| Stakeholders | Kementerian, pelaku UMKM, bank partner (pembayaran) |

### Analisis Pemilihan Model

**Opsi 1: Waterfall** — TIDAK cocok
- Requirements belum 100% pasti (user research masih berlanjut)
- Pelaku UMKM perlu melihat prototype untuk memberi feedback
- Timeline 6 bulan terlalu pendek untuk menunggu sampai akhir untuk testing

**Opsi 2: V-Model** — TIDAK cocok
- Overhead dokumentasi terlalu berat untuk tim kecil
- Meskipun ada aspek regulasi (UU PDP), bukan safety-critical

**Opsi 3: Spiral** — TIDAK cocok
- Tim terlalu kecil untuk overhead Spiral
- Risiko teknis moderat, bukan tinggi

**Opsi 4: Scrum + DevOps** — COCOK!
- Requirements evolving → Scrum mengakomodasi perubahan per sprint
- Tim 8 orang → pas untuk satu Scrum Team
- 6 bulan = 12 sprint (2 minggu) → cukup untuk iterasi
- Feedback berkala dari UMKM dan Kementerian via Sprint Review
- DevOps (CI/CD) untuk deployment cepat dan reliable
- Kanban board untuk bug tracking dan support post-launch

### Rencana Implementasi

```
Sprint 0 (Minggu 1-2):  Setup tech stack, CI/CD, design system
Sprint 1-3 (Bulan 1-2): Core features (login, inventori, penjualan)
Sprint 4-6 (Bulan 2-3): Laporan keuangan, integrasi bank
Sprint 7-9 (Bulan 3-4): Mobile app, testing dengan UMKM pilot
Sprint 10-11 (Bulan 5):  Feedback incorporation, performance tuning
Sprint 12 (Bulan 6):     Final UAT, security audit (UU PDP), launch
```

### Lessons Learned
1. Scrum cocok karena mengakomodasi feedback cepat dari user UMKM yang beragam
2. DevOps (CI/CD) memastikan setiap sprint menghasilkan software yang bisa di-deploy
3. Kanban digunakan post-launch untuk mengelola aliran bug reports dan feature requests
4. Aspek regulasi (UU PDP) ditangani sebagai "non-functional requirement" di setiap sprint

---

## AI Corner: AI untuk Memahami Proses SE (Level: Basic)

### 2.AI.1 Menggunakan AI untuk Memahami Model Proses

**Prompt yang Efektif:**
```
"Saya mahasiswa RPL semester 4. Jelaskan perbedaan Waterfall dan Scrum
menggunakan analogi kehidupan sehari-hari yang mudah dipahami. Berikan
contoh kasus di konteks Indonesia."
```

**Catatan:** Evaluasi apakah analogi AI akurat. Pastikan AI tidak menyederhanakan secara berlebihan.

### 2.AI.2 AI untuk Simulasi Sprint Planning

**Prompt:**
```
"Kamu adalah Product Owner untuk proyek Sistem Informasi Perpustakaan Kampus.
Buatkan Product Backlog dengan 15 User Stories, lengkap dengan Story Points
estimasi (menggunakan Fibonacci: 1, 2, 3, 5, 8, 13). Urutkan berdasarkan
prioritas bisnis."
```

**Evaluasi:** Periksa apakah AI mempertimbangkan:
- Dependencies antar stories
- Prioritas yang masuk akal (fitur dasar dulu)
- Estimasi yang realistis

### 2.AI.3 AI untuk Membandingkan Model

**Prompt:**
```
"Bandingkan Waterfall vs Scrum vs Kanban untuk skenario berikut:
- Proyek e-commerce startup dengan 5 developer dan requirements yang sering berubah
- Budget: Rp 200 juta, timeline: 4 bulan
Berikan rekomendasi model mana yang paling cocok dan alasannya."
```

### 2.AI.4 AI untuk Memahami Agile Manifesto

**Prompt:**
```
"Jelaskan 12 prinsip Agile Manifesto dengan contoh praktis yang relevan
untuk tim mahasiswa yang mengerjakan proyek akhir kuliah RPL (4 orang,
6 minggu, web app)."
```

### 2.AI.5 Batasan dan Etika Penggunaan AI

**Yang BOLEH:**
- Gunakan AI untuk memahami konsep yang sulit
- Gunakan AI sebagai sparring partner untuk diskusi
- Verifikasi jawaban AI dengan sumber referensi (Scrum Guide, Agile Manifesto)

**Yang TIDAK BOLEH:**
- Copy-paste jawaban AI langsung untuk tugas tanpa memahami
- Menganggap AI selalu benar — AI bisa salah tentang detail Scrum Guide
- Menggunakan AI saat kuis dan ujian (closed-book)

> **Prinsip Islami:** Dalam Islam, menuntut ilmu adalah ibadah. Menggunakan AI sebagai alat bantu belajar adalah baik, tetapi menyerahkan seluruh proses berpikir kepada AI sama dengan mengabaikan amanah sebagai penuntut ilmu. Pastikan Anda benar-benar memahami, bukan hanya meng-copy.

---

## Latihan Soal

### Level Dasar (C1-C2)

1. Sebutkan 4 aktivitas fundamental dalam proses perangkat lunak menurut Sommerville.
2. Jelaskan 3 kelebihan dan 3 kekurangan model Waterfall.
3. Sebutkan dan jelaskan 4 values dari Agile Manifesto.
4. Apa perbedaan antara Product Owner dan Scrum Master dalam Scrum?
5. Sebutkan 5 event dalam Scrum dan durasi time-box masing-masing.

### Level Menengah (C3-C4)

6. Sebuah rumah sakit ingin membangun Sistem Informasi Rekam Medis Elektronik. Requirements sudah fix oleh regulasi Kemenkes. Tim terdiri dari 15 developer, timeline 18 bulan. Model proses apa yang paling cocok? Jelaskan alasannya dengan merujuk pada decision tree.
7. Analisis mengapa banyak perusahaan startup di Indonesia (Gojek, Tokopedia, Traveloka) mengadopsi Scrum dibandingkan Waterfall. Kaitkan dengan 4 values Agile.
8. Buatlah contoh Sprint Backlog untuk Sprint 1 dari proyek Sistem Perpustakaan Kampus, lengkap dengan User Stories, Story Points, dan Sprint Goal.
9. Sebuah tim menggunakan Kanban untuk mengelola support tickets. Rata-rata lead time adalah 5 hari dan throughput 8 items per minggu. Jika ada 20 items baru per minggu, apa yang terjadi? Bagaimana solusinya menggunakan prinsip Kanban?
10. Bandingkan Scrum dan Kanban untuk dua skenario berikut: (a) Pengembangan fitur baru mobile app, (b) Maintenance dan bug fixing aplikasi legacy.

### Level Mahir (C5-C6)

11. Evaluasi pendekatan hybrid (Waterfall untuk fase Requirements dan Design, Agile untuk Construction dan Testing) — kapan ini cocok, apa risikonya, dan bagaimana mitigasinya?
12. Rancang proses pengembangan software yang menggabungkan Scrum + DevOps + XP practices untuk tim 6 orang yang membangun aplikasi manajemen UMKM. Jelaskan: (a) sprint duration dan mengapa, (b) XP practices mana yang diadopsi, (c) DevOps pipeline, (d) Definition of Done.
13. Sebuah bank nasional Indonesia ingin melakukan transformasi digital — memigrasikan sistem core banking dari mainframe ke microservices. Tim terdiri dari 200 developer. Evaluasi: apakah Scrum bisa di-scale? Apa alternatifnya? Bagaimana DORA metrics digunakan untuk mengukur keberhasilan?
14. Analisis kritis: "Agile telah mati" — beberapa praktisi mengatakan bahwa Agile telah kehilangan esensinya karena terlalu banyak proses dan sertifikasi. Setujukah Anda? Argumentasikan berdasarkan 12 prinsip asli Agile Manifesto.
15. Rancang model proses untuk proyek akhir mata kuliah RPL Anda (tim 4 orang, 10 minggu). Jelaskan: model yang dipilih, justifikasi, jadwal sprint, artifacts, dan metrics yang digunakan.

---

## Rangkuman

1. **Proses perangkat lunak** terdiri dari 4 aktivitas fundamental: specification, development, validation, dan evolution. Setiap model proses mengatur keempat aktivitas ini dengan cara berbeda.
2. **Model tradisional** (Waterfall, V-Model, Spiral) cocok untuk proyek dengan requirements stabil, regulasi ketat, atau risiko tinggi. Waterfall bersifat sequential, V-Model menambahkan testing paralel, dan Spiral menambahkan analisis risiko.
3. **Agile Manifesto** (2001) mengubah paradigma pengembangan software dengan 4 values yang mengutamakan individu, working software, kolaborasi pelanggan, dan respons terhadap perubahan.
4. **12 Agile Principles** memberikan pedoman praktis: delivery berkelanjutan, sambut perubahan, sustainable pace, technical excellence, dan tim self-organizing.
5. **Scrum** adalah framework Agile paling populer dengan 3 roles (PO, SM, Developers), 5 events (Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective), dan 3 artifacts (Product Backlog, Sprint Backlog, Increment).
6. **Kanban** cocok untuk continuous flow tanpa timeboxed sprint — menggunakan visualisasi board dan WIP limits untuk mengelola alur kerja.
7. **XP (Extreme Programming)** menekankan praktik engineering: TDD, pair programming, continuous integration, refactoring, dan simple design.
8. **DevOps** mengintegrasikan Development dan Operations melalui CAMS framework (Culture, Automation, Measurement, Sharing) untuk delivery yang lebih cepat dan reliable.
9. **Tidak ada model proses terbaik untuk semua situasi** — pemilihan bergantung pada stabilitas requirements, ukuran tim, tingkat risiko, regulasi industri, dan kematangan organisasi.
10. **Dalam praktik**, banyak organisasi menggunakan **hybrid approach** — misalnya Scrum untuk development, Kanban untuk maintenance, dan DevOps practices di seluruh pipeline.

---

## Referensi

1. Schwaber, K. & Sutherland, J. (2020). *The Scrum Guide: The Definitive Guide to Scrum*. Scrum.org.
2. Beck, K. et al. (2001). *Manifesto for Agile Software Development*. agilemanifesto.org.
3. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapters 2-3. Pearson.
4. Kim, G., Humble, J., Debois, P., & Willis, J. (2016). *The DevOps Handbook*. IT Revolution Press.
5. Boehm, B. W. (1988). "A Spiral Model of Software Development and Enhancement." *IEEE Computer*, 21(5), 61-72.
6. Beck, K. (1999). *Extreme Programming Explained: Embrace Change*. Addison-Wesley.
7. Anderson, D. J. (2010). *Kanban: Successful Evolutionary Change for Your Technology Business*. Blue Hole Press.
8. Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps*. IT Revolution Press.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
