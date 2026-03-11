# Test-Driven Writing (TDW) Protocol

## 1. What is Test-Driven Writing?

Inspired by Test-Driven Development (TDD) in software engineering:

```
TDD: Write test → Write code → Verify test passes
TDW: Define acceptance criteria → Write section → Verify criteria met
```

Every section of the paper is written against **pre-defined acceptance tests**. A section is "done" only when ALL tests pass. This ensures completeness, consistency, and defensibility.

---

## 2. Section-Level Acceptance Tests

### 2.1 Abstract

| Test ID | Criterion | Pass/Fail |
|---------|----------|-----------|
| ABS-01 | Contains specific problem statement (WSD bottleneck in ASAG) | ☐ |
| ABS-02 | States exactly 4 LLMs evaluated (named) | ☐ |
| ABS-03 | Contains at least 2 quantitative results (accuracy %, Pearson r) | ☐ |
| ABS-04 | States main finding in one sentence | ☐ |
| ABS-05 | Contains practical implication statement | ☐ |
| ABS-06 | Word count ≤ 250 | ☐ |
| ABS-07 | Keywords listed (5-7) | ☐ |
| ABS-08 | No citations in abstract | ☐ |
| ABS-09 | No abbreviations used without definition | ☐ |

### 2.2 Introduction

