# Phase 2 Final Benchmark List (v3)

**Project:** Benchmark Coverage Gap — A Systematic Analysis of Real-World AI Capabilities and Evaluation Practices
**Student:** Leon Kamau Kiunga (201759400)
**Phase:** 2, Week 5
**Version:** v3 — Final list after alternatives review (May 2026)

---

## Summary

| Capability | Code | Benchmarks | Count |
|---|---|---|---|
| Code Development and Technical Problem Solving | C02 | HumanEval+, SWE-bench Verified, LiveCodeBench, BigCodeBench Hard, SWE-Lancer Diamond | 5 |
| Information Retrieval and Advisory | C03 | MMLU-Pro, GPQA Diamond, Humanity's Last Exam, SimpleQA / FACTS Grounding, LiveBench | 5 |
| Content Generation | C01 | IFEval, WritingBench, EQ-Bench Creative Writing v3, WildBench | 4 |
| Data Analysis and Summarisation | C07 | InfiAgent-DABench, DA-Code, Spider 2.0, MMLongBench-Doc | 4 |
| Learning and Education Support | C04 | MathDial, MathTutorBench, TutorBench | 3 |
| Review and Feedback | C05 | CriticBench (Tsinghua), JudgeBench, RewardBench 2 | 3 |
| Conversational Interaction and Roleplay | C08 | PingPong, CoSER | 2 |
| Translation and Language Processing | C06 | BenchMAX, WMT24++ | 2 |
| **TOTAL** | | | **28** |

> **Scope note:** The final count of 28 exceeds the original 15–20 cap. This is justified by: (a) the Phase 1 FINAL taxonomy expanding scope to all eight capabilities; (b) the alternatives review replacing several weaker benchmarks with stronger, more recent ones rather than simply adding. The 28 benchmarks span the complete C01–C08 capability space validated by the Feb 2026 AEI data. If the supervisor requires a hard cap at 20, the trimming protocol at the bottom of this document specifies which benchmarks to drop first.

---

## Decision Log: What Changed from v2 and Why

| Benchmark (v2) | Decision | Replacement / Reason |
|---|---|---|
| B001 HumanEval / HumanEval+ | **Demoted to legacy** | Saturated (>90% frontier). Retained only as a historical anchor noted in the database; not a primary coverage metric. Freed the slot for SWE-Lancer Diamond. |
| B002 MBPP / MBPP+ | **Demoted to legacy** | Same saturation issue. Dropped from primary inventory. |
| B009 HelloBench / LongBench-Write | **Dropped** | Low adoption outside authors; not cited in any frontier model report. Replaced by WildBench, which has higher Arena correlation and real-user grounding. |
| B015 TriviaQA / Natural Questions | **Demoted to legacy** | Effectively solved (>85% EM). Replaced by Humanity's Last Exam and LiveBench. |
| B019 QRData | **Dropped** | Narrower scope than InfiAgent-DABench; lower adoption. Replaced. |
| B020 Text2Analysis | **Dropped** | Superseded by DA-Code and Spider 2.0 for analytical depth and adoption. Replaced. |
| B011 MRBench | **Dropped** | Subsumed by TutorBench, which is multimodal and multi-subject. MRBench's eight pedagogical dimensions are now better covered. |
| B018 Auto-J + Shepherd + MetaCritique | **Replaced** | 2023 vintage; superseded methodologically by JudgeBench (ICLR 2025) and RewardBench 2. |
| B025 FIREBALL | **Replaced** | 2023; D&D-specific; low generalisation. Replaced by CoSER (ICML 2025), which is far broader and more recent. |
| B023 Multi-IF | **Replaced** | Absorbed by WMT24++, which covers multilingual instruction quality as part of a broader 55-language evaluation. |

---

## Full Benchmark Descriptions

### C02 — Code Development and Technical Problem Solving (5 benchmarks)

**Usage share:** 34.0% of top 103 tasks. Highest-priority capability.

---

