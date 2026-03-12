# Deliverables Checklist — Paper 1: LLM-WSD for ASAG

## 1. Research Artifacts

### 1.1 Data Deliverables

| # | Deliverable | Format | Size Est. | Sprint | Status |
|---|------------|--------|-----------|--------|--------|
| D1 | Mohler dataset (parsed) | CSV | ~500 KB | Sprint 1 | ☐ |
| D2 | Content word extraction | CSV | ~200 KB | Sprint 1 | ☐ |
| D3 | Polysemy statistics report | JSON + MD | ~50 KB | Sprint 1 | ☐ |
| D4 | Lesk baseline WSD results | CSV | ~1 MB | Sprint 1 | ☐ |
| D5 | Gold standard annotation template | XLSX | ~100 KB | Sprint 2 | ☐ |
| D6 | Annotation guidelines | PDF/MD | ~20 KB | Sprint 2 | ☐ |
| D7 | Final gold standard | CSV | ~50 KB | Sprint 2 | ☐ |
| D8 | Inter-annotator agreement report | JSON + MD | ~20 KB | Sprint 2 | ☐ |
| D9 | LLM WSD raw results (all conditions) | CSV | ~5 MB | Sprint 3 | ☐ |
| D10 | Full pipeline ASAG scores (all conditions) | CSV | ~2 MB | Sprint 3 | ☐ |
| D11 | Intrinsic evaluation tables | CSV | ~50 KB | Sprint 3 | ☐ |
| D12 | Extrinsic evaluation tables | CSV | ~50 KB | Sprint 4 | ☐ |
| D13 | Error analysis case studies | MD | ~30 KB | Sprint 4 | ☐ |
| D14 | Cost-benefit analysis | CSV + MD | ~20 KB | Sprint 4 | ☐ |

### 1.2 Code Deliverables

| # | Deliverable | Language | Lines Est. | Sprint | Status |
|---|------------|----------|-----------|--------|--------|
| C1 | Mohler data loader | Python | ~150 | Sprint 1 | ☐ |
| C2 | Content word extractor | Python | ~200 | Sprint 1 | ☐ |
| C3 | Lesk WSD engine | Python | ~100 | Sprint 1 | ☐ |
| C4 | LLM WSD engine (4 models × 4 prompts) | Python | ~400 | Sprint 3 | ☐ |
| C5 | SemSpace vector lookup | Python | ~150 | Sprint 1 | ☐ |
| C6 | MaLSTM pipeline | Python | ~300 | Sprint 1 | ☐ |
| C7 | Evaluation metrics module | Python | ~200 | Sprint 3-4 | ☐ |
| C8 | Statistical tests module | Python | ~150 | Sprint 3-4 | ☐ |
| C9 | Visualization module | Python | ~250 | Sprint 4 | ☐ |
| C10 | Unit tests | Python | ~300 | All sprints | ☐ |
| C11 | Experiment runner script | Python | ~100 | Sprint 3 | ☐ |

### 1.3 Paper Deliverables

| # | Deliverable | Format | Pages Est. | Sprint | Status |
|---|------------|--------|-----------|--------|--------|
| P1 | Abstract | MD → LaTeX | 0.25 | Sprint 5 | ☐ |
| P2 | Introduction | MD → LaTeX | 1.5 | Sprint 5 | ☐ |
| P3 | Related Work | MD → LaTeX | 2.0 | Sprint 5 | ☐ |
| P4 | Methodology | MD → LaTeX | 3.0 | Sprint 5 | ☐ |
| P5 | Experimental Setup | MD → LaTeX | 1.0 | Sprint 5 | ☐ |
| P6 | Results | MD → LaTeX | 2.5 | Sprint 5 | ☐ |
| P7 | Discussion | MD → LaTeX | 2.0 | Sprint 5 | ☐ |
| P8 | Conclusion | MD → LaTeX | 0.75 | Sprint 5 | ☐ |
| P9 | References | BibTeX | 1.0 | Sprint 5 | ☐ |
| P10 | Figures (6-8 figures) | PDF/PNG 300dpi | N/A | Sprint 5 | ☐ |
| P11 | Supplementary materials | ZIP | N/A | Sprint 6 | ☐ |
| P12 | Cover letter | PDF | 1 page | Sprint 6 | ☐ |

