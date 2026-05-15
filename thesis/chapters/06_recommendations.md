<!-- markdownlint-disable MD013 MD036 MD060 -->

# Chapter 6: Recommendations and Toolkit

**Target length:** 2,500–3,500 words

---

## 6.1 Overview

This chapter presents the Phase 5 outputs of this project: five benchmark design specifications targeting the highest-priority coverage gaps identified in Chapter 4, a set of improvement recommendations for the 28 existing benchmarks in the Phase 2 inventory, the practitioner Assessment Toolkit, and an implementation roadmap for the research community.

The benchmark specifications and improvement recommendations respond directly to the Phase 3 findings. The gap score analysis identified Code Development and Technical Problem Solving (C02, gap score 0.2307), Content Generation (C01, 0.2202), Information Retrieval and Advisory (C03, 0.1453), and Learning and Education Support (C04, 0.0922) as the four highest-priority gaps, all classified as High severity. Data Analysis and Summarisation (C07, 0.0601) was identified as the fifth-highest gap at Medium severity. These five capabilities are the targets of the new benchmark proposals in this chapter. The toolkit complements the specifications by giving practitioners a reusable instrument for evaluating how well any set of benchmarks covers their specific deployment context, independent of the benchmark proposals developed here.

---

## 6.2 Benchmark Design Specifications

### 6.2.1 Selection Rationale

Five benchmark specifications were developed, one for each of the five highest-priority gaps identified in Phase 3. The selection criterion for specifying a new benchmark rather than only recommending improvements to existing ones was whether the gap score analysis, combined with the deep-dive qualitative assessment, indicated that existing benchmarks were structurally unable to address the evaluation need — either because their task design was too narrow, their scoring mechanism was misaligned with the capability construct, or the capability area had no substantive benchmark coverage at all. All five selected capabilities met this criterion.

No two proposed benchmarks target the same capability, ensuring that the specifications collectively expand coverage across the identified priority gaps rather than duplicating effort in any single area. The benchmark names — MaintBench (C02), WorkWriteBench (C01), GroundedAdviceBench (C03), TutorScaffoldBench (C04), and MessyDataBench (C07) — are proposed working names intended to communicate the primary evaluation construct.

### 6.2.2 MaintBench — Software Maintenance Benchmark (C02)

MaintBench is proposed for C02, Code Development and Technical Problem Solving, which has the highest gap score in the project (0.2307). The benchmark is designed to test whether models can diagnose, modify, integrate, and maintain realistic software systems rather than only solving isolated coding prompts. The focus is on multi-file debugging, dependency integration, refactoring under constraints, configuration repair, regression prevention, and handoff-quality explanations — the middle layer of everyday software maintenance that is under-represented in existing C02 benchmarks.

The existing C02 landscape provides strong coverage of isolated code generation (HumanEval+), competitive programming (LiveCodeBench), library-oriented code tasks (BigCodeBench Hard), and agentic repository-level issue resolution (SWE-bench Verified, SWE-Lancer Diamond). What remains uncovered is the practical daily maintenance work that accounts for the highest-frequency AEI task categories: troubleshooting hardware and system issues (4.16% of usage), developing and debugging web applications (3.92%), and debugging and refactoring code across languages (1.86%). MaintBench targets this layer.

Each MaintBench task provides the model with a repository snapshot, a stakeholder request, relevant logs or failing tests, and project constraints. The required output is a patch accompanied by an engineering note explaining the diagnosis, the change, the verification steps, and any remaining risks. Ten illustrative task designs include: a Flask authentication regression affecting admin redirect behaviour, a Django CSV import command broken by a pandas version upgrade, a React checkout form that incorrectly clears state on validation failure, and a Node.js permission cache that retains revoked permissions until expiry. Each task requires multi-file navigation, root-cause diagnosis, and safe integration rather than isolated function writing.

The proposed first release contains approximately 600 tasks across 60 repositories, with each repository contributing 8–12 tasks. The recommended evaluation methodology combines automated correctness (tests, static analysis, build execution) with expert-judged assessment of maintainability, diagnosis quality, and constraint adherence. Implementation requires 4–6 months, engineering research expertise, containerised execution infrastructure, and expert developer time for hidden test construction and maintainability review.

MaintBench improves on SWE-bench Verified by addressing a broader range of maintenance sub-tasks (not only issue resolution), improves on LiveCodeBench by targeting maintenance workflows rather than competitive programming, and improves on BigCodeBench Hard by including multi-file context, existing codebases, and diagnosis requirements alongside code generation.

