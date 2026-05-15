<!-- markdownlint-disable MD013 -->

# Benchmark Specification: WorkWriteBench

## 1. Capability Measured and Rationale

WorkWriteBench is my proposed benchmark for C01, Content Generation. I designed it to test whether large language models can produce useful workplace-oriented written artefacts under realistic constraints. The focus is professional writing, rewriting from briefs, audience adaptation, tone control, document transformation, and constraint-following in practical contexts.

The rationale comes from the Phase 3 gap analysis. C01 has a usage frequency of 0.256846, a normalised coverage score of 0.142857, and a gap score of 0.220154. The Phase 1 taxonomy shows common tasks such as drafting professional emails, creating marketing content, writing business strategy documents, producing legal correspondence, and composing personal communications. These tasks require outputs that fit audience, purpose, tone, and constraints, not just fluent generic prose.

The Phase 2 inventory shows that existing coverage is partial. IFEval measures verifiable instruction following but not substantive writing quality. WritingBench is the strongest current direct writing benchmark, but it is not specifically focused on workplace use. EQ-Bench Creative Writing v3 captures creative style and voice, while WildBench includes real-user writing prompts but is too broad for precise C01 attribution. WorkWriteBench targets the uncovered area of professional document creation where source facts, stakeholder audience, and practical usability matter.

## 2. Task Structure

Each WorkWriteBench item would give the model a writing brief, source facts, target audience, purpose, format requirements, and constraints. The model would produce a complete written artefact and, in some items, a short rationale explaining how the artefact addresses the audience and constraints.

The benchmark would cover professional communication, decision and strategy documents, marketing and public communication, technical and process documentation, academic and formal writing support, and audience or tone adaptation. Each item would include a brief, source facts that must be preserved, audience context, output format, required inclusions, prohibited claims, and rubric dimensions for factual preservation, audience fit, structure, tone, usefulness, and constraint adherence.

The following bullet points are examples of tasks that could exist in the proposed WorkWriteBench benchmark. They are intended to show the kind of writing situations the benchmark could include, not to define the final dataset.

- An executive project update based on notes about a two-week launch delay, payment provider API changes, 70 percent integration completion, customer beta status, and no budget increase. The expected output would be concise, accountable, and non-defensive.
- A customer apology email after a 45-minute dashboard outage affecting EU users. The response would explain what happened, what was done, and what will change, without blaming an individual engineer.
- A one-page security policy brief for non-technical managers about multi-factor authentication, conditional access, and device compliance checks. The output would explain what changes, why it matters, and what managers need to do.
- Landing-page copy for a budgeting app aimed at freelance designers. The output would be persuasive but would avoid guaranteeing tax savings.
- Release notes based on a technical changelog covering OAuth token refresh fixes, faster CSV export, keyboard navigation, and a deprecated webhook format. The model would translate technical changes into business-user language and flag action required.
- A 250-word grant application summary about this benchmark coverage gap project, including the purpose, methods, contribution, and expected toolkit outputs.
- An internal training announcement about a mandatory data protection refresher, with a friendly but firm tone and a clear deadline.
- An audience-adaptation task where the same performance-review facts must be rewritten separately for managers and employees while preserving factual consistency.
- An external developer documentation section about API rate limits, including behaviour, headers, error handling, and best practices.
- A sensitive rewriting task where an inflammatory vendor-termination sentence must be turned into neutral board-report language that preserves the material facts without subjective insult.

## 3. Dataset Composition

The first release should contain around 1,000 tasks across the six task families. This scale is feasible because writing tasks are cheaper to execute than repository-level coding tasks, although reliable scoring still requires careful human review.

The dataset should use realistic but non-sensitive source briefs. Suitable sources include public-domain business scenarios, synthetic workplace notes written by trained annotators, anonymised fictional examples, public product documentation, public policy documents, and researcher-authored briefs based on Phase 1 usage patterns. The dataset should not contain confidential emails, employee records, or personal data.

Each item should record metadata for the C01 sub-category, domain, audience, format, required facts, prohibited claims, tone requirement, expected length, risk level, and whether the output is a single artefact, a multi-version artefact, or a transformation from notes. Quality control should include two reviewers for brief clarity, a human reference answer, a fact inventory, a constraint checklist, and a calibrated rubric.

## 4. Evaluation Methodology

WorkWriteBench should use hybrid scoring because workplace writing quality is partly objective and partly judgement-based. The primary metric should be a weighted writing usefulness score that combines factual preservation, constraint adherence, audience fit, structure, tone, actionability, and risk management.

Automatic checks can assess length, required headings, required facts, prohibited claims, and some formatting constraints. Human evaluation or validated LLM-judge scoring is needed for audience fit, tone, usefulness, and writing quality. I would not use LLM judges without validation against human ratings because judge-dependent writing benchmarks can reward style or verbosity in ways that do not match human usefulness.

The benchmark should report total scores and dimension-level scores. This matters because a fluent answer should not be rewarded if it drops important facts, adds unsupported claims, or fails the audience.

## 5. Validation Strategy

Validation should begin with a 100-item pilot across all task families. Human writers should produce reference outputs for calibration, but model outputs should not be penalised simply for differing from the references. The target is whether the output satisfies the brief.

The validation process should map each task to C01 sub-categories, calibrate rubrics with at least three annotators, calculate inter-rater reliability, validate any LLM judge against human scores, evaluate weaker and stronger models for sensitivity, and review cultural or organisational bias. I would target weighted kappa above 0.75 for subjective dimensions and above 0.80 for factual or constraint dimensions.

## 6. Implementation Requirements

A first release would likely take 3 to 4 months. It would require a lead researcher, trained writers or annotators, reviewers for rubric calibration, and an engineer for the scoring harness and data packaging. The infrastructure would include a structured task database, an annotation platform, validators for length and required facts, and scripts for score aggregation and confidence intervals.

The cost level is medium, with human review being the main cost rather than compute. The deliverables would be a public task schema, a public development split with example rubrics, a private evaluation split, baseline model results, rubric documentation, and annotator guidelines.

## 7. Expected Challenges and Mitigations

The main challenge is that writing quality is subjective. I would manage this by using task-specific analytic rubrics rather than one general "good writing" score. Factual fidelity and constraint adherence should be separated from style preference.

LLM-judge bias is another risk, because automated judges may reward verbosity, familiar style, or outputs from models similar to themselves. I would calibrate against human ratings, use multiple judges only as secondary evidence, and publish disagreement analysis. Generic polished outputs should be penalised through fact inventories, audience-specific requirements, and prohibited-claim checks. Privacy risk should be handled by using synthetic and public-domain scenarios rather than confidential workplace documents.

## 8. Comparison to Existing Benchmarks

WorkWriteBench builds on IFEval by keeping verifiable constraint checks but adds substantive writing quality and audience adaptation. It differs from WritingBench by narrowing the construct to workplace and professional writing, where stakeholder needs and source facts are central. It differs from EQ-Bench because the target is not creative voice but practical artefacts such as memos, release notes, announcements, and decision briefs. It borrows WildBench's real-user orientation but isolates C01 and reports dimension-level results.

The intended contribution is a benchmark that asks whether generated text is usable, not just fluent. A strong model should preserve the brief, write for the audience, follow constraints, manage risk, and produce an artefact that would need minimal human repair.
