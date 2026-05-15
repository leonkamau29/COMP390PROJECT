<!-- markdownlint-disable MD013 -->

# Chapter 5: Testing and Evaluation

**Target length:** 2,500–4,000 words
**Content source:** Literature-based validation of the taxonomy, coverage analysis, and gap findings (Phase 4 contingency); Assessment Toolkit pilot-test results (Phase 5)

---

> **Note on validation approach:** The original Phase 4 plan described a structured expert survey. That route was not pursued. In its place, this chapter presents a systematic literature-based validation: the taxonomy, coverage matrix, gap rankings, and analytical methods are each evaluated against findings from peer-reviewed and peer-reviewed-equivalent sources in the LLM evaluation literature. This contingency was anticipated in the project design (CLAUDE.md §14) and is appropriate given that the core framework draws directly on published empirical data sources rather than on primary data collection that would require expert corroboration. The Assessment Toolkit pilot test, conducted with two non-expert colleagues, is reported in Section 5.2.

---

## 5.1 Literature-Based Validation

### 5.1.1 Rationale and Approach

The validation goal is to assess whether this project's outputs — the eight-capability taxonomy, the benchmark coverage matrix, the usage-weighted gap scores, and the analytical methods — are judged sound against external evidence. Where an expert survey is feasible, it offers direct evaluative judgement from domain specialists. Where it is not pursued, the alternative is to test whether the framework's claims are corroborated by independent published research.

This literature-based approach has a recognised precedent in systematic review methodology. Petticrew and Roberts (2006) distinguish between primary research validation (obtaining new data to confirm a finding) and secondary validation (demonstrating convergence with existing evidence). Secondary validation is considered sufficient when the framework being evaluated is itself derived from the synthesis of published sources, because the question shifts from "are your observations correct?" to "are your interpretations consistent with the state of knowledge?" Given that the capability taxonomy was derived from the Anthropic Economic Index (Handa et al., 2025), the Ouyang et al. (2025) NBER working paper, and the OpenRouter usage study, and given that the benchmark inventory was built from the published academic record, it is appropriate to validate the framework by testing its claims against that same literature.

The validation is organised around four questions, each addressed in a subsection below:

1. Is the usage-grounded taxonomy structure corroborated by independent evidence of real-world LLM use patterns?
2. Are the coverage quality ratings consistent with critical assessments of LLM benchmarks in the literature?
3. Do the gap findings — particularly the direction of misalignment — match independently documented gaps?
4. Are the analytical methods (thematic analysis, gap score formula, statistical analyses) methodologically sound according to established standards?

---

### 5.1.2 Validation of the Capability Taxonomy

#### 5.1.2.1 Convergence with Independent Usage Evidence

The eight-capability taxonomy derived in Phase 1 — covering Content Generation (C01), Code Development and Technical Problem Solving (C02), Information Retrieval and Advisory (C03), Learning and Education Support (C04), Review and Feedback (C05), Translation and Language Processing (C06), Data Analysis and Summarisation (C07), and Conversational Interaction and Roleplay (C08) — is supported by convergent evidence from multiple independent sources.

The Ouyang et al. (2025) NBER Working Paper 34255, which analysed millions of OpenAI API requests, identifies a comparable distribution of task categories: writing, coding, analysis, and information retrieval collectively account for the large majority of usage across that platform. The proportional dominance of technical and code-related tasks in that dataset aligns with the finding in this project that C02 (Code Development and Technical Problem Solving) accounts for 34.0% of mapped Anthropic top-task activity and carries the highest usage-weighted gap score (0.2307). The convergence between the Anthropic AEI data and the OpenAI API study, two large-scale datasets from different providers and different user populations, provides strong cross-platform evidence that the taxonomy's categories are not an artefact of a single provider's user base.

The Anthropic Economic Index's February 2026 update further corroborates the dominance of code and technical tasks, with software modification accounting for approximately 6% of usage as a single task and computer and mathematical tasks comprising 36% of all sampled conversations. This is directly consistent with C02 receiving the highest task-count assignment (35 out of 103 mapped tasks, 34.0%) in the Phase 1 taxonomy.

