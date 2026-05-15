# Benchmark Selection Rationale (v3)

**Project:** Benchmark Coverage Gap — A Systematic Analysis of Real-World AI Capabilities and Evaluation Practices
**Student:** Leon Kamau Kiunga (201759400)
**Phase:** 2, Week 5
**Revised:** May 2026 — updated to reflect Phase 1 FINAL taxonomy (Feb 2026 AEI data), expanded benchmark inventory, and alternatives review replacing weaker benchmarks with stronger, more recent ones

---

## Selection Criteria

All included benchmarks must meet ALL three of the following:

1. **Publicly documented** — a paper or technical report must be available (arXiv, ACL Anthology, conference proceedings, or official technical blog).
2. **Multi-lab adoption** — cited or used by ≥2 major labs or research organisations OR selected to directly represent an underserved capability gap with documented evidence of absence from frontier reports.
3. **Taxonomy alignment** — must test at least one capability identified in the Phase 1 FINAL taxonomy (C01–C08, validated against Anthropic AEI Feb 2026 top-103 tasks).

> **Scope:** 15–20 benchmarks across 4–5 capability areas per supervisor feedback (revised down from 40–50). The revised Phase 1 taxonomy, grounded in the February 2026 Anthropic Economic Index update, redistributes usage shares across eight capabilities. This revision upgrades three previously deprioritised capabilities — C06 Translation and Language Processing, C07 Data Analysis and Summarisation, and C08 Conversational Interaction and Roleplay — to warranted inventory slots. Final count: **28 benchmarks across 8 capability areas (C01–C08)**.
>
> **Scope note on count:** The final count of 28 exceeds the original 15–20 cap. This is justified by: (a) the Phase 1 FINAL taxonomy expanding scope to all eight capabilities; (b) the alternatives review replacing several weaker benchmarks with stronger, more recent ones rather than simply adding. The addition of C06, C07, and C08 slots, combined with these replacements, takes the inventory above the original cap. This is a deliberate, documented scope revision. Retaining these capabilities without benchmark coverage would create an internal inconsistency between the taxonomy and the inventory. The supervisor may confirm or trim this at the Phase 2 review milestone. If a hard cap of 20 is required, a trimming protocol is provided at the bottom of this document.

---

## Capability Scope Decision

The eight-capability scope is determined by the Phase 1 FINAL taxonomy, which maps directly to the Anthropic Economic Index (Handa et al., 2025; Feb 2026 update, arXiv:2503.04761), supplemented by Ouyang et al. (2025, NBER WP 34255) and OpenRouter (2025). The empirically validated distribution across the 103 top tasks is:

| Rank | Capability                                       | Code | Task Count (of 103) | % of Top 103 |
| ---- | ------------------------------------------------ | ---- | ------------------- | ------------ |
| 1    | Code Development and Technical Problem Solving   | C02  | 35                  | 34.0%        |
| 2    | Information Retrieval and Advisory               | C03  | 22                  | 21.4%        |
| 3    | Content Generation                               | C01  | 18                  | 17.5%        |
| 4    | Data Analysis and Summarisation                  | C07  | 11                  | 10.7%        |
| 5    | Learning and Education Support                   | C04  | 8                   | 7.8%         |
| 6    | Review and Feedback                              | C05  | 4                   | 3.9%         |
| 7    | Conversational Interaction and Roleplay          | C08  | 3                   | 2.9%         |
| 8    | Translation and Language Processing              | C06  | 2                   | 1.9%         |

**Key revision from v1 rationale:** The original rationale (v1) operated on a prior five-capability scope (C02, C01, C04, C03, C05) derived from an earlier AEI estimate. The February 2026 AEI update substantially revises the picture. C07 Data Analysis and Summarisation rises to 10.7% of usage — third-ranked, ahead of C04. C08 Conversational Interaction and Roleplay registers 2.9%, and C06 Translation and Language Processing registers 1.9%. All three now meet the threshold for benchmark coverage within the inventory. The five-capability scope from v1 is accordingly expanded to all eight taxonomy capabilities, with benchmark allocations proportional to usage rank and gap severity.

**Key revision from v2 rationale:** The alternatives review conducted in May 2026 identified several benchmarks in the v2 inventory that were either saturated, superseded, narrowly scoped, or lacked adoption outside their author groups. These have been replaced with stronger, more recent benchmarks as detailed in the decision log below. No benchmark was added purely to increase count; each addition directly replaced a weaker entry or filled a sub-category gap identified in Phase 1.

---

## Decision Log: What Changed from v2 and Why

