# CLAUDE.md

> Guidelines for AI assistants working on this repository.

---

## Project Overview

This is an **educational materials repository** for courses in the Computer Science (Informatika) program at **Universitas Al Azhar Indonesia (UAI)**. The materials are organized **per curriculum semester** following the **Kurikulum Informatika 2025 Revisi 2026**, whose official registry is transcribed in `mata-kuliah/00-kurikulum-if-2025-revisi-2026/`.

- **567 Markdown documents** under `mata-kuliah/` (count as of 9 October 2026 — recount with `find mata-kuliah -name '*.md' | wc -l` before quoting a number).
- **10 course folders:** 8 active courses in `mata-kuliah/semester-N/` (placed by their registry semester) and 2 old-curriculum courses in `mata-kuliah/arsip/`.
- **Reference layers:** the curriculum registry (`mata-kuliah/00-kurikulum-if-2025-revisi-2026/`), the internal OBE guidelines and registries (`mata-kuliah/00-pedoman-obe/`), and repository meta documents (`mata-kuliah/00-meta/`: execution checklist, lecturer review list, audits, and generation prompts).

**Author of all materials (*penyusun materi*):** Tri Aji Nugroho, S.T., M.T. — for **every** course in this repository, including courses whose registry instructor (*pengampu*) is someone else:

| Course | Penyusun materi | Pengampu (registri) |
|---|---|---|
| Rekayasa Perangkat Lunak (`IF52520011`) | Tri Aji Nugroho, S.T., M.T. | Dr. Ir. Winangsari Pradani, M.T. |
| Metodologi Penelitian (`IF52510021`) | Tri Aji Nugroho, S.T., M.T. | Andi Arniaty Arsyad, Ph.D. |

For all other active courses the registry *pengampu* is also Tri Aji Nugroho, S.T., M.T.

The content is static Markdown plus **one interactive HTML module**, `mata-kuliah/semester-2/analisis-data-statistik/03-modules/regresi-berganda.html` (self-contained page with an inline `<script>`; not counted in the Markdown total and not scanned by the validator). The only script/tool is `tools/validasi-obe.py`, a dependency-free consistency validator. There is **no application code, no build system, no automated test suite, and no CI/CD**.

---

## Execution Control (read first)

`mata-kuliah/00-meta/KENDALI-EKSEKUSI.md` is the **single living checklist** of open work: deadlines anchored to lecture weeks (Mg), pending lecturer decisions (`D-xx`), formal documents to collect (`F-xx`), and the evidence for finished items. The audit report (`mata-kuliah/00-meta/AUDIT-MENYELURUH-2026-10.md`) is the reference for *findings*; the *status of audit findings and work items* lives only in the control file (dated notes in `91`, `konversi-nilai.md` §B and Pedoman §J/§K record the status of those documents themselves).

In every session:

1. **Read the control file before starting.** If the request matches an item, cite its ID (e.g., `T0-09`). Without a specific request, propose the open item with the nearest deadline that is not ⏸.
2. **Respect dependencies.** Do not carry out an item whose "Butuh" column names an undecided `D-xx`; ask the lecturer, or do only the part that does not depend on the decision.
3. **Close the loop.** After finishing, set the status to ☑ with the short commit hash or date, update `diperbarui:`, and record a decision (date + content) in §1 when the lecturer makes one. Add newly found open items with the next free ID in the right stage — never renumber. Keep the file ≤ 180 lines (`tipe: mutu`, validator V11); summarize finished batches in §7, one line each.
4. **The repository is public.** Decision `D-08` (8–9 October 2026, partial): **practice papers** for UTS and UAS may be published — `05-assessments/latihan-uts.md` / `latihan-uas.md`, `latihan-uts-pembahasan.md` / `latihan-uas-pembahasan.md` (worked solutions and scoring guide) and `latihan-uts-cetak-biru.md` / `latihan-uas-cetak-biru.md` (item blueprint and variant guide). The **real** UTS/UAS papers are generated separately as **variants** of the practice paper (same blueprint: Sub-CPMK, Bloom level, points, duration; new context, data and numbers) and, like quiz papers, answer keys, question banks and per-student grades, are **never committed**. The rest of `D-08` (private storage location, quizzes, the three UTS + answer-key pairs already committed for Genap 2025/2026) is still open.

---

## Repository Structure

