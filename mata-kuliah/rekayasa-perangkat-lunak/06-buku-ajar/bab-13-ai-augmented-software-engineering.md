# BAB 13: AI-AUGMENTED SOFTWARE ENGINEERING

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 7.1 | Mengevaluasi peran AI tools (Copilot, Claude Code, Cursor) dalam setiap fase SDLC | C5 (Mengevaluasi) |
| 7.2 | Menerapkan prompt engineering untuk development tasks dan mengelola AI secara bertanggung jawab | C3-C5 |

---

## 13.1 Lanskap AI Tools untuk SE (2025-2026)

### 13.1.1 Kategori AI Tools

| Kategori | Tools | Fungsi |
|----------|-------|--------|
| **Code Completion** | GitHub Copilot, Codeium | Autocomplete kode real-time |
| **AI Chat + Code** | Claude Code, ChatGPT, Cursor | Diskusi + generate kode |
| **Agentic Development** | Claude Code (agent mode), Devin, SWE-Agent | AI mengerjakan task secara mandiri |
| **Code Review** | CodeRabbit, Sourcery | Review PR otomatis |
| **Testing** | Diffblue, CodiumAI | Generate test otomatis |
| **Documentation** | Mintlify, README.ai | Generate docs dari kode |

### 13.1.2 AI di Setiap Fase SDLC

| Fase SDLC | AI Capability | Contoh |
|-----------|---------------|--------|
| Requirements | Analisis requirements, generate user stories | "Buatkan user stories dari dokumen SRS ini" |
| Design | Suggest arsitektur, generate UML | "Buatkan class diagram untuk fitur checkout" |
| Construction | Code generation, completion, refactoring | Copilot autocomplete, Claude Code implement |
| Testing | Test generation, edge case finding | "Generate pytest tests untuk class ini" |
| Deployment | CI/CD config, Dockerfile generation | "Buatkan GitHub Actions workflow" |
| Maintenance | Bug analysis, code explanation, refactoring | "Jelaskan dan refactor fungsi legacy ini" |

## 13.2 Prompt Engineering untuk Developers

### 13.2.1 Anatomy of Good Prompts

```
Konteks + Instruksi + Format + Constraints

Contoh:
"Saya membangun Sistem Perpustakaan dengan Flask + SQLAlchemy.
Buatkan REST API endpoint untuk fitur peminjaman buku.
Gunakan Flask Blueprint, return JSON, include error handling.
Jangan gunakan raw SQL — gunakan SQLAlchemy ORM saja."
```

### 13.2.2 Prompt Patterns

| Pattern | Template | Kapan Digunakan |
|---------|----------|----------------|
| **Persona** | "Kamu adalah senior Flask developer..." | Expert-level output |
| **Step-by-step** | "Jelaskan langkah demi langkah cara..." | Pemahaman proses |
| **Few-shot** | "Contoh input-output: ... Sekarang buatkan untuk..." | Pattern matching |
| **Constraint** | "Jangan gunakan..., Harus menggunakan..." | Control output |
| **Review** | "Review kode ini dari sisi security dan performance" | Code review |

### 13.2.3 Contoh Prompts per Fase

**Requirements:**
```
"Saya membangun aplikasi antrian puskesmas. Stakeholder: pasien, 
petugas, dokter, admin. Buatkan 10 functional requirements dan 
5 non-functional requirements dalam format IEEE 830."
```

**Testing:**
```
"Buatkan pytest unit tests untuk class berikut. Cover: 
happy path, edge cases (empty input, None, very large data),
dan error handling. Gunakan fixtures dan parametrize."
```

## 13.3 Agentic Development

### 13.3.1 Apa Itu Agentic Development?

Agentic development adalah paradigma di mana AI agent secara **otonom** menyelesaikan task development — bukan hanya menjawab pertanyaan, tapi mengeksekusi:
- Membaca kode
- Menulis dan mengedit file
- Menjalankan terminal commands
- Mengiterasi berdasarkan error

### 13.3.2 Claude Code sebagai AI Agent

```bash
# Claude Code bisa:
# 1. Baca dan pahami codebase
# 2. Implement fitur baru
# 3. Debug dan fix error
# 4. Jalankan tests
# 5. Commit dan push kode
```

### 13.3.3 Human-in-the-Loop

Meskipun AI agent powerful, engineer tetap harus:
- **Review** setiap output AI
- **Approve** sebelum merge ke production
- **Guide** AI dengan konteks yang tepat
- **Reject** output yang salah atau tidak sesuai

## 13.4 AI Limitations dan Hallucinations

### 13.4.1 Keterbatasan AI

