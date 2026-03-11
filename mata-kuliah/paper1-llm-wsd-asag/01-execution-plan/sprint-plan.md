# Sprint Plan — Hour-by-Hour AI-Agentic Execution

## Overview

| Total Sprints | 6 |
|--------------|---|
| Total AI Hours | 22-28 |
| Total Human Hours | 7-10 |
| Calendar Estimate | 4-6 weeks (part-time) or 2 weeks (intensive) |
| Methodology | AI-Agentic with Claude Code as primary executor |

---

## Sprint 0: Pre-Execution (Before Coding Begins)

**Duration:** 2-3 hours (mostly human)
**Blocker:** Must complete before Sprint 1

| Task | Actor | Action | Output | Done? |
|------|-------|--------|--------|-------|
| 0.1 | Human | Email Orhan/Tulu (ctulu@atu.edu.tr) requesting SemSpace vectors | Email sent | ☐ |
| 0.2 | Human | Download Mohler dataset from official source | `data/mohler/` directory | ☐ |
| 0.3 | Human | Set up API keys: Gemini API, Hugging Face token | `.env` file | ☐ |
| 0.4 | Human | Install Ollama + pull Qwen-2.5, Mistral, Llama-3 models | Models available locally | ☐ |
| 0.5 | Human | Confirm promotor approves 4 LLM selection | Approval noted | ☐ |
| 0.6 | Claude | Verify Mohler dataset format and count records | Dataset stats report | ☐ |

**Gate:** Cannot proceed to Sprint 1 until Mohler dataset is accessible and at least 2 LLMs are runnable.

---

## Sprint 1: Environment Setup & Baseline Replication

**Duration:** 4 hours (AI-agentic)
**Dependencies:** Sprint 0 complete

### Hour 1: Environment & Data Loading

```
Claude Code Tasks:
├── Create project structure
│   ├── src/
│   │   ├── data/         → data loaders
│   │   ├── wsd/          → WSD engines (Lesk + LLM)
│   │   ├── pipeline/     → SemSpace + MaLSTM pipeline
│   │   ├── evaluation/   → metrics + statistical tests
│   │   └── visualization/→ publication figures
│   ├── data/
│   │   ├── mohler/       → raw dataset
│   │   ├── gold_standard/→ WSD annotations
│   │   └── results/      → experiment outputs
│   ├── notebooks/        → analysis notebooks
│   └── tests/            → unit tests for each module
│
├── Install dependencies
│   pip install torch transformers nltk vllm
│   pip install pandas numpy scipy scikit-learn
│   pip install matplotlib seaborn
│   pip install google-generativeai  # Gemini
│   pip install openai               # OpenAI-compatible APIs
│
├── Load & parse Mohler dataset
│   → Parse into structured DataFrame
│   → Columns: question_id, student_answer, reference_answer, score_1, score_2, avg_score
│   → Verify: 87 questions, 2,273 answers
│
└── Generate dataset statistics
    → Total words, unique words, polysemous words
    → Distribution of #senses per word
    → Output: data/mohler/dataset_stats.json
```

**Test:** `assert len(mohler_df) == 2273` and `assert mohler_df['question_id'].nunique() == 87`

### Hour 2: Content Word Extraction & Analysis

```
Claude Code Tasks:
├── Extract all content words from Mohler answers
│   → Tokenize with NLTK
│   → POS tag (Penn Treebank)
│   → Filter: nouns, verbs, adjectives (content words only)
│   → Map to WordNet POS
│
├── Identify polysemous words
│   → For each content word: count WordNet synsets
│   → Filter: words with ≥2 synsets
│   → Record: word, POS, sentence_context, num_senses
│
├── Compute polysemy statistics
│   → Total content words extracted
│   → % polysemous (≥2 senses)
│   → Distribution: 2-3 senses, 4-7 senses, 8+ senses
│   → Most ambiguous words in dataset
│   → CS-specific terms identification
│
└── Output: data/mohler/content_words.csv
```

**Test:** Verify CS-specific terms (process, node, stack, queue, tree) are captured with correct POS.

### Hour 3: Lesk Baseline Implementation

```
Claude Code Tasks:
├── Implement NLTK Lesk WSD
│   → For each polysemous content word:
│     → Apply nltk.wsd.lesk(sentence, word, pos)
│     → Record: word, context, predicted_synset, confidence
│   → Handle edge cases:
│     → Word not in WordNet → mark as OOV
│     → Lesk returns None → use first synset (most frequent sense)
│
├── Run Lesk on ALL Mohler content words
│   → Reference answers: ~87 × avg_words
│   → Student answers: ~2,273 × avg_words
│   → Total: estimated 30,000-50,000 WSD decisions
│
├── Compute Lesk coverage statistics
│   → % of words successfully disambiguated
│   → % falling back to most-frequent-sense
│   → % OOV
│
└── Output: data/results/lesk_baseline_wsd.csv
```