| Benchmark (v2) | Decision | Replacement / Reason |
|---|---|---|
| B001 HumanEval / HumanEval+ | **Demoted to legacy; slot reallocated** | Saturated (>90% frontier). Retained only as a historical anchor noted in the database; not a primary coverage metric. Slot freed for SWE-Lancer Diamond (B005). |
| B002 MBPP / MBPP+ | **Removed from primary inventory** | Same saturation issue as HumanEval. Dropped in favour of SWE-bench Verified, which now takes the B002 slot. |
| B009 HelloBench / LongBench-Write | **Replaced** | Low adoption outside authors; not cited in any frontier model report. Replaced by WildBench (B014), which has higher Arena correlation and real-user grounding. |
| B015 TriviaQA / Natural Questions | **Replaced** | Effectively solved (>85% EM). Replaced by Humanity's Last Exam (B008) and LiveBench (B010). |
| B019 QRData | **Replaced** | Narrower scope than InfiAgent-DABench; lower adoption. Replaced by InfiAgent-DABench (B015). |
| B020 Text2Analysis | **Replaced** | Superseded by DA-Code (B016) and Spider 2.0 (B017) for analytical depth and adoption. |
| B021 READoc | **Replaced** | Limited to layout/format conversion (C07c). Replaced by MMLongBench-Doc (B018), which measures deeper question-answering across long multimodal documents. |
| B011 MRBench | **Replaced** | Subsumed by TutorBench (B021), which is multimodal and multi-subject. MRBench's eight pedagogical dimensions are now better covered. |
| B018 Auto-J + Shepherd + MetaCritique | **Replaced** | 2023 vintage; superseded methodologically by JudgeBench (B023, ICLR 2025) and RewardBench 2 (B024). |
| B025 FIREBALL | **Replaced** | 2023; D&D-specific; low generalisation. Replaced by CoSER (B026, ICML 2025), which is far broader and more recent. |
| B023 Multi-IF | **Replaced** | Absorbed by WMT24++ (B028), which covers multilingual instruction quality as part of a broader 55-language evaluation. |

---

## Inclusion Decisions

### C02 — Code Development and Technical Problem Solving (5 benchmarks: B001–B005)

**Usage share:** 34.0% of top 103 tasks. Highest-priority capability.

**B001 — HumanEval / HumanEval+** *(Legacy anchor — retained in database, not a primary gap metric)*
Included solely to demonstrate historical saturation progression in Phase 3 temporal analysis. Chen et al. (OpenAI) 2021; Liu et al. 2023. arXiv:2107.03374 / arXiv:2305.01210. 164 Python function stubs; pass@k evaluation; HumanEval+ adds 80× test cases. Despite being the most-cited C02 benchmark globally (>8,000 citations), frontier models exceed 90% — this benchmark no longer discriminates. Its saturation is itself the analytical point. Do not use as a primary coverage score input.

**B002 — SWE-bench Verified** *(Primary — agentic real-world coding)*
Jimenez et al. (Princeton/Stanford) 2024; OpenAI verification. arXiv:2310.06770. 500 human-verified real GitHub issues across 12 Python repositories; model must produce a passing code patch. Binary pass/fail via real test suites. The de-facto standard for agentic software engineering in 2025; cited in Claude 4, Gemini 2.5, GPT-4o, Llama 4, and DeepSeek R1 technical reports. **Replaces MBPP / MBPP+**, which suffered from the same saturation as HumanEval and no longer discriminates at the frontier. SWE-bench Verified measures C02b and C02c directly against real-world software tasks.

**B003 — LiveCodeBench** *(Primary — contamination-resistant algorithmic coding)*
Jain et al. 2024. arXiv:2403.07974. ~2,000+ problems with monthly refresh from post-training-cutoff competition sources (LeetCode, AtCoder, Codeforces). Four sub-tasks: code generation, self-repair, test output prediction, code execution reasoning. Cited in Claude 4, Gemini 2.5, Llama 4 reports. Provides a temporally stable, anti-contamination signal essential for Phase 3 temporal trend analysis. Satisfies all three inclusion criteria.

**B004 — BigCodeBench (Hard)** *(Primary — library and tool integration)*
Zhuo et al. 2024. arXiv:2406.15877. 148 hard tasks requiring real library and API calls across diverse domains. Cited in Claude 4 and Gemini 2.5 reports. Measures C02a/C02b (real-world library usage) as opposed to algorithmic puzzle-solving — the dominant real-world C02 activity. Satisfies all three inclusion criteria.

**B005 — SWE-Lancer Diamond** *(Primary — economic value and managerial judgment)*
Miserendino et al. (OpenAI) 2025. arXiv:2502.12115. 1,488 real Upwork/Expensify freelance tasks (IC SWE bug fixes + feature builds + SWE-Manager proposal selection); total payout pool US $1,000,000; Diamond subset = $500,800. End-to-end tests triple-verified by senior engineers. **Why added:** The first benchmark to attach dollar values to task completion — directly operationalises "economic impact" from the Anthropic Economic Index framing that motivates this entire project. Also the first to include managerial judgment tasks (SWE-Manager), covering C02f. No other benchmark closes this gap. **Replaces the HumanEval+ slot**, freed when HumanEval+ was demoted to legacy status.

**Excluded C02 candidates:** MBPP / MBPP+ (saturated; demoted in favour of SWE-bench Verified); APPS (high difficulty competitive programming; partially redundant with LiveCodeBench); DS-1000 (data science; overlaps C07); CodeContests (very high difficulty; redundant with LiveCodeBench); Aider Polyglot / Terminal-Bench (agentic; redundant with SWE-bench Verified within 5-benchmark cap).

---

### C03 — Information Retrieval and Advisory (5 benchmarks: B006–B010)

**Usage share:** 21.4% of top 103 tasks. Second-ranked capability. Most outdated area in v2.

**B006 — MMLU-Pro** *(Primary — broad knowledge baseline, contamination-hardened)*
Wang et al. 2024. arXiv:2406.01574. 12,032 questions across 14 disciplines with 10 answer choices and reasoning-intensive items replacing easy factual recall. MMLU-Pro is included rather than plain MMLU because frontier models exceed 87% on MMLU, making it non-discriminating. MMLU-Pro is cited in GPT-4o, Claude 3.5/4, Gemini 2.5, Llama 4 reports. Provides the historical anchor for the C03 timeline and a broad-coverage baseline. Satisfies all three inclusion criteria.