**Path convention in this file:** paths are relative to the repository root (`mata-kuliah/00-…`, `mata-kuliah/semester-N/…`), so they can be checked with `test -e` from the root. Three shorthands are used where the base is stated or obvious: (a) in tables with a "Folder (under `mata-kuliah/`)" column, in the Placement & Authorship Rules, and wherever "under `mata-kuliah/`" is stated, `semester-N/…` and `arsip/…` are relative to `mata-kuliah/`; (b) bare registry file names (`11-susunan-mata-kuliah-dan-dosen.md`, `13-…`, `14-…`, `15-…`, `15a`–`15e`) are files in `mata-kuliah/00-kurikulum-if-2025-revisi-2026/`, and bare Pedoman file names (`pedoman-obe-konvensi.md`, `konversi-nilai.md`) are in `mata-kuliah/00-pedoman-obe/`; (c) course subfolders and files (`01-rps/`, `00-halaman-depan.md`, …) are relative to the course folder.

```
research-ai-agentic/
├── README.md                                 # Root overview: course list, structure, total file count
├── CLAUDE.md                                 # This file
├── tools/
│   ├── validasi-obe.py                       # OBE consistency validator (rules V1–V13), pure Python
│   └── validasi-obe-baseline.json            # Accepted legacy violations (for --baseline)
└── mata-kuliah/
    ├── 00-kurikulum-if-2025-revisi-2026/     # Official curriculum registry (Markdown transcription of
    │                                         #   Revisi_2026_Kurikulum_OBE_IF_2025_2.xlsx): profil lulusan,
    │                                         #   CPL, bahan kajian, course list & lecturers (11), CPMK (13),
    │                                         #   Sub-CPMK (15, 15b–15e), assessment weights (15a)
    ├── 00-pedoman-obe/                       # Internal OBE guidelines & registries: pedoman-obe-konvensi.md,
    │                                         #   konversi-nilai.md (grade scale), cpl-master.md,
    │                                         #   taksonomi-cap.md, checklist-verifikasi.md,
    │                                         #   migrasi/ (Sub-CPMK code migration table for INF-101)
    ├── 00-meta/
    │   ├── README.md                         # Index of the meta documents and their status
    │   ├── KENDALI-EKSEKUSI.md               # Living execution checklist (status, deadlines, decisions) — read first
    │   ├── TINJAUAN-DOSEN-2026-10.md         # Agent choices awaiting lecturer approval (TD-01 …), Oct 2026
    │   ├── AUDIT-MENYELURUH-2026-10.md       # Full repository audit, October 2026 (findings reference)
    │   ├── AUDIT-KESELARASAN-IF2205-IF2206.md    # Historical IF2205 × IF2206 alignment audit
    │   ├── prompt-algoritma-pemrograman.md       # Master prompt (Algoritma dan Pemrograman) — flagged outdated
    │   └── prompt-paket-mata-kuliah-informatika.md   # Generic course-package prompt — flagged outdated
    │
    ├── semester-1/                           # Ganjil
    │   ├── README.md                         # Semester course map (all registry MK, SKS, pengampu)
    │   └── probabilitas-dan-statistik/       # IF52510033
    ├── semester-2/                           # Genap
    │   ├── README.md
    │   ├── algoritma-pemrograman/            # IF52520004 (formerly INF-101)
    │   ├── praktikum-algoritma-pemrograman/  # IF52520005 (formerly INF-102)
    │   └── analisis-data-statistik/          # IF52520025 (formerly IF2XXX in the materials,
    │                                         #   TBD-STAT in Pedoman OBE / 91 §2.1; 2 → 3 SKS)
    ├── semester-3/                           # Ganjil — README.md only (no course material yet)
    ├── semester-4/                           # Genap
    │   ├── README.md
    │   └── rekayasa-perangkat-lunak/         # IF52520011 (formerly IF2205)
    │                                         #   penyusun materi: Tri Aji Nugroho, S.T., M.T.
    │                                         #   pengampu (registri): Dr. Ir. Winangsari Pradani, M.T.
    ├── semester-5/                           # Ganjil
    │   ├── README.md
    │   ├── dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/   # IF52510031
    │   └── teknopreneur/                     # ST52510002
    ├── semester-6/                           # Genap — README.md only
    ├── semester-7/                           # Ganjil
    │   ├── README.md
    │   └── metodologi-penelitian/            # IF52510021 — pengampu (registri): Andi Arniaty Arsyad, Ph.D.
    ├── semester-8/                           # Genap — README.md only
    └── arsip/                                # Old-curriculum courses with no active counterpart
        ├── README.md                         # Archive contents, reasons, content-bank mapping, rules
        ├── kecerdasan-buatan-machine-learning/   # IF3XXX (4 SKS) — superseded by IF52510031
        └── praktikum-rekayasa-perangkat-lunak/   # IF2206 (1 SKS) — not in the new curriculum
```

