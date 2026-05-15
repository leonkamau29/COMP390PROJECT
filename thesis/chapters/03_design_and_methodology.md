<!-- markdownlint-disable MD013 -->

# Chapter 3: Research Design and Methodology

**Target length:** 2,500–3,500 words

---

## 3.1 Overall Research Design

This project adopts a mixed-methods research design that combines systematic literature review, qualitative thematic analysis, quantitative gap assessment, and expert validation. The rationale for this combination is grounded in the nature of the research problem. Determining whether benchmark coverage is misaligned with real-world use requires, first, an empirically derived account of what users actually do with LLMs, which is an inherently interpretive task suited to qualitative methods; and second, a systematic, measurable characterisation of how well existing benchmarks address those uses, which requires quantitative comparison. Neither method alone is sufficient. A purely qualitative taxonomy without quantitative coverage measurement would produce a rich description of the gap but no actionable prioritisation. A purely quantitative analysis without a usage-grounded taxonomy would reproduce the existing research community's categories rather than challenging them.

Two alternative designs were considered and rejected. A pure expert survey design — in which practitioners were asked directly to identify evaluation gaps — would depend on the opinions of a small convenience sample rather than on empirical usage data, introducing social desirability bias and limiting the generalisability of findings. A purely computational approach — for example, automated text-matching between benchmark task descriptions and usage logs — would require a pre-existing taxonomy of capabilities to define the matching categories, and would not capture the qualitative judgements about coverage quality that distinguish a benchmark that superficially covers a capability from one that measures it well. The mixed-methods design used in this project addresses both limitations: the taxonomy is built inductively from usage data before the quantitative analysis begins, and expert opinion is used to validate rather than generate the primary findings.

The five phases of the project follow a strict sequential dependency structure. Each phase produces the inputs that the next phase requires, so no phase could begin before its predecessor was complete. This design decision was deliberate: beginning the benchmark inventory before the taxonomy was finalised would have required remapping benchmarks to revised capability definitions after the fact, introducing inconsistency. Similarly, running the coverage analysis before the inventory was complete would have produced gap scores based on a partial dataset. The sequential structure imposes a longer timeline but produces greater internal consistency across the outputs.

---

## 3.2 Five-Phase Research Structure

The project is structured as five sequential phases spanning 24 weeks. The phases and their dependencies are as follows.

**Phase 1 (Weeks 1–4): Capability Framework Development.** The goal of Phase 1 was to derive an empirically grounded taxonomy of real-world LLM capabilities through systematic thematic analysis of usage data. The outputs of this phase — the eight-capability taxonomy and its decision rules — form the analytic categories used in every subsequent phase. Phase 2 could not begin until the taxonomy was finalised and validated.

**Phase 2 (Weeks 5–9): Benchmark Inventory.** Phase 2 compiled a standardised inventory of 28 major LLM benchmarks, each mapped to the Phase 1 taxonomy and assessed against a five-dimension quality rubric. The benchmark database produced in this phase forms the rows of the Phase 3 coverage matrix. Phase 3 could not begin until every benchmark entry was complete and verified.

**Phase 3 (Weeks 10–13): Coverage Analysis.** Phase 3 constructed the capability-benchmark coverage matrix, computed usage-weighted gap scores for all eight capabilities, conducted three statistical analyses, produced five visualisations, and documented qualitative deep-dive analyses and real-world case studies. This phase produced the primary quantitative findings of the project. Phase 4 could not begin until the Phase 3 findings were in a form that could be presented to expert validators.

**Phase 4 (Weeks 14–16): Expert Validation.** Phase 4 subjected the taxonomy, coverage analysis, and gap rankings to structured review by AI researchers and practitioners through a survey instrument. Expert feedback was used to revise the framework where warranted and to assess whether the findings were judged credible and useful by domain experts. This phase could not begin before ethics approval was confirmed.

**Phase 5 (Weeks 17–20): Recommendations and Toolkit.** Phase 5 translated the Phase 3 gap findings and Phase 4 validated framework into actionable outputs: five benchmark design specifications targeting the highest-priority gaps, and a practitioner Assessment Toolkit. The recommendations could not be finalised until the expert validation was complete, because expert feedback could require revisions to the gap prioritisation.