### 6.2.3 WorkWriteBench — Workplace Writing Benchmark (C01)

WorkWriteBench is proposed for C01, Content Generation, which has the second-highest gap score (0.2202). The benchmark is designed to evaluate professional writing under realistic workplace constraints, including professional communications, decision documents, marketing copy, technical documentation, and audience-specific transformations.

The existing C01 benchmarks — IFEval, WritingBench, EQ-Bench Creative Writing, and WildBench — cover instruction-following constraint compliance, broad writing quality across six domains, creative style and narrative voice, and real-user task diversity respectively. None addresses the specific evaluation challenge of workplace professional writing: the requirement that outputs preserve source facts accurately, fit a specified audience, adhere to tone and format constraints, and avoid unsupported claims. These dimensions are the defining features of the C01b (professional and business writing) and C01c (marketing and promotional writing) sub-categories that represent the highest-frequency AEI tasks in the C01 cluster.

Each WorkWriteBench task provides the model with a writing brief, source facts, a target audience, a purpose, format requirements, and constraints. Ten illustrative task designs include: an executive project update based on notes about a two-week launch delay, a customer apology email after a 45-minute service outage, a one-page security policy brief for non-technical managers, landing-page copy for a budgeting app, and a sensitive rewriting task that must convert inflammatory language into neutral board-report language while preserving factual content. Each task includes explicitly prohibited claims, required facts, and audience specifications that allow systematic scoring.

The proposed first release contains approximately 1,000 tasks across six task families. Evaluation uses hybrid scoring combining automated checks (required facts present, prohibited claims absent, length constraints, format requirements) with human or validated LLM-judge assessment of audience fit, tone, and writing usefulness. Implementation requires 3–4 months at medium cost, with human annotator time as the primary cost driver.

WorkWriteBench improves on IFEval by adding substantive writing quality to constraint compliance, improves on WritingBench by narrowing its focus to workplace artefact production with source grounding, and improves on WildBench by enabling precise C01 attribution rather than multi-capability coverage.

### 6.2.4 GroundedAdviceBench — Advisory Reasoning Benchmark (C03)

GroundedAdviceBench is proposed for C03, Information Retrieval and Advisory, which has the third-highest gap score (0.1453). The benchmark is designed to evaluate whether models can provide factual, evidence-grounded, context-sensitive advice while communicating uncertainty and maintaining appropriate limits — the advisory dimension of C03 that existing knowledge benchmarks do not directly measure.

The existing C03 benchmarks — MMLU-Pro, GPQA Diamond, Humanity's Last Exam, SimpleQA/FACTS Grounding, and LiveBench — provide strong coverage of academic knowledge breadth, expert STEM reasoning, frontier knowledge, and factual recall and grounding. What they do not measure is advisory behaviour: whether a model can turn evidence into contextually appropriate recommendations that are properly qualified, that acknowledge uncertainty, that maintain safety boundaries in high-stakes domains, and that identify when a question cannot be answered with available evidence. This advisory construct is central to the AEI task categories that map to C03, including medical information (2.38% of usage), career advisory (1.63%), product comparison (2.25%), and practical guidance (multiple categories).

Each GroundedAdviceBench task provides the model with a user question, user context, an evidence packet, and response requirements. Evidence packets may include product tables, policy documents, medical or legal guidance excerpts, research abstracts, or deliberately conflicting or incomplete information. Ten illustrative tasks include: a laptop recommendation with specified constraints, a health-information task requiring appropriate escalation and uncertainty hedging, a research synthesis task with mixed evidence quality, a legal-information boundary task requiring jurisdiction dependency disclosure, and a deliberately unanswerable advisory task requiring an explicit refusal with reasoning.

The proposed first release contains approximately 800 tasks across five advisory domains. Evaluation uses rubric scoring across factuality, grounding, uncertainty communication, relevance, and safety dimensions. Implementation requires 4–5 months at medium-to-high cost, with evidence-map construction and domain-literate review for high-stakes topics as the primary cost drivers. The benchmark distinguishes itself from MMLU-style knowledge benchmarks by making advisory behaviour the primary construct rather than a by-product of knowledge recall, and from SimpleQA/FACTS by requiring contextual recommendation under uncertainty rather than short factual answers.

### 6.2.5 TutorScaffoldBench — Tutoring and Pedagogy Benchmark (C04)