Odd curriculum semesters (1, 3, 5, 7) run in the **Semester Ganjil** of the academic year; even ones (2, 4, 6, 8) in the **Semester Genap**.

### Courses

**Active courses** (placed by registry semester; registry data from `mata-kuliah/00-kurikulum-if-2025-revisi-2026/11-susunan-mata-kuliah-dan-dosen.md`):

| Folder (under `mata-kuliah/`) | Official code | Course (registry name) | SKS (registry) | Curriculum semester | Former code | Pengampu (registri), if not the author | Materials written for |
|---|---|---|---|---|---|---|---|
| `semester-1/probabilitas-dan-statistik/` | `IF52510033` | Probabilitas dan Statistik | 3 | 1 (Ganjil) | — | — | Kurikulum 2025 Rev. 2026 (Ganjil 2026/2027) |
| `semester-2/algoritma-pemrograman/` | `IF52520004` | Algoritma Pemrograman | 2 | 2 (Genap) | INF-101 | — | Old curriculum (Genap 2025/2026) |
| `semester-2/praktikum-algoritma-pemrograman/` | `IF52520005` | Praktikum Algoritma Pemrograman | 1 | 2 (Genap) | INF-102 | — | Old curriculum (Genap 2025/2026) |
| `semester-2/analisis-data-statistik/` | `IF52520025` | Analisis Data Statistik | 3 (materials: 2) | 2 (Genap) | `IF2XXX` in the materials (`TBD-STAT` in Pedoman OBE / `91` §2.1) | — | Old curriculum (Genap 2025/2026) |
| `semester-4/rekayasa-perangkat-lunak/` | `IF52520011` | Rekayasa Perangkat Lunak | 3 | 4 (Genap) | IF2205 | **Dr. Ir. Winangsari Pradani, M.T.** | Old curriculum (Genap 2025/2026) |
| `semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/` | `IF52510031` | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin | 3 | 5 (Ganjil) | — | — | Kurikulum 2025 Rev. 2026 (Ganjil 2026/2027) |
| `semester-5/teknopreneur/` | `ST52510002` | Teknopreneur | 3 | 5 (Ganjil) | — | — | Kurikulum 2025 Rev. 2026 (Ganjil 2026/2027) |
| `semester-7/metodologi-penelitian/` | `IF52510021` | Metodologi Penelitian | 2 | 7 (Ganjil) | — | **Andi Arniaty Arsyad, Ph.D.** | Kurikulum 2025 Rev. 2026 (Ganjil 2026/2027) |

**Archived courses** (old curriculum, no active counterpart — see `mata-kuliah/arsip/README.md`):

| Folder (under `mata-kuliah/`) | Former code | Course | SKS (old) | Status |
|---|---|---|---|---|
| `arsip/kecerdasan-buatan-machine-learning/` | IF3XXX | Kecerdasan Buatan dan Machine Learning | 4 | Superseded by `IF52510031` (semester 5), which has its own new materials; kept as a content bank |
| `arsip/praktikum-rekayasa-perangkat-lunak/` | IF2206 | Praktikum Rekayasa Perangkat Lunak | 1 | Not in the new curriculum; fate pending a prodi decision |

Materials written for the old curriculum (semester-2 courses, Rekayasa Perangkat Lunak, and `arsip/`) still use the old scheme — local `CPMK-1` … `CPMK-7`, old course codes, old assessment weights. Courses in `semester-N/` must be aligned with the registry before they are used under the new curriculum (see the semester READMEs, `mata-kuliah/00-kurikulum-if-2025-revisi-2026/91-validasi-dan-catatan-dampak.md` §2, and `mata-kuliah/00-meta/AUDIT-MENYELURUH-2026-10.md`).

---

## Placement & Authorship Rules

