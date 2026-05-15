<!-- markdownlint-disable MD013 -->

# Benchmark Specification: MessyDataBench - Real-World Data Analysis, Interpretation, and Communication

## 1. Capability Measured and Rationale

**Target capability:** C07 - Data Analysis and Summarisation.

MessyDataBench is a proposed benchmark for evaluating whether large language models can analyse imperfect real-world data, interpret results responsibly, and communicate findings to a non-technical audience. The benchmark focuses on tasks where users provide spreadsheets, documents, charts, or mixed files and expect the model to clean, analyse, summarise, and explain the result. It targets the Phase 1 sub-categories of data analysis and statistical computing, document processing, text summarisation, business intelligence, and forecasting.

The rationale is grounded in the Phase 3 gap analysis. C07 has a usage frequency of 0.075144, a normalised coverage score of 0.200000, and a gap score of 0.060115. Although its gap score is lower than C02, C01, C03, and C04, it remains strategically important because many real-world users ask models to process files, extract information, summarise documents, create dashboards, and perform data analysis. The Phase 1 examples include extracting and analysing content from images and documents, comprehensive business research analysis, statistical computing, visualisation, forecasting, and argument or document summarisation.

The Phase 2 inventory shows relatively strong C07 coverage compared with several other capabilities. InfiAgent-DABench (B015) evaluates agentic data analysis over CSV files. DA-Code (B016) tests executable data-science workflows across wrangling, machine learning, and exploratory analysis. Spider 2.0 (B017) evaluates enterprise SQL and BI workflows. MMLongBench-Doc (B018) evaluates long-context multimodal document understanding and evidence-supported QA over complex PDFs. FACTS Grounding within SimpleQA/FACTS (B009), LiveBench (B010), and WildBench (B014) provide partial coverage.

However, the current benchmarks still leave a practical gap. Real user workflows often involve messy spreadsheets, ambiguous column meanings, inconsistent units, missing values, duplicate records, business context, and the need to communicate conclusions to a manager. Existing benchmarks are often CSV-centric, SQL-centric, execution-centric, or document-QA-centric. MessyDataBench targets the full analyst workflow: understand the question, inspect messy data, clean it conservatively, perform appropriate analysis, avoid unsupported claims, and produce a clear decision-oriented summary.

## 2. Task Structure

Each MessyDataBench item gives the model a user request, one or more data files or document excerpts, and a communication target. The model must produce an analysis output, which may include cleaned data, calculations, charts, written interpretation, caveats, and recommendations. For executable settings, the model can generate code or use tools. For text-only settings, the model must describe the analysis method and result from supplied summaries.

The benchmark is organised into six task families:

- **Messy spreadsheet analysis:** clean and analyse tabular data with missing values, duplicates, inconsistent labels, or unit issues.
- **Business KPI interpretation:** compute metrics and explain trends for a stakeholder.
- **Document and table synthesis:** extract and summarise information from PDFs, tables, reports, or mixed text.
- **Statistical reasoning:** select appropriate descriptive or inferential analysis and interpret results.
- **Forecasting and scenario analysis:** make bounded projections and communicate uncertainty.
- **Analyst communication:** produce executive summaries, caveats, and recommendations from analysis outputs.

Each task includes:

- User question.
- Data packet, such as CSV, spreadsheet, table, document excerpts, or chart descriptions.
- Business or research context.
- Required output format.
- Ground truth calculations where possible.
- Expected caveats and data-quality issues.
- Rubric for correctness, method appropriateness, uncertainty, and communication.

### Example Item 1: Duplicate Customer Revenue

**Input:** A CSV of customer purchases contains duplicate transaction IDs, missing region labels, and mixed currency symbols. User asks: "Which region generated the most revenue last quarter?" Context: internal sales review.

**Expected output:** Cleaned revenue calculation by region, explanation of duplicate handling, note on missing region records, and a concise answer.

**Evaluation criteria:** Duplicate transactions are not double-counted; currency parsing is correct; missing regions are disclosed; conclusion matches cleaned data.

### Example Item 2: Support Ticket Trend

**Input:** A spreadsheet contains support tickets with dates, categories, severity, and resolution time. Some categories are spelled inconsistently, such as "billing", "Billing", and "billng". User asks for the top three drivers of increased ticket volume.

**Expected output:** Normalised category analysis, trend comparison over time, and a manager-facing summary of likely drivers.

**Evaluation criteria:** Category normalisation is sensible; trend calculation uses comparable periods; conclusion distinguishes observed increase from causal claim.

### Example Item 3: Survey Results With Missing Data

**Input:** A student survey has Likert responses, free-text comments, and missing demographic fields. User asks whether satisfaction differs by year group.

**Expected output:** Descriptive comparison by year group, missing-data caveat, and cautious interpretation.

**Evaluation criteria:** Does not ignore missingness; uses appropriate descriptive statistics; avoids overclaiming statistical significance unless tested.

