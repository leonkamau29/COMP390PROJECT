# Phase 2 Benchmark Inventory Summary

**Project:** Benchmark Coverage Gap — A Systematic Analysis of Real-World AI
Capabilities and Evaluation Practices
**Student:** Leon Kamau Kiunga (201759400)
**Supervisor:** Dr Konstantinos Tsakaldis
**Phase:** 2, Week 9 

---

## 1. Overview

Phase 2 inventoried approximately 120 candidate LLM benchmarks drawn from four
sourcing channels: (1) Papers with Code historical snapshots, (2) frontier model
technical reports from GPT-4, Claude 3/4, Gemini 1.0–2.5, Llama 3/4, and
DeepSeek R1, (3) targeted literature search for underserved-capability benchmarks,
and (4) leaderboard platforms including HELM, Open LLM Leaderboard v2, LMSYS
Chatbot Arena, SWE-bench, BigCodeBench, and the Artificial Analysis Intelligence
Index. The full candidate set is documented in `data/phase2/benchmark_candidates.csv`.

From this pool, **18 benchmarks were selected** for the final inventory, covering
five capability areas identified in Phase 1 as empirically dominant: C02 Code
Development, C01 Content Generation, C04 Learning and Education Support, C03
Information Retrieval and Advisory, and C05 Review and Feedback. The selection
rationale is documented in full in `data/phase2/benchmark_selection_rationale.md`.

---

## 2. Key Findings

| Metric                                                      | Value                       |
| ----------------------------------------------------------- | --------------------------- |
| Total candidate benchmarks inventoried                      | ~120                        |
| Benchmarks selected for final inventory                     | 18                          |
| Year range (final 18)                                       | 2017–2025                  |
| Capability areas covered                                    | 5 (C02, C01, C04, C03, C05) |
| Benchmarks with cross-lab consensus (≥3 frontier reports)  | 10                          |
| Benchmarks absent from all frontier technical reports       | 6                           |
| Average quality rating across all 18 (mean of 5 dimensions) | 3.9 / 5                     |
| Benchmarks with fully automated evaluation                  | 8                           |
| Benchmarks requiring LLM-as-judge or reward model           | 6                           |
| Benchmarks requiring human evaluation                       | 4                           |

---

## 3. Distribution by Capability Area

| Capability                | Benchmarks | IDs        | Real-world usage share |
| ------------------------- | ---------- | ---------- | ---------------------- |
| C02 Code Development      | 5          | B001–B005 | ~37–42%               |
| C01 Content Generation    | 4          | B006–B009 | ~15–20%               |
| C04 Learning & Education  | 3          | B010–B012 | ~10–14%               |
| C03 Information Retrieval | 4          | B013–B016 | ~9–12%                |
| C05 Review & Feedback     | 2          | B017–B018 | ~7–10%                |

The benchmark count is loosely proportional to real-world usage, with one
deliberate inversion: C05 receives only 2 benchmark slots despite being the fifth
most common capability, because the thesis argument requires demonstrating that this
capability is systematically absent from frontier evaluation — not that it lacks
benchmarks in the academic literature.

---

## 4. Distribution by Publication Year

| Year       | Benchmarks | Names                                                                                                                                 |
| ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 2017–2019 | 2          | TriviaQA/NQ (B015)                                                                                                                    |
| 2020–2021 | 3          | MMLU/MMLU-Pro (B013), HumanEval+ (B001), MBPP+ (B002)                                                                                 |
| 2023       | 4          | IFEval (B006), EQ-Bench-CW (B008), MathDial (B010), GPQA (B014)                                                                       |
| 2024       | 6          | SWE-bench-V (B003), LCB (B004), BCB-Hard (B005), HelloBench (B009), SimpleQA/FACTS (B016), CriticBench (B017), Auto-J/Shepherd (B018) |
| 2025       | 3          | WritingBench (B007), MRBench (B011), MathTutorBench (B012)                                                                            |

The preponderance of 2023–2025 benchmarks reflects the maturation of LLM
evaluation: newer benchmarks are needed because older ones saturate as models
improve. However, the newest benchmarks (2025) are concentrated in
underserved capability areas (C01, C04) — precisely those with the largest
coverage gaps — and have not yet achieved the multi-lab citation patterns
needed for frontier-report inclusion.

---

## 5. Distribution by Evaluation Method

| Evaluation method                               | Count | Benchmarks                                     |
| ----------------------------------------------- | ----- | ---------------------------------------------- |
| Automated (pass/fail unit tests or exact match) | 8     | B001, B002, B003, B004, B005, B006, B013, B015 |
| LLM-as-judge (no human in primary loop)         | 4     | B007, B008, B009, B016                         |
| Reward model (trained on human preferences)     | 1     | B012                                           |
| Expert/human annotation (ground truth)          | 3     | B011, B014, B017                               |
| Human annotation + automatic metrics            | 2     | B010, B018                                     |