1. **New course → `mata-kuliah/semester-N/<slug>/`**, where N is the course's semester in the registry (`11-susunan-mata-kuliah-dan-dosen.md`) and `<slug>` is the registry course name in lowercase kebab-case (e.g., `rekayasa-perangkat-lunak`, `dasar-kecerdasan-artifisial-dan-pembelajaran-mesin`). Then update `semester-N/README.md` and the root `README.md`.
2. **Old-curriculum course without a counterpart → `mata-kuliah/arsip/<slug>/`**, recorded in `arsip/README.md` (old code, SKS, file count, reason, successor). An old course whose successor has separately written materials is also archived (IF3XXX → `IF52510031`). An old course that maps directly onto a registry course goes to that course's `semester-N/` folder (INF-101 → `semester-2/algoritma-pemrograman/`, IF2205 → `semester-4/rekayasa-perangkat-lunak/`).
3. **Do not develop new material inside `arsip/`.** To reuse archived content, copy the needed part into the target course in `semester-N/` and align it with that course's RPS, CPMK and Sub-CPMK.
4. **No course folders directly under `mata-kuliah/`.** The `00-*` folders are reference layers only. Semester folders without materials keep only their `README.md`.
5. **Moving files:** use `git mv` to keep history, then fix every relative link from the file's new location (cross-course links now go through `../semester-N/…` or `../arsip/…`).
6. **Authorship (penyusun vs. pengampu):** every material in this repository is authored by **Tri Aji Nugroho, S.T., M.T.** (*penyusun materi*). The registry *pengampu* may differ. When it differs, state both explicitly and never replace one with the other — for Rekayasa Perangkat Lunak: *"Penyusun materi: Tri Aji Nugroho, S.T., M.T.; Pengampu (registri): Dr. Ir. Winangsari Pradani, M.T."* Semester READMEs carry a "Penyusun materi" note, and course tables use a "Pengampu (registri)" column (see `mata-kuliah/semester-4/README.md`).

---

## Sources of Truth

| Topic | Authoritative source |
|---|---|
| Course list, official codes, SKS, semester, registry *pengampu* | `mata-kuliah/00-kurikulum-if-2025-revisi-2026/11-susunan-mata-kuliah-dan-dosen.md` |
| CPL, CPMK (program-level) | `mata-kuliah/00-kurikulum-if-2025-revisi-2026/03-cpl-prodi.md`, `13-cpmk-master.md`, `14-pemetaan-cpl-mk-cpmk.md` |
| Sub-CPMK, indicators, criteria per course | `mata-kuliah/00-kurikulum-if-2025-revisi-2026/15-pemetaan-mk-cpmk-subcpmk.md`, `15b`–`15e` |
| Assessment weights per course (new-curriculum codes) | `mata-kuliah/00-kurikulum-if-2025-revisi-2026/15a-rekap-bobot-penilaian.md` |
| AI integration per course | `mata-kuliah/00-kurikulum-if-2025-revisi-2026/14a-ai-curriculum-infusion-matrix.md` |
| Grade conversion scale (all courses) | `mata-kuliah/00-pedoman-obe/konversi-nilai.md` |
| Repository conventions (metadata, codes, footer, consistency and validation rules) | `mata-kuliah/00-pedoman-obe/pedoman-obe-konvensi.md` |

- `pedoman-obe-konvensi.md` states that it prevails over `CLAUDE.md` and the `prompt-*.md` files on conventions; the registry README states that the registry prevails over existing course materials. The two still differ on some codes (bahan kajian, CPMK model, Sub-CPMK format, assessment codes). The order of authority is an open decision for the lecturer (`mata-kuliah/00-meta/AUDIT-MENYELURUH-2026-10.md` §7.1 and §9) — do not resolve it silently; follow what the target course's RPS already uses and flag the conflict.
- **Registry sheet transcriptions** — the files numbered `00` to `16` in `mata-kuliah/00-kurikulum-if-2025-revisi-2026/`, including `06a`, `14a` and `15a`–`15e` (`14a` is a sheet transcription even though the registry README lists it under "Arah pengembangan dan catatan kerja") — transcribe the official Excel file: do not edit their content. Report internal discrepancies instead (audit §7.3). They change only through a full re-extraction (registry README, "Cara Memperbarui").
- **Registry working notes** — `90-ringkasan-mk-pengampu-tri-aji-nugroho.md` (a quick-reference summary compiled from the transcription files; registry README: "Lembar acuan cepat") and `91-validasi-dan-catatan-dampak.md` (header: "Analisis turunan — bukan transkripsi sheet") — are not part of the official document. Keep them up to date with the repository's state (folder paths, the old → new course mapping in `91` §2.1, impact notes), adding a dated update note as the 2026-10-07 update in `91` §2 does. The registry `README.md` (folder index) is likewise maintained.

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
| Course folders      | `semester-N/<slug>/` or `arsip/<slug>/` | `semester-4/rekayasa-perangkat-lunak/`   |