### Example Item 4: Executive Summary From Long Report

**Input:** Excerpts from a 40-page sustainability report include emissions tables, reduction targets, and risk notes. User asks for a 250-word executive summary for senior management.

**Expected output:** Concise summary of current emissions, targets, progress, risks, and next steps.

**Evaluation criteria:** Important quantitative facts preserved; no unsupported environmental claims; risk caveats included; format and length followed.

### Example Item 5: A/B Test Interpretation

**Input:** Experiment data shows conversion rates for version A and B, sample sizes, and confidence intervals. User asks whether to roll out version B.

**Expected output:** Interpretation of effect size, uncertainty, and practical recommendation considering sample size and risk.

**Evaluation criteria:** Correctly interprets confidence interval; avoids treating non-significant result as proof of no effect; recommendation is bounded.

### Example Item 6: Forecasting With Limited History

**Input:** Monthly sales data for 14 months includes a holiday spike and one stockout month. User asks for next quarter forecast.

**Expected output:** Simple forecast with explicit caveats, treatment of outlier months, and recommendation to collect more data.

**Evaluation criteria:** Handles outliers transparently; does not present a precise forecast as certain; communicates assumptions.

### Example Item 7: Multi-File Join

**Input:** One CSV contains orders; another contains customer segments; a third contains refund records. User asks which customer segment has the highest refund rate.

**Expected output:** Correct joins, refund-rate calculation by segment, and explanation of denominator choice.

**Evaluation criteria:** Joins use correct keys; refund rate is calculated as refunds divided by orders or customers with justification; missing keys are reported.

### Example Item 8: Chart Critique And Correction

**Input:** User provides a bar chart description where the y-axis starts at 90, making small differences look dramatic. They ask whether the chart is misleading.

**Expected output:** Explanation of why the truncated axis may exaggerate differences, suggested corrected chart, and neutral wording.

**Evaluation criteria:** Identifies visualisation issue; explains impact; suggests appropriate correction; does not accuse intent without evidence.

### Example Item 9: Thematic Summary Of Comments

**Input:** 120 short customer comments about a delivery service. User asks for main themes and representative quotes. Comments contain mixed sentiment and some duplicates.

**Expected output:** Theme summary with approximate counts, representative anonymised quotes, duplicate caveat, and actionable recommendations.

**Evaluation criteria:** Themes are grounded in comments; duplicate issue is handled; quotes are representative; recommendations follow from themes.

### Example Item 10: Conflicting Metrics In Business Review

**Input:** A business dashboard shows revenue up 8 percent, active users down 5 percent, churn up 3 points, and average order value up 12 percent. User asks if the business is healthier this quarter.

**Expected output:** Balanced interpretation explaining that revenue improved but user retention weakened, with suggested follow-up analyses.

**Evaluation criteria:** Handles conflicting signals; avoids one-dimensional conclusion; suggests relevant further analysis; explains metrics clearly.

## 3. Dataset Composition

The proposed first release should contain **700 tasks** with associated data packets. This size is smaller than text-only benchmarks because data packaging, executable validation, and ground-truth creation are more expensive.

Suggested distribution:

- 160 messy spreadsheet analysis tasks.
- 120 business KPI interpretation tasks.
- 120 document and table synthesis tasks.
- 100 statistical reasoning tasks.
- 80 forecasting and scenario tasks.
- 120 analyst communication tasks.

Data packets should vary in complexity:

- Single CSV or spreadsheet.
- Multi-file joins.
- Mixed tabular and text documents.
- Report excerpts with embedded tables.
- Chart descriptions or image-derived chart data.
- Precomputed statistical outputs requiring interpretation.

Data should be synthetic or public, with no personal data. Synthetic datasets should be realistic enough to include common data-quality issues: missing values, inconsistent labels, duplicates, outliers, merged cells, ambiguous column names, and inconsistent units. Public datasets may be adapted if licensing permits and if task prompts are newly written to reduce contamination.

Metadata should include:

- Task family.
- File type.
- Domain.
- Required operations.
- Data-quality issues.
- Ground truth answer or acceptable answer range.
- Required caveats.
- Whether code execution is required.
- Communication audience.

Quality control should include independent verification of calculations, ideally by two reviewers or by separate scripts. For open-ended summaries, a reference evidence map should identify facts that must appear and claims that would be unsupported.

## 4. Evaluation Methodology

MessyDataBench should combine executable correctness, calculation checks, and communication scoring.

**Primary metric:** analyst workflow score.

**Rubric dimensions:**

- **Data understanding:** correctly identifies relevant fields, joins, units, and data-quality issues.
- **Cleaning appropriateness:** handles missing values, duplicates, outliers, and inconsistent labels in justified ways.
- **Calculation correctness:** computes metrics, summaries, or tests correctly.
- **Method fit:** selects analysis appropriate to the user's question and data limitations.
- **Interpretation quality:** explains what results mean without overclaiming.
- **Uncertainty and caveats:** states limitations, missing data issues, and assumptions.
- **Communication usefulness:** produces an output suitable for the intended audience.
- **Reproducibility:** where code is used, steps are clear and rerunnable.

