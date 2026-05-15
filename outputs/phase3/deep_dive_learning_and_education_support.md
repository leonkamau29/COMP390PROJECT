# Deep Dive: Learning and Education Support

I classify Learning and Education Support as a moderate coverage capability. Its capability ID is C04, its usage frequency is 0.1113, its normalised coverage score is 0.1714, and its gap score is 0.0922. The benchmark inventory includes 8 benchmarks that touch this area, with an average quality score of 3.0000 among the covering benchmarks.

## 1. Current Evaluation Landscape

In the Phase 1 taxonomy, I define Learning and Education Support as the ability to help users acquire knowledge, skills, or academic qualifications through tutoring, explanation, worked examples, and structured guidance. This includes support for understanding concepts, completing assignments as learning exercises, solving problems, and developing academic competence. In this role, the model acts as a tutor, teacher, or study partner rather than only as an answer generator.

The strongest coverage comes from TutorBench and MathTutorBench, both rated 5/5. TutorBench is important because it evaluates multisubject multimodal tutoring, although it is very new and depends on LLM judging. MathTutorBench also gives strong coverage because it is designed around pedagogical tasks, but it is primarily mathematical and its aggregate scores may be difficult to interpret because of reward-model bias. MathDial receives 4/5 because it tests multi-turn tutoring dialogue, although it is limited to mathematics and may penalise valid alternative teaching approaches when they do not match the reference.

The remaining benchmarks provide weaker coverage. MMLU-Pro, Humanity's Last Exam, and GPQA Diamond mainly test academic knowledge or expert reasoning, but they do so through formats that are closer to examination than tutoring. WildBench includes real-user tasks, but its broadness makes construct attribution less precise. CriticBench is relevant because critique and correction can support learning, but its focus is more STEM and reasoning oriented than broad educational support.

This landscape suggests that education is no longer completely ignored, but it is still only partially covered. Many benchmarks test whether a model can answer difficult questions. Fewer test whether it can teach well, adapt to a learner, diagnose misunderstanding, or guide a student without simply giving away an answer.

## 2. Technical and Practical Challenges to Evaluation

I find this capability difficult to evaluate because good tutoring is interactive and context-sensitive. The taxonomy includes academic assignment support, concept explanation, skill development, and educational material creation. A benchmark has to decide whether it is measuring correctness, pedagogy, learner adaptation, encouragement, scaffolding, or some combination of these.

Static answer-key scoring is often too narrow for this capability. A tutoring response can be factually correct but pedagogically weak, or it can use a different teaching path that is still valid. The Phase 2 notes also point to contamination risk, LLM judge dependence, and reduced ecological validity when education is reduced to multiple-choice questions. These issues matter because the project is interested in real educational use, not only exam-style performance.

## 3. Real-World Importance

I ground the importance of this capability in the mapped Anthropic AEI top-task data. The strongest examples are assisting with academic assignments and coursework across disciplines at 5.1945%, creating educational materials and explaining concepts at 1.9390%, and helping solve and explain mathematics problems across levels at 1.4013%.

These examples show that education-related use is not a niche behaviour. Users often come to LLMs for explanation, structured help, and academic support. A usage-weighted analysis is therefore necessary because a model's ability to pass an exam benchmark does not necessarily show that it can support learning responsibly or effectively.

## 4. Consequences of Inadequate Evaluation

If this capability is evaluated poorly, models may be selected because they know the answer rather than because they can teach. This can lead to systems that provide overconfident explanations, give away solutions without building understanding, fail to adapt to a learner's level, or reinforce misconceptions. In educational settings, these weaknesses can directly affect student learning.

For Learning and Education Support, the mismatch between benchmark confidence and real use is especially important because users may be students, teachers, or self-directed learners. A high score on an academic QA benchmark may not indicate that a model can scaffold reasoning, ask useful follow-up questions, or explain mistakes in a way that helps the learner improve.

## 5. Requirements for Adequate Coverage

In my view, adequate coverage would need realistic tutoring dialogues, assignment-support scenarios, and educational material creation tasks. It should separate the sub-capabilities so that a model's strength in mathematics tutoring does not hide weakness in writing support, conceptual explanation, or skill development. The scoring should combine correctness with pedagogical quality, and it should include calibrated human or expert judgement where open-ended teaching quality matters.

I would also expect contamination controls and clearer reporting of what each benchmark can and cannot support. Scores should be connected to learner context, subject area, and intended use. For Phase 5, this capability remains a useful candidate for benchmark design if existing education benchmarks do not cover the most common real-world learning scenarios identified in the usage data.