**Test:** Lesk correctly disambiguates "stack" in CS context as data structure (not pile).

### Hour 4: Pipeline Skeleton (SemSpace + MaLSTM)

```
Claude Code Tasks:
├── SemSpace vector lookup
│   IF pre-trained vectors available:
│   │   → Load SemSpace vectors
│   │   → Implement synset → vector lookup
│   │   → Handle missing synsets (fallback to zero vector)
│   │
│   IF NOT available (Plan B):
│   │   → Implement AutoExtend (Rothe & Schütze, 2015)
│   │   → OR use LMMS (Loureiro & Jorge, 2019)
│   │   → OR use WordNet path-based similarity as proxy
│   │   → Document deviation from Tulu's pipeline
│
├── MaLSTM implementation
│   → Implement Manhattan LSTM (Mueller & Thyagarajan, 2016)
│   → Input: two sequences of sense vectors
│   → Output: Manhattan similarity score [0, 1]
│   → Scale to 0-5 range (× 5.0)
│
├── Full pipeline test
│   → Run 5 sample answers through: Lesk → SemSpace → MaLSTM → Score
│   → Compare with Tulu's published numbers (sanity check)
│   → Document any discrepancies
│
└── Output: Pipeline runnable end-to-end
```

**Test:** Pipeline produces scores in [0, 5] range. Per-question correlation direction matches Tulu.

**Sprint 1 Gate:** Pipeline runs end-to-end. Lesk baseline results are available.

---

## Sprint 2: Gold Standard Construction

**Duration:** 4 hours (2 AI + 2-4 human)
**Dependencies:** Sprint 1 complete

### Hour 5: Stratified Sampling & Annotation Template

```
Claude Code Tasks:
├── Stratified sampling of 500 polysemous words
│   Strategy:
│   │   → 200 words with 2-3 senses (low ambiguity)
│   │   → 200 words with 4-7 senses (medium ambiguity)
│   │   → 100 words with 8+ senses (high ambiguity)
│   │
│   Additional stratification:
│   │   → Balance across question topics
│   │   → Include at least 50 CS-specific terms
│   │   → Include at least 30 general English terms
│   │   → Balance across POS (nouns, verbs, adjectives)
│
├── Generate annotation spreadsheet
│   Columns:
│   │   → word_id, word, POS, sentence_context
│   │   → question_id (from Mohler)
│   │   → candidate_synsets (numbered, with glosses)
│   │   → annotator_1_choice, annotator_2_choice (empty)
│   │   → notes (empty)
│
├── AI pre-annotation (acceleration)
│   → Use Claude to pre-fill "obvious" cases:
│     → Words with only 2 senses where context is clear
│     → CS-specific terms where domain sense is obvious
│   → Mark confidence: "auto-filled" vs "needs human"
│   → Estimated: 150-200 auto-filled, 300-350 needs human
│
├── Generate annotation guidelines document
│   → Rules for annotators
│   → Examples of tricky cases
│   → How to handle "none of the senses fit"
│
└── Output: data/gold_standard/annotation_template.xlsx
          data/gold_standard/annotation_guidelines.pdf
```

**Test:** 500 words sampled, balanced across strata. All candidate synsets listed correctly.

### Hour 6-7: Human Annotation (HUMAN TASK)

```
HUMAN TASKS (Bu Endang + 1 CS colleague):
├── Review auto-filled annotations (150-200 words)
│   → Approve or correct each auto-fill
│   → Estimated: 30-45 minutes
│
├── Annotate remaining words (300-350 words)
│   → Each annotator independently selects correct synset
│   → Flag disagreements for discussion
│   → Estimated: 2-3 hours per annotator (can be parallel)
│
└── Resolve disagreements
    → Discussion-based resolution
    → If unresolvable: 3rd annotator (Tri Aji or Teguh)
```

**Note:** This is the primary bottleneck. Consider doing in 2 sessions to avoid fatigue.

### Hour 8: Inter-Annotator Agreement Analysis

