# Deep Dive: Learning and Education Support

**Coverage profile:** Moderate Coverage Capability
**Capability ID:** C04
**Usage frequency:** 0.1113
**Normalised coverage score:** 0.1714
**Gap score:** 0.0922
**Benchmark count:** 8
**Average quality among covering benchmarks:** 3.0000

## 1. Current Evaluation Landscape

Learning and Education Support is defined in the Phase 1 taxonomy as follows: Learning and Education Support is the capability to assist users in acquiring knowledge, skills, or academic qualifications through tutoring, explanation, worked examples, and structured guidance. This includes helping learners understand concepts, complete assignments, solve problems as learning exercises, and develop academic competencies. The model acts as tutor, teacher, or study partner, with the primary goal of building the user's understanding or academic capability.

The updated Phase 2 benchmark inventory provides the following coverage:

- B021 TutorBench (TutorBench): coverage rating 5/5; task type: Multisubject multimodal tutoring; limitation noted in Phase 2: Very new; LLM judge dependence; citation/adoption not yet established
- B020 MathTutorBench (MathTutorBench): coverage rating 5/5; task type: Multi-task pedagogical benchmark; limitation noted in Phase 2: Reward-model bias; primarily mathematics; aggregate interpretation complex
- B019 MathDial (MathDial): coverage rating 4/5; task type: Multi-turn tutoring dialogue; limitation noted in Phase 2: Math-only; reference matching penalises valid alternative pedagogy
- B006 MMLU-Pro (MMLU-Pro): coverage rating 2/5; task type: Multiple-choice knowledge and reasoning; limitation noted in Phase 2: Still multiple-choice; tests academic recall more than situated advice
- B014 WildBench (WildBench): coverage rating 2/5; task type: Real-user task benchmark; limitation noted in Phase 2: Broadness makes construct attribution less precise; LLM judge dependence
- B008 Humanity's Last Exam (HLE): coverage rating 2/5; task type: Expert knowledge and multimodal reasoning; limitation noted in Phase 2: Very new; private split complicates full independent replication; difficult items may overrepresent contest-style expertise
- B007 GPQA Diamond (GPQA Diamond): coverage rating 2/5; task type: Expert-level multiple-choice science QA; limitation noted in Phase 2: Small and STEM-only; gated access limits replication
- B022 CriticBench (Tsinghua) (CriticBench): coverage rating 2/5; task type: Critique and correction; limitation noted in Phase 2: STEM/reasoning focused; weak coverage of prose editing and stylistic feedback

This landscape shows that coverage is not only a question of benchmark count. A capability can have multiple benchmarks while still lacking direct coverage of the real-world situations described in the Phase 1 taxonomy. The coverage ratings therefore treat benchmark construct validity, task realism, scoring reliability, and update strategy as distinct from mere benchmark presence.

## 2. Technical and Practical Challenges to Evaluation

Evaluating Learning and Education Support is difficult because the capability definition spans several sub-categories: C04a — Academic assignment support; C04b — Concept explanation and tutoring; C04c — Skill development; C04d — Educational material creation. Benchmark design must decide which sub-categories are in scope, how user context is represented, and what counts as a valid response. Static answer-key scoring is easiest where outputs are short and objectively checkable, but many tasks in this capability require contextual judgement, long-form outputs, human preference, or multi-step tool use.

The Phase 2 quality notes indicate recurring constraints: contamination risk for static public datasets, operational cost for agentic environments, judge reliability for open-ended outputs, and reduced ecological validity when a benchmark uses a proxy format such as multiple choice. These constraints are especially important because the project aims to compare benchmark coverage against actual usage rather than against historically convenient evaluation formats.

## 3. Real-World Importance

The importance of this capability is grounded in mapped Anthropic AEI top-task usage. Examples include:

- Assisting with academic assignments and coursework across disciplines (Anthropic AEI, 5.1945%).
- Creating educational materials and explaining concepts (Anthropic AEI, 1.9390%).
- Helping solve and explain mathematics problems across levels (Anthropic AEI, 1.4013%).

These examples show why usage-weighted analysis is necessary. A benchmark ecosystem can look active in aggregate while leaving everyday user workflows under-tested, particularly when common tasks require judgement, context preservation, or end-to-end completion rather than isolated answer production.

## 4. Consequences of Inadequate Evaluation

Inadequate evaluation can produce three deployment risks. First, model-selection decisions may reward benchmark-specific competence rather than capability fit. Second, teams may deploy models into user workflows where the highest-risk failure modes were not measured. Third, improvements may be optimised toward visible leaderboards while lower-visibility but high-usage behaviours receive less research attention.

For Learning and Education Support, the most direct consequence is mismatch between benchmark confidence and user-facing reliability. If the benchmark primarily tests simplified or proxy tasks, high scores may not imply performance on realistic inputs, ambiguous user goals, domain constraints, or longer interaction histories.

## 5. Requirements for Adequate Coverage

Adequate coverage for this capability would require:

- Task samples drawn from realistic user workflows and documented source distributions.
- Clear separation of sub-capabilities so that aggregate scores do not hide weak areas.
- Scoring methods matched to output type, combining automated checks where possible with calibrated human or expert judgement where necessary.
- Contamination controls, including post-cutoff data, private holdouts, or continuously refreshed task pools.
- Reporting that links benchmark scores to use-case assumptions, limitations, and confidence intervals rather than headline accuracy alone.

For Phase 5, this capability should be considered for new benchmark design if it remains high in the gap ranking or if existing benchmarks fail to cover the most deployment-relevant sub-categories.
