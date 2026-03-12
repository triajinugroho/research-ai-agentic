# Section 6: Discussion

> **Target length:** 2.0 pages (IEEE two-column) | ~1,600 words
> **TDW tests:** DIS-01 through DIS-08

---

## 6. Discussion

### 6.1 Answering the Research Questions

**RQ1: LLM WSD Accuracy vs. Lesk.** Our results demonstrate that [BEST_LLM] outperforms the Lesk algorithm on WSD accuracy by [X] percentage points, with the advantage concentrated in [medium/high]-ambiguity words. This finding extends the work of Sumanathilaka et al. [8] and Yae et al. [9] — who established LLM WSD competence on general-domain benchmarks — to the educational domain. The advantage appears to stem from [LLMs' ability to leverage broader contextual understanding / domain knowledge encoded during pre-training / better handling of short contexts], rather than from systematic differences in error patterns.

Notably, [LLM performance on CS-specific terms was particularly strong / showed no significant advantage over Lesk for CS-specific terms], suggesting that [pre-training corpora contain sufficient CS knowledge for domain-specific WSD / domain specificity remains a challenge even for LLMs]. This has practical implications for deploying LLM-WSD in subject-specific ASAG systems: [domain-primed prompting (P3) partially addresses this / additional domain adaptation may be necessary].

**RQ2: Downstream Impact on ASAG.** The relationship between WSD quality and ASAG performance is [stronger / weaker / more nuanced] than we initially hypothesized. While [BEST_LLM] improves aggregate Pearson r from [X to Y], the improvement is [statistically significant / not significant / significant only for a subset of questions]. The per-question analysis reveals an important pattern: LLM-WSD provides the largest grading improvements for questions whose answers contain [highly polysemous vocabulary / domain-specific terms / longer answers], where traditional WSD is most likely to err.

This finding carries a diagnostic implication that goes beyond the specific performance numbers. If WSD quality had no effect on ASAG performance, it would suggest that the pipeline's bottleneck lies elsewhere — in the sense vectors, the similarity model, or the scoring function. Our results indicate that WSD [is / is not / is partially] a limiting factor, which [supports / undermines / qualifies] the value of continued investment in improving the WSD component of knowledge-based ASAG systems.

**RQ3: Error Cascade Patterns.** The error cascade analysis reveals that not all WSD errors are created equal from a grading perspective. Domain confusion errors (Type A) — where a CS-specific sense is replaced by a general-language sense — have [disproportionately large / moderate / surprisingly small] impact on downstream scores, because the resulting sense vectors are [far apart / moderately distant / sometimes close] in SemSpace. By contrast, fine-grained confusion (Type C) between related senses often produces [minimal score change because the SemSpace vectors for related senses are similar / surprising large changes due to...].

This finding has practical value for ASAG system design: improving WSD accuracy on [domain-specific terms / highly polysemous words / Type A error cases] would yield the greatest downstream benefit, while perfect disambiguation of fine-grained distinctions may not justify the additional computational cost.

### 6.2 Implications for ASAG System Design

Our results suggest three practical guidelines for researchers and practitioners building knowledge-based ASAG systems:

1. **WSD matters, but selectively.** Not every word needs perfect disambiguation. System designers should prioritize WSD quality for domain-specific terms and highly polysemous words, where errors propagate most strongly through the pipeline.

2. **LLMs offer a viable WSD upgrade path.** For existing pipelines that use traditional WSD (Lesk, UKB), substituting an LLM-based WSD engine [requires minimal architectural change / can be done as a drop-in replacement] and provides [meaningful / modest] improvements. The local open-source models we tested achieve this at zero API cost.

3. **Modular analysis reveals actionable insights.** Our controlled substitution design demonstrates the value of evaluating pipeline components individually, rather than treating the system as a monolithic black box. This approach can be applied to other pipeline components (e.g., the similarity function, the scoring model) to identify the most impactful improvement targets.

### 6.3 Relationship to End-to-End LLM Grading

A natural question arises: if LLMs are powerful enough to perform WSD, why not use them for end-to-end ASAG? Recent work by Ferreira Mello et al. [22] shows that GPT-4 can grade short answers competitively without any pipeline. Our work does not contradict this finding — it addresses a different question.

Pipeline-based ASAG and end-to-end LLM grading serve different needs. Pipelines offer *interpretability*: an instructor can inspect which senses were assigned, how the answer was represented, and where the system's judgment diverged. They also offer *component-level improvement*: as we demonstrate, upgrading a single module yields measurable gains. End-to-end systems offer *simplicity* and often *higher absolute performance*, but provide limited insight into *why* a grade was assigned.

We view these approaches as complementary, not competing. Our error cascade analysis could inform end-to-end systems as well — for instance, by identifying the types of semantic distinctions that are most critical for grading, which could guide prompt design or fine-tuning for LLM-as-judge approaches.

### 6.4 Limitations

We acknowledge several limitations of this study:

1. **Single dataset.** Our evaluation uses only the Mohler dataset (computer science, English). Results may not generalize to other domains (biology, history) or languages. Cross-domain evaluation is needed.

2. **Zero-shot only.** We evaluate LLMs in a zero-shot setting without fine-tuning. Fine-tuned models, or few-shot approaches with sense-annotated examples, would likely achieve higher WSD accuracy. Our results establish a lower bound for LLM-WSD capability in this context.

3. **SemSpace dependency.** The extrinsic evaluation is mediated by SemSpace vectors and MaLSTM, which have their own limitations. Improvements in WSD may be attenuated or amplified by the vector space's structure. Different sense embedding methods might show different sensitivity to WSD quality.

4. **Gold standard size.** Our gold standard covers 500 words, a sample from the full dataset. While stratified and sufficient for statistical testing, it does not cover every word the pipeline disambiguates. Edge cases outside the sample may exhibit different patterns.

5. **Model snapshot.** LLMs are rapidly evolving. Our results reflect specific model versions available in [month] 2026. Newer models may perform differently, though the experimental framework itself remains applicable.

6. **Quantized models.** The open-source models were run in Q4_K_M quantization for practical reasons. Full-precision inference might yield slightly different results, though prior work suggests quantization effects on classification tasks are modest.

### 6.5 Future Work

Three directions emerge naturally from this study:

1. **Paper 2 context — Cross-lingual ASAG.** Extending this evaluation to Indonesian-language short answers, where WSD presents additional challenges due to limited WordNet coverage and morphological complexity.

2. **Paper 3 context — Hybrid pipeline.** Integrating LLM-based WSD with LLM-based scoring in a unified but still modular architecture (NS-XASAG), combining the interpretability of pipeline approaches with the flexibility of LLMs.

3. **Beyond WSD.** Applying the same controlled-substitution methodology to other pipeline components — the sense embedding method, the similarity function, the scoring model — to build a complete diagnostic profile of knowledge-based ASAG systems.

---

## TDW Verification

| Test ID | Criterion | Status |
|---------|----------|--------|
| DIS-01 | Each RQ discussed with interpretation | ✅ 6.1 covers all three |
| DIS-02 | Results connected to prior work | ✅ References Sumanathilaka, Yae, Ferreira Mello |
| DIS-03 | Unexpected findings discussed | ✅ Template includes surprise patterns |
| DIS-04 | Practical implications stated | ✅ Section 6.2 — three guidelines |
| DIS-05 | Limitations with at least 5 honest limitations | ✅ Six limitations in 6.4 |
| DIS-06 | No overclaiming — hedging language | ✅ "suggests", "may", brackets for uncertainty |
| DIS-07 | Future work specific and actionable | ✅ Section 6.5 — three concrete directions |
| DIS-08 | Connection to broader landscape | ✅ Section 6.3 — pipeline vs end-to-end |

---

*Section status: TEMPLATE — Requires experimental results to fill [TBD] values and refine interpretation*
