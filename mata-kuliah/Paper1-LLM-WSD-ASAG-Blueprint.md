# Paper 1: LLM-Enhanced Synset Preparation for ASAG
## Full End-to-End Blueprint — Arahan Promotor Bu Endang

> **Judul Kerja:** "Comparative Evaluation of Large Language Models for Word Sense Disambiguation in Automatic Short Answer Grading"
> **Peneliti:** Endang Ripmiatin (lead), dengan bimbingan promotor
> **Supporting review:** Teguh Eko Budiarto & Tri Aji Nugroho (Rafiqspace.ai)
> **Tanggal:** Maret 2026
> **Estimasi penyelesaian:** ~16-23 jam efektif dengan AI-agentic workflow

---

# BAGIAN 1 — KONTEKS & JUSTIFIKASI

## 1.1 Apa Yang Diminta Promotor

```
"Paper 1 — di langkah 3 — seperti paper-nya Tulu,
tapi data pre-processing pakai LLM,
membandingkan performance 4 LLM dalam persiapan synset
(Qwen, Mistral, Llama, Gemini)"
```

### Terjemahan Teknis

**Paper acuan:** Tulu, Ozkaya & Orhan (2021) — "Automatic Short Answer Grading with SemSpace Sense Vectors and MaLSTM" (IEEE Access)

**Pipeline Tulu (7 langkah):**

```
Langkah 1: Input (reference answer + student answer)
Langkah 2: Tokenisasi & preprocessing teks
Langkah 3: Word Sense Disambiguation (WSD) → pilih synset WordNet  ← FOKUS PAPER 1
Langkah 4: SemSpace sense vector generation (dari synset terpilih)
Langkah 5: Input ke parallel LSTM (MaLSTM)
Langkah 6: Manhattan Similarity computation
Langkah 7: Score prediction → evaluasi (Pearson r, RMSE)
```

**Yang diubah Bu Endang:**
- Tulu di Langkah 3 pakai **Lesk algorithm** (tradisional, rule-based)
- Bu Endang ganti dengan **4 LLM** dan bandingkan mana yang paling akurat
- Sisanya (Langkah 4-7) tetap sama → isolasi variabel di WSD saja

### Kenapa Ini Smart

| Aspek | Penjelasan |
|-------|-----------|
| **Scope terkontrol** | Hanya 1 variabel yang diubah (WSD method), sisanya fixed |
| **Baseline jelas** | Tulu (2021) = baseline, hasilnya sudah dipublikasi |
| **Novelty jelas** | Belum ada paper yang benchmark LLM untuk WSD dalam konteks ASAG |
| **Eksperimen mudah** | API call ke 4 LLM, tidak perlu training model |
| **Publishable** | Format "comparative evaluation" sangat diterima di venue AI/Education |
| **Disertasi-friendly** | Jadi building block untuk paper-paper berikutnya |

---

## 1.2 Literature Landscape: LLM untuk WSD

### Status Terkini (per Maret 2025-2026)

**Paper kunci yang mendukung riset ini:**

1. **Sumanathilaka et al. (2025)** — "Exploring the Word Sense Disambiguation Capabilities of Large Language Models"
   - Benchmark LLM untuk WSD menggunakan XL-WSD dataset
   - Fine-tuned Llama-8B mencapai F1 0.8652 untuk English
   - LLM zero-shot perform baik tapi belum kalahkan SOTA supervised
   - **Gap:** Mereka TIDAK mengevaluasi dampak WSD quality ke downstream task (ASAG)

2. **Yae et al. (2025)** — "Leveraging Large Language Models for Word Sense Disambiguation" (Neural Computing and Applications)
   - 3 teknik evaluasi LLM untuk WSD: multiple choice, binary verification, unseen word
   - 7 generative LLM dievaluasi
   - **Gap:** Tidak ada koneksi ke educational application

3. **Sumanathilaka et al. (2025b)** — "An Exploration-Analysis-Disambiguation Reasoning Framework for WSD with Low-Parameter LLMs"
   - Model kecil (Gemma-2-2B, Qwen-2.5-3B, Llama-3.2-3B) dievaluasi
   - Reasoning framework terstruktur meningkatkan performa bahkan model kecil
   - Outperform GPT-3.5 Turbo meskipun parameter jauh lebih kecil
   - **Gap:** Tidak diaplikasikan ke ASAG pipeline

4. **Tulu et al. (2021)** — "Automatic Short Answer Grading with SemSpace Sense Vectors and MaLSTM" (IEEE Access)
   - Pipeline SemSpace + MaLSTM pada Mohler dataset
   - Per-question: Pearson >0.95, RMSE 0.04
   - Aggregate: Pearson 0.15 (performa turun drastis cross-question)
   - WSD menggunakan traditional Lesk algorithm
   - **Gap:** WSD-nya tradisional, tidak memanfaatkan LLM

