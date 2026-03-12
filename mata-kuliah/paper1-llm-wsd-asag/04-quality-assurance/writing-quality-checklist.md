# Writing Quality Checklist

## 1. Humanized Academic Writing Standards

### 1.1 Sentence-Level Checks

| # | Check | How to Verify | Status |
|---|-------|--------------|--------|
| 1 | No section starts with "In recent years" | Ctrl+F | ☐ |
| 2 | No "It is worth noting that" | Ctrl+F | ☐ |
| 3 | No "plays a crucial role" | Ctrl+F | ☐ |
| 4 | No "has garnered significant attention" | Ctrl+F | ☐ |
| 5 | No "In the realm of" | Ctrl+F | ☐ |
| 6 | No "delve into" or "delves into" | Ctrl+F | ☐ |
| 7 | "Moreover" / "Furthermore" / "Additionally" used ≤3 times total | Ctrl+F count | ☐ |
| 8 | "comprehensive" used ≤2 times | Ctrl+F count | ☐ |
| 9 | No 3+ consecutive paragraphs starting with "The" | Manual scan | ☐ |
| 10 | No "utilize" (use "use" instead) | Ctrl+F | ☐ |
| 11 | No "leverage" as verb (use "use" or "exploit") | Ctrl+F | ☐ |
| 12 | No "paradigm shift" or "groundbreaking" | Ctrl+F | ☐ |
| 13 | First sentence of paper is NOT "In this paper, we..." | Manual check | ☐ |

### 1.2 Paragraph-Level Checks

| # | Check | Status |
|---|-------|--------|
| 14 | Each paragraph has exactly one main idea | ☐ |
| 15 | No paragraph exceeds 150 words (aim for 80-120) | ☐ |
| 16 | Transition sentences connect paragraphs logically | ☐ |
| 17 | Topic sentences are the first sentence of each paragraph | ☐ |
| 18 | No orphan paragraphs (single sentence) | ☐ |

### 1.3 Variety and Flow

| # | Check | Status |
|---|-------|--------|
| 19 | Sentence length varies (mix of 10-15 and 20-30 word sentences) | ☐ |
| 20 | Active voice for our contributions ("We evaluate..." not "It is evaluated...") | ☐ |
| 21 | Passive voice for general facts ("WSD has been studied..." is OK) | ☐ |
| 22 | No more than 2 passive-voice sentences in a row | ☐ |
| 23 | Specific numbers used instead of "significantly" or "substantially" | ☐ |

---

## 2. Technical Writing Standards

### 2.1 Terminology Consistency

| Term | Correct Form | Incorrect Forms |
|------|-------------|----------------|
| Word Sense Disambiguation | WSD (after first use) | word-sense disambiguation, word sense disambig. |
| Large Language Model | LLM (after first use) | large language model (after first use) |
| Automatic Short Answer Grading | ASAG (after first use) | auto grading, automatic grading |
| SemSpace-MaLSTM | SemSpace-MaLSTM (always) | Semspace, SEMSPACE, Ma-LSTM |
| Pearson r | Pearson r (italic r) | Pearson R, Pearson's r, pearson r |
| p-value | p < 0.05 (italic p) | P < 0.05, p-value < 0.05 |

### 2.2 Number Formatting

| Rule | Correct | Incorrect |
|------|---------|-----------|
| Numbers < 10 in text | "three models" | "3 models" |
| Numbers ≥ 10 in text | "87 questions" | "eighty-seven questions" |
| Starting a sentence | "Eighty-seven questions" | "87 questions were..." |
| Percentages | "68.5%" | "68.5 %" or "sixty-eight percent" |
| Decimals | "r = 0.15" | "r = .15" (include leading zero) |

### 2.3 Citation Formatting (IEEE Style)

| Rule | Correct | Incorrect |
|------|---------|-----------|
| Single citation | "...as shown by Tulu et al. [4]" | "...as shown by [4]" (for named reference) |
| Multiple citations | "[4], [8], [9]" | "[4, 8, 9]" (IEEE uses separate brackets) |
| Beginning of sentence | "Tulu et al. [4] demonstrated..." | "[4] demonstrated..." |
| Possessive | "Tulu et al.'s [4] results" | "Tulu et al. [4]'s results" |

---

## 3. Structural Checks

### 3.1 Cross-References

| # | Check | Status |
|---|-------|--------|
| 1 | All figures referenced in text ("as shown in Figure 2") | ☐ |
| 2 | All tables referenced in text | ☐ |
| 3 | No orphan figures/tables (not referenced) | ☐ |
| 4 | Figure/table numbers are sequential | ☐ |
| 5 | Section references are correct ("as described in Section 3.2") | ☐ |
| 6 | All RQs stated in Intro are answered in Results/Discussion | ☐ |
| 7 | All contributions listed in Intro are delivered in paper | ☐ |

### 3.2 Data Consistency

| # | Check | Status |
|---|-------|--------|
| 8 | Numbers in text match numbers in tables | ☐ |
| 9 | Numbers in abstract match numbers in Results | ☐ |
| 10 | Percentages in tables sum correctly | ☐ |
| 11 | Dataset statistics (87Q, 2273A) are consistent throughout | ☐ |
| 12 | Gold standard size (500 words) is consistent | ☐ |

---

## 4. Pre-Submission Final Pass

### 4.1 Formatting

| # | Check | Status |
|---|-------|--------|
| 1 | IEEE two-column format applied correctly | ☐ |
| 2 | Page count within limit (≤14 for TLT) | ☐ |
| 3 | Figures are 300 DPI minimum | ☐ |
| 4 | Figures are legible at print size | ☐ |
| 5 | Tables fit within column width | ☐ |
| 6 | References formatted per IEEE style | ☐ |
| 7 | Author information blinded (for double-blind review) | ☐ |

### 4.2 Language Quality

| # | Check | Status |
|---|-------|--------|
| 8 | Spellcheck completed (US English) | ☐ |
| 9 | Grammar check (Grammarly or similar) | ☐ |
| 10 | No contractions (don't → do not, can't → cannot) | ☐ |
| 11 | No colloquialisms or informal language | ☐ |
| 12 | Consistent spelling (analyze vs analyse — pick one) | ☐ |

### 4.3 Ethical and Legal

| # | Check | Status |
|---|-------|--------|
| 13 | Data availability statement included | ☐ |
| 14 | Ethical statement included | ☐ |
| 15 | All co-authors have reviewed and approved | ☐ |
| 16 | No undisclosed conflicts of interest | ☐ |
| 17 | No copyrighted material used without permission | ☐ |

---

## 5. Quick Hedging Guide

### When to hedge (use cautious language):
- Interpreting results: "This suggests that..." not "This proves that..."
- Generalizing: "Our findings indicate that LLM-WSD may improve..." not "LLM-WSD improves..."
- Causal claims: "The improvement appears to be driven by..." not "The improvement is caused by..."

### When NOT to hedge (be direct):
- Describing methodology: "We evaluate four LLMs" not "We attempt to evaluate..."
- Reporting data: "Accuracy increases from 55% to 68%" not "Accuracy seems to increase..."
- Stating facts: "The Mohler dataset contains 2,273 answers" not "The dataset reportedly contains..."

### Hedging vocabulary:

| Strength | Words |
|----------|-------|
| Strong | demonstrates, shows, reveals, confirms |
| Moderate | suggests, indicates, implies, supports |
| Weak | may, might, could, appears to |

**Rule of thumb:** Use "shows" for data, "suggests" for interpretation, "may" for speculation.

---

*Document version: 1.0 — March 2026*
