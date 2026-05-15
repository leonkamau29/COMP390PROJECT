

# Benchmark Specification: TutorScaffoldBench

## 1. Capability Measured and Rationale

TutorScaffoldBench is my proposed benchmark for C04, Learning and Education Support. I designed it to test whether large language models can support learning through misconception diagnosis, adaptive scaffolding, formative feedback, and pedagogically appropriate explanation. The key point is that the benchmark should evaluate models as tutors, not answer engines.

The rationale comes from the Phase 3 gap analysis. C04 has a usage frequency of 0.111313, a normalised coverage score of 0.171429, and a gap score of 0.092231. The Phase 1 taxonomy shows real-world tasks such as academic assignment support, concept explanation, mathematics help, programming fundamentals, STEM coursework, and academic writing support. These tasks are common because learners use models as study partners, not only as tools for retrieving answers.

The Phase 2 inventory shows growing but incomplete C04 coverage. MathDial evaluates multi-turn mathematics tutoring, MathTutorBench evaluates pedagogical sub-skills, and TutorBench broadens tutoring across subjects and modalities. However, many academic benchmarks such as MMLU-Pro, GPQA Diamond, and Humanity's Last Exam still test knowledge rather than teaching. TutorScaffoldBench targets the missing construct: whether a model can help a learner understand.

## 2. Task Structure

Each task would present the model with a learner profile, a learning objective, a student attempt or question, and a tutoring constraint. The model would respond as a tutor by diagnosing the learner's current understanding and providing an appropriate next step. Some tasks would be single-turn, while others would be short multi-turn scenarios where the model must adapt after a learner response.

The benchmark would cover misconception diagnosis, scaffolded hinting, formative feedback, concept explanation, and adaptive follow-up. Each item would include the subject and level, learning objective, learner profile, student attempt or misconception, tutoring policy, expert rubric, and optional reference tutoring moves.

The following bullet points are examples of tasks that could exist in the proposed TutorScaffoldBench benchmark. They are examples of the kinds of tutoring situations the benchmark could contain, not a final task list.

- A Year 9 algebra task where a student solves `3(x + 2) = 15` as `3x + 2 = 15`. The model would identify the distribution error, explain that 3 must multiply both terms, and guide the student to retry without simply replacing their work with the final answer.
- A beginner Python task where a student uses `range(1,5)` and wonders why 5 is missing. The model would explain that the stop value is exclusive, give a small example, and prompt the learner to try `range(1,6)`.
- A first-year essay feedback task where a paragraph about social media and loneliness has a claim but no evidence. The model would give formative feedback on evidence, generalisation, and revision strategy without rewriting the whole paragraph.
- A GCSE physics explanation task asking why heavier objects do not fall faster than lighter objects. The model would use an analogy, avoid calculus, and distinguish idealised motion from air resistance.
- A chemistry safety task where a student asks how to mix household chemicals for a school video. The model would avoid unsafe procedural detail and offer a safe educational alternative.
- A multi-turn fraction-hinting task where the student asks how to add `1/3` and `1/4`, then responds with `2/7`. The model would introduce common denominators and then diagnose why numerators and denominators are not added separately.
- A study-planning task where a student has two weeks before a biology exam, struggles with cell respiration, and can study 45 minutes per day. The output would use spaced practice, retrieval questions, diagram review, and achievable daily goals.
- A proof-feedback task where a student claims all rectangles are squares because both have four right angles. The model would explain the missing side-length condition using definitions.
- A language-learning feedback task where a Spanish sentence contains gender agreement and verb conjugation errors. The model would correct the sentence, explain the rules, and give one practice sentence.
- An academic-integrity task where a university student asks for a full answer to an assessed assignment. The model would decline to produce the submission and offer learning-support alternatives such as interpreting the question, building an outline, explaining concepts, or reviewing a draft.

## 3. Dataset Composition

The first release should contain around 1,200 tasks, including both single-turn and short multi-turn tutoring scenarios. The tasks should cover misconception diagnosis, scaffolded hinting, formative feedback, concept explanation, and adaptive follow-up.

Subjects should include mathematics, programming, natural sciences, academic writing, language learning, study skills, and humanities concepts. Mathematics should remain present for comparison with MathDial and MathTutorBench, but it should not dominate the benchmark. I would aim for mathematics to make up no more than about 30 percent of the dataset.

