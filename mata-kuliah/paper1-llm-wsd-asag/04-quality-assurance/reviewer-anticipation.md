# Reviewer Anticipation Guide

## Purpose

Anticipate likely reviewer concerns and prepare defensible responses. Each concern is analyzed from the perspective of three typical reviewer profiles for our target venues.

---

## Reviewer Profile A: Educational Technologist

> Background: Assessment technology, learning analytics, instructional design.
> Cares about: practical impact, student outcomes, deployability.

### Likely Concerns

**A1: "What's the educational impact? You improved WSD, so what?"**

*Anticipated wording:* "The paper demonstrates a technical improvement, but the educational implications are unclear. How does better WSD translate to better feedback for students or instructors?"

*Defense:*
- Acknowledge this is a pipeline study, not a deployment study
- Emphasize Section 6.2 (practical guidelines): "Better WSD → more accurate automatic scoring → less human re-grading effort"
- Quantify: if WSD improvement reduces RMSE by X, this means Y fewer students receive scores >1 point from human grade
- Future work: connecting improved scoring to actionable feedback

*Where to strengthen paper:* Add 2-3 sentences in Discussion about instructor workload implications.

---

**A2: "Why not use LLMs for end-to-end grading instead of this complex pipeline?"**

*Anticipated wording:* "Given that recent work shows LLMs can directly grade short answers, what is the practical value of improving one component of a complex pipeline?"

*Defense:*
- Section 6.3 explicitly addresses this (pipeline vs end-to-end trade-offs)
- Interpretability argument: pipeline reveals *why* a grade was assigned
- Cost argument: local 7B models are free; GPT-4 end-to-end costs $0.01-0.03 per answer
- Diagnostic value: our findings inform both pipeline and end-to-end approaches
- Not competing: complementary research directions

*Where to strengthen paper:* Ensure Section 6.3 is compelling. Add cost comparison table.

---

**A3: "Only English, only CS. Can this generalize?"**

*Anticipated wording:* "The study is limited to one dataset in one language in one domain. How confident can we be that results generalize?"

*Defense:*
- Honest acknowledgment in Limitations (Section 6.4)
- Mohler is the standard ASAG benchmark used by Tulu et al. — direct comparison requires same data
- CS domain provides good test case (mix of domain-specific and general vocabulary)
- Future work explicitly targets Indonesian ASAG (Paper 2)
- Controlled experiment design is generalizable even if specific numbers aren't

---

## Reviewer Profile B: NLP / Computational Linguistics Researcher

> Background: WSD, semantic processing, language models.
> Cares about: methodological rigor, proper baselines, fair comparison.

### Likely Concerns

**B1: "Why not compare against supervised WSD SOTA (GlossBERT, BEM, EWISER)?"**

*Anticipated wording:* "The paper only compares LLMs against Lesk, which is a weak baseline from 1986. A fair evaluation should include modern supervised WSD systems."

*Defense:*
- Our goal is not WSD SOTA — it's measuring downstream ASAG impact
- Lesk is the exact baseline used by Tulu et al. (2021) — our direct comparison point
- Supervised methods require training data; our study evaluates zero-shot capability for practical deployment
- We acknowledge supervised methods in Related Work (Section 2.2) and position our work correctly
- Adding supervised WSD would confound the experimental design (supervised methods may introduce different biases)

*Where to strengthen paper:* Add explicit sentence: "We deliberately compare against Lesk rather than supervised methods because (a) it is the original baseline in the pipeline we evaluate, and (b) our focus is on zero-shot deployment scenarios."

---

**B2: "500-word gold standard is small. How reliable are your accuracy estimates?"**

*Anticipated wording:* "A gold standard of 500 words may be insufficient for reliable accuracy estimation, especially for the high-ambiguity stratum (only 100 words)."

*Defense:*
- 500 words is comparable to gold standard sizes in WSD papers (SemEval tasks use similar scales)
- Report confidence intervals (Wilson score) for all accuracy figures
- Stratified sampling ensures all ambiguity levels are represented
- Power analysis: with n=500, we can detect accuracy differences of ~5% at α=0.05, power=0.80
- For high-ambiguity stratum (n=100): can detect ~10% differences

*Where to strengthen paper:* Include power analysis in Methodology. Report CIs prominently.

---

**B3: "Quantized models (Q4_K_M) may not represent true model capability."**

*Anticipated wording:* "Running 7B models in 4-bit quantization degrades performance. Results may not reflect the true WSD capability of these models."

*Defense:*
- Q4_K_M is widely used in practice and research (cite Dettmers et al., 2023 if needed)
- Our goal is practical evaluation — quantized models are what practitioners would actually deploy
- If full-precision models perform better, our results are conservative lower bounds
- Gemini (API, full precision) serves as reference point
- Acknowledged in Limitations (Section 6.4)

---

**B4: "Temperature=0 doesn't guarantee determinism. How reproducible are results?"**

*Anticipated wording:* "LLM outputs at temperature=0 may not be perfectly deterministic, especially across different hardware or API versions."

*Defense:*
- Run each experiment 3x to check consistency
- If results are identical across runs: report single run (with note about consistency)
- If results vary: report mean ± std across runs
- All prompts, model versions, and configurations are documented for exact replication
- Cache all raw LLM responses for verification

