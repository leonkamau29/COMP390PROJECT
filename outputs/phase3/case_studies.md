# Phase 3 Case Studies: Benchmark Scores and Real-World Deployment Failures

In this section, I examine cases where strong benchmark performance, or confidence created by benchmark reporting, did not translate into reliable behaviour in realistic deployment settings. My aim is not to argue that benchmarks have no value. Instead, I use these examples to show why benchmark scores need to be interpreted through the capability coverage framework developed in this project.

## Search Strategy

I searched academic and industry sources using terms such as `LLM deployment failure`, `benchmark performance gap`, `AI evaluation mismatch`, medical LLM failures, legal hallucination failures, benchmark contamination, and leaderboard instability. I gave priority to sources already central to this project, especially the papers listed in `CLAUDE.md`, and I added peer-reviewed or preprint evidence where it directly supported a case.

## Case 1: Autonomous Workplace Agents Complete Only a Minority of Consequential Tasks

The first case I considered is TheAgentCompany, which evaluates frontier LLM agents in a simulated software-company workplace. Although these models are usually presented as strong performers on standard frontier evaluations, Xu et al. (2025) report that the best autonomous workplace completion rate is only about 30%. This creates a clear mismatch between general benchmark confidence and actual task completion in a realistic work setting.

The deployment context matters because the tasks require agents to browse, code, communicate, and complete work across HR, finance, engineering, legal, and administrative scenarios. In this setting, the main failure mode is not simply factual error. The agents often struggle with long-horizon planning, tool use, and context management. I therefore map this case mainly to C02, C03, and C07, because it combines technical problem solving, information retrieval, and data or document processing within integrated workflows.

For this project, the consequence is important because it shows that benchmark strength does not automatically imply production readiness for autonomous work. Human oversight, narrower task boundaries, and better workflow-specific evaluation remain necessary. The source used for this case is Xu, F. F. et al. (2025), *TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks*, arXiv:2412.14161.

## Case 2: Coding Scores Fall on Post-Cutoff Problems, Exposing Contamination Risk

The second case focuses on coding benchmarks. Many models perform strongly on established code benchmarks such as HumanEval, but LiveCodeBench shows that performance can fall on problems released after likely training cutoffs. I treat this as evidence that older public coding benchmarks can overstate generalisation when benchmark items are memorised, leaked, or too similar to training data.

The real-world context is competitive programming and code generation, using tasks collected by release date from sources such as LeetCode, AtCoder, and Codeforces. The key failure mode is inflated confidence from saturated or contaminated tasks. I map this case to C02 because it directly concerns code development and technical problem solving under contamination-resistant, temporally controlled evaluation.

The practical risk is that teams may choose models based on coding scores that do not reflect performance on new bugs, unfamiliar libraries, or unseen engineering tasks. This case supports the need for post-cutoff data, refreshed task pools, and clearer reporting of contamination risk. The source used here is Jain, N. et al. (2024), *LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code*, arXiv:2403.07974.

## Case 3: Multiple-Choice Rankings Change Under Answer-Order Perturbations

The third case concerns MMLU-style multiple-choice evaluation. These scores are widely used in leaderboards and model-selection decisions, but Pezeshkpour and Hruschka (2024) show that changing the order of answer options can shift model rankings by up to eight positions. I interpret this as a construct-validity problem because the underlying question has not changed, yet the reported performance can change materially.

The deployment context is factual and reasoning evaluation where answer options can be reordered without changing the intended task. The observed failure mode is option-order sensitivity, which means that leaderboard outcomes may partly reflect presentation artefacts rather than stable capability. I map this case to C03 because information retrieval and advisory tasks should be robust to superficial prompt and answer-format changes.

The consequence is that a model selected for a marginal leaderboard advantage may not actually be more reliable in real advisory settings. For my coverage analysis, this case supports the need to look beyond headline scores and ask whether the benchmark format measures the capability it claims to measure. The source used is Pezeshkpour, P. and Hruschka, E. (2024), *Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions*, Findings of NAACL 2024.

## Case 4: Clinical Decision-Making Failures Persist Despite Medical Benchmark Success

The fourth case looks at medical LLMs and frontier models. These systems can achieve strong results on medical exams or clinical benchmark tasks, but studies still report failures in realistic clinical decision-making. I use this case because it shows how aggregate benchmark scores can hide safety-relevant error patterns.

The deployment context involves patient cases that require diagnosis, treatment planning, interpretation of laboratory results, and attention to patient-specific context. The failure modes include diagnostic mistakes, weak guideline following, poor adjustment to patient context, and unsafe responses to patient questions. I map this case mainly to C03 and C07 because clinical use requires advisory reasoning and careful analysis of supplied patient information.

The main consequence is patient-safety risk. A model may appear competent when judged by broad medical benchmark scores while still making errors that lead to under-triage, unsafe advice, or inappropriate treatment suggestions. The source used here is Kanjee, Z. et al. (2024), *Evaluation and mitigation of the limitations of large language models in clinical decision-making*, *Nature Medicine*.

## Case 5: Legal Hallucinations Lead to False Citations and Professional Sanctions

The fifth case concerns legal research and legal drafting. General LLMs and specialised legal research systems can appear fluent and authoritative, but evaluations and real incidents show that they can generate fictitious legal authorities and unreliable legal statements. I include this case because legal work depends not only on plausible prose, but also on accurate citations, quotations, and jurisdiction-specific authority.

The real-world deployment context is legal research and brief drafting, where users need verifiable cases and accurate legal references. The main failure mode is hallucination of legal sources and claims. I map the case to C03, C05, and C01 because it combines legal information retrieval, review of generated claims, and professional document generation.

The consequences are serious because false citations can mislead courts and clients, lead to professional sanctions, and damage trust in legal AI tools. This case shows why evaluation needs to test source-grounded reliability rather than just fluent answer production. The source used is Magesh, V. et al. (2025), *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*, arXiv:2405.20362.

## Case 6: Leaderboard Disclosure Practices Distort Model Selection

The sixth case focuses on the way benchmark results are reported. Closed-source and selectively reported model releases often present strong headline results across common leaderboards, but Singh et al. (2025) show that selective disclosure and leaderboard choices can materially distort rankings. I treat this as a cross-cutting evaluation-validity issue rather than a failure of one specific capability.

The deployment context is model selection based on public technical reports and benchmark tables. The failure mode is that practitioners may see an incomplete or strategically selected evidence base and assume it represents overall model quality. This is especially relevant to C03 and C02 because organisations often rely on benchmark tables when choosing models for advisory work or technical work.

The consequence is that model-selection decisions may be based on reported benchmark strength rather than actual fit to the intended use case. This supports my decision in Phase 3 to treat benchmark coverage as a capability-specific validity question, not simply as a count of available leaderboards. The source used is Singh, S. et al. (2025), *The Leaderboard Illusion*, arXiv:2504.20879.

## Cross-Case Pattern

Across these cases, I find the same underlying pattern. Benchmarks are useful, but they are often treated as broader evidence than they can support. A score may reflect a narrow task format, a particular data distribution, a scoring method, or a selective disclosure context. For that reason, I treat Phase 3 coverage as a question of construct validity at the capability level, rather than as a simple inventory of benchmark names.