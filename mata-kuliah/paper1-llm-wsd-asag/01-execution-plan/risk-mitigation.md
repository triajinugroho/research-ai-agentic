# Risk Mitigation Plan — Paper 1: LLM-WSD for ASAG

## 1. Critical Dependencies

### Dependency Map

```
                    Paper Submission
                         │
              ┌──────────┼──────────┐
              │          │          │
          Full Paper   Figures    References
              │          │          │
         ┌────┴────┐     │     Verification
         │         │     │
     Results   Writing   │
         │               │
    ┌────┴────┐          │
    │         │          │
  Intrinsic Extrinsic   │
  Eval      Eval        │
    │         │          │
    │    ┌────┴────┐     │
    │    │         │     │
    │  Pipeline  Scores  │
    │    │               │
    ├────┴──┐            │
    │       │            │
  LLM    SemSpace ◄──── CRITICAL
  WSD    Vectors        DEPENDENCY
    │       │
    │       │
  Gold   Mohler
  Std    Dataset
    │
  Human
  Annotators
```

---

## 2. Risk Register (Detailed)

### Risk 1: SemSpace Vectors Unavailable

| Attribute | Detail |
|-----------|--------|
| **Probability** | Medium (40%) |
| **Impact** | High — blocks entire extrinsic evaluation |
| **Detection** | Email response from Tulu within 1-2 weeks |
| **Trigger** | No response after 2 weeks, or explicit refusal |

**Mitigation Plan:**

| Plan | Description | Effort | Quality vs Original |
|------|------------|--------|-------------------|
| **A (preferred)** | Get vectors from Tulu via email | 0 hours | 100% — identical |
| **B** | Re-implement SemSpace using their published paper (Expert Systems w/ Applications 2021) | 6-8 hours | 95% — may have minor numerical differences |
| **C** | Use LMMS sense embeddings (Loureiro & Jorge, 2019) as alternative | 3-4 hours | 80% — different embedding, document deviation |
| **D** | Use AutoExtend (Rothe & Schütze, 2015) | 4-5 hours | 80% — same caveat as Plan C |
| **E** | Use WordNet path-similarity as proxy for sense similarity | 2 hours | 60% — significant deviation, weaker paper |

**Action Now:** Send email to ctulu@atu.edu.tr today. Prepare Plan B code in parallel.

---

### Risk 2: Competitor Publishes First

| Attribute | Detail |
|-----------|--------|
| **Probability** | Low-Medium (20%) |
| **Impact** | High — reduces novelty claim |
| **Detection** | Google Scholar alerts for "LLM WSD ASAG", monthly arXiv check |
| **Trigger** | Paper found on arXiv or published venue |

**Mitigation Plan:**

| Scenario | Response |
|----------|----------|
| Competitor uses different LLMs | Cite them, emphasize our unique LLM selection and cascade analysis |
| Competitor uses different dataset | Cite them, emphasize Mohler as standard ASAG benchmark |
| Competitor does same thing | Pivot framing: "independent replication + deeper analysis" |
| Competitor's results conflict with ours | Excellent discussion material — both papers become more interesting |

**Action Now:** Set up Google Scholar alert. Aim for submission by May 2026.

---

### Risk 3: Low Inter-Annotator Agreement

| Attribute | Detail |
|-----------|--------|
| **Probability** | Low-Medium (25%) |
| **Impact** | Medium — weakens gold standard credibility |
| **Detection** | After annotation round completion |
| **Trigger** | Cohen's κ < 0.6 |

**Mitigation Plan:**

| κ Range | Interpretation | Action |
|---------|---------------|--------|
| > 0.8 | Almost perfect | Proceed — ideal scenario |
| 0.6-0.8 | Substantial | Proceed — acceptable for WSD |
| 0.4-0.6 | Moderate | Review guidelines, re-annotate disagreements, add 3rd annotator |
| < 0.4 | Poor | Redesign annotation scheme, train annotators, reduce sample |

**Prevention:**
- Clear annotation guidelines with examples
- Pilot round (50 words) before full annotation
- Training session for annotators on WordNet synset interpretation

---

### Risk 4: LLM API Issues (Rate Limits, Outages, Cost)

| Attribute | Detail |
|-----------|--------|
| **Probability** | Medium (35%) |
| **Impact** | Low-Medium — delays experiments |
| **Detection** | During experiment execution |
| **Trigger** | API errors, rate limiting, unexpected costs |

**Mitigation Plan:**

| LLM | Primary Access | Backup Access | Cost Estimate |
|-----|---------------|---------------|---------------|
| Qwen-2.5 | Ollama (local, free) | DashScope API | $0 local / ~$5 API |
| Mistral-7B | Ollama (local, free) | Mistral API | $0 local / ~$3 API |
| Llama-3.1-8B | Ollama (local, free) | Together API | $0 local / ~$5 API |
| Gemini-1.5-Flash | Google AI Studio (free tier) | Vertex AI (paid) | $0-15 |

