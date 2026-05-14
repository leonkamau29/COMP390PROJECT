# Benchmark Selection Rationale (v2)

**Project:** Benchmark Coverage Gap — A Systematic Analysis of Real-World AI Capabilities and Evaluation Practices
**Student:** Leon Kamau Kiunga (201759400)
**Phase:** 2, Week 5
**Revised:** May 2026 — updated to reflect Phase 1 FINAL taxonomy (Feb 2026 AEI data) and expanded benchmark inventory

---

## Selection Criteria

All included benchmarks must meet ALL three of the following:

1. **Publicly documented** — a paper or technical report must be available (arXiv, ACL Anthology, conference proceedings, or official technical blog).
2. **Multi-lab adoption** — cited or used by ≥2 major labs or research organisations OR selected to directly represent an underserved capability gap with documented evidence of absence from frontier reports.
3. **Taxonomy alignment** — must test at least one capability identified in the Phase 1 FINAL taxonomy (C01–C08, validated against Anthropic AEI Feb 2026 top-103 tasks).

> **Scope:** 15–20 benchmarks across 4–5 capability areas per supervisor feedback (revised down from 40–50). The revised Phase 1 taxonomy, grounded in the February 2026 Anthropic Economic Index update, redistributes usage shares across eight capabilities. This revision upgrades three previously deprioritised capabilities — C06 Translation and Language Processing, C07 Data Analysis and Summarisation, and C08 Conversational Interaction and Roleplay — to warranted inventory slots. Final count: **25 benchmarks across 8 capability areas (C01–C08)**.
>
> **Scope note on count:** The addition of C06, C07, and C08 slots takes the inventory above the original 15–20 cap. This is a deliberate, documented scope revision justified by the Phase 1 taxonomy revision, which elevated C07 to 10.7% of usage (third-ranked), C08 to 2.9%, and confirmed C06 at 1.9%. Retaining these capabilities without benchmark coverage would create an internal inconsistency between the taxonomy and the inventory. The supervisor may confirm or trim this at the Phase 2 review milestone.

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

---

## Inclusion Decisions

### C02 — Code Development and Technical Problem Solving (5 benchmarks: B001–B005)

*Unchanged from v1. Rationale reproduced and confirmed against Phase 1 FINAL taxonomy.*

**B001 — HumanEval / HumanEval+**
Included as a controlled baseline. Despite saturation, HumanEval is the most-cited C02 benchmark globally (>8,000 citations) and appears in every major frontier release table since 2021. HumanEval+ is included as the directly improved version (same 164 problems, 80× more test cases) rather than treating them as separate entries. Together they anchor the historical baseline and surface the saturation problem central to the gap argument.

**B002 — MBPP / MBPP+ (EvalPlus)**
Included to complement HumanEval with broader problem coverage (~974 problems vs. 164) and a different difficulty distribution. MBPP is a universal baseline across labs (GPT-4, Claude 3, Gemini, Llama 3 all cite it). MBPP+ is included as the improved version for the same reasons as HumanEval+.

**B003 — SWE-bench Verified**
Included as the de-facto standard for agentic code evaluation in 2025. It measures real-world software engineering (patching actual GitHub issues) rather than algorithmic puzzle-solving. The Verified subset (500 human-validated issues) is the version used in all 2025 frontier reports. Essential for demonstrating the gap between HumanEval-style evaluation and real C02b/C02c workflows.

**B004 — LiveCodeBench**
Included for its contamination-resistant design (monthly refresh from post-training-cutoff competition problems). Cited in Claude 4, Gemini 2.5, and Llama 4 reports. Its continuous update mechanism is directly relevant to the Phase 3 temporal trend analysis.

**B005 — BigCodeBench (Hard)**
Included to cover library and tool integration — the dominant real-world C02a/C02b activity (using existing APIs rather than implementing algorithms from scratch). BCB Hard (148 tasks) is included rather than the full benchmark for scope management. Cited in Claude 4 and Gemini 2.5 reports.

**Excluded C02 candidates:** APPS (high difficulty competitive programming; partially redundant with LiveCodeBench); DS-1000 (data science; overlaps C07); CodeContests (very high difficulty; redundant with LiveCodeBench); Aider Polyglot / Terminal-Bench (agentic; redundant with SWE-bench Verified within 5-benchmark cap).

