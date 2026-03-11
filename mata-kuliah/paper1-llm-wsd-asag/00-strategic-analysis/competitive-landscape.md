# Competitive Landscape — Paper 1: LLM-WSD for ASAG

## 1. Direct Competitors (Papers in Adjacent Space)

### 1.1 Papers That Could Have Done This But Didn't

| # | Paper | Year | What They Did | What They DIDN'T Do | Why We're Different |
|---|-------|------|--------------|---------------------|---------------------|
| 1 | Tulu, Ozkaya & Orhan | 2021 | SemSpace+MaLSTM for ASAG with Lesk WSD | Did not try LLM-based WSD | We upgrade their WSD step |
| 2 | Sumanathilaka et al. | 2025 | Benchmarked LLMs for WSD on XL-WSD | Did not apply to ASAG | We apply to ASAG pipeline |
| 3 | Yae et al. | 2025 | 7 LLMs evaluated for WSD with 3 techniques | No downstream task evaluation | We measure downstream impact |
| 4 | Sumanathilaka et al. (b) | 2025 | Small LLMs with reasoning for WSD | No educational application | We use ASAG as application |
| 5 | Ferreira Mello et al. | 2024 | GPT-4 for ASAG (end-to-end) | No modular WSD analysis | We do modular analysis |

### 1.2 Detailed Competitor Analysis

#### Competitor 1: Tulu et al. (2021) — Our Direct Baseline

**Paper:** "Automatic Short Answer Grading with SemSpace Sense Vectors and MaLSTM"
**Venue:** IEEE Access (IF ~3.9 in 2021)
**Core idea:** Use SemSpace sense vectors (WordNet-based) + MaLSTM for ASAG

**Their results:**
- Per-question Pearson: >0.95 (strong)
- Aggregate Pearson: 0.15 (weak)
- RMSE: ~1.0

**Their limitation (our opportunity):**
- Used traditional Lesk algorithm for WSD
- Never questioned whether WSD quality was a bottleneck
- Per-question vs aggregate gap suggests inconsistent WSD across different vocabulary

**Our relationship:** Direct extension. We keep their pipeline intact but upgrade one component (WSD). This makes our contribution surgically precise and easy to attribute.

#### Competitor 2: Sumanathilaka et al. (2025) — WSD Benchmark

**Paper:** "Exploring the Word Sense Disambiguation Capabilities of Large Language Models"
**Venue:** arXiv (under review)
**Core idea:** Benchmark multiple LLMs for WSD using XL-WSD dataset

**Their results:**
- Fine-tuned Llama-8B: F1 = 0.8652 (English)
- Zero-shot LLMs: below supervised SOTA but competitive
- Model size matters but not linearly

**Their limitation (our opportunity):**
- Purely intrinsic evaluation (accuracy on WSD benchmark)
- No downstream task to show why WSD quality matters
- Dataset is general-purpose, not domain-specific (CS education)

**Our relationship:** We extend their finding ("LLMs can do WSD") to a concrete application ("and it actually helps ASAG").

#### Competitor 3: Yae et al. (2025) — Prompt Design for WSD

**Paper:** "Leveraging Large Language Models for Word Sense Disambiguation"
**Venue:** Neural Computing and Applications (Q2, IF ~5.1)
**Core idea:** Three prompt techniques for LLM-based WSD: multiple choice, binary verification, unseen word

**Their results:**
- Multiple-choice prompting significantly outperforms open-ended
- Structured prompts help smaller models more than larger ones
- 7 LLMs evaluated

**Their limitation (our opportunity):**
- No application to any downstream NLP task
- No domain-specific evaluation
- Didn't test with educational text

**Our relationship:** We adopt their best practice (multiple-choice prompting) and extend it with domain-primed and chain-of-thought variants in an ASAG context.

#### Competitor 4: Ferreira Mello et al. (2024) — LLM End-to-End ASAG

**Paper:** Title varies (LAK/AIED submission)
**Core idea:** Use GPT-4 directly for ASAG (no pipeline, end-to-end prompting)

**Their results:**
- GPT-4 achieves competitive ASAG performance
- Zero-shot or few-shot prompting sufficient
- Simpler than pipeline approaches

**Their limitation (our opportunity):**
- End-to-end = black box, no insight into why it works
- Expensive (GPT-4 API costs)
- No analysis of which NLP sub-task (WSD, similarity, etc.) drives performance