---

## 2. Quality Gates

Each deliverable must pass its quality gate before the sprint is considered complete:

### Sprint 1 Gate
- [ ] D1: Mohler dataset has 87 questions, 2,273 answers
- [ ] D2: Content words include nouns, verbs, adjectives with correct POS
- [ ] D4: Lesk results cover all polysemous words
- [ ] C1-C6: All modules runnable, unit tests pass
- [ ] Pipeline produces scores in [0, 5] range

### Sprint 2 Gate
- [ ] D5: 500 words sampled with stratified balance
- [ ] D7: All 500 words have resolved gold synset
- [ ] D8: Cohen's κ > 0.6

### Sprint 3 Gate
- [ ] D9: 8,000 LLM WSD results (4 LLMs × 4 prompts × 500 words)
- [ ] D10: 11,365 pipeline scores (5 conditions × 2,273 answers)
- [ ] D11: At least 1 LLM significantly outperforms Lesk (p < 0.05)

### Sprint 4 Gate
- [ ] D12: Pearson r and RMSE for all 5 conditions
- [ ] D13: At least 3 case studies with traceable cascade analysis
- [ ] D14: Timing and cost data for all conditions

### Sprint 5 Gate
- [ ] P1-P9: All sections complete with real data (no placeholders)
- [ ] P10: All figures publication-quality
- [ ] TDW protocol: All section-level tests pass
- [ ] Humanization: All anti-AI writing tests pass
- [ ] Cross-section consistency verified

### Sprint 6 Gate
- [ ] Internal review feedback incorporated
- [ ] Final formatting per venue requirements
- [ ] Page count within limit
- [ ] P12: Cover letter ready
- [ ] Paper submitted to venue

---

## 3. File Organization

```
project-root/
├── src/
│   ├── data/
│   │   ├── mohler_loader.py          (C1)
│   │   └── content_word_extractor.py (C2)
│   ├── wsd/
│   │   ├── lesk_engine.py            (C3)
│   │   └── llm_wsd_engine.py         (C4)
│   ├── pipeline/
│   │   ├── semspace_vectors.py       (C5)
│   │   └── malstm_pipeline.py        (C6)
│   ├── evaluation/
│   │   ├── metrics.py                (C7)
│   │   └── statistical_tests.py      (C8)
│   ├── visualization/
│   │   └── paper_figures.py          (C9)
│   └── run_experiments.py            (C11)
├── tests/                            (C10)
│   ├── test_mohler_loader.py
│   ├── test_lesk_engine.py
│   ├── test_llm_wsd.py
│   ├── test_pipeline.py
│   └── test_evaluation.py
├── data/
│   ├── mohler/                       (D1)
│   ├── gold_standard/                (D5-D8)
│   └── results/                      (D9-D14)
├── paper/
│   ├── sections/                     (P1-P9)
│   ├── figures/                      (P10)
│   ├── supplementary/                (P11)
│   └── cover_letter.md               (P12)
├── notebooks/
│   ├── 01-data-exploration.ipynb
│   ├── 02-wsd-analysis.ipynb
│   └── 03-results-visualization.ipynb
├── requirements.txt
└── README.md
```

---

## 4. Handoff Criteria

Paper is ready for submission when ALL of these are true:

- [ ] All deliverables (D1-D14, C1-C11, P1-P12) marked complete
- [ ] All quality gates passed
- [ ] All TDW acceptance tests passed
- [ ] All 3 internal reviewers (Endang, Tri Aji, Teguh) have signed off
- [ ] Paper formatted per venue template
- [ ] Supplementary materials packaged
- [ ] Cover letter written and reviewed

---

*Document version: 1.0 — March 2026*
