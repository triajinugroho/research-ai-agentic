# Journal Target Analysis — Paper 1: LLM-WSD for ASAG

## 1. Target Venue Selection

### 1.1 Q1 Journal Candidates

| # | Journal | IF (2024) | Quartile | Scope Fit | Review Time | OA Cost | Verdict |
|---|---------|-----------|----------|-----------|-------------|---------|---------|
| 1 | **IEEE Transactions on Learning Technologies** | 4.4 | Q1 (Education) | ★★★★★ | 3-6 months | ~$2,000 (hybrid) | **PRIMARY TARGET** |
| 2 | **Expert Systems with Applications** | 7.5 | Q1 (CS/AI) | ★★★★☆ | 2-4 months | $3,390 (OA) | **BACKUP #1** |
| 3 | **Computers & Education** | 12.0 | Q1 (Education) | ★★★☆☆ | 4-8 months | $3,470 (OA) | Too education-focused |
| 4 | **Knowledge-Based Systems** | 7.2 | Q1 (CS/AI) | ★★★★☆ | 2-5 months | $3,390 (OA) | Good fit for WSD angle |

### 1.2 Q2 Journal Candidates (Fallback)

| # | Journal | IF (2024) | Quartile | Scope Fit | Review Time | Verdict |
|---|---------|-----------|----------|-----------|-------------|---------|
| 5 | **IEEE Access** | 3.4 | Q2 | ★★★★★ | 1-2 months | Fast review, Tulu's venue |
| 6 | **Neural Computing and Applications** | 4.5 | Q2 (CS/AI) | ★★★★☆ | 3-5 months | Yae's WSD paper was here |
| 7 | **Education and Information Technologies** | 4.8 | Q2 (Education) | ★★★★☆ | 3-6 months | Good ed-tech fit |
| 8 | **Applied Intelligence** | 3.4 | Q2 (CS/AI) | ★★★☆☆ | 3-5 months | General AI applications |

---

## 2. Primary Target: IEEE Transactions on Learning Technologies (TLT)

### 2.1 Why TLT

1. **Scope match.** TLT publishes "innovative research on advanced learning technologies" — our paper bridges NLP (LLM-WSD) with learning technology (ASAG)
2. **Audience.** TLT readers are educational technologists who care about both the AI methodology and the educational impact
3. **Prestige.** Q1 journal in IEEE Computer Society — strong for Bu Endang's dissertation
4. **Precedent.** TLT has published ASAG papers before (Galhardi & Brancher, 2018; others)
5. **Complementary to Tulu.** Tulu published in IEEE Access; TLT is a step up in the same IEEE ecosystem

### 2.2 TLT Submission Requirements

| Requirement | Our Compliance |
|------------|---------------|
| Page limit | Regular paper: 14 pages (two-column IEEE format) |
| Abstract | ≤250 words |
| Keywords | 5-7 terms from IEEE taxonomy |
| Format | IEEE two-column, conference or transactions template |
| Supplementary | Allowed (code, data, additional tables) |
| Open data | Encouraged — we can share annotations + code |
| Review type | Double-blind |
| Ethical statement | Required — need to address data ethics |

### 2.3 TLT Framing Strategy

**Title for TLT:**
"Does Better Disambiguation Mean Better Grading? Evaluating Large Language Models for Word Sense Disambiguation in Knowledge-Based Automatic Short Answer Grading"

**Framing emphasis:**
- Lead with educational technology impact (not NLP methodology)
- Emphasize practical implications for ASAG system design
- Include discussion of deployment considerations (cost, latency, accessibility)
- Connect to broader automated assessment landscape

### 2.4 Section Length Planning (14 pages)

| Section | Target Pages | Content Focus |
|---------|-------------|---------------|
| Abstract | 0.25 | Results-focused, educational impact |
| Introduction | 1.5 | Educational context → WSD bottleneck → LLM opportunity |
| Related Work | 2.0 | ASAG landscape, WSD evolution, LLMs in education |
| Methodology | 3.0 | Pipeline, prompt design, gold standard, evaluation protocol |
| Experimental Setup | 1.0 | Data, models, computing environment |
| Results | 2.5 | Tables, figures, statistical tests |
| Discussion | 2.0 | Implications, limitations, practical guidelines |
| Conclusion | 0.75 | Summary, future work |
| References | 1.0 | 35-45 references |
| **Total** | **14.0** | |

---

## 3. Backup Target: Expert Systems with Applications (ESWA)

### 3.1 Why ESWA as Backup