```
Claude Code Tasks:
├── Compute agreement metrics
│   → Cohen's Kappa (κ) — inter-annotator agreement
│   → Target: κ > 0.7 (substantial agreement)
│   → Minimum: κ > 0.6 (moderate agreement)
│   → If κ < 0.6: review annotation guidelines, re-annotate worst cases
│
├── Agreement by category
│   → By ambiguity level (low/medium/high)
│   → By POS
│   → By CS-specific vs general
│
├── Generate final gold standard
│   → Merge annotations (majority vote or discussion-resolved)
│   → Final file: word, context, correct_synset_id, agreement_status
│
└── Output: data/gold_standard/gold_standard.csv
          data/gold_standard/agreement_report.json
```

**Test:** κ > 0.6 overall. 500 words annotated with resolved synsets.

**Sprint 2 Gate:** Gold standard CSV complete with documented inter-annotator agreement.

---

## Sprint 3: LLM WSD Experiments

**Duration:** 4 hours (AI-agentic)
**Dependencies:** Sprint 2 complete

### Hour 9: Prompt Engineering & Testing

```
Claude Code Tasks:
├── Implement 4 prompt variants (P1-P4)
│   P1: Basic (synset ID + gloss)
│   P2: With examples (add WordNet example sentences)
│   P3: Domain-primed ("CS exam" context)
│   P4: Chain-of-thought (step-by-step reasoning)
│
├── Implement LLM callers
│   → Qwen-2.5: via Ollama (local) → OpenAI-compatible API
│   → Mistral-7B: via Ollama (local)
│   → Llama-3.1-8B: via Ollama (local)
│   → Gemini-1.5-Flash: via Google Generative AI SDK
│
├── Sanity test: 20 words × 4 LLMs × 4 prompts = 320 calls
│   → Verify output format (single number)
│   → Test parsing robustness
│   → Measure latency per call
│   → Check for refusals, empty responses, explanation-only responses
│
├── Fix edge cases
│   → LLM returns text instead of number → regex parsing
│   → LLM refuses → retry with simplified prompt
│   → Response out of range → flag as unparseable, fallback to Lesk
│
└── Output: All prompts tested and working. Edge case handlers in place.
```

**Test:** All 4 LLMs respond with parseable synset numbers on 20 test words. Parse success rate > 95%.

### Hour 10: Full WSD Experiment Run

```
Claude Code Tasks:
├── Run all experiments
│   Scope: 4 LLMs × 4 prompt variants × 500 gold standard words
│   Total API calls: 8,000
│   Estimated time: 30-60 minutes (parallel where possible)
│
│   For each (llm, prompt_variant, word):
│   │   → Build prompt from template
│   │   → Call LLM (temperature=0.0)
│   │   → Parse response → synset number
│   │   → Log: word_id, llm, prompt, predicted_synset, raw_response, latency_ms
│   │   → Compare with gold standard → correct/incorrect
│
├── Rate limiting & retry logic
│   → Gemini API: respect 60 calls/min limit
│   → Local models (Ollama): no limit, but sequential
│   → Retry on timeout: max 3 retries with exponential backoff
│
├── Important: For P4 (chain-of-thought):
│   → Set max_tokens = 300 (not 10!)
│   → Parse LAST number from response
│
└── Output: data/results/llm_wsd_results.csv
          (columns: word_id, llm, prompt_variant, predicted_synset,
           gold_synset, correct, raw_response, latency_ms)
```

**Test:** 8,000 results logged. Parse success rate > 95%. No more than 5% missing data.

### Hour 11: Intrinsic Evaluation

```
Claude Code Tasks:
├── Compute accuracy per condition
│   → 5 WSD methods (Lesk + 4 LLMs) × 4 prompt variants
│   → Overall accuracy, accuracy by ambiguity level, by POS, by domain
│
├── Statistical significance tests
│   → McNemar's test: pairwise comparison between methods
│   → Bonferroni correction for multiple comparisons (10 pairs)
│   → Effect size: Cohen's h for proportion differences
│
├── Identify best prompt variant per LLM
│   → Statistical comparison of P1 vs P2 vs P3 vs P4 per LLM
│   → Select "best config" for each LLM for extrinsic evaluation
│
├── Generate intrinsic result tables
│   → Table 1: Overall WSD accuracy comparison
│   → Table 2: Accuracy by ambiguity level
│   → Table 3: Accuracy by POS
│   → Table 4: Statistical significance matrix
│   → Table 5: Prompt variant comparison
│
└── Output: data/results/intrinsic_evaluation/
          ├── accuracy_table.csv
          ├── significance_tests.csv
          ├── prompt_comparison.csv
          └── figures/ (bar charts, heatmaps)
```

**Test:** At least 1 LLM significantly outperforms Lesk (p < 0.05 after correction).

### Hour 12: Full Pipeline Run with LLM WSD