This distribution reveals a structural tension in benchmark design: the
capabilities most used in the real world (C01 writing, C04 tutoring, C05 review)
require subjective evaluation, while automated metrics are only reliable for
C02 (code execution) and C03 (factual recall). The result is that benchmarks
for the top real-world capabilities are necessarily slower, costlier, and harder
to reproduce — which is one reason frontier labs exclude them from technical
reports.

---

## 6. Quality Ratings Summary

Average quality ratings across the 18 benchmarks on each dimension (scale 1–5):

| Dimension  | Mean rating | Min | Max | Interpretation                                                     |
| ---------- | ----------- | --- | --- | ------------------------------------------------------------------ |
| Coherence  | 4.2         | 3   | 5   | Tasks are generally well-structured and internally consistent      |
| Accuracy   | 4.1         | 3   | 5   | Ground truth reliability is good; weaker for LLM-judged benchmarks |
| Clarity    | 4.3         | 3   | 5   | Instructions and specifications are mostly unambiguous             |
| Relevance  | 4.4         | 3   | 5   | Strong real-world applicability especially for newer benchmarks    |
| Efficiency | 3.7         | 2   | 5   | Wide variation; LLM-judge and agentic benchmarks score lowest      |

The lowest efficiency scores are concentrated in C04 and C05 benchmarks, where
the cost of human annotation or reward-model evaluation creates a scalability
barrier. The highest relevance scores are in C02 (SWE-bench, BigCodeBench) and
C01 (WritingBench, EQ-Bench, HelloBench) — the benchmarks designed to address
real-world tasks rather than proxy tasks.

---

## 7. Contamination Risk Profile

| Risk level | Count | Benchmarks                                                                |
| ---------- | ----- | ------------------------------------------------------------------------- |
| High       | 3     | HumanEval+ (B001), MBPP+ (B002), MMLU/MMLU-Pro (B013), TriviaQA/NQ (B015) |
| Medium     | 2     | SWE-bench-V (B003), BigCodeBench (B005)                                   |
| Low        | 13    | All others                                                                |

High contamination risk is concentrated in the oldest and most widely published
benchmarks (2017–2021). This pattern supports the thesis argument that benchmarks
saturate not only because models improve, but because training data increasingly
overlaps with benchmark content. The newer underserved-capability benchmarks
(WritingBench, MathTutorBench, CriticBench) have low contamination risk
partly by design (LLM-judge and reward-model evaluation resists gaming) and
partly because they are too new to have been included in training data at scale.

---

## 8. Coverage Gap: What the Inventory Reveals

The inventory's primary finding is not quantitative but structural. **Benchmark
supply is heavily concentrated on C02 and C03, while the capabilities ranked
second through fifth in real-world usage (C01, C04, C05) are represented almost
exclusively by benchmarks absent from frontier technical reports.**

Specifically:

- **C02 Code**: 10+ benchmarks cited in frontier reports across all labs.
  The 5-benchmark inventory sample captures the saturation-to-agentic progression.
- **C03 Information Retrieval**: 15+ benchmarks cited in frontier reports.
  The 4-benchmark inventory captures the from-saturation (MMLU, TriviaQA) to
  frontier-difficulty (GPQA) to hallucination-measurement (SimpleQA, FACTS) arc.
- **C01 Content Generation**: Only 2 proxy benchmarks (IFEval, MT-Bench) cited
  in frontier reports. Direct writing-quality benchmarks (WritingBench,
  EQ-Bench, HelloBench) exist but are absent from all technical reports reviewed.
- **C04 Learning & Education**: Zero dedicated pedagogical benchmarks cited in
  frontier reports. Math-solving benchmarks (GSM8K, MATH, AIME) are used as
  proxies despite measuring the opposite skill from tutoring.
- **C05 Review & Feedback**: Zero benchmarks of any kind cited in frontier
  technical reports. SWE-bench is the implicit proxy (debugging as review)
  despite conflating fault localisation with patch generation.

This three-way mismatch — real-world usage rank, academic benchmark availability,
and frontier-report citation — is the empirical foundation for the Phase 3
coverage analysis. The prediction entering Phase 3 is that usage-weighted gap
scores will be highest for C04 and C05, moderately high for C01, and near zero
for C02 and C03.

---

## 9. Completeness Check

All 18 benchmarks have 100% field completion across all 27 database fields.
Fields marked "not reported" or "not available" where information could not be
verified: citation counts for 2025 publications (marked as "<100" or "not yet
established"), GitHub URLs for two benchmarks with pending releases (WritingBench,
MRBench), and the peer-reviewed venue for MathTutorBench (currently arXiv
preprint under TMLR review).

Phase 2 completion criterion status:

- All 15–20 benchmarks fully documented with 100% field completion: **MET (18)**
- All benchmarks cited in ≥2 major model technical reports included: **MET**
  (all 10 cross-consensus benchmarks from frontier reports are in the inventory)
- Recall target ≥90% vs. major model reports: **MET** (all benchmarks from
  the frontier-report cross-lab consensus list appear in B001–B018 or are
  documented as excluded with rationale)

---
