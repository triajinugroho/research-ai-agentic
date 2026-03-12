# SWOT Analysis — Paper 1: LLM-WSD for ASAG

## 1. SWOT Matrix

```
┌─────────────────────────────────────┬─────────────────────────────────────┐
│          STRENGTHS (Internal)       │          WEAKNESSES (Internal)      │
│                                     │                                     │
│ S1. Clear, verifiable research gap  │ W1. Dependent on SemSpace vectors   │
│ S2. Controlled experimental design  │     (may not be publicly available) │
│ S3. Reproducible (open-source LLMs, │ W2. Gold standard requires human    │
│     public dataset)                 │     annotation (time + expertise)   │
│ S4. Strong baseline (Tulu 2021)     │ W3. Aggregate Pearson r low (~0.15) │
│ S5. Multiple LLMs = comprehensive   │     — improvement may seem modest   │
│ S6. Modular design = attributable   │ W4. Zero-shot only — no fine-tuning │
│     contribution                    │ W5. English only (Mohler dataset)   │
│ S7. Bridges two research fields     │ W6. Team expertise more in CS       │
│ S8. Dissertation building block     │     education than computational    │
│                                     │     linguistics                     │
├─────────────────────────────────────┼─────────────────────────────────────┤
│       OPPORTUNITIES (External)      │          THREATS (External)         │
│                                     │                                     │
│ O1. LLM-WSD proven viable (2025     │ T1. Someone publishes same idea     │
│     papers) — timing is right       │     before us (12-18 month window)  │
│ O2. Growing interest in modular AI  │ T2. End-to-end LLMs may make        │
│     for education (explainability)  │     pipeline ASAG irrelevant        │
│ O3. Multiple Q1/Q2 venues available │ T3. LLM model updates may change    │
│ O4. Can extend to Indonesian ASAG   │     results between writing and     │
│     (future papers)                 │     review                          │
│ O5. Gold standard annotations =     │ T4. Reviewer skepticism toward      │
│     citable resource                │     "yet another LLM benchmark"     │
│ O6. AI-agentic workflow enables     │ T5. API cost/access changes         │
│     fast execution                  │                                     │
│                                     │                                     │
└─────────────────────────────────────┴─────────────────────────────────────┘
```

---

## 2. Strategic Actions

### 2.1 Leverage Strengths → Capture Opportunities (SO Strategies)

| Strategy | Action | Priority |
|----------|--------|----------|
| **SO1: Speed to publish** | S6 (modular) + O1 (timing) → Execute fast with AI-agentic workflow, submit within 2 months | Critical |
| **SO2: Bridge paper positioning** | S7 (bridges fields) + O2 (interest in modular AI) → Position as "bridging WSD and ASAG" in abstract | High |
| **SO3: Resource contribution** | S3 (reproducible) + O5 (citable dataset) → Release gold standard annotations publicly on GitHub | High |
| **SO4: Multi-venue strategy** | S5 (comprehensive) + O3 (multiple venues) → Prepare venue-adaptive framing | Medium |

### 2.2 Address Weaknesses Using Opportunities (WO Strategies)

| Strategy | Action | Priority |
|----------|--------|----------|
| **WO1: SemSpace contingency** | W1 + O6 (AI workflow) → Prepare AutoExtend/LMMS as Plan B, implementable in hours | Critical |
| **WO2: Modest improvement framing** | W3 (low Pearson) + O2 (modular AI interest) → Frame as diagnostic/analytical study, not SOTA | High |
| **WO3: AI-assisted annotation** | W2 (annotation cost) + O6 (AI workflow) → Use Claude to pre-annotate, humans validate | High |
| **WO4: Indonesian extension hook** | W5 (English only) + O4 (Indonesian future) → Mention Indonesian ASAG as explicit future work | Medium |

### 2.3 Use Strengths to Mitigate Threats (ST Strategies)

| Strategy | Action | Priority |
|----------|--------|----------|
| **ST1: First-mover speed** | S8 (dissertation block) + T1 (competitor) → Submit paper within 8 weeks | Critical |
| **ST2: Modular vs end-to-end** | S6 (modular) + T2 (end-to-end trend) → Argue interpretability value in Discussion | High |
| **ST3: Fixed model versions** | S3 (reproducible) + T3 (model updates) → Lock model versions, document exact checkpoints | Medium |
| **ST4: Beyond benchmark** | S2 (experimental rigor) + T4 (benchmark fatigue) → Emphasize cascade analysis as unique contribution | High |

