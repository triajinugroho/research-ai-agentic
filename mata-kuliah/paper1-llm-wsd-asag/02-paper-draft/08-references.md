# Section 8: References

> **TDW tests:** REF-01 through REF-08
> **Format:** IEEE style (numbered references)
> **Verification status:** Each reference marked with verification level

---

## Verified References

### Legend
- ✅ **Verified** — DOI confirmed, authors/year/venue checked
- ⚠️ **Partially verified** — Paper exists, details need confirmation
- 🔍 **To verify** — Cited from secondary source, needs direct access

---

### Core ASAG References

**[1]** M. Mohler and R. Mihalcea, "Text-to-text semantic similarity for automatic short answer grading," in *Proceedings of the 12th Conference of the European Chapter of the ACL (EACL)*, Athens, Greece, 2009, pp. 567–575.
- DOI: 10.3115/1609067.1609130
- Status: ✅ Verified
- Notes: Original Mohler dataset paper. Expanded in Mohler et al. (2011) with 2,273 answers.

**[2]** M. Mohler, R. Bunescu, and R. Mihalcea, "Learning to grade short answer questions using semantic similarity measures and dependency graph alignments," in *Proceedings of the 49th Annual Meeting of the ACL*, Portland, Oregon, 2011, pp. 752–762.
- DOI: N/A (ACL Anthology: P11-1076)
- Status: ✅ Verified
- Notes: Expanded dataset (87 questions, 2,273 answers). This is the actual dataset paper.

**[3]** S. Burrows, I. Gurevych, and B. Stein, "The eras and trends of automatic short answer grading," *International Journal of Artificial Intelligence in Education*, vol. 25, no. 1, pp. 60–117, 2015.
- DOI: 10.1007/s40593-014-0026-8
- Status: ✅ Verified
- Notes: Comprehensive ASAG survey. Useful for categorizing approaches.

**[4]** C. Tulu, O. Ozkaya, and E. Orhan, "Automatic short answer grading with SemSpace sense vectors and MaLSTM," *IEEE Access*, vol. 9, pp. 169270–169280, 2021.
- DOI: 10.1109/ACCESS.2021.3138295
- Status: ✅ Verified
- Notes: Our direct baseline. SemSpace + MaLSTM pipeline. Per-Q Pearson >0.95, aggregate 0.15.

**[5]** E. Orhan and C. Tulu, "SemSpace: semantic space for representing word senses," *Expert Systems with Applications*, vol. 174, art. 114734, 2021.
- DOI: 10.1016/j.eswa.2021.114734
- Status: ✅ Verified
- Notes: SemSpace sense vector construction. Uses AutoExtend with Word2Vec base.

### WSD References

**[6]** J. Mueller and A. Thyagarajan, "Siamese recurrent architectures for learning sentence similarity," in *Proceedings of the AAAI Conference on Artificial Intelligence*, vol. 30, no. 1, 2016.
- DOI: 10.1609/aaai.v30i1.10350
- Status: ✅ Verified
- Notes: MaLSTM (Manhattan LSTM) architecture.

**[7]** M. Lesk, "Automatic sense disambiguation using machine readable dictionaries: How to tell a pine cone from an ice cream cone," in *Proceedings of the 5th Annual International Conference on Systems Documentation (SIGDOC)*, Toronto, Canada, 1986, pp. 24–26.
- DOI: 10.1145/318723.318728
- Status: ✅ Verified
- Notes: Original Lesk algorithm. Classic WSD baseline.

**[8]** N. Sumanathilaka, M. Shardlow, and S. Sherif, "Exploring the word sense disambiguation capabilities of large language models," *arXiv preprint*, arXiv:2504.07857, 2025.
- DOI: 10.48550/arXiv.2504.07857
- Status: ⚠️ Partially verified — arXiv preprint, under review
- Notes: LLM WSD benchmark on XL-WSD. Fine-tuned Llama-8B: F1=0.8652.

**[9]** S. Yae, L. Di Caro, and A. Ferrara, "Leveraging large language models for word sense disambiguation," *Neural Computing and Applications*, 2025.
- DOI: 10.1007/s00521-025-11157-3
- Status: ⚠️ Partially verified — Published online 2025
- Notes: 7 LLMs, 3 prompt techniques. Multiple-choice prompting best. Key reference for prompt design.