1. **Higher IF** (7.5) — would be excellent for dissertation
2. **Scope.** "Expert and intelligent systems in all areas" — our LLM-as-WSD-expert fits naturally
3. **Faster review** (typically 2-4 months)
4. **SemSpace paper** (Orhan & Tulu, 2021) was published here — direct connection

### 3.2 ESWA Framing Strategy

**Title for ESWA:**
"LLM-Enhanced Word Sense Disambiguation for Automatic Short Answer Grading: A Comparative Evaluation on the SemSpace-MaLSTM Pipeline"

**Framing emphasis:**
- Lead with expert system design (LLM as WSD expert module)
- Emphasize system architecture and modular pipeline design
- More technical depth on WSD methodology and prompt engineering
- Detailed error analysis and system diagnostics

---

## 4. Conference Options (Preliminary + Journal)

### 4.1 Fast-Track Strategy

Publish preliminary results at a conference, then expand for journal:

| Conference | Deadline (est.) | Format | Purpose |
|-----------|----------------|--------|---------|
| **SENDAMAS 2026 (UAI)** | Oct 2026 | National seminar paper (6-8 pages) | Establish priority, UAI credit |
| **AIED 2026** | Feb-Mar 2026 | Short paper (6 pages) | International visibility |
| **EDM 2026** | Mar-Apr 2026 | Full paper (8 pages) | Strong ASAG community presence |

### 4.2 Dual Submission Policy

- **TLT:** No dual submission. Conference publication → significantly expanded journal version is OK
- **ESWA:** No dual submission. Same expansion policy
- **Strategy:** Submit short paper to SENDAMAS (national, no conflict), then full paper to TLT/ESWA

---

## 5. Keyword Strategy

### 5.1 Primary Keywords (for all venues)

1. Word Sense Disambiguation
2. Large Language Models
3. Automatic Short Answer Grading
4. SemSpace
5. WordNet

### 5.2 Additional Keywords (venue-specific)

| Venue | Additional Keywords |
|-------|-------------------|
| TLT | Automated Assessment, Learning Analytics, Educational NLP |
| ESWA | Expert System, Knowledge-Based System, Sense Embeddings |
| AIED | AI in Education, Assessment Technology |

### 5.3 SEO Considerations

For Google Scholar discoverability:
- Include "LLM" or "Large Language Model" in title (trending search term)
- Include "ASAG" or "Automatic Short Answer Grading" (niche but targeted)
- Include "WSD" or "Word Sense Disambiguation" (established NLP term)

---

## 6. Reviewer Profile Analysis

### 6.1 Expected Reviewer Types (TLT)

| Reviewer Type | Their Background | What They'll Focus On | How to Satisfy |
|--------------|-----------------|----------------------|---------------|
| **Educational technologist** | Assessment, learning analytics | Educational impact, practical value | Strong Discussion on implications |
| **NLP researcher** | WSD, text processing | Methodology rigor, baselines | Proper WSD evaluation protocol |
| **AI/ML generalist** | Deep learning, LLMs | Model selection, experimental design | Controlled variables, statistical tests |

### 6.2 Expected Reviewer Types (ESWA)

| Reviewer Type | Their Background | What They'll Focus On | How to Satisfy |
|--------------|-----------------|----------------------|---------------|
| **Expert systems designer** | Knowledge-based systems | System architecture, modularity | Clear pipeline diagram, component analysis |
| **NLP specialist** | Computational linguistics | WSD state-of-the-art, prompt design | Comparison with supervised SOTA |
| **Applied AI researcher** | Practical AI deployment | Scalability, cost, deployment | Cost-benefit analysis section |

---

## 7. Decision Matrix

| Criterion (weight) | TLT (Q1) | ESWA (Q1) | IEEE Access (Q2) | NCA (Q2) |
|-------------------|-----------|-----------|-------------------|----------|
| Prestige (25%) | 9 | 9 | 6 | 7 |
| Scope fit (25%) | 9 | 8 | 9 | 7 |
| Review speed (15%) | 6 | 8 | 9 | 7 |
| Acceptance chance (20%) | 7 | 7 | 8 | 8 |
| Cost (15%) | 7 | 5 | 6 | 6 |
| **Weighted Score** | **7.9** | **7.7** | **7.5** | **7.1** |

### Recommendation

1. **Submit to IEEE TLT** (Q1) — best combination of prestige + scope fit
2. **If rejected, pivot to ESWA** (Q1) — reframe toward expert systems
3. **If time-pressed, go to IEEE Access** (Q2) — fast review, Tulu's venue

---

*Document version: 1.0 — March 2026*
