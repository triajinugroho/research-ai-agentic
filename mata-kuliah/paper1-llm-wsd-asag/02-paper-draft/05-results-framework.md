# Section 5: Results

> **Target length:** 2.5 pages (IEEE two-column) | ~2,000 words
> **TDW tests:** RES-01 through RES-12
> **Note:** This section contains result TEMPLATES with [TBD] placeholders to be filled after experiments.

---

## 5. Results

We present results across three evaluation dimensions: intrinsic WSD accuracy (5.1), extrinsic ASAG performance (5.2), and diagnostic error analysis (5.3). We additionally report prompt sensitivity (5.4) and practical considerations (5.5).

### 5.1 Intrinsic WSD Evaluation

**Table 4: WSD Accuracy on 500-Word Gold Standard**

| WSD Method | Overall Acc. | Low Amb. (2-3) | Med Amb. (4-7) | High Amb. (8+) | CS-Specific | General |
|-----------|-------------|----------------|----------------|---------------|-------------|---------|
| Lesk (baseline) | [TBD]% | [TBD]% | [TBD]% | [TBD]% | [TBD]% | [TBD]% |
| Qwen-2.5 | [TBD]% | [TBD]% | [TBD]% | [TBD]% | [TBD]% | [TBD]% |
| Mistral-7B | [TBD]% | [TBD]% | [TBD]% | [TBD]% | [TBD]% | [TBD]% |
| Llama-3.1-8B | [TBD]% | [TBD]% | [TBD]% | [TBD]% | [TBD]% | [TBD]% |
| Gemini-1.5-Flash | [TBD]% | [TBD]% | [TBD]% | [TBD]% | [TBD]% | [TBD]% |

