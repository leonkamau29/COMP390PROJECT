<!-- markdownlint-disable MD013 -->

# Benchmark Specification: GroundedAdviceBench

## 1. Capability Measured and Rationale

GroundedAdviceBench is my proposed benchmark for C03, Information Retrieval and Advisory. I designed it to evaluate whether large language models can provide factual, evidence-grounded, context-sensitive advice while communicating uncertainty and limitations. The key idea is that advisory tasks are not only about knowing facts. They also require the model to decide what is supported, what is uncertain, what depends on the user's situation, and where a boundary should be drawn.

The rationale comes from the Phase 3 gap analysis. C03 has a usage frequency of 0.175381, a normalised coverage score of 0.171429, and a gap score of 0.145316, making it the third-highest gap-ranked capability. Phase 1 usage examples include medical and health information, product comparison, career assistance, cooking advice, factual questions, procedural guidance, investment information, and scientific information. These tasks require more than answer selection because the user often needs a practical recommendation that is appropriately qualified.

The Phase 2 inventory already includes several strong C03-adjacent benchmarks. MMLU-Pro measures broad academic knowledge, GPQA Diamond measures expert STEM reasoning, Humanity's Last Exam tests frontier expert knowledge, SimpleQA and FACTS Grounding measure factuality and faithfulness, LiveBench adds dynamic contamination-resistant coverage, WildBench includes real-user information-seeking prompts, and MMLongBench-Doc overlaps through document-grounded QA. However, none of these isolates advisory quality as its main construct. GroundedAdviceBench therefore targets the missing layer: whether a model can turn evidence into useful, bounded advice for a specific user without hallucination, overconfidence, or unsafe overgeneralisation.

## 2. Task Structure

Each GroundedAdviceBench item would give the model a user question, user context, evidence packet, and response requirements. The evidence packet could include short documents, product tables, policy excerpts, medical or legal guidance, web-style snippets, or research abstracts. The model would need to answer the user, refer to the evidence, identify uncertainty, and provide practical next steps where appropriate.

The benchmark would cover factual advisory, comparison and recommendation, procedural guidance, research synthesis, and high-stakes bounded advice. Each item would include the user prompt, context, 2 to 8 evidence sources or structured facts, optional conflicting or distracting evidence, user priorities, response constraints, a gold evidence map, and a rubric for factuality, grounding, uncertainty, relevance, and safety.

The following bullet points are examples of tasks that could exist in the proposed GroundedAdviceBench benchmark. They show the sort of advisory situations the benchmark could test, rather than a fixed final dataset.

- A laptop recommendation for university programming classes with a budget of GBP 800. The user would need at least 16 GB RAM, lightweight design, battery life above 8 hours, and no gaming laptop, while the evidence packet would contain a table of five models.
- A health-information task where a user asks whether persistent chest pain after exercise is probably anxiety. The model would need to avoid diagnosis, summarise warning signs from the evidence, communicate uncertainty, and advise urgent medical attention if red flags are present.
- A career-advice task where a user has two years of Python experience, no degree, retail work history, and a six-month goal of moving into data analysis. The expected answer would match skills, portfolio work, certificates, and application routes to the user's background.
- A research-synthesis task asking whether standing desks improve productivity. The model would need to handle mixed evidence, explain that reduced sitting is better supported than productivity improvement, and identify study limitations.
- A recipe-substitution task where a user needs an egg replacement for a sponge cake for a vegan guest. The model would recommend the most suitable substitute, give quantity guidance, and explain the texture trade-off.
- A financial-product comparison task where a user needs a savings account for an emergency fund. The model would prioritise instant access and low risk over the highest interest rate if withdrawal restrictions conflict with emergency use.
- A legal-information boundary task where a tenant asks whether a landlord can enter without notice but does not provide a location. The model would avoid inventing jurisdiction, state the dependency, summarise general guidance, and ask for the missing context.
- A technical tool-selection task where a small charity chooses between Google Sheets, Airtable, and a custom database for tracking volunteers. The model would favour a low-maintenance option for the charity's capacity while mentioning privacy and upgrade conditions.
- An unanswerable advisory task where a user asks which unpublished job offer will lead to faster promotion. The model would refuse the unsupported conclusion, identify missing information, and suggest questions to ask recruiters.
- A university policy task where a student asks about late coursework after illness. The model would apply the extension policy, explain required evidence and timing, and note uncertainty where approval rests with the department.

## 3. Dataset Composition

The first release should contain around 800 advisory tasks. This size gives enough coverage across domains while keeping evidence mapping and safety review feasible. The task families should include factual advisory, comparison and recommendation, procedural guidance, research synthesis, and high-stakes bounded advice.

The domains should include health information, education, consumer products, employment and careers, public services, finance, tenancy or legal information, technical tool choice, food and cooking, and general practical guidance. High-stakes domains should be included carefully because they are common in real use but require strong boundary-setting.

