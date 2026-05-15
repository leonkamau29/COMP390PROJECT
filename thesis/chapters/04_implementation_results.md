<!-- markdownlint-disable MD013 -->

# Chapter 4: Implementation and Results

**Target length:** 9,000–13,000 words (combines Phases 1–3 results; longest chapter)

---

> **Note on structure:** This chapter presents the results of the three core analytical phases: the capability taxonomy development (Phase 1), the benchmark inventory (Phase 2), and the coverage analysis, gap quantification, statistical testing, qualitative deep dives, and case studies (Phase 3). Phases 4 and 5 are presented in Chapters 5 and 6 respectively.

---

## 4.1 Phase 1 — Capability Taxonomy Development

### 4.1.1 Data Collection and Task Instance Extraction

The Phase 1 capability taxonomy was developed through systematic thematic analysis of a corpus of 131 task instances drawn from three primary empirical sources. The sources were selected to provide coverage across commercial enterprise usage, consumer commercial usage, and open-source model usage, ensuring that the resulting taxonomy reflected a broad range of LLM interaction patterns rather than those associated with any single platform or user population.

The primary source was the Anthropic Economic Index (AEI) February 2026 update (Handa et al., 2025), which contributed 103 task instances corresponding to the 103 task categories identified from approximately four million Claude.ai conversations mapped to Occupational Information Network (O\*NET) Detailed Work Activities. Each AEI task instance was accompanied by a usage percentage indicating the proportion of recorded interactions that involved that task type, making this source the primary anchor for quantitative usage frequency weights in the later gap score analysis. The AEI was treated as the primary source because it is the largest published usage dataset for a commercial LLM with task-level quantification and because its O\*NET mapping provides a principled connection to an established occupational taxonomy.

The second source was Ouyang et al. (2025), an NBER Working Paper reporting an analysis of OpenAI platform usage patterns across millions of API requests. This source contributed 19 task category rows covering writing, coding, analysis, tutoring, and conversational interaction. Its inclusion served two purposes: cross-platform validation of the task categories visible in the Anthropic data, and the introduction of task patterns characteristic of API-oriented developer usage that may be underrepresented in the consumer-facing AEI conversations.

The third source was the OpenRouter 100T Token Study, which contributed nine category rows drawn from aggregate usage data across a multi-model platform serving both commercial and open-source model traffic. This source was particularly important for capturing roleplay, creative fiction, and open-ended conversational interaction, which account for a disproportionately large share of token consumption in open-source contexts but appear less prominently in occupationally framed usage logs.

All 131 task instances were structured in a standardised spreadsheet with fields recording the source citation, task description, preliminary domain classification, usage frequency where reported, interaction context, and source type. The WILDCHAT dataset (Zhao et al., 2024), a publicly available corpus of anonymised ChatGPT conversations, was considered for inclusion but excluded on methodological grounds. WILDCHAT conversations are not pre-categorised into task types, and the sampling and manual coding required to extract comparable task instances would have introduced a different layer of analyst interpretation at the data collection stage rather than at the coding stage. This exclusion was documented as a deliberate methodological boundary before coding began and is noted in Chapter 3.

### 4.1.2 Thematic Analysis Procedure

The thematic analysis followed the six-phase framework of Braun and Clarke (2006) in strict sequence, as described in detail in Chapter 3. This section reports the outcomes of each phase as they applied to the 131-task corpus.

**Familiarisation** produced a memo noting that the Anthropic data was dominated by technical and software-development tasks, that professional writing and business communication formed a visible secondary cluster, and that creative and conversational interaction tasks were visible in the OpenRouter data but absent from the occupationally framed AEI categories. The memo recorded the preliminary analytical decision to treat agentic and multi-step reasoning as a modality of task execution rather than a distinct capability, on the grounds that agentic behaviour cuts across domains — an agent might perform a coding task, an information retrieval task, or a data analysis task — rather than defining a distinct user intention.

**Open coding** assigned a short descriptive label to each of the 131 task instances in the researcher's own words, without theoretical interpretation. Labels captured what the user was asking the model to do at the level of observable activity: "fix syntax errors in Python script", "draft a professional email to a client", "explain photosynthesis for a student", "translate a legal document from French to English", and "provide relationship advice in a sustained dialogue".

**Axial coding** grouped the 131 open codes into 19 intermediate categories. This stage revealed several convergences that were non-obvious from the surface labels. Software engineering, web development, debugging, DevOps, and agentic technical execution all shared the defining characteristic that the expected output was an executable artefact or technical configuration; they were grouped into a single technical problem-solving category. Professional writing, creative writing, marketing content, and clinical documentation shared the characteristic that the model was the primary author producing a new written artefact; they were grouped into a single content generation category. Academic assignment support, tutoring, and concept explanation shared the characteristic that the user's goal was knowledge acquisition rather than task completion; they were grouped into a single educational support category. These convergences informed the subsequent selective coding decisions.

**Selective coding** collapsed the 19 axial categories into eight core capabilities using the criterion that two axial categories should remain distinct if they would require different evaluation approaches — that is, if they would be assessed by different benchmarks using different metrics. This criterion was applied most carefully in two cases. Content Generation (C01) and Review and Feedback (C05) were kept separate because the model's role differs categorically: as author in C01 and as reviewer or editor in C05. The evaluation challenge differs accordingly, since generating content can be assessed with reference to quality criteria applied to a new artefact, whereas reviewing content requires the model to assess and improve a user-supplied artefact against standards of accuracy, clarity, and improvement. Information Retrieval and Advisory (C03) and Learning and Education Support (C04) were kept separate because the user's primary goal differs: obtaining a complete answer in C03 versus acquiring understanding through guided engagement in C04.

**Definition and naming** produced formal two-to-four-sentence definitions for each of the eight capabilities, each accompanied by explicit if/then decision rules for resolving classification ambiguities. These definitions and rules were recorded before validation and formed the basis for the inter-coder reliability assessment.

**Taxonomy production** compiled the final taxonomy document, incorporating formal definitions, hierarchical sub-category structures, decision rules, worked examples, and edge case resolutions.

### 4.1.3 The Eight-Capability Taxonomy

The Phase 1 analysis produced a taxonomy of eight core capabilities, identified as C01 through C08, that together account for all documented patterns of real-world LLM use in the source corpus. The capabilities and their formal definitions are as follows.

**C01 — Content Generation** is the capability to produce original, purposeful written or multimedia text artefacts in response to a user's creative, professional, or communicative goal. The model acts as author or co-author, generating content that serves the user's intended audience and context. Sub-categories include academic and educational writing (C01a), professional and business writing (C01b), marketing and promotional writing (C01c), creative writing (C01d), and technical and specialised writing (C01e).