---

### C01 — Content Generation (4 benchmarks: B006–B009)

*Unchanged from v1. Rationale reproduced and confirmed against Phase 1 FINAL taxonomy (C01 = 17.5% of top 103 tasks).*

**B006 — IFEval**
Included as the only C01 benchmark with cross-lab consensus (cited in Claude 4, Gemini 2.5, Llama 4, and the Open LLM Leaderboard v2). Its inclusion serves a dual analytical purpose: it anchors the "what is currently measured" side of the gap argument, and its short-prompt constraint-following design makes the proxy problem visible. A model can satisfy IFEval perfectly while failing at real writing tasks. Inclusion is justified under criterion 2 (multi-lab adoption) and criterion 3 (C01 alignment, albeit partial).

**B007 — WritingBench**
Included as the primary direct measure of C01. WritingBench (NeurIPS 2025) covers 1,239 queries across 6 writing domains and 100 subdomains with a query-dependent critic model. No frontier technical report cites it — which is itself evidence of the C01 gap. Satisfies criterion 1 (NeurIPS-published) and criterion 3. Multi-lab adoption criterion partially waived: absence from frontier reports is the analytical point, not a disqualifier.

**B008 — EQ-Bench Creative Writing v3 + Longform Writing**
Included for its live community leaderboard (eqbench.com) and for measuring dimensions absent from IFEval: character voice, emotional authenticity, narrative craft, stylistic originality. Elo-based ranking across >40 models provides an existing comparison baseline.

**B009 — HelloBench / LongBench-Write**
Included to close the long-form writing gap. Both IFEval and MT-Bench use short prompts; HelloBench and LongBench-Write explicitly target document-length outputs. Together they represent the C01b/C01e use case as it actually occurs in real workflows (drafting a report, writing a multi-section essay).

**Excluded C01 candidates:** MT-Bench (GPT-4-judged multi-turn; primarily C01/C03 hybrid; replaced by WritingBench + EQ-Bench); Suri (multi-constraint long-form; partially redundant with WritingBench); IFBench (harder IFEval variant; partially redundant with IFEval).

---

### C03 — Information Retrieval and Advisory (4 benchmarks: B013–B016)

*Unchanged from v1. Rationale reproduced and confirmed against Phase 1 FINAL taxonomy (C03 = 21.4% of top 103 tasks — now second-ranked, up from fourth in v1).*

**B013 — MMLU / MMLU-Pro**
Included as the universal knowledge benchmark. MMLU (2020, >10,000 citations) is cited in every major frontier model release table since GPT-4. MMLU-Pro (2024) is its contamination-resistant update with harder reasoning-intensive items. Together they provide the C03 baseline and allow temporal comparison across model generations. MMLU saturation is itself a relevant finding for the coverage gap analysis.

**B014 — GPQA Diamond**
Included as the current frontier C03 benchmark (graduate-level expert-validated questions). Present in every 2025 release table. Expert-validated questions give it the highest ground-truth reliability of any C03 benchmark. Has replaced MMLU at the frontier difficulty end.

**B015 — TriviaQA / Natural Questions**
Included as historical open-domain QA anchors. Still cited by Llama 3 and Gemini 1.5. Their age (2017/2019) and saturation are analytically relevant — they illustrate how C03 benchmarks age and how contamination risk grows over time.

**B016 — SimpleQA / FACTS Grounding**
Included to cover hallucination measurement directly. SimpleQA (4,326 unambiguous facts) and FACTS Grounding (860 document-grounded tasks) measure whether models generate false information — the most practically consequential failure mode in C03 advisory contexts. Both cited in 2024–2025 frontier reports (Claude 4 / Gemini 2.0).

**Excluded C03 candidates:** SQuAD 1.1/2.0 (saturated and superseded); HotpotQA / DROP (multi-hop reasoning; partially captured by BBH); TruthfulQA (partially redundant with SimpleQA); commonsense benchmarks (HellaSwag / WinoGrande / ARC-C) (GPQA and MMLU-Pro cover this layer more robustly for current frontier analysis).