**Our relationship:** Complementary. We argue that modular analysis (understanding each pipeline step) is valuable even if end-to-end LLMs exist, because it provides interpretability and design insights.

---

## 2. Competitive Positioning Map

```
                        Modular Pipeline ◄──────────────► End-to-End LLM
                              │                                 │
                              │                                 │
    Traditional    Tulu (2021)│                                 │
    WSD            Lesk+SemSpace                                │
                   +MaLSTM    │                                 │
                              │                                 │
    ──────────────────────────┼─────────────────────────────────┤
                              │                                 │
    LLM-based      ★ PAPER 1 │                    Ferreira Mello│
    WSD            LLM+SemSpace                   (2024)        │
                   +MaLSTM    │                   GPT-4 direct  │
                              │                                 │
    ──────────────────────────┼─────────────────────────────────┤
                              │                                 │
    LLM-based      (Future    │                    (Majority of │
    WSD + LLM      Paper 3)   │                    2025-2026    │
    Scoring        NS-XASAG   │                    ASAG papers) │
                              │                                 │
```

**Our niche:** Modular pipeline with LLM-enhanced WSD — combining the interpretability of pipeline approaches with the language understanding of LLMs.

---

## 3. Why Now? (Timeliness Argument)

### 3.1 Technology Readiness

| Factor | 2021 (Tulu's time) | 2026 (Now) | Impact |
|--------|-------------------|------------|--------|
| LLM availability | GPT-3 (limited API) | 4+ open-source LLMs, free APIs | Can now do multi-LLM comparison |
| LLM WSD capability | Unproven | Demonstrated (Sumanathilaka, Yae) | Scientific basis exists |
| Local LLM inference | Not practical | Ollama, vLLM, 7B models on consumer GPU | Reproducible without API costs |
| WSD evaluation tools | Scattered | Consolidated (XL-WSD, raganato framework) | Standardized evaluation |

### 3.2 Research Community Readiness

- AIED 2025 keynote: "Modular AI for Education" — signals community interest in understanding components
- ACL 2025 workshop on WSD: renewed interest in sense-level NLP
- Growing concern about "black box" LLM evaluation in education → our modular approach provides interpretability

### 3.3 Window of Opportunity

This window is approximately **12-18 months** (mid-2025 to end-2026):
- Before: LLM WSD wasn't established enough to justify the study
- After: Someone else will likely connect these dots, or end-to-end approaches may make pipeline-based ASAG obsolete

**We must publish within this window.**

---

## 4. Differentiation Strategy

### 4.1 Our Unique Value Propositions

1. **Bridge paper.** We connect two established but disconnected fields. This type of paper is highly valued because it opens new research directions.

2. **Diagnostic value.** We don't just improve a number — we explain *where* the improvement comes from (WSD quality → sense vectors → grading accuracy).

3. **Practical contribution.** Our gold standard annotations for Mohler dataset are a new resource that others can use.

4. **Reproducibility.** Open-source LLMs, public dataset, documented prompts — complete reproducibility without API costs.

### 4.2 Anticipated Competitive Responses

| If a competitor publishes... | Our defense |
|-----------------------------|------------|
| LLM-WSD for ASAG (same idea) | We have deeper analysis (cascade effect, prompt variants, error taxonomy) |
| Better ASAG system overall | Our contribution is diagnostic (understanding WSD's role), not SOTA-chasing |
| Fine-tuned WSD model for ASAG | We provide zero-shot baseline; fine-tuning is natural next step we acknowledge |
| End-to-end LLM ASAG that's better | We argue modular understanding complements end-to-end — not competing |

---

## 5. Citation Potential

### 5.1 Who Would Cite This Paper

| Community | Why They'd Cite Us | Estimated Citations (3 years) |
|-----------|-------------------|-------------------------------|
| ASAG researchers | Baseline for WSD improvement | 10-15 |
| WSD researchers | Application of WSD to educational NLP | 5-10 |
| Educational NLP | Modular pipeline analysis | 8-12 |
| Sense embedding researchers | Downstream evaluation of sense-level representations | 3-5 |
| **Total** | | **26-42** |

### 5.2 Self-Citation Path (Dissertation)

- Paper 2 will cite Paper 1 as establishing the WSD baseline
- Paper 3 will cite both Paper 1 and Paper 2 as building blocks
- Dissertation will cite all three as an integrated contribution

---

*Document version: 1.0 — March 2026*
