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
| **Durasi** | 150 menit (3 × 50 menit) |
| **Metode** | Ceramah interaktif, simulasi Scrum mini, studi kasus |

## Tujuan Pembelajaran

1. **Membedakan** model proses tradisional (Waterfall, V-Model, Spiral) dan modern (Agile, DevOps) (C2)
2. **Menjelaskan** Agile Manifesto (4 values, 12 principles) (C2)
3. **Menjelaskan** framework Scrum: roles, events, dan artifacts (C2)
4. **Memilih** model proses yang sesuai untuk skenario proyek tertentu (C2)

## Materi Pembelajaran

### 2.1 Konsep Proses Perangkat Lunak

Proses software terdiri dari 4 aktivitas fundamental:
1. **Specification** — mendefinisikan apa yang harus dilakukan
2. **Development** — merancang dan mengimplementasikan
3. **Validation** — memastikan sesuai kebutuhan
4. **Evolution** — mengubah sesuai kebutuhan baru

### 2.2 Model Tradisional

#### Waterfall Model
```
Requirements → Design → Implementation → Testing → Deployment → Maintenance
     ↓            ↓          ↓              ↓          ↓            ↓
  (Selesai     (Selesai   (Selesai      (Selesai   (Selesai    (Ongoing)
   dulu)        dulu)      dulu)         dulu)      dulu)
```

**Kapan cocok:** Proyek dengan requirements yang stabil dan jelas (embedded systems, regulasi ketat).

#### V-Model
Setiap fase development dipasangkan dengan fase testing:
- Requirements ↔ Acceptance Testing
- System Design ↔ System Testing
- Detailed Design ↔ Integration Testing
- Coding ↔ Unit Testing

#### Spiral Model (Boehm)
Menambahkan risk analysis di setiap iterasi. Cocok untuk proyek berisiko tinggi.

### 2.3 Agile Software Development

#### Agile Manifesto — 4 Values:

| Kami menghargai... | Lebih dari... |
|-------------------|---------------|
| **Individuals and interactions** | Processes and tools |
| **Working software** | Comprehensive documentation |
| **Customer collaboration** | Contract negotiation |
| **Responding to change** | Following a plan |

#### Scrum Framework

```
Product     Sprint        Daily         Sprint      Sprint
Backlog  →  Planning  →   Standup   →   Review  →  Retrospective
   ↑           ↓          (15 min)      (Demo)     (Improve)
   │      Sprint Backlog     ↓
   │           ↓          Working
   └─── Feedback ←──── Increment (2-4 minggu)
```

**Scrum Roles:**
- **Product Owner** — mengelola backlog, mewakili stakeholder
- **Scrum Master** — memfasilitasi proses, menghilangkan hambatan
- **Development Team** — 3-9 orang, self-organizing

**Scrum Events:** Sprint Planning, Daily Standup (15 min), Sprint Review, Sprint Retrospective

**Scrum Artifacts:** Product Backlog, Sprint Backlog, Increment

### 2.4 Kanban

- **Visual Board:** To Do → In Progress → Review → Done
- **WIP Limits:** Batasi jumlah task in-progress
- **Flow:** Fokus pada continuous flow, bukan timeboxed sprints

### 2.5 DevOps Culture

```
     Plan → Code → Build → Test
       ↑                      ↓
    Monitor ← Operate ← Deploy ← Release
```

DevOps = Development + Operations — kultur kolaborasi untuk deliver software lebih cepat dan reliable.

### 2.6 Perbandingan Model

| Aspek | Waterfall | Scrum | Kanban | DevOps |
|-------|-----------|-------|--------|--------|
| Iterasi | Tidak | Sprint 2-4 minggu | Continuous | Continuous |
| Requirements | Fixed upfront | Evolving | Evolving | Evolving |
| Tim | Terpisah | Cross-functional | Flexible | Dev + Ops |
| Feedback | Di akhir | Setiap sprint | Real-time | Real-time |
| Cocok untuk | Stabil, regulasi | Sebagian besar proyek | Maintenance, support | Modern web apps |

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Membaca Agile Manifesto di [agilemanifesto.org](https://agilemanifesto.org/)
- Membaca The Scrum Guide (ringkasan 2 halaman)

### In-class (120 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-30 menit | Model tradisional: Waterfall, V-Model, Spiral | Ceramah interaktif |
| 30-60 menit | Agile Manifesto & Scrum Framework | Ceramah + video |
| 60-90 menit | **Simulasi Scrum Mini**: Sprint Planning + Daily Standup | Simulasi kelompok |
| 90-110 menit | Kanban & DevOps overview | Ceramah + diskusi |
| 110-120 menit | Diskusi: "Model mana yang cocok untuk proyek X?" | Studi kasus |

### Post-class (15 menit)
- Refleksi: Bandingkan Waterfall vs Scrum — kapan masing-masing cocok?
- Preview: Requirements Engineering minggu depan

## Referensi

1. Schwaber, K. & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org.
2. Beck, K. et al. (2001). *Manifesto for Agile Software Development*.
3. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 2-3.
4. Kim, G. et al. (2016). *The DevOps Handbook*. IT Revolution Press.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
