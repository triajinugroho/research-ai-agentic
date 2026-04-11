# Lab 14: End-to-End SE Pipeline

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 13 dari 13 (Minggu 14) — Capstone Lab |
| **Topik** | Full SDLC Pipeline, Integrasi Seluruh Artifact, Mini Retrospective, Lessons Learned, Career Roadmap |
| **CPMK** | CPMK-7 (Merancang dan membangun web application secara end-to-end, memanfaatkan AI sebagai co-developer secara bertanggung jawab) |
| **Sub-CPMK** | Sub-CPMK-7.3, Sub-CPMK-7.4 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 01-13 selesai, proyek tim mendekati tahap final |

---

## Tujuan

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. **Mendemonstrasikan** (C3) seluruh pipeline SDLC (Requirements → Design → Code → Test → Deploy) untuk satu mini-feature
2. **Mengevaluasi** (C5) kelengkapan dan keterkaitan semua artifact proyek yang telah dibuat selama 1 semester
3. **Menganalisis** (C4) proses pengembangan melalui mini retrospective (Start-Stop-Continue)
4. **Merancang** (C6) personal SE career roadmap berdasarkan pengalaman dan refleksi selama perkuliahan

---

## Konsep Singkat

### Mengapa Lab Ini Penting?

Lab ini adalah **capstone** — titik kulminasi seluruh pembelajaran selama 1 semester. Selama 13 minggu, Anda telah mempelajari setiap fase SDLC secara terpisah. Sekarang saatnya menyambungkan semua puzzle tersebut menjadi satu gambaran utuh.

```
Peta Seluruh Lab yang Telah Dilalui:

  Lab 01-02    Lab 03-04    Lab 05-06    Lab 07       Lab 09-10
  ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐
  │Intro & │   │Require-│   │Arsitek-│   │Collabo-│   │Testing │
  │Process │ → │ments   │ → │tur &   │ → │rative  │ → │& QA    │
  │Models  │   │Engine- │   │Design  │   │Coding  │   │        │
  └────────┘   │ering   │   └────────┘   └────────┘   └────────┘
               └────────┘
                                                          │
  Lab 14       Lab 13       Lab 12       Lab 11          │
  ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐      │
  │E2E     │   │AI-Aug- │   │Mainten-│   │DevOps  │      │
  │Pipeline│ ← │mented  │ ← │ance &  │ ← │& CI/CD │ ← ──┘
  │(ANDA   │   │Develop-│   │Evolut- │   │        │
  │DI SINI)│   │ment    │   │ion     │   │        │
  └────────┘   └────────┘   └────────┘   └────────┘
```

### Pipeline SDLC dalam Satu Alur

Seorang software engineer profesional harus mampu menjalankan seluruh pipeline ini untuk setiap fitur — dari requirements hingga deployment:

```
Full SDLC Pipeline:

  Requirements → Design → Implementation → Testing → Deployment → Monitoring
       │            │          │              │           │            │
  User Story    Sequence   Python Code    pytest     git push     Check logs
  + Accept.     Diagram    + Flask route  + unit     + CI/CD      + verify
  Criteria      + ERD      + template     + E2E      + merge      + working
```

### Retrospective: Start-Stop-Continue

Retrospective adalah ritual penting di Agile/Scrum — tim merefleksikan apa yang berjalan baik dan apa yang perlu diperbaiki. Format **Start-Stop-Continue** adalah salah satu yang paling sederhana:

| Kategori | Pertanyaan | Contoh |
|----------|-----------|--------|
| **Start** | Apa yang belum kita lakukan tapi sebaiknya mulai dilakukan? | "Start: menulis test sebelum code" |
| **Stop** | Apa yang kita lakukan tapi sebaiknya dihentikan? | "Stop: merge tanpa review" |
| **Continue** | Apa yang sudah berjalan baik dan perlu dilanjutkan? | "Continue: daily standup 15 menit" |

