# Progress Report — Phases 1 & 2

**Project:** Benchmark Coverage Gap: A Systematic Analysis of Real-World AI Capabilities and Evaluation Practices
**Student:** Leon Kamau Kiunga (201759400)
**Supervisor:** Dr Konstantinos Tsakaldis
**Date:** 17 April 2026

---

## Phase 1 — Capability Framework Development (Weeks 1–4)

### What was done

Phase 1 produced the empirical foundation on which the rest of the project rests: a
validated taxonomy of eight core LLM capabilities, derived through systematic thematic
analysis of real-world usage data.

The primary data source was Handa et al. (2025) — *Which Economic Tasks are Performed
with AI? Evidence from Millions of Claude Conversations* (arXiv:2503.04761) — which
analysed approximately four million Claude.ai conversations mapped to O\*NET occupational
tasks. This was supplemented with O\*NET Detailed Work Activities, Chatterji et al.
(2025) on ChatGPT usage patterns, and Aubakirova et al. (2025) from OpenRouter's
100-trillion-token study.

123 concrete task instances were extracted from these sources and subjected to Braun &
Clarke's (2006) six-phase thematic analysis: familiarisation, open coding, axial coding,
selective coding, definition, and final taxonomy construction. This produced 20 axial
categories which collapsed into **8 core capabilities**, each given a formal definition,
decision rules for classification, sub-categories, and a minimum of five worked examples
drawn from real tasks.

The taxonomy was then validated against Anthropic's empirically-derived top 100 tasks.
Every one of the 100 tasks was mappable to one of the eight capabilities —
**100% coverage against a target of ≥95%**. Inter-coder reliability was assessed on a
10% subsample (10 tasks), with both coders reaching complete agreement:
**Cohen's κ = 1.00 against a target of >0.80**.

### The Eight Capabilities

| ID  | Capability                                   | Share of Anthropic top 100 |
| --- | -------------------------------------------- | -------------------------- |
| C02 | Code Development & Technical Problem Solving | 36.0%                      |
| C03 | Information Retrieval & Advisory             | 23.0%                      |
| C01 | Content Generation                           | 18.0%                      |
| C07 | Data Analysis & Summarisation                | 8.0%                       |
| C05 | Review & Feedback                            | 6.0%                       |
| C04 | Learning & Education Support                 | 5.0%                       |
| C06 | Translation & Language Processing            | 2.0%                       |
| C08 | Conversational Interaction & Roleplay        | 2.0%                       |

Each capability has a two-part decision rule ("a task belongs to CXX if and only if…"),
explicit resolution of ambiguous cases, and hierarchical sub-categories. For example,
C05 Review & Feedback contains five sub-categories ranging from proofreading (C05a)
through to academic peer-review simulation (C05c) and interview feedback (C05e). The
decision rules are precise enough to distinguish, for instance, "fix the bug in my code"
(→ C02b, technical repair) from "review my code for best practices" (→ C05, evaluative
review).

### Outputs Produced

All Phase 1 deliverables specified in the project plan were completed:

- `data/phase1/task_instances_raw.csv` — 123 extracted task instances
- `data/phase1/task_instances_coded.csv` — with open code, axial category, and core capability columns
- `data/phase1/familiarisation_memo.md` — initial impressions memo
- `data/phase1/capability_definitions_draft.md` — working definitions
- `data/phase1/anthropic_top100_mapping.csv` — 100/100 tasks mapped with confidence and justification
- `data/phase1/intercoder_reliability.csv` — κ = 1.00 on 10-task subsample
- `outputs/phase1/capability_taxonomy_FINAL.md` — complete publication-ready taxonomy
- `outputs/phase1/capability_taxonomy_FINAL.csv` — structured CSV for Phase 3 use

**Phase 1 completion criteria: fully met.**

---

## Phase 2 — Benchmark Inventory (Weeks 5–9)

### What was done

Phase 2 built the benchmark database that will drive the coverage analysis in Phase 3.
The core task was systematically identifying, screening, and documenting LLM benchmarks —
then selecting 18 for deep analysis.

**One significant methodological note:** Papers with Code, which was specified as a
primary sourcing channel in the project plan, was sunsetted by Meta in July 2025. Its
leaderboards are no longer maintained and the domain now redirects to Hugging Face.
Historical benchmark data was reconstructed using Internet Archive snapshots, Sebastian
Ruder's NLP-Progress catalogue, and direct arXiv/ACL Anthology searches. This did not
materially affect the inventory — the benchmark pool is well-documented through other
channels.

### Capability Scope Revision