*Best result in each column is bolded. Results marked with * are statistically significant vs. Lesk (p < 0.05, McNemar's test, Bonferroni-corrected).*

**Narrative template:** [BEST_LLM] achieves the highest overall accuracy at [X]%, representing a [Y] percentage-point improvement over the Lesk baseline ([Z]%). The improvement is most pronounced for [high/medium]-ambiguity words, where [BEST_LLM] correctly disambiguates [A]% compared to [B]% for Lesk (McNemar χ² = [C], p = [D]). For CS-specific terms, [the pattern holds / reverses / shows no significant difference], suggesting that [interpretation].

**Table 5: Pairwise Statistical Comparisons (McNemar's Test, Bonferroni-Corrected)**

| Comparison | χ² | p-value | Cohen's h | Significant? |
|-----------|-----|---------|-----------|-------------|
| Lesk vs Qwen | [TBD] | [TBD] | [TBD] | [TBD] |
| Lesk vs Mistral | [TBD] | [TBD] | [TBD] | [TBD] |
| Lesk vs Llama | [TBD] | [TBD] | [TBD] | [TBD] |
| Lesk vs Gemini | [TBD] | [TBD] | [TBD] | [TBD] |
| Qwen vs Mistral | [TBD] | [TBD] | [TBD] | [TBD] |
| Qwen vs Llama | [TBD] | [TBD] | [TBD] | [TBD] |
| Qwen vs Gemini | [TBD] | [TBD] | [TBD] | [TBD] |
| Mistral vs Llama | [TBD] | [TBD] | [TBD] | [TBD] |
| Mistral vs Gemini | [TBD] | [TBD] | [TBD] | [TBD] |
| Llama vs Gemini | [TBD] | [TBD] | [TBD] | [TBD] |

**Figure 2: WSD Accuracy by Ambiguity Level**
```
[Bar chart placeholder]
- X-axis: WSD Method (5 bars per group)
- Y-axis: Accuracy (%)
- Groups: Low / Medium / High ambiguity
- Error bars: 95% confidence intervals
- Format: Grouped bar chart, colorblind-safe palette
```

### 5.2 Extrinsic ASAG Evaluation

Using the best prompt variant per LLM (determined in Section 5.4), we run the full pipeline on all 2,273 answers and compare predicted scores against human grades.

**Table 6: ASAG Performance (Main Result Table)**

| WSD Condition | Agg. Pearson r | p-value | Agg. RMSE | Mean Per-Q r | Median Per-Q r |
|--------------|---------------|---------|-----------|-------------|---------------|
| Lesk (baseline) | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Qwen-2.5 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Mistral-7B | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Llama-3.1-8B | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Gemini-1.5-Flash | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Tulu et al. [4]* | 0.15 | — | ~1.0 | — | — |

*\* Published reference numbers for comparison; may differ from our Lesk baseline due to implementation differences.*

**Narrative template:** Replacing Lesk with [BEST_LLM] [improves / does not significantly change / yields mixed results for] aggregate Pearson correlation, [increasing it from X to Y / leaving it at X]. The per-question analysis reveals [a more nuanced picture]: [BEST_LLM] improves correlation for [N] of 87 questions, degrades it for [M], and shows negligible change for the remainder. The paired Wilcoxon signed-rank test [is / is not] significant (W = [TBD], p = [TBD], Cohen's d = [TBD]).

**Table 7: Statistical Tests for ASAG Improvement**

| Comparison | Paired t | p | Wilcoxon W | p | Cohen's d | Direction |
|-----------|---------|---|-----------|---|-----------|-----------|
| Lesk → Qwen | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Lesk → Mistral | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Lesk → Llama | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Lesk → Gemini | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |

**Figure 3: Per-Question Pearson r Distribution**
```
[Box plot placeholder]
- X-axis: WSD Condition (5 boxes)
- Y-axis: Per-question Pearson r
- Show median, IQR, outliers
- Horizontal dashed line at r = 0 (baseline reference)
```

**Figure 4: Scatter Plot — WSD Accuracy vs. ASAG Improvement**
```
[Scatter plot placeholder]
- X-axis: WSD accuracy on gold standard (%)
- Y-axis: Change in aggregate Pearson r (vs Lesk)
- Each point = one LLM condition
- Annotate each point with model name
- Fit trend line if meaningful (R² > 0.5)
```

### 5.3 Error Cascade Analysis

To answer RQ3, we trace WSD differences through the pipeline to identify which disambiguation errors have the greatest impact on grading.

**Error taxonomy.** We classify WSD disagreements between Lesk and the best-performing LLM into four categories:

| Error Type | Description | Count | % | Mean ASAG Δ |
|-----------|------------|-------|---|-------------|
| **A: Domain confusion** | CS term → general sense (or vice versa) | [TBD] | [TBD]% | [TBD] |
| **B: POS ambiguity** | Noun sense selected for verb usage (or vice versa) | [TBD] | [TBD]% | [TBD] |
| **C: Fine-grained confusion** | Similar senses confused (e.g., two programming-related senses) | [TBD] | [TBD]% | [TBD] |
| **D: OOV / fallback** | Different fallback behavior for unknown words | [TBD] | [TBD]% | [TBD] |

**Case Study 1: Domain Confusion (High Impact)**
> Student answer: "[actual sentence from dataset]"
> Word: "[word]" — Lesk selected synset `[X]` ("[general gloss]"), LLM selected `[Y]` ("[CS-specific gloss]")
> SemSpace vector cosine distance between synsets: [TBD]
> Score change: [old] → [new] (human grade: [actual])
> **Interpretation:** [Why the LLM's choice better captures the intended meaning]

**Case Study 2: [TBD after experiments]**

**Case Study 3: [TBD after experiments]**

**Figure 5: Error Type Distribution by LLM**
```
[Stacked bar chart placeholder]
- X-axis: LLM model
- Y-axis: Count of WSD disagreements with Lesk
- Stack colors: Error types A, B, C, D
```

### 5.4 Prompt Sensitivity Analysis

**Table 8: WSD Accuracy by Prompt Variant (Best LLM Only)**

| Prompt Variant | Description | Accuracy | Δ vs P1 |
|---------------|------------|----------|---------|
| P1: Basic | Synset + gloss | [TBD]% | baseline |
| P2: With examples | + example sentences | [TBD]% | [TBD] |
| P3: Domain-primed | + CS exam context | [TBD]% | [TBD] |
| P4: Chain-of-thought | + step-by-step reasoning | [TBD]% | [TBD] |

**Narrative template:** Domain-primed prompting (P3) [provides / does not provide] a meaningful advantage over basic prompting, suggesting that [providing exam context helps LLMs narrow the sense space / LLMs are robust enough to determine domain from the sentence alone]. Chain-of-thought (P4) [helps / hurts / has no effect], which [aligns with / contradicts] Yae et al.'s finding that structured prompts benefit smaller models.

### 5.5 Practical Considerations

**Table 9: Throughput and Cost**

| Method | Time/word (s) | Time/answer (s) | Pipeline throughput (ans/min) | Cost per 1K words |
|--------|-------------|----------------|------------------------------|-------------------|
| Lesk | [TBD] | [TBD] | [TBD] | $0 (local) |
| Qwen-2.5 | [TBD] | [TBD] | [TBD] | $0 (local) |
| Mistral-7B | [TBD] | [TBD] | [TBD] | $0 (local) |
| Llama-3.1-8B | [TBD] | [TBD] | [TBD] | $0 (local) |
| Gemini-1.5-Flash | [TBD] | [TBD] | [TBD] | ~$[TBD] (API) |

---

## Summary of Key Findings

| RQ | Finding |
|-----|---------|
| RQ1 | [BEST_LLM] achieves [X]% WSD accuracy vs [Y]% for Lesk (p = [Z]) |
| RQ2 | LLM-WSD [improves / does not change] ASAG performance: Pearson r [from X to Y] |
| RQ3 | Domain confusion errors (Type A) have the highest impact on grading; [BEST_LLM] reduces these by [N]% |

---

*Section status: TEMPLATE — All [TBD] values to be filled after Sprint 3-4 experiments*
