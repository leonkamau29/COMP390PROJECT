# Phase 3 Statistical Analysis Report


**Methodological basis:** Phase 3 instructions , using the Phase 1 taxonomy and updated 28-row Phase 2 benchmark database.

## Data Inputs

- Benchmarks analysed: 28 from `outputs/phase2/benchmark_database_FINAL.csv`.
- Capabilities analysed: 8 from `outputs/phase1/capability_taxonomy_FINAL.csv`.
- Non-zero coverage judgements: 50 justified ratings in `data/phase3/coverage_matrix_notes.csv`.
- Usage frequencies were calculated by summing Anthropic AEI top-task `usage_pct` values after mapping each task to the Phase 1 capability taxonomy.

## Key Results

- Highest usage-weighted gap: **Code Development and Technical Problem Solving** (C02), gap score 0.2307.
- Highest normalised benchmark coverage: **Code Development and Technical Problem Solving** (C02), coverage score 0.2357.
- The gap score formula used was: `Gap Score = Usage_Frequency x (1 - Normalized_Coverage_Score)`.

## Gap Score Ranking


| Rank | Capability                                         | Usage frequency | Coverage score | Benchmark count | Average quality | Gap score | Severity |
| ---- | -------------------------------------------------- | --------------- | -------------- | --------------- | --------------- | --------- | -------- |
| 1    | C02 Code Development and Technical Problem Solving | 0.3019          | 0.2357         | 10              | 3.3000          | 0.2307    | High     |
| 2    | C01 Content Generation                             | 0.2568          | 0.1429         | 6               | 3.3333          | 0.2202    | High     |
| 3    | C03 Information Retrieval and Advisory             | 0.1754          | 0.1714         | 7               | 3.4286          | 0.1453    | High     |
| 4    | C04 Learning and Education Support                 | 0.1113          | 0.1714         | 8               | 3.0000          | 0.0922    | High     |
| 5    | C07 Data Analysis and Summarisation                | 0.0751          | 0.2000         | 7               | 4.0000          | 0.0601    | Medium   |
| 6    | C05 Review and Feedback                            | 0.0308          | 0.1286         | 5               | 3.6000          | 0.0269    | Medium   |
| 7    | C06 Translation and Language Processing            | 0.0271          | 0.0714         | 2               | 5.0000          | 0.0252    | Medium   |
| 8    | C08 Conversational Interaction and Roleplay        | 0.0215          | 0.1286         | 5               | 3.6000          | 0.0188    | Low      |


## Statistical Tests


| Analysis                   | Capability | Statistic | p-value | Effect size | 95% CI                                | Interpretation                                                         |
| -------------------------- | ---------- | --------- | ------- | ----------- | ------------------------------------- | ---------------------------------------------------------------------- |
| Pearson correlation        | ALL        | 0.6393    | 0.0878  | 0.6393      | [-0.1189, 0.9266]                     | Higher-usage capabilities tend to receive more benchmark coverage.     |
| Chi-square goodness-of-fit | ALL        | 31.9584   | 0.0     | 0.3022      | Cramer's V bootstrap [0.2019, 0.5280] | Benchmark coverage is not distributed in proportion to observed usage. |
| Temporal linear regression | C01        | 0.5143    | 0.0213  | 0.7714      | Slope [0.1257, 0.9029]                | Positive slope indicates increasing benchmark activity over time.      |
| Temporal linear regression | C02        | 0.7429    | 0.3796  | 0.1958      | Slope [-1.3474, 2.8331]               | Positive slope indicates increasing benchmark activity over time.      |
| Temporal linear regression | C03        | 0.6       | 0.2292  | 0.3345      | Slope [-0.5748, 1.7748]               | Positive slope indicates increasing benchmark activity over time.      |
| Temporal linear regression | C04        | 0.7429    | 0.0086  | 0.8521      | Slope [0.3132, 1.1725]                | Positive slope indicates increasing benchmark activity over time.      |
| Temporal linear regression | C05        | 0.6       | 0.0344  | 0.7132      | Slope [0.0718, 1.1282]                | Positive slope indicates increasing benchmark activity over time.      |
| Temporal linear regression | C06        | 0.2857    | 0.1583  | 0.4286      | Slope [-0.1723, 0.7437]               | Positive slope indicates increasing benchmark activity over time.      |
| Temporal linear regression | C07        | 0.6       | 0.4411  | 0.1543      | Slope [-1.3501, 2.5501]               | Positive slope indicates increasing benchmark activity over time.      |
| Temporal linear regression | C08        | 0.3714    | 0.1164  | 0.4995      | Slope [-0.1447, 0.8876]               | Positive slope indicates increasing benchmark activity over time.      |


## Interpretation

The coverage matrix shows that benchmark availability is shaped by research-community priorities rather than by measured usage alone. Code, data-analysis, knowledge, and newer tutoring benchmarks now have visible coverage, while coverage remains thinner for capabilities whose validity depends on subjective or context-sensitive judgement, such as review, roleplay, and multilingual language support.

The chi-square test should be interpreted as a distributional diagnostic rather than a causal claim. The expected distribution assumes benchmark counts should track Anthropic usage frequencies, which is a defensible gap-analysis baseline but not the only possible allocation rule. Some low-usage capabilities, such as translation, are intentionally represented by mature specialised benchmarks because they have high deployment risk despite lower frequency in the Anthropic top-task file.

The temporal regressions use only six annual observations (2020-2025), so slopes should be read as descriptive signals. They are most useful for identifying where recent benchmark activity is accelerating, not for forecasting long-term research investment.



