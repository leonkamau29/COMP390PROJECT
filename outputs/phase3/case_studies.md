# Phase 3 Case Studies: Benchmark Scores and Real-World Deployment Failures

**Objective:** Document real-world cases where strong benchmark performance or benchmark confidence did not translate into reliable deployment behaviour.
**Scope:** Six cases are included, exceeding the minimum acceptable three cases in the Phase 3 protocol.

## Search Strategy

Searches covered academic and industry sources for `LLM deployment failure`, `benchmark performance gap`, `AI evaluation mismatch`, medical LLM failures, legal hallucination failures, benchmark contamination, leaderboard instability, and the project core papers. The cases below prioritise sources already named in `CLAUDE.md` and additional peer-reviewed or preprint evidence where directly relevant.

## Case 1: Autonomous workplace agents complete only a minority of consequential tasks

**Model name and benchmark performance:** Frontier LLM agents evaluated in TheAgentCompany. Models report strong scores on standard frontier evaluations, but the best reported autonomous workplace completion rate in TheAgentCompany is about 30%.

**Real-world deployment context:** A simulated software-company workplace requiring agents to browse, code, communicate, and complete HR, finance, engineering, legal, and administration tasks.

**Specific failure mode observed:** Agents frequently fail long-horizon task planning, tool use, and context management despite high benchmark performance.

**Capability gap implicated:** C02, C03, and C07: technical problem solving, information retrieval, and data/document processing in integrated workflows.

**Consequences:** The result indicates that benchmark strength does not imply production readiness for autonomous work; human oversight and constrained scope remain necessary.

**Source documentation:** Xu, F. F. et al. (2025). TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks. arXiv:2412.14161.

## Case 2: Coding scores fall on post-cutoff problems, exposing contamination risk

**Model name and benchmark performance:** LLMs evaluated on LiveCodeBench and older code benchmarks. Many models perform strongly on established code benchmarks such as HumanEval, while LiveCodeBench reports performance drops on problems released after training cutoffs for some model families.

**Real-world deployment context:** Competitive-programming and code-generation tasks collected by release date from LeetCode, AtCoder, and Codeforces.

**Specific failure mode observed:** Performance on older public problems can overstate generalisation because memorised or contaminated items inflate apparent capability.

**Capability gap implicated:** C02: code development and technical problem solving under contamination-resistant, temporally controlled evaluation.

**Consequences:** Deployment decisions based on saturated coding benchmarks may overestimate reliability on new bugs, libraries, and unseen engineering tasks.

**Source documentation:** Jain, N. et al. (2024). LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code. arXiv:2403.07974.

## Case 3: Multiple-choice benchmark rankings change under answer-order perturbations

**Model name and benchmark performance:** LLMs evaluated on MMLU-style multiple-choice tasks. MMLU-style scores are widely used in model selection and leaderboard reporting.

**Real-world deployment context:** Multiple-choice factual and reasoning questions where answer options can be reordered without changing the underlying task.

**Specific failure mode observed:** Option-order sensitivity changes model scores and can shift rankings by up to eight positions, showing that leaderboard outcomes can depend on presentation artefacts.

**Capability gap implicated:** C03: information retrieval and advisory evaluation that is robust to prompt and answer-format artefacts.

**Consequences:** A model selected because of a marginal leaderboard advantage may not be more reliable in real advisory settings.

**Source documentation:** Pezeshkpour, P. and Hruschka, E. (2024). Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions. Findings of NAACL 2024.

## Case 4: Clinical decision-making failures persist despite medical benchmark success

**Model name and benchmark performance:** State-of-the-art medical LLMs and general frontier models. Medical LLMs and frontier models can achieve strong medical-exam or clinical benchmark results.

**Real-world deployment context:** Clinical decision-making over real or realistic patient cases requiring diagnosis, treatment planning, and interpretation of laboratory and contextual information.

**Specific failure mode observed:** Studies report failures in diagnostic accuracy, guideline following, patient-context adjustment, and unsafe responses to patient-posed questions.

**Capability gap implicated:** C03 and C07: advisory reasoning and context-sensitive analysis of patient information.

**Consequences:** Aggregate benchmark scores can mask patient-safety-relevant error patterns such as under-triage or unsafe advice.

**Source documentation:** Kanjee, Z. et al. (2024). Evaluation and mitigation of the limitations of large language models in clinical decision-making. Nature Medicine.

## Case 5: Legal hallucinations lead to false citations and professional sanctions

**Model name and benchmark performance:** ChatGPT and specialised legal research LLM systems. General and legal-domain LLMs can appear fluent and authoritative on legal questions.

**Real-world deployment context:** Legal research and brief drafting where users require accurate cases, quotations, and citations.

**Specific failure mode observed:** LLMs generated fictitious legal authorities and unreliable legal statements; specialised systems still hallucinated in later evaluations.

**Capability gap implicated:** C03, C05, and C01: legal information retrieval, review of generated claims, and professional document generation.

**Consequences:** False citations can mislead courts and clients, producing sanctions and undermining trust in legal AI tools.

**Source documentation:** Magesh, V. et al. (2025). Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools. arXiv:2405.20362.

## Case 6: Leaderboard disclosure practices distort model selection

**Model name and benchmark performance:** Closed-source and selectively reported model releases. Vendors report strong headline benchmark results across common leaderboards.

**Real-world deployment context:** Model-selection decisions made from public technical reports and benchmark tables.

**Specific failure mode observed:** Selective disclosure and leaderboard choices can materially distort rankings, separating reported benchmark success from actual comparative utility.

**Capability gap implicated:** Cross-cutting evaluation validity; especially C03 and C02 where organisations rely on benchmark tables for deployment choices.

**Consequences:** Practitioners may select models based on incomplete or strategically disclosed evidence rather than fit to their real use cases.

**Source documentation:** Singh, S. et al. (2025). The Leaderboard Illusion. arXiv:2504.20879.

## Cross-Case Pattern

Across these cases, the recurring problem is not that benchmarks are useless. It is that benchmark scores are often treated as general evidence of deployment reliability when they are actually evidence for a narrower task format, data distribution, scoring method, or disclosure context. Phase 3 therefore treats coverage as a capability-specific construct-validity question rather than as a count of available leaderboards.
