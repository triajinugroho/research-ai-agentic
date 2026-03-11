# Annotated Bibliography — Paper 1: LLM-WSD for ASAG

## Reading Guide

Setiap entry memiliki:
- **Identitas:** Authors, year, title, venue, DOI
- **Ringkasan:** 2-3 kalimat inti paper
- **Relevansi:** Kenapa penting untuk Paper 1 kita
- **Apa yang TIDAK dilakukan:** Gap yang kita isi
- **Key data points:** Angka-angka yang kita cite
- **Must-read sections:** Bagian yang wajib dibaca tim
- **Priority:** A (must read), B (should read), C (good to know)

---

## Stream 1: ASAG (Automatic Short Answer Grading)

---

### [1] Mohler & Mihalcea (2009) — The Original Benchmark

**Full citation:** M. Mohler and R. Mihalcea, "Text-to-text semantic similarity for automatic short answer grading," in *Proceedings of EACL 2009*, pp. 567–575.
**DOI:** 10.3115/1609067.1609130
**Priority:** A

**Ringkasan:** Membandingkan 8 similarity measures (BLEU, LSA, ESA, dll.) untuk ASAG pada dataset CS dari UNT. Mengusulkan kombinasi measures sebagai pendekatan terbaik.

**Relevansi untuk kita:**
- Memperkenalkan dataset Mohler yang kita gunakan
- Baseline awal untuk ASAG pada data CS
- Best result: per-question Pearson r = 0.518

**Apa yang TIDAK dilakukan:** Tidak ada sense-level processing. Semua measures beroperasi di level kata atau dokumen, bukan di level makna (synset).

**Key data points:**
- 87 questions, ~2,273 answers (expanded in Mohler et al. 2011)
- Grading scale 0-5, 2 human graders
- Domain: CS (data structures, algorithms, OS)
- Best combined measure: r = 0.518

**Must-read:** Section 3 (dataset), Section 4 (measures), Table 2 (results)

---

### [2] Mohler, Bunescu & Mihalcea (2011) — Expanded Dataset

**Full citation:** M. Mohler, R. Bunescu, and R. Mihalcea, "Learning to grade short answer questions using semantic similarity measures and dependency graph alignments," in *Proceedings of ACL 2011*, pp. 752–762.
**ACL Anthology:** P11-1076
**Priority:** A

**Ringkasan:** Memperluas dataset 2009 menjadi 87 questions × 2,273 answers. Menambahkan dependency graph alignment sebagai fitur. Memperkenalkan pendekatan supervised learning untuk menggabungkan similarity measures.

**Relevansi:** Versi definitif dataset yang kita dan Tulu gunakan. Harus dicite untuk deskripsi dataset.

**Apa yang TIDAK dilakukan:** Masih tidak ada WSD. Dependency graph beroperasi di level sintaksis, bukan semantik sense-level.

**Key data points:**
- Full dataset specs: 87Q, 2,273A, 0-5 scale
- Best system: r = 0.5180 (knowledge-based), r = 0.5544 (combined)

**Must-read:** Section 2 (dataset description — definitive reference)

---

### [3] Burrows, Gurevych & Stein (2015) — ASAG Survey

**Full citation:** S. Burrows, I. Gurevych, and B. Stein, "The eras and trends of automatic short answer grading," *Int. J. Artificial Intelligence in Education*, vol. 25, no. 1, pp. 60–117, 2015.
**DOI:** 10.1007/s40593-014-0026-8
**Priority:** B

**Ringkasan:** Survey komprehensif ASAG dari era rule-based sampai machine learning. Mengkategorikan pendekatan menjadi 5 era. Mengidentifikasi tren dan tantangan.

**Relevansi:** Framing Related Work. Taxonomy pendekatan ASAG yang kita gunakan untuk memposisikan pipeline approach.

**Apa yang TIDAK dilakukan:** Survey berakhir 2014 — tidak mencakup era deep learning, transformer, atau LLM. Tidak membahas WSD sebagai komponen ASAG secara khusus.