```
Claude Code Tasks:
├── Run WSD on ALL Mohler content words (not just gold 500)
│   → Use best prompt variant per LLM (from Hour 11)
│   → 5 conditions: Lesk, Qwen, Mistral, Llama, Gemini
│   → Total: ~30,000-50,000 WSD decisions × 5 = 150,000-250,000
│   → For local models: batch processing to speed up
│
├── Feed through SemSpace → MaLSTM → Score pipeline
│   → For each condition:
│     → Convert synsets to SemSpace vectors
│     → Run MaLSTM on (reference, student) pairs
│     → Compute Manhattan similarity → predicted score
│   → Total: 5 × 2,273 = 11,365 pipeline runs
│
├── Log all intermediate results
│   → synsets_per_condition.csv
│   → vectors_per_condition.csv (or summary stats)
│   → predicted_scores_per_condition.csv
│
└── Output: data/results/pipeline_results/
          ├── asag_scores_lesk.csv
          ├── asag_scores_qwen.csv
          ├── asag_scores_mistral.csv
          ├── asag_scores_llama.csv
          └── asag_scores_gemini.csv
```

**Test:** All 11,365 pipeline runs complete. Predicted scores in [0, 5] range. Lesk scores match Sprint 1 baseline.

**Sprint 3 Gate:** All experimental data collected. Intrinsic results show LLM > Lesk.

---

## Sprint 4: Analysis & Error Investigation

**Duration:** 3 hours (AI-agentic)
**Dependencies:** Sprint 3 complete

### Hour 13: Extrinsic Evaluation

```
Claude Code Tasks:
├── Compute ASAG metrics per condition
│   → Aggregate Pearson r + p-value
│   → Aggregate RMSE
│   → Per-question Pearson r (87 questions × 5 conditions)
│   → Per-question RMSE
│
├── Statistical comparison
│   → Paired t-test: Pearson r per question, Lesk vs each LLM
│   → Wilcoxon signed-rank: non-parametric alternative
│   → Effect size: Cohen's d
│   → Confidence intervals for improvement
│
├── Generate extrinsic result tables
│   → Table 6: ASAG performance comparison (main result table)
│   → Table 7: Per-question performance distribution
│   → Table 8: Statistical significance for ASAG improvement
│
├── Key visualizations
│   → Figure 1: Bar chart — Pearson r per condition (with CI)
│   → Figure 2: Scatter plot — WSD accuracy vs ASAG Pearson r
│   → Figure 3: Box plot — per-question Pearson r distribution
│   → Figure 4: Improvement heatmap (question × LLM)
│
└── Output: data/results/extrinsic_evaluation/
```

**Test:** Extrinsic results show consistent direction with intrinsic results.

### Hour 14: Error Cascade Analysis

```
Claude Code Tasks:
├── Identify high-impact WSD differences
│   → Find answers where WSD method changed score by >0.5 points
│   → For each: trace which word(s) had different WSD
│   → For each: what synset was chosen differently
│   → For each: how did the vector change
│
├── Error taxonomy
│   → Type A: Domain confusion (CS term → general sense)
│   → Type B: POS ambiguity (noun vs verb)
│   → Type C: Fine-grained sense distinction (similar senses confused)
│   → Type D: OOV handling differences
│   → Count and % per type per LLM
│
├── Case study selection
│   → 5 best cases: LLM WSD dramatically improved ASAG score
│   → 5 worst cases: LLM WSD hurt ASAG score (vs Lesk)
│   → Write narrative for each:
│     "Student X answered '...' The word '...' was disambiguated as
│      [synset_a] by Lesk but [synset_b] by Gemini. This changed the
│      predicted score from X to Y because..."
│
├── Confusion analysis
│   → Per LLM: which synsets are most commonly confused
│   → Domain-specific confusion patterns
│
└── Output: data/results/error_analysis/
          ├── high_impact_differences.csv
          ├── error_taxonomy.csv
          ├── case_studies.md
          └── confusion_matrices/
```

**Test:** At least 3 illustrative case studies where WSD change clearly explains score change.

### Hour 15: Cost-Benefit & Practical Analysis

```
Claude Code Tasks:
├── Performance metrics
│   → Time per disambiguation: Lesk vs each LLM
│   → Total pipeline time per condition
│   → Throughput: words/second for each method
│
├── Cost analysis
│   → Local models (Qwen, Mistral, Llama): compute cost estimate
│   → API models (Gemini): actual API cost for 500 and full dataset
│   → Scale projections: cost for 10K, 100K, 1M words
│
├── Deployment recommendation matrix
│   → Best accuracy: which LLM
│   → Best cost-efficiency: which LLM
│   → Best for real-time: which LLM
│   → Best for offline batch: which LLM
│
└── Output: data/results/practical_analysis/
          ├── timing_comparison.csv
          ├── cost_analysis.csv
          └── deployment_recommendations.md
```

