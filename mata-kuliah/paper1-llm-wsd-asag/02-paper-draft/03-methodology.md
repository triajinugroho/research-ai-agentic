# Section 3: Methodology

> **Target length:** 3.0 pages (IEEE two-column) | ~2,400 words
> **TDW tests:** MTD-01 through MTD-10

---

## 3. Methodology

Our experimental design follows a controlled substitution strategy: we replace a single component (WSD) in an established ASAG pipeline while holding all other components constant, then measure the effect on both WSD accuracy and downstream grading performance. This section describes the pipeline architecture (3.1), gold standard construction (3.2), LLM-based WSD design (3.3), and evaluation protocol (3.4).

### 3.1 Pipeline Architecture

Figure 1 illustrates the SemSpace-MaLSTM pipeline adapted from Tulu et al. [4]. The pipeline processes a student answer and reference answer through four stages:

```
┌─────────────────────────────────────────────────────────────────┐
│                    ASAG Pipeline Architecture                    │
│                                                                  │
│  Input:  Student Answer + Reference Answer                       │
│          "A stack uses LIFO to manage data"                      │
│          "A stack is a LIFO data structure"                      │
│                                                                  │
│  Stage 1: Preprocessing                                          │
│  ├── Tokenization (NLTK word_tokenize)                          │
│  ├── POS Tagging (Penn Treebank → WordNet POS)                  │
│  └── Content Word Filtering (nouns, verbs, adjectives)          │
│                                                                  │
│  Stage 2: Word Sense Disambiguation    ◄── EXPERIMENTAL VARIABLE │
│  ├── Condition A: Lesk algorithm (baseline)                     │
│  ├── Condition B: Qwen-2.5 (7B)                                │
│  ├── Condition C: Mistral-7B-Instruct                           │
│  ├── Condition D: Llama-3.1-8B-Instruct                        │
│  └── Condition E: Gemini-1.5-Flash                              │
│  Output: Each content word → WordNet synset ID                  │
│                                                                  │
│  Stage 3: Sense Vector Lookup                                    │
│  └── Synset ID → SemSpace vector (300-dim)                      │
│      (Held constant across all conditions)                       │
│                                                                  │
│  Stage 4: Similarity Scoring                                     │
│  └── MaLSTM: Two sense-vector sequences → Manhattan distance    │
│      → Predicted score [0, 5]                                    │
│      (Held constant across all conditions)                       │
│                                                                  │
│  Output: Predicted grade (0-5 scale)                             │
└─────────────────────────────────────────────────────────────────┘

Figure 1: Pipeline architecture. Only Stage 2 (WSD) varies between conditions;
all other stages are identical, enabling attribution of performance differences
to the WSD component.
```

**Controlled variables.** Stages 1, 3, and 4 remain identical across all five experimental conditions. The same tokenization, POS tagging, SemSpace vectors, and MaLSTM weights are used regardless of which WSD method produced the synset assignments. This controlled substitution design ensures that any observed difference in ASAG performance is attributable solely to the WSD step.

**Independent variable.** The WSD method (5 levels: Lesk, Qwen-2.5, Mistral-7B, Llama-3.1-8B, Gemini-1.5-Flash).

**Dependent variables.** (1) WSD accuracy against gold standard (intrinsic), (2) ASAG Pearson correlation and RMSE against human grades (extrinsic).

### 3.2 Gold Standard Construction

To evaluate WSD accuracy, we construct a gold standard of manually annotated word senses for polysemous words in the Mohler dataset.

**Sampling strategy.** From the full set of polysemous content words (those with ≥ 2 WordNet synsets), we draw a stratified sample of 500 words:

| Ambiguity Level | Synsets | Sample Size | Rationale |
|----------------|---------|-------------|-----------|
| Low | 2-3 | 200 | Most common; establishes baseline |
| Medium | 4-7 | 200 | Core challenge for WSD |
| High | 8+ | 100 | Stress-tests disambiguation |

Additional stratification ensures representation across:
- Question topics (data structures, algorithms, OS concepts, etc.)
- Parts of speech (nouns, verbs, adjectives)
- Domain specificity (CS-specific terms vs. general vocabulary)

**Annotation process.** Two annotators — both computer science researchers familiar with the Mohler dataset's domain — independently assign the correct WordNet synset for each word in its sentence context. The annotation interface presents:
- The target word highlighted in its full sentence context
- The question to which the student was responding (providing topical context)
- All candidate synsets with their WordNet glosses and example sentences
- An option for "none of the senses fit" (recorded but excluded from evaluation)

**AI-assisted pre-annotation.** To accelerate the process, we use a separate LLM (distinct from the four being evaluated) to pre-annotate cases with high estimated confidence: words with only two senses where one is clearly domain-inappropriate, and CS-specific terms where the technical sense is unambiguous. Pre-annotations are clearly marked and must be explicitly approved or corrected by human annotators.

