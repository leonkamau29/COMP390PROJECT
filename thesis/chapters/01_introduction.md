# Chapter 1: Introduction

**Target length:** 1,500–2,000 words
**Content source:** Problem statement, research objectives, contributions

---

## 1.1 Background and Motivation

Large language models (LLMs) have moved rapidly from research prototypes to deployed tools used by millions of people across professional, educational, and personal contexts. This transition has generated a pressing practical question: how well do the evaluation frameworks developed by the research community actually reflect what users ask these models to do?

The dominant answer, reflected in press releases, model documentation, and public leaderboards, has been to cite performance on standardised benchmarks. Models are reported to achieve high scores on the Massive Multitask Language Understanding benchmark (Hendrycks et al., 2021), on competitive programming tasks such as HumanEval and LiveCodeBench (Jain et al., 2024), and on mathematical reasoning datasets. These scores are widely used to compare models, to justify deployment decisions, and to direct research investment toward particular capability areas. Yet a growing body of evidence suggests that strong benchmark performance does not reliably translate to strong performance on the tasks that users actually bring to these systems.

Handa et al. (2025) analysed approximately four million Claude.ai conversations mapped to occupational task categories drawn from the O\*NET Detailed Work Activities database. Their analysis revealed that technical assistance accounts for approximately 65.1% of real-world usage, reviewing and improving existing work accounts for 58.9%, information retrieval accounts for 16.6%, and summarisation accounts for 16.6%. Critically, reviewing work — the second most common pattern of use — has no dedicated evaluation framework. Users regularly ask models to edit drafts, provide structured feedback on code or writing, and improve the quality of existing content, yet the benchmark ecosystem provides almost no standardised means of measuring how well models perform these tasks.

This disconnect has practical consequences. Xu et al. (2025) demonstrate in the TheAgentCompany benchmark that state-of-the-art models, despite strong performance on standard evaluations, complete only approximately 30% of autonomous workplace tasks. Singh et al. (2025) document systematic selective disclosure of benchmark results, showing that published leaderboard rankings are distorted by up to 112 positions when all results rather than selected subsets are considered. Pezeshkpour and Hruschka (2024) show that simply changing the order of answer options in multiple-choice questions shifts model rankings by approximately eight positions, revealing sensitivity to format rather than genuine capability. Balloccu et al. (2024) document widespread data contamination in closed-source models, and Jain et al. (2024) show that model performance on programming problems drops sharply after training cutoff dates, providing evidence that strong scores often reflect memorisation rather than generalisation.

Together, these findings motivate a systematic investigation into the gap between what benchmarks measure and what users need. Despite substantial individual evidence of misalignment, no existing study provides a comprehensive, usage-weighted map of the entire benchmark ecosystem that quantifies where coverage gaps are most severe and most consequential. This thesis addresses that gap.

---

## 1.2 Problem Statement

The central problem addressed in this thesis is the systematic misalignment between LLM evaluation practice and empirically documented patterns of real-world use. Standard benchmarks measure a narrow and historically determined set of capabilities — predominantly multiple-choice knowledge recall, algorithmic coding, and formal mathematical reasoning — while real users employ LLMs for a broader range of tasks that resist easy operationalisation, such as reviewing and improving content, providing grounded advisory responses, and supporting learning across diverse domains.

This misalignment is not merely an academic concern. When evaluation frameworks do not reflect use, research investment flows toward capabilities that score well on benchmarks rather than capabilities that matter most in deployment. Model selection decisions based on benchmark rankings may not identify the best model for a given practical purpose. Failure modes in deployed systems go undetected until they manifest as real-world errors with real-world consequences.

The specific gap in the literature that this project addresses is the absence of a systematic, empirically grounded, usage-weighted analysis of benchmark coverage across the full range of documented real-world LLM capabilities. Existing critiques of individual benchmarks are numerous and well-founded, but they do not provide the kind of comprehensive diagnostic that practitioners and researchers would need to understand where the evaluation ecosystem as a whole is most deficient and what new benchmarks should be prioritised.

---

## 1.3 Research Objectives