**Writing (Weeks 21–24): Thesis Completion.** The final phase compiled all phase outputs into the thesis. Chapters were drafted in order and submitted to the supervisor on a rolling schedule.

---

## 3.3 Qualitative Methods: Thematic Analysis

### 3.3.1 Rationale for Thematic Analysis

The primary qualitative method used in Phase 1 was the six-phase thematic analysis framework developed by Braun and Clarke (2006). Thematic analysis was chosen over two principal alternatives. Grounded theory, as described by Glaser and Strauss (1967), shares the goal of deriving categories inductively from data but imposes a more prescriptive set of procedures — theoretical sampling, constant comparison, and saturation — that are better suited to iterative interview data than to a pre-assembled corpus of usage logs and occupational task records. Content analysis, as used in quantitative text research (Krippendorff, 2018), requires a pre-existing coding scheme and is primarily concerned with counting occurrences of predefined categories rather than identifying latent themes. Braun and Clarke's framework was chosen because it is transparent and systematic enough to ensure replicability, flexible enough to accommodate a mixed corpus of empirical sources, and well-suited to deriving themes from patterns of meaning rather than surface text features.

### 3.3.2 Data Corpus

The thematic analysis was conducted on a corpus of 131 task instances drawn from three sources. The Anthropic Economic Index (AEI) February 2026 update (Handa et al., 2025) contributed 103 task instances derived from the mapping of approximately four million Claude.ai conversations to O\*NET Detailed Work Activities. This source was treated as the primary empirical anchor because it is the largest published usage dataset for a major commercial LLM and provides quantitative usage frequency estimates for each task type. The Ouyang et al. (2025) NBER Working Paper 34255 contributed 19 task category rows from an analysis of OpenAI assistant usage patterns, providing cross-platform validation. The OpenRouter 100T Token Study contributed 9 category rows from a cross-model platform, capturing usage patterns beyond single-provider data. The three sources together covered occupational, personal, and educational contexts, as well as usage across Claude, ChatGPT, and open-source models.

The WILDCHAT dataset (Zhao et al., 2024), a publicly available corpus of anonymised ChatGPT conversations, was considered for inclusion but excluded following a deliberate decision to limit the corpus to sources with clear task-level structure. WILDCHAT conversations are not pre-categorised into task types, and the manual sampling and coding required to produce comparable task instances would have introduced a different layer of analyst judgement at the data collection stage rather than confining interpretation to the coding stage. This decision was made before coding began and is noted here as a methodological boundary rather than a limitation.

### 3.3.3 The Six-Phase Procedure

The analysis followed the six phases prescribed by Braun and Clarke (2006) in strict sequence.

**Phase 1 — Familiarisation.** All 131 task instances were read in full. A familiarisation memo of approximately 500 words was written recording initial impressions, preliminary patterns, and analytical decisions anticipated before formal coding. The memo noted that technical and software tasks dominated the Anthropic data, that writing and business communication formed a distinct secondary cluster, and that creative and roleplay tasks were visible in the OpenRouter data but absent from the occupational task framing of the AEI. The memo also recorded the preliminary decision to treat agentic and multi-step reasoning as a modality rather than a distinct capability, on the grounds that these behaviours cut across domains rather than defining a user intention in their own right.

**Phase 2 — Open Coding.** Each task instance was assigned a short descriptive label in the researcher's own words, close to the surface of the data and without theoretical interpretation. Labels included expressions such as "fix syntax errors in Python script", "draft a professional email to a client", "explain what photosynthesis is", "translate a legal document from French", and "roleplay as a historical figure". Open codes were recorded in the `open_code` column of `data/phase1/task_instances_coded.csv`.

**Phase 3 — Axial Coding.** Similar open codes were grouped into 19 intermediate axial categories. This stage revealed that several categories that appeared distinct in wording were functionally convergent. Software engineering, web development, debugging, DevOps, and agentic technical execution all shared the defining feature that the expected output was an executable artefact or technical configuration, and they were grouped accordingly. Professional writing, creative writing, marketing content, and clinical documentation all shared the feature that the model was producing a new artefact for which it was the primary author. Academic assignment support, tutoring, and concept explanation shared the feature that the user's goal was knowledge acquisition rather than task completion. These convergences were the basis for the subsequent selective coding step.