**C02 — Code Development and Technical Problem Solving** is the capability to write, debug, refactor, and maintain software code; to design and implement technical systems; and to diagnose and resolve technical failures in software, hardware, and networked infrastructure. Sub-categories include web application development (C02a), software engineering and systems (C02b), code debugging and refactoring (C02c), machine learning and AI development (C02d), DevOps and infrastructure (C02e), and technical troubleshooting (C02f).

**C03 — Information Retrieval and Advisory** is the capability to locate, synthesise, and deliver factual information, evidence-based recommendations, or domain-specific advisory guidance in response to a user's question or decision-making need. Sub-categories include factual and encyclopaedic information (C03a), product and service recommendations (C03b), career, financial, and personal advisory (C03c), research synthesis and literature overview (C03d), and practical how-to guidance (C03e).

**C04 — Learning and Education Support** is the capability to assist users in acquiring knowledge, skills, or academic qualifications through tutoring, explanation, worked examples, and structured guidance. Sub-categories include academic assignment support (C04a), concept explanation and tutoring (C04b), skill development (C04c), and educational material creation (C04d).

**C05 — Review and Feedback** is the capability to evaluate, critique, edit, and improve existing written or creative work produced by the user or a third party. The model acts as reviewer, editor, or assessor, identifying errors, weaknesses, and opportunities for improvement. Sub-categories include proofreading and grammar correction (C05a), substantive editing and content improvement (C05b), academic feedback and grading (C05c), and peer review and manuscript revision (C05d).

**C06 — Translation and Language Processing** is the capability to convert text between natural languages, assist users in learning or practising a foreign language, and perform language-specific transformations where the defining feature is a cross-lingual purpose. Sub-categories include document and text translation (C06a), language learning and grammar support (C06b), and multilingual content formatting (C06c).

**C07 — Data Analysis and Summarisation** is the capability to process, analyse, and synthesise existing datasets, documents, or information corpora to extract insights, patterns, statistical results, or compressed representations. The defining feature is that the user supplies existing data or content as the primary input. Sub-categories include text summarisation and compression (C07a), data analysis and statistical computing (C07b), document processing and format conversion (C07c), and business intelligence and forecasting (C07d).

**C08 — Conversational Interaction and Roleplay** is the capability to engage in open-ended, interactive dialogue with users for purposes of entertainment, personal support, social practice, or collaborative world-building. The defining feature is that the primary user value lies in the interactive exchange itself rather than in a discrete output artefact. Sub-categories include personal and emotional support dialogue (C08a), interactive roleplay and collaborative fiction (C08b), social and conversational practice (C08c), and entertainment and games (C08d).

A cross-capability disambiguation table accompanies the taxonomy, providing explicit resolutions for fourteen common ambiguous scenarios: for example, a user asking the model to write code maps to C02, to explain code maps to C04, and to review their code maps to C05. The disambiguation table was used in the validation phase and in the inter-coder reliability exercise.

The distribution of the 103 Anthropic AEI top tasks across the eight capabilities was as follows: C02 received 35 tasks (34.0%), C03 received 22 tasks (21.4%), C01 received 18 tasks (17.5%), C07 received 11 tasks (10.7%), C04 received 8 tasks (7.8%), C05 received 4 tasks (3.9%), C08 received 3 tasks (2.9%), and C06 received 2 tasks (1.9%).

### 4.1.4 Validation

The taxonomy was validated against two criteria: coverage of the Anthropic AEI top-task data and inter-coder reliability.

**Coverage validation.** All 103 task categories from the Anthropic AEI February 2026 top-task list were systematically mapped to the taxonomy using the formal decision rules. The mapping was recorded in `data/phase1/anthropic_top100_mapping.csv` with fields recording each task description, the mapped capability, the confidence level (high, medium, or low), and a justification. Of the 103 tasks, 99 were mapped at high confidence on first application of the decision rules. Four tasks were classified at medium confidence because they involved elements of two capabilities: for example, a task involving generating and then reviewing a professional document. These four cases were resolved through the dual-capability disambiguation procedure documented in the taxonomy, which specifies that where a task spans two capabilities, the primary user intention governs the classification. No task required the introduction of a new capability category, and no task remained unmapped. Coverage was therefore 103/103 = 100.0%, exceeding the 95% target specified in the project success criteria (Handa et al., 2025).

**Inter-coder reliability.** A 10% subsample of ten tasks from the mapped set was independently coded by a second coder using only the task description and the formal if/then decision rules, without access to the primary coder's labels. The subsample was selected to include at least one task from each of the eight capabilities. Cohen's κ was calculated using the formula κ = (P_o − P_e) / (1 − P_e), where P_o is the observed proportion of agreement and P_e is the agreement expected by chance. The result was κ = 1.0000 (P_o = 1.0, P_e = 0.1667, based on six capability categories represented in the subsample). This result indicates perfect agreement between coders and substantially exceeds the project target of κ > 0.80 (Cohen, 1960). The κ = 1.00 result reflects the precision of the if/then decision rules, which guided both coders to the same classification without ambiguity in the subsample. This should not be interpreted as evidence that the taxonomy is trivially simple: the zero disagreement rate in the subsample is consistent with the possibility of disagreements in other regions of the task space not covered by the ten sampled items. The inter-coder exercise demonstrates that the decision rules are sufficiently precise to support consistent application.

### 4.1.5 Limitations of Phase 1

Three limitations of the Phase 1 analysis are acknowledged. First, the primary coding was conducted by a single researcher, with a second coder involved only in the validation subsample. While the κ result indicates that the decision rules support consistent application, a complete dual-coding exercise across all 131 task instances would provide stronger inter-rater evidence. Second, the usage frequency weights used throughout the project are derived from a single provider's data — Anthropic's Claude.ai platform — and may not fully represent usage patterns on other platforms, particularly those serving developer, enterprise, or non-English-language populations. The Ouyang et al. (2025) and OpenRouter data are included partly to mitigate this limitation but do not provide the same depth of quantitative frequency data as the AEI. Third, the AEI data was collected at a specific point in time (February 2026), and the relative frequencies of different capability types may shift as LLM capabilities and user familiarity evolve. The taxonomy captures a snapshot of usage at this moment and should be revisited as new large-scale usage data becomes available.

---

## 4.2 Phase 2 — Benchmark Inventory

### 4.2.1 Search Strategy and Candidate Identification

The Phase 2 benchmark inventory was compiled through a four-channel systematic search designed to identify the major LLM benchmarks in active use as of early 2026. The four channels were implemented sequentially, with the outputs of each feeding into the candidate list.