---

### C04 — Learning and Education Support (3 benchmarks: B010–B012)

*Unchanged from v1. Rationale reproduced and confirmed against Phase 1 FINAL taxonomy (C04 = 7.8% of top 103 tasks — fifth-ranked).*

**B010 — MathDial**
Included as the foundational tutoring-dialogue benchmark. MathDial (EMNLP 2023, 2,900 student–tutor dialogues) establishes the conceptual distinction between solving a maths problem and teaching a student to solve it — the core argument for why GSM8K and MATH are inadequate C04 proxies. Chronologically earliest of the C04 benchmarks; necessary for temporal analysis.

**B011 — MRBench**
Included for its explicit multi-dimensional pedagogical taxonomy (8 dimensions; Desired Annotation Match Rate metric; NAACL 2025). Provides the most fine-grained operationalisation of what "good tutoring" means across scaffolding, error correction, and encouragement.

**B012 — MathTutorBench**
Included as the most comprehensive C04 benchmark available, covering 7 pedagogical tasks with a pedagogy reward model and a public leaderboard. Its finding that stronger solvers are sometimes worse tutors is a key thesis argument.

**Excluded C04 candidates:** Bridge (elementary-school remediation; narrower scope than MathDial); KMP-Bench (2026 publication; very new; limited adoption); math-solving benchmarks (GSM8K, MATH, AIME) (measure C04 output, not C04 pedagogy; included under C03 if relevant).

---

### C05 — Review and Feedback (2 benchmarks: B017–B018)

*Unchanged from v1. Rationale reproduced and confirmed against Phase 1 FINAL taxonomy (C05 = 3.9% of top 103 tasks — sixth-ranked).*

**B017 — CriticBench (Tsinghua)**
Included as the primary and most comprehensive C05 benchmark. 3,825 instances across 15 datasets in 5 reasoning domains (critique-and-correct format; ACL 2024 Findings). Its absence from all frontier technical reports reviewed is the central piece of evidence for the C05 coverage gap.

**B018 — Auto-J + Shepherd + MetaCritique (grouped)**
Included to complement CriticBench by covering open-ended prose critique tasks (essay feedback, code review, general instruction evaluation) absent from CriticBench's STEM focus. Auto-J provides 4,396 instances across 58 real-world scenarios; Shepherd provides human-authored reference feedback; MetaCritique enables meta-evaluation. The group is treated as a single inventory entry.

**Excluded C05 candidates:** CriticBench (Tencent) (redundant with Tsinghua version; Tsinghua preferred for broader domain coverage); CritiqueLLM / UltraCM (critique-tuned models rather than benchmarks per se); GEC benchmarks (CoNLL-2014 / JFLEG / BEA-2019) (narrow grammatical error-correction proxy; does not capture argumentative, structural, or stylistic feedback dimensions central to C05b–C05d).

---

### C07 — Data Analysis and Summarisation (3 benchmarks: B019–B021)

**Scope justification:** C07 is the fourth most common capability in the Phase 1 FINAL taxonomy, accounting for 10.7% of Anthropic's top 103 tasks. It was excluded from the v1 inventory as a consequence of the prior usage estimate (~5–7%) placing it outside the provisional top-five scope. The February 2026 AEI revision elevates C07 substantially and makes its exclusion analytically unjustifiable. Three benchmarks are added to provide coverage across the three distinct C07 sub-tasks: text summarisation (C07a), statistical and data analysis (C07b), and document processing and extraction (C07c).

**B019 — QRData (Quantitative Reasoning with Data)**
*Liu et al. (2024). ACL 2024 Findings. arXiv / DOI: 10.18653/v1/2024.findings-acl.548.*

Included as the primary C07b benchmark for statistical and causal reasoning on real-world data. QRData comprises 411 questions accompanied by real data sheets drawn from textbooks, online learning materials, and academic papers, testing whether models can reason about data rather than simply retrieve facts from training. An auxiliary text-only set (QRText, 290 questions) enables direct comparison of data-grounded versus text-only reasoning. Satisfies all three inclusion criteria: publicly documented (ACL 2024 Findings); the evaluation scope spans capabilities relevant to multiple labs' deployments; directly tests C07b (data analysis and statistical computing). Its finding that GPT-4 achieves only 58% accuracy, with strong models like Deepseek-coder reaching just 37%, establishes the gap between benchmark performance on retrieval tasks and genuine analytical capability on data — a key Phase 3 argument.