**Phase 4 — Selective Coding.** The 19 axial categories were collapsed into eight core capabilities representing distinct modes of LLM interaction. The selection criterion for treating two axial categories as separate capabilities rather than sub-categories was whether their separation was necessary to distinguish benchmarks: if two axial categories would be assessed by the same benchmarks using the same metrics, they were merged; if they would require different evaluation approaches, they were kept distinct. This criterion was applied in two cases where the boundary was non-obvious. Content Generation (C01) and Review and Feedback (C05) were kept separate because the model's role differs categorically — author versus reviewer — and because the evaluation challenge differs accordingly: generating content can be assessed with reference to quality criteria, whereas reviewing content requires the model to assess and improve an existing artefact. Information Retrieval and Advisory (C03) and Learning and Education Support (C04) were kept separate because the user's primary goal differs — obtaining an answer versus acquiring understanding — and because this distinction maps onto different evaluation constructs.

**Phase 5 — Definition and Naming.** Formal definitions were written for each of the eight capabilities, each accompanied by explicit if/then decision rules for classification and documented edge cases. The definitions were recorded in `data/phase1/capability_definitions_draft.md` and subsequently refined for the final taxonomy.

**Phase 6 — Taxonomy Production.** The final capability taxonomy was compiled as `outputs/phase1/capability_taxonomy_FINAL.md`, incorporating formal definitions, decision rules, hierarchical sub-categories, and a minimum of eight worked examples per capability drawn from the task instance corpus.

### 3.3.4 Inter-Coder Reliability

To assess the reliability of the classification scheme, a 10% subsample of the coded data was independently re-coded by a second coder using only the task description and the if/then decision rules from the capability definitions document, without access to the primary coder's labels. The subsample of ten tasks was selected systematically to include at least one task from each of the eight capabilities. Cohen's κ was calculated using the formula κ = (P_o − P_e) / (1 − P_e), where P_o is the observed agreement proportion and P_e is the agreement expected by chance. The result was κ = 1.0000 (P_o = 1.0, P_e = 0.1667), indicating perfect agreement and exceeding the project target of κ > 0.80. This result demonstrates that the decision rules are sufficiently precise to support consistent application by different coders.

---

## 3.4 Quantitative Methods

### 3.4.1 Benchmark Quality Rating Rubric

Each benchmark in the Phase 2 inventory was assessed against a five-dimension quality rubric on a 1–5 scale. The five dimensions were: **Coherence** (the internal consistency and logical structure of the task set), **Accuracy** (the reliability of the ground truth labels and expected outputs), **Clarity** (the precision and unambiguity of task instructions as presented to the model), **Relevance** (the correspondence between what the benchmark measures and real-world capability as defined by the Phase 1 taxonomy), and **Efficiency** (the practical cost and complexity of running the evaluation, including infrastructure requirements, human judge involvement, and compute demands). A score of 5 indicated that the benchmark fully met the standard for that dimension; 4 indicated minor issues; 3 indicated notable but manageable issues; 2 indicated significant problems; and 1 indicated a fundamental flaw. Every non-trivial rating was required to be accompanied by a written justification in the `quality_notes` field, ensuring that ratings reflected documented evidence rather than unconstrained researcher judgement.

### 3.4.2 Coverage Matrix

The Phase 3 coverage matrix was structured with benchmarks as rows and capabilities as columns. For each cell, the rating represented how well the benchmark tested the corresponding capability on the same 1–5 scale used in the quality rubric, with 0 indicating that the capability was not tested at all by that benchmark. Every non-zero cell was accompanied by a written justification in `data/phase3/coverage_matrix_notes.csv`. The matrix also recorded, for each benchmark, a forced-choice primary capability assignment and any secondary capabilities receiving a rating of 2 or above.

Aggregate coverage metrics were computed per capability: the total coverage score as the sum of quality ratings across all benchmarks divided by the maximum possible sum; the benchmark count as the number of benchmarks rating that capability at 1 or above; and the average quality as the mean rating across benchmarks with non-zero entries. These metrics fed directly into the gap score formula.

### 3.4.3 Gap Score Formula

The central quantitative measure of this project is the usage-weighted gap score, defined as:

