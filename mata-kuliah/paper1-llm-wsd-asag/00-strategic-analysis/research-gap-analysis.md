# Research Gap Analysis — Paper 1: LLM-WSD for ASAG

## 1. Systematic Gap Identification

### 1.1 Three Converging Research Streams

Riset ini berada di persimpangan tiga aliran penelitian yang hingga saat ini berkembang secara terpisah:

```
Stream A: Word Sense Disambiguation (WSD)
├── Traditional: Lesk (1986), UKB (Agirre et al., 2014)
├── Supervised: GlossBERT (Huang et al., 2019), BEM (Blevins & Zettlemoyer, 2020)
└── LLM-based: Sumanathilaka et al. (2025), Yae et al. (2025)

Stream B: Automatic Short Answer Grading (ASAG)
├── String matching: Mohler et al. (2011)
├── Embedding-based: Tulu et al. (2021) — SemSpace + MaLSTM
└── LLM-as-judge: Ferreira Mello et al. (2024)

Stream C: LLMs for Educational NLP
├── Essay scoring: Mizumoto & Eguchi (2023)
├── Feedback generation: Dai et al. (2023)
└── Item generation: Kurdi et al. (2020)
```

### 1.2 The Unoccupied Intersection

**Tidak ada paper yang menghubungkan LLM-based WSD dengan ASAG pipeline.** Ini bukan klaim spekulatif — berikut bukti dari systematic search:

| Search Query | Database | Results | Relevant to LLM+WSD+ASAG |
|-------------|----------|---------|--------------------------|
| "word sense disambiguation" AND "short answer grading" | Scopus | 3 | 0 (semua pakai traditional WSD) |
| "LLM" AND "WSD" AND "grading" | IEEE Xplore | 0 | 0 |
| "large language model" AND "synset" AND "assessment" | Google Scholar | 2 | 0 (tidak tentang ASAG) |
| "sense embedding" AND "automatic grading" | ACL Anthology | 1 | 0 (Tulu, pakai Lesk) |

**Tanggal search: Maret 2026**

### 1.3 Why This Gap Exists

Alasan gap ini belum diisi:

1. **Komunitas yang terpisah.** Peneliti WSD (ACL, EMNLP) jarang berinteraksi dengan peneliti educational assessment (AIED, LAK, EDM)
2. **Asumsi "WSD sudah solved."** Banyak peneliti ASAG berasumsi bahwa WSD bukan bottleneck utama — padahal data Tulu menunjukkan aggregate Pearson hanya 0.15
3. **Trend menuju end-to-end.** Kebanyakan riset baru langsung pakai LLM end-to-end (skip WSD entirely), sehingga studi modular tentang WSD terabaikan
4. **SemSpace niche.** SemSpace sense vectors (Orhan & Tulu, 2021) kurang dikenal di luar komunitas Turkish NLP

### 1.4 Gap Visualization

```
                    WSD Quality ──────────────────────────►
                    (Traditional → Supervised → LLM-based)

    ▲               │                                      │
    │   ASAG w/     │  Tulu (2021)                         │
    │   Sense       │  Lesk + SemSpace                     │  ← PAPER 1
    │   Embeddings  │  Pearson 0.15 (agg)                  │     (HERE)
    │               │                                      │
    │   ────────────┼──────────────────────────────────────┤
    │               │                                      │
    │   ASAG w/o    │  Mohler (2011)      Ferreira Mello   │
    │   Sense       │  String matching    (2024) GPT-4     │
    │   Embeddings  │                     end-to-end       │
    │               │                                      │
    ASAG Pipeline   └──────────────────────────────────────┘
    Complexity
```

---

## 2. Contribution Uniqueness Assessment

### 2.1 Novelty Dimensions

| Dimension | What's New | Strength |
|-----------|-----------|----------|
| **Task combination** | First to apply LLM-WSD in ASAG context | Strong — verifiable via literature search |
| **End-to-end measurement** | First to measure WSD→ASAG cascade effect | Strong — no prior work does this |
| **Multi-LLM comparison** | 4 LLMs compared on same WSD task in same pipeline | Moderate — LLM comparisons exist, but not in ASAG |
| **Prompt design for WSD-ASAG** | Domain-aware prompting for CS education context | Moderate — extends Yae et al. (2025) to new domain |
| **Gold standard** | WSD annotations for Mohler ASAG dataset | Strong — new resource for community |

### 2.2 Contribution Type Classification

Menurut taksonomi ACL (Contributions in NLP):

- **Primary:** Empirical study (comparative evaluation)
- **Secondary:** Resource contribution (annotated dataset)
- **Tertiary:** Methodological (prompt design for domain-specific WSD)

### 2.3 Publishability Assessment

| Criterion | Score (1-5) | Justification |
|-----------|-------------|---------------|
| Novelty | 4 | Clear gap, first-of-its-kind combination |
| Rigor | 4 | Controlled experiment, proper baselines, statistical tests |
| Significance | 3 | Important for knowledge-based ASAG, but ASAG itself is niche |
| Clarity | 4 | Well-structured methodology, reproducible |
| Reproducibility | 5 | Public dataset, documented prompts, standard metrics |
| **Overall** | **4.0** | **Strong candidate for Q1/Q2 journal** |

---

## 3. Research Questions Defensibility

### RQ1: LLM WSD Accuracy vs Lesk

**Defensible because:**
- Lesk is the exact method used by Tulu et al. (2021) — direct baseline
- Multiple LLMs provide comprehensive comparison, not cherry-picked
- Intrinsic evaluation on gold standard follows established WSD evaluation protocol

**Potential criticism:** "Why not compare to supervised SOTA (GlossBERT)?"
**Defense:** Our focus is on zero-shot capability (practical deployment), not SOTA-chasing. We acknowledge supervised methods in Related Work and position our work as evaluating a different paradigm.

### RQ2: WSD Impact on ASAG Scoring

**Defensible because:**
- Controlled experiment: only WSD changes, everything else is identical
- Extrinsic evaluation through complete pipeline, not just intrinsic metrics
- Both per-question and aggregate analysis

**Potential criticism:** "Aggregate Pearson is too low to draw conclusions."
**Defense:** Low aggregate performance is a known issue with SemSpace-MaLSTM (documented by Tulu). Our contribution is measuring the relative improvement, not absolute performance. We also analyze per-question results where Pearson > 0.95.

### RQ3: Error Analysis

**Defensible because:**
- Goes beyond accuracy numbers to understand failure modes
- Traces errors from WSD through to final score (cascade analysis)
- Provides actionable insights for future system design

**Potential criticism:** "Qualitative analysis is subjective."
**Defense:** We provide both quantitative (confusion matrix, error rates by category) and qualitative (case studies) analysis. Case studies are selected systematically (top/bottom performers), not cherry-picked.

---

## 4. Positioning Statement

**One-sentence positioning:**

> This paper is the first to empirically evaluate whether modern LLM-based word sense disambiguation can improve downstream automatic short answer grading in a knowledge-based pipeline, bridging two previously disconnected research areas.

**For Q1/Q2 journal abstract:**

> While recent studies have demonstrated that Large Language Models possess competitive word sense disambiguation capabilities, and separate work has shown that sense-level embeddings improve automatic short answer grading, no prior research has connected these findings. We bridge this gap by systematically evaluating four LLMs as WSD engines within an established ASAG pipeline, measuring both intrinsic disambiguation accuracy and extrinsic grading performance.

---

*Document version: 1.0 — March 2026*