**B020 — Text2Analysis**
*He et al. (2024). AAAI 2024 Technical Track on NLP. DOI: 10.1609/aaai.v38i16.29779.*

Included to extend C07b coverage beyond statistical reasoning to advanced tabular analysis tasks: forecasting, chart generation, and complex SQL-beyond operations on ambiguous real-world queries. Text2Analysis collected 2,249 query-result pairs across 347 tables, with five annotation methods including LLM augmentation for data quality enhancement. Crucially, the benchmark includes "unclear queries" that mirror real user questions — directly addressing the C07 sub-category of business intelligence and forecasting (C07d). No major frontier technical report cites it, which is itself evidence of the C07 gap. Satisfies criterion 1 (AAAI 2024) and criterion 3 (C07b/C07d alignment). Multi-lab adoption criterion partially waived on the same basis as WritingBench: absence from frontier reports is the analytical point.

**B021 — READoc**
*Li et al. (2025). ACL 2025 Findings. DOI: 10.18653/v1/2025.findings-acl.1128.*

Included to cover C07c (document processing and format conversion) — the sub-capability involving extraction of structured content from unstructured source documents. READoc defines Document Structured Extraction (DSE) as the realistic task of converting unstructured PDFs into semantically rich Markdown, derived from 3,576 diverse real-world documents from arXiv, GitHub, and Zenodo. The DSE Evaluation S3uite provides standardised assessment across pipeline tools, expert visual models, and Vision-Language Models, enabling comparison across system types. This benchmark closes the document-processing gap: no existing frontier evaluation directly measures structured extraction from real-world document corpora. Satisfies criterion 1 (ACL 2025 Findings) and criterion 3 (C07c alignment). Its identification of the gap between current work and realistic DSE objectives maps directly onto the Phase 3 coverage matrix methodology.

**Excluded C07 candidates:** SummEval (summarisation quality; covered at the sub-task level by READoc and partially by WritingBench; omitted under scope management); FABLES (narrative summarisation; niche sub-task; omitted); DS-1000 (data science code generation; C02/C07 hybrid; excluded to maintain C02 boundary); TAT-QA (tabular QA; partially redundant with Text2Analysis).

---

### C06 — Translation and Language Processing (2 benchmarks: B022–B023)

**Scope justification:** C06 accounts for 1.9% of Anthropic's top 103 tasks in the Phase 1 FINAL taxonomy (two tasks: language-learning assistance with translation and grammar help; professional, academic, medical and religious content translation between languages). While this is the smallest capability by task count, it is meaningfully distinct from all other capabilities and directly matched to tasks in the empirical usage data. Moreover, translation represents a high-volume, high-stakes real-world use case (professional document translation, multilingual communication) that warrants independent benchmark assessment. Two benchmarks are allocated: one for translation quality across languages (C06a), one for multilingual instruction-following that spans C06 and other capabilities in cross-lingual deployment (C06b/C06a).

**B022 — BenchMAX**
*Huang et al. (2025). EMNLP 2025 Findings. DOI: 10.18653/v1/2025.findings-emnlp.909.*

Included as the primary multilingual evaluation benchmark spanning translation and cross-lingual capabilities. BenchMAX covers 10 diverse tasks (including instruction following, reasoning, code generation, and long-context understanding) across 16 languages, with each sample post-edited by three native annotators after machine translation from English. Its explicit coverage of cross-lingual capability gaps — and its finding that uneven utilisation of core capabilities across languages is not resolved by scaling alone — directly supports the Phase 3 argument about benchmark gaps in non-English contexts. Satisfies criterion 1 (EMNLP 2025 Findings) and criterion 3 (C06a/C06b alignment across multilingual dimensions). The dataset and code are publicly accessible. Multi-lab adoption is nascent given the 2025 publication date, but the benchmark's comprehensive multilingual scope and post-edited quality make it the strongest candidate in the C06 space.