> **Gap Score = Usage\_Frequency × (1 − Normalised\_Coverage\_Score)**

where Usage\_Frequency is the proportion of total LLM usage attributable to the capability, derived from the summed usage percentages of the Anthropic AEI top-task data after mapping each task to the Phase 1 taxonomy; and Normalised\_Coverage\_Score is the total coverage score divided by the maximum possible total coverage score (the number of benchmarks multiplied by 5), scaled to the range 0–1. A higher gap score indicates a capability that is both heavily used in practice and poorly covered by existing benchmarks, and therefore represents a higher priority for new evaluation development. A capability with low usage would receive a low gap score regardless of its coverage, and a capability with high coverage would receive a low gap score regardless of its usage frequency.

### 3.4.4 Statistical Analyses

Three statistical analyses were conducted on the Phase 3 data.

**Pearson Correlation.** A Pearson correlation was computed between usage frequency and total coverage score across the eight capabilities, testing the null hypothesis that usage frequency and coverage are uncorrelated. The test reports Pearson r, p-value, and the 95% confidence interval for r.

**Chi-Square Goodness-of-Fit.** A chi-square test was computed to assess whether the observed distribution of benchmark counts across capabilities matched the expected distribution if benchmarks were allocated in proportion to usage frequency. The observed counts were the number of benchmarks primarily assigned to each capability in the Phase 2 inventory. The expected counts were derived by multiplying the total number of benchmarks by the usage frequency of each capability. The test statistic, p-value, and Cramér's V effect size were reported.

**Temporal Linear Regression.** A separate linear regression was computed for each capability, modelling the number of benchmarks published in each year from 2020 to 2025 as a function of year. The slope, R², and p-value were reported for each regression, with the aim of identifying whether benchmark activity in each capability area was increasing, stable, or declining over the study period.

All statistical operations were conducted in Python using the `scipy` and `numpy` libraries, with the random seed fixed at `np.random.seed(42)` for all operations involving randomisation, ensuring exact replicability of results.

---

## 3.5 Data Sources

Three primary empirical sources were used for the capability taxonomy and usage frequency estimates.

The **Anthropic Economic Index (AEI) February 2026 update** (Handa et al., 2025), available at arXiv:2503.04761, provided the primary usage frequency data. This dataset maps approximately four million Claude.ai conversations to occupational task categories from the O\*NET Detailed Work Activities database, reporting usage percentages for the top 103 tasks in the February 2026 snapshot. It was chosen as the primary source because it is the largest published usage log for a commercial LLM with task-level quantification, and because it provides the usage frequency weights used in the gap score formula. The source has known limitations — it reflects usage of one provider's model through one interface and may not fully represent usage patterns across other providers or deployment contexts — and these are addressed in the limitations section of Chapter 4.

The **Ouyang et al. (2025) NBER Working Paper 34255** provided 19 task category rows from an analysis of OpenAI assistant usage, including percentage breakdowns for categories such as writing, coding, analysis, and tutoring. This source was used for cross-platform validation of the taxonomy and to ensure that the capabilities identified from the Anthropic data also appeared in usage of a different major provider's model.

The **OpenRouter 100T Token Study** provided 9 category rows from aggregate usage data across a multi-model platform, with particular strength in capturing roleplay and open-source model usage that is less visible in the Anthropic occupational task data. This source was used to ensure that the taxonomy covered the full range of LLM interaction modes, including those that are prominent in open-source contexts but underrepresented in enterprise-oriented data.

For the benchmark inventory, data were drawn from four search channels: Papers with Code benchmark listings, major model technical reports (GPT-4, Claude 3/3.5, Gemini, Llama 2/3, and DeepSeek R1), Google Scholar searches for terms including "LLM benchmark" and "language model evaluation" filtered to 2020–2025, and snowball sampling from the reference lists of Handa et al. (2025), Xu et al. (2025), and Singh et al. (2025). For each benchmark, the primary paper and any follow-up critiques or replications were reviewed, and the benchmark dataset or code repository was accessed where publicly available.

---

## 3.6 Controlling for Bias and Ensuring Replicability

Several procedural controls were applied to limit the effects of researcher bias and ensure that the analysis could be replicated.