**Agreement measurement.** We report Cohen's κ for inter-annotator agreement, computed overall and stratified by ambiguity level and domain specificity. Disagreements are resolved through discussion; unresolvable cases are adjudicated by a third annotator. We target κ > 0.7 (substantial agreement) and require κ > 0.6 (moderate agreement) as a minimum threshold.

### 3.3 LLM-Based WSD: Prompt Design

We design four prompt variants, informed by best practices from Yae et al. [9], to systematically evaluate how prompt structure affects WSD accuracy.

**Prompt P1 — Basic (Synset ID + Gloss)**

```
Given the sentence: "{sentence}"
The word "{word}" (as a {pos}) can have these meanings:
1. {synset_1_id}: {gloss_1}
2. {synset_2_id}: {gloss_2}
...
Which meaning number best fits the word in this sentence?
Answer with only the number.
```

**Prompt P2 — With Examples**

Extends P1 by appending WordNet example sentences for each synset:
```
1. {synset_1_id}: {gloss_1}
   Examples: {example_sentences_1}
```

**Prompt P3 — Domain-Primed**

Prepends domain context:
```
You are analyzing a student's answer to a computer science exam question.
The exam question was: "{question_text}"
[... rest follows P2 format ...]
```

**Prompt P4 — Chain-of-Thought**

Instructs step-by-step reasoning:
```
[... P3 preamble ...]
Think step by step:
1. What is the sentence about?
2. What role does "{word}" play in this sentence?
3. Which meaning best matches?
Provide your reasoning, then state your final answer as a single number on the last line.
```

**LLM configurations.** All models are run with temperature = 0.0 for reproducibility. For P1-P3, max_tokens = 10 (expecting a single number). For P4, max_tokens = 300 (to accommodate reasoning). Responses are parsed to extract the final integer; unparseable responses are flagged and the Lesk result is used as fallback (with fallback rate reported).

### 3.4 Evaluation Protocol

**Intrinsic evaluation (WSD quality).** For each WSD method, we compute:
- **Accuracy**: proportion of correctly disambiguated words against the gold standard
- **Accuracy by stratum**: broken down by ambiguity level (low/medium/high), POS, and domain specificity
- **Statistical comparison**: McNemar's test [27] for pairwise comparison between methods, with Bonferroni correction for 10 pairwise comparisons (5 methods, C(5,2) = 10 pairs). Effect size measured via Cohen's h for proportion differences.

**Extrinsic evaluation (ASAG quality).** For each WSD condition, the full pipeline produces a predicted score for each of 2,273 student answers. We compute:
- **Aggregate Pearson r**: correlation between predicted and human-assigned scores across all answers
- **Per-question Pearson r**: correlation computed within each of 87 questions separately
- **RMSE**: root mean squared error between predicted and actual scores
- **Statistical comparison**: paired t-test and Wilcoxon signed-rank test on per-question Pearson values, with Cohen's d for effect size

**Error cascade analysis.** For answers where the WSD method produced different synset assignments than Lesk:
- Trace the changed synset → changed SemSpace vector → changed MaLSTM score → changed grade
- Categorize WSD errors into a taxonomy (Section 5.3)
- Quantify the proportion of ASAG score variance attributable to WSD differences

**Practical evaluation.** We additionally report:
- Disambiguation latency (seconds per word) for each method
- Total pipeline throughput (answers per minute)
- API cost for cloud-based models
- Parse success rate (proportion of LLM responses that yield a valid synset number)

---

## TDW Verification

| Test ID | Criterion | Status |
|---------|----------|--------|
| MTD-01 | Pipeline diagram present (with WSD step highlighted) | ✅ Figure 1 (ASCII) |
| MTD-02 | Independent, controlled, and dependent variables listed | ✅ Explicitly labeled |
| MTD-03 | Dataset described | ✅ In 3.1 and 3.2 (Mohler, 87Q, 2273A) |
| MTD-04 | Gold standard: sampling, annotation, agreement | ✅ Section 3.2 in full |
| MTD-05 | All 4 prompt variants shown with examples | ✅ P1-P4 with templates |
| MTD-06 | LLM configurations: model, version, size, temp | ✅ End of 3.3 |
| MTD-07 | Evaluation metrics defined | ✅ Section 3.4 |
| MTD-08 | Statistical tests justified | ✅ McNemar + Bonferroni, paired t + Wilcoxon |
| MTD-09 | Reproducible without contacting authors | ✅ Full detail provided |
| MTD-10 | Ethical considerations addressed | ✅ In frontmatter; data is public |

---

*Section status: DRAFT COMPLETE — Figure 1 to be replaced with publication-quality diagram*