### Research Gap yang Diisi Paper 1

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  LLM-WSD Research          ASAG Research                     │
│  (Sumanathilaka 2025,      (Tulu 2021,                       │
│   Yae 2025)                 Mohler 2011)                     │
│                                                              │
│  ✅ LLM bisa WSD           ✅ WSD penting untuk ASAG         │
│  ✅ Benchmark ada           ✅ SemSpace butuh WSD akurat      │
│  ❌ Tidak ditest di ASAG   ❌ WSD masih tradisional (Lesk)   │
│                                                              │
│              ┌────────────────────────┐                      │
│              │   PAPER 1 BU ENDANG    │                      │
│              │                        │                      │
│              │  LLM-WSD → SemSpace    │                      │
│              │  → MaLSTM → ASAG Score │                      │
│              │                        │                      │
│              │  "Bagaimana kualitas   │                      │
│              │   WSD oleh LLM        │                      │
│              │   mempengaruhi ASAG?"  │                      │
│              └────────────────────────┘                      │
│                                                              │
│  INI BELUM ADA DI LITERATURE MANAPUN.                       │
└──────────────────────────────────────────────────────────────┘
```

---

# BAGIAN 2 — PAPER DRAFT LENGKAP

---

## TITLE

**"Comparative Evaluation of Large Language Models for Word Sense Disambiguation in Automatic Short Answer Grading: Impact on SemSpace-MaLSTM Pipeline"**

*Alternatif pendek:*
"LLM-Enhanced Synset Preparation for Automatic Short Answer Grading"

---

## ABSTRACT (Draft ~200 kata)

Word Sense Disambiguation (WSD) is a critical preprocessing step in knowledge-based Automatic Short Answer Grading (ASAG) systems that rely on sense-level embeddings. Prior work by Tulu et al. (2021) demonstrated effective ASAG using SemSpace sense vectors with MaLSTM, but employed traditional WSD methods (Lesk algorithm) that are limited in contextual understanding. With recent advances showing that Large Language Models (LLMs) can perform WSD competitively, this study investigates whether replacing traditional WSD with LLM-based disambiguation improves downstream ASAG performance.

We evaluate four LLMs — Qwen-2.5, Mistral-7B, Llama-3, and Gemini-1.5-Flash — on their ability to select correct WordNet synsets for ambiguous words in student and reference answers from the Mohler ASAG dataset. We measure both intrinsic WSD accuracy (against human-annotated gold standard) and extrinsic impact on ASAG scoring (Pearson correlation and RMSE) through the complete SemSpace-MaLSTM pipeline.

Results show that [LLM-X] achieves the highest WSD accuracy at [X]%, improving downstream ASAG Pearson correlation from [baseline] to [improved], while [LLM-Y] shows unexpected degradation due to [reason]. Our findings demonstrate that LLM-based WSD is a viable and effective upgrade to knowledge-based ASAG pipelines, with implications for improving sense-level educational NLP systems.

**Keywords:** Word Sense Disambiguation, Large Language Models, Automatic Short Answer Grading, SemSpace, WordNet, Synset Selection

---

## 1. INTRODUCTION

### 1.1 Background

Automatic Short Answer Grading (ASAG) is the task of computationally evaluating free-text student responses against reference answers. Among various ASAG approaches, knowledge-based methods that leverage lexical-semantic resources like WordNet offer unique advantages: they can capture precise conceptual meanings and handle polysemy — the phenomenon where a single word has multiple meanings.

Tulu et al. (2021) demonstrated an effective knowledge-based ASAG approach using SemSpace sense vectors with Manhattan LSTM (MaLSTM). SemSpace generates distinct vector representations for each word sense (synset) in WordNet, enabling the system to distinguish between different meanings of the same word. The pipeline achieved strong results on the Mohler benchmark dataset, with per-question Pearson correlations exceeding 0.95.

However, the effectiveness of this pipeline critically depends on a preprocessing step that has received limited attention: **Word Sense Disambiguation (WSD)** — the process of selecting the correct synset for each word given its context. Tulu et al. employed the traditional Lesk algorithm for WSD, which determines word sense by measuring overlap between the word's context and WordNet glosses. While functional, this approach is limited in its ability to capture nuanced contextual meaning.

### 1.2 The WSD Bottleneck

In knowledge-based ASAG, WSD errors cascade through the entire pipeline:

```
Wrong synset selected
    → Wrong SemSpace sense vector
        → Wrong sentence representation
            → Wrong similarity score
                → Wrong grade
```

A single WSD error on a key concept word can dramatically affect the final ASAG score. For example, if "process" in a Computer Science context is disambiguated as the chemical/biological process rather than the computational process, the resulting sense vector will be fundamentally wrong.

Traditional WSD methods like Lesk are particularly vulnerable to:
- **Short contexts** — Student answers are often brief, providing limited disambiguation clues
- **Technical vocabulary** — Domain-specific terms may have specialized senses not well-represented in WordNet glosses
- **Informal language** — Students write in varied registers, often with misspellings or non-standard phrasing

### 1.3 LLMs as WSD Engines

Recent research has demonstrated that Large Language Models possess strong WSD capabilities. Sumanathilaka et al. (2025) showed that LLMs can perform WSD competitively in zero-shot settings, while Yae et al. (2025) evaluated seven generative LLMs across multiple WSD techniques. A particularly relevant finding by Sumanathilaka et al. (2025b) showed that even small-parameter LLMs (2-4B parameters) can achieve strong WSD performance when guided by structured reasoning frameworks.

These findings suggest a natural upgrade path: replacing the traditional Lesk algorithm in Tulu's pipeline with LLM-based WSD. However, no prior work has:
1. Evaluated LLM-based WSD specifically in an ASAG context
2. Measured the downstream impact of WSD quality on ASAG scoring
3. Compared multiple LLMs for this specific application

### 1.4 Research Questions

- **RQ1:** How accurately can different LLMs (Qwen, Mistral, Llama, Gemini) perform Word Sense Disambiguation on ASAG text compared to traditional Lesk algorithm?
- **RQ2:** How does the quality of LLM-based WSD affect downstream ASAG performance (Pearson correlation, RMSE) in the SemSpace-MaLSTM pipeline?
- **RQ3:** What types of WSD errors do different LLMs make, and how do these errors impact ASAG scoring?

### 1.5 Contributions

1. **First comparative evaluation** of multiple LLMs for WSD in an ASAG context
2. **End-to-end impact analysis** measuring how WSD quality propagates to final ASAG scores
3. **Practical guidelines** for selecting and prompting LLMs for synset preparation in educational NLP pipelines
4. **Gold standard WSD annotations** for a subset of the Mohler ASAG dataset (to be released)

---

## 2. RELATED WORK

### 2.1 ASAG with Sense Embeddings

The Mohler dataset (Mohler et al., 2011) contains 2,273 student answers to 87 questions from an introductory Computer Science course, graded on a 0-5 scale by two human raters. It remains the most widely-used benchmark for ASAG research.

Tulu et al. (2021) introduced SemSpace sense vectors into ASAG, achieving strong per-question results (Pearson r > 0.95) but weaker aggregate performance (Pearson r = 0.15). This discrepancy suggests that sense disambiguation varies in quality across different questions and vocabulary domains. Their pipeline consists of: (1) text preprocessing, (2) POS tagging, (3) WSD via Lesk algorithm, (4) SemSpace sense vector lookup, (5) MaLSTM encoding, (6) Manhattan similarity, (7) score prediction.

The SemSpace method itself (Orhan & Tulu, 2021) generates sense vectors by optimizing weights for semantic relations in WordNet, using an LVQ-inspired algorithm aligned with human similarity judgments on benchmark datasets (RG65, WS353, MEN3K).

### 2.2 Word Sense Disambiguation

WSD is one of the oldest tasks in NLP. Key approaches include:

**Knowledge-based methods:**
- Lesk algorithm (1986) and variants — gloss overlap
- Graph-based methods — PageRank on WordNet graph (UKB, Babelfy)
- Structural methods — path similarity, information content

**Supervised methods:**
- BERT-based fine-tuning on SemCor (Bevilacqua et al., 2021)
- Bi-encoder architectures mapping contexts to synset embeddings
- Current SOTA: GlossBERT variants achieving >80% F1 on standard benchmarks

**LLM-based methods (emerging):**
- Zero-shot: Direct prompting of LLMs to select word senses
- Few-shot: Providing sense examples in context
- Structured reasoning: Multi-step disambiguation frameworks

### 2.3 LLMs for WSD — Current State

Sumanathilaka et al. (2025) extended the XL-WSD benchmark for LLM evaluation, finding that fine-tuned Llama-8B achieves F1 of 0.8652 on English WSD, outperforming all other methods. However, zero-shot LLMs do not surpass supervised SOTA, suggesting prompt design matters significantly.

Yae et al. (2025) evaluated seven LLMs across three WSD techniques (multiple choice, binary verification, unseen word inference). Key finding: structured multiple-choice prompting (presenting synset options to the LLM) significantly outperforms open-ended sense generation.

Sumanathilaka et al. (2025b) demonstrated that small LLMs (2-4B parameters) with structured reasoning frameworks can outperform GPT-3.5 Turbo on WSD, challenging the assumption that model size is the primary determinant of WSD performance.

### 2.4 Gap Analysis

| Paper | WSD Method | LLM Comparison | ASAG Context | Downstream Impact |
|-------|-----------|---------------|-------------|------------------|
| Tulu et al. (2021) | Lesk | ❌ | ✅ | Not measured (WSD quality) |
| Sumanathilaka et al. (2025) | LLM (multiple) | ✅ | ❌ | Not measured (intrinsic only) |
| Yae et al. (2025) | LLM (7 models) | ✅ | ❌ | Not measured |
| Sumanathilaka et al. (2025b) | LLM (small) | ✅ | ❌ | Not measured |
| **This paper** | **LLM (4 models)** | **✅** | **✅** | **✅ Full pipeline** |

**Our unique contribution: connecting LLM-WSD quality to ASAG scoring through end-to-end pipeline evaluation.**

---

## 3. METHODOLOGY

### 3.1 Overview

We replicate the Tulu et al. (2021) SemSpace-MaLSTM pipeline, but replace the WSD component (Langkah 3) with four different LLMs, plus retain the original Lesk algorithm as baseline.

```
EXPERIMENTAL DESIGN