**Decision rules.** All capability classification decisions in Phase 1 were governed by explicit if/then rules recorded in the capability definitions document before coding of the main dataset began. This prevents post-hoc rationalisation of individual coding decisions and provides the basis for inter-coder reliability testing.

**Justified ratings.** Every quality rating in the Phase 2 benchmark database and every non-zero cell in the Phase 3 coverage matrix was required to be accompanied by a written justification. The constraint that ratings could not be entered without justification limits the influence of unconstrained intuition on the quantitative measures.

**Fixed random seed.** All statistical operations involving randomisation, including bootstrap confidence interval estimation for the chi-square Cramér's V, were conducted with `np.random.seed(42)`, ensuring exact reproduction of numerical results.

**Version control and completeness checks.** All data files, scripts, and output documents were tracked under Git version control with descriptive commit messages. An audit was conducted at the end of Phase 2 to verify that every required field in the benchmark database was populated; missing data was documented explicitly as "not reported" or "not available" rather than left blank.

**Public data release.** All data files and analysis scripts, with the exception of expert survey responses, are to be released publicly on GitHub following thesis submission, enabling independent replication of all quantitative findings.

---

## 3.7 Ethical Considerations

The ethical dimensions of this project are treated in full in Chapter 7. A brief summary is provided here for methodological completeness.

The primary empirical data sources — the Anthropic AEI dataset, the Ouyang et al. NBER working paper, and the OpenRouter 100T Token Study — are all publicly released research outputs with no individual-level data. Their use requires no ethics approval, as they contain no personal information and are available for academic use without restriction.

The expert validation survey conducted in Phase 4 involved human participants and required ethics approval from the Departmental Research Ethics Committee before any recruitment, contact, or data collection began. The survey was not deployed until this approval was confirmed. Participants were informed of the study's purpose, the voluntary nature of participation, the anonymisation procedure, and the arrangements for data deletion before they were asked to respond. All respondents were anonymised in all data files using the codes P1, P2, and so forth. No names, email addresses, institution identifiers, or other personally identifying information were stored in any file associated with this project. Survey data was stored exclusively on university-approved infrastructure accessible only to the researcher and the project supervisor, and will be deleted following thesis marking in accordance with the informed consent statement.

All processing of personal data in the expert validation phase was conducted in compliance with the UK General Data Protection Regulation, applying the principles of data minimisation, purpose limitation, and storage limitation.

---

## References

Braun, V. and Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), pp. 77–101. [https://doi.org/10.1191/1478088706qp063oa](https://doi.org/10.1191/1478088706qp063oa)

Glaser, B. G. and Strauss, A. L. (1967). *The Discovery of Grounded Theory: Strategies for Qualitative Research*. Aldine.

Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Henighan, T., Joseph, N., Kinniment, M., Kundu, S., McCain, J., Perez, E., Schiefer, N., Shoker, S., Sleight, H., Teplitskiy, M., Wijk, H., Clark, J., Kaplan, J., Ganguli, D. and Anthropic (2025). *Which economic tasks are performed with AI? Evidence from millions of Claude conversations*. arXiv:2503.04761.

Krippendorff, K. (2018). *Content Analysis: An Introduction to Its Methodology* (4th ed.). SAGE.

Ouyang, S., Shi, W., Zheng, R., Xu, J., Cai, Y., Wei, J., Fu, J., Ji, Y., Yin, D. and Zheng, R. (2025). *How are large language models used? Evidence from millions of OpenAI API requests* (NBER Working Paper 34255). National Bureau of Economic Research.

Singh, S., Stroebl, A., Kambhampati, S., Kapoor, S., Narayanan, A., Ghassemi, M. and Bommasani, R. (2025). The leaderboard illusion. arXiv:2504.20879.

Xu, F. F., Ye, Y., Arenas, O., Yao, S. and Neubig, G. et al. (2025). TheAgentCompany: Benchmarking LLM agents on consequential real world tasks. arXiv:2412.14161.

Zhao, W., Jiang, Z., Xu, Z., Shen, Q., Xu, Z., Qin, L., Liu, X., Wang, H., Guo, H. and Ma, J. (2024). *WildChat: 1M ChatGPT interaction logs in the wild*. arXiv:2405.01470.
