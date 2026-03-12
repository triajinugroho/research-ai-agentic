# Frontmatter — Paper 1

## Title

**Does Better Disambiguation Mean Better Grading? Evaluating Large Language Models for Word Sense Disambiguation in Knowledge-Based Automatic Short Answer Grading**

### Alternative Titles (for different venues)

- **IEEE TLT version:** "Does Better Disambiguation Mean Better Grading? Evaluating Large Language Models for Word Sense Disambiguation in Knowledge-Based Automatic Short Answer Grading"
- **ESWA version:** "LLM-Enhanced Word Sense Disambiguation for Automatic Short Answer Grading: A Comparative Evaluation on the SemSpace-MaLSTM Pipeline"
- **Short version:** "LLM-Based WSD for Improved Automatic Short Answer Grading"

---

## Authors

Endang Ripmiatin¹*, Teguh Eko Budiarto², Tri Aji Nugroho¹

¹ Program Studi Informatika, Universitas Al Azhar Indonesia, Jakarta, Indonesia
² [Teguh's affiliation]

\* Corresponding author: endang.ripmiatin@uai.ac.id

---

## Abstract

> **Target: ≤ 250 words | Current: ~230 words (with placeholders)**

Automatic Short Answer Grading (ASAG) systems that rely on semantic similarity between student and reference answers must accurately capture word meaning. In knowledge-based pipelines that use sense-level embeddings — such as the SemSpace-MaLSTM architecture — Word Sense Disambiguation (WSD) directly determines which sense vector represents each word, making it a critical yet understudied component. Prior work on this pipeline employed the traditional Lesk algorithm for WSD and reported strong per-question correlations (Pearson r > 0.95) but weak aggregate performance (r ≈ 0.15), suggesting inconsistent disambiguation across diverse vocabulary.

Recent studies have demonstrated that Large Language Models (LLMs) possess competitive WSD capabilities in general-domain benchmarks. However, no prior research has evaluated whether this capability translates to improved downstream ASAG performance. We address this gap by systematically comparing four LLMs — Qwen-2.5, Mistral-7B, Llama-3.1-8B, and Gemini-1.5-Flash — against the Lesk baseline as WSD engines within an otherwise identical SemSpace-MaLSTM pipeline, evaluated on the Mohler computer science dataset.

Our evaluation spans both intrinsic WSD accuracy (against a 500-word gold standard we constructed with inter-annotator agreement κ = [TBD]) and extrinsic ASAG performance (Pearson r and RMSE). We further contribute an error cascade analysis tracing how specific WSD decisions propagate through the pipeline to affect final grades. Results show that [BEST_LLM] achieves [X]% WSD accuracy (compared to [Y]% for Lesk), which translates to [an improvement / no significant change / a mixed effect] in downstream grading performance, with aggregate Pearson r [increasing from 0.15 to Z / remaining unchanged].

---

## Keywords

Word Sense Disambiguation, Large Language Models, Automatic Short Answer Grading, SemSpace, WordNet, Sense Embeddings, Educational NLP

---

## IEEE Taxonomy Terms

- Computing methodologies → Natural language processing → Word sense disambiguation
- Computing methodologies → Machine learning → Machine learning approaches
- Applied computing → Education → Computer-assisted instruction

---

## Data Availability Statement

The Mohler dataset used in this study is publicly available. Our gold standard WSD annotations and all experimental code are available at [GitHub repository URL]. Pre-trained model weights are accessible through their respective public repositories. SemSpace vectors were [obtained from the original authors / reconstructed following Orhan and Tulu (2021)].

---

## Ethical Statement

This study uses the publicly available Mohler et al. (2011) dataset containing anonymized student answers from a computer science course. No personally identifiable information is present in the dataset. LLMs were used as automated WSD tools, not as substitutes for human grading decisions. No student data was collected for this study.

---

## Acknowledgments

[To be completed — acknowledge: promotor, funding if any, Tulu/Orhan for SemSpace vectors if provided]

---

## Author Contributions (CRediT)

| Author | Roles |
|--------|-------|
| Endang Ripmiatin | Conceptualization, Methodology, Investigation, Writing — Original Draft, Data Curation |
| Teguh Eko Budiarto | Supervision, Writing — Review & Editing, Validation |
| Tri Aji Nugroho | Software, Formal Analysis, Visualization, Writing — Review & Editing |

---

*Section TDW Status: Pending (requires experimental results to fill placeholders)*