**Key data points:**
- 5 eras: concept mapping, info extraction, corpus-based, ML, fusion
- 35 systems reviewed
- Identifies "semantic gap" as key challenge

**Must-read:** Section 2 (taxonomy), Section 5 (challenges — semantic gap)

---

### [4] Tulu, Ozkaya & Orhan (2021) — OUR DIRECT BASELINE ★★★

**Full citation:** C. Tulu, O. Ozkaya, and E. Orhan, "Automatic short answer grading with SemSpace sense vectors and MaLSTM," *IEEE Access*, vol. 9, pp. 169270–169280, 2021.
**DOI:** 10.1109/ACCESS.2021.3138295
**Priority:** A (CRITICAL — read every section)

**Ringkasan:** Mengusulkan pipeline ASAG yang beroperasi di level sense: (1) WSD via Lesk → (2) SemSpace sense vector lookup → (3) MaLSTM similarity scoring. Diuji pada dataset Mohler.

**Relevansi:** BASELINE LANGSUNG. Kita menggunakan pipeline yang sama, hanya mengganti step WSD.

**Apa yang TIDAK dilakukan:**
- Hanya menggunakan Lesk — tidak pernah menguji WSD alternatif
- Tidak menganalisis apakah WSD adalah bottleneck
- Tidak mencoba LLM-based WSD (belum ada paper LLM-WSD di 2021)
- Tidak memberikan error analysis per WSD decision

**Key data points:**
- Per-question Pearson r: >0.95 (beberapa pertanyaan) — SANGAT KUAT
- Aggregate Pearson r: 0.15 — SANGAT LEMAH
- Gap per-Q vs aggregate = evidence bahwa ada inkonsistensi lintas pertanyaan
- RMSE: ~1.0
- SemSpace vectors: 300-dim, WordNet-based
- MaLSTM hidden dim: 50

**Must-read:** SELURUH PAPER. Fokus: Section III (methodology), Table II (results), Section V (discussion tentang aggregate vs per-question gap).

**Questions to answer while reading:**
1. Exactly how is Lesk called? NLTK version? Parameters?
2. How is MaLSTM trained? What split? Random seed?
3. What happens when Lesk returns None?
4. What percentage of words are OOV for SemSpace?

---

### [5] Orhan & Tulu (2021) — SemSpace Vectors

**Full citation:** E. Orhan and C. Tulu, "SemSpace: semantic space for representing word senses," *Expert Systems with Applications*, vol. 174, art. 114734, 2021.
**DOI:** 10.1016/j.eswa.2021.114734
**Priority:** A

**Ringkasan:** Membangun sense-level vectors (SemSpace) dengan meng-extend Word2Vec embeddings ke level synset menggunakan framework AutoExtend. Evaluasi pada similarity tasks.

**Relevansi:** Stage 3 pipeline kita — sense vectors. Perlu memahami konstruksinya untuk interpreting results.

**Apa yang TIDAK dilakukan:** Tidak mengevaluasi SemSpace dalam konteks ASAG (dilakukan di [4]). Tidak menguji sensitivitas terhadap WSD accuracy.

**Key data points:**
- Base embeddings: Google News Word2Vec (300-dim)
- Extension method: AutoExtend (Rothe & Schütze, 2015)
- Coverage: X synsets (perlu dicek dari paper)

**Must-read:** Section 3 (construction method), Section 4.1 (coverage stats)

---

### [12] Sultan, Salazar & Sumner (2016) — WordNet ASAG

**Full citation:** M. A. Sultan, C. Salazar, and T. Sumner, "Fast and easy short answer grading with high accuracy," in *Proceedings of NAACL-HLT 2016*, pp. 1070–1075.
**DOI:** 10.18653/v1/N16-1123
**Priority:** B

**Ringkasan:** Menggunakan WordNet-based alignment untuk mencocokkan kata-kata antara student dan reference answer. Achieves strong results tanpa deep learning.

**Relevansi:** Contoh knowledge-based ASAG yang menggunakan WordNet tapi BUKAN di level sense. Kontras dengan Tulu yang menggunakan sense-level processing.