Independent Variable: WSD method
  → Lesk (baseline, same as Tulu)
  → Qwen-2.5 (7B/72B)
  → Mistral-7B (v0.3 / Nemo)
  → Llama-3.1 (8B/70B)
  → Gemini-1.5-Flash

Controlled Variables (held constant):
  → Dataset: Mohler (2011)
  → Sense embeddings: SemSpace (Orhan & Tulu, 2021)
  → Sequence model: MaLSTM
  → Similarity metric: Manhattan distance
  → Training/test split: same as Tulu

Dependent Variables (measured):
  → WSD accuracy (intrinsic)
  → Pearson correlation r (extrinsic, ASAG)
  → RMSE (extrinsic, ASAG)
  → Per-question performance variance
```

### 3.2 Dataset

**Mohler Extended Dataset (2011):**
- 87 questions from introductory Computer Science (Data Structures)
- 2,273 student answers
- Graded 0-5 by two human raters (average used as gold standard)
- Includes instructor reference answers per question

**WSD Gold Standard (new, constructed for this study):**
- Subset: 500 content words sampled from Mohler answers
- Stratified by: question topic, word frequency, number of WordNet senses
- Annotated by 2 human annotators with CS domain expertise
- Inter-annotator agreement measured via Cohen's Kappa
- Each word annotated with correct WordNet synset ID

**Sampling strategy for gold standard:**

```
Step 1: Extract all content words (nouns, verbs, adj) from Mohler dataset
Step 2: Filter to polysemous words (≥2 synsets in WordNet)
Step 3: Stratified sample:
  - 200 words with 2-3 senses (low ambiguity)
  - 200 words with 4-7 senses (medium ambiguity)
  - 100 words with 8+ senses (high ambiguity)
Step 4: Include sentence context for each word
Step 5: Two annotators independently select correct synset
Step 6: Resolve disagreements via discussion
```

### 3.3 LLM-based WSD: Prompt Design

This is the most critical component. Following best practices from Yae et al. (2025), we use a **multiple-choice synset selection** prompt format.

**Prompt Template:**

```
You are a Word Sense Disambiguation expert. Given a sentence from a 
Computer Science exam, select the correct WordNet synset for the 
target word.

SENTENCE: "{sentence}"
TARGET WORD: "{target_word}"

CANDIDATE SYNSETS:
{for each synset of target_word in WordNet:}
  {synset_number}. {synset_id} — {gloss}
     Example: {example_sentence_from_WordNet}

INSTRUCTIONS:
- Consider the Computer Science context of this sentence
- Select the synset that best matches the meaning of "{target_word}" 
  in this specific context
- Respond with ONLY the synset number (e.g., "1" or "3")

YOUR ANSWER:
```

**Example (filled in):**

```
SENTENCE: "A linked list stores each element in a separate node 
that contains the data and a pointer to the next node."

TARGET WORD: "node"

CANDIDATE SYNSETS:
1. node.n.01 — a connecting point at which several lines come together
2. node.n.02 — any thickened enlargement (anatomy)
3. node.n.03 — (physics) the point of minimum displacement in a 
   periodic system
4. node.n.04 — (computer science) any computer that is hooked up 
   to a computer network
5. node.n.05 — any bulge or swelling of an anatomical structure
6. node.n.06 — (astronomy) a point where an orbit crosses a plane

YOUR ANSWER: 4
```

**Prompt Variations (for robustness testing):**

| Variant | Description | Purpose |
|---------|------------|---------|
| **P1: Basic** | Synset ID + gloss only | Minimal information baseline |
| **P2: With examples** | Add WordNet example sentences | Test if examples help |
| **P3: Domain-primed** | Add "This is from a CS exam" context | Test domain awareness |
| **P4: Chain-of-thought** | Ask LLM to reason step-by-step before selecting | Test reasoning impact |

### 3.4 LLM Configurations

| Model | Provider | Size | Access Method | Temperature | Max Tokens |
|-------|----------|------|---------------|-------------|------------|
| **Qwen-2.5** | Alibaba | 7B / 72B | API or local (Ollama) | 0.0 | 10 |
| **Mistral** | Mistral AI | 7B-Instruct | API or local | 0.0 | 10 |
| **Llama-3.1** | Meta | 8B / 70B-Instruct | API or local | 0.0 | 10 |
| **Gemini-1.5-Flash** | Google | Unknown (proprietary) | API | 0.0 | 10 |

**Temperature = 0.0** untuk deterministic output (reproducibility).
**Max tokens = 10** karena output hanya angka synset.

**Catatan penting:** Untuk fair comparison, semua model mendapat prompt yang identik. Tidak ada fine-tuning — murni zero-shot evaluation.

### 3.5 Pipeline Replication

**Langkah 1-2: Preprocessing (identical to Tulu)**

```python
# Pseudocode
for each (question, ref_answer, student_answer, human_score) in Mohler:
    tokens_ref = tokenize(ref_answer)
    tokens_stu = tokenize(student_answer)
    pos_ref = pos_tag(tokens_ref)
    pos_stu = pos_tag(tokens_stu)
    content_words_ref = filter_content_words(tokens_ref, pos_ref)
    content_words_stu = filter_content_words(tokens_stu, pos_stu)