> **Referensi:** Materi lengkap tersedia di modul Minggu 14 (`week-14`) dan Bab 14 Buku Ajar.

---

## Persiapan

| Kebutuhan | Detail |
|-----------|--------|
| Repository | Repository proyek tim (dari Lab 01-13) — pastikan up-to-date |
| Codespace | Aktif dengan semua tools terinstal (Flask, pytest, dll) |
| Artifact | SRS, UML diagrams, ADR, test files, CI/CD pipeline |
| Tim | Seluruh anggota tim hadir (diskusi retrospective) |

---

## Langkah-langkah

### Langkah 1: Review Full Pipeline — Peta Artifact (15 menit)

**Mengapa:** Sebelum menambah fitur baru, kita perlu memastikan semua artifact dari lab sebelumnya terhubung dengan baik. Artifact yang terputus menandakan ada fase SDLC yang terlewat.

**Instruksi:**

Buat file `docs/artifact-map.md` yang memetakan semua deliverable proyek:

```markdown
# Peta Artifact Proyek — Sistem Perpustakaan UAI

## Checklist Kelengkapan Artifact per Fase SDLC

### 1. Requirements (Lab 03-04)
- [ ] SRS (Software Requirements Specification) → `docs/srs.md`
- [ ] User Stories (15+ stories dengan INVEST) → `docs/user-stories.md`
- [ ] Acceptance Criteria (Given-When-Then) → embedded di user stories
- [ ] Product Backlog (MoSCoW prioritization) → `docs/backlog.md`

### 2. Design (Lab 05-06)
- [ ] Architecture Decision Record (ADR) → `docs/adr/`
- [ ] Class Diagram (Mermaid) → `docs/class-diagram.md`
- [ ] Sequence Diagram (Mermaid) → `docs/sequence-diagram.md`
- [ ] ERD (Mermaid) → `docs/erd.md`
- [ ] REST API Endpoints → `docs/api-endpoints.md`

### 3. Construction (Lab 07)
- [ ] Git branching strategy → branch `develop` + `feature/*`
- [ ] Conventional commits → cek `git log --oneline`
- [ ] Code review history → cek Pull Requests di GitHub
- [ ] Refactoring evidence → commit messages tipe `refactor`

### 4. Testing (Lab 09-10)
- [ ] Unit tests → `tests/` folder
- [ ] Test coverage ≥ 70% → `coverage report`
- [ ] Test berjalan di CI → GitHub Actions log

### 5. DevOps (Lab 11)
- [ ] Dockerfile → `Dockerfile`
- [ ] CI/CD pipeline → `.github/workflows/`
- [ ] Deployment config → `Procfile` atau equivalent

### 6. AI Usage (Lab 13)
- [ ] AI Usage Log → `docs/ai-usage-log.md`
- [ ] Refleksi AI → embedded di usage log

### Status Keseluruhan
| Fase | Artifact Lengkap? | Catatan |
|------|-------------------|---------|
| Requirements | ☐ Ya / ☐ Sebagian / ☐ Belum | |
| Design | ☐ Ya / ☐ Sebagian / ☐ Belum | |
| Construction | ☐ Ya / ☐ Sebagian / ☐ Belum | |
| Testing | ☐ Ya / ☐ Sebagian / ☐ Belum | |
| DevOps | ☐ Ya / ☐ Sebagian / ☐ Belum | |
| AI Usage | ☐ Ya / ☐ Sebagian / ☐ Belum | |
```

**Aktivitas:**
1. Isi checklist di atas berdasarkan kondisi nyata repository Anda
2. Identifikasi artifact yang **BELUM ada** atau **belum lengkap**
3. Prioritaskan mana yang harus dilengkapi sebelum demo (Minggu 15)

**Diskusi tim (5 menit):**
- Artifact mana yang paling sering terlewat? Mengapa?
- Jawaban umum: Testing dan AI Usage Log sering terlewat karena dianggap "bisa nanti"

**Estimasi waktu:** 15 menit

---

### Langkah 2: Mini End-to-End Pipeline — Satu Fitur dari Requirements sampai Deploy (30 menit)

**Mengapa:** Ini adalah inti dari lab capstone — membuktikan bahwa mahasiswa bisa menjalankan seluruh pipeline SDLC secara end-to-end untuk satu fitur. Di industri, seorang engineer yang bisa handle full stack + full pipeline sangat dihargai.

**Instruksi:**

Pilih **satu mini-feature baru** yang sederhana (bisa diselesaikan dalam 30 menit). Contoh:

**Fase 1 — Requirements (3 menit):**

```markdown
## User Story
As a mahasiswa, I want melihat riwayat peminjaman saya,
so that saya bisa melacak buku yang pernah saya pinjam.

## Acceptance Criteria
Given: mahasiswa sudah login
When: mahasiswa mengakses GET /api/peminjaman/riwayat
Then: sistem menampilkan daftar peminjaman
  - Setiap item berisi: judul buku, tanggal pinjam, status
  - Diurutkan dari terbaru
  - Hanya peminjaman milik mahasiswa tersebut
```

**Fase 2 — Design (5 menit):**

Sketch Sequence Diagram (cukup di kertas atau ASCII):

```
  Mahasiswa → Controller → Service → Database
      │           │           │          │
      │  GET /api/│           │          │
      │  riwayat  │           │          │
      │──────────>│           │          │
      │           │ get_      │          │
      │           │ riwayat() │          │
      │           │──────────>│          │
      │           │           │ SELECT   │
      │           │           │ FROM     │
      │           │           │ peminja  │
      │           │           │ man WHERE│
      │           │           │ user_id= │
      │           │           │──────────>
      │           │           │ [data]   │
      │           │           │<─────────│
      │           │  [list]   │          │
      │           │<──────────│          │
      │  200 OK   │           │          │
      │  [JSON]   │           │          │
      │<──────────│           │          │
```

API Design:
- Endpoint: `GET /api/peminjaman/riwayat`
- Response: `[{judul, tanggal_pinjam, status}, ...]`
- Auth: Membutuhkan login (session/token)

**Fase 3 — Implementation (10 menit):**

```python
# Backend: app/routes/peminjaman.py
@peminjaman_bp.route('/riwayat', methods=['GET'])
@login_required
def riwayat():
    """GET /api/peminjaman/riwayat — riwayat peminjaman user."""
    # Ambil peminjaman milik user yang login, urut dari terbaru
    data = Peminjaman.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Peminjaman.tanggal_pinjam.desc()
    ).all()
    
    result = [{
        'id': p.id,
        'judul': p.buku.judul if p.buku else 'Unknown',
        'tanggal_pinjam': p.tanggal_pinjam.isoformat(),
        'tanggal_jatuh_tempo': p.tanggal_jatuh_tempo.isoformat() if p.tanggal_jatuh_tempo else None,
        'status': p.status
    } for p in data]
    
    return jsonify({
        'status': 'success',
        'count': len(result),
        'data': result
    })
```

```html
<!-- Frontend (opsional): templates/riwayat.html -->
<h1>Riwayat Peminjaman</h1>
<table id="riwayat-table">
  <tr><th>Judul</th><th>Tanggal</th><th>Status</th></tr>
</table>
<script>
fetch('/api/peminjaman/riwayat')
  .then(r => r.json())
  .then(resp => {
    const table = document.getElementById('riwayat-table');
    resp.data.forEach(p => {
      table.innerHTML += `<tr>
        <td>${p.judul}</td>
        <td>${p.tanggal_pinjam}</td>
        <td>${p.status}</td>
      </tr>`;
    });
  });
</script>
```

**Fase 4 — Testing (5 menit):**

```python
# tests/test_riwayat.py
def test_riwayat_empty(client, auth_user):
    """Riwayat kosong jika belum pernah meminjam."""
    auth_user.login()
    resp = client.get('/api/peminjaman/riwayat')
    assert resp.status_code == 200
    assert resp.json['count'] == 0
    assert resp.json['data'] == []

def test_riwayat_with_data(client, auth_user, sample_peminjaman):
    """Riwayat menampilkan data peminjaman yang ada."""
    auth_user.login()
    resp = client.get('/api/peminjaman/riwayat')
    assert resp.status_code == 200
    assert resp.json['count'] >= 1
    assert 'judul' in resp.json['data'][0]
    assert 'tanggal_pinjam' in resp.json['data'][0]
    assert 'status' in resp.json['data'][0]

def test_riwayat_unauthorized(client):
    """Riwayat tanpa login mengembalikan 401."""
    resp = client.get('/api/peminjaman/riwayat')
    assert resp.status_code == 401
```

**Fase 5 — Commit, CI/CD, Deploy (7 menit):**

```bash
# Buat feature branch
git checkout develop
git checkout -b feature/riwayat-peminjaman

# Commit bertahap
git add docs/
git commit -m "docs(riwayat): tambah user story dan API design riwayat peminjaman"

git add app/routes/peminjaman.py app/templates/riwayat.html
git commit -m "feat(riwayat): implementasi endpoint dan halaman riwayat peminjaman"

git add tests/test_riwayat.py
git commit -m "test(riwayat): tambah 3 test cases untuk endpoint riwayat"

# Push dan buat PR
git push -u origin feature/riwayat-peminjaman
# Di GitHub: Create Pull Request → develop
```

**Fase 6 — Verifikasi (3 menit):**

Verifikasi E2E:
- [ ] User story terdokumentasi
- [ ] API design ter-sketch
- [ ] Kode terimplementasi
- [ ] Test pass (`python -m pytest tests/test_riwayat.py -v`)
- [ ] CI pipeline hijau (cek GitHub Actions)
- [ ] PR dibuat dan siap di-review

**Expected Output** (endpoint berjalan):

```json
GET /api/peminjaman/riwayat

{
  "status": "success",
  "count": 2,
  "data": [
    {
      "id": 5,
      "judul": "Clean Code",
      "tanggal_pinjam": "2026-04-05T10:30:00",
      "tanggal_jatuh_tempo": "2026-04-19T10:30:00",
      "status": "dipinjam"
    },
    {
      "id": 3,
      "judul": "Design Patterns",
      "tanggal_pinjam": "2026-03-20T14:00:00",
      "tanggal_jatuh_tempo": "2026-04-03T14:00:00",
      "status": "dikembalikan"
    }
  ]
}
```

**Estimasi waktu:** 30 menit

> **Diskusi:** Dari 6 fase di atas, fase mana yang memakan waktu paling lama? Fase mana yang paling sering dilewati oleh developer di bawah tekanan deadline?

---

### Langkah 3: Mini Retrospective — Start-Stop-Continue (20 menit)

**Mengapa:** Retrospective adalah praktik inti Agile untuk continuous improvement. Tim yang tidak melakukan retrospective cenderung mengulangi kesalahan yang sama.

**Instruksi:**

Lakukan retrospective bersama tim (seluruh anggota berpartisipasi). Buat file `docs/retrospective.md`:

```markdown
# Retrospective — Sprint Final

**Tim:** [Nama tim]
**Tanggal:** [Tanggal hari ini]
**Anggota:** [Nama 1], [Nama 2], [Nama 3], [Nama 4]

## Start (Mulai lakukan)
Hal-hal yang belum kami lakukan tapi sebaiknya dilakukan:

1. ____________________________________________
2. ____________________________________________
3. ____________________________________________

## Stop (Berhenti lakukan)
Hal-hal yang kami lakukan tapi sebaiknya dihentikan:

1. ____________________________________________
2. ____________________________________________
3. ____________________________________________

## Continue (Lanjutkan)
Hal-hal yang sudah berjalan baik dan perlu dilanjutkan:

1. ____________________________________________
2. ____________________________________________
3. ____________________________________________
```

**Panduan diskusi (setiap anggota 3 menit):**

Setiap anggota menjawab 3 pertanyaan:
1. **Start:** "Apa satu hal yang menurut saya tim kita harus mulai lakukan di sprint berikutnya?"
2. **Stop:** "Apa satu hal yang menurut saya menghambat kita dan perlu dihentikan?"
3. **Continue:** "Apa satu hal yang berjalan baik dan harus kita lanjutkan?"

**Contoh jawaban yang umum muncul:**

```
START:
- Menulis test SEBELUM code (TDD), bukan test di menit terakhir
- Daily standup 10 menit setiap pagi
- Code review sebelum merge (bukan merge langsung)
- Memecah task menjadi lebih kecil (max 4 jam per task)

STOP:
- Push langsung ke main tanpa PR
- Menulis commit message yang tidak deskriptif ("fix bug", "update")
- Menunda dokumentasi sampai akhir sprint
- Bekerja 12 jam di hari terakhir deadline

CONTINUE:
- Menggunakan GitHub Projects untuk tracking task
- Standup meeting rutin
- Code review yang konstruktif (bukan sekadar "LGTM")
- Menggunakan AI tools dengan AI Usage Log
```

**Setelah semua anggota berbicara, buat 3 action items:**

```markdown
## Action Items
| No | Action | Penanggung Jawab | Deadline |
|----|--------|-----------------|----------|
| 1 | (dari Start) | (nama) | (tanggal) |
| 2 | (dari Stop) | (nama) | (tanggal) |
| 3 | (dari Continue) | (nama) | (tanggal) |
```

**Estimasi waktu:** 20 menit

---

### Langkah 4: Dokumentasi Lessons Learned (15 menit)

**Mengapa:** Lessons learned adalah pengetahuan yang diperoleh dari pengalaman — baik keberhasilan maupun kegagalan. Mendokumentasikan lessons learned membantu diri sendiri dan orang lain menghindari kesalahan yang sama di masa depan.

**Instruksi:**

Buat file `docs/lessons-learned.md`:

```markdown
# Lessons Learned — Proyek Perpustakaan UAI

**Tim:** [Nama tim]
**Semester:** Genap 2025/2026

## Teknikal

### Apa yang berjalan baik secara teknis?
- ____________________________________________
- ____________________________________________

### Apa kesalahan teknis terbesar yang kami buat?
- ____________________________________________
- Dampaknya: ____________________________________________
- Cara mencegah di proyek selanjutnya: ____________________________________________

### Tools/teknologi mana yang paling membantu?
- ____________________________________________

### Tools/teknologi mana yang paling menyulitkan?
- ____________________________________________

## Proses

### Agile/Scrum — Apakah sprint planning efektif?
- ____________________________________________

### Estimasi waktu — Seberapa akurat estimasi kami?
- ____________________________________________
- Rata-rata: overestimate / underestimate / tepat

### Komunikasi tim — Apa yang bisa diperbaiki?
- ____________________________________________

## AI Usage

### Kapan AI paling membantu?
- ____________________________________________

### Kapan AI justru menyesatkan?
- ____________________________________________

### Berapa persen kode proyek yang di-generate AI vs ditulis manual?
- AI: ___%, Manual: ___%, Mixed: ___%

## Satu Hal Terpenting yang Dipelajari
(Setiap anggota tulis satu kalimat)

- [Nama 1]: ____________________________________________
- [Nama 2]: ____________________________________________
- [Nama 3]: ____________________________________________
- [Nama 4]: ____________________________________________
```

**Aktivitas:**
1. Isi template di atas secara bersama-sama (diskusi 10 menit)
2. Setiap anggota menulis "Satu Hal Terpenting" secara individu (5 menit)

**Contoh "Satu Hal Terpenting":**

```
- Ahmad: "Software engineering bukan hanya coding — planning dan testing
  sama pentingnya."
- Siti: "Komunikasi yang jelas dalam tim menghemat lebih banyak waktu
  daripada coding lebih cepat."
- Budi: "AI membantu tapi tidak menggantikan pemahaman fundamental —
  jika tidak paham, output AI pun tidak bisa dievaluasi."
- Dewi: "Menulis test memang memakan waktu di awal, tapi menyelamatkan
  banyak waktu saat debugging."
```

**Estimasi waktu:** 15 menit

---

### Langkah 5: Personal SE Career Roadmap (20 menit)

**Mengapa:** Mata kuliah ini bukan hanya tentang mendapat nilai — tetapi mempersiapkan karir. Setiap mahasiswa perlu merefleksikan kekuatan, minat, dan area pengembangan mereka untuk membuat rencana karir yang realistis.

**Instruksi:**

Buat file pribadi `docs/career-roadmap-[nama].md`:

```markdown
# Personal SE Career Roadmap

**Nama:** ____________
**NIM:** ____________
**Tanggal:** ____________

## Self-Assessment (Evaluasi Diri)

Berikan rating 1-5 (1=pemula, 5=mahir) untuk setiap area:

| Area | Rating (1-5) | Bukti/Catatan |
|------|:------------:|---------------|
| Requirements Engineering | | |
| Software Design (UML, ERD) | | |
| Python Programming | | |
| Web Development (Flask) | | |
| Testing (pytest) | | |
| Git & Collaboration | | |
| DevOps (Docker, CI/CD) | | |
| AI-Augmented Development | | |
| Komunikasi Tim | | |
| Problem Solving | | |

## Area Terkuat (Top 3)
1. _____________ karena _____________
2. _____________ karena _____________
3. _____________ karena _____________

## Area yang Perlu Ditingkatkan (Top 3)
1. _____________ — Rencana: _____________
2. _____________ — Rencana: _____________
3. _____________ — Rencana: _____________

## Minat Spesialisasi

Dari berbagai peran SE berikut, mana yang paling menarik bagi Anda?
(Centang 1-2 yang paling diminati)

- [ ] Frontend Engineer (UI/UX, React, Vue)
- [ ] Backend Engineer (API, database, system design)
- [ ] Full-Stack Engineer (frontend + backend)
- [ ] DevOps/SRE Engineer (infrastructure, automation)
- [ ] QA/Test Engineer (testing strategy, automation)
- [ ] Data Engineer (pipeline, ETL, big data)
- [ ] Mobile Developer (Android/iOS/Flutter)
- [ ] AI/ML Engineer (model development, deployment)
- [ ] Product Manager (requirements, roadmap, stakeholder)
- [ ] Other: _____________

Alasan: _____________________________________________

## Rencana 1 Tahun ke Depan

| Timeline | Action | Target |
|----------|--------|--------|
| Semester ini (sisa) | | |
| Libur semester | | |
| Semester 5 | | |
| Libur panjang | | |
| Semester 6 | | |

## Sumber Belajar yang Direncanakan

| Sumber | Topik | Timeline |
|--------|-------|----------|
| (kursus online / buku / proyek) | | |
| | | |
| | | |

## Tren SE yang Ingin Dipelajari Lebih Lanjut

Berdasarkan modul Minggu 14 (Modern SE Trends), pilih 2 tren:

- [ ] Software Supply Chain Security (SBOM)
- [ ] Green Software Engineering
- [ ] Platform Engineering
- [ ] AI-Augmented Development (Agentic AI)
- [ ] Low-Code / No-Code Platforms
- [ ] Edge Computing
- [ ] Other: _____________

Alasan: _____________________________________________
```

**Aktivitas:**
1. Isi self-assessment berdasarkan pengalaman nyata di proyek tim (10 menit)
2. Identifikasi minat spesialisasi dan rencana 1 tahun (10 menit)

**Diskusi kelas (5 menit):**
- Sharing: apa area terkuat dan terlemah Anda setelah 1 semester?
- Apa satu hal yang akan Anda lakukan berbeda jika mengulang proyek ini dari awal?

> **Konteks Indonesia:** Industri software engineering Indonesia tumbuh pesat. Perusahaan seperti Gojek, Tokopedia, Traveloka, dan Bukalapak terus mencari talent. Skill yang paling dicari: problem solving, system design, dan kemampuan bekerja dalam tim Agile.

**Estimasi waktu:** 20 menit

---

## Tantangan Tambahan

### Tantangan 1: Dasar
Buat **presentasi 5 slide** (boleh Markdown atau tool lain) yang merangkum proyek tim Anda: (1) Problem statement, (2) Arsitektur, (3) Demo screenshot, (4) Lessons learned, (5) Tim & kontribusi. Ini bisa menjadi persiapan untuk demo Minggu 15.

### Tantangan 2: Menengah
Hitung **velocity tim** Anda berdasarkan story points yang diselesaikan per sprint. Buat grafik burn-down sederhana (ASCII atau tool apa pun). Analisis: apakah velocity konsisten? Kapan penurunan terjadi? Mengapa?

```
Contoh burn-down (ASCII):

  Story Points
  40 │ x
  35 │   x
  30 │     x
  25 │       x        Ideal
  20 │         x────── burn-down
  15 │           x
  10 │        x    x   Aktual (ada "naik"
   5 │               x  saat scope berubah)
   0 │─────────────────x──
     Sprint1  Sprint2  Sprint3  Sprint4
```

### Tantangan 3: Lanjutan
Tulis **blog post** (500-800 kata) tentang pengalaman Anda mengembangkan proyek perpustakaan menggunakan Agile/Scrum selama 1 semester. Targetkan untuk portfolio pribadi (LinkedIn atau blog). Simpan di `docs/blog-post.md`. Topik yang bisa dibahas: tantangan tim, peran AI, TDD experience, deployment, dll.

---

## Refleksi & AI Usage Log

Ini adalah lab terakhir — refleksi kali ini mencakup seluruh semester:

**Pertanyaan refleksi akhir:**

1. **Dari seluruh 13 lab, lab mana yang paling berkesan dan paling banyak mengajarkan Anda? Mengapa?**
2. **Jika Anda memulai proyek dari awal lagi, apa 3 hal yang akan Anda lakukan berbeda?**
3. **Bagaimana pemahaman Anda tentang "software engineering" berubah dari Minggu 1 hingga sekarang?**
4. **Bagaimana nilai-nilai amanah dan tanggung jawab (Islamic values) tercermin dalam proses pengembangan software yang Anda jalani?**
5. **Apa rencana Anda untuk terus mengembangkan skill SE setelah semester ini berakhir?**

Jika menggunakan AI selama lab, catat di **AI Usage Log**:

| Prompt yang Diberikan | Output AI | Modifikasi yang Dilakukan | Refleksi |
|----------------------|-----------|--------------------------|----------|
| (contoh prompt) | (ringkasan output) | (apa yang diubah) | (apa yang dipelajari) |

---

## Checklist Penyelesaian

- [ ] Peta artifact (`docs/artifact-map.md`) terisi dengan status kelengkapan per fase SDLC
- [ ] Mini E2E pipeline berhasil dijalankan (requirement → design → code → test → PR) untuk 1 fitur
- [ ] Retrospective Start-Stop-Continue dilakukan bersama tim dengan 3+ action items
- [ ] Lessons learned terdokumentasi (`docs/lessons-learned.md`)
- [ ] Personal career roadmap tertulis (`docs/career-roadmap-[nama].md`) dengan self-assessment dan rencana 1 tahun
- [ ] Refleksi akhir semester (5 pertanyaan) dijawab
- [ ] Semua file di-commit ke repository

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
