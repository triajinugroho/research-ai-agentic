# Section 4: Experimental Setup

> **Target length:** 1.0 page (IEEE two-column) | ~800 words
> **TDW tests:** Subset of MTD tests + reproducibility

---

## 4. Experimental Setup

### 4.1 Dataset

We use the Mohler et al. [1] dataset, a widely used ASAG benchmark consisting of student answers to undergraduate computer science examination questions at the University of North Texas. Table 2 summarizes its characteristics.

**Table 2: Mohler Dataset Statistics**

| Property | Value |
|----------|-------|
| Questions | 87 |
| Student answers | 2,273 |
| Grading scale | 0-5 (continuous) |
| Human graders | 2 (scores averaged) |
| Domain | Computer science (data structures, algorithms, OS) |
| Answer length | [TBD] words (mean ± std) |
| Unique content words | [TBD] |
| Polysemous words (≥ 2 synsets) | [TBD] ([TBD]% of content words) |

We chose this dataset for three reasons: (1) it is the same dataset used by Tulu et al. [4], enabling direct comparison, (2) it is publicly available for reproducibility, and (3) its computer science domain provides a natural mix of domain-specific and general vocabulary that challenges WSD systems.

### 4.2 LLM Models

Table 3 details the four LLMs selected for evaluation.

**Table 3: LLM Specifications**

| Model | Parameters | Access | Version/Checkpoint | Quantization |
|-------|-----------|--------|-------------------|-------------|
| Qwen-2.5 | 7B | Ollama (local) | qwen2.5:7b | Q4_K_M |
| Mistral-7B-Instruct | 7B | Ollama (local) | mistral:7b-instruct | Q4_K_M |
| Llama-3.1-8B-Instruct | 8B | Ollama (local) | llama3.1:8b | Q4_K_M |
| Gemini-1.5-Flash | Undisclosed | Google AI Studio API | gemini-1.5-flash-latest | N/A (API) |

**Model selection rationale.** We selected three open-source models of comparable size (7-8B parameters) to control for the effect of model architecture and training data while keeping computational requirements manageable. Gemini-1.5-Flash represents a closed-source, potentially larger model accessible only through API, serving as a reference point for what commercial-grade models can achieve. All open-source models are run locally via Ollama to ensure reproducibility without API dependency.

We deliberately excluded very large models (70B+) and proprietary models requiring paid API access (GPT-4, Claude) to maintain accessibility — researchers should be able to replicate our experiments on commodity hardware. We note this as a scope limitation and suggest large-model evaluation as future work.

### 4.3 Baseline: Lesk Algorithm

Our baseline is the NLTK implementation of the simplified Lesk algorithm (`nltk.wsd.lesk`), which is the same WSD method used by Tulu et al. [4]. For words where Lesk returns no result, we fall back to the most frequent sense (first synset in WordNet), consistent with standard WSD practice.

### 4.4 SemSpace Sense Vectors

We use the SemSpace sense vectors developed by Orhan and Tulu [5], which provide 300-dimensional embeddings for WordNet synsets. These vectors are constructed by extending Word2Vec embeddings to the synset level using the AutoExtend framework [28].

[If vectors obtained from authors:] *The vectors were obtained directly from the original authors.*

[If re-implemented:] *As the original vectors were not publicly available, we re-implemented the SemSpace construction process following the methodology described in [5], using the same Word2Vec base embeddings (Google News, 300-dim) and AutoExtend framework. We verified our reconstruction by comparing a random sample of synset vectors against the original paper's similarity rankings.*

For synsets not covered by SemSpace (approximately [TBD]% of all WSD outputs), we assign a zero vector, following the handling described by Tulu et al. [4].

### 4.5 MaLSTM Configuration

The Manhattan LSTM [6] is configured with:
- Hidden dimension: 50 (following Tulu et al.)
- Input dimension: 300 (SemSpace vector size)
- Training: [TBD — either pre-trained weights from Tulu or retrained on Mohler train split]
- Similarity: Manhattan distance, scaled to [0, 5] range

### 4.6 Computing Environment

| Component | Specification |
|-----------|--------------|
| Hardware | [TBD — e.g., NVIDIA RTX 3090, 24GB VRAM] |
| OS | Ubuntu 22.04 LTS |
| Python | 3.10+ |
| Key libraries | PyTorch 2.x, Transformers 4.x, NLTK 3.8, Ollama 0.x |
| LLM inference | Ollama (local), Google AI Studio SDK (Gemini) |
| Random seed | 42 (for all stochastic operations) |

### 4.7 Reproducibility

All code, prompts, gold standard annotations, and experiment configurations are available at [GitHub repository URL]. The repository includes:
- Data loading and preprocessing scripts
- All four prompt templates with parameter configurations
- WSD engine implementations (Lesk + LLM callers)
- Evaluation scripts with statistical tests
- Figure generation notebooks
- Raw experimental results (CSV format)

---

*Section status: DRAFT WITH PLACEHOLDERS — requires actual system specs and data stats after Sprint 1*