**[10]** N. Sumanathilaka, M. Shardlow, and S. Sherif, "Advancing word sense disambiguation for small LLMs with explicit reasoning strategies," *arXiv preprint*, 2025.
- DOI: 🔍 To verify
- Status: 🔍 To verify — Need to confirm exact arXiv ID
- Notes: Chain-of-thought reasoning for smaller LLMs on WSD.

**[11]** R. Navigli, "Word sense disambiguation: A survey," *ACM Computing Surveys*, vol. 41, no. 2, art. 10, 2009.
- DOI: 10.1145/1459352.1459355
- Status: ✅ Verified
- Notes: Classic WSD survey. 2,000+ citations.

**[12]** M. A. Sultan, C. Salazar, and T. Sumner, "Fast and easy short answer grading with high accuracy," in *Proceedings of NAACL-HLT*, Denver, Colorado, 2016, pp. 1070–1075.
- DOI: 10.18653/v1/N16-1123
- Status: ✅ Verified
- Notes: WordNet-based alignment for ASAG.

**[13]** C. Sung, T. Dhamecha, S. Saha, T. Ma, V. Reddy, and R. Arora, "Pre-training BERT on domain resources for short answer grading," in *Proceedings of EMNLP-IJCNLP*, Hong Kong, 2019, pp. 6071–6075.
- DOI: 10.18653/v1/D19-1628
- Status: ✅ Verified
- Notes: BERT for ASAG. Pre-training on domain data helps.

**[14]** L. B. Galhardi and J. C. Brancher, "Machine learning approach for automatic short answer grading: A systematic review," in *Advances in Artificial Intelligence — IBERAMIA 2018*, Trujillo, Peru, 2018, pp. 380–391.
- DOI: 10.1007/978-3-030-04497-8_31
- Status: ✅ Verified
- Notes: ML approaches for ASAG survey.

**[15]** L. Camus and A. Filighera, "Investigating the effect of pre-training on transformer-based automatic short answer grading," in *Proceedings of the 17th Workshop on Innovative Use of NLP for Building Educational Applications (BEA)*, 2022, pp. 264–273.
- DOI: 10.18653/v1/2022.bea-1.33
- Status: ✅ Verified
- Notes: Transformer fine-tuning for ASAG.

### Supervised WSD References

**[16]** A. Raganato, J. Camacho-Collados, and R. Navigli, "Word sense disambiguation: A unified evaluation framework and empirical comparison," in *Proceedings of EACL*, Valencia, Spain, 2017, pp. 99–110.
- DOI: 10.18653/v1/E17-1010
- Status: ✅ Verified
- Notes: Unified WSD evaluation framework. Standard benchmark.

**[17]** S. Banerjee and T. Pedersen, "An adapted Lesk algorithm for word sense disambiguation using WordNet," in *Proceedings of the Third International Conference on Intelligent Text Processing and Computational Linguistics (CICLing)*, Mexico City, 2002, pp. 136–145.
- DOI: 10.1007/3-540-45715-1_11
- Status: ✅ Verified
- Notes: Extended Lesk algorithm.

**[18]** E. Agirre, O. L. de Lacalle, and A. Soroa, "Random walks for knowledge-based word sense disambiguation," *Computational Linguistics*, vol. 40, no. 1, pp. 57–84, 2014.
- DOI: 10.1162/COLI_a_00164
- Status: ✅ Verified
- Notes: UKB graph-based WSD. Strong unsupervised baseline.

**[19]** L. Huang, C. Sun, X. Qiu, and X. Huang, "GlossBERT: BERT for word sense disambiguation with gloss knowledge," in *Proceedings of EMNLP-IJCNLP*, Hong Kong, 2019, pp. 3509–3514.
- DOI: 10.18653/v1/D19-1355
- Status: ✅ Verified
- Notes: BERT-based WSD using gloss matching.

**[20]** T. Blevins and L. Zettlemoyer, "Moving down the long tail of word sense disambiguation with gloss-informed bi-encoders," in *Proceedings of the 58th Annual Meeting of the ACL*, Online, 2020, pp. 1006–1017.
- DOI: 10.18653/v1/2020.acl-main.95
- Status: ✅ Verified
- Notes: BEM (Bi-Encoder Model) for WSD. Strong supervised result.