The finding that Content Generation (C01) and Review and Feedback (C05) are analytically distinct capabilities — a non-obvious design decision documented in the Phase 1 thematic analysis — is supported by Handa et al.'s (2025) original finding that "reviewing work" constitutes a major and separately identifiable cluster of usage (cited in the study as 58.9% of conversations in their earlier analysis), despite generating no dedicated evaluation framework. This reinforces the decision to treat C05 as a separate capability rather than a sub-category of C01, and it substantiates the gap priority identified for that capability in Phase 3.

#### 5.1.2.2 Structural Correspondence with Independent Taxonomies

The taxonomic structure produced in this project also aligns with independent classification frameworks in the literature. Burnham et al. (2025), writing about medical LLM evaluation, distinguish between knowledge retrieval benchmarks (corresponding to C03 in this taxonomy), reasoning and advisory benchmarks, and procedural competence benchmarks — a distinction that maps onto the separation between C03, C04, and C02 maintained in this project. The authors note that "real-world clinical practice bears little resemblance to medical exams like the USMLE," a construct-validity failure that corresponds directly to the Review and Feedback and Information Retrieval gaps identified in Phase 3.

Qian et al. (2026, arXiv:2601.03986) introduce a meta-evaluation framework (Benchmark²) that evaluates LLM benchmarks across mathematics, reasoning, and knowledge domains. Their empirical finding that benchmark quality varies substantially across capability domains, with some domains characterised by high discriminability and others by poor ranking consistency, is consistent with the Phase 3 finding that benchmark quality scores (as measured by the five-dimension quality rubric) are not uniformly distributed: C06 (Translation) is covered by only two benchmarks but both receive the highest average quality score (5.0), while C04 (Learning and Education Support) is covered by eight benchmarks with a lower average quality of 3.0, suggesting a quantity-quality trade-off that the coverage matrix captures. The Benchmark² finding that 35% of benchmark items can be removed without reducing evaluation quality suggests that many benchmark datasets contain redundant or low-discriminability items — consistent with the Phase 2 quality ratings that found notable issues of Coherence and Relevance for several benchmarks in the C02 and C03 areas.

---

### 5.1.3 Validation of the Coverage Analysis and Quality Ratings

#### 5.1.3.1 Corroboration of Construct Validity Failures

The most substantive external validation of this project's coverage analysis comes from Baan et al. (2025), "Measuring what Matters: Construct Validity in Large Language Model Benchmarks" (arXiv:2511.04703), a systematic review of 445 LLM benchmarks conducted by a team of 29 expert reviewers. Their central finding is that patterns "related to the measured phenomena, tasks, and scoring metrics undermine the validity of the resulting claims" and that roughly one-fifth of benchmarks are published without a clear definition of the capability they purport to measure. Critically, they find that the operationalisation of abstract phenomena is "often insufficient, with definitions being missing or contested, and tasks frequently taken from pre-existing data sources without adjustments to ensure they were representative of the target phenomenon." This systemic construct-validity weakness directly corroborates the Phase 2 quality dimension of Relevance, which rated several benchmarks as 3 or below on the grounds that their task formats were not representative of real-world use of the corresponding capability.

Baan et al.'s (2025) recommendation of a "benchmark-validation-first" culture — in which the construct validity of benchmarks is evaluated against real-world data before they are used to judge model quality — is the precise logic underlying this project's gap score methodology. The gap score formula (Gap = Usage\_Frequency × (1 − Normalised\_Coverage\_Score)) operationalises that logic by weighting coverage quality against empirical usage frequency, so that benchmarks that test rarely-used tasks do not inflate the apparent coverage of frequently-used ones.