**Total worst case:** ~$28 for all 8,000 WSD calls. Manageable.

**Prevention:**
- Use local models for 3/4 LLMs (only Gemini requires API)
- Implement exponential backoff retry logic
- Cache all API responses (avoid re-calling on parsing failures)
- Run experiments during off-peak hours for API stability

---

### Risk 5: Results Show No WSD Improvement

| Attribute | Detail |
|-----------|--------|
| **Probability** | Low (15%) |
| **Impact** | High — undermines paper premise |
| **Detection** | After intrinsic evaluation (Hour 11) |
| **Trigger** | No LLM significantly outperforms Lesk on WSD accuracy |

**Mitigation Plan:**

| Scenario | Reframing |
|----------|----------|
| LLMs slightly better but not significant | "LLM-WSD is comparable to Lesk with practical advantages (no WordNet gloss engineering)" |
| LLMs worse than Lesk | "Surprising negative result — LLMs struggle with fine-grained synset selection in short text" (still publishable as empirical finding) |
| Mixed results (some LLMs better, some worse) | "LLM capability varies significantly — model selection matters for downstream impact" |
| WSD improves but ASAG doesn't | "WSD quality is NOT the bottleneck in knowledge-based ASAG — other pipeline components dominate" (valuable diagnostic finding) |

**All scenarios are publishable** — the scientific community values well-executed negative results.

---

### Risk 6: MaLSTM Replication Gap

| Attribute | Detail |
|-----------|--------|
| **Probability** | Medium (30%) |
| **Impact** | Medium — may not match Tulu's exact numbers |
| **Detection** | Sprint 1, Hour 4 |
| **Trigger** | Baseline results deviate >10% from Tulu's published numbers |

**Mitigation Plan:**

1. **Acceptable deviation:** Document exact replication steps and any differences
2. **Our key contribution is RELATIVE comparison** (LLM vs Lesk within OUR pipeline run), not ABSOLUTE numbers matching Tulu
3. If significant deviation: add sentence in paper: "While our baseline differs slightly from Tulu et al. due to [reason], the relative comparison between WSD methods remains valid as all conditions use identical pipeline components."

---

### Risk 7: Reviewer Rejects as "Incremental"

| Attribute | Detail |
|-----------|--------|
| **Probability** | Medium (30%) |
| **Impact** | High — paper rejected |
| **Detection** | During review |
| **Trigger** | Reviewer comment: "merely replacing one component is incremental" |

**Pre-emptive Defense (build into paper):**

1. **Bridge contribution argument:** "This paper connects two previously disconnected fields, enabling a new research direction at their intersection"
2. **Diagnostic value:** "Understanding which pipeline component matters most is itself a significant contribution to system design"
3. **Resource contribution:** "The gold standard WSD annotations for Mohler are a new community resource"
4. **Practical impact:** "Concrete, deployable guidelines for improving existing ASAG systems"
5. **Foundation for future work:** "Opens path for deeper improvements (Paper 2, 3)"

---

## 3. Decision Points & Go/No-Go Gates

| Gate | Timing | Decision Criteria | Go | No-Go Action |
|------|--------|-------------------|-----|-------------|
| **G0** | Before Sprint 1 | Mohler dataset accessible? | Yes → Sprint 1 | Download from alternative source |
| **G1** | After Sprint 1 | Pipeline runs end-to-end? | Yes → Sprint 2 | Debug pipeline; consider simpler pipeline |
| **G2** | After Sprint 2 | Gold standard κ > 0.6? | Yes → Sprint 3 | Revise annotations; reduce sample size |
| **G3** | After Sprint 3 | At least 1 LLM > Lesk? | Yes → Sprint 4 | Pivot to negative result framing |
| **G4** | After Sprint 4 | Sufficient for paper? | Yes → Sprint 5 | Run additional experiments |
| **G5** | After Sprint 5 | Paper draft complete? | Yes → Sprint 6 | Additional writing time |

---

## 4. Communication Plan

| Stakeholder | Update Frequency | Channel | Content |
|-------------|-----------------|---------|---------|
| Bu Endang | After each Sprint | WhatsApp/Email | Sprint results + next steps |
| Promotor | After Sprint 3 + 5 | Email with attachment | Preliminary results, draft paper |
| Tri Aji | Real-time during execution | Claude Code session | Technical decisions, code review |
| Teguh | After Sprint 4 | Email | Analysis review, literature check |

---

*Document version: 1.0 — March 2026*