**B001 — HumanEval / HumanEval+** *(Legacy anchor — retained in database, not a primary gap metric)*
Chen et al. (OpenAI) 2021; Liu et al. 2023. arXiv:2107.03374 / arXiv:2305.01210.
164 Python function stubs; pass@k evaluation; HumanEval+ adds 80× test cases. Retained solely to demonstrate historical saturation progression in Phase 3 temporal analysis. Frontier models exceed 90% — this benchmark no longer discriminates. Do not use as a primary coverage score input.

**B002 — SWE-bench Verified** *(Primary — agentic real-world coding)*
Jimenez et al. (Princeton/Stanford) 2024; OpenAI verification. arXiv:2310.06770.
500 human-verified real GitHub issues across 12 Python repositories; model must produce a passing code patch. Binary pass/fail via real test suites. The de-facto standard for agentic software engineering in 2025; cited in Claude 4, Gemini 2.5, GPT-4o, Llama 4, and DeepSeek R1 technical reports. Measures C02b and C02c directly.

**B003 — LiveCodeBench** *(Primary — contamination-resistant algorithmic coding)*
Jain et al. 2024. arXiv:2403.07974.
~2,000+ problems with monthly refresh from post-training-cutoff competition sources (LeetCode, AtCoder, Codeforces). Four sub-tasks: code generation, self-repair, test output prediction, code execution reasoning. Cited in Claude 4, Gemini 2.5, Llama 4 reports. Provides a temporally stable, anti-contamination signal essential for Phase 3 temporal trend analysis.

**B004 — BigCodeBench (Hard)** *(Primary — library and tool integration)*
Zhuo et al. 2024. arXiv:2406.15877.
148 hard tasks requiring real library and API calls across diverse domains. Cited in Claude 4 and Gemini 2.5 reports. Measures C02a/C02b (real-world library usage) as opposed to algorithmic puzzle-solving.

**B005 — SWE-Lancer Diamond** *(Primary — economic value and managerial judgment)*
Miserendino et al. (OpenAI) 2025. arXiv:2502.12115.
1,488 real Upwork/Expensify freelance tasks (IC SWE bug fixes + feature builds + SWE-Manager proposal selection); total payout pool US $1,000,000; Diamond subset = $500,800. End-to-end tests triple-verified by senior engineers. As of early 2026, Claude 3.5 Sonnet leads at ~26% IC SWE resolution. **Why added:** The first benchmark to attach dollar values to task completion — directly operationalises "economic impact" from the Anthropic Economic Index framing that motivates this entire project. Also the first to include managerial judgment tasks (SWE-Manager), covering C02f. No other benchmark closes this gap.

---

### C03 — Information Retrieval and Advisory (5 benchmarks)

**Usage share:** 21.4% of top 103 tasks. Second-ranked capability. Most outdated area in v2.

---

**B006 — MMLU-Pro** *(Primary — broad knowledge baseline, contamination-hardened)*
Wang et al. 2024. arXiv:2406.01574.
12,032 questions across 14 disciplines with 10 answer choices and reasoning-intensive items replacing easy factual recall. MMLU-Pro is included rather than plain MMLU because frontier models exceed 87% on MMLU, making it non-discriminating. MMLU-Pro is cited in GPT-4o, Claude 3.5/4, Gemini 2.5, Llama 4 reports. Provides the historical anchor for the C03 timeline and a broad-coverage baseline.

**B007 — GPQA Diamond** *(Primary — frontier reasoning ceiling)*
Rein et al. 2023. arXiv:2311.12022.
448 expert-validated graduate-level multiple-choice science questions (biology, chemistry, physics); gated against contamination. Present in every major 2025 frontier release table. Difficult enough that frontier models still score in the 50–75% range. The current upper-difficulty anchor for C03.