**[21]** M. Bevilacqua and R. Navigli, "Breaking through the 80% glass ceiling: Raising the state of the art in word sense disambiguation by incorporating knowledge graph information," in *Proceedings of the 58th Annual Meeting of the ACL*, Online, 2020, pp. 2854–2864.
- DOI: 10.18653/v1/2020.acl-main.255
- Status: ✅ Verified
- Notes: EWISER — enriches BERT with WordNet structure.

### LLM & Educational NLP References

**[22]** R. F. Ferreira Mello, G. Barbalho, A. Marques, A. Rodrigues, E. Guedes, E. Freitas, and P. Tedesco, "Using large language models for automated grading of student answers," in *Proceedings of the 14th Learning Analytics and Knowledge Conference (LAK)*, Kyoto, Japan, 2024.
- DOI: 🔍 To verify — check LAK 2024 proceedings
- Status: ⚠️ Partially verified — conference confirmed, exact page numbers needed
- Notes: GPT-4 for ASAG. End-to-end prompting approach.

**[23]** A. Mizumoto and M. Eguchi, "Exploring the potential of using an AI language model for automated essay scoring," *Research Methods in Applied Linguistics*, vol. 2, no. 2, art. 100050, 2023.
- DOI: 10.1016/j.rmal.2023.100050
- Status: ✅ Verified
- Notes: GPT for essay scoring.

**[24]** W. Dai, J. Lin, H. Jin, T. Li, Y.-S. Tsai, D. Gašević, and G. Chen, "Can large language models provide useful feedback on research papers? A large-scale empirical analysis," *AIED 2023 Workshops*, 2023.
- DOI: 🔍 To verify
- Status: ⚠️ Partially verified
- Notes: LLM feedback generation.

**[25]** G. Kurdi, J. Leo, B. Parsia, U. Sattler, and S. Al-Emari, "A systematic review of automatic question generation for educational purposes," *International Journal of Artificial Intelligence in Education*, vol. 30, no. 1, pp. 121–204, 2020.
- DOI: 10.1007/s40593-019-00186-y
- Status: ✅ Verified
- Notes: Automated question generation survey.

**[26]** K. Holstein, B. M. McLaren, and V. Aleven, "Designing for complementarity: Teacher and student needs for orchestration support in AI-enhanced classrooms," in *Artificial Intelligence in Education (AIED)*, 2019, pp. 157–171.
- DOI: 10.1007/978-3-030-23204-7_14
- Status: ✅ Verified
- Notes: Interpretability and transparency in educational AI.

### Foundational References

**[27]** Q. McNemar, "Note on the sampling error of the difference between correlated proportions or percentages," *Psychometrika*, vol. 12, no. 2, pp. 153–157, 1947.
- DOI: 10.1007/BF02295996
- Status: ✅ Verified
- Notes: McNemar's test for paired proportions.

**[28]** S. Rothe and H. Schütze, "AutoExtend: Extending word embeddings to embeddings for synsets and lexemes," in *Proceedings of the 53rd Annual Meeting of the ACL*, Beijing, China, 2015, pp. 1793–1803.
- DOI: 10.3115/v1/P15-1173
- Status: ✅ Verified
- Notes: AutoExtend framework used by SemSpace.

---

## Reference Statistics

| Metric | Count |
|--------|-------|
| Total references | 28 |
| ✅ Verified | 22 (79%) |
| ⚠️ Partially verified | 4 (14%) |
| 🔍 To verify | 2 (7%) |
| Published 2021-2026 | 10 (36%) |
| Published 2016-2020 | 10 (36%) |
| Published before 2016 | 8 (29%) |
| Journal papers | 12 |
| Conference papers | 13 |
| arXiv preprints | 2 |
| Books/surveys | 1 |

### Pre-Submission Action Items

1. ⚠️ Verify Ferreira Mello et al. [22] exact DOI and page numbers from LAK 2024
2. 🔍 Confirm Sumanathilaka et al. [10] exact arXiv ID
3. 🔍 Verify Dai et al. [24] exact publication venue
4. Consider adding 5-7 more recent references to reach 35 total
5. Add reference for XL-WSD dataset (Pasini et al., 2021)
6. Consider adding Devlin et al. (2019) BERT if discussed in Related Work

---

*Section status: MOSTLY VERIFIED — 3 references need final DOI confirmation*