Before finalising the benchmark list, the Phase 1 capability ranking was cross-validated
against the full Handa et al. (2025) evidence base. This revealed two important
corrections to the researcher's prior:

- **C01 Content Generation** was significantly under-ranked. Writing and editing
  collectively account for approximately 15–20% of real-world usage — making it the
  second-largest capability, not the fifth.
- **C04 Learning & Education Support** was missing from the prior entirely. It is the
  third-largest capability at ~10–14%, and has been the fastest-growing category across
  subsequent Anthropic Economic Index waves as Claude for Education has scaled.
- **C07 Data Analysis** was consequently dropped from the top five.

The revised top-five scope — **C02, C01, C04, C03, C05** — is the analytical focus for
Phase 3.

### Four Sourcing Channels

Approximately **120 candidate benchmarks** were identified across:

1. **Papers with Code** (reconstructed) — yielded the major NLP task clusters including
   HumanEval, MBPP, SQuAD, MMLU, WMT, and summarisation benchmarks
2. **Frontier model technical reports** — GPT-4, Claude 3/4, Gemini 1.0–2.5, Llama 3/4,
   DeepSeek R1 — yielding cross-lab consensus benchmarks and revealing which capabilities
   each lab prioritises
3. **Targeted literature search** — specifically for underserved-capability benchmarks
   (C01, C04, C05, C08) that do not appear in frontier reports
4. **Leaderboard platforms** — HELM, Open LLM Leaderboard v2, LMSYS Chatbot Arena,
   SWE-bench, BigCodeBench, Artificial Analysis Intelligence Index

### The 18-Benchmark Shortlist

From the 120 candidates, **18 benchmarks were selected** — within the 15–20 scope cap
agreed with the supervisor. Selection balanced three criteria: cross-lab consensus (so
the coverage-gap claim is defensible), direct coverage of underserved capabilities (so
the gap has live alternatives to point to), and format diversity (automated, LLM-as-judge,
human-annotated, agentic).

| #    | Benchmark                        | Year    | Capability | Key Feature                                                     |
| ---- | -------------------------------- | ------- | ---------- | --------------------------------------------------------------- |
| B001 | HumanEval / HumanEval+           | 2021/23 | C02        | Most-cited code benchmark; saturated baseline                   |
| B002 | MBPP / MBPP+                     | 2021/23 | C02        | Broader problem coverage than HumanEval                         |
| B003 | SWE-bench Verified               | 2024    | C02        | De-facto agentic code standard; real GitHub issues              |
| B004 | LiveCodeBench                    | 2024    | C02        | Monthly refresh; contamination-resistant                        |
| B005 | BigCodeBench (Hard)              | 2024    | C02        | Library integration; most realistic C02 benchmark               |
| B006 | IFEval                           | 2023    | C01        | Only C01 benchmark with cross-lab consensus; a proxy            |
| B007 | WritingBench                     | 2025    | C01        | 1239-query direct C01 measure; absent from all frontier reports |
| B008 | EQ-Bench CW v3                   | 2023–  | C01        | LLM-judged Elo; style and voice dimensions                      |
| B009 | HelloBench / LongBench-Write     | 2024    | C01        | Long-form writing; closes the short-prompt gap                  |
| B010 | MathDial                         | 2023    | C04        | 2900 tutoring dialogues; foundational C04 dataset               |
| B011 | MRBench                          | 2025    | C04        | 8 pedagogical dimensions; expert-annotated                      |
| B012 | MathTutorBench                   | 2025    | C04        | 7 pedagogical tasks; public leaderboard                         |
| B013 | MMLU / MMLU-Pro                  | 2020/24 | C03        | Universal knowledge baseline and harder update                  |
| B014 | GPQA Diamond                     | 2023    | C03        | Graduate-level; gated; frontier difficulty standard             |
| B015 | TriviaQA / Natural Questions     | 2017/19 | C03        | Classic open-domain QA; saturation anchors                      |
| B016 | SimpleQA / FACTS Grounding       | 2024    | C03        | Hallucination measurement; cited in Claude 4 / Gemini 2.0       |
| B017 | CriticBench (Tsinghua)           | 2024    | C05        | 15 datasets across 5 domains; only comprehensive C05 benchmark  |
| B018 | Auto-J + Shepherd + MetaCritique | 2023/24 | C05        | Open-ended prose critique; essay feedback; code review          |

Each benchmark was documented across all 27 fields in the database — including authors,
venue, citation count, task type, format, dataset size and source, evaluation metric,
human involvement, primary and secondary capabilities, known limitations, contamination
risk, update frequency, public availability, URLs, and quality ratings on five dimensions
(coherence, accuracy, clarity, relevance, efficiency) with written justifications.