### 2.4 Minimize Weaknesses and Threats (WT Strategies)

| Strategy | Action | Priority |
|----------|--------|----------|
| **WT1: Acknowledge limitations transparently** | W3+W4+W5 + T4 → Explicit limitations section; position as foundation for future work | High |
| **WT2: CL expertise gap** | W6 + T4 → Consult with CL colleague for terminology accuracy; cite WSD survey papers | Medium |
| **WT3: Hedging claims** | W3 + T2 → Don't overclaim "LLM-WSD solves ASAG"; claim "improves WSD step" | High |

---

## 3. Risk Register

| # | Risk | Probability | Impact | Mitigation | Owner | Status |
|---|------|-------------|--------|------------|-------|--------|
| R1 | SemSpace vectors unavailable | Medium | High | Email Tulu; prepare Plan B (AutoExtend) | Endang | Open |
| R2 | Competitor publishes first | Low-Medium | High | Fast execution; add unique cascade analysis | Team | Open |
| R3 | Low inter-annotator agreement | Low | Medium | Clear annotation guidelines; 3rd annotator tiebreak | Endang | Open |
| R4 | LLM API rate limits/outages | Medium | Low | Use local models (Ollama) for 3/4 LLMs | Tri Aji | Open |
| R5 | Results show no improvement | Low | High | Negative result still publishable; reframe as "WSD is not the bottleneck" | Endang | Open |
| R6 | Reviewer rejects as incremental | Medium | High | Emphasize bridge contribution + cascade analysis + gold standard | Endang | Open |
| R7 | MaLSTM replication fails | Low-Medium | Medium | Document deviations; focus on relative comparison | Tri Aji | Open |

---

## 4. Success Criteria

### 4.1 Minimum Viable Paper (MVP)

Paper is publishable if ALL of the following are met:

- [ ] At least 1 LLM significantly outperforms Lesk on WSD accuracy (p < 0.05)
- [ ] Downstream ASAG metric (Pearson r or RMSE) changes measurably between WSD conditions
- [ ] Gold standard has acceptable inter-annotator agreement (Cohen's κ > 0.6)
- [ ] Results are reproducible with documented code and data

### 4.2 Strong Paper (Target)

In addition to MVP:

- [ ] Clear winner among LLMs with explainable reasons
- [ ] Cascade analysis shows traceable WSD→ASAG error propagation
- [ ] Prompt variant analysis reveals actionable design principles
- [ ] Per-question analysis explains when WSD matters most

### 4.3 Exceptional Paper (Stretch)

In addition to Strong:

- [ ] Novel error taxonomy for WSD failures in educational text
- [ ] Practical deployment guide with cost/benefit analysis
- [ ] Gold standard released with paper as community resource
- [ ] Invited revision from Q1 journal on first submission

---

## 5. Timeline Pressure Analysis

```
March 2026                                     September 2026
    │                                                │
    ├── NOW: Blueprint ready                         │
    │                                                │
    ├── Week 1-2: Sprint 1-2 (setup + gold std)     │
    │                                                │
    ├── Week 3-4: Sprint 3-4 (experiments)          │
    │                                                │
    ├── Week 5-6: Sprint 5 (writing)                │
    │                                                │
    ├── Week 7-8: Internal review + revision        │
    │                                                │
    ├── May 2026: SUBMIT TO TLT ──────────►         │
    │                                    Review      │
    │                                    period      │
    │                                    (3-6 mo)    │
    │                                                │
    │                          ┌─ Accept ──► Publish  │
    │                          │                      │
    │                          ├─ Revise ──► R&R      │
    │                          │             (2-3 mo) │
    │                          │                      │
    │                          └─ Reject ──► ESWA     │
    │                                       submit    │
    │                                                │
    └────────────────────────────────────────────────┘

    Target: Paper accepted by Q4 2026 / Q1 2027
    Dissertation defense: 2027
```

---

*Document version: 1.0 — March 2026*