The first channel was the Papers with Code benchmark catalogue, filtered to the Natural Language Processing and Language Models categories. This source provided a comprehensive starting set of benchmarks with citation counts, leaderboard data, and links to primary papers and code repositories. The second channel was the technical reports of major model releases: specifically, the GPT-4 technical report (OpenAI, 2023), the Claude 3 and Claude 3.5 technical reports (Anthropic, 2024), the Gemini technical reports (Google, 2023; 2024), the Llama 2 and Llama 3 technical reports (Meta AI, 2023; 2024), and the DeepSeek R1 technical report (DeepSeek, 2025). Each benchmark cited in two or more of these reports was added to the candidate list, on the grounds that use in multiple major model releases indicates community-wide adoption as a comparison standard. The third channel was a Google Scholar search for "LLM benchmark" and "language model evaluation" filtered to the period 2020–2025, with inclusion of papers reporting citation counts of 50 or more at the time of search. The fourth channel was snowball sampling from the reference lists of Handa et al. (2025), Xu et al. (2025), and Singh et al. (2025), capturing benchmarks that are directly relevant to the real-world use and evaluation validity questions motivating this project.

The four channels collectively identified 127 candidate benchmarks. These were screened against three inclusion criteria: public documentation (a paper or technical report must be available), use in at least two major model technical reports or equivalent community adoption, and coverage of at least one capability identified in the Phase 1 taxonomy. The screening process selected 28 benchmarks for the final inventory. The scope was expanded from the original 15–20 benchmark target following the completion of the Phase 1 taxonomy, which identified eight capabilities requiring representation. The selection rationale is documented in full in `data/phase2/benchmark_selection_rationale_v3.md`.

### 4.2.2 Inclusion Criteria and Selection Rationale

The three inclusion criteria applied in the screening process were chosen to ensure that the final inventory contained benchmarks that are both substantively well-documented and practically relevant as de facto evaluation standards.

The public documentation criterion excluded benchmarks that existed only in press releases, blog posts, or conference presentations without an accompanying academic paper or formal technical report. This criterion was necessary to ensure that the quality ratings computed in Phase 3 were grounded in documented evidence rather than in informal claims.

The adoption criterion ensured that the inventory reflected benchmarks that have genuine community uptake rather than proposals that have not been taken up. Citation in two or more major model technical reports was the primary proxy for adoption, supplemented by evidence of leaderboard presence, paper citations, and downstream replication in follow-up work.

The capability coverage criterion ensured that the final inventory spanned all eight capabilities identified in Phase 1, rather than concentrating in the capabilities most easily represented by established benchmarks. This required the inclusion of several newer benchmarks in capabilities such as tutoring (C04), review and feedback (C05), and conversational interaction (C08) that were not yet represented in major model technical reports at the time of the inventory, but which document the current evaluation landscape for those capabilities.

The final 28 benchmarks represent a deliberate choice to prioritise coverage of the capability space over exhaustive representation of any single capability. The benchmarks most commonly cited in frontier model technical reports — HumanEval, MMLU, HumanEval+, GPQA Diamond, Humanity's Last Exam, SWE-bench, and LiveCodeBench — are all present in the inventory, while newer benchmarks addressing gaps in tutoring, workplace writing, and conversational quality are also included to provide a more complete picture of the current evaluation landscape.

### 4.2.3 Inventory Overview

The 28 benchmarks in the final inventory span all eight capabilities and a publication year range of 2021 to 2025. Table 4.1 presents the distribution by primary capability.

**Table 4.1: Benchmark distribution by primary capability**

| Capability | Code | Benchmark count | Benchmark IDs |
|---|---|---|---|
| Code Development and Technical Problem Solving | C02 | 5 | B001–B005 |
| Information Retrieval and Advisory | C03 | 5 | B006–B010 |
| Content Generation | C01 | 4 | B011–B014 |
| Data Analysis and Summarisation | C07 | 4 | B015–B018 |
| Learning and Education Support | C04 | 3 | B019–B021 |
| Review and Feedback | C05 | 3 | B022–B024 |
| Conversational Interaction and Roleplay | C08 | 2 | B025–B026 |
| Translation and Language Processing | C06 | 2 | B027–B028 |

The C02 benchmarks (B001–B005) comprise HumanEval/HumanEval+ (Chen et al., 2021; Liu et al., 2023), SWE-bench Verified (Jimenez et al., 2024), LiveCodeBench (Jain et al., 2024), BigCodeBench Hard (Zhuo et al., 2024), and SWE-Lancer Diamond (Miserendino et al., 2025). These range from legacy single-function code generation (HumanEval) to frontier agentic software engineering with economic task value (SWE-Lancer Diamond), reflecting the evolution of coding evaluation from narrow proxy measures toward realistic software engineering workflows.

The C03 benchmarks (B006–B010) comprise MMLU-Pro (Wang et al., 2024), GPQA Diamond (Rein et al., 2023), Humanity's Last Exam (Phan et al., 2025), SimpleQA/FACTS Grounding (Wei et al., 2024; Jacovi et al., 2025), and LiveBench (White et al., 2024). These span academic knowledge breadth (MMLU-Pro), expert STEM reasoning (GPQA Diamond), frontier expert knowledge (Humanity's Last Exam), factuality and grounding (SimpleQA/FACTS), and contamination-resistant multi-domain reasoning (LiveBench).

The C01 benchmarks (B011–B014) comprise IFEval (Zhou et al., 2023), WritingBench (Chen et al., 2025), EQ-Bench Creative Writing v3 (Paech, 2023/2025), and WildBench (Lin et al., 2024). These address instruction following with verifiable constraints, broad writing quality across six domains, creative writing style and narrative quality, and real-user task performance across a curated sample of challenging prompts.

The C07 benchmarks (B015–B018) comprise InfiAgent-DABench (Hu et al., 2024), DA-Code (Huang et al., 2024), Spider 2.0 (Lei et al., 2024), and MMLongBench-Doc (Ma et al., 2024). These address agentic CSV analysis, executable data science workflows, enterprise SQL and BI tasks, and long-context multimodal document question answering.

The C04 benchmarks (B019–B021) comprise MathDial (Macina et al., 2023), MathTutorBench (Macina et al., 2025), and TutorBench (Srinivasa et al., 2025). These provide tutoring-specific evaluation grounded in pedagogical rubrics, distinguishing tutoring quality from answer correctness.

The C05 benchmarks (B022–B024) comprise CriticBench (Lin et al., 2024), JudgeBench (Tan et al., 2024/2025), and RewardBench 2 (Malik et al., 2025). These capture critique and correction capability, LLM-as-judge calibration, and reward model evaluation for alignment signal quality.

The C08 benchmarks (B025–B026) comprise PingPong (Gusev, 2024/2025) and CoSER (Wang et al., 2025). These provide dynamic multi-turn roleplay evaluation and authentic character roleplay grounded in literary sources.

