# Benchmark Selection Rationale

**Project:** Benchmark Coverage Gap — A Systematic Analysis of Real-World AI Capabilities and Evaluation Practices
**Student:** Leon Kamau Kiunga (201759400)
**Phase:** 2, Week 5 ·

---

## Selection Criteria

All included benchmarks must meet ALL three of the following:

1. **Publicly documented** — a paper or technical report must be available (arXiv, ACL Anthology, conference proceedings, or official technical blog).
2. **Multi-lab adoption** — cited or used by ≥2 major labs or research organisations OR selected to directly represent an underserved capability gap with documented evidence of absence from frontier reports.
3. **Taxonomy alignment** — must test at least one capability identified in the Phase 1 taxonomy (C01–C08).

> **Scope cap:** 15–20 benchmarks across 4–5 capability areas, per supervisor feedback (revised down from 40–50). Final count: **18 benchmarks across 5 capability areas (C02, C01, C04, C03, C05)**.

---

## Capability Scope Decision

The top-five capability scope (C02, C01, C04, C03, C05) was determined by cross-referencing the Phase 1 taxonomy against Handa et al. (2025), which analysed approximately four million Claude.ai conversations. The empirically supported ranking is:

| Rank | Capability                                       | Estimated share of real-world usage |
| ---- | ------------------------------------------------ | ----------------------------------- |
| 1    | C02 Code Development & Technical Problem Solving | ~37–42%                            |
| 2    | C01 Content Generation                           | ~15–20%                            |
| 3    | C04 Learning & Education Support                 | ~10–14%                            |
| 4    | C03 Information Retrieval & Advisory             | ~9–12%                             |
| 5    | C05 Review & Feedback                            | ~7–10%                             |

