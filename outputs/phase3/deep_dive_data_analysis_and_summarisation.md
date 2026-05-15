# Deep Dive: Data Analysis and Summarisation

**Coverage profile:** Well-Covered Capability
**Capability ID:** C07
**Usage frequency:** 0.0751
**Normalised coverage score:** 0.2000
**Gap score:** 0.0601
**Benchmark count:** 7
**Average quality among covering benchmarks:** 4.0000

## 1. Current Evaluation Landscape

Data Analysis and Summarisation is defined in the Phase 1 taxonomy as follows: Data Analysis and Summarisation is the capability to process, analyse, and synthesise existing datasets, documents, or information corpora to extract insights, patterns, statistical results, or compressed representations. The model acts as an analyst or information processor, converting raw or verbose input into structured, meaningful output. The defining feature is that the user supplies existing data or content as the primary input.

The updated Phase 2 benchmark inventory provides the following coverage:

- B017 Spider 2.0 (Spider 2.0): coverage rating 5/5; task type: Enterprise text-to-SQL and BI workflow; limitation noted in Phase 2: SQL and BI focused; may underrepresent non-SQL analysis; heavy environment requirements
- B016 DA-Code (DA-Code): coverage rating 5/5; task type: Executable data-science task benchmark; limitation noted in Phase 2: Environment setup cost; low current model success can make scores sparse
- B015 InfiAgent-DABench (InfiAgent-DABench): coverage rating 5/5; task type: Agentic data analysis over CSV files; limitation noted in Phase 2: CSV-centric; narrower than enterprise analytics; open-ended answers require careful scoring
- B018 MMLongBench-Doc (MMLongBench-Doc): coverage rating 5/5; task type: Long-context multimodal document QA; limitation noted in Phase 2: PDF-processing pipeline complexity; document QA is not full statistical analysis
- B009 SimpleQA / FACTS Grounding (SimpleQA/FACTS): coverage rating 3/5; task type: Factuality and grounded QA; limitation noted in Phase 2: SimpleQA is narrow factual recall; FACTS uses supplied documents and does not cover full advisory synthesis
- B010 LiveBench (LiveBench): coverage rating 3/5; task type: Holistic dynamic reasoning benchmark; limitation noted in Phase 2: Multicapability benchmark makes attribution to a single capability less clean
- B014 WildBench (WildBench): coverage rating 2/5; task type: Real-user task benchmark; limitation noted in Phase 2: Broadness makes construct attribution less precise; LLM judge dependence

This landscape shows that coverage is not only a question of benchmark count. A capability can have multiple benchmarks while still lacking direct coverage of the real-world situations described in the Phase 1 taxonomy. The coverage ratings therefore treat benchmark construct validity, task realism, scoring reliability, and update strategy as distinct from mere benchmark presence.

## 2. Technical and Practical Challenges to Evaluation

Evaluating Data Analysis and Summarisation is difficult because the capability definition spans several sub-categories: C07a — Text summarisation and compression; C07b — Data analysis and statistical computing; C07c — Document processing and format conversion; C07d — Business intelligence and forecasting. Benchmark design must decide which sub-categories are in scope, how user context is represented, and what counts as a valid response. Static answer-key scoring is easiest where outputs are short and objectively checkable, but many tasks in this capability require contextual judgement, long-form outputs, human preference, or multi-step tool use.

The Phase 2 quality notes indicate recurring constraints: contamination risk for static public datasets, operational cost for agentic environments, judge reliability for open-ended outputs, and reduced ecological validity when a benchmark uses a proxy format such as multiple choice. These constraints are especially important because the project aims to compare benchmark coverage against actual usage rather than against historically convenient evaluation formats.

## 3. Real-World Importance

The importance of this capability is grounded in mapped Anthropic AEI top-task usage. Examples include:

- Creating, converting, formatting, and manipulating documents across file types (Anthropic AEI, 2.1915%).
- Extracting, analysing, and processing content from images and documents (Anthropic AEI, 1.4706%).
- Assisting with data analysis, statistical computing, and database management tasks (Anthropic AEI, 0.9618%).

These examples show why usage-weighted analysis is necessary. A benchmark ecosystem can look active in aggregate while leaving everyday user workflows under-tested, particularly when common tasks require judgement, context preservation, or end-to-end completion rather than isolated answer production.

## 4. Consequences of Inadequate Evaluation

Inadequate evaluation can produce three deployment risks. First, model-selection decisions may reward benchmark-specific competence rather than capability fit. Second, teams may deploy models into user workflows where the highest-risk failure modes were not measured. Third, improvements may be optimised toward visible leaderboards while lower-visibility but high-usage behaviours receive less research attention.

For Data Analysis and Summarisation, the most direct consequence is mismatch between benchmark confidence and user-facing reliability. If the benchmark primarily tests simplified or proxy tasks, high scores may not imply performance on realistic inputs, ambiguous user goals, domain constraints, or longer interaction histories.

## 5. Requirements for Adequate Coverage

Adequate coverage for this capability would require:

- Task samples drawn from realistic user workflows and documented source distributions.
- Clear separation of sub-capabilities so that aggregate scores do not hide weak areas.
- Scoring methods matched to output type, combining automated checks where possible with calibrated human or expert judgement where necessary.
- Contamination controls, including post-cutoff data, private holdouts, or continuously refreshed task pools.
- Reporting that links benchmark scores to use-case assumptions, limitations, and confidence intervals rather than headline accuracy alone.

For Phase 5, this capability should be considered for new benchmark design if it remains high in the gap ranking or if existing benchmarks fail to cover the most deployment-relevant sub-categories.