The C06 benchmarks (B027–B028) comprise BenchMAX (Huang et al., 2025) and WMT24++ (Deutsch et al., 2025). These provide comprehensive multilingual capability evaluation and machine translation quality assessment with human-written references.

### 4.2.4 Quality Ratings Analysis

Each of the 28 benchmarks was rated on five quality dimensions using a 1–5 scale: Coherence (internal consistency and logical structure of the task set), Accuracy (reliability of the ground truth labels and expected outputs), Clarity (precision and unambiguity of task instructions), Relevance (correspondence between what the benchmark measures and real-world capability as defined by the Phase 1 taxonomy), and Efficiency (practical cost and complexity of running the evaluation). Every rating was accompanied by a written justification in the benchmark database.

The mean ratings across all 28 benchmarks were: Coherence 4.61, Accuracy 4.39, Clarity 4.21, Relevance 4.54, and Efficiency 3.50. The Coherence and Relevance scores are highest, reflecting the decision to replace saturated or weakly adopted benchmarks with more recent designs grounded in real-world workflows and with stronger construct validity for their stated capability areas. The Efficiency score is lowest at 3.50, driven by agentic benchmarks (SWE-bench Verified, DA-Code, Spider 2.0, SWE-Lancer Diamond), writing benchmarks requiring LLM judges (WritingBench, EQ-Bench Creative Writing), tutoring benchmarks requiring human or LLM evaluation (MathDial, TutorBench), and roleplay benchmarks requiring multi-turn simulation (PingPong, CoSER). These benchmarks score low on Efficiency not because they are poorly designed but because their validity depends on realistic evaluation conditions that are inherently more costly than simple automated scoring.

### 4.2.5 Contamination Risk Assessment

Each benchmark was assigned a contamination risk level (High, Medium, or Low) based on the nature of its task design, the currency of its test data, and the availability of information about training data for models that have been evaluated on it.

The results were: High contamination risk, 1 benchmark; Medium risk, 3 benchmarks; Low risk, 24 benchmarks. HumanEval (B001) is the single high-risk benchmark, assigned this classification because its 164-problem test set has been publicly available since 2021, is widely distributed in training corpora, and has been noted as saturated in subsequent evaluation literature (Jain et al., 2024). MMLU-Pro (B006), BigCodeBench Hard (B004), and WildBench (B014) are the three medium-risk benchmarks, assigned this classification because their public availability creates some memorisation risk despite their more recent release dates or greater task complexity. The remaining 24 benchmarks are classified as low risk due to recent release dates, dynamic task refreshing, private holdouts, gated access, or task designs (open-ended generation, agentic execution, multi-turn interaction) that substantially limit the value of memorised responses.

The low contamination rate in the v3 inventory reflects a deliberate curation decision: where older, higher-risk benchmarks were the only option for a capability area, newer alternatives were included where available. The retention of HumanEval as a legacy anchor benchmark is appropriate for historical comparison purposes, but it is accompanied by an explicit recommendation not to treat it as a primary model selection criterion.

### 4.2.6 Limitations of Phase 2

Three limitations of the Phase 2 inventory are acknowledged. First, the inventory is restricted to benchmarks published in English and is likely to underrepresent evaluation frameworks developed by research communities working in other languages, particularly for capabilities such as translation (C06) and conversational interaction (C08). Second, citation counts and technical report mentions are used as proxies for community adoption, but citation patterns may reflect the visibility and publication venues of proposing teams rather than genuine uptake in evaluation practice. Third, the quality ratings are researcher judgements based on the primary paper, available code repositories, and documented follow-up literature; they do not include direct empirical testing of the benchmarks, and they may not capture implementation-specific issues that are only apparent when the benchmarks are run in practice.

---

## 4.3 Phase 3 — Coverage Analysis

### 4.3.1 Coverage Matrix Construction

The Phase 3 coverage matrix was constructed by systematically assessing how well each of the 28 benchmarks in the Phase 2 inventory tests each of the eight capabilities in the Phase 1 taxonomy. The matrix has benchmarks as rows and capabilities as columns; each cell contains a rating from 0 (capability not tested) to 5 (capability tested at excellent quality). Every non-zero cell is accompanied by a written justification in the companion notes file (`data/phase3/coverage_matrix_notes.csv`).

The rating scale for coverage cells follows the same five-point quality rubric used in the Phase 2 benchmark database, applied now to capability-specific coverage: 5 indicates that the benchmark fully and rigorously tests the capability as defined in the taxonomy; 4 indicates good coverage with minor gaps; 3 indicates adequate coverage with notable limitations; 2 indicates partial or secondary coverage with significant limitations; and 1 indicates marginal or highly indirect coverage. A rating of 0 indicates that the benchmark provides no meaningful test of the capability.

Across the full 28 × 8 matrix (224 possible cells), 50 cells received non-zero justified ratings. This relatively sparse matrix reflects the fact that most benchmarks are designed to measure a specific capability rather than to provide general-purpose evaluation, and that secondary coverage ratings of 2 or above were assigned only where there was genuine and documented evidence that the benchmark addressed the secondary capability in a substantive way.

For each of the eight capabilities, three aggregate coverage metrics were computed from the matrix: the total coverage score (the sum of all cell ratings divided by the maximum possible sum of 140, representing 28 benchmarks at the maximum rating of 5 each), the benchmark count (the number of benchmarks with a non-zero rating), and the average quality (the mean rating across non-zero cells). These metrics are presented in Table 4.2 alongside the usage frequency weights derived from the AEI data and the gap scores computed in Phase 3.2.

### 4.3.2 Gap Score Computation

The central quantitative measure of this analysis is the usage-weighted gap score, defined in Chapter 3 as:

> **Gap Score = Usage\_Frequency × (1 − Normalised\_Coverage\_Score)**

where Usage\_Frequency is the proportion of total LLM usage attributable to the capability (derived from the summed AEI usage percentages for tasks mapped to each capability), and Normalised\_Coverage\_Score is the total coverage score expressed as a proportion of the maximum possible score (0–1). A higher gap score indicates a capability that is both heavily used in practice and poorly covered by existing benchmarks.

Usage frequencies for each capability were derived by summing the usage percentages from the Anthropic AEI top-103 task data for all tasks mapped to that capability in Phase 1. C02 had the highest usage frequency at 0.3019 (the sum of all AEI task percentages for tasks classified as code development and technical problem solving, including the 4.16% for troubleshooting hardware and system issues, the 3.92% for web application development, the 1.86% for debugging and refactoring, and so on). C01 had the second highest frequency at 0.2568, C03 at 0.1754, C04 at 0.1113, C07 at 0.0751, C05 at 0.0308, C06 at 0.0271, and C08 at 0.0215.