### Folder Structure per Course

Each course folder (`mata-kuliah/semester-N/<slug>/` or `mata-kuliah/arsip/<slug>/`) follows a consistent template (Pedoman OBE §D):

1. `README.md` — course overview
2. `00-strategic-analysis/` (theory courses) or `00-pedoman-praktikum/` (lab courses) — strategic positioning or lab guidelines
3. `01-rps/` — Rencana Pembelajaran Semester (Semester Learning Plan)
4. `02-rtm/` — Rencana Tugas Mahasiswa (Student Task Plan)
5. `03-modules/` (theory) or `03-modul-praktikum/` (lab) — weekly materials
6. `04-labs/` (most theory courses) or `04-assessments/` (`algoritma-pemrograman` and the lab courses)
7. `05-assessments/` (courses with `04-labs/`) or `05-buku-ajar/` (`algoritma-pemrograman` only)
8. `06-buku-ajar/` — textbook (every theory course except `algoritma-pemrograman`)
9. `mutu/` — quality documents (Pedoman OBE §F; currently only `algoritma-pemrograman`)
10. `datasets/` — dataset references and resources

---

## Pedagogical Framework

Understanding these principles is critical when editing or creating content:

### OBE (Outcome-Based Education)

Every module, assignment, and assessment traces back to:
- **CPL** (Capaian Pembelajaran Lulusan) — Program Learning Outcomes
- **CPMK** (Capaian Pembelajaran Mata Kuliah) — Course Learning Outcomes:
  - **New-curriculum courses:** program-level CPMK shared across courses (26 CPMK for 11 CPL, codes such as `CPMK032`), assigned per course in `14-pemetaan-cpl-mk-cpmk.md`; courses differ at the Sub-CPMK level
  - **Old-curriculum materials:** 7 local CPMK per course (`CPMK-1` … `CPMK-7`)
- **Sub-CPMK** — Weekly learning objectives (new-curriculum courses: taken verbatim from the registry, `15-pemetaan-mk-cpmk-subcpmk.md` and `15b`–`15e`)

Use **Bloom's Taxonomy** verb levels (C1-C6) for all learning objectives (cognitive, affective and psychomotor levels: `mata-kuliah/00-kurikulum-if-2025-revisi-2026/16-taksonomi-bloom-cap.md`, `mata-kuliah/00-pedoman-obe/taksonomi-cap.md`):
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

These rules **must** be followed across all documents. Where a rule here and `mata-kuliah/00-pedoman-obe/pedoman-obe-konvensi.md` differ, the Pedoman prevails — with one explicit exception: the **date scoping in rule 1** applies even though Pedoman §I.1 still states "Semester Genap 2025/2026 … Jakarta, Februari 2026" without condition. §I.1 was written for the Genap 2025/2026 package and has not yet been updated for courses of other semesters (its `berlaku_untuk` already includes IF3XXX, a Ganjil 2026/2027 course dated "Agustus 2026"). Until §I.1 is updated, do not use it to change another course's dates to "Februari 2026".

1. **Date references:** Materials written for **Semester Genap 2025/2026** (Algoritma dan Pemrograman/INF-101, Praktikum Algoritma dan Pemrograman/INF-102, Analisis Data Statistik, Rekayasa Perangkat Lunak/IF2205, Praktikum Rekayasa Perangkat Lunak/IF2206) use publication year **2026** (not 2025) and "Jakarta, Februari 2026" (Pedoman OBE §I.1). This date applies **only** to those materials: for other courses, follow the academic year and date already used in that course's RPS and textbook front matter (`00-halaman-depan.md`), and do not copy "Februari 2026" into them.

2. **Course name:** Use the full formal name, never an abbreviation. Materials in `semester-2/algoritma-pemrograman/` use "Algoritma dan Pemrograman" — never "Algoritma & Pemrograman" or "AlPro". The registry name of `IF52520004` is "Algoritma Pemrograman"; registry-facing tables (e.g., semester READMEs) use the registry name.

3. **Names:** The author's name is always "Tri Aji Nugroho, S.T., M.T." — never abbreviated. Other lecturers' names are written exactly as in registry sheet 11 (e.g., "Dr. Ir. Winangsari Pradani, M.T."). Author vs. registry *pengampu*: see Placement & Authorship Rules, item 6.