**B023 — Multi-IF**
*Xu et al. (2024). arXiv:2410.15553.*

Included to cover multi-turn, multilingual instruction-following — the intersection of C06 and C01 that is entirely absent from monolingual benchmarks such as IFEval. Multi-IF expands IFEval by incorporating multi-turn sequences (three turns per conversation) and translating English prompts into 7 additional languages, resulting in 4,501 multilingual conversations. The benchmark uses a hybrid framework combining LLM and human annotators. Its evaluation of models including o1-preview, Llama 3.1 405B, GPT-4o, Claude-3.5 Sonnet, and Gemini-1.5 pro provides cross-lab comparison data. Directly satisfies criterion 3 (C06a/C06b alignment: cross-lingual instruction compliance). Satisfies criterion 2 partially — while no frontier report labels Multi-IF as a primary evaluation, its basis in IFEval (which is universally cited) and its cross-lab model evaluations establish its relevance. Its inclusion also addresses the methodological gap identified in Phase 1: monolingual instruction-following evaluation systematically underestimates deployment failures in multilingual contexts.

**Excluded C06 candidates:** FLORES-101 / FLORES+ (translation quality; covers primarily MT system evaluation rather than LLM-as-translator assessment; relevant but more specialised than BenchMAX for LLM evaluation purposes); WMT shared tasks (shared tasks rather than fixed benchmarks; methodology inconsistent across years; excluded for comparability reasons); standard MT metrics (BLEU/COMET) (metrics, not benchmarks per se).

---

### C08 — Conversational Interaction and Roleplay (2 benchmarks: B024–B025)

**Scope justification:** C08 accounts for 2.9% of Anthropic's top 103 tasks in the Phase 1 FINAL taxonomy (tasks include: relationship, dating, parenting and personal advice dialogue; job interview practice and professional scenario roleplay; and mental health and ADHD support resources). While 2.9% represents a modest share of the AEI enterprise-oriented dataset, the OpenRouter (2025) data shows that roleplay and interactive fiction constitutes approximately 50% of open-source model token usage. The C08 coverage gap is therefore particularly severe when evaluated against the broader deployment context. Additionally, the absence of any C08 benchmark from frontier technical reports constitutes strong gap evidence. Two benchmarks are allocated to cover the two distinct C08 sub-tasks: character-consistent multi-turn roleplay (C08b) and open-ended dialogue quality (C08a/C08c).

**B024 — PingPong**
*Gusev (2024). arXiv:2409.06820.*

Included as the primary C08b benchmark. PingPong evaluates role-playing capabilities through a three-component framework: a player model adopting a character role, an interrogator model simulating user behaviour in a specific situation, and a judge model ensemble evaluating conversation quality on three metrics (character consistency, entertainment value, and language fluency). The benchmark evaluated more than 40 models in English and Russian, with each model participating in 64 conversations across 8 characters and 8 situations. Human annotation validation demonstrates strong correlations between automated and human evaluations across multiple criteria. Satisfies criterion 1 (arXiv; revised to v4 April 2025, with leaderboard updates) and criterion 3 (C08b direct alignment: character role-play in multi-turn conversations). The cross-lingual evaluation (English and Russian) also provides partial C06 relevance. Its absence from all frontier technical reports is consistent with the broader C08 gap evidence.

**B025 — FIREBALL**
*Zhu et al. (2023). ACL 2023 Long Papers. DOI: 10.18653/v1/2023.acl-long.229.*

Included to cover collaborative interactive fiction and game-state-aware roleplay (C08b/C08d) — sub-tasks that require the model to maintain coherent narrative state across extended multi-turn exchanges with externally defined game rules. FIREBALL contains nearly 25,000 unique D&D gameplay sessions from real Discord play using the Avrae bot, with true game state information (language, game commands, and underlying game state captured simultaneously). It provides a rare dataset of real, sustained interactive roleplay with verifiable game-state ground truth. Satisfies criterion 1 (ACL 2023 Long Papers) and criterion 3 (C08b/C08d alignment). Its real-user provenance distinguishes it from synthetic roleplay datasets. The finding that LLMs with access to state information generate higher-quality game turns than those relying on dialogue history alone has direct implications for C08 evaluation methodology in Phase 5 benchmark design proposals.