**B008 — Humanity's Last Exam (HLE)** *(Primary — the new frontier knowledge standard)*
Phan, Gatti, Han et al. (CAIS + Scale AI) 2025. arXiv:2501.14249; published *Nature*, January 2026.
2,500 public + 500 private expert-vetted questions across >100 disciplines; 24% multimodal; designed so no frontier model scored above 10% at launch. As of May 2026, the leading score is ~50% (Grok 4 Heavy, xAI). **Cited by OpenAI (GPT-5 family), Anthropic (Sonnet 4 through Opus 4.7), Google (Gemini 2.5 Pro, Gemini 3 Pro, Gemini 3 Deep Think), xAI (Grok 4 Heavy), and DeepSeek (R1, V3.1)** — the most universally adopted frontier benchmark in existence as of 2026. Replaces TriviaQA / Natural Questions as the C03 difficulty ceiling. Essential for Phase 3 gap analysis because its breadth and cross-lab adoption make it the definitive measure of C03a/C03d coverage.

**B009 — SimpleQA / FACTS Grounding** *(Primary — factuality and hallucination measurement)*
Wei et al. (OpenAI) 2024 (SimpleQA); Jacovi et al. (Google DeepMind) 2025 (FACTS Grounding). arXiv:2501.03200.
SimpleQA: 4,326 unambiguous short-answer factual questions designed to resist tools-enabled retrieval. FACTS Grounding: 860 document-grounded tasks measuring faithfulness to provided source documents. Both cited in Claude 4 and Gemini 2.0/2.5 reports. Together they cover parametric factuality (SimpleQA) and grounded factuality (FACTS) — the two dimensions of hallucination directly relevant to C03 advisory failure modes.

**B010 — LiveBench** *(Primary — contamination-limited holistic reasoning)*
White, Dooley, Roberts et al. 2024. arXiv:2406.19314. ICLR 2025 Spotlight.
18 tasks across 6 categories (Math, Reasoning, Data Analysis, Language, Coding, Instruction Following); monthly question refresh from post-cutoff sources (arXiv papers, IMDb synopses, math competitions); ground-truth automated scoring with no LLM judge bias. Top models score below 70% at launch. **Why added:** Provides a contamination-resistant, multi-domain, regularly updated signal that bridges C03 and C07. No other benchmark in the inventory is both contamination-limited by design and multi-domain; this makes it indispensable for Phase 3 temporal trend analysis.

---

### C01 — Content Generation (4 benchmarks)

**Usage share:** 17.5% of top 103 tasks. Third-ranked capability.

---

**B011 — IFEval** *(Primary — verifiable constraint-following; the one C01 benchmark all labs cite)*
Zhou et al. 2023. arXiv:2311.07911.
541 prompts with 25 types of verifiable instruction constraints (length, format, keyword). Cited in Claude 4, Gemini 2.5, Llama 4, Open LLM Leaderboard v2. Its analytical value in this project is dual: it anchors "what frontier labs actually measure in C01" and makes the proxy problem visible — a model can satisfy IFEval perfectly while completely failing at real writing tasks.

**B012 — WritingBench** *(Primary — direct multi-domain writing quality)*
Chen et al. 2025. NeurIPS 2025.
1,239 queries across 6 domains (creative, persuasive, expository, descriptive, narrative, technical) and 100 subdomains; query-dependent critic model avoids one-size-fits-all rubric problems. Not cited by any frontier technical report — which is itself the primary gap evidence for C01. The most direct and principled measure of real writing quality currently available.

**B013 — EQ-Bench Creative Writing v3** *(Primary — creative quality and live leaderboard)*
Paech 2023; v3 2025. eqbench.com.
LLM-as-judge with Elo scoring; captures character voice, emotional authenticity, narrative craft, spatial awareness, and stylistic originality. Active public leaderboard with >40 models ranked (Claude Opus 4.7 currently leads at Elo 2216). Provides the live community signal for open-ended creative generation quality absent from IFEval.