Automatic scoring can verify numerical answers, joins, filtered counts, statistical outputs, and chart-data values. Human or validated judge scoring is needed for interpretation, caveats, and stakeholder communication. For tasks with multiple valid cleaning choices, scoring should accept a range of answers if the method is justified and caveats are disclosed.

Benchmark reports should include:

- Exact numerical accuracy.
- Caveat recall.
- Unsupported-claim rate.
- Data-cleaning error rate.
- Communication score.
- End-to-end task success.

This avoids rewarding a model that computes correctly but communicates misleadingly, or one that writes a polished summary based on incorrect calculations.

## 5. Validation Strategy

Validation should use both computational and expert review.

1. **Ground-truth verification:** Create independent solution scripts for all tasks with objective calculations.
2. **Data-quality review:** Check that each task contains intended issues and that they are solvable from the provided data.
3. **Pilot execution:** Run a 70-task pilot with baseline models and inspect common failure modes.
4. **Rubric calibration:** Train annotators on interpretation and communication scoring using model outputs with known calculation correctness.
5. **Reliability testing:** Calculate weighted kappa for subjective dimensions and target above 0.75.
6. **Comparison with existing benchmarks:** Compare with InfiAgent-DABench, DA-Code, Spider 2.0, MMLongBench-Doc, LiveBench, and WildBench.
7. **Stress testing:** Include tasks with tempting but wrong shortcuts, such as ignoring missing denominators or confusing correlation with causation.

Validation should confirm that MessyDataBench measures a broader analyst workflow than SQL execution, document QA, or CSV question answering alone.

## 6. Implementation Requirements

**Estimated time:** 4-5 months.

**Personnel:**

- 1 lead researcher.
- 2-3 data analysts or data-science annotators.
- 2 reviewers for calculation verification.
- 1 engineer for data packaging and evaluation scripts.
- Optional domain reviewers for business, education, or public-sector datasets.

**Infrastructure:**

- File-based task packaging.
- Sandboxed Python/R execution environment for model-generated code where applicable.
- Ground-truth solution scripts.
- Annotation interface for interpretation scoring.
- Automated numerical comparison with tolerance handling.

**Estimated cost level:** Medium to high because of dataset creation and verification.

**Deliverables:**

- Public development split with datasets and solution explanations.
- Private evaluation split.
- Evaluation harness for numerical and text outputs.
- Baseline model results.
- Documentation on data-quality issue taxonomy.

## 7. Expected Challenges and Mitigations

**Challenge: many analysis tasks have multiple defensible methods.**

**Mitigation:** Define acceptable method families, require method explanation, and score caveats rather than enforcing one exact path.

**Challenge: numerical correctness and narrative quality can diverge.**

**Mitigation:** Report separate calculation and communication dimensions.

**Challenge: execution environments are costly.**

**Mitigation:** Provide both executable and non-executable tracks. The executable track tests tool use; the non-executable track tests interpretation from supplied summaries.

**Challenge: synthetic data can feel unrealistic.**

**Mitigation:** Seed synthetic datasets with realistic data-quality issues and review them with practising analysts.

**Challenge: models may hallucinate causal explanations.**

**Mitigation:** Include unsupported-claim penalties and explicit causal-inference caveats in rubrics.

## 8. Comparison to Existing Benchmarks

**InfiAgent-DABench (B015)** directly evaluates agentic data analysis over CSV files and is a strong C07 baseline. MessyDataBench builds on its open-ended analysis orientation but adds mixed file types, messy data-quality issues, stakeholder communication, and caveat scoring.

**DA-Code (B016)** evaluates executable data-science workflows. MessyDataBench includes executable workflows but places greater emphasis on interpretation and communication, not only task resolution.

**Spider 2.0 (B017)** is strong for enterprise SQL and business intelligence workflows. MessyDataBench differs by covering non-SQL spreadsheets, documents, mixed evidence, and ambiguous analysis requests.

**MMLongBench-Doc (B018)** evaluates long multimodal document understanding over PDFs. MessyDataBench overlaps in document/table synthesis but adds quantitative analysis, cleaning decisions, and stakeholder-facing conclusions.

**SimpleQA/FACTS Grounding (B009)** provides grounding methods relevant to document-based analysis, but MessyDataBench extends beyond grounded answers to calculation, transformation, and interpretation.

**LiveBench (B010)** and **WildBench (B014)** include data-analysis-like tasks, but broad benchmark design makes C07 attribution less precise. MessyDataBench isolates the analyst workflow and reports dimension-level performance.

The intended contribution is a benchmark for the practical analyst role: not just writing SQL or answering questions over a clean CSV, but working through messy evidence and producing a responsible conclusion that a human decision-maker can use.