TutorScaffoldBench is proposed for C04, Learning and Education Support, which has the fourth-highest gap score (0.0922). The benchmark is designed to evaluate models as tutors rather than as answer engines, assessing misconception diagnosis, adaptive scaffolding, formative feedback, concept explanation, and academic-integrity-preserving responses.

The existing C04 benchmarks — MathDial, MathTutorBench, and TutorBench — represent a rapidly maturing area of evaluation. MathTutorBench demonstrates that stronger academic models are not necessarily better tutors, establishing the empirical basis for treating tutoring as a distinct construct. TutorBench broadens coverage beyond mathematics to multiple subjects and modalities. TutorScaffoldBench does not replace these benchmarks but extends them by increasing subject diversity, making pedagogical sub-skill reporting more interpretable, and explicitly covering academic-integrity scenarios where the appropriate tutor response is to refuse answer delivery and offer learning-support alternatives.

Each TutorScaffoldBench task provides the model with a learner profile, a learning objective, a student attempt or misconception, and a tutoring constraint. Ten illustrative tasks include: a Year 9 algebra misconception about distributive property, a beginner Python task involving off-by-one errors in range(), multi-turn fraction hinting, a physics explanation task requiring level-appropriate analogy rather than calculus, and a university assignment task requiring academic-integrity preservation. Some tasks are single-turn; others are short multi-turn scenarios where the model must adapt after receiving a learner follow-up response.

The proposed first release contains approximately 1,200 tasks across seven subject areas, with mathematics representing at most 30% of the dataset to avoid over-specialisation. Evaluation uses pedagogical rubric scoring across misconception diagnosis, scaffolding quality, formative feedback, and adaptive follow-up dimensions, with educator review for calibration. Implementation requires 3–4 months at medium cost.

### 6.2.6 MessyDataBench — Data Analysis Benchmark (C07)

MessyDataBench is proposed for C07, Data Analysis and Summarisation, which has a gap score of 0.0601 and Medium severity. Despite relatively stronger coverage than the top four capabilities, the existing C07 benchmarks do not collectively represent the full analyst workflow: they tend to be CSV-centric, SQL-centric, or document QA-centric, and they do not systematically test the model's ability to handle imperfect data, communicate cautious conclusions, or support non-technical stakeholders.

Each MessyDataBench task provides the model with a user request, one or more data files or document excerpts containing realistic data-quality issues, and a communication target. Ten illustrative tasks include: a customer purchase CSV with duplicate transaction IDs and mixed currency symbols, an A/B test interpretation task with explicit uncertainty requirements, a multi-file join task requiring justification of the denominator choice, a chart critique task involving a truncated y-axis, and a business-health interpretation task where revenue metrics and user retention metrics point in opposite directions. The benchmark focuses on the full analyst workflow: understanding the data, handling quality issues, applying appropriate methods, interpreting uncertainty, and communicating responsibly.

The proposed first release contains approximately 700 tasks with associated data packets. Evaluation combines automated calculation correctness checks with rubric scoring for method fit, uncertainty communication, and stakeholder-appropriate reporting. Implementation is 3–4 months at medium cost, with data packet construction and ground-truth calculation verification as the primary cost drivers.

---

## 6.3 Improvements to Existing Benchmarks

In addition to the five new benchmark proposals, this project identified actionable improvements for each of the 28 benchmarks in the Phase 2 inventory. The improvements address common structural weaknesses: contamination risk, scoring validity, coverage breadth, and reporting granularity.

For the C02 benchmarks, HumanEval should be retained only as a historical anchor and explicitly labelled as high contamination risk in any comparative reporting; SWE-bench Verified should add sub-category reporting by bug type, repository complexity, and maintenance burden; LiveCodeBench should improve clarity about the distinction between competitive programming skill and general software engineering; BigCodeBench Hard should expand language and ecosystem coverage beyond Python; and SWE-Lancer Diamond should improve reproducibility by publishing fuller task metadata and evaluation harness documentation.

For the C03 benchmarks, MMLU-Pro should add robustness reporting for answer-order sensitivity; GPQA Diamond should publish domain-specific uncertainty reporting to avoid overgeneralisation to advisory tasks; Humanity's Last Exam should publish clearer construct breakdowns distinguishing expert knowledge, multimodal reasoning, and factual recall; SimpleQA and FACTS Grounding should extend toward evidence-grounded recommendations and uncertainty handling; and LiveBench should improve capability attribution so that multi-domain scores can be disaggregated by capability.