4. **Chapter numbering:**
   - Bab 13 = AI-Augmented Programming (Algoritma dan Pemrograman)
   - Bab 14 = Proyek Akhir (Final Project)
   - References to "proyek akhir" must point to **Bab 14**, not Bab 13
   - Each textbook's own table of contents (`00-halaman-depan.md`) is the reference for chapter titles (e.g., Bab 14 of Metodologi Penelitian is the research proposal)

5. **Assessment weights must total 100%:**
   - **Courses with an official code (new curriculum):** the authoritative weights of the six assessment techniques (Partisipasi, Kuis, Observasi, Unjuk Kerja, UTS, UAS) for each course are in `mata-kuliah/00-kurikulum-if-2025-revisi-2026/15a-rekap-bobot-penilaian.md`. Use them when writing or aligning any course — do not copy the legacy schemes below into new-curriculum materials.
   - **Legacy schemes still written in the old-curriculum materials** (valid only for those materials as they currently stand, until they are aligned):
     - Algoritma dan Pemrograman (INF-101): Kuis 20% + UTS 30% + UAS 40% + Partisipasi 10%
     - Praktikum Algoritma dan Pemrograman (INF-102): Laporan 25% + Tugas 25% + Proyek 35% + Responsi 10% + Partisipasi 5%
     - Analisis Data Statistik (`IF2XXX`, old, 2 SKS): Tugas 15% + Kuis 10% + UTS 20% + Proyek 25% + UAS 25% + Partisipasi 5%
     - Rekayasa Perangkat Lunak (IF2205): Tugas 15% + Kuis 10% + UTS 20% + Proyek 25% + UAS 25% + Partisipasi 5%
     - Archived AI/ML (IF3XXX): Tugas 15% + Kuis 10% + UTS 20% + Proyek 25% + UAS 25% + Partisipasi 5%
     - Archived Praktikum RPL (IF2206): Laporan 25% + Tugas 25% + Proyek 35% + Responsi 10% + Partisipasi 5%

6. **Grade conversion scale:** defined **only** in `mata-kuliah/00-pedoman-obe/konversi-nilai.md` — official UAI scale: A ≥ 81,00; nine letters (A, A−, B+, B, B−, C+, C, D, E); pass mark C (55,00). The "Konversi Nilai" section of every RPS and assessment framework copies its §A table verbatim and links to it. Enforced by validator rule V13.

7. **CPMK traceability:** Every Sub-CPMK in RPS must trace to a CPMK. Every textbook chapter must reference its Sub-CPMK. Every assessment must indicate which CPMK it measures.

8. **Python code:** Must be Google Colab-compatible, Python 3.x, with comments in Indonesian.

9. **AI literacy progression:** AI Corner tables must cover Bab 1-14 (not stop at Bab 13).

10. **Footer:** Every Markdown file under `mata-kuliah/` ends with (validator rule V8):
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
| scipy.stats, scikit-learn    | Statistics & machine learning     |
| TensorFlow/Keras             | Deep learning framework           |
| NLTK                         | NLP preprocessing                 |
| OpenCV                       | Computer vision                   |
| ChatGPT / Claude / Copilot  | AI as learning partner            |

---

## Development Workflow

### Git Practices

- The primary branch is `main`
- Feature branches use `claude/` prefix for AI-assisted development
- Commit messages may be in Indonesian or English
- Commits should describe the content changes clearly

### Content Development

- New-curriculum courses are built directly from the registry: Sub-CPMK, indicators, criteria and assessment weights are taken verbatim from `mata-kuliah/00-kurikulum-if-2025-revisi-2026/`
- Earlier content was generated from the prompts in `mata-kuliah/00-meta/`; both prompts are flagged outdated (see "Working with the Generation Prompts")
- After creating or modifying content, verify against the consistency rules above and run the validator

### Validation

Run from the repository root:

```
python3 tools/validasi-obe.py                # whole repository
python3 tools/validasi-obe.py --mk INF-101   # one course, by kode_mk in its RPS front-matter
python3 tools/validasi-obe.py --baseline tools/validasi-obe-baseline.json   # only violations NOT in the baseline
python3 tools/validasi-obe.py --help         # usage, rule list V1–V13, exit codes
```