**Apa yang TIDAK dilakukan:** Alignment berbasis kata, bukan sense. Tidak ada WSD eksplisit.

**Must-read:** Section 2 (alignment method)

---

### [13] Sung et al. (2019) — BERT for ASAG

**Full citation:** C. Sung et al., "Pre-training BERT on domain resources for short answer grading," in *Proceedings of EMNLP-IJCNLP 2019*, pp. 6071–6075.
**DOI:** 10.18653/v1/D19-1628
**Priority:** B

**Ringkasan:** Fine-tune BERT untuk ASAG dengan tambahan pre-training pada domain-specific text. Menunjukkan domain adaptation membantu.

**Relevansi:** Representasi neural approach untuk ASAG. Kontras dengan knowledge-based approach (Tulu). Shows that pre-trained models benefit from domain data.

**Apa yang TIDAK dilakukan:** End-to-end BERT — tidak ada komponen WSD eksplisit. No sense-level analysis.

---

### [15] Camus & Filighera (2022) — Transformers for ASAG

**Full citation:** L. Camus and A. Filighera, "Investigating the effect of pre-training on transformer-based automatic short answer grading," in *BEA Workshop 2022*, pp. 264–273.
**DOI:** 10.18653/v1/2022.bea-1.33
**Priority:** C

**Ringkasan:** Membandingkan beberapa transformer architectures untuk ASAG. Investigasi effect pre-training strategies.

**Relevansi:** Recent transformer-based ASAG. Shows state of the art but no interpretability.

---

### [22] Ferreira Mello et al. (2024) — GPT-4 for ASAG

**Full citation:** R. F. Ferreira Mello et al., "Using large language models for automated grading of student answers," in *LAK 2024*.
**DOI:** TBD (verify from LAK proceedings)
**Priority:** A

**Ringkasan:** Menggunakan GPT-4 langsung untuk menilai jawaban pendek (end-to-end prompting). Zero-shot dan few-shot. Competitive results tanpa pipeline.

**Relevansi:** Representasi paradigma "LLM as judge" yang kontras dengan pipeline approach kita. Penting untuk Discussion (Section 6.3).

**Apa yang TIDAK dilakukan:**
- End-to-end = black box. Tidak bisa tahu apakah LLM melakukan WSD internal
- Tidak ada component analysis
- Mahal (GPT-4 API)
- Not reproducible (proprietary model)

**Key data points:**
- GPT-4 performance: [need to read for exact numbers]
- Zero-shot vs few-shot comparison

**Must-read:** Results table, Discussion on practical deployment

---

## Stream 2: Word Sense Disambiguation (WSD)

---

### [7] Lesk (1986) — Classic WSD Baseline

**Full citation:** M. Lesk, "Automatic sense disambiguation using machine readable dictionaries," in *SIGDOC 1986*, pp. 24–26.
**DOI:** 10.1145/318723.318728
**Priority:** B (read for historical context)

**Ringkasan:** Algoritma pertama untuk WSD otomatis. Memilih sense berdasarkan overlap antara dictionary gloss dan konteks kata.

**Relevansi:** Baseline WSD yang dipakai Tulu dan kita. Perlu dipahami limitasinya: short context sensitivity, sparse glosses.

**Key data points:**
- Method: word overlap between gloss and context
- Accuracy: varies by dataset, typically 40-60% on modern benchmarks

---

### [11] Navigli (2009) — WSD Survey

**Full citation:** R. Navigli, "Word sense disambiguation: A survey," *ACM Computing Surveys*, vol. 41, no. 2, art. 10, 2009.
**DOI:** 10.1145/1459352.1459355
**Priority:** B

**Ringkasan:** Survey komprehensif WSD: supervised, unsupervised, knowledge-based methods. 2000+ citations. Mendefinisikan task dan evaluation framework.

**Relevansi:** Framing untuk Related Work Section 2.2. Taxonomy of WSD approaches.

---

### [16] Raganato, Camacho-Collados & Navigli (2017) — WSD Evaluation Framework