**Excluded C08 candidates:** MT-Bench (primarily C01/C03 multi-turn quality; not C08-specific); PersonaGym (persona assessment; QA-based rather than dialogue-based; does not capture sustained interactive exchange); CharacterEval (character fidelity in Chinese; scope limited to Chinese language; C06 complication); EmpathyBench-type benchmarks (empathetic response; too narrow for C08 full coverage — covers only C08a).

---

## Benchmark Count Distribution (v2)

| Capability                                     | Code | Count | Reasoning for allocation                                                                                                              |
| ---------------------------------------------- | ---- | ----- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Code Development and Technical Problem Solving | C02  | 5     | Highest usage share; saturated benchmark space requires multiple benchmarks to characterise the coverage landscape (B001–B005)        |
| Information Retrieval and Advisory             | C03  | 4     | Second-highest; well-covered in general but saturation and hallucination measurement require multiple anchors (B013–B016)             |
| Content Generation                             | C01  | 4     | Third-highest; major gap with only 1 consensus benchmark (IFEval) means 3 gap-illustrating alternatives needed (B006–B009)           |
| Data Analysis and Summarisation                | C07  | 3     | Fourth-highest (10.7%); entirely absent from frontier reports; 3 benchmarks cover C07a text summarisation, C07b statistical analysis, and C07c document extraction (B019–B021) |
| Learning and Education Support                 | C04  | 3     | Fifth-highest; entirely absent from frontier reports; 3 benchmarks illustrate the gap across foundational / multi-dimensional / comprehensive levels (B010–B012) |
| Review and Feedback                            | C05  | 2     | Sixth-highest; zero frontier report presence; minimum viable coverage with 2 slots (B017–B018)                                        |
| Conversational Interaction and Roleplay        | C08  | 2     | Seventh-highest in AEI but dominant in OSS usage (~50% token share per OpenRouter 2025); zero frontier report presence (B024–B025)    |
| Translation and Language Processing            | C06  | 2     | Eighth-highest; zero dedicated frontier evaluation; 2 benchmarks cover multilingual quality and multilingual instruction-following (B022–B023) |
| **Total**                                | —    | **25**| Expanded from 18 to 25 to accommodate C07, C06, C08 additions justified by Phase 1 FINAL taxonomy revision                           |

---

## Cross-Capability Alignment with Phase 1 FINAL Taxonomy

The following table maps each benchmark to its primary taxonomy capability and the relevant Phase 1 sub-categories it exercises. This alignment was verified against the capability definitions and decision rules in `outputs/phase1/capability_taxonomy_FINAL.md`.

| Benchmark ID | Name (abbreviated) | Primary Capability | Phase 1 Sub-categories Exercised |
| ------------ | ------------------ | ------------------ | --------------------------------- |
| B001         | HumanEval+         | C02                | C02a, C02b                        |
| B002         | MBPP+              | C02                | C02b, C02c                        |
| B003         | SWE-bench Verified | C02                | C02b, C02c (C05 secondary)        |
| B004         | LiveCodeBench      | C02                | C02a, C02b                        |
| B005         | BigCodeBench Hard  | C02                | C02a, C02b, C02e                  |
| B006         | IFEval             | C01                | C01b, C01e (proxy)                |
| B007         | WritingBench       | C01                | C01a–C01e (all sub-categories)    |
| B008         | EQ-Bench-CW        | C01                | C01d, C01e                        |
| B009         | HelloBench         | C01                | C01b, C01e (long-form)            |
| B010         | MathDial           | C04                | C04b                              |
| B011         | MRBench            | C04                | C04b, C04d                        |
| B012         | MathTutorBench     | C04                | C04b, C04c                        |
| B013         | MMLU-Pro           | C03                | C03a, C03d                        |
| B014         | GPQA Diamond       | C03                | C03a                              |
| B015         | TriviaQA/NQ        | C03                | C03a, C03e                        |
| B016         | SimpleQA/FACTS     | C03                | C03a (hallucination sub-task)     |
| B017         | CriticBench        | C05                | C05b, C05c, C05d                  |
| B018         | Auto-J/Shepherd    | C05                | C05b, C05d                        |
| B019         | QRData             | C07                | C07b                              |
| B020         | Text2Analysis      | C07                | C07b, C07d                        |
| B021         | READoc             | C07                | C07c                              |
| B022         | BenchMAX           | C06                | C06a, C06b                        |
| B023         | Multi-IF           | C06                | C06a, C06b (C01 secondary)        |
| B024         | PingPong           | C08                | C08b, C08c                        |
| B025         | FIREBALL           | C08                | C08b, C08d                        |