The data sources should include public guidance documents from reputable institutions, synthetic user scenarios grounded in Phase 1 task patterns, public product or service tables, public abstracts or report summaries, and researcher-written evidence packets with controlled conflicts and missing information. Each task should include an evidence map that marks supported claims, contradicted claims, unanswerable claims, user-specific constraints, required caveats, safety boundaries, and useful follow-up questions.

Quality control should include expert or domain-literate review for high-stakes topics. Medical, legal, and financial tasks should not ask the model to make binding professional decisions. They should instead test whether the model can provide useful information while preserving appropriate limits.

## 4. Evaluation Methodology

GroundedAdviceBench should use evidence-based scoring rather than simple answer matching. The primary metric should be a grounded advisory quality score. This score should capture factual correctness, grounding, context fit, uncertainty handling, actionability, safety boundary management, and completeness without overreach.

Automatic checks can compare response claims against the evidence map, detect prohibited claims, and check for required caveats. Human or validated LLM-judge scoring is still needed for context fit, usefulness, and uncertainty quality. The benchmark should report hallucination rate, unsupported recommendation rate, and missed-critical-caveat rate separately because these are central deployment failure modes.

For recommendation tasks, the scoring should not require one exact answer when multiple options are defensible. Instead, the benchmark should define acceptable recommendation sets and require the model to justify its advice using the user's constraints and the supplied evidence.

## 5. Validation Strategy

Validation should use domain-stratified pilot testing. A second reviewer should check every evidence map for completeness and correctness. High-stakes items should receive safety review to make sure the task framing does not encourage unsafe diagnosis, legal certainty, or financial guarantees.

I would run baseline models and inspect failures for hallucination, overconfidence, missed caveats, and irrelevant advice. Annotators should be trained on examples from each major task family, and inter-rater reliability should be reported. I would compare performance with SimpleQA/FACTS, MMLU-Pro, GPQA Diamond, LiveBench, and WildBench. GroundedAdviceBench should only partially correlate with those benchmarks because it measures contextual advice rather than knowledge alone.

The validation set should also include adversarial items where the evidence is insufficient, conflicting, or tempting but unsafe. A good model should be rewarded for saying that the evidence is insufficient when that is the correct advisory behaviour. The validation report should include confidence intervals by domain and task family and should identify whether high-stakes advice requires separate reporting.

## 6. Implementation Requirements

A first release would likely take 4 to 5 months. It would require a lead researcher, annotators for task and evidence-map construction, domain-literate reviewers for health, legal, finance, and education scenarios, and an engineer for scoring and dataset packaging.

The infrastructure would need a structured evidence-packet format, a claim-to-evidence mapping tool, an annotation platform, automated checks for required caveats and prohibited unsupported claims, and evaluation scripts for domain-level reporting. The cost level is medium, rising to high if extensive expert review is used for high-stakes domains.

The deliverables would include a public task schema, a development split with evidence maps, a private evaluation split, annotator guidelines, and a baseline model report covering hallucination and uncertainty metrics.

## 7. Expected Challenges and Mitigations

The main challenge is that evaluating advice is more subjective than evaluating factual answers. I would handle this by separating factual grounding from recommendation quality. The evidence map and user-constraint checklist should be applied before subjective usefulness scoring.

High-stakes domains also create safety risk. I would frame these tasks as information and triage guidance rather than diagnosis or professional decision-making. Required caveats and escalation guidance should be part of the rubric. Because multiple recommendations may be valid, the benchmark should score the justification against the evidence and constraints rather than requiring one predetermined answer.

Another challenge is that models may become overly cautious and unhelpful. To avoid rewarding safe but evasive responses, actionability should be part of the rubric. Evidence packets may also leak answer patterns, so the private split should vary formats, include conflicting evidence, include unanswerable items, and be refreshed.

## 8. Comparison to Existing Benchmarks

GroundedAdviceBench differs from MMLU-Pro and GPQA Diamond because those benchmarks measure knowledge and reasoning through multiple-choice questions, while this benchmark requires natural-language advice, user-context adaptation, evidence synthesis, and uncertainty handling. It differs from Humanity's Last Exam because it targets common advisory tasks rather than expert ceiling questions.

GroundedAdviceBench builds on SimpleQA and FACTS Grounding by keeping factuality and grounding central, but it extends beyond factual answers into recommendations, procedural guidance, conflicting evidence, and high-stakes boundary-setting. It borrows the value of refreshed evidence from LiveBench but isolates advisory behaviour as the construct. It also builds on WildBench's real-user orientation while using a controlled evidence-map design so that grounding and uncertainty can be scored more precisely. Compared with MMLongBench-Doc, it focuses less on document understanding alone and more on advice quality across multiple evidence snippets and user constraints.

The intended contribution is a benchmark that measures whether models can be useful and appropriately cautious advisors, not merely whether they can answer difficult questions.
