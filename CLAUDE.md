**DATORY INSTRUCTION FOR ALL CLAUDE CODE SESSIONS**

> You MUST read this file in full at the start of every session before writing a single line of code, generating any output, or performing any analysis. This document is the single source of truth for this project. Every decision — architectural, analytical, or methodological — must be traceable back to a section of this file. If you are unsure whether an action is appropriate, check this file first. Do not deviate from the methodology described here without explicit instruction from the researcher (Leon Kamau Kiunga, Student ID: 201759400).

---

## TABLE OF CONTENTS

1. [Project Identity](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#1-project-identity)
2. [Core Problem &amp; Motivation](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#2-core-problem--motivation)
3. [Research Objectives](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#3-research-objectives)
4. [Methodology Overview](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#4-methodology-overview)
5. [Data Sources &amp; Access Rules](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#5-data-sources--access-rules)
6. [Phase 1: Capability Framework Development (Weeks 1–4)](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#6-phase-1-capability-framework-development-weeks-14)
7. [Phase 2: Benchmark Inventory (Weeks 5–9)](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#7-phase-2-benchmark-inventory-weeks-59)
8. [Phase 3: Coverage Analysis (Weeks 10–13)](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#8-phase-3-coverage-analysis-weeks-1013)
9. [Phase 4: Expert Validation (Weeks 14–16)](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#9-phase-4-expert-validation-weeks-1416)
10. [Phase 5: Recommendations &amp; Toolkit (Weeks 17–20)](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#10-phase-5-recommendations--toolkit-weeks-1720)
11. [Writing &amp; Thesis (Weeks 21–24)](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#11-writing--thesis-weeks-2124)
12. [Technical Environment &amp; Standards](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#12-technical-environment--standards)
13. [File &amp; Folder Structure](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#13-file--folder-structure)
14. [Quality Standards &amp; Success Criteria](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#14-quality-standards--success-criteria)
15. [Risk Flags &amp; Escalation Rules](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#15-risk-flags--escalation-rules)
16. [Key Literature &amp; Citation Standards](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#16-key-literature--citation-standards)
17. [Glossary](https://claude.ai/chat/ea69af48-96e5-4cfa-8d10-53ec05bdb4c1#17-glossary)

---

## 1. PROJECT IDENTITY

| Field                     | Value                                                                                                |
| ------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Full Title**      | Benchmark Coverage Gap: A Systematic Analysis of Real-World AI Capabilities and Evaluation Practices |
| **Student**         | Leon Kamau Kiunga                                                                                    |
| **Student ID**      | 201759400                                                                                            |
| **Supervisor**      | Dr Konstantinos Tsakaldis                                                                            |
| **Submission Date** | End of Week 24                                                                                       |
| **Total Duration**  | 24 weeks (~470 hours)                                                                                |
| **Degree**          | Honours Research Project (BCS-aligned)                                                               |
| **Project Type**    | Research-focused (not software product); primary deliverable is the thesis                           |

---

## 2. CORE PROBLEM & MOTIVATION

### The Disconnect

LLM benchmarks (e.g., MMLU, HumanEval, GSM8K) drive major decisions — model selection, research priorities, deployment choices — but they do not reflect how people actually use LLMs.

### Evidence of the Gap

- **Handa et al. (2025)** analysed 4 million Claude.ai conversations mapped to O*NET tasks. Findings:
  - **Technical assistance** : 65.1% of usage
  - **Reviewing work** (editing, feedback, improving content): 58.9% of usage
  - **Information retrieval** : 16.6%
  - **Summarization** : 16.6%
  - **Critical finding** : "Reviewing work" has NO dedicated evaluation framework despite being the second most common use case.
- **Xu et al. (2025)** — TheAgentCompany: top models complete only 30% of autonomous workplace tasks despite strong benchmark scores.
- **Pezeshkpour & Hruschka** — Changing answer order in MMLU shifts model rankings by ~8 positions.
- **Singh et al. (2025)** — Leaderboard Illusion: companies selectively disclose results, distorting rankings by up to 112%.
- **Balloccu et al. (2024)** — Widespread data contamination in closed-source models.
- **Jain et al. (2024)** — LLM performance on Codeforces problems drops sharply after training cutoff dates, evidence of memorisation not capability.

### Why This Matters

1. Models score well on benchmarks but fail at real user tasks.
2. Research effort flows toward well-benchmarked capabilities, leaving practical functions underserved.
3. Deployment decisions use metrics that don't predict real-world utility.
4. No systematic, usage-weighted map of the entire benchmark ecosystem exists.

### This Project's Contribution

A systematic, empirically grounded framework that:

- Maps what benchmarks actually test vs. what users actually do
- Quantifies gaps weighted by real usage frequency
- Provides actionable recommendations and a reusable assessment toolkit

---

## 3. RESEARCH OBJECTIVES

Execute ALL of the following. None are optional unless explicitly scoped down by Leon.

| #  | Objective                                                                                                                                                | Deliverable                                                                                           |
| -- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| O1 | Build empirically grounded capability taxonomy from real usage data                                                                                      | Taxonomy document with formal definitions, decision rules, sub-categories, 5+ examples per capability |
| O2 | Compile standardised inventory of 15–20 major LLM benchmarks (originally 40–50; scoped to 15–20 across 4–5 capability areas per supervisor feedback) | Structured database (Excel/CSV) with all metadata fields                                              |
| O3 | Map benchmarks to capabilities via coverage matrix                                                                                                       | Coverage matrix with quality ratings; heatmaps and charts                                             |
| O4 | Quantify gaps using usage-weighted gap scores                                                                                                            | Gap score rankings with statistical analysis                                                          |
| O5 | Conduct qualitative deep-dive case analysis                                                                                                              | 3–4 case studies (3–5 pages each)                                                                   |
| O6 | Validate framework via expert survey                                                                                                                     | Survey instrument, response data, revision log                                                        |
| O7 | Produce 3–5 new benchmark design specifications                                                                                                         | Specification documents (5–8 pages each)                                                             |
| O8 | Build Assessment Toolkit                                                                                                                                 | Excel workbook + PDF documentation (10–15 pages)                                                     |
| O9 | Write and submit thesis                                                                                                                                  | Complete thesis document                                                                              |

> **SCOPE NOTE** : The benchmark inventory was revised from 40–50 benchmarks to **15–20 benchmarks across 4–5 capability areas** following critical feedback rating the initial proposal 7.5/10. Do not revert to the larger scope unless Leon explicitly instructs you to.

---

## 4. METHODOLOGY OVERVIEW

### Approach

Mixed-methods: systematic literature review + thematic analysis + quantitative gap assessment + expert validation.

### Five Sequential Phases

```
Phase 1 (Wk 1–4):   Capability Framework Development
Phase 2 (Wk 5–9):   Benchmark Inventory
Phase 3 (Wk 10–13): Coverage Analysis
Phase 4 (Wk 14–16): Expert Validation
Phase 5 (Wk 17–20): Recommendations & Toolkit
Writing  (Wk 21–24): Thesis Completion
```

Each phase **must** be completed before the next begins. Do not skip ahead.

### Analytical Methods

- **Qualitative** : Braun & Clarke (2006) six-phase thematic analysis
- **Quantitative** : Pearson correlation, chi-square, linear regression, descriptive statistics, gap score formula (defined in Phase 3)
- **Validation** : Cohen's κ (target > 0.8), Fleiss' κ for multi-rater expert data, inter-coder reliability on 10% subsample

---

## 5. DATA SOURCES & ACCESS RULES

### Primary Empirical Sources (No Ethics Required)

| Source                                                  | Description                                                                          | Use in Project                                                   |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **Anthropic Economic Index (Handa et al., 2025)** | 4M Claude conversations mapped to O*NET tasks; top 100 tasks with usage percentages  | PRIMARY: capability taxonomy validation, usage frequency weights |
| **WILDCHAT Dataset**                              | Anonymised public ChatGPT conversations; use a sample of ~1,000                      | SECONDARY: cross-validation of capability taxonomy               |
| **O*NET Occupational Database**                   | US Dept of Labor; Detailed Work Activities across occupations                        | Cross-reference for task categorisation                          |
| **Academic Papers & Technical Reports**           | arXiv, ACL Anthology, model technical reports (GPT, Claude, Gemini, Llama, DeepSeek) | Benchmark inventory metadata                                     |
| **GitHub Repositories**                           | Public benchmark codebases                                                           | Verification of benchmark characteristics                        |
| **Papers with Code**                              | Benchmarking catalogue                                                               | Systematic benchmark discovery                                   |

### Primary Research Data (Ethics Approval Required — Week 12+)

| Source                             | Description                                                                  | Restrictions                                                                                                                                   |
| ---------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Expert Validation Survey** | 15–20 invitations; target 5–10 responses; AI researchers and practitioners | Do NOT deploy survey until ethics approval confirmed. Data stored on university Google Drive. Anonymised as P1, P2, etc. Deleted post-marking. |

### Data Management Rules

- All data stored on university OneDrive with regular backups
- Git version control for all code and documents
- Research data publicly released post-submission (GitHub) EXCEPT survey responses (deleted per ethics protocol)
- No personal data in any file unless anonymised
- Comply with UK GDPR at all times

---

## 6. PHASE 1: CAPABILITY FRAMEWORK DEVELOPMENT (Weeks 1–4)

### Goal

Produce a validated capability taxonomy that covers ≥95% of documented real-world LLM usage patterns.

### Week 1 — Literature Extraction

 **Objective** : Extract 100–200 concrete task instances from empirical sources.

 **Instructions** :

1. Review the following sources systematically:

- Handa et al. (2025) — extract all mentioned tasks/activities
- WILDCHAT dataset — sample 1,000 conversations, extract task types
- O*NET Detailed Work Activities — extract AI-relevant tasks
- 10–20 academic papers on AI usage and adoption

2. Record every task in a structured spreadsheet with these EXACT fields:

- `source` (citation)
- `task_description` (verbatim or close paraphrase)
- `domain` (e.g., writing, coding, research)
- `frequency` (if reported; otherwise leave blank)
- `context` (occupational/personal/educational)
- `source_type` (empirical study / survey / usage log)

3. Target: **100–200 task instances documented** before moving to Week 2.
4. Save as: `data/phase1/task_instances_raw.csv`
   *Output** : `data/phase1/task_instances_raw.csv`

---

### Week 2 — Thematic Analysis

 **Objective** : Apply Braun & Clarke (2006) six-phase thematic analysis to derive 6–10 core capabilities.

 **The Six Phases — Execute in strict order** :

1. **Content Familiarisation** : Read all 100–200 task instances. Write a brief memo (200–300 words) on initial impressions. Save as `data/phase1/familiarisation_memo.md`.
2. **Open Coding** : Assign a preliminary descriptive label to each task instance. Add column `open_code` to the spreadsheet. Codes should be short, descriptive, in the researcher's own words (e.g., "fix grammar in document", "explain algorithm", "generate email draft").
3. **Axial Coding** : Group similar open codes into broader categories. Add column `axial_category`. Aim for 15–25 intermediate categories at this stage.
4. **Selective Coding** : Collapse axial categories into **6–10 core capabilities** representing distinct modes of LLM interaction. Add column `core_capability`. Each capability must be meaningfully distinct — no significant overlap.
5. **Define and Name Themes** : Write a formal definition for each capability (2–4 sentences). Include explicit decision rules: "A task belongs to capability X if and only if..." Document how to resolve edge cases. Save as `data/phase1/capability_definitions_draft.md`.
6. **Produce Structured Taxonomy** : Compile final taxonomy document with:

- Formal name and definition for each capability
- Hierarchical structure showing sub-categories
- Decision rules for classification
- Minimum 5 worked examples per capability drawn from the task instances
- Edge cases and ambiguities explicitly addressed
- Save as `outputs/phase1/capability_taxonomy_v1.md`

 **Output Files** :

- `data/phase1/task_instances_coded.csv` (with open_code, axial_category, core_capability columns)
- `data/phase1/familiarisation_memo.md`
- `data/phase1/capability_definitions_draft.md`
- `outputs/phase1/capability_taxonomy_v1.md`

---

### Week 3 — Validation

 **Objective** : Validate taxonomy achieves ≥95% coverage of Anthropic's top 100 tasks; calculate inter-coder reliability.

 **Instructions** :

1. Obtain Anthropic's top 100 tasks (from Handa et al., 2025 — these represent 50% of all usage).
2. For each of the 100 tasks, map it to the primary capability in the taxonomy. Record mapping in `data/phase1/anthropic_top100_mapping.csv` with fields: `task`, `mapped_capability`, `confidence` (high/medium/low), `justification`.
3. Calculate coverage: `coverage = (tasks_mapped / 100) * 100` .
4. For any task that does not map cleanly, record it in `data/phase1/unmapped_tasks.csv` and revise the taxonomy accordingly (add sub-category, refine definition, or add new capability if justified).
5. **Inter-coder reliability** : Select 10% of coded data (10 tasks from each source = ~20 tasks). Have a second coder (colleague or supervisor) independently code these. Calculate Cohen's κ using the formula: κ = (P_o - P_e) / (1 - P_e).
6. Save reliability results as `data/phase1/intercoder_reliability.csv`.
   *Output Files** :

- `data/phase1/anthropic_top100_mapping.csv`
- `data/phase1/unmapped_tasks.csv`
- `data/phase1/intercoder_reliability.csv`

---

### Week 4 — Documentation

 **Objective** : Produce the final, publication-ready capability taxonomy document.

 **Instructions** :

1. Incorporate all revisions from Week 3 validation into the taxonomy.
2. Final taxonomy document must include:

- **Formal capability definitions** (precise, unambiguous)
- **Decision rules** for classification (if/then format)
- **Hierarchical structure** with sub-categories labelled
- **Minimum 5 examples per capability** drawn from real task instances
- **Edge cases and ambiguities** explicitly addressed with resolutions
- **Validation summary** : coverage %, Cohen's κ achieved

3. Save final version as `outputs/phase1/capability_taxonomy_FINAL.md`
4. Export taxonomy as structured CSV for use in Phase 3: `outputs/phase1/capability_taxonomy_FINAL.csv` (columns: `capability_id`, `capability_name`, `definition`, `sub_categories`, `decision_rule`, `examples`)
   *Phase 1 Completion Criterion** : Taxonomy covers ≥95% of Anthropic top 100 tasks AND Cohen's κ > 0.8.

---

## 7. PHASE 2: BENCHMARK INVENTORY (Weeks 5–9)

### Goal

Compile a standardised, verified inventory of **15–20 LLM benchmarks** spanning 4–5 capability areas identified in Phase 1.

> **SCOPE REMINDER** : The original proposal specified 40–50 benchmarks. This was revised DOWN to 15–20 benchmarks across 4–5 capability areas. Do not expand scope without Leon's explicit instruction.

### Week 5 — Systematic Search

 **Objective** : Identify and screen benchmarks to compile the final list of 15–20.

 **Search Strategy — Execute ALL four approaches** :

1. **Papers with Code** : Filter for 'Natural Language Processing' and 'Language Models'. Export all listed benchmarks. Record in `data/phase2/benchmark_candidates.csv`.
2. **Technical Reports** : Review these specific model releases and extract all cited benchmarks:

- GPT-4 technical report
- Claude 3 / Claude 3.5 technical report
- Google Gemini technical report
- Llama 2 / Llama 3 technical report
- DeepSeek R1 technical report
  Record in same spreadsheet with column `found_in_report`.

1. **Google Scholar** : Search "LLM benchmark" OR "language model evaluation" filtered to 2020–2025. Screen by citation count ≥50. Add to spreadsheet.
2. **Snowball Sampling** : Check references in Handa et al. (2025), Xu et al. (2025), and Singh et al. (2025). Add newly found benchmarks.

**Inclusion Criteria** (ALL must be met):

- Publicly documented (paper or technical report available)
- Used by ≥2 major models or labs
- Tests at least one capability identified in Phase 1 taxonomy

 **Selection for Final 15–20** :

- Prioritise benchmarks that span all 4–5 capability areas identified in Phase 1
- Ensure the most frequently referenced benchmarks are included
- Aim for balanced representation across capability areas (not all benchmarks from one area)
- Document rationale for inclusion/exclusion in `data/phase2/benchmark_selection_rationale.md`

 **Output Files** :

- `data/phase2/benchmark_candidates.csv` (all candidates found)
- `data/phase2/benchmark_final_list.csv` (final 15–20 selected)
- `data/phase2/benchmark_selection_rationale.md`

---

### Weeks 6–8 — Standardised Analysis

 **Objective** : Complete structured analysis template for each of the 15–20 benchmarks. Allocate ~40 minutes per benchmark.

 **For each benchmark, complete ALL fields in the database** :

| Field                      | Instructions                                                     |
| -------------------------- | ---------------------------------------------------------------- |
| `benchmark_id`           | B001, B002, etc.                                                 |
| `name`                   | Full official name                                               |
| `abbreviation`           | Common abbreviation (e.g., MMLU)                                 |
| `year`                   | Year of first publication                                        |
| `authors`                | Full author list                                                 |
| `venue`                  | Publication venue (conference, journal, arXiv)                   |
| `citation_count`         | Google Scholar citation count (record date checked)              |
| `task_type`              | Multiple choice / generation / classification / etc.             |
| `format`                 | How tasks are presented to the model                             |
| `domain`                 | Subject area(s) covered                                          |
| `dataset_size`           | Number of items in test set                                      |
| `dataset_source`         | How dataset was constructed                                      |
| `evaluation_metric`      | Primary metric (accuracy, BLEU, pass@k, etc.)                    |
| `human_involvement`      | Yes/No/Partial — human judges in loop?                          |
| `primary_capability`     | Map to Phase 1 taxonomy (capability_id)                          |
| `secondary_capabilities` | Additional capabilities tested (capability_ids, comma-separated) |
| `known_limitations`      | Documented issues (contamination, bias, etc.)                    |
| `contamination_risk`     | High/Medium/Low — with justification                            |
| `update_frequency`       | Static / Periodic / Continuous                                   |
| `public_availability`    | Fully public / Partial / Closed                                  |
| `github_url`             | Link to benchmark repository if available                        |
| `paper_url`              | arXiv or DOI link                                                |
| `quality_coherence`      | 1–5 rating (task consistency and logic)                         |
| `quality_accuracy`       | 1–5 rating (ground truth reliability)                           |
| `quality_clarity`        | 1–5 rating (instruction clarity)                                |
| `quality_relevance`      | 1–5 rating (real-world applicability)                           |
| `quality_efficiency`     | 1–5 rating (cost/complexity of evaluation)                      |
| `quality_notes`          | Justification for ratings (required)                             |

 **Quality Rating Scale** :

- 5 = Excellent (meets standard fully)
- 4 = Good (minor issues)
- 3 = Adequate (notable issues but usable)
- 2 = Poor (significant problems)
- 1 = Very Poor (fundamental flaws)

 **Procedure for each benchmark** :

1. Read benchmark paper/documentation
2. Access dataset on GitHub/Hugging Face if available
3. Search Google Scholar for follow-up papers, critiques, replications
4. Complete all fields above
5. Record any access issues in `data/phase2/access_log.md`
   *Output Files** :

- `data/phase2/benchmark_database.csv` (master database, all benchmarks, all fields)
- `data/phase2/access_log.md` (any paywalls, access failures, notes)

---

### Week 9 — Database Construction & Descriptive Analysis

 **Objective** : Compile final database, verify completeness, run basic descriptive statistics.

 **Instructions** :

1. Audit database for completeness: every field must be filled for every benchmark. Missing data must be documented in `quality_notes` as "not reported" or "not available" — do not leave blanks.
2. Run descriptive analysis using Python (pandas):

- Distribution of benchmarks by year (bar chart)
- Distribution by primary capability (bar chart)
- Distribution by publication venue (bar chart)
- Distribution of quality ratings across 5 dimensions (radar chart or grouped bar)
- Contamination risk summary (pie chart)

3. Save all charts to `outputs/phase2/charts/`
4. Write a 1–2 page summary of the benchmark landscape: `outputs/phase2/inventory_summary.md`
   *Output Files** :

- `outputs/phase2/benchmark_database_FINAL.csv`
- `outputs/phase2/charts/` (all visualisations)
- `outputs/phase2/inventory_summary.md`

 **Phase 2 Completion Criterion** : All 15–20 benchmarks fully documented with 100% field completion. All benchmarks cited in ≥2 major model technical reports are included in the inventory (target recall ≥90%).

---

## 8. PHASE 3: COVERAGE ANALYSIS (Weeks 10–13)

### Goal

Build a coverage matrix, quantify gaps using usage-weighted scores, and conduct qualitative case analysis.

### Week 10 — Capability-Benchmark Mapping

 **Objective** : Construct the capability-benchmark coverage matrix.

 **Instructions** :

1. Create matrix: rows = benchmarks (from Phase 2), columns = capabilities (from Phase 1).
2. For each cell, determine:

- **0** : Capability not tested by this benchmark
- **1–5** : Quality rating for how well the benchmark tests this capability (use the same scale as Phase 2 quality ratings)

3. Ratings must be justified. For each non-zero cell, record a justification in a companion notes file: `data/phase3/coverage_matrix_notes.csv` (fields: `benchmark_id`, `capability_id`, `rating`, `justification`)
4. Also record for each benchmark:

- Primary capability tested (forced choice — pick ONE even if multiple apply)
- Secondary capabilities (all others with rating ≥2)

5. Save matrix as `data/phase3/coverage_matrix.csv`
6. Compute per-capability aggregate metrics:

- `total_coverage_score` = Σ(quality ratings across all benchmarks) / max possible
- `benchmark_count` = number of benchmarks testing this capability (rating ≥1)
- `average_quality` = mean rating across benchmarks that test this capability (rating ≥1)
  Save as `data/phase3/capability_coverage_metrics.csv`
  *Output Files** :
- `data/phase3/coverage_matrix.csv`
- `data/phase3/coverage_matrix_notes.csv`
- `data/phase3/capability_coverage_metrics.csv`

---

### Week 11 — Gap Quantification & Visualisation

 **Objective** : Calculate usage-weighted gap scores, run statistical analyses, create all visualisations.

#### Gap Score Formula

```
Gap Score = Usage_Frequency × (1 - Normalized_Coverage_Score)
```

Where:

- `Usage_Frequency` = proportion of usage from Anthropic top 100 task data (e.g., 0.589 for reviewing work)
- `Normalized_Coverage_Score` = `total_coverage_score / max_possible_total_coverage_score` (scale 0–1)
- Higher Gap Score = more urgent gap

#### Statistical Analyses — Run ALL of the following:

1. **Pearson Correlation** : usage frequency vs. total coverage score per capability. Test H₀: no correlation. Report r, p-value, 95% CI.
2. **Chi-square Test** : Is benchmark coverage distributed across capabilities in proportion to usage frequency, or are some capabilities systematically over/under-represented? Use observed = benchmark counts per capability; expected = proportional to usage frequency.
3. **Temporal Trend Analysis** : Linear regression of benchmark count (y) ~ year of publication (x) for each capability separately. Report slope, R², p-value. Are coverage gaps widening or narrowing over time?

Save all statistical results as `data/phase3/statistical_analysis_results.csv` and `outputs/phase3/statistical_analysis_report.md`.

#### Visualisations — Produce ALL of the following:

| Chart                     | Description                                                                                                          | Save As                                                 |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Coverage Heatmap          | Matrix with capabilities on y-axis, benchmarks on x-axis, coloured by quality rating (0–5)                          | `outputs/phase3/charts/coverage_heatmap.png`          |
| Gap Score Bar Chart       | Capabilities ranked by gap score, horizontal bars, colour-coded by severity                                          | `outputs/phase3/charts/gap_scores.png`                |
| Usage vs Coverage Scatter | x = usage frequency, y = coverage score, one point per capability, annotated with capability names                   | `outputs/phase3/charts/usage_vs_coverage_scatter.png` |
| Temporal Trend            | Line chart showing benchmark count per capability over years 2020–2025                                              | `outputs/phase3/charts/temporal_trends.png`           |
| Quality Dimension Radar   | Radar/spider chart showing average quality across 5 dimensions (coherence, accuracy, clarity, relevance, efficiency) | `outputs/phase3/charts/quality_radar.png`             |

Use `matplotlib` and `seaborn`. Ensure all charts have: title, labelled axes, legend, and source attribution. Export at 300 DPI minimum.

 **Output Files** :

- `data/phase3/gap_scores.csv`
- `data/phase3/statistical_analysis_results.csv`
- `outputs/phase3/charts/` (all 5 charts)
- `outputs/phase3/statistical_analysis_report.md`

---

### Week 12 — Qualitative Deep Dives

 **Objective** : Write detailed analysis (3–5 pages each) for 4 capabilities spanning the coverage spectrum.

**Select exactly these 4 capability types** (substitute with actual capability names from Phase 1 taxonomy, but maintain this coverage profile):

1. **Highest Gap Capability** — e.g., "Reviewing Work" (the capability with the highest gap score)
2. **Well-Covered Capability** — e.g., "Information Retrieval" (the capability with the highest coverage)
3. **Moderate Coverage Capability** — e.g., "Text Generation" (mid-range gap score)
4. **Niche Gap Capability** — e.g., "Data Structuring" (low usage but disproportionately low coverage)
   *For each deep dive, write sections covering ALL of the following** :
5. Current evaluation landscape (which benchmarks exist, what they measure, aggregate quality assessment)
6. Technical and practical challenges to evaluation (why is this hard to benchmark?)
7. Real-world importance with ≥3 concrete examples of use (drawn from usage data)
8. Consequences of inadequate evaluation (what goes wrong in deployment?)
9. Requirements for adequate coverage (what would a good benchmark need?)

Save each as: `outputs/phase3/deep_dive_[capability_name].md`

---

### Week 13 — Case Studies

 **Objective** : Document 5–10 real-world cases of high benchmark scores + real-world deployment failures.

 **Procedure** :

1. Conduct systematic literature search for documented deployment failures:

- Search Google Scholar: "LLM deployment failure", "benchmark performance gap", "AI evaluation mismatch"
- Search industry reports, conference proceedings
- Include examples from key papers in this project (TheAgentCompany, medical LLM failures)

2. For each case study, document ALL of the following:

- Model name and benchmark performance (specific scores if available)
- Real-world deployment context
- Specific failure mode observed
- Capability gap implicated (map to taxonomy)
- Consequences (severity, scope)
- Source documentation (full citation)

3. Target: 5–10 cases. Minimum acceptable: 3 well-documented cases.
4. Save as `outputs/phase3/case_studies.md`
   *Phase 3 Completion Criterion** : Coverage matrix complete with justified ratings; gap scores computed for all capabilities; ≥5 statistical tests run and reported; all visualisations produced; 4 deep dives written; ≥3 case studies documented.

---

## 9. PHASE 4: EXPERT VALIDATION (Weeks 14–16)

### Goal

Validate framework and findings through detailed literature based validation ie published papers and research.

---

## 10. PHASE 5: RECOMMENDATIONS & TOOLKIT (Weeks 17–20)

### Goal

Produce actionable benchmark design specifications and a reusable assessment toolkit.

### Weeks 17–18 — Benchmark Design Specifications

 **Objective** : Write detailed specifications for 3–5 new benchmarks targeting the highest-priority gaps.

 **Selection** : Choose benchmarks addressing the top 3–5 gap scores from Phase 3. Ensure no two proposed benchmarks target the same capability.

 **Each specification document must include ALL of the following sections** :

1. **Capability Measured and Rationale** — what capability this benchmark tests and why it is important (reference Phase 3 gap analysis and usage data)
2. **Task Structure** — with minimum 10 worked example items in full detail (input, expected output, evaluation criteria)
3. **Dataset Composition** — size, domains covered, sources of data, construction method, quality control procedures
4. **Evaluation Methodology** — primary and secondary metrics, scoring procedure, role of human judges (if any), automation feasibility
5. **Validation Strategy** — how to establish the benchmark's own validity: pilot testing plan, inter-rater reliability protocol, ground truth verification
6. **Implementation Requirements** — time estimate, cost estimate, expertise required, infrastructure needed
7. **Expected Challenges and Mitigations** — specific challenges for this benchmark type and concrete solutions
8. **Comparison to Existing Benchmarks** — how this differs from and improves upon existing benchmarks in this capability area

Save each specification as: `outputs/phase5/benchmark_spec_[capability_name].md`

 **Reference** : Base designs on successful structural patterns from EXISTING benchmarks. Adapt proven approaches — do not invent entirely new evaluation paradigms without strong justification.

---

### Week 19 — Assessment Toolkit

 **Objective** : Build a practical Excel workbook enabling practitioners to assess benchmark relevance for their use case.

**Toolkit Components** (ALL required):

#### Excel Workbook: `outputs/phase5/assessment_toolkit.xlsx`

| Tab                      | Contents                                                                                                                          |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `Instructions`         | Step-by-step guide to using the toolkit; prerequisites; glossary of terms                                                         |
| `Capability_Checklist` | Dropdown-based checklist for users to identify which capabilities are relevant to their use case; linked to taxonomy from Phase 1 |
| `Benchmark_Profiles`   | Condensed data from Phase 2 database: one row per benchmark, key fields only                                                      |
| `Quality_Rubric`       | Five-dimension rubric (coherence, accuracy, clarity, relevance, efficiency) with definitions and scoring guidance                 |
| `Coverage_Calculator`  | User inputs their capability priorities (weights); auto-calculates weighted coverage score for their context using Phase 3 data   |
| `Worked_Examples`      | Minimum 3 worked case studies showing toolkit in action for different use-case scenarios                                          |
| `Interpretation_Guide` | Guidance on reading results: what scores mean, how to act on findings, limitations                                                |

 **Excel formulas must be** :

- Self-contained (no external dependencies)
- Clearly commented with cell notes
- Tested for correctness before delivery

#### PDF Documentation: `outputs/phase5/assessment_toolkit_documentation.pdf`

Length: 10–15 pages. Must include:

- Framework rationale (why these dimensions, why this structure)
- Step-by-step instructions for each toolkit component
- Common questions and answers
- Limitations of the toolkit
- How to update the toolkit as new benchmarks emerge

---

### Week 20 — Recommendations Synthesis

 **Objective** : Produce the final consolidated recommendations document.

 **Document** : `outputs/phase5/recommendations_synthesis.md`

 **Required Sections** :

1. **Executive Summary** (1 page max): key findings, top 3 recommendations
2. **Prioritised Gap List** : all capability gaps ranked by gap score, with brief description of each
3. **Detailed Benchmark Proposals** : summary of each specification (link to full spec documents)
4. **Improvement Suggestions for Existing Benchmarks** : for each of the 15–20 benchmarks in the inventory, suggest specific improvements where warranted
5. **Implementation Roadmap** : realistic timeline for the research community to address top gaps (short-term 0–1 year, medium-term 1–3 years, long-term 3+ years)
6. **Cost-Benefit Analysis** : rough estimates of implementation cost vs. expected improvement in evaluation validity for the top 3 proposed benchmarks
   *Phase 5 Completion Criterion** : 3–5 complete benchmark specifications; toolkit pilot-tested by 2 non-expert colleagues successfully; recommendations synthesis document complete.

---

## 11. WRITING & THESIS (Weeks 21–24)

### Goal

Produce a complete, submission-ready thesis demonstrating first-class honours quality.

### Thesis Structure

Write chapters in this order (earlier phases provide content for earlier chapters):

| Chapter                              | Content Source                                        | Target Length      |
| ------------------------------------ | ----------------------------------------------------- | ------------------ |
| Abstract                             | Summary of all phases                                 | 300–500 words     |
| Introduction                         | Problem statement, research objectives, contributions | 1,500–2,000 words |
| Literature Review                    | Phase 1 background + additional literature            | 4,000–5,000 words |
| Methodology                          | Phase overview, methods justification, ethics         | 2,500–3,500 words |
| Phase 1 Results: Capability Taxonomy | Phase 1 outputs                                       | 2,000–3,000 words |
| Phase 2 Results: Benchmark Inventory | Phase 2 outputs                                       | 2,000–3,000 words |
| Phase 3 Results: Coverage Analysis   | Phase 3 outputs                                       | 3,000–4,000 words |
| Phase 4 Results: Expert Validation   | Phase 4 outputs                                       | 1,500–2,500 words |
| Phase 5: Recommendations             | Phase 5 outputs                                       | 2,500–3,500 words |
| Discussion                           | Synthesis, implications, limitations                  | 2,000–3,000 words |
| Conclusion                           | Summary, future work                                  | 800–1,200 words   |
| References                           | All cited sources                                     | APA 7th format     |
| Appendices                           | Survey instrument, full taxonomy, full database       | As needed          |

### Writing Standards

- Academic formal register; no contractions; third-person perspective
- APA 7th edition citations throughout
- Every empirical claim must be cited
- Every figure and table must have a caption and be referenced in text
- Limitations must be addressed honestly in each results chapter AND the discussion
- Methodology decisions must be justified — explain why this approach over alternatives

### Supervisor Review Schedule

- Week 21: Draft chapters 1–4 to supervisor
- Week 22: Draft chapters 5–8 to supervisor
- Week 23: Draft chapters 9–11 + full thesis to supervisor
- Week 24: Final revisions and submission

---

## 12. TECHNICAL ENVIRONMENT & STANDARDS

### Required Python Packages

```
python >= 3.10
pandas
numpy
matplotlib
seaborn
scipy
openpyxl       # for Excel output
reportlab      # for PDF generation
jupyter        # for notebooks (optional but recommended)
```

Install via: `pip install pandas numpy matplotlib seaborn scipy openpyxl reportlab jupyter`

### Code Standards

- Every script must have a docstring explaining its purpose, inputs, and outputs
- Every function must have a docstring
- No hardcoded paths — use relative paths from project root
- All random operations must set a random seed: `np.random.seed(42)`
- All statistical tests must report: test statistic, p-value, effect size, confidence interval
- All charts must be saved as PNG at ≥300 DPI
- Use `requirements.txt` in project root; keep it updated

### Version Control

- Git repository initialised at project root
- Commit after every significant piece of work
- Commit messages must be descriptive (not "update" or "fix")
- `.gitignore` must exclude: raw data files with any PII, Excel temp files, `__pycache__`

### File Naming Conventions

- All lowercase, underscores for spaces, no special characters
- Data files: descriptive name + version if applicable (e.g., `benchmark_database_v2.csv`)
- Output files: descriptive name + FINAL when complete (e.g., `capability_taxonomy_FINAL.md`)
- Scripts: named by function (e.g., `compute_gap_scores.py`, `generate_heatmap.py`)

---

## 13. FILE & FOLDER STRUCTURE

```
project_root/
├── README.md                         # Project overview and setup instructions
├── requirements.txt                  # Python dependencies
├── CLAUDE_PROJECT_REFERENCE.md       # THIS FILE — always read first
│
├── data/
│   ├── phase1/
│   │   ├── task_instances_raw.csv
│   │   ├── task_instances_coded.csv
│   │   ├── familiarisation_memo.md
│   │   ├── capability_definitions_draft.md
│   │   ├── anthropic_top100_mapping.csv
│   │   ├── unmapped_tasks.csv
│   │   ├── wildchat_coding.csv
│   │   └── intercoder_reliability.csv
│   ├── phase2/
│   │   ├── benchmark_candidates.csv
│   │   ├── benchmark_final_list.csv
│   │   ├── benchmark_database.csv
│   │   ├── benchmark_selection_rationale.md
│   │   └── access_log.md
│   ├── phase3/
│   │   ├── coverage_matrix.csv
│   │   ├── coverage_matrix_notes.csv
│   │   ├── capability_coverage_metrics.csv
│   │   ├── gap_scores.csv
│   │   └── statistical_analysis_results.csv
│   └── phase4/
│       ├── survey_responses_anonymised.csv
│       ├── quantitative_summary.csv
│       ├── qualitative_themes.md
│       └── revision_log.md
│
├── outputs/
│   ├── phase1/
│   │   ├── capability_taxonomy_v1.md
│   │   └── capability_taxonomy_FINAL.md
│   │   └── capability_taxonomy_FINAL.csv
│   ├── phase2/
│   │   ├── benchmark_database_FINAL.csv
│   │   ├── inventory_summary.md
│   │   └── charts/
│   ├── phase3/
│   │   ├── statistical_analysis_report.md
│   │   └── charts/
│   │       ├── coverage_heatmap.png
│   │       ├── gap_scores.png
│   │       ├── usage_vs_coverage_scatter.png
│   │       ├── temporal_trends.png
│   │       └── quality_radar.png
│   ├── phase4/
│   │   └── validation_report.md
│   └── phase5/
│       ├── benchmark_spec_[capability].md (×3–5)
│       ├── assessment_toolkit.xlsx
│       ├── assessment_toolkit_documentation.pdf
│       └── recommendations_synthesis.md
│
├── scripts/
│   ├── phase1_thematic_analysis.py
│   ├── phase1_intercoder_reliability.py
│   ├── phase2_benchmark_analysis.py
│   ├── phase3_coverage_matrix.py
│   ├── phase3_gap_scores.py
│   ├── phase3_statistical_analysis.py
│   ├── phase3_visualisations.py
│   └── phase4_survey_analysis.py
│
└── thesis/
    ├── chapters/
    │   ├── 01_introduction.md
    │   ├── 02_literature_review.md
    │   ├── 03_methodology.md
    │   ├── 04_phase1_results.md
    │   ├── 05_phase2_results.md
    │   ├── 06_phase3_results.md
    │   ├── 07_phase4_results.md
    │   ├── 08_phase5_recommendations.md
    │   ├── 09_discussion.md
    │   └── 10_conclusion.md
    └── thesis_FINAL.docx
```

---

## 14. QUALITY STANDARDS & SUCCESS CRITERIA

### Phase-Level Success Criteria

| Phase   | Success Criterion                                                                | Measurement                             |
| ------- | -------------------------------------------------------------------------------- | --------------------------------------- |
| Phase 1 | Taxonomy covers ≥95% of Anthropic top 100 tasks AND Cohen's κ > 0.8            | Coverage % + κ calculation             |
| Phase 2 | All 15–20 benchmarks fully documented; recall ≥90% vs. major model reports     | Field completion check; cross-reference |
| Phase 3 | All statistical analyses run; all 5 visualisations produced; ≥3 case studies    | Checklist review                        |
| Phase 4 | ≥5 complete expert responses OR documented literature-based validation          | Response count                          |
| Phase 5 | 3–5 benchmark specs complete; toolkit pilot-tested by 2 colleagues successfully | Pilot feedback                          |
| Thesis  | Supervisor positive feedback; first-class honours target                         | Supervisor comments                     |

### Universal Quality Rules

- No claim in any output without a citation or documented evidence
- No rating without a written justification
- All statistical results reported with test statistic, p-value, effect size, and confidence interval
- All formulas verified independently before final reporting
- No data file delivered without a completeness check

---

## 15. RISK FLAGS & ESCALATION RULES

When any of the following conditions occur,  **stop immediately and flag to Leon before proceeding** :

| Condition                                                    | Action                                                                       |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| Cohen's κ < 0.8 after coding                                | Refine decision rules; re-code; do not proceed to Week 3 validation          |
| Taxonomy coverage < 95%                                      | Revise taxonomy; do not finalise until target met or alternative justified   |
| Benchmark recall < 90%                                       | Add missing benchmarks before proceeding to Phase 3                          |
| Expert response rate < 5                                     | Activate literature-based validation contingency; document substitution      |
| Any formula or calculation error found                       | Stop all dependent analysis; correct and rerun from point of error           |
| Ethics approval not received by start of Week 14             | Do not recruit or contact participants; activate contingency validation plan |
| Any personally identifiable information found in a data file | Remove immediately; do not commit to Git; notify Leon                        |

---

## 16. KEY LITERATURE & CITATION STANDARDS

### Core References (cite these accurately — do not paraphrase their findings without verification)

| Short Name              | Full Citation                                                                                                                          |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Handa et al. (2025)     | Handa, K. et al. (2025). Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations. arXiv:2503.04761. |
| Xu et al. (2025)        | Xu, F.F. et al. (2025). TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks. arXiv:2412.14161.                  |
| Braun & Clarke (2006)   | Braun, V. and Clarke, V. (2006). Using thematic analysis in psychology. Qualitative Research in Psychology, 3(2), pp. 77–101.         |
| Hendrycks et al. (2021) | Hendrycks, D. et al. (2021). Measuring Massive Multitask Language Understanding. arXiv:2009.03300.                                     |
| Jain et al. (2024)      | Jain, N. et al. (2024). LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code. arXiv:2403.07974. |
| Singh et al. (2025)     | Singh, S. et al. (2025). The Leaderboard Illusion. arXiv:2504.20879.                                                                   |
| Balloccu et al. (2024)  | Balloccu, S. et al. (2024). Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs. ACL.            |
| Pezeshkpour & Hruschka  | Pezeshkpour, P. and Hruschka, E. Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions.               |

### Citation Standards

- APA 7th edition throughout
- DOI or URL for all online sources
- arXiv papers cited with arXiv ID
- All citations verified against original source before inclusion in thesis
- Mendeley used for reference management

---

## 17. GLOSSARY

| Term                            | Definition                                                                                                                                         |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Capability**            | A distinct mode of LLM interaction identified through thematic analysis of real-world usage data (e.g., "reviewing work", "information retrieval") |
| **Benchmark**             | A standardised evaluation framework for assessing LLM performance on specific tasks                                                                |
| **Coverage Score**        | A measure of how well existing benchmarks collectively test a given capability (scale 0–1)                                                        |
| **Gap Score**             | Usage-weighted measure of evaluation coverage shortfall: Gap = Usage_Frequency × (1 − Normalized_Coverage_Score)                                 |
| **Usage Frequency**       | The proportion of LLM interactions involving a given capability, derived from empirical usage data                                                 |
| **Cohen's κ**            | A statistical measure of inter-coder agreement (target: >0.8 for strong agreement)                                                                 |
| **Fleiss' κ**            | Extension of Cohen's κ for >2 raters (target: >0.65 for expert validation)                                                                        |
| **Braun & Clarke (2006)** | The six-phase thematic analysis methodology used for capability taxonomy development                                                               |
| **O*NET**                 | US Department of Labor occupational task database used for cross-referencing AI task categories                                                    |
| **WILDCHAT**              | Publicly available anonymised corpus of ChatGPT conversations                                                                                      |
| **Benchmaxxing**          | The practice of optimising model training to improve benchmark scores without genuine capability improvement                                       |
| **Data Contamination**    | When benchmark test data appears in a model's training data, inflating benchmark scores artificially                                               |
| **Goodhart's Law**        | When a measure becomes a target, it ceases to be a good measure (applied here: benchmark scores become targets, losing validity)                   |
| **Usage-Weighted**        | Analysis that accounts for the relative frequency of real-world usage, giving higher importance to commonly used capabilities                      |
