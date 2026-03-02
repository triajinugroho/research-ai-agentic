# CLAUDE.md

> Guidelines for AI assistants working on this repository.

---

## Project Overview

This is an **educational materials repository** for three coordinated university courses in the Computer Science (Informatika) program at **Universitas Al Azhar Indonesia (UAI)**. It contains **123 Markdown documents** — lecture modules, lab guides, textbooks, assessments, and strategic analyses — for **Semester Genap 2025/2026**.

**Instructor:** Tri Aji Nugroho, S.T., M.T.

There is **no application code, no build system, no tests, and no CI/CD**. The entire repository is static Markdown content.

---

## Repository Structure

```
research-ai-agentic/
├── README.md                                    # Root overview
├── CLAUDE.md                                    # This file
└── mata kuliah/                                 # All course materials
    ├── prompt-algoritma-pemrograman.md           # Master prompt for generating course content
    │
    ├── algoritma-pemrograman/                   # INF-101: Algorithms & Programming (Theory, 2 SKS)
    │   ├── README.md
    │   ├── 00-strategic-analysis/               # SWOT, Porter's 5 Forces, AI trends
    │   ├── 01-rps/                              # Semester Learning Plan (RPS)
    │   ├── 02-rtm/                              # Student Task Plan (RTM)
    │   ├── 03-modules/                          # 16 weekly lecture modules
    │   ├── 04-assessments/                      # Assessment framework, exam specs, rubrics
    │   ├── 05-buku-ajar/                        # Textbook (14 chapters + front matter + appendices)
    │   └── datasets/                            # Resource guide
    │
    ├── praktikum-algoritma-pemrograman/         # INF-102: Programming Lab (1 SKS)
    │   ├── README.md
    │   ├── 00-pedoman-praktikum/                # Lab guidelines & rules
    │   ├── 01-rps/                              # Lab semester plan
    │   ├── 02-rtm/                              # Lab task plan
    │   ├── 03-modul-praktikum/                  # 13 lab modules (weeks 1-7, 9-14)
    │   ├── 04-assessments/                      # Rubrics, project guidelines
    │   └── datasets/                            # Dataset references
    │
    └── analisis-data-statistik/                 # Statistical Data Analysis (2 SKS)
        ├── README.md
        ├── 00-strategic-analysis/               # Strategic analysis
        ├── 01-rps/                              # Semester learning plan
        ├── 02-rtm/                              # Student task plan
        ├── 03-modules/                          # 16 weekly lecture modules
        ├── 04-labs/                             # 13 hands-on Python labs
        ├── 05-assessments/                      # Framework, rubrics, exam specs
        ├── 06-buku-ajar/                        # Textbook (14 chapters + appendices)
        └── datasets/                            # Dataset guide
```

### Three Courses

| Code    | Course                                | Credits | Type        |
|---------|---------------------------------------|---------|-------------|
| INF-101 | Algoritma dan Pemrograman             | 2 SKS   | Theory      |
| INF-102 | Praktikum Algoritma dan Pemrograman   | 1 SKS   | Lab (co-req INF-101) |
| —       | Analisis Data Statistik               | 2 SKS   | Theory + Lab |

---

## Content Conventions

### Language

- **Primary language:** Indonesian (Bahasa Indonesia)
- **Technical terms:** Bilingual (Indonesian + English)
- All new content should follow this bilingual convention

### File Naming

| Content Type        | Pattern                            | Example                                       |
|---------------------|------------------------------------|-----------------------------------------------|
| Weekly modules      | `week-NN-topic-name.md`            | `week-01-pengantar-algoritma-computational-thinking.md` |
| Lab modules         | `lab-NN-topic.md`                  | `lab-05-functions-decomposition.md`           |
| Textbook chapters   | `bab-NN-topic.md`                  | `bab-01-pengantar-algoritma-computational-thinking.md` |
| Plans               | `rps-*.md`, `rtm-*.md`            | `rps-algoritma-pemrograman.md`                |

### Folder Structure per Course