| Test ID | Criterion | Pass/Fail |
|---------|----------|-----------|
| INT-01 | Opens with broad context (ASAG importance) — not with "In recent years" | ☐ |
| INT-02 | Introduces WSD as bottleneck with evidence (Tulu's aggregate r = 0.15) | ☐ |
| INT-03 | Explains cascade effect (wrong WSD → wrong vector → wrong grade) | ☐ |
| INT-04 | Motivates LLM-based WSD with citations (Sumanathilaka, Yae) | ☐ |
| INT-05 | Explicitly states what NO prior work has done (3 gaps) | ☐ |
| INT-06 | Lists 3 research questions, each answerable and measurable | ☐ |
| INT-07 | Lists 3-4 contributions, each verifiable in the paper | ☐ |
| INT-08 | Each contribution maps to a specific section | ☐ |
| INT-09 | Final paragraph outlines paper structure | ☐ |
| INT-10 | No more than 2 pages (IEEE two-column) | ☐ |

### 2.3 Related Work

| Test ID | Criterion | Pass/Fail |
|---------|----------|-----------|
| RW-01 | Covers ASAG literature (at least 5 papers) | ☐ |
| RW-02 | Covers WSD literature (at least 5 papers, traditional + modern) | ☐ |
| RW-03 | Covers LLM-WSD literature (at least 3 papers) | ☐ |
| RW-04 | Gap analysis table present (our paper vs all competitors) | ☐ |
| RW-05 | Each cited paper has: what they did, what they DIDN'T do | ☐ |
| RW-06 | Final paragraph explicitly states our unique position | ☐ |
| RW-07 | No "strawman" — competitors' strengths acknowledged | ☐ |
| RW-08 | Chronological or thematic organization (not random list) | ☐ |
| RW-09 | At least 20 references in this section | ☐ |

### 2.4 Methodology

| Test ID | Criterion | Pass/Fail |
|---------|----------|-----------|
| MTD-01 | Pipeline diagram present (with WSD step highlighted) | ☐ |
| MTD-02 | Independent, controlled, and dependent variables listed | ☐ |
| MTD-03 | Dataset described: size, source, domain, grading scale | ☐ |
| MTD-04 | Gold standard construction: sampling strategy, annotation process, agreement | ☐ |
| MTD-05 | All 4 prompt variants shown with examples | ☐ |
| MTD-06 | LLM configurations: model name, version, size, access method, temperature | ☐ |
| MTD-07 | Evaluation metrics defined with formulas | ☐ |
| MTD-08 | Statistical tests justified (why McNemar? why Wilcoxon?) | ☐ |
| MTD-09 | Reproducibility: enough detail to replicate without contacting authors | ☐ |
| MTD-10 | Ethical considerations addressed | ☐ |

### 2.5 Results

| Test ID | Criterion | Pass/Fail |
|---------|----------|-----------|
| RES-01 | Intrinsic WSD results: accuracy table with confidence intervals | ☐ |
| RES-02 | Statistical significance indicated for all comparisons | ☐ |
| RES-03 | Best LLM identified with quantitative evidence | ☐ |
| RES-04 | Extrinsic ASAG results: Pearson r and RMSE for all conditions | ☐ |
| RES-05 | Per-question analysis present (not just aggregate) | ☐ |
| RES-06 | WSD accuracy vs ASAG performance correlation shown | ☐ |
| RES-07 | Error analysis: taxonomy with counts and examples | ☐ |
| RES-08 | At least 3 case studies with narrative | ☐ |
| RES-09 | Prompt sensitivity results reported | ☐ |
| RES-10 | All figures are publication-quality (300 DPI, colorblind-safe) | ☐ |
| RES-11 | Numbers in text match numbers in tables | ☐ |
| RES-12 | Every RQ explicitly answered | ☐ |

### 2.6 Discussion

| Test ID | Criterion | Pass/Fail |
|---------|----------|-----------|
| DIS-01 | Each RQ discussed with interpretation (not just restate results) | ☐ |
| DIS-02 | Results connected to prior work (how do our findings relate to Sumanathilaka, Yae?) | ☐ |
| DIS-03 | Unexpected findings discussed and explained | ☐ |
| DIS-04 | Practical implications stated (who benefits and how) | ☐ |
| DIS-05 | Limitations section with at least 5 honest limitations | ☐ |
| DIS-06 | No overclaiming — hedging language used appropriately | ☐ |
| DIS-07 | Future work directions are specific and actionable | ☐ |
| DIS-08 | Connection to broader ASAG and educational NLP landscape | ☐ |

### 2.7 Conclusion

| Test ID | Criterion | Pass/Fail |
|---------|----------|-----------|
| CON-01 | Restates main findings without new information | ☐ |
| CON-02 | Each contribution from Introduction verified as delivered | ☐ |
| CON-03 | Practical takeaway in one sentence | ☐ |
| CON-04 | Future work mentioned (2-3 directions) | ☐ |
| CON-05 | No longer than 0.75 pages | ☐ |

### 2.8 References

| Test ID | Criterion | Pass/Fail |
|---------|----------|-----------|
| REF-01 | All in-text citations appear in reference list | ☐ |
| REF-02 | All references are cited in text (no orphan references) | ☐ |
| REF-03 | Each reference has: authors, year, title, venue, DOI/URL | ☐ |
| REF-04 | Format consistent (IEEE or APA per venue) | ☐ |
| REF-05 | At least 35 references total | ☐ |
| REF-06 | At least 60% of references from last 5 years (2021-2026) | ☐ |
| REF-07 | Key papers verified via Google Scholar (exist and correct) | ☐ |
| REF-08 | No predatory journal citations | ☐ |

---

## 3. Humanized Academic Writing Tests

### 3.1 Anti-AI Writing Patterns

| Test ID | Criterion | Pass/Fail |
|---------|----------|-----------|
| HUM-01 | Does NOT start any section with "In recent years" | ☐ |
| HUM-02 | Does NOT use "It is worth noting that" | ☐ |
| HUM-03 | Does NOT use "plays a crucial role" | ☐ |
| HUM-04 | Does NOT use "has garnered significant attention" | ☐ |
| HUM-05 | Does NOT use "In the realm of" | ☐ |
| HUM-06 | Does NOT overuse "Moreover" / "Furthermore" / "Additionally" as paragraph starters | ☐ |
| HUM-07 | Does NOT use "delve into" | ☐ |
| HUM-08 | Does NOT use "In this paper, we" as the first sentence | ☐ |
| HUM-09 | Does NOT have more than 3 consecutive paragraphs starting with "The" | ☐ |
| HUM-10 | Does NOT use "comprehensive" more than twice in entire paper | ☐ |

### 3.2 Good Academic Writing Patterns

| Test ID | Criterion | Pass/Fail |
|---------|----------|-----------|
| HUM-11 | Sentence length varies (mix of short punchy + longer complex) | ☐ |
| HUM-12 | Active voice used for our contributions ("We evaluate..." not "It is evaluated...") | ☐ |
| HUM-13 | Passive voice used appropriately for general facts | ☐ |
| HUM-14 | Technical terms defined on first use | ☐ |
| HUM-15 | Acronyms defined on first use, used consistently after | ☐ |
| HUM-16 | Transition sentences connect paragraphs logically | ☐ |
| HUM-17 | Each paragraph has one main idea | ☐ |
| HUM-18 | Specific numbers used instead of vague qualifiers ("improved by 12%" not "significantly improved") | ☐ |
| HUM-19 | Author voice is present but not informal | ☐ |
| HUM-20 | Hedging is appropriate: "suggests" for interpretation, "shows" for data | ☐ |

### 3.3 Defensibility Checks

| Test ID | Criterion | Pass/Fail |
|---------|----------|-----------|
| DEF-01 | Every claim has evidence (data or citation) | ☐ |
| DEF-02 | Every "significant" result has p-value | ☐ |
| DEF-03 | Limitations are honest, not token | ☐ |
| DEF-04 | Competitors are described fairly (no strawman) | ☐ |
| DEF-05 | Scope is clearly bounded (what we do AND what we don't do) | ☐ |
| DEF-06 | Contribution claims in Intro are all delivered in paper | ☐ |
| DEF-07 | No logical gaps between premises and conclusions | ☐ |
| DEF-08 | Figures and tables are referenced in text (no orphans) | ☐ |

---

## 4. Writing Workflow Per Section

```
For each section:

Step 1: REVIEW TESTS
  → Read all acceptance tests for this section
  → Understand what "done" looks like

Step 2: OUTLINE
  → Write bullet-point outline covering all test criteria
  → Ensure no test will be missed

Step 3: DRAFT
  → Write section following outline
  → Don't self-edit during drafting — just write

Step 4: SELF-TEST
  → Go through each test criterion
  → Mark Pass/Fail
  → Note which tests fail

Step 5: REVISE
  → Fix all failing tests
  → Re-run tests

Step 6: HUMANIZE
  → Run anti-AI writing checks (HUM-01 to HUM-10)
  → Run good writing checks (HUM-11 to HUM-20)
  → Revise for natural academic voice

Step 7: DEFEND
  → Run defensibility checks (DEF-01 to DEF-08)
  → Imagine hostile reviewer reading each sentence
  → Strengthen weak claims or add hedging

Step 8: SIGN OFF
  → All tests pass → section complete
```

---

## 5. Cross-Section Consistency Tests

| Test ID | Criterion | Pass/Fail |
|---------|----------|-----------|
| XS-01 | RQs in Introduction match RQs answered in Results and Discussion | ☐ |
| XS-02 | Contributions in Introduction match evidence in Results | ☐ |
| XS-03 | Methods described in Methodology match what's reported in Results | ☐ |
| XS-04 | Limitations discussed match actual experimental constraints | ☐ |
| XS-05 | Future work in Conclusion follows from limitations | ☐ |
| XS-06 | Abstract accurately summarizes all sections | ☐ |
| XS-07 | Table/figure numbering is sequential and all are referenced | ☐ |
| XS-08 | Terminology is consistent across all sections | ☐ |
| XS-09 | Dataset statistics match between Methodology and Results | ☐ |
| XS-10 | No section contradicts another section | ☐ |

---

## 6. Pre-Submission Final Checklist

| # | Item | Done? |
|---|------|-------|
| 1 | All section-level tests pass | ☐ |
| 2 | All cross-section tests pass | ☐ |
| 3 | All humanization tests pass | ☐ |
| 4 | All defensibility tests pass | ☐ |
| 5 | Spellcheck completed | ☐ |
| 6 | Grammar check completed | ☐ |
| 7 | All figures are high-resolution | ☐ |
| 8 | Page count within venue limit | ☐ |
| 9 | Author information correct | ☐ |
| 10 | Cover letter prepared | ☐ |
| 11 | Supplementary materials organized | ☐ |
| 12 | All co-authors have reviewed | ☐ |
| 13 | Venue formatting requirements met | ☐ |
| 14 | Conflict of interest declared | ☐ |
| 15 | Data availability statement included | ☐ |

---

*Document version: 1.0 — March 2026*