Data sources should include researcher-authored student attempts with known misconceptions, public educational materials, curriculum-aligned learning objectives, synthetic learner profiles, expert-authored rubrics, and public examples of student errors where privacy and licensing allow. Each task should record subject, education level, learning objective, task family, misconception type, safety or academic-integrity requirements, expected tutoring move, and rubric dimensions.

Quality control should involve educators or domain-literate reviewers. Every task should be checked for accuracy, level appropriateness, and whether the expected behaviour is genuinely educational rather than simply answer delivery.

## 4. Evaluation Methodology

TutorScaffoldBench should use a pedagogical rubric rather than exact-match scoring. The primary metric should be a pedagogical support score that captures conceptual accuracy, misconception diagnosis, scaffolding quality, learner-level fit, actionability, supportive tone, and academic integrity or safety.

Some checks can be automated in limited cases, such as detecting whether a final answer appears when it is prohibited. Most scoring, however, needs human or validated judge assessment. For multi-turn tasks, the whole sequence should be scored rather than each turn in isolation. A model that gives the final answer immediately may be less useful than one that guides the learner step by step.

The benchmark should report separate scores for tutoring sub-skills. This matters because a model may be good at explanations but weak at misconception diagnosis, or strong in mathematics but weak at writing feedback.

## 5. Validation Strategy

Validation should use educator-informed review. Each task should be mapped to C04 sub-categories such as academic assignment support, concept explanation and tutoring, skill development, or educational material creation. Subject-literate reviewers should confirm correctness and level fit.

A 100-item pilot should be run with several models and at least one human tutor baseline for selected items. Annotators should be trained using examples of high-quality tutoring, over-answering, inaccurate explanation, and unhelpful feedback. Weighted kappa should be calculated for rubric dimensions, with a target above 0.75 overall and higher reliability for conceptual accuracy.

I would compare results with MathDial, MathTutorBench, TutorBench, MMLU-Pro, and WildBench. I would expect limited correlation with knowledge benchmarks because knowledge is necessary for tutoring but not sufficient. A validation report should distinguish correctness validity from pedagogical validity.

## 6. Implementation Requirements

A first release would likely take 4 to 6 months. It would require a lead researcher, subject-literate task writers, educator reviewers, an evaluation engineer, and ideally an educational psychology advisor for rubric design.

The infrastructure would need a structured task schema that supports multi-turn items, an annotation interface for turn-level and sequence-level scoring, rubric documentation, scripts for dimension-level reporting, and a private split for final evaluation. The cost level is medium to high because educator review is important.

The deliverables would include a public development split, a private evaluation split, a pedagogical rubric, an annotator training guide, and baseline model comparisons.

## 7. Expected Challenges and Mitigations

One challenge is that valid tutoring strategies differ. I would score against pedagogical principles rather than one reference answer. Another challenge is that models may optimise for correctness instead of learning, so the benchmark should include tasks where giving the final answer immediately is penalised.

Subject coverage can become shallow if the benchmark tries to cover too much too quickly. I would start with fewer subjects but ensure each has expert-reviewed task clusters. Academic integrity boundaries also vary by institution, so the benchmark should state its policy clearly and evaluate whether models offer useful learning-support alternatives. LLM judges may reward polished explanations even when pedagogy is weak, so judge scores should be validated against educator ratings.

## 8. Comparison to Existing Benchmarks

TutorScaffoldBench builds on MathDial by keeping the importance of dialogue but expanding beyond mathematics. It builds on MathTutorBench by using pedagogical sub-skills, while broadening subject coverage and separating scores for feedback, explanation, study planning, and integrity-sensitive support. It complements TutorBench by focusing on transparent task families, learner profiles, and interpretable pedagogical dimensions.

Knowledge benchmarks such as MMLU-Pro, GPQA Diamond, and Humanity's Last Exam test whether a model knows material, but they do not test whether it can teach. CriticBench evaluates critique and correction, but learner-centred feedback is a different construct. The intended contribution of TutorScaffoldBench is to measure whether a model can identify what a learner misunderstands, respond at the right level, preserve motivation, and guide the learner toward understanding.