```

**Langkah 3: WSD (THE VARIABLE — 5 conditions)**

```python
# Condition 1: Lesk (baseline)
synsets_lesk = [lesk_disambiguate(word, context) for word in content_words]

# Condition 2-5: LLM-based
for llm in [Qwen, Mistral, Llama, Gemini]:
    synsets_llm = []
    for word in content_words:
        candidates = wordnet.synsets(word)
        if len(candidates) <= 1:
            synsets_llm.append(candidates[0] if candidates else None)
        else:
            prompt = build_wsd_prompt(word, context, candidates)
            response = llm.generate(prompt, temperature=0)
            selected_synset = parse_synset_number(response)
            synsets_llm.append(candidates[selected_synset])
```

**Langkah 4-7: SemSpace → MaLSTM → Score (identical to Tulu)**

```python
# Identical across all conditions
sense_vectors_ref = [semspace.get_vector(synset) for synset in synsets_ref]
sense_vectors_stu = [semspace.get_vector(synset) for synset in synsets_stu]

# MaLSTM encoding
repr_ref = malstm.encode(sense_vectors_ref)
repr_stu = malstm.encode(sense_vectors_stu)

# Manhattan similarity → score
predicted_score = manhattan_similarity(repr_ref, repr_stu) * 5.0
```

### 3.6 Evaluation Metrics

**Intrinsic (WSD quality):**

| Metric | Formula | What It Measures |
|--------|---------|-----------------|
| WSD Accuracy | correct / total | Overall disambiguation correctness |
| Accuracy@k | correct in top-k / total | Whether correct sense is in top-k predictions |
| Accuracy by ambiguity | grouped by #senses | Performance on easy vs hard words |
| Accuracy by POS | grouped by noun/verb/adj | Performance across word classes |
| Domain accuracy | CS-specific words only | Domain-specific disambiguation |

**Extrinsic (ASAG performance):**

| Metric | Formula | What It Measures |
|--------|---------|-----------------|
| Pearson r | correlation(predicted, human) | Linear correlation with human grades |
| RMSE | sqrt(mean(predicted - human)²) | Prediction error magnitude |
| Per-question Pearson r | correlation per question | Question-level stability |
| Δr from baseline | r_llm - r_lesk | Improvement over Lesk |

**Error Analysis:**

| Analysis | Description |
|----------|------------|
| Confusion matrix | Which synsets are confused with which |
| Error cascade | How WSD errors on specific words affect ASAG scores |
| Qualitative examples | 10 best + 10 worst disambiguation cases per LLM |

### 3.7 Statistical Tests

- **McNemar's test** — pairwise WSD accuracy comparison between models
- **Paired t-test** — Pearson r comparison across questions
- **Wilcoxon signed-rank** — non-parametric alternative if normality violated
- **Effect size** — Cohen's d for magnitude of improvement

---

## 4. EXPERIMENTAL SETUP

### 4.1 Computing Environment

```
Hardware:
  - GPU: NVIDIA T4 or A100 (for local LLM inference)
  - RAM: 32GB minimum
  - Storage: 50GB for model weights

Software:
  - Python 3.10+
  - PyTorch 2.0+
  - HuggingFace Transformers
  - NLTK (WordNet, Lesk)
  - vLLM or Ollama (local LLM serving)
  - Google Generative AI SDK (Gemini API)

Data:
  - Mohler dataset (publicly available)
  - WordNet 3.0 via NLTK
  - SemSpace pre-trained vectors (from Orhan/Tulu or re-generated)
```

### 4.2 Experiment Execution Plan

```
Experiment 1: Gold Standard Construction
  Input:  500 sampled polysemous words + sentence context
  Action: 2 human annotators select correct synset
  Output: gold_standard.csv (word, context, correct_synset, annotator_agreement)

Experiment 2: LLM WSD Evaluation (Intrinsic)
  Input:  500 words × 4 prompt variants × 5 WSD methods (Lesk + 4 LLM)
  Action: Run each WSD method, compare with gold standard
  Output: wsd_results.csv (word, method, prompt_variant, predicted_synset, correct, time_ms)

Experiment 3: ASAG Pipeline Evaluation (Extrinsic)
  Input:  Full Mohler dataset (2,273 answers × 5 WSD conditions)
  Action: Run complete Tulu pipeline with each WSD method
  Output: asag_results.csv (question_id, answer_id, wsd_method, predicted_score, human_score)

Experiment 4: Error Analysis
  Input:  Results from Exp 2 + Exp 3
  Action: Analyze error patterns, cascade effects, qualitative review
  Output: error_analysis_report (tables, examples, visualizations)