The gap scores are presented in full in Table 4.2.

**Table 4.2: Gap score ranking — all eight capabilities**

| Rank | Capability | Usage frequency | Coverage score | Benchmark count | Average quality | Gap score | Severity |
|---|---|---|---|---|---|---|---|
| 1 | C02 Code Development | 0.3019 | 0.2357 | 10 | 3.30 | 0.2307 | High |
| 2 | C01 Content Generation | 0.2568 | 0.1429 | 6 | 3.33 | 0.2202 | High |
| 3 | C03 Information Retrieval and Advisory | 0.1754 | 0.1714 | 7 | 3.43 | 0.1453 | High |
| 4 | C04 Learning and Education Support | 0.1113 | 0.1714 | 8 | 3.00 | 0.0922 | High |
| 5 | C07 Data Analysis and Summarisation | 0.0751 | 0.2000 | 7 | 4.00 | 0.0601 | Medium |
| 6 | C05 Review and Feedback | 0.0308 | 0.1286 | 5 | 3.60 | 0.0269 | Medium |
| 7 | C06 Translation and Language Processing | 0.0271 | 0.0714 | 2 | 5.00 | 0.0252 | Medium |
| 8 | C08 Conversational Interaction and Roleplay | 0.0215 | 0.1286 | 5 | 3.60 | 0.0188 | Low |

The three highest-ranked gaps are C02 (0.2307), C01 (0.2202), and C03 (0.1453), all classified as High severity. A result that merits interpretation is that C02 — Code Development and Technical Problem Solving — ranks first despite having the highest number of benchmarks (ten, including secondary coverage assignments) and the highest normalised coverage score (0.2357). This is a consequence of the formula structure: C02's gap score is high because its usage frequency (0.3019) is so substantially greater than what even the densest benchmark coverage can proportionally address. The formula rewards benchmarks for their absolute coverage quality but scales the gap by the volume of real-world demand; where demand is very high, even a relatively well-covered capability can have a large gap score in absolute terms.

C01 ranks second with a gap score of 0.2202. In contrast to C02, C01 has both high demand (0.2568) and relatively thin coverage (0.1429 coverage score, six benchmarks, average quality 3.33). The dominant C01 benchmarks — IFEval, WildBench — measure constraint compliance and real-user task breadth respectively but do not directly evaluate the workplace writing quality, audience adaptation, and professional artefact production that characterise the most common C01 tasks in the AEI data.

C03 ranks third with a gap score of 0.1453. The C03 benchmarks, which include MMLU-Pro, GPQA Diamond, and Humanity's Last Exam, are well-designed for testing academic knowledge breadth and expert reasoning. However, they do not test the advisory dimension of C03 — whether models can provide contextually appropriate, evidence-grounded, and appropriately hedged recommendations for users making real decisions. SimpleQA and FACTS Grounding address factuality and source faithfulness but do not cover the full advisory construct as defined in the taxonomy.

C04 ranks fourth (0.0922), C07 fifth (0.0601), C05 sixth (0.0269), C06 seventh (0.0252), and C08 eighth (0.0188) in the gap rankings. C06 has a low gap score not because it is well-covered but because its usage frequency in the AEI data is relatively low (0.0271), and the two benchmarks that do cover it — BenchMAX and WMT24++ — are of high quality (average rating 5.00). C08 has the lowest gap score, reflecting both relatively low AEI-measured frequency and moderate coverage across five benchmarks.

### 4.3.3 Statistical Analysis

Three statistical analyses were conducted on the Phase 3 data using Python with the `scipy` and `numpy` libraries, with `np.random.seed(42)` set for all operations involving randomisation.

**Pearson Correlation.** A Pearson correlation was computed between usage frequency and total coverage score across the eight capabilities, testing the null hypothesis that usage frequency and benchmark coverage are uncorrelated. The result was r = 0.639, p = 0.088 (two-tailed), 95% confidence interval [−0.119, 0.927]. The moderate positive correlation indicates a tendency for higher-usage capabilities to receive more benchmark coverage, but the correlation is not statistically significant at the conventional α = 0.05 threshold, reflecting substantial uncertainty given the small sample of eight capabilities. The 95% confidence interval is wide, spanning from a weak negative relationship to a strong positive relationship, and the p-value should be interpreted in the context of this sample size rather than as evidence of a specific population-level relationship. The direction of the correlation is consistent with the hypothesis that the research community has directed benchmark development partly toward the capabilities with greatest demand, but the magnitude of the relationship is modest enough that systematic misalignment remains plausible.

**Chi-Square Goodness-of-Fit.** A chi-square goodness-of-fit test was computed to assess whether the observed distribution of benchmark counts across capabilities (using primary capability assignments from Phase 2) matched the expected distribution if benchmarks were allocated in proportion to usage frequency. The observed counts ranged from 2 benchmarks (C06) to 5 benchmarks (C02, C03, C04, C07), while the expected counts based on usage frequency ranged from 0.6 (C08) to 8.5 (C02). The test statistic was χ²(7) = 31.96, p < 0.001, Cramér's V = 0.302 (bootstrap 95% CI: [0.202, 0.528]). This result provides strong evidence that the distribution of benchmark coverage across capabilities does not match the distribution of real-world usage demand. Benchmarks are not proportionately allocated to the most heavily used capabilities: C02, which accounts for 30.2% of documented usage, has only 5 primary-capability benchmarks rather than the approximately 8.5 that proportional allocation would predict, while C06, accounting for 2.7% of usage, has 2 benchmarks rather than the 0.76 expected.

This chi-square result should be interpreted as a distributional diagnostic rather than a causal claim. The expected distribution is a modelling choice — it assumes that benchmarks should be distributed in proportion to usage frequency — and this assumption, while a defensible baseline for gap analysis, is not the only possible allocation rule. Some capabilities, such as translation (C06), may be well-served by fewer high-quality benchmarks given the nature of their evaluation requirements, while others, such as conversational interaction (C08), may warrant representation even at relatively low usage frequencies because of safety and deployment considerations.

**Temporal Linear Regression.** Separate linear regressions were computed for each capability, modelling the annual count of benchmarks published from 2020 to 2025 as a function of year. The results reveal that C01, C04, and C05 show statistically significant positive slopes, indicating accelerating benchmark activity in these capability areas. C01 has slope = 0.5143, R² = 0.7714, p = 0.0213 (95% CI: [0.126, 0.903]), suggesting increasing research investment in content generation evaluation. C04 has slope = 0.7429, R² = 0.8521, p = 0.0086 (95% CI: [0.313, 1.173]), reflecting the emergence of tutoring-specific benchmarks from approximately 2023. C05 has slope = 0.6000, R² = 0.7132, p = 0.0344 (95% CI: [0.072, 1.128]), consistent with growing interest in critique and feedback evaluation.