**Full citation:** A. Raganato, J. Camacho-Collados, and R. Navigli, "Word sense disambiguation: A unified evaluation framework and empirical comparison," in *EACL 2017*, pp. 99–110.
**DOI:** 10.18653/v1/E17-1010
**Priority:** B

**Ringkasan:** Mendefinisikan unified evaluation framework untuk WSD. Membandingkan semua major approaches pada benchmark yang sama.

**Relevansi:** Evaluation methodology reference. Our WSD evaluation (gold standard + accuracy metrics) follows this tradition.

---

### [19] Huang et al. (2019) — GlossBERT

**Full citation:** L. Huang et al., "GlossBERT: BERT for word sense disambiguation with gloss knowledge," in *EMNLP-IJCNLP 2019*, pp. 3509–3514.
**DOI:** 10.18653/v1/D19-1355
**Priority:** B

**Ringkasan:** Frame WSD sebagai sentence-pair classification: context vs gloss. Fine-tune BERT. Achieves strong results.

**Relevansi:** Supervised WSD SOTA reference. Penting untuk Related Work — kita acknowledge tapi argue our focus is zero-shot.

**Apa yang TIDAK dilakukan:** Requires training data. Not evaluated on downstream tasks.

**Key data points:** F1 on ALL benchmark: ~77% (pre-EWISER era)

---

### [20] Blevins & Zettlemoyer (2020) — BEM

**Full citation:** T. Blevins and L. Zettlemoyer, "Moving down the long tail of word sense disambiguation with gloss-informed bi-encoders," in *ACL 2020*, pp. 1006–1017.
**DOI:** 10.18653/v1/2020.acl-main.95
**Priority:** C

**Ringkasan:** Bi-encoder architecture yang separately encode context dan gloss, lalu match. Handles rare senses better.

**Relevansi:** Supervised SOTA reference.

---

### [21] Bevilacqua & Navigli (2020) — EWISER

**Full citation:** M. Bevilacqua and R. Navigli, "Breaking through the 80% glass ceiling: Raising the state of the art in word sense disambiguation by incorporating knowledge graph information," in *ACL 2020*, pp. 2854–2864.
**DOI:** 10.18653/v1/2020.acl-main.255
**Priority:** C

**Ringkasan:** Enriches BERT embeddings dengan WordNet structure. First to break 80% F1 on ALL benchmark.

**Relevansi:** SOTA reference point for supervised WSD.

**Key data points:** F1 on ALL: 80.8%

---

## Stream 3: LLM-Based WSD (Core Novelty References)

---

### [8] Sumanathilaka, Shardlow & Sherif (2025a) — LLM WSD Benchmark ★★

**Full citation:** N. Sumanathilaka, M. Shardlow, and S. Sherif, "Exploring the word sense disambiguation capabilities of large language models," *arXiv:2504.07857*, 2025.
**DOI:** 10.48550/arXiv.2504.07857
**Priority:** A (CRITICAL)

**Ringkasan:** Benchmark komprehensif kemampuan WSD berbagai LLM pada dataset XL-WSD. Evaluasi zero-shot dan fine-tuned. Menunjukkan LLM competitive dengan supervised methods.

**Relevansi:** JUSTIFIKASI UTAMA bahwa LLM-based WSD itu viable. Tanpa paper ini, premise kita lemah.

**Apa yang TIDAK dilakukan:**
- HANYA intrinsic evaluation (accuracy pada WSD benchmark)
- TIDAK ada downstream task evaluation
- TIDAK diuji pada educational text
- TIDAK diuji pada domain-specific text (CS)

**Key data points:**
- Fine-tuned Llama-8B: F1 = 0.8652 (English, XL-WSD)
- Zero-shot performance varies: model size matters but not linearly
- Smaller models with proper prompting can approach larger models

**Must-read:** Table 3 (main results), Section 4 (analysis of model size effects), Section 5 (error analysis)

**Questions to verify:**
1. Which exact Llama variant? Llama-2 or Llama-3?
2. What prompting strategy for zero-shot?
3. How do they handle output parsing?

---

### [9] Yae, Di Caro & Ferrara (2025) — Prompt Design for WSD ★★