**B007 — GPQA Diamond** *(Primary — frontier reasoning ceiling)*
Rein et al. 2023. arXiv:2311.12022. 448 expert-validated graduate-level multiple-choice science questions (biology, chemistry, physics); gated against contamination. Present in every major 2025 frontier release table. Difficult enough that frontier models still score in the 50–75% range. The current upper-difficulty anchor for C03. Satisfies all three inclusion criteria.

**B008 — Humanity's Last Exam (HLE)** *(Primary — the new frontier knowledge standard)*
Phan, Gatti, Han et al. (CAIS + Scale AI) 2025. arXiv:2501.14249; published *Nature*, January 2026. 2,500 public + 500 private expert-vetted questions across >100 disciplines; 24% multimodal; designed so no frontier model scored above 10% at launch. As of May 2026, the leading score is ~50% (Grok 4 Heavy, xAI). Cited by OpenAI (GPT-5 family), Anthropic (Sonnet 4 through Opus 4.7), Google (Gemini 2.5 Pro, Gemini 3 Pro), xAI (Grok 4 Heavy), and DeepSeek (R1, V3.1) — the most universally adopted frontier benchmark in existence as of 2026. **Replaces TriviaQA / Natural Questions**, which are effectively solved (>85% EM) and no longer discriminate among frontier models.

**B009 — SimpleQA / FACTS Grounding** *(Primary — factuality and hallucination measurement)*
Wei et al. (OpenAI) 2024 (SimpleQA); Jacovi et al. (Google DeepMind) 2025 (FACTS Grounding). arXiv:2501.03200. SimpleQA: 4,326 unambiguous short-answer factual questions designed to resist tools-enabled retrieval. FACTS Grounding: 860 document-grounded tasks measuring faithfulness to provided source documents. Both cited in Claude 4 and Gemini 2.0/2.5 reports. Together they cover parametric factuality (SimpleQA) and grounded factuality (FACTS) — the two dimensions of hallucination directly relevant to C03 advisory failure modes. Retained from v2 unchanged.

**B010 — LiveBench** *(Primary — contamination-limited holistic reasoning)*
White, Dooley, Roberts et al. 2024. arXiv:2406.19314. ICLR 2025 Spotlight. 18 tasks across 6 categories (Math, Reasoning, Data Analysis, Language, Coding, Instruction Following); monthly question refresh from post-cutoff sources (arXiv papers, IMDb synopses, math competitions); ground-truth automated scoring with no LLM judge bias. Top models score below 70% at launch. **Why added:** Provides a contamination-resistant, multi-domain, regularly updated signal that bridges C03 and C07. No other benchmark in the inventory is both contamination-limited by design and multi-domain; this makes it indispensable for Phase 3 temporal trend analysis. **Added to fill the slot freed by TriviaQA / Natural Questions.**

**Excluded C03 candidates:** TriviaQA / Natural Questions (effectively solved; demoted); SQuAD 1.1/2.0 (saturated and superseded); HotpotQA / DROP (multi-hop reasoning; partially captured by BBH); TruthfulQA (partially redundant with SimpleQA); commonsense benchmarks (HellaSwag / WinoGrande / ARC-C) (GPQA and MMLU-Pro cover this layer more robustly for current frontier analysis).

---

### C01 — Content Generation (4 benchmarks: B011–B014)

**Usage share:** 17.5% of top 103 tasks. Third-ranked capability.

**B011 — IFEval** *(Primary — verifiable constraint-following; the one C01 benchmark all labs cite)*
Zhou et al. 2023. arXiv:2311.07911. 541 prompts with 25 types of verifiable instruction constraints (length, format, keyword). Cited in Claude 4, Gemini 2.5, Llama 4, Open LLM Leaderboard v2. Its analytical value in this project is dual: it anchors "what frontier labs actually measure in C01" and makes the proxy problem visible — a model can satisfy IFEval perfectly while completely failing at real writing tasks. Satisfies all three inclusion criteria. Retained from v2 unchanged (renumbered from B006 to B011 for cross-capability ID consistency).

**B012 — WritingBench** *(Primary — direct multi-domain writing quality)*
Chen et al. 2025. NeurIPS 2025. 1,239 queries across 6 domains (creative, persuasive, expository, descriptive, narrative, technical) and 100 subdomains; query-dependent critic model avoids one-size-fits-all rubric problems. Not cited by any frontier technical report — which is itself the primary gap evidence for C01. The most direct and principled measure of real writing quality currently available. Multi-lab adoption criterion partially waived: absence from frontier reports is the analytical point, not a disqualifier. Retained from v2 unchanged (renumbered from B007 to B012).

**B013 — EQ-Bench Creative Writing v3** *(Primary — creative quality and live leaderboard)*
Paech 2023; v3 2025. eqbench.com. LLM-as-judge with Elo scoring; captures character voice, emotional authenticity, narrative craft, spatial awareness, and stylistic originality. Active public leaderboard with >40 models ranked (Claude Opus 4.7 currently leads at Elo 2216). Provides the live community signal for open-ended creative generation quality absent from IFEval. Retained from v2 unchanged (renumbered from B008 to B013).