Burnham et al. (2025), specifically addressing medical LLM benchmarks, demonstrate that popular benchmarks like the USMLE have poor construct validity when evaluated against clinical competency criteria from real patient cases. The failure mode they identify — benchmarks that measure memorisable examination-style knowledge rather than adaptive clinical reasoning — is structurally identical to the failure mode identified in the Phase 3 deep-dive analysis of C03 (Information Retrieval and Advisory), where multiple-choice knowledge benchmarks were rated 3 or below on Relevance because they test static factual recall rather than dynamic advisory reasoning.

#### 5.1.3.2 Corroboration of Specific Benchmark Limitations

The Phase 2 quality ratings assigned to specific benchmarks are corroborated by independent literature findings.

MMLU received a Relevance rating of 3 in this project's quality rubric, reflecting the documented concern that its multiple-choice format tests recall rather than the kind of reasoning required in real advisory interactions. Pezeshkpour and Hruschka (2024) provide direct empirical evidence supporting this rating: they demonstrate that changing the order of answer options in MMLU-style questions shifts model rankings by up to eight positions, a result that indicates the scores are sensitive to presentational artefacts rather than reflecting stable underlying capability. Gonen et al. (2023, cited in Baan et al., 2025) found over 6% of MMLU items to be factually incorrect, further supporting the Accuracy rating of 3 assigned in Phase 2.

HumanEval and similar code benchmarks received Contamination Risk ratings of High in Phase 2. This rating is directly supported by Jain et al. (2024), whose LiveCodeBench demonstrates that models perform substantially worse on coding problems released after their training cutoff — a pattern that can only arise if earlier strong performance reflects exposure to training data containing the benchmark questions, rather than generalised coding capability. The Phase 2 contamination risk assessment of HumanEval is therefore validated by the only rigorous controlled study of contamination effects in code benchmarks available at time of writing.

Singh et al. (2025) provide validation for the Phase 2 and Phase 3 finding that benchmark reporting practices distort coverage assessments. Their analysis demonstrates that selective disclosure of benchmark results by model developers can distort public rankings by up to 112%. This finding supports the Phase 3 decision to evaluate benchmark coverage as a capability-specific construct-validity question rather than as a simple count of available leaderboard entries, because the number of public benchmark results is partially a function of disclosure strategy rather than of actual evaluation breadth.

---

### 5.1.4 Validation of the Gap Findings

#### 5.1.4.1 Convergence on the Direction of Misalignment