### Key Findings from the Inventory

**The overall quality picture is strong.** The average quality rating across all 18
benchmarks is 4.12 out of 5. Relevance scores are highest (mean 4.28), reflecting that
newer benchmarks are increasingly designed around real-world task fidelity. Efficiency
is the weakest dimension (mean 3.78), driven by the C01, C04, and C05 benchmarks that
require LLM-as-judge or expert-annotation evaluation rather than automated pass/fail.

**Contamination risk is well-managed.** 12 of the 18 benchmarks carry Low contamination
risk, 2 Medium, and 4 High. The High-risk benchmarks (HumanEval, MBPP, MMLU,
TriviaQA/NQ) are all old, static, and widely published — their contamination is the
point, not a disqualifier. The newer underserved-capability benchmarks (WritingBench,
MathTutorBench, CriticBench) are all Low risk by design, since LLM-judge and
reward-model evaluation resists simple memorisation.

**The structural gap is already visible.** When benchmarks are classified by both what
they measure and whether they appear in frontier technical reports, a three-way mismatch
emerges:

- **C02 Code**: 10+ benchmarks appear in frontier reports across all labs. Saturated.
- **C03 Information Retrieval**: 15+ benchmarks appear in frontier reports. Saturated.
- **C01 Content Generation**: Only 2 proxy benchmarks (IFEval, MT-Bench) appear in
  frontier reports. Direct writing-quality benchmarks (WritingBench, EQ-Bench,
  HelloBench/LongBench-Write) exist in the academic literature but are absent from every
  technical report reviewed.
- **C04 Learning & Education**: Zero dedicated pedagogical benchmarks in any frontier
  report. GSM8K and MATH are used as proxies, despite MathTutorBench demonstrating that
  solving ability and teaching ability are negatively correlated once pedagogical
  specialisation is introduced.
- **C05 Review & Feedback**: Zero benchmarks of any kind in any frontier technical
  report. SWE-bench is the implicit proxy (debugging as review), conflating fault
  localisation with artefact critique.

This asymmetry — not a shortage of benchmarks, but a concentration of frontier-report
citations on exactly the capabilities least representative of real-world usage — is the
central empirical argument the project builds toward.

### Outputs Produced

All Phase 2 deliverables were completed:

- `data/phase2/benchmark_candidates.csv` — ~120 candidates, all four channels
- `data/phase2/benchmark_final_list.csv` — 18 selected benchmarks with rationale
- `data/phase2/benchmark_database.csv` — full 27-field database, all 18 benchmarks
- `data/phase2/benchmark_selection_rationale.md` — inclusion/exclusion reasoning per capability
- `data/phase2/access_log.md` — access status for all 18; 3 pending follow-ups flagged
- `outputs/phase2/benchmark_database_FINAL.csv` — verified final copy
- `outputs/phase2/inventory_summary.md` — 2-page narrative summary
- `outputs/phase2/charts/` — 5 charts at 300 DPI (by year, capability, venue, quality ratings, contamination risk)
- `scripts/phase2_benchmark_analysis.py` — fully documented analysis script

**Phase 2 completion criteria: fully met.**

---

## Where the Project Stands and What Comes Next

Both phases are complete and the project is on schedule. The capability taxonomy
(Phase 1) and benchmark database (Phase 2) together constitute the two inputs required
for Phase 3's coverage analysis.

Phase 3 (Weeks 10–13) will construct the capability-benchmark coverage matrix, calculate
usage-weighted gap scores using the formula:

```
Gap Score = Usage_Frequency × (1 − Normalised_Coverage_Score)
```

It will also run five statistical analyses (Pearson correlation, chi-square, temporal
regression), produce five visualisations including the central coverage heatmap, and
write four capability deep-dives. The prediction entering Phase 3, which the data will
either confirm or challenge, is that C04 and C05 carry the highest gap scores, C01 a
moderately high score, and C02/C03 near-zero scores.

One open question I would welcome your view on, Dr Tsakaldis: the emerging C01, C04,
and C05 benchmarks (WritingBench, MathTutorBench, CriticBench) can be framed in Phase 3
either as **solutions to the coverage gap** (they exist; labs should use them) or as
**further evidence of its depth** (they exist but no lab does use them, which itself
needs explaining). The framing has implications for how the Phase 5 recommendations are
pitched. I am inclined toward the latter framing — the absence-from-frontier-reports
finding is the more novel contribution — but would welcome your guidance before Phase 3
begins.

---

*Report prepared: 17 April 2026*
*Leon Kamau Kiunga (201759400)*