**B014 — WildBench** *(Primary — real-user task diversity)*
Lin, Deng, Chandu et al. (AI2) 2024. arXiv:2406.04770. ICLR 2025. 1,024 challenging tasks curated from one million WildChat human–chatbot conversation logs; task-specific checklists for evaluation; WB-Score achieves 0.95 Pearson correlation with Chatbot Arena Elo (surpassing Arena-Hard's 0.91). Covers writing, coding, math, role-playing, and planning from genuine user prompts. **Replaces HelloBench / LongBench-Write** (v2 B009), which had low adoption and no frontier report presence. WildBench's user-log origin directly parallels the Anthropic Economic Index methodology that grounds the entire project.

**Excluded C01 candidates:** HelloBench / LongBench-Write (low adoption; no frontier report presence; replaced by WildBench); MT-Bench (GPT-4-judged multi-turn; primarily C01/C03 hybrid; replaced by WritingBench + EQ-Bench); Suri (multi-constraint long-form; partially redundant with WritingBench); IFBench (harder IFEval variant; partially redundant with IFEval).

---

### C07 — Data Analysis and Summarisation (4 benchmarks: B015–B018)

**Usage share:** 10.7% of top 103 tasks. Fourth-ranked capability. Fully replaced from v2.

**Scope justification:** C07 is the fourth most common capability in the Phase 1 FINAL taxonomy, accounting for 10.7% of Anthropic's top 103 tasks. It was excluded from the v1 inventory as a consequence of the prior usage estimate (~5–7%) placing it outside the provisional top-five scope. The February 2026 AEI revision elevates C07 substantially and makes its exclusion analytically unjustifiable. The v2 benchmarks for C07 (QRData, Text2Analysis, READoc) were all replaced in the alternatives review: QRData was narrower in scope than InfiAgent-DABench; Text2Analysis was superseded by DA-Code and Spider 2.0 for analytical depth and adoption; READoc was limited to format conversion (C07c) and replaced by MMLongBench-Doc, which measures deeper question-answering across long multimodal documents. Four benchmarks now cover the full C07 sub-task range.

**B015 — InfiAgent-DABench** *(Primary — agentic data analysis on CSV files)*
Hu, Zhao, Wei et al. 2024. arXiv:2401.05507. ICML 2024. DAEval: 257 questions over 52 CSV files (extended: 603 questions / 124 CSVs). Benchmarks 34 LLMs on open-ended data analysis via format-prompting. The canonical precursor cited by every subsequent data-analysis benchmark (DA-Code, DABstep, TReB). ICML 2024 provides strong venue validation. Measures C07b directly. **Replaces QRData** (v2 B019), which had a narrower scope (411 questions) and lower community adoption. Satisfies all three inclusion criteria.

**B016 — DA-Code** *(Primary — agentic data science in executable environment)*
Huang, Luo, Yu et al. 2024. arXiv:2410.07331. EMNLP 2024. 500 tasks across Data Wrangling, Machine Learning, and Exploratory Data Analysis in a real Linux execution environment. Best current LLM resolves ~30.5% of tasks. Moves beyond Q&A over static CSVs to agentic multi-step execution — the dominant real-world C07b pattern. EMNLP 2024 is a top-tier venue with strong community adoption. Measures C07b/C07d. **Replaces Text2Analysis** (v2 B020), which was superseded by DA-Code and Spider 2.0 in analytical depth and community adoption.

**B017 — Spider 2.0** *(Primary — enterprise text-to-SQL and business intelligence)*
Lei, Chen, Ye et al. 2024. arXiv:2411.07763. ICLR 2025 Oral. Project-level enterprise SQL evaluation across BigQuery, Snowflake, Postgres, ClickHouse, DuckDB, and SQLite dialects; databases with >3,000 columns; the best agent framework resolves only 21.3% of tasks vs. 91.2% on Spider 1.0. ICLR 2025 Oral is among the highest acceptance signals in ML. Directly measures C07d (business intelligence and forecasting via SQL) at the enterprise scale that constitutes real-world usage. No other benchmark in the inventory covers enterprise SQL workflows. Satisfies all three inclusion criteria.

**B018 — MMLongBench-Doc** *(Primary — long-context multimodal document understanding)*
Ma, Zang, Chen et al. 2024. arXiv:2407.01523. NeurIPS 2024 Datasets & Benchmarks Spotlight. 1,082 expert-annotated questions across 135 PDFs (average 47.5 pages, 21,214 tokens); 7 domains; 33.7% cross-page questions requiring evidence integration across text, images, charts, tables, and layout. **Replaces READoc** (v2 B021). READoc was limited to structured extraction from PDFs (C07c). MMLongBench-Doc measures the deeper task of answering questions across long multimodal documents — the dominant real-world document-processing scenario (C07a/C07b/C07c combined). NeurIPS 2024 Spotlight validates the benchmark.

**Excluded C07 candidates:** QRData (narrower scope than InfiAgent-DABench; lower adoption; replaced); Text2Analysis (superseded by DA-Code and Spider 2.0; replaced); READoc (limited to format conversion; replaced by MMLongBench-Doc); SummEval (summarisation quality; covered at the sub-task level by MMLongBench-Doc and partially by WritingBench; omitted under scope management); FABLES (narrative summarisation; niche sub-task; omitted); DS-1000 (data science code generation; C02/C07 hybrid; excluded to maintain C02 boundary); TAT-QA (tabular QA; partially redundant with InfiAgent-DABench).

---

### C04 — Learning and Education Support (3 benchmarks: B019–B021)

**Usage share:** 7.8% of top 103 tasks. Fifth-ranked capability.

**B019 — MathDial** *(Primary — foundational tutoring dialogue baseline)*
Macina et al. 2023. EMNLP 2023. arXiv:2311.09885. 2,900 student–tutor dialogues grounded in GSM8K problems. Establishes the core distinction between solving a maths problem and teaching a student to solve it — the foundation of the C04 gap argument. Chronologically earliest C04 benchmark; necessary for Phase 3 temporal trend analysis showing when tutoring evaluation began. Retained from v2 unchanged (renumbered from B010 to B019).

**B020 — MathTutorBench** *(Primary — comprehensive multi-task tutoring evaluation)*
Macina, Daheim, Hakimi et al. 2025. EMNLP 2025 Oral. arXiv:2502.18940. 7 pedagogical tasks (scaffolding, mistake localisation, pedagogy-following, etc.) with a pedagogy reward model and a public leaderboard. The key empirical finding — stronger mathematical solvers are sometimes worse tutors — is a central argument for the C04 gap. EMNLP 2025 Oral is the strongest acceptance signal in this area. Retained from v2 (renumbered from B012 to B020; previously listed third, now listed second to reflect chronological and coverage logic).

**B021 — TutorBench** *(Primary — multi-subject multimodal tutoring)*
Srinivasa, Che, Zhang et al. (Scale AI) 2025. arXiv:2510.02663. 1,490 expert-curated samples at high-school and AP-level across mathematics, sciences, and humanities; multimodal inputs (handwritten student work, diagrams, screenshots); scored across 3–39 rubric criteria per item using Claude Sonnet 4 as judge. All evaluated frontier models score below 60%. Directly addresses the math-only limitation of MathDial and MathTutorBench; covers C04b and C04c across multiple subjects and multimodal inputs — the actual scope of real-world educational support tasks. **Replaces MRBench** (v2 B011), which was subsumed by TutorBench's broader multi-subject and multimodal coverage. Multi-lab adoption criterion partially waived: absence from frontier reports is the analytical point, consistent with the overall C04 gap evidence.

**Excluded C04 candidates:** MRBench (subsumed by TutorBench's broader coverage; replaced); Bridge (elementary-school remediation; narrower scope than MathDial); KMP-Bench (2026 publication; very new; limited adoption); math-solving benchmarks (GSM8K, MATH, AIME) (measure C04 output, not C04 pedagogy; included under C03 if relevant).

---

### C05 — Review and Feedback (3 benchmarks: B022–B024)

**Usage share:** 3.9% of top 103 tasks. Sixth-ranked capability.

**B022 — CriticBench (Tsinghua)** *(Primary — critique-and-correct across reasoning domains)*
Lin et al. 2024. ACL 2024 Findings. arXiv:2402.14809. 3,825 instances across 15 datasets in 5 reasoning domains (math, commonsense, symbolic, code, algorithmic); critique-and-correct format. Its complete absence from all frontier technical reports is the primary evidence for the C05 coverage gap. Retained as the anchor benchmark for the gap argument. Retained from v2 unchanged (renumbered from B017 to B022).

**B023 — JudgeBench** *(Primary — LLM-as-judge calibration on objective correctness)*
Tan, Zhang, Zhang et al. (ScalerLab) 2024. arXiv:2410.12784. ICLR 2025. Evaluates LLM-based judges on preference labels reflecting objective correctness (knowledge, reasoning, math, coding) rather than crowdsourced stylistic preference. Even GPT-4o performs near-random. Significantly harder than RewardBench's reasoning subset. **Replaces Auto-J + Shepherd + MetaCritique** (v2 B018). Those 2023-vintage benchmarks measured whether models could generate plausible-sounding critique; JudgeBench measures whether models can correctly identify the *better* answer when both are sophisticated — a harder, more deployment-relevant task that directly maps to C05b/C05d. ICLR 2025 acceptance validates it.

**B024 — RewardBench 2** *(Primary — reward model and feedback quality evaluation)*
Malik, Lambert et al. (AI2) 2025. arXiv:2506.01937. Benchmarks reward models across chat, safety, reasoning, and instruction-following; successor to the widely-cited RewardBench (arXiv:2403.13787). Now standard in RLHF and DPO alignment pipelines across labs. Provides the alignment-training perspective on feedback quality — directly measuring how well models produce feedback signals that improve model behaviour, which is C05's ultimate real-world function. Closes the gap left by CriticBench's purely reasoning-domain focus. **Added to replace the analytical gap left by dropping Auto-J/Shepherd/MetaCritique**, bringing C05 to three benchmarks with distinct sub-capability coverage.

**Excluded C05 candidates:** Auto-J + Shepherd + MetaCritique (2023 vintage; superseded by JudgeBench and RewardBench 2; replaced); CriticBench (Tencent) (redundant with Tsinghua version; Tsinghua preferred for broader domain coverage); CritiqueLLM / UltraCM (critique-tuned models rather than benchmarks per se); GEC benchmarks (CoNLL-2014 / JFLEG / BEA-2019) (narrow grammatical error-correction proxy; does not capture argumentative, structural, or stylistic feedback dimensions central to C05b–C05d).

---

### C08 — Conversational Interaction and Roleplay (2 benchmarks: B025–B026)

**Usage share:** 2.9% in AEI; ~50% of OSS token usage (OpenRouter 2025). Seventh-ranked in AEI.

**Scope justification:** C08 accounts for 2.9% of Anthropic's top 103 tasks in the Phase 1 FINAL taxonomy (tasks include: relationship, dating, parenting and personal advice dialogue; job interview practice and professional scenario roleplay; and mental health and ADHD support resources). While 2.9% represents a modest share of the AEI enterprise-oriented dataset, the OpenRouter (2025) data shows that roleplay and interactive fiction constitutes approximately 50% of open-source model token usage. The C08 coverage gap is therefore particularly severe when evaluated against the broader deployment context. Additionally, the absence of any C08 benchmark from frontier technical reports constitutes strong gap evidence.

**B025 — PingPong** *(Primary — dynamic multi-turn roleplay with contamination resistance)*
Gusev 2024 (v4: April 2025). arXiv:2409.06820. Three-component framework: player model (character), interrogator model (user simulator), judge ensemble (character consistency, entertainment value, language fluency); 40+ models evaluated in English and Russian; 64 conversations per model across 8 characters × 8 situations. Human annotation validation shows strong automated-human correlation. Retained from v2 because its dynamic adversarial design is the most contamination-resistant C08 evaluation methodology currently available (renumbered from B024 to B025).

**B026 — CoSER** *(Primary — large-scale authentic character roleplay)*
Wang, Wang, Zhang et al. 2025. arXiv:2502.09082. ICML 2025. 29,798 authentic conversations involving 17,966 characters from 771 books; conversation setups, character experiences, and internal thoughts; given-circumstance acting evaluation methodology; CoSER 70B matches/surpasses GPT-4o on InCharacter (75.80%) and LifeChoice (93.47%). **Replaces FIREBALL** (v2 B025). FIREBALL (2023) was constrained to D&D gameplay on Discord; CoSER covers fiction, historical figures, and diverse narratives from canonical literature across all genres. ICML 2025 acceptance and the dataset's scale make it the current best-practice benchmark for C08b character roleplay.

**Excluded C08 candidates:** FIREBALL (2023; D&D-specific; low generalisation; replaced by CoSER); MT-Bench (primarily C01/C03 multi-turn quality; not C08-specific); PersonaGym (persona assessment; QA-based rather than dialogue-based; does not capture sustained interactive exchange); CharacterEval (character fidelity in Chinese; scope limited to Chinese language; C06 complication); EmpathyBench-type benchmarks (empathetic response; too narrow for C08 full coverage — covers only C08a).

---

### C06 — Translation and Language Processing (2 benchmarks: B027–B028)

**Usage share:** 1.9% of top 103 tasks. Eighth-ranked capability.

**Scope justification:** C06 accounts for 1.9% of Anthropic's top 103 tasks in the Phase 1 FINAL taxonomy (two tasks: language-learning assistance with translation and grammar help; professional, academic, medical and religious content translation between languages). While this is the smallest capability by task count, it is meaningfully distinct from all other capabilities and directly matched to tasks in the empirical usage data. Moreover, translation represents a high-volume, high-stakes real-world use case (professional document translation, multilingual communication) that warrants independent benchmark assessment. Two benchmarks are allocated: one for multilingual capability evaluation spanning multiple tasks and languages (C06a/C06b), one for gold-standard translation quality across the broadest language coverage available (C06a).

**B027 — BenchMAX** *(Primary — comprehensive multilingual capability evaluation)*
Huang, Zhu, Hu et al. 2025. EMNLP 2025 Findings. DOI: 10.18653/v1/2025.findings-emnlp.909. 10 diverse tasks (including instruction following, reasoning, code generation, and long-context understanding) across 16 languages; each sample post-edited by three native annotators. Its finding that uneven capability utilisation across languages is not resolved by scaling alone directly supports the Phase 3 argument about benchmark gaps in non-English contexts. The most comprehensive multilingual LLM benchmark from a peer-reviewed 2025 venue. Retained from v2 unchanged (renumbered from B022 to B027).

**B028 — WMT24++** *(Primary — gold-standard translation quality across 55 languages)*
Deutsch, Freitag et al. (Google + Unbabel) 2025. arXiv:2502.12404. Extends WMT24 General MT to 55 languages and dialects with human-written references and post-edits; literary, news, social, and speech domains; frontier LLMs (OpenAI o1, Gemini 1.5 Pro, Claude 3.5 Sonnet) are found to be the best-performing MT systems across all 55 languages by automatic metrics. The WMT shared task is the annual gold standard for the MT community and the citation anchor that every translation evaluation paper references. **Replaces Multi-IF** (v2 B023). Multi-IF measured multilingual instruction-following at the constraint level; WMT24++ measures actual translation quality at human-evaluated level across the broadest language coverage available — a more direct and comprehensive measure of C06a.

**Excluded C06 candidates:** Multi-IF (replaced by WMT24++, which covers multilingual instruction quality as part of a broader 55-language evaluation); FLORES-101 / FLORES+ (translation quality; covers primarily MT system evaluation rather than LLM-as-translator assessment; relevant but more specialised than BenchMAX for LLM evaluation purposes); standard MT metrics (BLEU/COMET) (metrics, not benchmarks per se).

---

## Benchmark Count Distribution (v3)

| Capability                                     | Code | Count | Reasoning for allocation |
| ---------------------------------------------- | ---- | ----- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Code Development and Technical Problem Solving | C02  | 5     | Highest usage share; saturated benchmark space requires multiple benchmarks to characterise the coverage landscape (B001–B005) |
| Information Retrieval and Advisory             | C03  | 5     | Second-highest; saturation of prior benchmarks (TriviaQA/NQ) and hallucination measurement require additional anchors; LiveBench added (B006–B010) |
| Content Generation                             | C01  | 4     | Third-highest; major gap with only 1 consensus benchmark (IFEval) means 3 gap-illustrating alternatives needed (B011–B014) |
| Data Analysis and Summarisation                | C07  | 4     | Fourth-highest (10.7%); entirely absent from frontier reports; 4 benchmarks now cover C07a–C07d with stronger, more recent entries (B015–B018) |
| Learning and Education Support                 | C04  | 3     | Fifth-highest; entirely absent from frontier reports; 3 benchmarks illustrate the gap across foundational / comprehensive / multimodal levels (B019–B021) |
| Review and Feedback                            | C05  | 3     | Sixth-highest; zero frontier report presence; 3 benchmarks replace the single 2023-vintage grouped entry with two more recent, methodologically stronger benchmarks (B022–B024) |
| Conversational Interaction and Roleplay        | C08  | 2     | Seventh-highest in AEI but dominant in OSS usage (~50% token share per OpenRouter 2025); zero frontier report presence (B025–B026) |
| Translation and Language Processing            | C06  | 2     | Eighth-highest; zero dedicated frontier evaluation; 2 benchmarks cover multilingual quality and translation quality across 55 languages (B027–B028) |
| **Total**                                      | —    | **28**| Expanded from 25 to 28 through alternatives review: 10 benchmarks replaced (not added), plus 3 net new entries filling sub-capability gaps |

---

## Trimming Protocol (If Supervisor Requires Cap at 20)

If a hard cap of 20 benchmarks is required, drop in this order. Benchmarks listed first are the lowest-priority within their capability area.

| Drop order | Benchmark | Capability | Reason it can be dropped |
|---|---|---|---|
| 1 | HumanEval+ (legacy) B001 | C02 | Already demoted to legacy; not a primary metric |
| 2 | LiveBench B010 | C03 | Partially redundant with GPQA + HLE for reasoning; can be noted without full database entry |
| 3 | RewardBench 2 B024 | C05 | JudgeBench + CriticBench provide sufficient C05 coverage; RewardBench 2 is supplementary |
| 4 | WildBench B014 | C01 | EQ-Bench + WritingBench + IFEval cover C01 adequately; WildBench adds breadth but is not essential |
| 5 | DA-Code B016 | C07 | InfiAgent-DABench + Spider 2.0 + MMLongBench-Doc cover C07 sufficiently; DA-Code adds depth but is third-priority |
| 6 | TutorBench B021 | C04 | MathDial + MathTutorBench meet Phase 1 coverage targets; TutorBench extends to non-math but C04 is fifth-ranked |
| 7 | WMT24++ B028 | C06 | BenchMAX alone is defensible for a C06 slot given C06's 1.9% usage share |
| 8 | CoSER B026 | C08 | PingPong alone provides minimum viable C08 coverage given C08's rank |

Dropping items 1–8 yields exactly **20 benchmarks** while preserving full coverage of all 8 capabilities.

---

## Cross-Capability Alignment with Phase 1 FINAL Taxonomy

The following table maps each benchmark to its primary taxonomy capability and the relevant Phase 1 sub-categories it exercises. This alignment was verified against the capability definitions and decision rules in `outputs/phase1/capability_taxonomy_FINAL.md`.

| Benchmark ID | Name (abbreviated) | Primary Capability | Phase 1 Sub-categories Exercised |
| ------------ | ------------------ | ------------------ | --------------------------------- |
| B001         | HumanEval+ *(legacy)* | C02           | C02a, C02b                        |
| B002         | SWE-bench Verified | C02                | C02b, C02c                        |
| B003         | LiveCodeBench      | C02                | C02a, C02b                        |
| B004         | BigCodeBench Hard  | C02                | C02a, C02b, C02e                  |
| B005         | SWE-Lancer Diamond | C02                | C02b, C02c, C02f                  |
| B006         | MMLU-Pro           | C03                | C03a, C03d                        |
| B007         | GPQA Diamond       | C03                | C03a                              |
| B008         | Humanity's Last Exam | C03              | C03a, C03d                        |
| B009         | SimpleQA / FACTS Grounding | C03      | C03a                              |
| B010         | LiveBench          | C03, C07           | C03a, C07b                        |
| B011         | IFEval             | C01                | C01b, C01e                        |
| B012         | WritingBench       | C01                | C01a–C01e                         |
| B013         | EQ-Bench Creative Writing v3 | C01   | C01d, C01e                        |
| B014         | WildBench          | C01                | C01a–C01e                         |
| B015         | InfiAgent-DABench  | C07                | C07b                              |
| B016         | DA-Code            | C07                | C07b, C07d                        |
| B017         | Spider 2.0         | C07                | C07b, C07d                        |
| B018         | MMLongBench-Doc    | C07                | C07a, C07b, C07c                  |
| B019         | MathDial           | C04                | C04b                              |
| B020         | MathTutorBench     | C04                | C04b, C04c                        |
| B021         | TutorBench         | C04                | C04b, C04c                        |
| B022         | CriticBench (Tsinghua) | C05           | C05b, C05c, C05d                  |
| B023         | JudgeBench         | C05                | C05b, C05d                        |
| B024         | RewardBench 2      | C05                | C05b                              |
| B025         | PingPong           | C08                | C08b, C08c                        |
| B026         | CoSER              | C08                | C08b, C08d                        |
| B027         | BenchMAX           | C06                | C06a, C06b                        |
| B028         | WMT24++            | C06                | C06a                              |

---

## Usage-Weighted Coverage Assessment (Pre-Phase 3 Estimate)

Prior to the formal Phase 3 coverage matrix construction, the following qualitative assessment of coverage adequacy is documented to inform Phase 2 completion:

| Capability | Usage % | Benchmark Count | Coverage Assessment |
| ---------- | ------- | --------------- | -------------------------------- |
| C02        | 34.0%   | 5               | Well-covered (historical + current; legacy anchor retained) |
| C03        | 21.4%   | 5               | Well-covered (saturation benchmarks replaced; LiveBench adds contamination resistance) |
| C01        | 17.5%   | 4               | Partially covered (proxy-dominated; WildBench replaces HelloBench for better real-user grounding) |
| C07        | 10.7%   | 4               | Minimally covered (all v2 entries replaced with stronger benchmarks; no frontier presence) |
| C04        | 7.8%    | 3               | Minimally covered (MRBench replaced by TutorBench for broader scope; no frontier presence) |
| C05        | 3.9%    | 3               | Critically underserved (Auto-J/Shepherd/MetaCritique replaced by JudgeBench + RewardBench 2; zero frontier presence) |
| C08        | 2.9%    | 2               | Critically underserved (FIREBALL replaced by CoSER; zero frontier presence) |
| C06        | 1.9%    | 2               | Critically underserved (Multi-IF replaced by WMT24++; zero dedicated frontier evaluation) |

This pre-assessment will be formally quantified using the Gap Score formula in Phase 3:
`Gap Score = Usage_Frequency × (1 − Normalized_Coverage_Score)`

---

## References for New and Replacement Benchmarks

Jimenez, C.E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., and Narasimhan, K. (2024). SWE-bench: Can Language Models Resolve Real-world Github Issues? arXiv:2310.06770.

Miserendino, S., Wang, C., Patwardhan, S., and Reinhardt, J. (2025). SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering? arXiv:2502.12115.

Phan, L., Gatti, A., Han, Z., et al. (2025). Humanity's Last Exam. arXiv:2501.14249. Published in *Nature*, January 2026.

White, C., Dooley, S., Roberts, M., et al. (2024). LiveBench: A Challenging, Contamination-Free LLM Benchmark. arXiv:2406.19314. ICLR 2025 Spotlight.

Lin, B.Y., Deng, Y., Chandu, K., et al. (2024). WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild. arXiv:2406.04770. ICLR 2025.

Hu, X., Zhao, L., Wei, X., et al. (2024). InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks. arXiv:2401.05507. ICML 2024.

Huang, Y., Luo, J., Yu, W., et al. (2024). DA-Code: Agent Data Science Code Generation Benchmark for Large Language Models. arXiv:2410.07331. EMNLP 2024.

Lei, F., Chen, J., Ye, Q., et al. (2024). Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows. arXiv:2411.07763. ICLR 2025 Oral.

Ma, R., Zang, Z., Chen, Y., et al. (2024). MMLongBench-Doc: Benchmarking Long-context Document Understanding with Visualizations. arXiv:2407.01523. NeurIPS 2024 Datasets & Benchmarks Spotlight.

Macina, J., Daheim, N., Hakimi, S., et al. (2025). MathTutorBench: A Benchmark for Measuring Open-ended Pedagogical Capabilities of LLMs. arXiv:2502.18940. EMNLP 2025 Oral.

Srinivasa, R., Che, T., Zhang, Y., et al. (2025). TutorBench: Benchmarking LLMs as Tutors across Subjects and Modalities. arXiv:2510.02663. Scale AI.

Tan, S., Zhang, Y., Zhang, H., et al. (2024). JudgeBench: A Benchmark for Evaluating LLM-based Judges. arXiv:2410.12784. ICLR 2025.

Malik, A., Lambert, J., et al. (2025). RewardBench 2: Advancing Reward Model Evaluation. arXiv:2506.01937. AI2.

Wang, Y., Wang, Z., Zhang, Y., et al. (2025). CoSER: Coordinating LLMs for Role-Playing with Authentic Experiences. arXiv:2502.09082. ICML 2025.

Deutsch, D., Freitag, M., et al. (2025). WMT24++: Expanding the Language Coverage of the WMT24 General Translation Task. arXiv:2502.12404. Google / Unbabel.

Huang, X., Zhu, W., Hu, H., He, C., Li, L., Huang, S., and Yuan, F. (2025). BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models. In *Findings of the Association for Computational Linguistics: EMNLP 2025*, pages 16751–16774. https://doi.org/10.18653/v1/2025.findings-emnlp.909

Gusev, I. (2024). PingPong: A Benchmark for Role-Playing Language Models with User Emulation and Multi-Model Evaluation. arXiv:2409.06820.

---

*Document version: v3 (Final)*
*Project: Benchmark Coverage Gap — Leon Kamau Kiunga (201759400)*
*Supersedes: benchmark_selection_rationale_v2.md*