**Full citation:** S. Yae, L. Di Caro, and A. Ferrara, "Leveraging large language models for word sense disambiguation," *Neural Computing and Applications*, 2025.
**DOI:** 10.1007/s00521-025-11157-3
**Priority:** A (CRITICAL)

**Ringkasan:** Mengevaluasi 7 LLMs dengan 3 teknik prompting untuk WSD: multiple choice, binary verification, unseen word. Multiple-choice prompting secara signifikan terbaik.

**Relevansi:** LANGSUNG menginformasi desain prompt kita. P1 (basic) dan P2 (with examples) terinspirasi dari paper ini. Juga menunjukkan bahwa prompt design matters untuk WSD.

**Apa yang TIDAK dilakukan:**
- TIDAK ada downstream application evaluation
- TIDAK ada domain-specific evaluation
- TIDAK ada educational text

**Key data points:**
- Multiple-choice prompting >> open-ended prompting
- Structured prompts help smaller models more than larger ones
- 7 LLMs tested (need to check which ones — overlap with ours?)

**Must-read:** Section 3 (prompt design — PALING PENTING), Table 4 (prompt comparison results), Section 5 (model-size interaction with prompt type)

**Design decisions informed by this paper:**
- Our P1 uses their multiple-choice format (numbered synsets)
- Our P2 adds examples (their best augmentation)
- Our P3/P4 are OUR extensions not covered by Yae

---

### [10] Sumanathilaka, Shardlow & Sherif (2025b) — Small LLMs + Reasoning ★

**Full citation:** N. Sumanathilaka, M. Shardlow, and S. Sherif, "Advancing word sense disambiguation for small LLMs with explicit reasoning strategies," *arXiv preprint*, 2025.
**DOI:** TBD — PERLU DIVERIFIKASI
**Priority:** A

**Ringkasan:** Menunjukkan bahwa smaller LLMs (7B-8B) dengan chain-of-thought reasoning bisa mendekati performa model besar untuk WSD.

**Relevansi:** Justifikasi pilihan model kita (7B-8B). Juga justifikasi P4 (chain-of-thought prompt).

**Apa yang TIDAK dilakukan:** Sama seperti [8] — no downstream application.

**Key data points:**
- CoT improves small model WSD accuracy by X% (verify)
- 7B models with reasoning ≈ 70B models without

**ACTION: Verify this paper exists with exact arXiv ID**

---

## Stream 4: LLMs in Education

---

### [23] Mizumoto & Eguchi (2023) — GPT for Essay Scoring

**Full citation:** A. Mizumoto and M. Eguchi, "Exploring the potential of using an AI language model for automated essay scoring," *Research Methods in Applied Linguistics*, vol. 2, no. 2, art. 100050, 2023.
**DOI:** 10.1016/j.rmal.2023.100050
**Priority:** C

**Ringkasan:** GPT models for essay scoring (bukan short answer). Shows LLMs are viable for educational assessment.

**Relevansi:** Broader context for LLMs in assessment. Cite in Related Work 2.3.

---

### [25] Kurdi et al. (2020) — Automated Question Generation Survey

**Full citation:** G. Kurdi et al., "A systematic review of automatic question generation for educational purposes," *IJAIED*, vol. 30, no. 1, pp. 121–204, 2020.
**DOI:** 10.1007/s40593-019-00186-y
**Priority:** C

**Ringkasan:** Survey automated question generation. Complementary to ASAG.

**Relevansi:** Context for broader educational NLP landscape.

---

## Stream 5: Methodological References

---

### [6] Mueller & Thyagarajan (2016) — MaLSTM

**Full citation:** J. Mueller and A. Thyagarajan, "Siamese recurrent architectures for learning sentence similarity," in *AAAI 2016*.
**DOI:** 10.1609/aaai.v30i1.10350
**Priority:** B

**Ringkasan:** Mengusulkan Manhattan LSTM (MaLSTM) — Siamese LSTM yang menggunakan Manhattan distance untuk sentence similarity.

**Relevansi:** Stage 4 pipeline kita. Perlu memahami arsitekturnya.