| Limitasi | Deskripsi | Mitigasi |
|----------|-----------|----------|
| **Hallucination** | AI "mengkarang" API/library yang tidak ada | Selalu verifikasi di dokumentasi resmi |
| **Outdated knowledge** | Training data ada batas waktu | Cek apakah library/syntax masih valid |
| **Context window** | Tidak bisa memproses seluruh codebase besar | Berikan konteks yang relevan saja |
| **Security blind spots** | Bisa generate kode yang rentan | Manual security review tetap wajib |
| **Business logic** | Tidak memahami kebutuhan bisnis spesifik | Engineer harus specify requirements jelas |

### 13.4.2 Contoh Hallucination

```python
# AI mungkin menyarankan:
from flask_awesome_validator import validate  # Library TIDAK ADA!

# Yang benar:
from wtforms.validators import DataRequired, Email
```

## 13.5 Responsible AI Usage

### 13.5.1 AI Usage Log

| Tanggal | Task | Tool | Prompt | Output | Evaluasi |
|---------|------|------|--------|--------|----------|
| 2026-03-15 | Generate unit test | Claude | "Buatkan pytest..." | 5 test cases | 4/5 benar, 1 perlu fix edge case |
| 2026-03-16 | Refactor service | Copilot | Autocomplete | Method extraction | Sesuai, diterima |

### 13.5.2 Prinsip AI Bertanggung Jawab

1. **Transparansi** — dokumentasikan penggunaan AI (AI Usage Log)
2. **Verifikasi** — selalu review dan test output AI
3. **Pemahaman** — jangan submit kode yang tidak Anda pahami
4. **Atribusi** — jangan klaim AI output sebagai karya sendiri tanpa modifikasi
5. **Amanah** — gunakan AI untuk belajar, bukan untuk menghindari belajar

### 13.5.3 Perspektif Islam

- **Amanah dalam akademik**: Menggunakan AI untuk belajar = boleh. Menyalin tanpa pemahaman = melanggar amanah.
- **Ikhtiar**: AI adalah tool untuk memaksimalkan usaha, bukan menggantikan usaha.
- **Jujur**: Laporan AI Usage Log harus jujur dan lengkap.

---

## AI Corner: AI Integration Comprehensive (Level: Expert)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| Full feature development | "Implement fitur pencarian buku dengan autocomplete. Backend Flask, frontend vanilla JS, test with pytest" | Gunakan agentic mode jika tersedia |
| Code review with AI | "Review PR ini dari sisi: correctness, security, performance, readability, test coverage" | Bandingkan dengan review manual |
| Documentation | "Buatkan API documentation untuk semua endpoints di file routes.py ini" | Verifikasi akurasi |
| Debug complex issue | "Error ini muncul saat concurrent users > 10: [paste traceback]. Help debug." | AI bagus untuk debugging |

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Sebutkan 5 kategori AI tools untuk software engineering.
2. Jelaskan apa itu AI hallucination dan berikan contoh.
3. Apa perbedaan AI code completion dan agentic development?

### Level Menengah (C3-C4)
4. Gunakan AI untuk generate 5 unit tests untuk proyek Anda. Evaluasi: berapa yang benar? Apa yang perlu diperbaiki?
5. Tulis 3 prompt dengan teknik berbeda (persona, few-shot, constraint) untuk task yang sama: "Generate Flask API endpoint."
6. Isi AI Usage Log untuk 1 minggu penggunaan AI dalam proyek tim.

### Level Mahir (C5-C6)
7. Evaluasi: "Apakah AI developer tools akan menggantikan software engineer dalam 10 tahun?" — argumen berdasarkan bukti.
8. Rancang AI integration workflow untuk tim development 4 orang — kapan AI digunakan, kapan tidak, dan bagaimana memastikan kualitas.

---

## Rangkuman

1. **AI tools** hadir di setiap fase SDLC — dari requirements hingga maintenance.
2. **Prompt engineering** yang baik menghasilkan output AI yang lebih akurat dan useful.
3. **Agentic development** memungkinkan AI menyelesaikan task secara otonom, tapi tetap perlu human review.
4. **AI limitations** (hallucination, outdated, security blind spots) harus dipahami dan dimitigasi.
5. **Responsible AI usage** memerlukan transparansi (AI Usage Log), verifikasi, dan pemahaman.
6. **Perspektif Islam**: AI adalah tool untuk ikhtiar — gunakan dengan amanah dan kejujuran.

---

## Referensi

1. GitHub. (2024). *GitHub Copilot Documentation*. docs.github.com/copilot.
2. Anthropic. (2024). *Claude Documentation*. docs.anthropic.com.
3. Poldrack, R. A. et al. (2023). "AI-assisted coding: Experiments with GPT-4." *arXiv preprint*.
4. Vaithilingam, P. et al. (2022). "Expectation vs Experience: Evaluating the Usability of Code Generation Tools." *CHI 2022*.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
