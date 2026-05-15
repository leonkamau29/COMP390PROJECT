<!-- markdownlint-disable MD013 -->

# Benchmark Specification: MessyDataBench

## 1. Capability Measured and Rationale

MessyDataBench is my proposed benchmark for C07, Data Analysis and Summarisation. I designed it to test whether large language models can analyse imperfect real-world data, interpret results responsibly, and communicate findings to a non-technical audience. The benchmark focuses on user workflows involving spreadsheets, documents, charts, mixed files, cleaning, summarisation, analysis, and explanation.

The rationale comes from the Phase 3 gap analysis. C07 has a usage frequency of 0.075144, a normalised coverage score of 0.200000, and a gap score of 0.060115. Its gap score is lower than the largest capabilities, but it remains strategically important because users frequently ask models to process files, extract information, summarise documents, create dashboards, and perform data analysis.

The existing benchmark inventory gives C07 relatively strong coverage through InfiAgent-DABench, DA-Code, Spider 2.0, MMLongBench-Doc, FACTS Grounding, LiveBench, and WildBench. However, these benchmarks still tend to be CSV-centric, SQL-centric, execution-centric, or document-QA-centric. Real analysis work often involves messy spreadsheets, ambiguous columns, inconsistent units, missing values, duplicates, business context, and the need to communicate a cautious conclusion. MessyDataBench targets that full analyst workflow.

## 2. Task Structure

Each MessyDataBench item would give the model a user request, one or more data files or document excerpts, and a communication target. The model would produce an analysis output that may include cleaned data, calculations, charts, written interpretation, caveats, and recommendations.

The benchmark would cover messy spreadsheet analysis, business KPI interpretation, document and table synthesis, statistical reasoning, forecasting and scenario analysis, and analyst communication. Each task would include a user question, a data packet, context, required output format, ground-truth calculations where possible, expected caveats, and a rubric for correctness, method fit, uncertainty, and communication.

The following bullet points are examples of tasks that could exist in the proposed MessyDataBench benchmark. They illustrate possible task designs rather than fixing the final task set.

- A customer purchase CSV with duplicate transaction IDs, missing region labels, and mixed currency symbols. The user would ask which region generated the most revenue last quarter, and the model would need to avoid double-counting, parse currencies correctly, disclose missing-region records, and give the cleaned answer.
- A support-ticket spreadsheet with inconsistent category labels such as "billing", "Billing", and "billng". The model would normalise categories, compare ticket volume over time, and explain likely drivers without overclaiming causality.
- A student survey with Likert responses, comments, and missing demographic fields. The model would compare satisfaction by year group while stating the missing-data limitation.
- A 250-word executive summary from a sustainability report containing emissions tables, targets, and risk notes. The output would preserve key quantitative facts and avoid unsupported environmental claims.
- An A/B test interpretation task using conversion rates, sample sizes, and confidence intervals. The model would interpret effect size, uncertainty, and rollout risk without treating non-significance as proof of no effect.
- A short forecasting task using 14 months of sales data with a holiday spike and a stockout month. The model would produce a cautious next-quarter forecast and explain the assumptions.
- A multi-file join task involving orders, customer segments, and refund files. The model would calculate refund rate by segment, choose correct keys, justify the denominator, and report missing keys.
- A chart critique task involving a misleading bar chart with a truncated y-axis. The model would explain the visualisation issue, suggest a corrected chart, and avoid accusing intent without evidence.
- A thematic summary task using 120 customer comments. The model would identify themes, give approximate counts, select representative anonymised quotes, disclose duplicates, and make recommendations grounded in the comments.
- A business-health interpretation task where revenue is up but active users and churn have worsened. The model would handle conflicting metrics and suggest follow-up analysis rather than giving a one-dimensional answer.

## 3. Dataset Composition

The first release should contain around 700 tasks with associated data packets. This is smaller than text-only benchmarks because data packaging, executable validation, and ground-truth creation are more expensive.

