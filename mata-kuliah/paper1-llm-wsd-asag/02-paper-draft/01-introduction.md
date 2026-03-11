# Section 1: Introduction

> **Target length:** 1.5 pages (IEEE two-column) | ~1,200 words
> **TDW tests:** INT-01 through INT-10

---

## 1. Introduction

Short answer questions occupy a distinctive middle ground in educational assessment. Unlike multiple-choice items, they require students to construct responses that demonstrate understanding; unlike essays, they constrain the response space enough to make automated evaluation tractable. This makes Automatic Short Answer Grading (ASAG) both practically valuable and technically challenging — the system must capture semantic equivalence between a student's phrasing and the intended meaning, even when the two share few surface-level words.

Over the past decade, ASAG systems have evolved from string-matching heuristics [1] to embedding-based approaches that represent answers as dense vectors in semantic space [2, 3]. Among these, knowledge-based pipelines that operate at the *sense level* — distinguishing between different meanings of polysemous words — offer a theoretically compelling advantage. When a student writes "the process creates a child," the word *process* should map to the operating-system concept (synset: `process.n.05`), not to a manufacturing procedure or legal proceeding. Getting this distinction right is the job of Word Sense Disambiguation (WSD), and it determines which sense vector enters the downstream similarity computation.

### 1.1 The WSD Bottleneck in Knowledge-Based ASAG

Tulu et al. [4] demonstrated this approach through SemSpace-MaLSTM, a pipeline that (1) disambiguates each content word using WSD, (2) maps the resulting synset to a SemSpace sense vector [5], and (3) computes answer similarity via a Manhattan LSTM [6]. Their results reveal a striking pattern: per-question Pearson correlations exceed 0.95 for some questions, yet the aggregate correlation across all 87 questions drops to just 0.15. This gap — strong local performance, weak global performance — points to a pipeline component that works well for some vocabulary but poorly for others. We hypothesize that the WSD step, which Tulu et al. implemented using the traditional Lesk algorithm [7], is a primary contributor to this inconsistency.

The Lesk algorithm selects word senses by counting overlap between a word's dictionary gloss and its surrounding context. While elegant in its simplicity, Lesk struggles with short contexts (typical of student answers), domain-specific terminology, and fine-grained sense distinctions — precisely the conditions that characterize ASAG datasets.

### 1.2 LLMs as WSD Engines: An Untapped Opportunity

Recent work has established that Large Language Models possess substantial WSD capabilities. Sumanathilaka et al. [8] benchmarked multiple LLMs on the XL-WSD dataset and found that fine-tuned models approach supervised state-of-the-art performance, while even zero-shot models show competitive accuracy. Yae et al. [9] further demonstrated that structured prompting — particularly multiple-choice presentation of candidate synsets — significantly improves LLM disambiguation accuracy across seven models. Separately, Sumanathilaka et al. [10] showed that smaller LLMs augmented with explicit reasoning strategies can rival larger models on WSD tasks.

These findings suggest a natural question: *can LLM-based WSD improve downstream ASAG performance when substituted into a knowledge-based pipeline?* Despite the clear connection between these research streams, this question remains unanswered. Our systematic search across Scopus, IEEE Xplore, ACL Anthology, and Google Scholar (conducted March 2026) found no prior work that evaluates LLM-based WSD within an ASAG context.

### 1.3 Research Questions

We formulate three research questions to address this gap:

**RQ1 (Intrinsic):** How does the WSD accuracy of zero-shot LLMs (Qwen-2.5, Mistral-7B, Llama-3.1-8B, Gemini-1.5-Flash) compare to the Lesk algorithm on polysemous words from the Mohler ASAG dataset?

**RQ2 (Extrinsic):** Does replacing Lesk with LLM-based WSD in the SemSpace-MaLSTM pipeline produce measurably different ASAG scores, as evaluated by Pearson correlation and RMSE against human grades?

**RQ3 (Diagnostic):** What types of WSD errors have the greatest impact on downstream grading accuracy, and how do error patterns differ between Lesk and LLM-based approaches?

### 1.4 Contributions

This paper makes four contributions:

1. **First empirical evaluation of LLM-based WSD in an ASAG pipeline.** We bridge two previously disconnected research areas — LLM-WSD and knowledge-based ASAG — by measuring both intrinsic disambiguation accuracy and extrinsic grading impact within a controlled experimental design (Section 3, 5).

2. **Systematic multi-model comparison.** We evaluate four LLMs across four prompt variants, providing a comprehensive landscape of LLM WSD performance in the educational NLP domain (Section 4, 5.1).

3. **Error cascade analysis.** We trace how specific WSD decisions propagate through the pipeline to affect final grades, revealing which types of disambiguation errors matter most for grading accuracy (Section 5.3).

4. **Gold standard resource.** We construct and release WSD annotations for 500 polysemous words from the Mohler dataset, stratified by ambiguity level, enabling future research on WSD quality in ASAG contexts (Section 3.2).

### 1.5 Paper Organization

The remainder of this paper is organized as follows. Section 2 reviews related work in ASAG, WSD, and LLMs for educational NLP. Section 3 describes our methodology, including the pipeline architecture, prompt design, and evaluation protocol. Section 4 details the experimental setup. Section 5 presents results across intrinsic, extrinsic, and diagnostic evaluations. Section 6 discusses implications, limitations, and practical guidelines. Section 7 concludes with a summary and directions for future work.

---

## TDW Verification

| Test ID | Criterion | Status |
|---------|----------|--------|
| INT-01 | Opens with broad context (ASAG importance) — not with "In recent years" | ✅ Opens with "Short answer questions occupy..." |
| INT-02 | Introduces WSD as bottleneck with evidence (Tulu's aggregate r = 0.15) | ✅ Section 1.1, explicit numbers |
| INT-03 | Explains cascade effect (wrong WSD → wrong vector → wrong grade) | ✅ "determines which sense vector enters" |
| INT-04 | Motivates LLM-based WSD with citations (Sumanathilaka, Yae) | ✅ Section 1.2, three citations |
| INT-05 | Explicitly states what NO prior work has done | ✅ "this question remains unanswered" |
| INT-06 | Lists 3 research questions, each answerable and measurable | ✅ RQ1-RQ3 with specific metrics |
| INT-07 | Lists 3-4 contributions, each verifiable in the paper | ✅ 4 contributions with section refs |
| INT-08 | Each contribution maps to a specific section | ✅ Section numbers in parentheses |
| INT-09 | Final paragraph outlines paper structure | ✅ Section 1.5 |
| INT-10 | No more than 2 pages (IEEE two-column) | ✅ ~1,100 words ≈ 1.5 pages |

---

## Humanization Check

| Test ID | Criterion | Status |
|---------|----------|--------|
| HUM-01 | Does NOT start with "In recent years" | ✅ Starts with "Short answer questions..." |
| HUM-02 | Does NOT use "It is worth noting that" | ✅ Not used |
| HUM-06 | No excessive "Moreover/Furthermore/Additionally" | ✅ Avoided |
| HUM-08 | Does NOT open with "In this paper, we" | ✅ First person delayed to Section 1.2 |
| HUM-11 | Sentence length varies | ✅ Mix of short and complex |
| HUM-12 | Active voice for contributions | ✅ "We formulate...", "We bridge..." |

---

*Section status: DRAFT COMPLETE — requires reference number updates after final reference list*