```

---

## 5. EXPECTED RESULTS & ANALYSIS FRAMEWORK

### 5.1 Hypothesized Results

**Intrinsic WSD Accuracy (on gold standard):**

| Method | Expected Accuracy | Reasoning |
|--------|------------------|-----------|
| Lesk (baseline) | ~55-65% | Known limitation on short technical text |
| Qwen-2.5-7B | ~70-78% | Strong multilingual model, good at structured tasks |
| Mistral-7B | ~68-75% | Good instruction-following, European-trained |
| Llama-3.1-8B | ~72-80% | Meta's latest, strong English performance |
| Gemini-1.5-Flash | ~75-82% | Google's model, likely trained on more diverse data |

**Extrinsic ASAG Performance (Pearson r, aggregate):**

| Method | Expected Pearson r | Expected RMSE | Notes |
|--------|-------------------|---------------|-------|
| Tulu original (Lesk) | ~0.15 (aggregate) | ~1.0 | Published result |
| With Qwen WSD | ~0.18-0.22 | ~0.92 | Modest improvement |
| With Mistral WSD | ~0.17-0.21 | ~0.94 | Similar range |
| With Llama WSD | ~0.19-0.24 | ~0.90 | Potentially best |
| With Gemini WSD | ~0.20-0.25 | ~0.89 | Potentially best |

**Note:** Tulu's aggregate Pearson was very low (0.15). Even a modest WSD improvement could yield meaningful gains here, because WSD errors were likely a major contributor to the poor aggregate performance.

### 5.2 Analysis Structure

**Analysis 1: Overall WSD Comparison**
- Bar chart: accuracy per LLM per prompt variant
- Statistical significance table (pairwise McNemar tests)
- Key finding: which LLM is best, by how much

**Analysis 2: Accuracy by Word Characteristics**
- Heatmap: accuracy × ambiguity level × LLM
- Key finding: do LLMs handle high-ambiguity words better than Lesk?

**Analysis 3: Domain-Specific Performance**
- CS-specific words vs general words
- Key finding: are LLMs better at technical disambiguation?

**Analysis 4: Impact on ASAG Scoring**
- Scatter plot: WSD accuracy vs Pearson r
- Per-question analysis: which questions improve most?
- Key finding: quantify the WSD→ASAG improvement relationship

**Analysis 5: Error Cascade Analysis**
- Track specific WSD errors to final score impact
- Case studies: "Student X's answer scored 2.1 with Lesk but 3.4 with Gemini because..."
- Key finding: which types of WSD errors matter most for grading?

**Analysis 6: Prompt Sensitivity**
- Compare P1 vs P2 vs P3 vs P4 for each LLM
- Key finding: does chain-of-thought help? Does domain priming help?

**Analysis 7: Cost-Benefit Analysis**
- Time per disambiguation: Lesk vs each LLM
- API cost per 1000 words (for commercial LLMs)
- Key finding: practical deployment considerations

---

## 6. DISCUSSION (Framework)

### 6.1 Key Findings to Discuss

1. **LLM superiority over Lesk** — Expected, but quantifying the gap is the contribution
2. **Which LLM wins and why** — Relate to model training data, architecture differences
3. **Prompt design matters** — Which prompt variant works best and implications
4. **Diminishing returns** — After what WSD accuracy level do ASAG scores plateau?
5. **Domain specificity** — CS terms require domain-aware disambiguation
6. **Aggregate vs per-question** — Does better WSD help more on aggregate evaluation?

### 6.2 Limitations

- Zero-shot only (no fine-tuning) — fine-tuned models would likely be even better
- English only (Mohler) — Indonesian ASAG is future work
- SemSpace vectors fixed — WSD improvement helps but doesn't fix fundamental SemSpace limitations
- LLM API costs — not all educators have access to commercial APIs
- Gold standard limited to 500 words — larger annotation would be more robust

### 6.3 Implications for Disertasi

This paper establishes that LLM-based WSD is a viable and beneficial upgrade to knowledge-based ASAG. This motivates:
- **Paper 2 (Langkah 7):** With better WSD in place, now improve the scoring layer
- **Future papers:** Full neuro-symbolic framework (NS-XASAG) combining all improvements

---

## 7. CONCLUSION (Draft)

This study presents the first comparative evaluation of Large Language Models for Word Sense Disambiguation in an ASAG context. By systematically replacing the traditional Lesk algorithm in Tulu et al.'s (2021) SemSpace-MaLSTM pipeline with four different LLMs, we demonstrate that LLM-based WSD achieves [X]% higher disambiguation accuracy and improves downstream ASAG scoring by [Y] points in Pearson correlation.

Among the four evaluated LLMs, [best model] achieves the highest performance, particularly excelling at disambiguating domain-specific Computer Science terminology. Our analysis reveals that WSD quality has a direct and measurable impact on ASAG scores, with [specific insight about error cascade].

These findings validate the integration of modern language understanding capabilities into knowledge-based educational NLP pipelines and provide practical guidelines for educators and developers seeking to improve automated grading systems.

---

## REFERENCES (To be completed)

1. Tulu, C.N., Ozkaya, O., & Orhan, U. (2021). Automatic Short Answer Grading with SemSpace Sense Vectors and MaLSTM. IEEE Access, 9, 19270-19280.
2. Orhan, U., & Tulu, C.N. (2021). A novel embedding approach to learn word vectors by weighting semantic relations: SemSpace. Expert Systems with Applications, 176, 114898.
3. Mohler, M., Bunescu, R., & Mihalcea, R. (2011). Learning to grade short answer questions using semantic similarity measures and dependency graph alignments. ACL 2011.
4. Sumanathilaka, et al. (2025). Exploring the Word Sense Disambiguation Capabilities of Large Language Models. arXiv:2503.08662.
5. Yae, J.H., et al. (2025). Leveraging large language models for word sense disambiguation. Neural Computing and Applications, 37(6), 4093-4110.
6. Sumanathilaka, et al. (2025b). An Exploration-Analysis-Disambiguation Reasoning Framework for WSD with Low-Parameter LLMs. arXiv:2603.05400.
7. Bevilacqua, M., et al. (2021). Recent Trends in Word Sense Disambiguation: A Survey. IJCAI-21.
8. Lesk, M. (1986). Automatic sense disambiguation using machine readable dictionaries. SIGDOC.
9. Mueller, J., & Thyagarajan, A. (2016). Siamese Recurrent Architectures for Learning Sentence Similarity. AAAI.
10. Miller, G.A. (1995). WordNet: A Lexical Database for English. Communications of the ACM.
11. [Additional references to be added]

---

# BAGIAN 3 — EXECUTION PLAN DENGAN AI-AGENTIC WORKFLOW

## 3.1 Sprint Plan (Detail Per Jam)

```
╔══════════════════════════════════════════════════════════════════════╗
║  SPRINT 1: SETUP & BASELINE REPLICATION                   [4 jam]  ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Jam 1: Environment setup                                            ║
║    Claude Code:                                                      ║
║    → pip install torch transformers nltk vllm                        ║
║    → Download Mohler dataset                                         ║
║    → Download WordNet 3.0 data via NLTK                              ║
║    → Verify SemSpace availability (check GitHub, contact authors)    ║
║                                                                      ║
║  Jam 2: Data loading & exploration                                   ║
║    Claude Code:                                                      ║
║    → Parse Mohler dataset into structured format                     ║
║    → Extract all content words + sentence contexts                   ║
║    → Compute statistics: #unique words, #polysemous, #senses dist   ║
║    → Output: mohler_words.csv (word, sentence, pos, #senses)        ║
║                                                                      ║
║  Jam 3: Lesk baseline implementation                                 ║
║    Claude Code:                                                      ║
║    → Implement NLTK Lesk WSD on all Mohler content words             ║
║    → Generate: lesk_synsets.csv                                      ║
║    → Compute coverage stats (how many words successfully WSD'd)      ║
║                                                                      ║
║  Jam 4: Tulu pipeline skeleton                                       ║
║    Claude Code:                                                      ║
║    → Implement SemSpace vector lookup (or mock if unavailable)       ║
║    → Implement MaLSTM forward pass                                   ║
║    → Implement Manhattan similarity + score prediction               ║
║    → Run baseline (Lesk WSD) through full pipeline                   ║
║    → Verify: does output match Tulu's published numbers?             ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║  SPRINT 2: GOLD STANDARD CONSTRUCTION                     [4 jam]   ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Jam 5: Sample selection                                             ║
║    Claude Code:                                                      ║
║    → Stratified sampling of 500 polysemous words                     ║
║    → Generate annotation spreadsheet with:                           ║
║      word | sentence | POS | candidate_synsets (with glosses)        ║
║    → Output: annotation_template.xlsx                                ║
║                                                                      ║
║  Jam 6-7: Human annotation (semi-automated)                         ║
║    HUMAN TASK (Bu Endang + 1 annotator):                             ║
║    → Annotate 500 words (can be AI-assisted — let Claude             ║
║      pre-suggest and human validates)                                ║
║    → Track disagreements                                             ║
║    AI-assisted acceleration:                                         ║
║    → Claude pre-fills "obvious" cases (1-2 senses, clear context)   ║
║    → Humans focus on ambiguous cases                                 ║
║    → Estimated: 200 auto-filled + 300 human-decided                  ║
║                                                                      ║
║  Jam 8: Agreement analysis                                           ║
║    Claude Code:                                                      ║
║    → Compute Cohen's Kappa inter-annotator agreement                 ║
║    → Resolve disagreements                                           ║
║    → Output: gold_standard.csv (final)                               ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║  SPRINT 3: LLM WSD EXPERIMENTS                            [4 jam]   ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Jam 9: Prompt engineering & testing                                 ║
║    Claude Code:                                                      ║
║    → Implement 4 prompt variants (P1-P4)                             ║
║    → Test each on 20 sample words (sanity check)                     ║
║    → Verify output parsing (LLM returns correct format)              ║
║    → Fix edge cases (LLM refuses, returns explanation instead        ║
║      of number, word not in WordNet, etc.)                           ║
║                                                                      ║
║  Jam 10: Run all LLM experiments                                     ║
║    Claude Code:                                                      ║
║    → For each LLM × each prompt variant × 500 gold standard words:  ║
║      → Generate prompt → Call API → Parse response → Log result      ║
║    → Total calls: 4 LLM × 4 prompts × 500 words = 8,000 API calls  ║
║    → Estimated time: ~30-60 min (parallel where possible)            ║
║    → Output: llm_wsd_results.csv                                     ║
║                                                                      ║
║  Jam 11: Intrinsic evaluation                                        ║
║    Claude Code:                                                      ║
║    → Compute accuracy per LLM per prompt variant                     ║
║    → Compute accuracy by ambiguity level, POS, domain                ║
║    → Statistical significance tests (McNemar pairwise)               ║
║    → Generate all tables and charts                                  ║
║    → Output: intrinsic_results/ folder with all figures              ║
║                                                                      ║
║  Jam 12: Full pipeline run with LLM WSD                              ║
║    Claude Code:                                                      ║
║    → For each LLM (best prompt variant):                             ║
║      → Run WSD on ALL Mohler content words (not just gold 500)       ║
║      → Feed through SemSpace → MaLSTM → Score pipeline               ║
║    → Total: 5 conditions × 2,273 answers = 11,365 pipeline runs     ║
║    → Output: asag_results.csv                                        ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║  SPRINT 4: ANALYSIS & ERROR INVESTIGATION                 [3 jam]   ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Jam 13: Extrinsic evaluation                                        ║
║    Claude Code:                                                      ║
║    → Compute Pearson r, RMSE per condition (aggregate + per-Q)       ║
║    → Statistical tests (paired t-test, Wilcoxon)                     ║
║    → Generate comparison tables                                      ║
║    → Scatter plot: WSD accuracy vs ASAG Pearson r                    ║
║                                                                      ║
║  Jam 14: Error cascade analysis                                      ║
║    Claude Code:                                                      ║
║    → Identify answers where WSD method changed the score by >1 pt   ║
║    → Trace: which word's WSD changed → which synset → which vector   ║
║    → Select 10 best + 10 worst case studies                          ║
║    → Generate narrative examples for paper                           ║
║                                                                      ║
║  Jam 15: Cost-benefit & practical analysis                           ║
║    Claude Code:                                                      ║
║    → Compute: time/word, cost/word for each method                   ║
║    → Generate deployment recommendation table                        ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║  SPRINT 5: PAPER WRITING                                  [5 jam]   ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Jam 16-17: Draft all sections                                       ║
║    Claude (chat):                                                    ║
║    → Fill in all [placeholders] with actual results                  ║
║    → Write Results section from generated tables                     ║
║    → Write Discussion connecting findings to RQs                     ║
║    → Finalize Abstract with actual numbers                           ║
║                                                                      ║
║  Jam 18: Figures & tables                                            ║
║    Claude Code:                                                      ║
║    → Generate publication-ready figures (matplotlib/seaborn)         ║
║    → Format tables per venue requirements                            ║
║    → Architecture diagram (pipeline with highlighted WSD step)       ║
║                                                                      ║
║  Jam 19: Literature review completion                                ║
║    Claude (chat):                                                    ║
║    → Verify all citations have correct DOI/links                     ║
║    → Check no missing references                                     ║
║    → Ensure Related Work properly positions our contribution         ║
║                                                                      ║
║  Jam 20: Final editing & formatting                                  ║
║    Claude Code:                                                      ║
║    → LaTeX formatting per target venue                               ║
║    → Spell check, grammar check                                     ║
║    → Generate PDF                                                    ║
║    → Human final review                                              ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

## 3.2 Time Summary

| Sprint | Tasks | AI-Agentic Hours | Human Hours (non-parallelizable) |
|--------|-------|-----------------|-------------------------------|
| Sprint 1: Setup & Baseline | Environment, data, Lesk, pipeline | 4 | 0.5 (review) |
| Sprint 2: Gold Standard | Sampling, annotation, agreement | 2 | 3 (annotation) |
| Sprint 3: LLM Experiments | Prompts, API calls, evaluation | 4 | 0.5 (review) |
| Sprint 4: Analysis | Stats, errors, case studies | 3 | 1 (interpretation) |
| Sprint 5: Paper Writing | Draft, figures, formatting | 5 | 2 (editing) |
| **TOTAL** | | **18 jam AI** | **7 jam Human** |
| | | **= ~25 jam total** | |

**Calendar estimate: 5-7 hari kerja intensif, atau 2-3 minggu part-time.**

## 3.3 Critical Dependencies & Risk Mitigation

| Dependency | Risk | Mitigation |
|-----------|------|-----------|
| **SemSpace vectors** | Pre-trained vectors mungkin tidak publik | 1) Contact Orhan/Tulu; 2) Re-implement using their paper's algorithm; 3) Use alternative sense embeddings (AutoExtend, LMMS) |
| **Mohler dataset** | Formatting issues | Publicly available; multiple papers have parsed it successfully |
| **LLM API access** | Rate limits, cost | Use local models via Ollama/vLLM for Qwen/Mistral/Llama; API only for Gemini |
| **LLM output parsing** | Models may not return clean synset numbers | Robust parsing with regex + retry logic; fallback to Lesk for unparseable responses |
| **Gold standard quality** | Low inter-annotator agreement | Focus on clear CS-domain words; provide annotator guidelines; resolve via 3rd annotator |
| **Tulu replication gap** | Can't exactly replicate published numbers | Document any deviations; our contribution is relative comparison, not absolute numbers |