This project pursues nine specific objectives designed to produce a complete empirical account of the benchmark coverage gap and actionable recommendations for closing it.

**O1:** Build an empirically grounded capability taxonomy derived from real-world LLM usage data, covering a minimum of 95% of documented usage patterns and validated through inter-coder reliability analysis (target Cohen's κ > 0.8).

**O2:** Compile a standardised inventory of 15–20 major LLM benchmarks spanning 4–5 capability areas, with complete structured metadata for each benchmark including task format, evaluation metrics, dataset characteristics, quality ratings across five dimensions, and contamination risk assessments.

**O3:** Map all benchmarks to all capabilities in the taxonomy through a structured coverage matrix, with justified quality ratings for each benchmark-capability pairing.

**O4:** Quantify benchmark coverage gaps using a usage-weighted gap score formula that accounts for both the frequency with which each capability is used in practice and the quality and quantity of existing evaluation coverage.

**O5:** Conduct qualitative deep-dive analysis for a selection of capabilities spanning the coverage spectrum, examining the evaluation landscape, the technical challenges to measurement, the real-world consequences of inadequate evaluation, and requirements for adequate coverage.

**O6:** Validate the framework and findings through structured surveys with five to ten AI researchers and practitioners, using quantitative Likert-scale analysis and qualitative thematic analysis of open-ended responses.

**O7:** Produce three to five detailed benchmark design specifications targeting the highest-priority identified gaps, each including worked example items, dataset composition plans, evaluation methodology, validation strategies, and implementation requirements.

**O8:** Build a reusable Assessment Toolkit comprising an Excel workbook and PDF documentation enabling practitioners to evaluate benchmark relevance for their specific use case.

**O9:** Write and submit a complete thesis reporting all phases of this research.

---

## 1.4 Contributions

This thesis makes four contributions to the literature on LLM evaluation.

**First**, it provides the first comprehensive, empirically grounded capability taxonomy for real-world LLM use derived through systematic thematic analysis of usage data from multiple large-scale sources. The taxonomy identifies eight core capabilities — Content Generation (C01), Code Development and Technical Problem Solving (C02), Information Retrieval and Advisory (C03), Learning and Education Support (C04), Review and Feedback (C05), Translation and Language Processing (C06), Data Analysis and Summarisation (C07), and Conversational Interaction and Roleplay (C08) — that together cover 100% of the top tasks identified in the Anthropic Economic Index (Handa et al., 2025). The taxonomy is validated with a Cohen's κ of 1.00 and provides formal definitions, decision rules, and worked examples that enable consistent application in future research.

**Second**, it provides a systematically constructed benchmark inventory of 28 major LLM benchmarks with complete structured metadata and justified quality ratings across five dimensions: coherence, accuracy, clarity, relevance, and efficiency. The inventory is the first to map benchmarks explicitly to a usage-derived capability taxonomy rather than to researcher-defined categories, and it documents contamination risk, update frequency, and real-world applicability for each entry.

**Third**, it provides the first usage-weighted quantitative analysis of benchmark coverage gaps across all documented LLM use capabilities. The analysis demonstrates through chi-square testing that benchmark coverage is not distributed in proportion to usage frequency (χ² = 31.96, p < 0.001), and identifies Code Development and Technical Problem Solving (gap score 0.2307), Content Generation (0.2202), and Information Retrieval and Advisory (0.1453) as the three most urgent gaps. Contrary to the expectation drawn from prior literature that Review and Feedback would emerge as the primary gap, the analysis reveals that the highest-usage capabilities remain under-evaluated in absolute terms even where they have the most benchmarks, because the volume of real-world demand outstrips available evaluation coverage.

**Fourth**, it provides actionable design specifications for five new benchmarks — MaintBench, WorkWriteBench, GroundedAdviceBench, TutorScaffoldBench, and DataPipelineBench — and a reusable Assessment Toolkit that practitioners can apply to evaluate benchmark portfolios for their specific deployment contexts. These outputs are intended to be practically useful to the research community beyond the immediate scope of this project.

---

## 1.5 Thesis Structure

The remainder of this thesis is organised as follows.

Chapter 2 reviews the background literature on LLM evaluation, covering the development and critique of major benchmarks, empirical studies of real-world LLM use, and existing taxonomies of model capabilities. It situates this project within the broader discourse on evaluation validity and the gap between benchmark performance and practical utility.

Chapter 3 describes the research design and methodology, covering the five sequential research phases, the justification for methodological choices including the application of Braun and Clarke's (2006) six-phase thematic analysis and the quantitative gap score formula, and the ethical framework governing the expert validation phase.

Chapter 4 presents the implementation and results for the three core analytical phases: the development and validation of the eight-capability taxonomy (Phase 1), the systematic benchmark inventory (Phase 2), and the coverage matrix, gap score analysis, statistical testing, deep-dive analyses, and case studies (Phase 3).

Chapter 5 presents the testing and evaluation of the project outputs: the expert validation survey (Phase 4), including quantitative and qualitative analysis of responses and framework revisions made in response to feedback, and the pilot testing of the Assessment Toolkit.

Chapter 6 presents the recommendations outputs (Phase 5): the five benchmark design specifications targeting the highest-priority gaps and the Assessment Toolkit, with discussion of the implementation roadmap.

Chapter 7 addresses project ethics, covering data source ethics, the human participants protocol, data management, UK GDPR compliance, and AI tool use disclosure.

Chapter 8 concludes the thesis with a summary of findings, a review of each research objective, contributions to knowledge, consolidated limitations, and directions for future work.

Chapter 9 addresses the BCS Criteria and provides a critical self-reflection on the project process and outcomes.

---

## References

Balloccu, S., Schmidtová, P., Lango, M. and Dusek, O. (2024). Leak, cheat, repeat: Data contamination and evaluation malpractices in closed-source LLMs. In *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics*. Association for Computational Linguistics.

Braun, V. and Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), pp. 77–101.

Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Henighan, T., Joseph, N., Kinniment, M., Kundu, S., McCain, J., Perez, E., Schiefer, N., Shoker, S., Sleight, H., Teplitskiy, M., Wijk, H., Clark, J., Kaplan, J., Ganguli, D. and Anthropic (2025). *Which economic tasks are performed with AI? Evidence from millions of Claude conversations*. arXiv:2503.04761.

Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D. and Steinhardt, J. (2021). Measuring massive multitask language understanding. In *Proceedings of the 9th International Conference on Learning Representations*. arXiv:2009.03300.