The data packets should include single CSVs, multi-file joins, mixed tabular and text documents, report excerpts, chart descriptions, and precomputed statistical outputs. The datasets should be synthetic or public, with no personal data. Synthetic data should include realistic data-quality issues such as missing values, inconsistent labels, duplicates, outliers, merged cells, ambiguous column names, and inconsistent units.

Each task should record metadata for task family, file type, domain, required operations, data-quality issues, ground truth or acceptable answer range, required caveats, whether code execution is required, and communication audience. Quality control should include independent calculation verification and evidence maps for open-ended summaries.

## 4. Evaluation Methodology

MessyDataBench should combine executable correctness, calculation checks, and communication scoring. The primary metric should be an analyst workflow score that captures data understanding, cleaning appropriateness, calculation correctness, method fit, interpretation quality, uncertainty, communication usefulness, and reproducibility.

Automatic scoring can verify numerical answers, joins, filtered counts, statistical outputs, and chart data. Human or validated judge scoring is needed for interpretation, caveats, and stakeholder communication. Where multiple cleaning choices are defensible, scoring should accept a range of answers if the method is justified and limitations are disclosed.

Reports should separate numerical accuracy, caveat recall, unsupported-claim rate, data-cleaning error rate, communication quality, and end-to-end success. This prevents a model from being rewarded for a polished summary based on wrong calculations, or for correct calculations that are communicated misleadingly.

## 5. Validation Strategy

Validation should use both computational checks and expert review. Independent solution scripts should verify objective calculations. Reviewers should check that each task contains the intended data-quality issues and is solvable from the provided materials. A 70-task pilot should be run with baseline models, and common failure modes should be inspected.

Annotators should be calibrated on interpretation and communication scoring using outputs with known calculation correctness. Weighted kappa should be reported for subjective dimensions, with a target above 0.75. I would also compare results with InfiAgent-DABench, DA-Code, Spider 2.0, MMLongBench-Doc, LiveBench, and WildBench. The benchmark should confirm that MessyDataBench measures a broader analyst workflow than SQL execution, document QA, or clean CSV question answering alone.

## 6. Implementation Requirements

The first release would likely take 4 to 5 months. It would require a lead researcher, data analysts or data-science annotators, reviewers for calculation verification, an engineer for data packaging and scripts, and optional domain reviewers for business, education, or public-sector scenarios.

The infrastructure would include file-based task packaging, a sandboxed Python or R execution environment where appropriate, ground-truth solution scripts, an annotation interface, and numerical comparison with tolerance handling. The cost level is medium to high because dataset creation and verification are labour intensive.

The deliverables would include a public development split, a private evaluation split, an evaluation harness, baseline model results, solution explanations, and documentation on the data-quality issue taxonomy.

## 7. Expected Challenges and Mitigations

Many analysis tasks have more than one defensible method. I would handle this by defining acceptable method families, requiring method explanation, and scoring caveats rather than enforcing one exact path. Numerical correctness and narrative quality can diverge, so calculation and communication dimensions should be reported separately.

Execution environments are costly, so the benchmark should offer executable and non-executable tracks. Synthetic data can feel artificial, so practising analysts should review datasets for realism. Models may hallucinate causal explanations, so the rubric should penalise unsupported claims and require explicit causal caveats.

## 8. Comparison to Existing Benchmarks

MessyDataBench builds on InfiAgent-DABench by keeping open-ended data analysis but adding mixed file types, messy data issues, stakeholder communication, and caveat scoring. It overlaps with DA-Code through executable workflows, but places more emphasis on interpretation and communication. It differs from Spider 2.0 by covering non-SQL spreadsheets, documents, and ambiguous analysis requests. It overlaps with MMLongBench-Doc on document and table synthesis, but adds cleaning decisions and quantitative interpretation. It also uses grounding ideas from SimpleQA/FACTS while moving beyond grounded answers into calculation and analysis.

The intended contribution is a benchmark for the practical analyst role: working through messy evidence and producing a responsible conclusion that a human decision-maker can actually use.