## 3.4 Deliverables Checklist

```
□ Repository: GitHub with all code
  □ data/           — Mohler dataset (processed)
  □ gold_standard/  — 500-word WSD annotations
  □ prompts/        — All prompt templates (P1-P4)
  □ experiments/    — Experiment scripts
  □ results/        — All output CSVs
  □ analysis/       — Notebooks for analysis
  □ paper/          — LaTeX source + figures

□ Gold Standard Dataset
  □ annotation_guidelines.pdf
  □ gold_standard.csv (500 words, 2 annotators, resolved)
  □ inter_annotator_agreement.txt

□ Experiment Results
  □ lesk_baseline_wsd.csv
  □ qwen_wsd.csv
  □ mistral_wsd.csv
  □ llama_wsd.csv
  □ gemini_wsd.csv
  □ asag_scores_per_condition.csv

□ Paper
  □ manuscript.tex (or .docx)
  □ figures/ (all publication-ready)
  □ supplementary/ (full result tables)
```

---

# BAGIAN 4 — CODE TEMPLATES (Ready to Use)

## 4.1 Mohler Dataset Loader

```python
"""
mohler_loader.py — Load and parse Mohler ASAG dataset
Run with Claude Code: python mohler_loader.py
"""
import pandas as pd
import os

def load_mohler(data_dir):
    """Load Mohler dataset from directory structure."""
    records = []
    for q_file in sorted(os.listdir(data_dir)):
        if not q_file.endswith('.txt'):
            continue
        # Parse question files
        # Mohler format: question_id, student_answer, score1, score2, ref_answer
        # [Implementation depends on exact file format obtained]
        pass
    return pd.DataFrame(records, columns=[
        'question_id', 'student_answer', 'reference_answer',
        'score_1', 'score_2', 'avg_score'
    ])

def extract_content_words(text):
    """Extract polysemous content words with POS tags."""
    import nltk
    from nltk.corpus import wordnet as wn
    tokens = nltk.word_tokenize(text.lower())
    tagged = nltk.pos_tag(tokens)
    
    content_words = []
    for word, pos in tagged:
        wn_pos = penn_to_wn(pos)
        if wn_pos and len(wn.synsets(word, pos=wn_pos)) >= 2:
            content_words.append({
                'word': word,
                'pos': pos,
                'wn_pos': wn_pos,
                'num_senses': len(wn.synsets(word, pos=wn_pos)),
                'context': text
            })
    return content_words

def penn_to_wn(tag):
    """Convert Penn Treebank POS to WordNet POS."""
    if tag.startswith('N'): return 'n'
    if tag.startswith('V'): return 'v'
    if tag.startswith('J'): return 'a'
    if tag.startswith('R'): return 'r'
    return None
```