C02, C03, C07, C06, and C08 show positive slopes but not statistically significant ones, indicating that benchmark activity in these areas has increased over the study period but that the temporal pattern is not distinguishable from noise at the sample sizes available (six annual observations per capability). These temporal results should be read as descriptive signals rather than confirmatory evidence: with only six data points per regression, p-values are highly sensitive to individual year counts, and the regressions are not suitable for forecasting.

### 4.3.4 Deep-Dive Qualitative Analyses

Four qualitative deep-dive analyses were conducted for capabilities spanning the coverage spectrum: C02 (highest gap), C07 (moderate coverage with medium gap), C04 (increasing benchmark activity but moderate gap), and C06 (low usage with niche coverage). Each deep dive examined the current evaluation landscape, technical and practical challenges to evaluation, real-world importance grounded in usage data, and the requirements for adequate coverage. The following presents a summary of the main findings from each.

**C02 — Code Development and Technical Problem Solving (gap score 0.2307, highest gap).** The C02 benchmark landscape is the most active in the inventory, with five primary benchmarks (HumanEval, SWE-bench Verified, LiveCodeBench, BigCodeBench Hard, SWE-Lancer Diamond) plus secondary coverage from five further benchmarks. Despite this volume, the coverage is uneven across the sub-categories of the C02 taxonomy. The strongest benchmarks — SWE-bench Verified, BigCodeBench Hard, and SWE-Lancer Diamond — target repository-level issue resolution and library-oriented code generation, both of which are more aligned with professional software engineering than with the most frequent C02 task types in the AEI data. The tasks accounting for the highest usage frequencies in the AEI — troubleshooting hardware and system issues (4.16%), web application development (3.92%), debugging and refactoring (1.86%) — reflect everyday maintenance and multi-step technical support rather than either competitive programming (LiveCodeBench's primary focus) or high-stakes issue resolution in pre-verified repository environments (SWE-bench Verified's primary context). The aggregate quality score of 3.30 for C02 benchmarks reflects this unevenness: there are strong benchmarks, but they do not collectively cover the breadth of the capability as used in practice.

Technical challenges to C02 evaluation include the cost of agentic execution environments, the difficulty of specifying ground truth for open-ended technical solutions, the contamination risk in static public datasets, and the challenge of representing the full range of programming languages, frameworks, and deployment contexts used in real-world technical assistance. The consequences of inadequate C02 evaluation include misaligned model selection decisions for technical deployment contexts and potential optimisation of training toward benchmark-specific coding skills at the expense of broader technical problem-solving ability.

**C07 — Data Analysis and Summarisation (gap score 0.0601, medium gap).** The C07 benchmark landscape includes four primary benchmarks (InfiAgent-DABench, DA-Code, Spider 2.0, MMLongBench-Doc) with the highest average quality score in the inventory (4.00) and reasonable coverage of data analysis workflows. The coverage limitation is structural: existing C07 benchmarks tend to be CSV-centric (InfiAgent-DABench, DA-Code), SQL and business intelligence-centric (Spider 2.0), or document question answering-centric (MMLongBench-Doc). Real data analysis tasks, as documented in the AEI, often involve messy spreadsheets, inconsistent labels, missing values, mixed file formats, and the need to communicate cautious conclusions to non-technical audiences — a full analyst workflow that is not cleanly captured by any single benchmark in the inventory. The moderate gap score (0.0601) reflects both the relatively lower usage frequency of C07 compared to C01–C04 and the reasonably strong quality of existing C07 benchmarks.

**C04 — Learning and Education Support (gap score 0.0922, high gap).** The C04 evaluation landscape has grown substantially since 2023, driven by the introduction of MathDial (Macina et al., 2023), MathTutorBench (Macina et al., 2025), and TutorBench (Srinivasa et al., 2025). These benchmarks are distinctive in that they evaluate the model's performance as a tutor — its ability to diagnose misconceptions, provide scaffolded hints, offer formative feedback, and adapt to the learner's responses — rather than simply testing whether the model can produce the correct answer to an academic question. MathTutorBench in particular demonstrates that stronger academic reasoning models are not necessarily better tutors, providing evidence that the tutoring construct is distinct from general knowledge or reasoning performance. The average quality score of 3.00 for C04 benchmarks reflects the relative novelty of this evaluation paradigm and the methodological challenges of assessing pedagogical quality through automated or LLM-judge scoring. The temporal regression result for C04 (slope = 0.7429, p = 0.0086) indicates that this is the area of most rapid benchmark development in the recent period, suggesting that the gap may narrow as the field matures.

**C06 — Translation and Language Processing (gap score 0.0252, medium gap).** The C06 benchmark landscape is served by only two primary benchmarks — BenchMAX and WMT24++ — but both are of high quality (average rating 5.00). BenchMAX provides comprehensive multilingual evaluation across 16 languages with native annotator post-editing, while WMT24++ extends the established WMT shared task framework to 55 languages with human-written references and post-edits. The relatively low gap score for C06 reflects both its modest usage frequency in the AEI data (0.0271) and the maturity of machine translation evaluation as a research area. The main uncovered areas within C06 are language learning support and multilingual instruction following — sub-categories not well-addressed by either of the two primary benchmarks, both of which focus primarily on translation quality.

### 4.3.5 Case Studies — Benchmark Performance vs. Real-World Failure

Six case studies were documented to illustrate specific instances where high benchmark performance, or confidence generated by benchmark reporting, did not correspond to reliable performance in realistic deployment settings.

**Case 1: Autonomous workplace agents complete only 30% of tasks (Xu et al., 2025).** TheAgentCompany benchmark evaluates frontier LLM agents in a simulated software-company environment requiring navigation, coding, communication, and task completion across HR, finance, engineering, and administrative workflows. Despite strong performance on standard evaluations, the best models complete approximately 30% of these integrated tasks. The failure modes include long-horizon planning failures, tool use errors, and context management failures rather than isolated factual errors. This case implicates C02, C03, and C07, and demonstrates that aggregate benchmark strength does not predict production readiness for autonomous integrated work.

**Case 2: Coding scores fall on post-cutoff problems (Jain et al., 2024).** LiveCodeBench demonstrates that model performance on coding problems declines when evaluated on problems released after the model's likely training cutoff, providing direct evidence of contamination effects in static coding benchmarks. Teams that select models based on HumanEval or similar static benchmark scores may deploy models that perform substantially worse on new engineering problems than their scores suggest. This case implicates C02.