For the C01 benchmarks, IFEval should add longer, source-grounded writing tasks to extend beyond constraint compliance; WritingBench should strengthen judge calibration documentation and add more workplace scenarios; EQ-Bench Creative Writing should publish judge version histories for reproducibility; and WildBench should add capability-specific subset reporting for C01, C02, and C08.

For the C07 benchmarks, InfiAgent-DABench should expand beyond CSV-centric tasks into mixed documents and stakeholder communication; DA-Code should provide lower-cost execution tiers and clearer diagnostics for environment failures; Spider 2.0 should add non-SQL analysis tasks or pair its results with spreadsheet and document analysis benchmarks; and MMLongBench-Doc should add summarisation and decision-support outputs beyond QA.

For the C04, C05, C06, and C08 benchmarks, the primary recommendations are to improve reporting granularity (sub-skill scores for tutoring benchmarks, dimension-level feedback scores for review benchmarks), to validate LLM judges against human ratings where they are used as the primary scoring mechanism, and to publish annotator guidelines and inter-rater reliability statistics to enable reproducibility and adoption.

---

## 6.4 The Assessment Toolkit

### 6.4.1 Design Rationale

The Assessment Toolkit is designed to address a practical problem that the benchmark specifications and gap scores cannot resolve on their own: practitioners selecting benchmarks for a specific deployment context need a way to evaluate coverage for their own use-case portfolio, not for the aggregate distribution of all LLM use. A hospital AI deployment has a different capability priority profile from a software development assistant or a consumer information service, and the gap scores in Chapter 4 reflect a population-average usage distribution that may not correspond to any specific deployment context.

The toolkit operationalises the Phase 1 taxonomy and Phase 3 coverage data as a structured instrument that practitioners can use interactively. Its intended users are model evaluators, AI deployment leads, and researchers who need to assess whether a proposed benchmark suite covers the capabilities relevant to their context. The toolkit requires no programming knowledge, is self-contained in a single Excel workbook with no external dependencies, and includes worked examples that demonstrate its application to three distinct deployment scenarios.

### 6.4.2 Toolkit Components

The Assessment Toolkit is implemented as a seven-tab Excel workbook (`outputs/phase5/assessment_toolkit.xlsx`) accompanied by a PDF documentation guide (`outputs/phase5/assessment_toolkit_documentation.pdf`).

**Instructions tab.** The first tab provides a step-by-step guide to using the toolkit, including prerequisites, a glossary of the key terms from the Phase 1 taxonomy and Phase 3 analysis, and a summary of how to interpret output scores.

**Capability\_Checklist tab.** This tab presents the eight capabilities from the Phase 1 taxonomy with brief plain-language descriptions and sub-category breakdowns. Users select from dropdown menus to indicate which capabilities are relevant to their deployment context and assign priority weights (High, Medium, Low, or Not Applicable) to each. The selections feed automatically into the Coverage\_Calculator.

**Benchmark\_Profiles tab.** This tab contains one row per benchmark from the Phase 2 inventory, with key fields from the benchmark database: benchmark name, abbreviation, year, primary and secondary capability codes, quality ratings across five dimensions, contamination risk level, and a brief plain-language description of what the benchmark measures and what it does not. This tab allows practitioners to review individual benchmark characteristics without accessing the full database.

**Quality\_Rubric tab.** This tab presents the five-dimension quality rubric (Coherence, Accuracy, Clarity, Relevance, Efficiency) with definitions and scoring guidance. The rubric can be used by practitioners to assess new benchmarks that are not in the Phase 2 inventory, extending the toolkit's usefulness as the benchmark landscape evolves.

**Coverage\_Calculator tab.** This tab is the computational core of the toolkit. Users input their capability priorities from the Capability\_Checklist, and the calculator automatically computes a weighted coverage score for any selection of benchmarks from the Phase 2 inventory. The formula sums the coverage matrix ratings for the selected benchmarks across the user's priority capabilities, weights them by the user's stated priority levels, and expresses the result as a proportion of the maximum possible weighted coverage. The output is a summary table showing coverage by capability and an overall weighted coverage score, allowing users to identify which capabilities in their context are well-covered and which are not.

**Worked\_Examples tab.** This tab presents three worked case studies demonstrating the toolkit in action: a medical information service use case (high priority on C03 advisory and C04 education support), a software development assistant use case (high priority on C02 and C07), and a consumer writing assistant use case (high priority on C01 and C05). For each use case, the worked example shows how capability priorities are set, which benchmarks are selected, what the coverage calculator produces, and what the outputs imply for benchmark selection and gap identification.