**Test:** Timing data collected for all conditions. Cost estimates are reasonable.

**Sprint 4 Gate:** All analysis complete. Key findings identified. Case studies written.

---

## Sprint 5: Paper Writing

**Duration:** 6-8 hours (AI + Human collaboration)
**Dependencies:** Sprint 4 complete

### Hour 16-17: Fill Paper Draft with Real Results

```
Claude (Chat + Code) Tasks:
├── Abstract: Replace all [placeholders] with actual numbers
├── Results section: Write from generated tables/figures
│   → 5.1: Intrinsic WSD results (Table 1-5)
│   → 5.2: Extrinsic ASAG results (Table 6-8, Figure 1-4)
│   → 5.3: Error analysis (case studies, taxonomy)
│   → 5.4: Prompt sensitivity analysis
│   → 5.5: Cost-benefit analysis
├── Discussion: Connect findings to RQs
│   → RQ1 answered: [which LLM best for WSD]
│   → RQ2 answered: [how much WSD affects ASAG]
│   → RQ3 answered: [what errors matter most]
├── Conclusion: Finalize with actual contributions
└── Verify all numbers match between text, tables, and figures
```

### Hour 18: Publication-Ready Figures

```
Claude Code Tasks:
├── Generate all figures in 300 DPI, vector format where possible
├── Architecture diagram: Pipeline with highlighted WSD step
├── Result figures formatted per venue requirements
├── Color scheme: colorblind-safe palette
└── Output: paper/figures/ (PDF + PNG)
```

### Hour 19: Reference Verification & Literature Check

```
Claude (Chat) Tasks:
├── Verify all 35+ references: correct DOI, authors, year, venue
├── Cross-check all in-text citations match reference list
├── Ensure no missing citations (especially for claims in Related Work)
├── Add any new references discovered during analysis
└── Format per venue requirement (IEEE or APA)
```

### Hour 20: Academic Writing Quality Pass

```
Apply Test-Driven Writing Protocol (see test-driven-writing-protocol.md):
├── Hedging check: No overclaiming, appropriate qualifiers
├── Flow check: Logical transitions between paragraphs
├── Humanization check: Varied sentence structure, no robotic prose
├── Consistency check: Terminology, abbreviations, formatting
├── Grammar & spelling: Final proofread
└── Reviewer anticipation: Re-read through 3 reviewer perspectives
```

**Sprint 5 Gate:** Paper draft complete, all sections filled with real results.

---

## Sprint 6: Quality Assurance & Submission Prep

**Duration:** 3-4 hours (AI + Human)
**Dependencies:** Sprint 5 complete

### Hour 21: Internal Review Cycle

```
├── Bu Endang reviews full paper (2-3 hours, human)
├── Tri Aji reviews methodology + code (1-2 hours, human)
├── Teguh reviews literature + positioning (1 hour, human)
├── Collect all feedback → revision list
└── Claude implements revisions
```

### Hour 22: Final Formatting & Submission

```
Claude Code Tasks:
├── Format in IEEE two-column template (LaTeX or Word)
├── Final spell check, grammar check
├── Verify page count (≤14 for TLT, ≤12 for ESWA)
├── Prepare supplementary materials
│   → Code repository link
│   → Gold standard dataset
│   → Extended result tables
├── Write cover letter to editor
├── Generate PDF for submission
└── Submit via venue's manuscript system
```

**Sprint 6 Gate:** Paper submitted. 🎯

---

## Sprint Summary

| Sprint | Hours (AI) | Hours (Human) | Deliverables |
|--------|-----------|---------------|-------------|
| 0: Pre-execution | 0.5 | 2-3 | Environment ready, data downloaded |
| 1: Setup & baseline | 4 | 0.5 | Pipeline working, Lesk baseline |
| 2: Gold standard | 2 | 3-4 | 500-word annotated dataset |
| 3: LLM experiments | 4 | 0.5 | All WSD + pipeline results |
| 4: Analysis | 3 | 1 | Tables, figures, case studies |
| 5: Writing | 6-8 | 2 | Complete paper draft |
| 6: QA & submission | 2-3 | 2-3 | Submitted paper |
| **TOTAL** | **21.5-25.5** | **11.5-14.5** | |
| **GRAND TOTAL** | | **33-40 hours** | |

---

*Document version: 1.0 — March 2026*