**Case 3: Multiple-choice rankings change under answer-order perturbations (Pezeshkpour and Hruschka, 2024).** Changing the order of answer options in MMLU-style questions shifts model rankings by up to eight positions. The underlying knowledge has not changed; only the surface presentation has. This format sensitivity means that leaderboard rankings based on multiple-choice benchmarks are partly a function of presentation format rather than stable capability. This case implicates C03 and the general validity of multiple-choice evaluation for any capability area.

**Case 4: Clinical decision-making failures persist despite strong medical benchmark scores (Kanjee et al., 2024).** LLMs that achieve strong results on medical knowledge benchmarks continue to make clinically significant errors in realistic patient case scenarios, including diagnostic mistakes, guideline adherence failures, and inappropriate responses to patient-specific context. This case implicates C03 (medical advisory) and C07 (clinical data analysis), and demonstrates the gap between aggregate knowledge benchmark performance and capability for consequential real-world decision support.

**Case 5: Legal hallucinations lead to false citations and professional sanctions (Magesh et al., 2025).** Legal research tools based on general LLMs generate fictitious legal citations and unsupported legal claims that appear authoritative. Practitioners who rely on these outputs without verification risk professional sanctions. This case implicates C03 (legal information retrieval), C01 (legal document drafting), and C05 (review of legal content), and illustrates why factuality and grounding benchmarks that measure short-fact recall are insufficient for the advisory tasks that carry the greatest real-world consequence.

**Case 6: Leaderboard disclosure practices distort model selection (Singh et al., 2025).** Systematic analysis of technical report benchmark tables demonstrates that providers selectively cite the benchmarks on which their models perform best, with full-disclosure rankings differing by up to 112 positions from selectively reported rankings. Practitioners who rely on reported benchmark tables for model selection decisions may choose models on the basis of a strategically curated rather than representative evidence base. This case implicates all capability areas and represents a structural validity problem in the benchmark reporting ecosystem rather than a failure of any specific benchmark.

The cross-case pattern is consistent: benchmarks are valid instruments for measuring specific capabilities under specific conditions, but they are regularly used as broader evidence of capability than their design and context can support. Reliable deployment decisions require capability-specific evaluation rather than aggregate benchmark scores, and the gap analysis presented in this chapter identifies where the evaluation frameworks needed for such decisions are most urgently missing.

### 4.3.6 Limitations of Phase 3

Four limitations of the Phase 3 analysis are acknowledged. First, all coverage ratings in the matrix are researcher judgements rather than experimentally verified measures; different researchers applying the same rubric might assign different ratings to some cells, and the written justifications, while they constrain the rating space, do not eliminate this subjectivity. Second, the usage frequency weights are derived from a single provider's data (Anthropic AEI), which may not represent the full distribution of LLM use across different providers, deployment contexts, and user populations. Third, the Pearson correlation and chi-square tests are based on eight capability-level observations, which is a small sample for statistical inference; the results should be treated as descriptive summaries of the observed data rather than as confirmatory tests of population-level hypotheses. Fourth, the temporal regressions use only six annual observations (2020–2025), making individual year counts highly influential and slope estimates correspondingly uncertain.

---

## References

Balloccu, S., Schmidtová, P., Lango, M. and Dusek, O. (2024). Leak, cheat, repeat: Data contamination and evaluation malpractices in closed-source LLMs. In *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics*. Association for Computational Linguistics.

Braun, V. and Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), pp. 77–101. https://doi.org/10.1191/1478088706qp063oa

Chen, M., Tworek, J., Jun, H., Yuan, Q. and Zaremba, W. et al. (2021). Evaluating large language models trained on code. arXiv:2107.03374.

Chen, Y., Zhang, Y., Li, J., Liang, X., He, J., Yang, C., Huang, Y., Gong, M., Zhang, M. and Liu, L. (2025). WritingBench: A comprehensive benchmark for generative writing. In *Advances in Neural Information Processing Systems* (Vol. 38).

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), pp. 37–46.

DeepSeek AI (2025). DeepSeek R1: Incentivizing reasoning capability in LLMs via reinforcement learning. arXiv:2501.12948.

Deutsch, F., Freitag, M., Blain, F., Dhawan, M., Marchisio, G., Reinauer, J. and Bojar, O. (2025). WMT24++: Expanding evaluation to more languages and modalities. arXiv:2502.12404.

Gusev, A. (2024). PingPong: A benchmark for role-playing language models with user simulator and the evaluation of in-context learning. arXiv:2409.06820.

Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Henighan, T., Joseph, N., Kinniment, M., Kundu, S., McCain, J., Perez, E., Schiefer, N., Shoker, S., Sleight, H., Teplitskiy, M., Wijk, H., Clark, J., Kaplan, J., Ganguli, D. and Anthropic (2025). *Which economic tasks are performed with AI? Evidence from millions of Claude conversations*. arXiv:2503.04761.

Hu, Y., Zhao, J., Wei, X., Liu, Q., Liu, Y., Chu, Z., Yin, W., Lin, B. Y. and Bing, L. (2024). InfiAgent-DABench: Evaluating agents on data analysis tasks. In *Proceedings of the 41st International Conference on Machine Learning*. arXiv:2401.05507.

Huang, J., Zhu, Y., Hu, Y., Li, X., Yao, X., Wan, X. and He, Z. (2025). BenchMAX: A comprehensive multilingual evaluation suite for LLMs. In *Findings of EMNLP 2025*. https://doi.org/10.18653/v1/2025.findings-emnlp.909

Huang, H., Luo, X., Yu, Z., Zhang, Y., Lin, Y., Ma, X., Wen, X., Liu, Y. and Xu, B. (2024). DA-Code: Agent data science code generation benchmark for large language models. In *Proceedings of EMNLP 2024*. arXiv:2410.07331.

Jacovi, A., Caciularu, A., Goldman, O. and Goldberg, Y. (2025). FACTS Grounding: A new benchmark for evaluating the factuality of large language models. arXiv:2501.03200.

Jain, N., Han, K., Gu, A., Li, W.-D., Yan, F., Zhang, T., Wang, S., Solar-Lezama, A., Sen, K. and Stoica, I. (2024). LiveCodeBench: Holistic and contamination free evaluation of large language models for code. arXiv:2403.07974.

Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O. and Narasimhan, K. (2024). SWE-bench: Can language models resolve real-world GitHub issues? In *Proceedings of the 12th International Conference on Learning Representations*. arXiv:2310.06770.

Kanjee, Z., Crowe, B. and Rodman, A. (2024). Evaluation and mitigation of the limitations of large language models in clinical decision-making. *Nature Medicine*, 30, pp. 2613–2615.