## 4.2 LLM WSD Engine

```python
"""
llm_wsd.py — LLM-based Word Sense Disambiguation
"""
from nltk.corpus import wordnet as wn
import json

PROMPT_TEMPLATES = {
    "P1_basic": """Select the correct WordNet synset for the word "{word}" in this sentence:
"{sentence}"

Candidate synsets:
{candidates}

Reply with ONLY the number.""",

    "P2_with_examples": """Select the correct WordNet synset for the word "{word}" in this sentence:
"{sentence}"

Candidate synsets:
{candidates_with_examples}

Reply with ONLY the number.""",

    "P3_domain_primed": """You are grading a Computer Science exam. Select the correct WordNet synset 
for the word "{word}" in this student's answer:
"{sentence}"

Candidate synsets:
{candidates}

Reply with ONLY the number.""",

    "P4_chain_of_thought": """Select the correct WordNet synset for "{word}" in:
"{sentence}"

Candidate synsets:
{candidates}

Think step-by-step:
1. What does "{word}" mean in this context?
2. Which synset matches that meaning?
3. Final answer (number only):"""
}

def build_candidates(word, wn_pos=None):
    """Build numbered candidate list from WordNet."""
    synsets = wn.synsets(word, pos=wn_pos)
    candidates = []
    for i, ss in enumerate(synsets):
        gloss = ss.definition()
        examples = '; '.join(ss.examples()[:2]) if ss.examples() else 'No example'
        candidates.append({
            'number': i + 1,
            'synset_id': ss.name(),
            'gloss': gloss,
            'examples': examples
        })
    return candidates

def format_candidates(candidates, include_examples=False):
    """Format candidates for prompt."""
    lines = []
    for c in candidates:
        line = f"{c['number']}. {c['synset_id']} — {c['gloss']}"
        if include_examples:
            line += f"\n   Example: {c['examples']}"
        lines.append(line)
    return '\n'.join(lines)

def call_llm(prompt, model_name, api_config):
    """Call LLM API and return response."""
    # Implementation varies per model
    # Qwen: via OpenAI-compatible API or local
    # Mistral: via Mistral API or local
    # Llama: via local (Ollama/vLLM)
    # Gemini: via Google Generative AI SDK
    pass

def parse_synset_response(response_text, num_candidates):
    """Extract synset number from LLM response."""
    import re
    # Try to find a number in the response
    numbers = re.findall(r'\b(\d+)\b', response_text.strip())
    if numbers:
        selected = int(numbers[-1])  # Take last number (often after reasoning)
        if 1 <= selected <= num_candidates:
            return selected - 1  # 0-indexed
    return None  # Parsing failed — fallback to Lesk
```

## 4.3 Evaluation Script