**Key data points:**
- Similarity = exp(-||h1 - h2||₁) where h1, h2 are final LSTM hidden states
- Originally for paraphrase detection

**Must-read:** Section 3 (architecture definition)

---

### [28] Rothe & Schütze (2015) — AutoExtend

**Full citation:** S. Rothe and H. Schütze, "AutoExtend: Extending word embeddings to embeddings for synsets and lexemes," in *ACL 2015*, pp. 1793–1803.
**DOI:** 10.3115/v1/P15-1173
**Priority:** B (critical if Plan B needed for SemSpace)

**Ringkasan:** Framework untuk meng-extend word embeddings (e.g., Word2Vec) ke synset-level dan lexeme-level embeddings menggunakan WordNet constraints.

**Relevansi:** Foundation of SemSpace construction [5]. If we need to reconstruct SemSpace vectors (Plan B), we use this.

---

## Additional References to Consider Adding

### Not Yet in Paper — Should Add

| Paper | Year | Why Add |
|-------|------|---------|
| **Miller (1995)** — WordNet | 1995 | Foundational reference for synsets. *Communications of the ACM, 38(11), 39-41.* DOI: 10.1145/219717.219748 |
| **Pasini et al. (2021)** — XL-WSD | 2021 | Dataset used by Sumanathilaka [8]. *ACL 2021.* DOI: 10.18653/v1/2021.acl-long.243 |
| **Devlin et al. (2019)** — BERT | 2019 | If we mention BERT in Related Work. *NAACL 2019.* DOI: 10.18653/v1/N19-1423 |
| **Loureiro & Jorge (2019)** — LMMS | 2019 | Alternative sense embeddings (Plan C). *ACL 2019.* DOI: 10.18653/v1/P19-1569 |
| **Touvron et al. (2023)** — Llama 2 | 2023 | Model family reference. *arXiv:2307.09288* |
| **Jiang et al. (2023)** — Mistral | 2023 | Model reference. *arXiv:2310.06825* |
| **Team Qwen (2024)** — Qwen 2.5 | 2024 | Model reference. Check exact arXiv ID. |

---

## Tim Reading Assignment

### Bu Endang (Researcher) — Priority A papers:
1. [4] Tulu et al. (2021) — SELURUH PAPER, catat semua detail methodology
2. [8] Sumanathilaka et al. (2025a) — Focus: results tables, WSD evaluation protocol
3. [9] Yae et al. (2025) — Focus: prompt design (Section 3), kita adopt prompt strategy dari sini
4. [22] Ferreira Mello et al. (2024) — Focus: results, untuk framing Discussion

### Teguh (Promotor review) — Priority A+B papers:
1. [3] Burrows et al. (2015) — ASAG landscape, pastikan kita tidak miss major approaches
2. [11] Navigli (2009) — WSD landscape, pastikan terminology kita benar
3. [8] & [9] — Verify our LLM-WSD claims align with what these papers actually say

### Tri Aji (Technical execution) — Priority A+B papers:
1. [4] Tulu et al. (2021) — Implementation details, reproduce pipeline
2. [5] Orhan & Tulu (2021) — SemSpace construction, Plan B preparation
3. [6] Mueller & Thyagarajan (2016) — MaLSTM architecture details
4. [9] Yae et al. (2025) — Prompt design details untuk implementation

---

## Quick Reference Card

### Angka-angka yang sering dikutip:

| Fact | Number | Source |
|------|--------|--------|
| Mohler dataset: questions | 87 | [2] |
| Mohler dataset: answers | 2,273 | [2] |
| Tulu per-question best Pearson | >0.95 | [4] |
| Tulu aggregate Pearson | 0.15 | [4] |
| Tulu RMSE | ~1.0 | [4] |
| Sumanathilaka best LLM WSD F1 | 0.8652 | [8] |
| EWISER SOTA F1 (supervised) | 80.8% | [21] |
| SemSpace vector dim | 300 | [5] |

---

*Document version: 1.0 — March 2026*
*Total papers annotated: 20*
*Recommended additions: 7*
