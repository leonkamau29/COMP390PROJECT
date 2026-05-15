# Phase 2 Benchmark Inventory Summary

**Phase:** 2, Week 9
**Inventory version:** v3, aligned to Phase 1 FINAL taxonomy and `benchmark_selection_rationale_v3.md`

---

## 1. Overview

Phase 2 now documents **28 final benchmarks** across all eight capabilities in the Phase 1 FINAL taxonomy. The scope expansion follows the v3 rationale: the February 2026 Anthropic AEI mapping validates C01-C08

---

## 2. Key Metrics

- Total candidate benchmarks screened: 127 documented candidate rows in `benchmark_candidates.csv`.
- Benchmarks selected for final inventory: 28.
- Capability areas covered: 8 (C01-C08).
- Year range: 2021-2025.
- Mean overall quality rating: 4.25 / 5.
- Field completion: 100% of required database fields populated; unavailable evidence is explicitly labelled rather than left blank.

---

## 3. Distribution by Capability


| Capability                                     | Code | Benchmarks | IDs                          | Usage share |
| ---------------------------------------------- | ---- | ---------- | ---------------------------- | ----------- |
| Code Development and Technical Problem Solving | C02  | 5          | B001, B002, B003, B004, B005 | 34.0%       |
| Information Retrieval and Advisory             | C03  | 5          | B006, B007, B008, B009, B010 | 21.4%       |
| Content Generation                             | C01  | 4          | B011, B012, B013, B014       | 17.5%       |
| Data Analysis and Summarisation                | C07  | 4          | B015, B016, B017, B018       | 10.7%       |
| Learning and Education Support                 | C04  | 3          | B019, B020, B021             | 7.8%        |
| Review and Feedback                            | C05  | 3          | B022, B023, B024             | 3.9%        |
| Conversational Interaction and Roleplay        | C08  | 2          | B025, B026                   | 2.9%        |
| Translation and Language Processing            | C06  | 2          | B027, B028                   | 1.9%        |


---

## 4. Quality Ratings Summary


| Dimension  | Mean rating |
| ---------- | ----------- |
| Coherence  | 4.61        |
| Accuracy   | 4.39        |
| Clarity    | 4.21        |
| Relevance  | 4.54        |
| Efficiency | 3.50        |


The strongest dimensions are clarity and relevance, reflecting the decision to replace saturated or weakly adopted legacy tasks with more recent benchmarks grounded in real-world workflows. Efficiency remains the weakest dimension because agentic, writing, tutoring, review, and roleplay benchmarks often require execution environments, LLM judges, reward models, or human validation.

---

## 5. Contamination Risk Summary


| Risk level | Count |
| ---------- | ----- |
| High       | 1     |
| Medium     | 3     |
| Low        | 24    |


High contamination risk is concentrated in legacy static benchmarks such as HumanEval. Most additions in v3 are recent, dynamic, gated, or open-ended, lowering memorisation risk relative to older multiple-choice and short-answer benchmarks.

