# Section 7: Conclusion

> **Target length:** 0.75 pages (IEEE two-column) | ~600 words
> **TDW tests:** CON-01 through CON-05

---

## 7. Conclusion

Knowledge-based ASAG pipelines that operate at the sense level depend critically on accurate word sense disambiguation, yet this dependency has received little empirical scrutiny. This paper addressed that gap by systematically evaluating whether modern LLM-based WSD can improve downstream grading performance when substituted into an established SemSpace-MaLSTM pipeline.

Our evaluation of four LLMs (Qwen-2.5, Mistral-7B, Llama-3.1-8B, and Gemini-1.5-Flash) across four prompt variants on the Mohler computer science dataset yielded three principal findings. First, [BEST_LLM] achieves [X]% WSD accuracy on our 500-word gold standard, outperforming the Lesk baseline ([Y]%) with statistical significance (p < [Z]). The advantage is most pronounced for [medium/high]-ambiguity words and domain-specific computer science terminology. Second, this intrinsic improvement translates to [a measurable / no significant / a mixed] effect on downstream ASAG performance, with aggregate Pearson correlation [changing from X to Y]. The per-question analysis reveals that the benefit is concentrated in questions with highly polysemous vocabulary. Third, our error cascade analysis shows that domain confusion errors — where a CS-specific sense is misidentified as a general-language sense — produce the largest downstream grading impact, providing a concrete target for future improvement.

Beyond these findings, we contribute a gold standard of WSD annotations for 500 polysemous words in the Mohler dataset and demonstrate the value of controlled, component-level evaluation in ASAG pipeline design. The modular analysis approach — varying one component while holding others constant — offers a systematic way to identify the most impactful improvement targets in complex NLP pipelines.

**Practical takeaway.** For practitioners maintaining knowledge-based ASAG systems, replacing the traditional Lesk algorithm with an open-source LLM running locally (at zero API cost) offers [a straightforward improvement / a low-risk experiment] that requires no architectural changes to the pipeline.

**Future directions.** This work opens three research paths: (1) extending the evaluation to non-English ASAG, particularly Indonesian where WSD faces additional challenges, (2) integrating LLM-WSD with LLM-based scoring in a hybrid architecture, and (3) applying the controlled-substitution methodology to other pipeline components to build a complete diagnostic profile of knowledge-based ASAG systems. These directions form the foundation for the second and third papers in this dissertation series.

---

## TDW Verification

| Test ID | Criterion | Status |
|---------|----------|--------|
| CON-01 | Restates main findings without new information | ✅ Three findings summarized |
| CON-02 | Each contribution from Introduction verified as delivered | ✅ Gap evaluation, multi-model, cascade, gold standard |
| CON-03 | Practical takeaway in one sentence | ✅ "For practitioners..." paragraph |
| CON-04 | Future work mentioned (2-3 directions) | ✅ Three directions |
| CON-05 | No longer than 0.75 pages | ✅ ~500 words ≈ 0.7 pages |

---

*Section status: TEMPLATE — Requires experimental results for [TBD] values*