Jain, N., Han, K., Gu, A., Li, W.-D., Yan, F., Zhang, T., Wang, S., Solar-Lezama, A., Sen, K. and Stoica, I. (2024). LiveCodeBench: Holistic and contamination free evaluation of large language models for code. arXiv:2403.07974.

Pezeshkpour, P. and Hruschka, E. (2024). Large language models sensitivity to the order of options in multiple-choice questions. *arXiv preprint*.

Singh, S., Stroebl, A., Kambhampati, S., Kapoor, S., Narayanan, A., Ghassemi, M. and Bommasani, R. (2025). The leaderboard illusion. arXiv:2504.20879.

Xu, F. F., Ye, Y., Arenas, O., Yao, S., Bairi, R., Bishop, J., Budzianowski, P., Carroll, M., Chen, L., Chen, Y., Chu, Z., Corea, F., Ding, H., Du, Y., Gu, K., Gupta, S., Hendryx, S., Hira, K., Huang, C., Huang, T., Joshi, P., Kabirzadeh, M., Kang, A., Kapoor, A., Katara, P., Kirk, A., Kulzhabayev, T., Lan, N., Larsen, J., Liu, L., Liu, X., Liu, Y., Ma, M., Ma, T., Mounsaveng, S., Nguyen, T., Ni, J., Shan, K., Shi, H., Srivastava, S., Su, K., Thavamani, T., Verma, P., Wang, Z., Webb, S., Wu, L., Xia, R., Xie, J., Yang, X., Zhang, C., Zhang, J., Zhang, K., Zhao, Y., Zhong, V., Zhu, K. and Neubig, G. (2025). TheAgentCompany: Benchmarking LLM agents on consequential real world tasks. arXiv:2412.14161.