```python
"""
evaluate.py — Compute all metrics
"""
import numpy as np
from scipy.stats import pearsonr
from sklearn.metrics import cohen_kappa_score, confusion_matrix

def intrinsic_evaluation(predictions, gold_standard):
    """Evaluate WSD accuracy against gold standard."""
    correct = sum(p == g for p, g in zip(predictions, gold_standard))
    total = len(gold_standard)
    accuracy = correct / total
    
    # By ambiguity level
    results = {'overall': accuracy}
    for level in ['low', 'medium', 'high']:
        mask = [ambiguity_level(w) == level for w in words]
        if any(mask):
            level_correct = sum(p == g for p, g, m in zip(predictions, gold_standard, mask) if m)
            level_total = sum(mask)
            results[f'accuracy_{level}'] = level_correct / level_total
    
    return results

def extrinsic_evaluation(predicted_scores, human_scores):
    """Evaluate ASAG scoring performance."""
    r, p_value = pearsonr(predicted_scores, human_scores)
    rmse = np.sqrt(np.mean((np.array(predicted_scores) - np.array(human_scores))**2))
    return {'pearson_r': r, 'p_value': p_value, 'rmse': rmse}

def per_question_evaluation(results_df):
    """Compute metrics per question."""
    per_q = []
    for q_id in results_df['question_id'].unique():
        q_data = results_df[results_df['question_id'] == q_id]
        r, _ = pearsonr(q_data['predicted'], q_data['human'])
        per_q.append({'question_id': q_id, 'pearson_r': r, 'n_answers': len(q_data)})
    return pd.DataFrame(per_q)
```

---

# BAGIAN 5 — PUBLICATION & POSITIONING STRATEGY

## 5.1 Target Venues

| Venue | Type | Fit | Deadline (est.) | Notes |
|-------|------|-----|-----------------|-------|
| **EDM 2026** | Conference | ★★★★★ | Mar-Apr 2026 | Many ASAG papers here; WSD angle is fresh |
| **AIED 2026** | Conference (Springer) | ★★★★☆ | Feb-Mar 2026 | Strong AI+Education venue |
| **LAK 2027** | Conference (ACM) | ★★★★☆ | Oct 2026 | Ferreira Mello's GPT-4 ASAG paper was here |
| **IEEE Access** | Journal (OA) | ★★★★☆ | Rolling | Tulu's original paper was published here — natural follow-up |
| **SENDAMAS 2026 (UAI)** | National seminar | ★★★☆☆ | Oct 2026 | Quick publication, establish priority |

**Recommended strategy:**
1. Submit to **IEEE Access** — direct follow-up to Tulu et al. (2021), same venue
2. Present preliminary at **SENDAMAS 2026** for UAI credit
3. If IEEE Access rejected, pivot to **EDM 2027** or **AIED 2027**

## 5.2 Title Variations per Venue

| Venue | Suggested Title |
|-------|----------------|
| IEEE Access | "LLM-Enhanced Word Sense Disambiguation for Automatic Short Answer Grading: A Comparative Study on the SemSpace-MaLSTM Pipeline" |
| EDM/AIED | "Does Better Disambiguation Mean Better Grading? Evaluating LLMs for Synset Selection in Knowledge-Based ASAG" |
| SENDAMAS | "Evaluasi Komparatif Large Language Model untuk Word Sense Disambiguation pada Automatic Short Answer Grading" |

## 5.3 How This Connects to Disertasi Roadmap

```
DISERTASI BU ENDANG — Roadmap

Paper 0: Literature & Foundation
  → Rangkuman ChatGPT (sudah ada)
  → NS-XASAG concept paper (kita sudah buatkan)

Paper 1: LLM-Enhanced Synset Preparation ← INI YANG SEDANG KITA BUAT
  → Langkah 3 dari Tulu pipeline
  → Membandingkan 4 LLM untuk WSD
  → Kontribusi: proof bahwa LLM-WSD memperbaiki ASAG

Paper 2: [Langkah 7 — Scoring Layer] ← PAPER BERIKUTNYA
  → Arahan promotor selanjutnya
  → Kemungkinan: NLI-based scoring, LLM-as-judge, atau hybrid
  → Depends on Paper 1 results

Paper 3: Integration & Explainability
  → Gabungkan Paper 1 (better WSD) + Paper 2 (better scoring)
  → Add explainability layer
  → This becomes the NS-XASAG full framework

Disertasi: Compile all papers into coherent narrative
  → Chapter 1: Introduction + NS-XASAG framework overview
  → Chapter 2: Related Work (expanded)
  → Chapter 3: Paper 1 (WSD)
  → Chapter 4: Paper 2 (Scoring)
  → Chapter 5: Paper 3 (Integration)
  → Chapter 6: Conclusion + Future Work
```

---

# BAGIAN 6 — FAQ & TROUBLESHOOTING

## Q: Bagaimana kalau SemSpace pre-trained vectors tidak available?

**Option A (preferred):** Email Orhan/Tulu langsung — ctulu@atu.edu.tr. Researchers biasanya senang kalau ada yang melanjutkan risetnya.

**Option B:** Re-implement SemSpace. Paper mereka (Expert Systems with Applications, 2021) menjelaskan algoritmanya. Dengan Claude Code, re-implementation ~4-6 jam.

**Option C:** Gunakan alternatif sense embedding: AutoExtend (Rothe & Schütze, 2015) atau LMMS (Loureiro & Jorge, 2019). Dokumentasikan sebagai "adapted pipeline" dan acknowledge the deviation.

## Q: Bagaimana kalau aggregate Pearson tetap rendah meskipun WSD lebih baik?

Ini expected — Tulu sendiri mendapat r=0.15 aggregate. Paper kita bukan tentang mencapai SOTA, tapi tentang **mengukur seberapa banyak WSD improvement helps**. Bahkan peningkatan dari r=0.15 ke r=0.22 sudah bermakna jika statistically significant.

Frame contribution sebagai: "We demonstrate that WSD quality is a bottleneck in knowledge-based ASAG and that LLM-based WSD partially alleviates this bottleneck."

## Q: Bagaimana kalau salah satu LLM jauh lebih baik dari yang lain?

Ini justru good result — reviewer suka clear winners. Analisis kenapa: training data? Model size? Architecture? Ini jadi material Discussion yang kaya.

## Q: Apakah perlu Indonesian dataset juga?

Untuk Paper 1, **TIDAK.** Mohler dataset sudah cukup. Indonesian ASAG bisa jadi Paper 2 atau 3. Jangan overscope Paper 1.

## Q: Bagaimana handle out-of-vocabulary words (tidak ada di WordNet)?

Log mereka sebagai "OOV" dan exclude dari WSD evaluation. Report OOV rate sebagai limitation. Catatan: WordNet coverage untuk CS domain cukup baik (terms like "array", "stack", "queue", "pointer" semuanya ada).

## Q: Prompt design — perlu berapa variant?

4 variant (P1-P4) sudah cukup. Lebih dari itu akan membuat paper terlalu lebar. Focus utama adalah LLM comparison, prompt sensitivity adalah secondary analysis.

---

*Document version: 1.0 — March 2026*
*Status: Ready for Bu Endang & promotor review*
*Next step: Bu Endang confirms, then Sprint 1 begins*