Lei, F., Chen, Y., Ye, Q., Peng, W., Liu, S., Huang, M., Wang, H., Liu, H., Chen, W., Wen, B., Cohan, A. and Yilmaz, E. (2024). Spider 2.0: Evaluating language models on real-world enterprise text-to-SQL workflows. arXiv:2411.07763.

Lin, J., Deng, Y., Chandu, K., Brahman, F., Dziri, N., Hwang, J. D., Bhagavatula, C., Peng, X., Smith, N. A. and Choi, Y. (2024). WildBench: Benchmarking LLMs with challenging tasks from real users in the wild. arXiv:2406.04770.

Lin, Z., Rañola, J. M., Mao, Y., Zhang, J. and Zhao, J. (2024). CriticBench: Benchmarking LLMs for critique capability. In *Findings of the Association for Computational Linguistics: ACL 2024*. arXiv:2402.14809.

Liu, J., Xia, C. S., Wang, Y. and Zhang, L. (2023). Is your code generated by ChatGPT really correct? Rigorous evaluation of large language models with EvalPlus. In *Advances in Neural Information Processing Systems* (Vol. 36). arXiv:2305.01210.

Ma, R., Zang, P., Chen, X., Dong, X., Zhang, J., Lu, J., Chen, H. and Zhu, J. (2024). MMLongBench-Doc: Benchmarking long-context document understanding with visualizations. In *Advances in Neural Information Processing Systems* (Vol. 37). arXiv:2407.01523.

Macina, J., Daheim, N., Chowdhury, S. P., Sinha, T., Kapur, M., Gurevych, I. and Sachan, M. (2023). MathDial: A dialogue tutoring dataset with rich pedagogical properties grounded in math reasoning problems. In *Findings of EMNLP 2023*. arXiv:2311.09885.

Macina, J., Daheim, N., Hakimi, R., Chowdhury, S. P., Kapur, M., Gurevych, I. and Sachan, M. (2025). MathTutorBench: A benchmark for measuring open-ended pedagogical capabilities of tutoring systems. In *Proceedings of EMNLP 2025*. arXiv:2502.18940.

Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D. and Ho, D. E. (2025). Hallucination-free? Assessing the reliability of leading AI legal research tools. arXiv:2405.20362.

Malik, J., Lambert, N., Dubois, Y., Jain, P., Farquhar, S., Bhatt, U. and Kiela, D. (2025). RewardBench 2: Advancing reward model evaluation. arXiv:2506.01937.

Meta AI (2023). Llama 2: Open foundation and fine-tuned chat models. arXiv:2307.09288.

Meta AI (2024). The Llama 3 herd of models. arXiv:2407.21783.

Miserendino, S., Wang, J., Jain, S., Boisvert, A., Salemans, T., Dou, B., Allen, D., Bhatt, U., Brundage, M. and OpenAI (2025). SWE-lancer: Can frontier LLMs earn $1 million from real-world freelance software engineering? arXiv:2502.12115.

OpenAI (2023). GPT-4 technical report. arXiv:2303.08774.

Anthropic (2024). Claude 3 model card. https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model-Card-Claude-3.pdf

Ouyang, S., Shi, W., Zheng, R., Xu, J., Cai, Y., Wei, J., Fu, J., Ji, Y., Yin, D. and Zheng, R. (2025). *How are large language models used? Evidence from millions of OpenAI API requests* (NBER Working Paper 34255). National Bureau of Economic Research.

Paech, S. (2023/2025). EQ-Bench: An emotional intelligence benchmark for large language models. arXiv:2312.06281.

Pezeshkpour, P. and Hruschka, E. (2024). Large language models sensitivity to the order of options in multiple-choice questions. In *Findings of the Association for Computational Linguistics: NAACL 2024*. arXiv:2308.11483.

Phan, L., Gatti, A., Han, Z. and Scale AI et al. (2025). Humanity's last exam. arXiv:2501.14249.

Rein, D., Hou, B. L., Stickland, A. C., Petty, J., Pang, R. Y., Dirani, J., Michael, J. and Bowman, S. R. (2023). GPQA: A graduate-level Google-proof Q&A benchmark. arXiv:2311.12022.

Singh, S., Stroebl, A., Kambhampati, S., Kapoor, S., Narayanan, A., Ghassemi, M. and Bommasani, R. (2025). The leaderboard illusion. arXiv:2504.20879.

Srinivasa, A., Che, P., Zhang, D., Ge, X., Wang, P., Weiss, J., Mou, C. and Scale AI (2025). TutorBench: A multisubject multimodal benchmark for evaluating AI tutoring systems. arXiv:2510.02663.

Tan, J., Zhang, D., Zhang, M., Huang, X., Zhou, L., Zhang, Y. and Shi, S. (2024). JudgeBench: A benchmark for evaluating LLM-based judges. arXiv:2410.12784.

Wang, Y., Ma, X., Zhang, G., Ni, Y. and Chen, W. et al. (2024). MMLU-Pro: A more robust and challenging multi-task language understanding benchmark. arXiv:2406.01574.

Wang, C., Wang, X., Zhang, H., Lin, X., Che, W., Chen, L. and Li, Z. (2025). CoSER: Towards consistent, structured and expressive roleplay agents. In *Proceedings of the 42nd International Conference on Machine Learning*. arXiv:2502.09082.

Wei, J., Ho, D. E., Manning, C. D. and OpenAI (2024). Measuring short-form factuality in large language models. OpenAI technical blog.

White, C., Dooley, S., Roberts, M. and Goldstein, T. et al. (2024). LiveBench: A challenging, contamination-free LLM benchmark. In *Proceedings of the 13th International Conference on Learning Representations*. arXiv:2406.19314.

Xu, F. F., Ye, Y., Arenas, O., Yao, S. and Neubig, G. et al. (2025). TheAgentCompany: Benchmarking LLM agents on consequential real world tasks. arXiv:2412.14161.

Zhao, W., Jiang, Z., Xu, Z., Shen, Q., Xu, Z., Qin, L., Liu, X., Wang, H., Guo, H. and Ma, J. (2024). WildChat: 1M ChatGPT interaction logs in the wild. arXiv:2405.01470.

Zhou, J., Lu, T., Mishra, S., Brahma, S., Basu, S., Luan, Y., Zhou, D. and Hou, L. (2023). Instruction-following evaluation for large language models. arXiv:2311.07911.

Zhuo, T. Y., Cassano, F., Dekoninck, J., Szafraniec, M., Yim, H. H., Tran, K., Xu, N., Lappert, M., Defreez, D., Jain, A., Evtikhiev, M., Ding, T., Cassano, F., Gu, Q., Tian, T., Zhang, H. and Ding, B. (2024). BigCodeBench: Benchmarking code generation with diverse function calls and complex instructions. arXiv:2406.15877.