- Checks every `mata-kuliah/**/*.md` against rules V1–V13 (Pedoman OBE §Q): V1 front-matter, V2 unique `id`, V3 referential integrity, V4 old code patterns, V5 coverage, V6 weights = 100%, V7 master data (SKS only in RPS), V8 footer tagline, V9 revoked regulation citations, V10 relative links (links inside fenced code blocks and inline code are ignored; `#anchor` fragments are **not** checked), V11 size caps, V12 approval status, V13 grade scale vs. `konversi-nilai.md`.
- Exit codes: 0 = no violation (with `--baseline`: no *new* violation), 1 = violations found, 2 = usage error (unknown option, missing value, unreadable or malformed baseline).
- The baseline is **not clean** — 832 violations as of 8 October 2026 (V1 518, V4 253, V8 60, V10 1):
  - **V1 (no front-matter):** most files outside `mata-kuliah/semester-2/algoritma-pemrograman/` and `mata-kuliah/00-pedoman-obe/` have none — including the **new-curriculum course folders** under `mata-kuliah/` (`semester-1/probabilitas-dan-statistik/`, `semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/`, `semester-5/teknopreneur/`, `semester-7/metodologi-penelitian/`; about 228 V1 findings as of 7 October 2026) and the registry (`mata-kuliah/00-kurikulum-if-2025-revisi-2026/`, 26 files). A V1 finding on these files is baseline, not a new violation — and these folders are **not** validator-clean.
  - **V4/V8/V10:** old-curriculum folders also carry these legacy findings (the outdated prompts in `mata-kuliah/00-meta/` carry V4 as well). The single V10 left is a real broken link in `mata-kuliah/arsip/praktikum-rekayasa-perangkat-lunak/04-assessments/rubrik-laporan-praktikum.md`.
  - Only courses whose RPS has front-matter `tipe: rps` (currently INF-101) are recognized for V3/V5/V6/V7.
- **Committed baseline:** `tools/validasi-obe-baseline.json` lists the accepted legacy violations (matched by rule + file + message; line numbers are ignored, so shifted lines do not count as new). After your change, `--baseline tools/validasi-obe-baseline.json` must report **0 new** — especially V8 (footer), V10 (relative links) and V13 (grade scale). When you fix legacy violations, regenerate it in the same commit with `--baseline-tulis tools/validasi-obe-baseline.json`; never regenerate it to absorb a new violation.
- The validator does not scan files outside `mata-kuliah/` (e.g., this file or the root README) and does not check anchors; check those links manually (`test -e`, GitHub heading slugs).

### What This Repository Does NOT Have

- No package manager (no `package.json`, `pyproject.toml`, etc.)
- No build system or compilation step
- No automated test suite or CI/CD pipelines (the validator is run manually)
- No deployment configuration
- No application code — only educational documentation with embedded Python examples, one interactive HTML module (`mata-kuliah/semester-2/analisis-data-statistik/03-modules/regresi-berganda.html`), plus `tools/validasi-obe.py`

---

## Common Tasks for AI Assistants

### Adding or Updating Course Materials

1. Place the material in the correct folder (see Placement & Authorship Rules)
2. Follow the appropriate content structure template (textbook chapter, module, or lab)
3. Maintain CPMK traceability
4. Use Indonesian with bilingual technical terms
5. Include Indonesian-context examples and datasets
6. Ensure the footer tagline is present
7. Verify consistency rules (dates, names, chapter numbers) and run `python3 tools/validasi-obe.py`

### Editing Existing Content

1. Read the file first to understand its current structure
2. Preserve the established formatting patterns
3. Maintain cross-references between theory and lab materials
4. Keep assessment weight totals at 100%

### Updating README Files

1. The root `README.md` contains the overall course list, repository structure and total file count
2. Each semester has a `mata-kuliah/semester-N/README.md` (semesters 1–8): the full course map for that semester from registry sheet 11 (code, group, SKS, *pengampu* registri), a "Materi di repositori" column, a "Materi di Folder Ini" section, and the "Penyusun materi" note. Update it whenever a course folder is added, moved or removed in that semester
3. `mata-kuliah/arsip/README.md` lists the archived courses (old code, SKS, file count, reason, successor) and the archive rules
4. Each course has its own `README.md` with course-specific details
5. When adding files, update the relevant file count tables (root README, `arsip/README.md`), recounting with `find`

### Working with the Generation Prompts

Both prompts live in `mata-kuliah/00-meta/`:

- `prompt-algoritma-pemrograman.md` — the master prompt used to generate the Algoritma dan Pemrograman materials (specifications, anti-patterns, verification checklists)
- `prompt-paket-mata-kuliah-informatika.md` — the generic prompt for a full course package