**B014 — WildBench** *(Primary — real-user task diversity)*
Lin, Deng, Chandu et al. (AI2) 2024. arXiv:2406.04770. ICLR 2025.
1,024 challenging tasks curated from one million WildChat human–chatbot conversation logs; task-specific checklists for evaluation; WB-Score achieves 0.95 Pearson correlation with Chatbot Arena Elo (surpassing Arena-Hard's 0.91). Covers writing, coding, math, role-playing, and planning from genuine user prompts. **Replaces HelloBench / LongBench-Write**, which had low adoption and no frontier report presence. WildBench's user-log origin directly parallels the Anthropic Economic Index methodology that grounds the entire project.

---

### C07 — Data Analysis and Summarisation (4 benchmarks)

**Usage share:** 10.7% of top 103 tasks. Fourth-ranked capability. Fully replaced from v2.

---

**B015 — InfiAgent-DABench** *(Primary — agentic data analysis on CSV files)*
Hu, Zhao, Wei et al. 2024. arXiv:2401.05507. ICML 2024.
DAEval: 257 questions over 52 CSV files (extended: 603 questions / 124 CSVs). Benchmarks 34 LLMs on open-ended data analysis via format-prompting. The canonical precursor cited by every subsequent data-analysis benchmark (DA-Code, DABstep, TReB). ICML 2024 provides strong venue validation. Measures C07b directly.

**B016 — DA-Code** *(Primary — agentic data science in executable environment)*
Huang, Luo, Yu et al. 2024. arXiv:2410.07331. EMNLP 2024.
500 tasks across Data Wrangling, Machine Learning, and Exploratory Data Analysis in a real Linux execution environment. Best current LLM resolves ~30.5% of tasks. **Why included:** Moves beyond Q&A over static CSVs to agentic multi-step execution — the dominant real-world C07b pattern (e.g., a user uploads a dataset and asks for a full analysis pipeline). EMNLP 2024 is a top-tier venue with strong community adoption. Measures C07b/C07d.

**B017 — Spider 2.0** *(Primary — enterprise text-to-SQL and business intelligence)*
Lei, Chen, Ye et al. 2024. arXiv:2411.07763. ICLR 2025 Oral.
Project-level enterprise SQL evaluation across BigQuery, Snowflake, Postgres, ClickHouse, DuckDB, and SQLite dialects; databases with >3,000 columns; the best agent framework resolves only 21.3% of tasks vs. 91.2% on Spider 1.0. ICLR 2025 Oral is among the highest acceptance signals in ML. **Why included:** Directly measures C07d (business intelligence and forecasting via SQL) at the enterprise scale that constitutes real-world usage. No other benchmark in the inventory covers enterprise SQL workflows.

**B018 — MMLongBench-Doc** *(Primary — long-context multimodal document understanding)*
Ma, Zang, Chen et al. 2024. arXiv:2407.01523. NeurIPS 2024 Datasets & Benchmarks Spotlight.
1,082 expert-annotated questions across 135 PDFs (average 47.5 pages, 21,214 tokens); 7 domains; 33.7% cross-page questions requiring evidence integration across text, images, charts, tables, and layout. **Why included:** READoc (v2) covered structured extraction from PDFs but was limited to layout/format conversion (C07c). MMLongBench-Doc measures the deeper task of answering questions across long multimodal documents — the dominant real-world document-processing scenario (C07a/C07b/C07c combined). NeurIPS 2024 Spotlight validates the benchmark. Replaces READoc.

---

### C04 — Learning and Education Support (3 benchmarks)

**Usage share:** 7.8% of top 103 tasks. Fifth-ranked capability.

---

**B019 — MathDial** *(Primary — foundational tutoring dialogue baseline)*
Macina et al. 2023. EMNLP 2023. arXiv:2311.09885.
2,900 student–tutor dialogues grounded in GSM8K problems. Establishes the core distinction between solving a maths problem and teaching a student to solve it. Chronologically earliest C04 benchmark; necessary for Phase 3 temporal trend analysis showing when tutoring evaluation began.

**B020 — MathTutorBench** *(Primary — comprehensive multi-task tutoring evaluation)*
Macina, Daheim, Hakimi et al. 2025. EMNLP 2025 Oral. arXiv:2502.18940.
7 pedagogical tasks (scaffolding, mistake localisation, pedagogy-following, etc.) with a pedagogy reward model and a public leaderboard. The key empirical finding — stronger mathematical solvers are sometimes worse tutors — is a central argument for the C04 gap. EMNLP 2025 Oral is the strongest acceptance signal in this area.

**B021 — TutorBench** *(Primary — multi-subject multimodal tutoring)*
Srinivasa, Che, Zhang et al. (Scale AI) 2025. arXiv:2510.02663.
1,490 expert-curated samples at high-school and AP-level across mathematics, sciences, and humanities; multimodal inputs (handwritten student work, diagrams, screenshots); scored across 3–39 rubric criteria per item using Claude Sonnet 4 as judge. All evaluated frontier models score below 60%. **Why added:** Directly addresses the math-only limitation of MathDial and MathTutorBench; covers C04b and C04c across multiple subjects and multimodal inputs — the actual scope of real-world educational support tasks. **Replaces MRBench**, which was subsumed by TutorBench's broader coverage.

---

### C05 — Review and Feedback (3 benchmarks)

**Usage share:** 3.9% of top 103 tasks. Sixth-ranked capability.

---

**B022 — CriticBench (Tsinghua)** *(Primary — critique-and-correct across reasoning domains)*
Lin et al. 2024. ACL 2024 Findings. arXiv:2402.14809.
3,825 instances across 15 datasets in 5 reasoning domains (math, commonsense, symbolic, code, algorithmic); critique-and-correct format. Its complete absence from all frontier technical reports is the primary evidence for the C05 coverage gap. Retained as the anchor benchmark for the gap argument.

**B023 — JudgeBench** *(Primary — LLM-as-judge calibration on objective correctness)*
Tan, Zhang, Zhang et al. (ScalerLab) 2024. arXiv:2410.12784. ICLR 2025.
Evaluates LLM-based judges on preference labels reflecting objective correctness (knowledge, reasoning, math, coding) rather than crowdsourced stylistic preference. Even GPT-4o performs near-random. Significantly harder than RewardBench's reasoning subset. **Why replaces Auto-J/Shepherd/MetaCritique:** Those 2023-vintage benchmarks measured whether models could generate plausible-sounding critique; JudgeBench measures whether models can correctly identify the *better* answer when both are sophisticated — a harder, more deployment-relevant task that directly maps to C05b/C05d (substantive editing and peer review). ICLR 2025 acceptance validates it.

**B024 — RewardBench 2** *(Primary — reward model and feedback quality evaluation)*
Malik, Lambert et al. (AI2) 2025. arXiv:2506.01937.
Benchmarks reward models across chat, safety, reasoning, and instruction-following; successor to the widely-cited RewardBench (arXiv:2403.13787). Now standard in RLHF and DPO alignment pipelines across labs. **Why included:** Provides the alignment-training perspective on feedback quality — directly measuring how well models produce feedback signals that improve model behaviour, which is C05's ultimate real-world function. Closes the gap left by CriticBench's purely reasoning-domain focus.

---

### C08 — Conversational Interaction and Roleplay (2 benchmarks)

**Usage share:** 2.9% in AEI; ~50% of OSS token usage (OpenRouter 2025). Seventh-ranked in AEI.

---

**B025 — PingPong** *(Primary — dynamic multi-turn roleplay with contamination resistance)*
Gusev 2024 (v4: April 2025). arXiv:2409.06820.
Three-component framework: player model (character), interrogator model (user simulator), judge ensemble (character consistency, entertainment value, language fluency); 40+ models evaluated in English and Russian; 64 conversations per model across 8 characters × 8 situations. Human annotation validation shows strong automated-human correlation. Retained from v2 because its dynamic adversarial design is the most contamination-resistant C08 evaluation methodology currently available.

**B026 — CoSER** *(Primary — large-scale authentic character roleplay)*
Wang, Wang, Zhang et al. 2025. arXiv:2502.09082. ICML 2025.
29,798 authentic conversations involving 17,966 characters from 771 books; conversation setups, character experiences, and internal thoughts; given-circumstance acting evaluation methodology; CoSER 70B matches/surpasses GPT-4o on InCharacter (75.80%) and LifeChoice (93.47%). **Why replaces FIREBALL:** FIREBALL (2023) was constrained to D&D gameplay on Discord; CoSER covers fiction, historical figures, and diverse narratives from canonical literature across all genres. ICML 2025 acceptance and the dataset's scale make it the current best-practice benchmark for C08b character roleplay.

---

### C06 — Translation and Language Processing (2 benchmarks)

**Usage share:** 1.9% of top 103 tasks. Eighth-ranked capability.

---

**B027 — BenchMAX** *(Primary — comprehensive multilingual capability evaluation)*
Huang, Zhu, Hu et al. 2025. EMNLP 2025 Findings. DOI: 10.18653/v1/2025.findings-emnlp.909.
10 diverse tasks across 16 languages; each sample post-edited by three native annotators; covers instruction following, reasoning, code generation, and long-context understanding. Finds that uneven capability utilisation across languages is not resolved by scaling alone. The most comprehensive multilingual LLM benchmark from a peer-reviewed 2025 venue.

**B028 — WMT24++** *(Primary — gold-standard translation quality across 55 languages)*
Deutsch, Freitag et al. (Google + Unbabel) 2025. arXiv:2502.12404.
Extends WMT24 General MT to 55 languages and dialects with human-written references and post-edits; literary, news, social, and speech domains; frontier LLMs (OpenAI o1, Gemini 1.5 Pro, Claude 3.5 Sonnet) are found to be the best-performing MT systems across all 55 languages by automatic metrics. **Why replaces Multi-IF:** Multi-IF measured multilingual instruction-following at the constraint level; WMT24++ measures actual translation quality at human-evaluated level across the broadest language coverage available. The WMT shared task is the annual gold standard for the MT community and the citation anchor that every translation evaluation paper references.

---

## Trimming Protocol (If Supervisor Requires Cap at 20)

If a hard cap of 20 benchmarks is required, drop in this order. Benchmarks listed first are the lowest-priority within their capability area.

| Drop order | Benchmark | Capability | Reason it can be dropped |
|---|---|---|---|
| 1 | HumanEval+ (legacy) | C02 | Already demoted to legacy; not a primary metric |
| 2 | LiveBench | C03 | Partially redundant with GPQA + HLE for reasoning; can be noted without full database entry |
| 3 | RewardBench 2 | C05 | JudgeBench + CriticBench provide sufficient C05 coverage; RewardBench 2 is supplementary |
| 4 | WildBench | C01 | EQ-Bench + WritingBench + IFEval cover C01 adequately; WildBench adds breadth but is not essential |
| 5 | DA-Code | C07 | InfiAgent-DABench + Spider 2.0 + MMLongBench-Doc cover C07 sufficiently; DA-Code adds depth but is third-priority |
| 6 | TutorBench | C04 | MathDial + MathTutorBench meet Phase 1 coverage targets; TutorBench extends to non-math but C04 is fifth-ranked |
| 7 | WMT24++ | C06 | BenchMAX alone is defensible for a C06 slot given C06's 1.9% usage share |
| 8 | CoSER | C08 | PingPong alone provides minimum viable C08 coverage given C08's rank |

Dropping items 1–8 yields exactly **20 benchmarks** while preserving full coverage of all 8 capabilities.

---

## Final Cross-Capability Alignment Table

| ID | Benchmark | Capability | Sub-categories | Venue / Year | Frontier Reports |
|---|---|---|---|---|---|
| B001 | HumanEval+ *(legacy)* | C02 | C02a, C02b | arXiv 2021/2023 | All major labs (historical) |
| B002 | SWE-bench Verified | C02 | C02b, C02c | arXiv 2024 | Claude 4, Gemini 2.5, GPT-4o, Llama 4, DeepSeek R1 |
| B003 | LiveCodeBench | C02 | C02a, C02b | arXiv 2024 | Claude 4, Gemini 2.5, Llama 4 |
| B004 | BigCodeBench Hard | C02 | C02a, C02b, C02e | arXiv 2024 | Claude 4, Gemini 2.5 |
| B005 | SWE-Lancer Diamond | C02 | C02b, C02c, C02f | arXiv 2025 (OpenAI) | OpenAI (primary) |
| B006 | MMLU-Pro | C03 | C03a, C03d | arXiv 2024 | GPT-4o, Claude 4, Gemini 2.5, Llama 4 |
| B007 | GPQA Diamond | C03 | C03a | arXiv 2023 | All 2025 frontier releases |
| B008 | Humanity's Last Exam | C03 | C03a, C03d | Nature 2026 / arXiv:2501.14249 | OpenAI, Anthropic, Google, xAI, DeepSeek |
| B009 | SimpleQA / FACTS Grounding | C03 | C03a | arXiv 2024 / 2025 | Claude 4, Gemini 2.0 |
| B010 | LiveBench | C03, C07 | C03a, C07b | arXiv 2024; ICLR 2025 Spotlight | Cross-lab leaderboard |
| B011 | IFEval | C01 | C01b, C01e | arXiv 2023 | Claude 4, Gemini 2.5, Llama 4 |
| B012 | WritingBench | C01 | C01a–C01e | NeurIPS 2025 | None (gap evidence) |
| B013 | EQ-Bench Creative Writing v3 | C01 | C01d, C01e | eqbench.com 2025 | Community leaderboard |
| B014 | WildBench | C01 | C01a–C01e | arXiv 2024; ICLR 2025 | Llama 3, Yi, open-model reports |
| B015 | InfiAgent-DABench | C07 | C07b | arXiv 2024; ICML 2024 | DA-Code, DABstep (downstream) |
| B016 | DA-Code | C07 | C07b, C07d | arXiv 2024; EMNLP 2024 | Downstream data-analysis papers |
| B017 | Spider 2.0 | C07 | C07b, C07d | arXiv 2024; ICLR 2025 Oral | Snowflake AI challenge |
| B018 | MMLongBench-Doc | C07 | C07a, C07b, C07c | arXiv 2024; NeurIPS 2024 Spotlight | Multimodal model reports |
| B019 | MathDial | C04 | C04b | EMNLP 2023 | None (gap evidence) |
| B020 | MathTutorBench | C04 | C04b, C04c | arXiv 2025; EMNLP 2025 Oral | None (gap evidence) |
| B021 | TutorBench | C04 | C04b, C04c | arXiv 2025 (Scale AI) | None (gap evidence) |
| B022 | CriticBench (Tsinghua) | C05 | C05b, C05c, C05d | ACL 2024 Findings | None (gap evidence) |
| B023 | JudgeBench | C05 | C05b, C05d | arXiv 2024; ICLR 2025 | Alignment research community |
| B024 | RewardBench 2 | C05 | C05b | arXiv 2025 (AI2) | RLHF/DPO pipeline papers |
| B025 | PingPong | C08 | C08b, C08c | arXiv 2024 (v4: 2025) | None (gap evidence) |
| B026 | CoSER | C08 | C08b, C08d | arXiv 2025; ICML 2025 | Roleplay reward-model papers |
| B027 | BenchMAX | C06 | C06a, C06b | EMNLP 2025 Findings | None (gap evidence) |
| B028 | WMT24++ | C06 | C06a | arXiv 2025 (Google/Unbabel) | MT community standard |

---

*Document version: v3 (Final)*
*Project: Benchmark Coverage Gap — Leon Kamau Kiunga (201759400)*
*Supersedes: benchmark_selection_rationale_v2.md*