Each course follows a consistent template:
1. `00-strategic-analysis/` or `00-pedoman-praktikum/` — Strategic positioning or lab guidelines
2. `01-rps/` — Rencana Pembelajaran Semester (Semester Learning Plan)
3. `02-rtm/` — Rencana Tugas Mahasiswa (Student Task Plan)
4. `03-modules/` or `03-modul-praktikum/` — Weekly materials
5. `04-assessments/` or `04-labs/` — Assessment or lab content
6. `05-buku-ajar/` or `05-assessments/` — Textbook or assessments
7. `06-buku-ajar/` — Textbook (statistics course)
8. `datasets/` — Dataset references and resources

---

## Pedagogical Framework

Understanding these principles is critical when editing or creating content:

### OBE (Outcome-Based Education)

Every module, assignment, and assessment traces back to:
- **CPL** (Capaian Pembelajaran Lulusan) — Program Learning Outcomes
- **CPMK** (Capaian Pembelajaran Mata Kuliah) — Course Learning Outcomes (7 per course)
- **Sub-CPMK** — Weekly learning objectives

Use **Bloom's Taxonomy** verb levels (C1-C6) for all learning objectives:
- C1 (Remember): mendefinisikan, menyebutkan
- C2 (Understand): menjelaskan, membedakan
- C3 (Apply): menerapkan, mengimplementasikan
- C4 (Analyze): menganalisis, membandingkan
- C5 (Evaluate): menilai, menguji
- C6 (Create): merancang, membangun

### AI-Augmented Learning

AI tools (ChatGPT, Claude, Copilot) are integrated as **coding partners**, not replacements:
- Each textbook chapter has an **"AI Corner"** section
- AI literacy progresses: Basic (Ch 1-4) → Intermediate (Ch 5-7) → Advanced (Ch 8-11) → Expert (Ch 12-14)
- Students must maintain an **AI Usage Log** for academic integrity
- AI is **NOT** allowed during exams (UTS/UAS are closed-book)

### Islamic Values Integration

Values must be integrated **naturally**, not forced:
- **Amanah** (Trustworthiness): academic integrity, no plagiarism
- **Al-Khwarizmi Heritage**: the word "algorithm" comes from the Muslim scholar — highlight in Chapter 1
- Ethics and social responsibility in technology use

### Indonesian Context

All examples, datasets, and case studies use Indonesian context:
- BPS (Central Statistics Bureau) data
- Local scenarios (TransJakarta, e-commerce Indonesia, hospital queues)
- Indonesian problem sets and real-world data

---

## Content Structure Templates

### Textbook Chapter Structure (bab-NN-*.md)

Every chapter must contain:
1. `# BAB N: JUDUL` + author name
2. **Tujuan Pembelajaran** — table with Sub-CPMK, description, Bloom's level
3. **Numbered sections** (N.1, N.2, ...) with subsections (N.1.1, N.1.2, ...)
4. **AI Corner** — progressive AI usage guidance for the chapter's topic
5. **Latihan Soal** — exercises at 3 levels: Dasar, Menengah, Mahir
6. **Rangkuman** — key takeaways
7. **Referensi** — sources

### Weekly Module Structure (week-NN-*.md)

1. `# Minggu N: Title`
2. **Informasi Modul** — table (MK, week, topic, CPMK, duration, method)
3. **Tujuan Pembelajaran** — numbered list with Bloom's verbs
4. **Materi Pembelajaran** — detailed content with theory, examples, Python code, ASCII diagrams
5. **Kegiatan Pembelajaran** — class activities (pre-class, in-class, post-class)
6. **Penugasan** — if applicable for that week
7. **Referensi**

### Lab Module Structure (lab-NN-*.md)

1. Header with course info, duration, prerequisites
2. **Tujuan Praktikum** — what students will achieve
3. **Persiapan** — what to prepare
4. **Langkah-langkah** — step-by-step with complete Python code
5. **Tantangan Tambahan** — 2-3 extra challenges
6. **Checklist Penyelesaian** — completion checklist

---

## Consistency Rules

These rules **must** be followed across all documents:

1. **Date references:** Semester Genap 2025/2026. Publication year is **2026** (not 2025). Use "Jakarta, Februari 2026".

2. **Course name:** Always "Algoritma dan Pemrograman" in formal docs — never "Algoritma & Pemrograman" or "AlPro".