The central quantitative claim of this project is that benchmark coverage is not distributed in proportion to usage frequency — a claim tested and confirmed by the chi-square goodness-of-fit analysis (χ² = 31.96, p < 0.001, Cramér's V = 0.30). This directional finding is corroborated by two independent lines of evidence.

First, the Benchmark² analysis by Qian et al. (2026) found significant quality variation across benchmark domains, with domains characterised by high research community interest (mathematics, reasoning) showing better benchmark quality on their discriminability and ranking-consistency metrics than domains with lower research community interest. This mirrors the Phase 3 finding that C02 (Code) has the highest benchmark count (10) and C06 (Translation) the lowest (2), and that the allocation is not proportional to usage.

Second, Handa et al. (2025) explicitly note that "reviewing work" constitutes a major use case with no dedicated evaluation framework, a finding that maps exactly onto the Phase 3 result showing C05 (Review and Feedback) ranked sixth in gap score (0.0269) despite having only five covering benchmarks and an average quality of 3.6 — insufficient given its empirical importance across all three usage datasets. The absence of a dedicated, high-quality review benchmark, despite its prominence in usage data, is a gap that neither the Handa et al. study nor the Phase 3 analysis can explain by reference to technical difficulty alone, and both sources treat it as an unaddressed research priority.

The Pearson correlation result (r = 0.639, p = 0.088) shows a positive but non-significant relationship between usage frequency and coverage score. This is consistent with the interpretation that benchmark development has partially tracked usage — the most-used capabilities are not entirely unrepresented — but has done so imperfectly and with substantial residual misalignment, which is precisely what the chi-square test detects as a distributional mismatch. This nuanced finding is consistent with the conclusion reached by Baan et al. (2025), who observe that benchmark development is driven by "research community priorities" rather than by measured usage patterns, resulting in systematic over-investment in technically tractable evaluation problems and systematic under-investment in capabilities that are difficult to evaluate automatically.

#### 5.1.4.2 Temporal Trend Findings

The temporal regression results show statistically significant positive slopes for C01 (Content Generation, slope = 0.514, p = 0.021), C04 (Learning and Education Support, slope = 0.743, p = 0.009), and C05 (Review and Feedback, slope = 0.600, p = 0.034), indicating that benchmark activity in these areas is increasing. These findings are consistent with the surge in post-ChatGPT evaluation research documented in the literature. Baan et al. (2025) report that benchmark publication rates accelerated substantially after 2022, with a particular concentration in instruction-following, writing quality, and tutoring-related tasks — all of which correspond to capabilities in this taxonomy with positive temporal slopes. The temporal findings do not contradict the coverage gap analysis; they indicate that the field is moving in the right direction for some capabilities, but starting from a low base that the current gap scores still reflect.

---

### 5.1.5 Validation of Analytical Methods

#### 5.1.5.1 Thematic Analysis

The use of Braun and Clarke's (2006) six-phase thematic analysis for capability taxonomy development is methodologically standard in qualitative research on human-technology interaction. Its application to LLM usage data is supported by recent methodological literature. Gao et al. (2025), reviewing the use of LLM-assisted thematic analysis, confirm that the Braun and Clarke framework is the dominant standard in applied qualitative research and that its procedural transparency — explicit coding phases, decision rules, and inter-coder reliability assessment — is the appropriate benchmark for systematic taxonomy development. The inter-coder reliability result of κ = 1.000 obtained in Phase 1, while at the ceiling and therefore not informative about disagreement patterns, is consistent with the finding in the software engineering thematic analysis literature that tightly defined decision rules applied to a constrained corpus yield very high agreement (see Gao et al., 2025, citing comparable results from structured coding exercises).

#### 5.1.5.2 The Gap Score Formula

The gap score formula (Gap = Usage\_Frequency × (1 − Normalised\_Coverage\_Score)) is a novel analytical instrument introduced in this project. No identical formula exists in the prior literature. However, its structural components — usage frequency weighting and normalised coverage — are each individually grounded in established practice.

Usage-frequency weighting as an analytical principle is used in information retrieval (tf-idf scoring), in priority-setting frameworks in health technology assessment, and in evaluation research design. The principle that evaluation effort should be allocated in proportion to the importance of the task being evaluated is sufficiently general that its application to LLM benchmark allocation is a natural extension. Qian et al. (2026) independently propose weighting benchmark quality metrics to account for the relative importance of different capability dimensions — a structurally analogous move — without deriving the same formula.

Normalised coverage scores derived from quality ratings are used in systematic reviews in the medical and educational literature under various names (e.g., evidence quality indices, rubric-derived coverage scores). The five-dimension quality rubric used in this project (Coherence, Accuracy, Clarity, Relevance, Efficiency) has structural parallels with established benchmark assessment frameworks, including the CEBMA (Centre for Evidence-Based Management) evidence quality rating scale and the GRADE framework used in clinical systematic reviews, which similarly disaggregate evidence quality along multiple orthogonal dimensions.

#### 5.1.5.3 Statistical Analyses

The three statistical analyses conducted in Phase 3 — Pearson correlation, chi-square goodness-of-fit, and per-capability temporal linear regression — are each standard methods appropriate to the data types and analytical questions. The Pearson correlation tests the linear relationship between two continuous variables (usage frequency and coverage score) across eight observations. The sample size of eight is small, and the non-significant p-value (p = 0.088) is interpreted accordingly as a directional finding rather than a definitive test. This interpretation is consistent with the guidance in Field (2018) that Pearson correlation with n < 10 should be reported with the caveat that statistical power is limited and effect size (r = 0.639) carries more inferential weight than the p-value alone.

The chi-square goodness-of-fit test is the standard method for testing whether an observed distribution differs from an expected distribution (Field, 2018). Its application here — comparing observed benchmark counts per capability against expected counts proportional to usage frequency — is a direct operationalisation of the coverage gap hypothesis. The Cramér's V effect size (0.30, 95% CI [0.20, 0.53]) indicates a medium effect, providing confidence that the distributional mismatch is substantively meaningful and not a numerical artefact of the specific formula parameters.

The temporal regression models use only six data points (2020–2025), making their slopes descriptive rather than confirmatory. This limitation is acknowledged in Section 5.2.3 and in the statistical analysis report. The slopes are used to identify directional signals in benchmark investment trends, not to forecast future publication rates, and their interpretation remains within the scope appropriate to the available data.

---

### 5.1.6 Evaluation Against Original Objectives

Table 5.1 presents a structured mapping of each research objective against the evidence that the framework meets it, drawing on both the Phase outputs and the literature corroboration reported above.

### Table 5.1: Evaluation of Research Objectives Against Evidence

| Objective | Description | Evidence of Achievement | Literature Corroboration |
| --------- | ----------- | ----------------------- | ------------------------ |
| O1 | Build empirically grounded capability taxonomy | 8-capability taxonomy; 100% coverage of AEI top 103 tasks; κ = 1.000 | Convergence with Ouyang et al. (2025) and Handa et al. (2025) cross-platform findings |
| O2 | Compile standardised benchmark inventory (15–20) | 28 benchmarks; 100% field completion; all five quality dimensions rated with justification | Consistent with Baan et al. (2025) finding of systemic benchmark quality variation |
| O3 | Map benchmarks to capabilities via coverage matrix | 8×28 matrix; 50 non-zero cells with written justifications | Quality ratings corroborated by independent findings on MMLU, HumanEval, LiveCodeBench |
| O4 | Quantify gaps using usage-weighted scores | Gap scores for all 8 capabilities; chi-square confirms distributional mismatch (p < 0.001) | Qian et al. (2026) corroborate quality variation by domain; Handa et al. (2025) corroborate C05 gap |
| O5 | Conduct qualitative deep-dive and case analysis | 4 deep-dive analyses; 6 case studies from the literature | Singh et al. (2025), Jain et al. (2024), Xu et al. (2025) provide independent evidence for each case |
| O6 | Validate framework | Literature-based validation; convergence with Baan et al. (2025), Burnham et al. (2025), Qian et al. (2026) | — |
| O7 | Produce 3–5 benchmark design specifications | 5 benchmark specifications produced targeting top gap capabilities | Design patterns grounded in existing benchmark literature |
| O8 | Build Assessment Toolkit | Excel workbook (7 tabs) + PDF documentation; pilot-tested (see Section 5.2) | — |

---

## 5.2 Assessment Toolkit Pilot Testing

### 5.2.1 Pilot Design

The Assessment Toolkit produced in Phase 5 (`outputs/phase5/assessment_toolkit.xlsx` and `outputs/phase5/assessment_toolkit_documentation.pdf`) was pilot-tested with two non-expert colleagues prior to finalisation. The pilot aimed to test whether the toolkit was usable by practitioners without specialist knowledge of LLM evaluation, and whether the instructions, worked examples, and formula-driven components were sufficient for independent use.

Both participants were postgraduate students outside the field of machine learning or NLP — one in business analytics and one in software engineering — providing a realistic proxy for the practitioner audience of AI-team leads and product managers described in the Phase 5 toolkit documentation. Neither participant was briefed on the research project beyond being told that the toolkit was designed to help teams choose appropriate LLM benchmarks for their use case.

Each participant was given the toolkit documentation PDF and the Excel workbook and asked to complete a use-case scenario independently, without assistance from the researcher. The scenario specified a fictional organisation evaluating LLMs for a customer support application that required document review, question answering, and report summarisation. Participants were asked to: (1) identify the relevant capabilities using the Capability\_Checklist tab; (2) enter their capability priority weights in the Coverage\_Calculator tab; (3) read the resulting weighted coverage score; and (4) use the Interpretation\_Guide tab to determine what action the score recommended. Feedback was collected via a brief written questionnaire asking participants to identify any steps that were unclear, any errors or unexpected results, and any improvements they would suggest.

### 5.2.2 Pilot Findings

Both participants successfully completed the full use-case scenario without assistance. Neither made an error in entering weights or interpreting results. The time taken to complete the scenario was approximately 18 minutes for participant A and 23 minutes for participant B, both within the target range of 15–25 minutes indicated in the documentation.

Participant A identified one usability issue: the dropdown labels in the Capability\_Checklist tab used formal taxonomy names (e.g., "Review and Feedback") without a brief plain-English description of what each capability covers. They noted that they were unsure whether "document review" in the scenario corresponded to C05 or to C03. This issue was addressed by adding a one-line plain-English description to each dropdown option in the final workbook, and by expanding the Capability\_Checklist worked example to show how to classify borderline tasks.

Participant B noted that the Coverage\_Calculator tab did not flag when the entered priority weights summed to more than 1.0, which could lead to a weighted coverage score greater than 1.0 and cause confusion. A validation formula was added to the final workbook to alert the user when weights exceed the valid range and to normalise them automatically if they do.

No errors were found in the underlying formulas. Both participants rated the toolkit as "easy to use" or "somewhat easy to use" on the questionnaire, and both indicated that they would use such a tool in a professional context. No changes were made to the framework logic, capability definitions, or benchmark profile data as a result of the pilot; the revisions were confined to usability and validation improvements within the Excel workbook.

### 5.2.3 Limitations of the Evaluation

Several limitations of both the literature-based validation and the toolkit pilot test should be acknowledged.

**Literature-based validation scope.** The validation approach relies on published sources that were, in most cases, themselves drawn upon in the construction of the framework. While convergence with these sources demonstrates internal consistency, it does not rule out shared blind spots. If the LLM evaluation literature as a whole underweights a particular usage pattern — for example, low-resource language use or highly specialised professional domains — then the taxonomy, the benchmark inventory, and the validating literature would all exhibit the same gap.

**Small pilot sample.** The toolkit pilot was conducted with two participants, both postgraduate students. This is the minimum specified in the project design and is sufficient to identify usability errors, but it is insufficient to establish the external validity of the usability findings. The two participants may not be representative of the practitioner audience in terms of prior familiarity with benchmark concepts, tolerance for technical language, or use-case diversity. A larger and more diverse pilot would be required before the toolkit could be recommended for deployment in professional evaluation contexts without additional adaptation.

**Absence of direct expert rating.** Without a structured expert survey, it is not possible to report Fleiss' κ across expert raters, or to quantify inter-expert agreement on the taxonomy or gap rankings. The literature-based validation provides convergent validity but not the discriminant validity evidence that expert disagreement data would supply. Specifically, it is not known whether domain experts in areas such as NLP evaluation or AI policy would rate the taxonomy boundaries differently, or whether they would endorse the gap prioritisation as it stands.

**Single-provider usage data.** The usage frequency weights used in the gap score formula are derived primarily from the Anthropic AEI dataset. While cross-platform corroboration from Ouyang et al. (2025) and the OpenRouter study increases confidence, the weights still reflect usage patterns for a specific class of models and deployment contexts. Usage frequencies may differ systematically for open-source models, enterprise deployments, or non-English-language contexts — and these differences would alter the gap score rankings if they were large enough.

**Temporal limitations of coverage data.** The benchmark inventory reflects the state of published benchmarks as of the data collection period (2020–2025). New benchmarks addressing current gaps may have been published between data collection and thesis submission, and the coverage matrix would require updating to reflect them. The toolkit's Coverage\_Calculator tab was designed with this limitation in mind — the Interpretation\_Guide advises users to verify that the embedded benchmark profile data is current before relying on the weighted scores.

Despite these limitations, the convergence between the project's findings and a broad base of independently conducted research provides reasonable confidence that the taxonomy categories, benchmark quality ratings, and gap rankings reflect genuine patterns in the LLM evaluation landscape rather than idiosyncrasies of the methodology used here. The limitations point toward directions for future work, which are elaborated in Chapter 7.

---

## References

Alaa, A., Hartvigsen, T., Golchini, N., Dutta, S., Dean, F., Raji, I. D. and Zack, T. (2025). Medical large language model benchmarks should prioritize construct validity. arXiv:2503.10694.

Baan, J., Giulianelli, M., Kuribayashi, T., Linzen, T., Röttger, P., Shwartz, V., White, B., Zhu, W. and Fokkens, A. (2025). Measuring what matters: Construct validity in large language model benchmarks. arXiv:2511.04703.

Balloccu, S., Schmidtová, P., Lango, M. and Dušek, O. (2024). Leak, cheat, repeat: Data contamination and evaluation malpractices in closed-source LLMs. In *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2024)*, pp. 67–93.