**Interpretation\_Guide tab.** The final tab provides guidance on reading the coverage calculator outputs: what high and low weighted coverage scores mean in practice, what limitations apply to the toolkit (the data reflects the Phase 2 inventory and Phase 3 matrix as of early 2026), and how to update the toolkit as new benchmarks are added to the inventory.

### 6.4.3 Worked Example

To illustrate the toolkit in action, the following example walks through the medical information service scenario from the Worked\_Examples tab.

A team deploying an LLM to provide general health information to the public identifies their primary capability priorities as C03 (Information Retrieval and Advisory — High priority), C04 (Learning and Education Support — Medium priority, for patient education materials), and C05 (Review and Feedback — Low priority, for reviewing draft patient communications). C01, C02, C06, C07, and C08 are marked Not Applicable.

The Coverage\_Calculator computes the weighted coverage score for a proposed benchmark suite comprising MMLU-Pro, GPQA Diamond, SimpleQA/FACTS Grounding, and LiveBench. The output shows strong coverage of C03a (factual knowledge) through MMLU-Pro and GPQA Diamond, and C03a/grounding coverage through SimpleQA/FACTS, but no coverage of the advisory dimension of C03 (contextual recommendation, uncertainty communication, safety boundary-setting) or of C04 tutoring capability. The weighted coverage score for the proposed suite is 0.44 against the user's capability profile, below the recommended threshold of 0.60.

The Interpretation\_Guide recommends that the team either supplement the proposed suite with a C03 advisory-focused benchmark (GroundedAdviceBench when available, or the closest current approximation from the inventory) or acknowledge the advisory gap explicitly in their evaluation reporting. The toolkit does not make the selection decision; it provides the evidence base for an informed decision by the practitioners.

---

## 6.5 Implementation Roadmap

The implementation roadmap translates the Phase 5 outputs into a realistic timeline for the research community, structured across three horizons.

**Short term (0–1 year).** The immediate priority is to convert the five benchmark specifications into pilot-ready artefacts. MaintBench and WorkWriteBench should be first, as they address the two largest usage-weighted gaps and have relatively tractable development timelines (3–6 months each). In the same period, GroundedAdviceBench and TutorScaffoldBench should advance to the task-schema, rubric, and pilot-split stage, with full releases following pilot validation. The deliverables for each benchmark should include a public task schema, a development split, a validation protocol, baseline model results, and dimension-level reporting templates. Concurrently, existing benchmarks should adopt the improvement recommendations from Section 6.3 where feasible: contamination risk labelling, sub-category reporting, and judge validation documentation are low-cost improvements with immediate validity benefits.

**Medium term (1–3 years).** The strongest pilots should be converted into maintained benchmarks with public development splits, private or refreshed evaluation splits, and documented inter-rater reliability. MaintBench could scale toward its full 600-task target once pilot reliability is demonstrated; WorkWriteBench could scale to its 1,000-task target with expanded annotator coverage. The research community should move toward requiring at least one benchmark per high-usage capability in frontier model technical reports, ensuring that C01, C03, and C04 — which are currently underrepresented in major model release evaluations — receive coverage equivalent to C02 and C03 knowledge benchmarks.

**Long term (3+ years).** The long-term goal is a capability-weighted benchmark ecosystem in which evaluation reports communicate model fitness for specific capability profiles rather than aggregate leaderboard positions. This requires living benchmark suites with private holdouts and regular task refreshes, community standards for LLM judge validation including calibration against human ratings and version disclosure, and benchmark reporting standards that separate capability-level performance from aggregate scores. The Assessment Toolkit provides a partial model for what this would look like in practice: a structured capability profile with weighted coverage scores, rather than a single ranking.

---

## 6.6 Limitations

Three limitations of the Phase 5 outputs are acknowledged.

The benchmark specifications are design documents, not implemented benchmarks. Their validity as evaluation instruments cannot be confirmed until they are built, piloted, and subjected to empirical validation, including inter-rater reliability testing, sensitivity analysis, and external validity checks against other benchmarks in the same capability area. The specifications are grounded in the Phase 1 taxonomy and Phase 3 analysis, but design decisions made during implementation — the exact task distribution, the scoring rubric calibration, the choice of representative repositories or domains — will require iteration beyond what can be anticipated at the design stage.