C07 Data Analysis (previously ranked #4 in the researcher's prior) is dropped from the top five. C04 (absent from the prior) is added. C01 (previously ranked #5) is elevated to #2. This revision is documented in full in `data/phase2/PHASE2RESEARCH.md`, Step 1.

---

## Inclusion Decisions

### C02 — Code Development & Technical Problem Solving (5 benchmarks: B001–B005)

**B001 — HumanEval / HumanEval+**
Included as a controlled baseline. Despite saturation, HumanEval is the most-cited C02 benchmark globally (>8000 citations) and appears in every major frontier release table since 2021. Its inclusion is methodologically necessary to anchor the historical baseline and demonstrate the progression from isolated function generation to more realistic evaluation. HumanEval+ is included as the directly improved version (same 164 problems, 80× more test cases) rather than treating them separately.

**B002 — MBPP / MBPP+ (EvalPlus)**
Included to complement HumanEval with broader problem coverage (~974 problems vs. 164) and different difficulty distribution. MBPP is also a universal baseline across labs (GPT-4, Claude 3, Gemini, Llama 3 all cite it). MBPP+ is included as the improved version for the same reasons as HumanEval+.

**B003 — SWE-bench Verified**
Included as the de-facto standard for agentic code evaluation in 2025. Its significance lies in measuring real-world software engineering (patching actual GitHub issues) rather than algorithmic puzzle-solving. The Verified subset (500 human-validated issues) is the version used in all 2025 frontier reports. This benchmark is essential to demonstrate the gap between HumanEval-style evaluation and real-world code capability.

**B004 — LiveCodeBench**
Included for its contamination-resistant design (monthly refresh from post-training-cutoff competition problems). Addresses a critical methodological limitation of static benchmarks. Cited in Claude 4, Gemini 2.5, and Llama 4 reports. Its continuous update mechanism is directly relevant to Phase 3 analysis of benchmark update frequency.

**B005 — BigCodeBench (Hard)**
Included to cover library and tool integration — the dominant real-world software engineering activity (using existing APIs rather than implementing algorithms from scratch). BCB Hard (148 tasks) is included rather than the full benchmark for scope management. Cited in Claude 4 and Gemini 2.5 reports.

**Excluded C02 candidates:**

- APPS: High difficulty competitive programming; partially redundant with LiveCodeBench; narrower real-world relevance.
- DS-1000: Good data-science benchmark but overlaps with C07; omitted to preserve the C07 exclusion decision.
- CodeContests: Very high difficulty; partially redundant with LiveCodeBench; limited frontier report presence.
- Aider Polyglot / Terminal-Bench: Agentic; partially redundant with SWE-bench Verified within the 5-benchmark cap.

---

### C01 — Content Generation (4 benchmarks: B006–B009)

**B006 — IFEval**
Included despite being a proxy for C01 rather than a direct measure. IFEval is the only C01 benchmark with cross-lab consensus (cited in Claude 4, Gemini 2.5, Llama 4, and the Open LLM Leaderboard v2). Its inclusion serves a dual analytical purpose: (a) it anchors the "what is currently measured" side of the coverage-gap argument, and (b) its short-prompt constraint-following design makes the proxy problem visible — a model can satisfy IFEval perfectly while failing at real writing tasks. Inclusion justified under criterion 2 (multi-lab adoption) and criterion 3 (C01 alignment, albeit partial).

**B007 — WritingBench**
Included as the primary direct measure of C01. WritingBench (NeurIPS 2025) covers 1239 queries across 6 writing domains and 100 subdomains with a query-dependent critic model. No frontier technical report cites it — which is itself evidence of the C01 gap. Satisfies criterion 1 (NeurIPS-published) and criterion 3 (direct C01 measurement). Multi-lab adoption criterion partially waived: the benchmark's absence from frontier reports is the analytical point, not a disqualifier.

**B008 — EQ-Bench Creative Writing v3 + Longform Writing**
Included for its live community leaderboard (eqbench.com) and for measuring dimensions absent from IFEval: character voice, emotional authenticity, narrative craft, stylistic originality. Elo-based ranking across >40 models provides an existing comparison baseline. Partially satisfies criterion 2 (widely referenced in independent evaluation communities despite absence from frontier reports).

**B009 — HelloBench / LongBench-Write**
Included to close the long-form writing gap. Both IFEval and MT-Bench use short prompts; HelloBench and LongBench-Write explicitly target document-length outputs. Together they represent the C01 use case as it actually occurs (drafting a report, writing a multi-section essay) rather than completing a sentence-level task. Grouped together as they serve the same gap-coverage purpose within the 4-benchmark C01 allocation.

**Excluded C01 candidates:**

- MT-Bench: GPT-4-judged multi-turn quality; useful but only 80 items; primarily a C01/C03 hybrid; replaced by WritingBench + EQ-Bench for coverage purposes.
- Suri: Multi-constraint long-form; partially redundant with WritingBench; omitted under scope cap.
- IFBench: Harder IFEval variant; partially redundant with IFEval; omitted.

---

### C04 — Learning & Education Support (3 benchmarks: B010–B012)

**B010 — MathDial**
Included as the foundational tutoring-dialogue benchmark. MathDial (EMNLP 2023, 2900 student–tutor dialogues) establishes the conceptual distinction between solving a maths problem and teaching a student to solve it — the core argument for why GSM8K and MATH are inadequate C04 proxies. Satisfies all three criteria. Chronologically earliest of the C04 benchmarks; necessary for temporal analysis in Phase 3.

**B011 — MRBench**
Included for its explicit multi-dimensional pedagogical taxonomy (8 dimensions: Desired Annotation Match Rate metric). NAACL 2025. Provides the most fine-grained operationalisation of what "good tutoring" means across scaffolding, error correction, encouragement, and other dimensions. Expert annotations ground it in validated pedagogical theory.

**B012 — MathTutorBench**
Included as the most comprehensive C04 benchmark available, covering 7 pedagogical tasks with a pedagogy reward model and public leaderboard. 2025 publication. The leaderboard enables direct model comparison — the only C04 benchmark with this feature. Directly replicable and designed for ongoing community use. The finding from its paper (stronger solvers are sometimes worse tutors) is a key thesis argument.

**Excluded C04 candidates:**

- Bridge: Elementary-school remediation; useful but narrower scope than MathDial; partially redundant within 3-benchmark cap.
- KMP-Bench: 2026 publication; very new; limited adoption; omitted pending establishment.
- Math-solving benchmarks (GSM8K, MATH, AIME): These measure C04 output (maths ability) not C04 pedagogy (teaching ability). Included under C03/reasoning but not as C04 benchmarks. This distinction is a key thesis argument.

---

### C03 — Information Retrieval & Advisory (4 benchmarks: B013–B016)

**B013 — MMLU / MMLU-Pro**
Included as the universal knowledge benchmark. MMLU (2020, >10000 citations) is cited in every major frontier model release table since GPT-4. MMLU-Pro (2024) is its contamination-resistant update with harder reasoning-intensive items. Together they provide the C03 baseline and allow temporal comparison across model generations. Saturation of MMLU itself is a relevant finding for the coverage-gap analysis.

**B014 — GPQA Diamond**
Included as the current frontier C03 benchmark (graduate-level expert-validated questions). Present in every 2025 release table. Gated access and expert-validated questions give it the highest ground-truth reliability of any C03 benchmark. Has replaced MMLU at the frontier difficulty end.

**B015 — TriviaQA / Natural Questions**
Included as historical open-domain QA anchors. Still cited by Llama 3 and Gemini 1.5 as standard C03 measures. Their age (2017/2019) and saturation are analytically relevant — they illustrate how C03 benchmarks age and how contamination risk grows over time. Grouped together as complementary open-domain QA benchmarks.

**B016 — SimpleQA / FACTS Grounding**
Included to cover hallucination measurement directly. SimpleQA (4326 unambiguous facts) and FACTS Grounding (860 document-grounded tasks) measure whether models generate false information — the most practically consequential failure mode in C03 advisory contexts. Both cited in 2024–2025 frontier reports (Claude 4 / Gemini 2.0). Grouped as complementary hallucination benchmarks.

**Excluded C03 candidates:**

- SQuAD 1.1/2.0: Saturated and superseded; dropped in favour of NQ and SimpleQA.
- HotpotQA / DROP: Multi-hop and discrete reasoning; partially captured by BBH; omitted under scope cap.
- BIG-Bench Hard: Strong C03/reasoning benchmark; not included as a primary C03 slot is filled by GPQA; BBH is noted as a key frontier benchmark in the research report.
- TruthfulQA: Factual accuracy; partially redundant with SimpleQA; omitted.
- Commonsense benchmarks (HellaSwag / WinoGrande / ARC-C / CommonsenseQA): All in candidates list; GPQA and MMLU-Pro cover the reasoning layer more robustly for current frontier analysis.

---

### C05 — Review & Feedback (2 benchmarks: B017–B018)

**B017 — CriticBench (Tsinghua)**
Included as the primary and most comprehensive C05 benchmark. 15 datasets across 5 reasoning domains; critique-and-correct format; ACL 2024 Findings. Its absence from all frontier technical reports reviewed is the central piece of evidence for the C05 coverage gap. The breadth of domain coverage (math / commonsense / code / symbolic / algorithmic) enables meaningful gap quantification in Phase 3.

**B018 — Auto-J + Shepherd + MetaCritique (grouped)**
Included to complement CriticBench by covering open-ended prose critique tasks (essay feedback, code review, general instruction evaluation) that are absent from CriticBench's STEM focus. Three benchmarks are grouped because each alone is insufficient for C05 coverage: Auto-J provides the broadest scenario coverage (58 real-world scenarios), Shepherd provides human-authored reference feedback, and MetaCritique enables meta-evaluation. The group is treated as a single entry within the 2-benchmark C05 allocation.

**Excluded C05 candidates:**

- CriticBench (Tencent): Similar scope to Tsinghua version; redundant within 2-slot cap; Tsinghua version preferred for broader domain coverage.
- CritiqueLLM / UltraCM: Critique-tuned models rather than evaluation benchmarks per se; methodology differs.
- GEC benchmarks (CoNLL-2014 / JFLEG / BEA-2019): Grammatical error correction is a narrow C05 proxy; does not capture the argumentative / structural / stylistic feedback dimensions.

---

## C07 Exclusion Decision

C07 Data Analysis & Summarisation was excluded from the top-five capability scope based on the empirical revision from Handa et al. (2025). C07 represents approximately 5–7% of real-world LLM usage, placing it outside the top five. The supervisor may request a 20-benchmark variant adding **SummEval** and **FABLES** as C07 slots 19–20 without displacing the existing 18 benchmarks.

C08 Conversational & Roleplay was excluded from the shortlist as it represents <3% of usage in the filtered Handa et al. sample. A full set of C08 candidates is documented in `benchmark_candidates.csv` for reference.

---

## Benchmark Count Distribution

| Capability                | Count        | Reasoning for allocation                                                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| C02 Code                  | 5            | Highest usage share; saturated benchmark space requires multiple benchmarks to characterise the coverage landscape                                   |
| C01 Content Generation    | 4            | Second-highest usage; major gap with only 1 consensus benchmark (IFEval) means 3 gap-illustrating alternatives needed                                |
| C04 Learning & Education  | 3            | Third-highest; entirely absent from frontier reports; 3 benchmarks illustrate the gap across foundational / multi-dimensional / comprehensive levels |
| C03 Information Retrieval | 4            | Fourth-highest; well-covered in general but saturation and hallucination measurement require multiple anchors                                        |
| C05 Review & Feedback     | 2            | Fifth-highest; zero frontier report presence justifies minimum viable coverage with 2 slots; gap argument does not require exhaustive C05 coverage   |
| **Total**           | **18** | Within 15–20 scope cap                                                                                                                              |