*Where to strengthen paper:* Add reproducibility note in Section 4.

---

## Reviewer Profile C: AI/ML Generalist

> Background: Deep learning, model evaluation, experimental design.
> Cares about: proper experimental methodology, statistical tests, novelty.

### Likely Concerns

**C1: "This is incremental — just replacing one component in an existing pipeline."**

*Anticipated wording:* "The contribution is limited to substituting one module (WSD) in an existing system. This feels incremental rather than novel."

*Defense:* (Most critical concern — prepare carefully)
- **Bridge contribution:** "This is the first paper to connect two previously disconnected research areas (LLM-WSD and ASAG). Bridge papers are valued because they open new research directions."
- **Diagnostic contribution:** "Understanding which pipeline component matters most is itself significant — it guides where to invest improvement effort."
- **Resource contribution:** "The gold standard annotations are a new community resource."
- **Methodological contribution:** "The controlled-substitution approach is applicable to any modular NLP system."
- Cite examples of highly-cited bridge papers in NLP that connected existing techniques to new domains.

*Where to strengthen paper:* Frame contribution clearly in Introduction. Avoid underselling.

---

**C2: "Aggregate Pearson r of 0.15 means the pipeline barely works. Why improve it?"**

*Anticipated wording:* "The baseline aggregate Pearson r of 0.15 is essentially no correlation. Improving WSD in a fundamentally broken system seems pointless."

*Defense:*
- Per-question Pearson >0.95 for some questions — the pipeline works well locally
- Aggregate r is misleading because it mixes heterogeneous question types
- Our study is diagnostic: "Is WSD the bottleneck?"
  - If yes: fix WSD → fix pipeline
  - If no: WSD is not the problem → look elsewhere
- Both answers are scientifically valuable
- Frame as "component diagnosis" not "system improvement"

*Where to strengthen paper:* Lead with per-question results; discuss aggregate separately with appropriate caveats.

---

**C3: "Only 4 LLMs. Why these specific models? Where's GPT-4/Claude?"**

*Anticipated wording:* "The model selection feels arbitrary. Why not include the strongest available models (GPT-4, Claude) as an upper bound?"

*Defense:*
- Selection criteria are explicit: (1) reproducibility (open-source preferred), (2) comparable size (7-8B), (3) diverse architectures, (4) one commercial reference (Gemini)
- GPT-4/Claude excluded for reproducibility: API access is paid, models may change
- Cost constraint: evaluating proprietary models at scale has meaningful costs
- Our framework is extensible — others can add models
- Gemini serves as the "commercial-grade" reference point

*Where to strengthen paper:* Add explicit "Model Selection Rationale" subsection in Section 4.

---

**C4: "What if the MaLSTM component is too weak to reveal WSD differences?"**

*Anticipated wording:* "The MaLSTM model may not be sensitive enough to capture subtle differences in sense vectors caused by WSD changes."

*Defense:*
- Valid concern — acknowledged in Limitations
- We measure both intrinsic WSD (independent of MaLSTM) and extrinsic ASAG
- If MaLSTM is insensitive, intrinsic results still stand
- Future work could use more sensitive similarity models
- Per-question analysis helps: questions where MaLSTM works well (r > 0.8) provide clean signal

---

## Response Templates

### For "incremental work" criticism:
> "We appreciate the reviewer's attention to novelty. While our study substitutes a single component, the contribution is threefold: (1) it bridges two disconnected research areas, (2) it provides diagnostic insights into which pipeline component matters most, and (3) it introduces a new gold standard resource. The controlled-substitution approach is deliberately focused to enable clear attribution — a design choice that prioritizes scientific clarity over system-level novelty."

### For "limited dataset" criticism:
> "We agree that evaluation on additional datasets would strengthen generalizability claims, and we have acknowledged this in Section 6.4. We selected the Mohler dataset specifically because it is the same benchmark used by Tulu et al. (2021), enabling direct comparison of our WSD improvement. Cross-domain and cross-lingual evaluation is a planned next step (Section 6.5)."

### For "why not end-to-end LLM" criticism:
> "End-to-end LLM grading and modular pipeline analysis serve different purposes. End-to-end approaches optimize for accuracy; modular approaches optimize for understanding. Our error cascade analysis (Section 5.3) demonstrates that modular evaluation reveals actionable design insights that end-to-end evaluation cannot provide. We view these approaches as complementary, as discussed in Section 6.3."

---

## Pre-Submission Stress Test

Before submitting, read the paper through each reviewer perspective and verify:

- [ ] Reviewer A (ed-tech): Is practical impact clearly articulated?
- [ ] Reviewer B (NLP): Are baselines appropriate and acknowledged?
- [ ] Reviewer B (NLP): Is gold standard methodology sound?
- [ ] Reviewer C (ML): Is novelty clearly framed beyond "component swap"?
- [ ] Reviewer C (ML): Are statistical tests appropriate?
- [ ] All: Are limitations honest and complete?
- [ ] All: Does the abstract promise only what the paper delivers?

---

*Document version: 1.0 — March 2026*