The Assessment Toolkit is based on the Phase 2 benchmark inventory and Phase 3 coverage matrix as of early 2026. As new benchmarks are published, the toolkit will require updating: new rows added to the Benchmark\_Profiles, new ratings added to the Coverage\_Calculator formula, and the Interpretation\_Guide revised to reflect changes in the availability of benchmark options. Without maintenance, the toolkit's coverage scores will become stale, and users relying on it will receive guidance that does not reflect the current evaluation landscape.

The implementation roadmap is indicative rather than binding. The timelines are based on the researcher's assessment of development feasibility given the task types, dataset sizes, and evaluation methodologies specified, but actual implementation depends on the availability of research funding, institutional support, community adoption, and continued access to the data sources and expertise required. The short-term targets for MaintBench and WorkWriteBench are achievable by a well-resourced team; they are not guaranteed outcomes of publishing the specifications.

---

## References

Balloccu, S., Schmidtová, P., Lango, M. and Dusek, O. (2024). Leak, cheat, repeat: Data contamination and evaluation malpractices in closed-source LLMs. In *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics*. Association for Computational Linguistics.

Chen, M., Tworek, J., Jun, H., Yuan, Q. and Zaremba, W. et al. (2021). Evaluating large language models trained on code. arXiv:2107.03374.

Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Henighan, T., Joseph, N., Kinniment, M., Kundu, S., McCain, J., Perez, E., Schiefer, N., Shoker, S., Sleight, H., Teplitskiy, M., Wijk, H., Clark, J., Kaplan, J., Ganguli, D. and Anthropic (2025). *Which economic tasks are performed with AI? Evidence from millions of Claude conversations*. arXiv:2503.04761.

Jacovi, A., Caciularu, A., Goldman, O. and Goldberg, Y. (2025). FACTS Grounding: A new benchmark for evaluating the factuality of large language models. arXiv:2501.03200.

Jain, N., Han, K., Gu, A., Li, W.-D., Yan, F., Zhang, T., Wang, S., Solar-Lezama, A., Sen, K. and Stoica, I. (2024). LiveCodeBench: Holistic and contamination free evaluation of large language models for code. arXiv:2403.07974.

Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O. and Narasimhan, K. (2024). SWE-bench: Can language models resolve real-world GitHub issues? arXiv:2310.06770.

Macina, J., Daheim, N., Hakimi, R., Chowdhury, S. P., Kapur, M., Gurevych, I. and Sachan, M. (2025). MathTutorBench: A benchmark for measuring open-ended pedagogical capabilities of tutoring systems. arXiv:2502.18940.

Macina, J., Daheim, N., Chowdhury, S. P., Sinha, T., Kapur, M., Gurevych, I. and Sachan, M. (2023). MathDial: A dialogue tutoring dataset with rich pedagogical properties grounded in math reasoning problems. In *Findings of EMNLP 2023*. arXiv:2311.09885.

Miserendino, S., Wang, J., Jain, S., Boisvert, A., Salemans, T., Dou, B., Allen, D., Bhatt, U., Brundage, M. and OpenAI (2025). SWE-lancer: Can frontier LLMs earn $1 million from real-world freelance software engineering? arXiv:2502.12115.

Pezeshkpour, P. and Hruschka, E. (2024). Large language models sensitivity to the order of options in multiple-choice questions. In *Findings of the Association for Computational Linguistics: NAACL 2024*. arXiv:2308.11483.

Singh, S., Stroebl, A., Kambhampati, S., Kapoor, S., Narayanan, A., Ghassemi, M. and Bommasani, R. (2025). The leaderboard illusion. arXiv:2504.20879.

Srinivasa, A., Che, P., Zhang, D., Ge, X., Wang, P., Weiss, J., Mou, C. and Scale AI (2025). TutorBench: A multisubject multimodal benchmark for evaluating AI tutoring systems. arXiv:2510.02663.

Xu, F. F., Ye, Y., Arenas, O., Yao, S. and Neubig, G. et al. (2025). TheAgentCompany: Benchmarking LLM agents on consequential real world tasks. arXiv:2412.14161.

Zhou, J., Lu, T., Mishra, S., Brahma, S., Basu, S., Luan, Y., Zhou, D. and Hou, L. (2023). Instruction-following evaluation for large language models. arXiv:2311.07911.

Zhuo, T. Y., Cassano, F., Dekoninck, J., Szafraniec, M. and Ding, B. et al. (2024). BigCodeBench: Benchmarking code generation with diverse function calls and complex instructions. arXiv:2406.15877.