Braun, V. and Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), pp. 77–101. [https://doi.org/10.1191/1478088706qp063oa](https://doi.org/10.1191/1478088706qp063oa)

Field, A. (2018). *Discovering Statistics Using IBM SPSS Statistics* (5th ed.). SAGE.

Gao, Z., Treude, C. and Rashid, A. (2025). Large language models in thematic analysis: Prompt engineering, evaluation, and guidelines for qualitative software engineering research. arXiv:2510.18456.

Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Henighan, T., Joseph, N., Kinniment, M., Kundu, S., McCain, J., Perez, E., Schiefer, N., Shoker, S., Sleight, H., Teplitskiy, M., Wijk, H., Clark, J., Kaplan, J., Ganguli, D. and Anthropic (2025). Which economic tasks are performed with AI? Evidence from millions of Claude conversations. arXiv:2503.04761.

Jain, N., Han, K., Gu, A., Li, W., Yan, F., Zhang, T., Wang, S., Solar-Lezama, A., Sen, K. and Stoica, I. (2024). LiveCodeBench: Holistic and contamination free evaluation of large language models for code. arXiv:2403.07974.

Kanjee, Z., Crowe, B. and Rodman, A. (2023). Accuracy of a generative artificial intelligence model in a complex clinical case. *JAMA*, 330(1), pp. 78–80. [https://doi.org/10.1001/jama.2023.8288](https://doi.org/10.1001/jama.2023.8288)

Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D. and Ho, D. E. (2024). Hallucination-free? Assessing the reliability of leading AI legal research tools. arXiv:2405.20362.

Ouyang, S., Shi, W., Zheng, R., Xu, J., Cai, Y., Wei, J., Fu, J., Ji, Y., Yin, D. and Zheng, R. (2025). *How are large language models used? Evidence from millions of OpenAI API requests* (NBER Working Paper 34255). National Bureau of Economic Research.

Petticrew, M. and Roberts, H. (2006). *Systematic Reviews in the Social Sciences: A Practical Guide*. Blackwell.

Pezeshkpour, P. and Hruschka, E. (2023). Large language models sensitivity to the order of options in multiple-choice questions. *Findings of the Association for Computational Linguistics: NAACL 2024*, pp. 2006–2017.

Qian, Q., Huang, C., Huang, J., Wang, W. and Liu, Q. (2026). Benchmark²: Systematic evaluation of LLM benchmarks. arXiv:2601.03986.

Singh, S., Stroebl, A., Kambhampati, S., Kapoor, S., Narayanan, A., Ghassemi, M. and Bommasani, R. (2025). The leaderboard illusion. arXiv:2504.20879.

Xu, F. F., Ye, Y., Arenas, O., Yao, S. and Neubig, G. et al. (2025). TheAgentCompany: Benchmarking LLM agents on consequential real world tasks. arXiv:2412.14161.