Both carry a banner marking their conventions **outdated** (as of 5 September 2026) and naming `mata-kuliah/00-pedoman-obe/pedoman-obe-konvensi.md` as the source of truth. Do not regenerate content from them without updating them first; for new-curriculum courses, the registry (`mata-kuliah/00-kurikulum-if-2025-revisi-2026/`) governs the substance.

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `README.md` | Repository overview with course listing, structure and file count |
| `tools/validasi-obe.py` | OBE consistency validator (V1–V13) |
| `mata-kuliah/semester-N/README.md` | Course map per curriculum semester (1–8) |
| `mata-kuliah/arsip/README.md` | Archived courses, reasons, content-bank mapping, archive rules |
| `mata-kuliah/00-kurikulum-if-2025-revisi-2026/README.md` | Registry index |
| `mata-kuliah/00-kurikulum-if-2025-revisi-2026/11-susunan-mata-kuliah-dan-dosen.md` | Official course list per semester: codes, SKS, *pengampu* |
| `mata-kuliah/00-kurikulum-if-2025-revisi-2026/13-cpmk-master.md` | Program-level CPMK (26) |
| `mata-kuliah/00-kurikulum-if-2025-revisi-2026/15-pemetaan-mk-cpmk-subcpmk.md` | Course × CPMK × Sub-CPMK mapping (details in `15b`–`15e`) |
| `mata-kuliah/00-kurikulum-if-2025-revisi-2026/15a-rekap-bobot-penilaian.md` | Assessment weights per course (six techniques) |
| `mata-kuliah/00-kurikulum-if-2025-revisi-2026/90-ringkasan-mk-pengampu-tri-aji-nugroho.md` | Quick reference for the courses whose registry *pengampu* is Tri Aji Nugroho |
| `mata-kuliah/00-kurikulum-if-2025-revisi-2026/91-validasi-dan-catatan-dampak.md` | Curriculum impact notes; old → new course mapping (§2.1) |
| `mata-kuliah/00-pedoman-obe/pedoman-obe-konvensi.md` | Repository conventions (§D folders, §G metadata, §I consistency, §Q validation) |
| `mata-kuliah/00-pedoman-obe/konversi-nilai.md` | Official UAI grade conversion scale (single source) |
| `mata-kuliah/00-pedoman-obe/checklist-verifikasi.md` | Manual verification checklist |
| `mata-kuliah/00-meta/KENDALI-EKSEKUSI.md` | **Execution checklist** — open items, deadlines, pending decisions, evidence (read first) |
| `mata-kuliah/00-meta/TINJAUAN-DOSEN-2026-10.md` | Choices made when documents conflicted (TD-xx), awaiting lecturer approval; decisions go to KENDALI §1 |
| `mata-kuliah/00-meta/AUDIT-MENYELURUH-2026-10.md` | Latest full audit: readiness per course, findings reference |
| `mata-kuliah/00-meta/prompt-algoritma-pemrograman.md` | Master prompt for Algoritma dan Pemrograman (outdated) |
| `mata-kuliah/semester-2/algoritma-pemrograman/01-rps/rps-algoritma-pemrograman.md` | Algoritma dan Pemrograman (INF-101 → `IF52520004`) semester learning plan |
| `mata-kuliah/semester-2/algoritma-pemrograman/05-buku-ajar/00-halaman-depan.md` | Algoritma dan Pemrograman textbook front matter and table of contents |
| `mata-kuliah/semester-2/praktikum-algoritma-pemrograman/00-pedoman-praktikum/*.md` | Lab rules and guidelines |
| `mata-kuliah/semester-2/analisis-data-statistik/01-rps/rps-statistika-analisis-data.md` | Analisis Data Statistik semester plan |
| `mata-kuliah/semester-4/rekayasa-perangkat-lunak/01-rps/rps-rekayasa-perangkat-lunak.md` | Rekayasa Perangkat Lunak (IF2205 → `IF52520011`) semester plan |
| `mata-kuliah/semester-5/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md` | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) semester plan |
| `mata-kuliah/arsip/kecerdasan-buatan-machine-learning/01-rps/rps-kecerdasan-buatan-machine-learning.md` | Archived AI/ML (IF3XXX) semester plan |
| `mata-kuliah/arsip/kecerdasan-buatan-machine-learning/06-buku-ajar/00-halaman-depan.md` | Archived AI/ML textbook front matter |