3. **Instructor name:** Always "Tri Aji Nugroho, S.T., M.T." — never abbreviated.

4. **Chapter numbering:**
   - Bab 13 = AI-Augmented Programming
   - Bab 14 = Proyek Akhir (Final Project)
   - References to "proyek akhir" must point to **Bab 14**, not Bab 13

5. **Assessment weights must total 100%:**
   - INF-101: Kuis 20% + UTS 30% + UAS 40% + Partisipasi 10%
   - INF-102: Laporan 25% + Tugas 25% + Proyek 35% + Responsi 10% + Partisipasi 5%
   - Statistik: Tugas 15% + Kuis 10% + UTS 20% + Proyek 25% + UAS 25% + Partisipasi 5%

6. **CPMK traceability:** Every Sub-CPMK in RPS must trace to a CPMK. Every textbook chapter must reference its Sub-CPMK. Every assessment must indicate which CPMK it measures.

7. **Python code:** Must be Google Colab-compatible, Python 3.x, with comments in Indonesian.

8. **AI literacy progression:** AI Corner tables must cover Bab 1-14 (not stop at Bab 13).

9. **Footer:** Every file ends with:
   ```
   *"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
   ```

---

## Tools & Technologies Referenced

| Tool                        | Purpose                           |
|-----------------------------|-----------------------------------|
| Python 3.x                  | Primary programming language      |
| Google Colab                 | Cloud IDE for all labs            |
| pandas, numpy                | Data manipulation                 |
| matplotlib, seaborn          | Data visualization                |
| scipy.stats, scikit-learn    | Statistics & basic ML             |
| ChatGPT / Claude / Copilot  | AI as learning partner            |

---

## Development Workflow

### Git Practices

- The primary branch is `master`
- Feature branches use `claude/` prefix for AI-assisted development
- Commit messages may be in Indonesian or English
- Commits should describe the content changes clearly

### Content Development

- New content is typically generated from the master prompt (`mata kuliah/prompt-algoritma-pemrograman.md`)
- Follow the batch generation order described in the prompt file for large content creation
- After creating or modifying content, verify against the consistency rules above

### What This Repository Does NOT Have

- No package manager (no `package.json`, `pyproject.toml`, etc.)
- No build system or compilation step
- No automated tests or linting
- No CI/CD pipelines
- No deployment configuration
- No application code — only educational documentation with embedded Python examples

---

## Common Tasks for AI Assistants

### Adding or Updating Course Materials

1. Follow the appropriate content structure template (textbook chapter, module, or lab)
2. Maintain CPMK traceability
3. Use Indonesian with bilingual technical terms
4. Include Indonesian-context examples and datasets
5. Ensure the footer tagline is present
6. Verify consistency rules (dates, names, chapter numbers)

### Editing Existing Content

1. Read the file first to understand its current structure
2. Preserve the established formatting patterns
3. Maintain cross-references between theory and lab materials
4. Keep assessment weight totals at 100%

### Updating README Files

1. The root `README.md` contains the overall repository structure and file counts
2. Each course has its own `README.md` with course-specific details
3. When adding files, update the relevant file count tables

### Working with the Master Prompt

The file `mata kuliah/prompt-algoritma-pemrograman.md` contains the comprehensive prompt used to generate the Algoritma dan Pemrograman course materials. It documents all specifications, anti-patterns, and verification checklists. Refer to this file for authoritative guidance on content standards.

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `README.md` | Repository overview with course listing and structure |
| `mata kuliah/prompt-algoritma-pemrograman.md` | Master prompt with full course specifications |
| `mata kuliah/algoritma-pemrograman/01-rps/rps-algoritma-pemrograman.md` | INF-101 semester learning plan |
| `mata kuliah/algoritma-pemrograman/05-buku-ajar/00-halaman-depan.md` | Textbook front matter and table of contents |
| `mata kuliah/praktikum-algoritma-pemrograman/00-pedoman-praktikum/*.md` | Lab rules and guidelines |
| `mata kuliah/analisis-data-statistik/01-rps/rps-statistika-analisis-data.md` | Statistics course semester plan |