---

## Usage-Weighted Coverage Assessment (Pre-Phase 3 Estimate)

Prior to the formal Phase 3 coverage matrix construction, the following qualitative assessment of coverage adequacy is documented to inform Phase 2 completion:

| Capability | Usage % | Benchmark Count | Coverage Assessment              |
| ---------- | ------- | --------------- | -------------------------------- |
| C02        | 34.0%   | 5               | Well-covered (historical + current) |
| C03        | 21.4%   | 4               | Well-covered (but saturation risk) |
| C01        | 17.5%   | 4               | Partially covered (proxy-dominated) |
| C07        | 10.7%   | 3               | Minimally covered (new entrants, no frontier presence) |
| C04        | 7.8%    | 3               | Minimally covered (no frontier presence) |
| C05        | 3.9%    | 2               | Critically underserved (zero frontier presence) |
| C08        | 2.9%    | 2               | Critically underserved (zero frontier presence) |
| C06        | 1.9%    | 2               | Critically underserved (zero dedicated evaluation) |

This pre-assessment will be formally quantified using the Gap Score formula in Phase 3:
`Gap Score = Usage_Frequency × (1 − Normalized_Coverage_Score)`

---

## References for New Benchmarks (B019–B025)

Liu, X., Wu, Z., Wu, X., Lu, P., Chang, K.-W., and Feng, Y. (2024). Are LLMs Capable of Data-based Statistical and Causal Reasoning? Benchmarking Advanced Quantitative Reasoning with Data. In *Findings of the Association for Computational Linguistics: ACL 2024*, pages 9215–9235. https://doi.org/10.18653/v1/2024.findings-acl.548

He, X., Zhou, M., Xu, X., Ma, X., Ding, R., Du, L., Gao, Y., Jia, R., Chen, X., Han, S., Yuan, Z., and Zhang, D. (2024). Text2Analysis: A Benchmark of Table Question Answering with Advanced Data Analysis and Unclear Queries. In *Proceedings of the AAAI Conference on Artificial Intelligence*, 38(16), pages 18206–18215. https://doi.org/10.1609/aaai.v38i16.29779

Li, Z., Abulaiti, A., Lu, Y., Chen, X., Zheng, J., Lin, H., Han, X., Jiang, S., Dong, B., and Sun, L. (2025). READoc: A Unified Benchmark for Realistic Document Structured Extraction. In *Findings of the Association for Computational Linguistics: ACL 2025*, pages 21889–21905. https://doi.org/10.18653/v1/2025.findings-acl.1128

Huang, X., Zhu, W., Hu, H., He, C., Li, L., Huang, S., and Yuan, F. (2025). BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models. In *Findings of the Association for Computational Linguistics: EMNLP 2025*, pages 16751–16774. https://doi.org/10.18653/v1/2025.findings-emnlp.909

Xu, T., Lv, H., et al. (2024). Multi-IF: Benchmarking LLMs on Multi-Turn and Multilingual Instructions Following. arXiv:2410.15553.

Gusev, I. (2024). PingPong: A Benchmark for Role-Playing Language Models with User Emulation and Multi-Model Evaluation. arXiv:2409.06820.

Zhu, A., Aggarwal, K., Feng, A., Martin, L. J., and Callison-Burch, C. (2023). FIREBALL: A Dataset of Dungeons and Dragons Actual-Play with Structured Game State Information. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 4171–4193. https://doi.org/10.18653/v1/2023.acl-long.229

---

*Document version: v2 (May 2026)*
*Project: Benchmark Coverage Gap — Leon Kamau Kiunga (201759400)*
*Supersedes: benchmark_selection_rationale.md (v1)*
