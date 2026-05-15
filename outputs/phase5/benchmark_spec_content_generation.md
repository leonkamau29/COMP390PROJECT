<!-- markdownlint-disable MD013 -->

# Benchmark Specification: WorkWriteBench - Workplace Writing, Rewriting, Constraints, and Audience Adaptation

## 1. Capability Measured and Rationale

**Target capability:** C01 - Content Generation.

WorkWriteBench is a proposed benchmark for evaluating whether large language models can produce useful workplace-oriented written artefacts under realistic constraints. The benchmark focuses on professional writing, rewriting from briefs, audience adaptation, tone control, document transformation, and constraint-following in practical contexts. It is designed to test the forms of content generation represented in the Phase 1 taxonomy: professional and business writing, marketing and promotional writing, technical and specialised writing, academic and educational writing, and controlled creative writing where the primary output is a newly composed artefact.

The rationale is grounded in the Phase 3 gap analysis. C01 is the second-highest gap-ranked capability, with a usage frequency of 0.256846, a normalised coverage score of 0.142857, and a gap score of 0.220154. The Phase 1 taxonomy records common real-world tasks such as drafting professional emails, creating marketing content, writing business strategy documents, producing legal correspondence, and composing personal communications. These tasks are common because users often need complete artefacts that fit audience, purpose, tone, and constraints rather than merely fluent text.

The Phase 2 inventory shows partial C01 coverage. IFEval (B011) evaluates instruction following using programmatically verifiable constraints, but it does not directly assess substantive writing quality. WritingBench (B012) is the strongest current C01 benchmark in the inventory because it evaluates open-ended writing across genres and subdomains, but it relies partly on critic models and is not specifically focused on workplace use. EQ-Bench Creative Writing v3 (B013) captures style, voice, and longform quality, but its prompt set is small and creative-writing focused. WildBench (B014) is grounded in real-user tasks and includes many writing prompts, but its broad scope makes capability attribution less precise. LiveBench (B010) includes language and instruction-following tasks but does not directly assess rich content-generation quality.

WorkWriteBench therefore targets a specific uncovered zone: realistic professional document creation where outputs must satisfy competing constraints, preserve supplied facts, adapt to a specified audience, and be usable with minimal human editing.

## 2. Task Structure

Each WorkWriteBench item gives the model a writing brief, factual source notes, target audience, purpose, format requirements, and constraints. The model must produce a complete written artefact. Some tasks also require a short rationale explaining how the output addresses the audience and constraints.

The benchmark is organised into six task families:

- **Professional communication:** emails, memos, announcements, meeting follow-ups, stakeholder updates.
- **Decision and strategy documents:** briefs, proposals, summaries for managers, risk notes.
- **Marketing and public communication:** product descriptions, landing-page copy, social posts, campaign variants.
- **Technical and process documentation:** user guides, release notes, onboarding documents, internal FAQs.
- **Academic and formal writing support:** abstracts, statements, structured summaries, formal letters.
- **Audience and tone adaptation:** rewriting the same facts for executives, customers, students, technical staff, or public audiences.

Each item includes:

- User brief.
- Source facts that must be preserved.
- Audience and context.
- Output format and length target.
- Required inclusions and exclusions.
- Risk constraints, such as avoiding legal claims, unsupported medical claims, or confidential detail.
- Rubric dimensions for factual preservation, audience fit, structure, tone, usefulness, and constraint adherence.

### Example Item 1: Executive Project Update

**Input:** A product manager provides bullet notes: launch delayed by two weeks because the payment provider changed API requirements; engineering has completed 70 percent of integration work; customer beta remains on schedule; no budget increase requested. Audience: executive leadership. Output: 180-220 word status update. Tone: concise, accountable, non-defensive.

**Expected output:** A polished status update that explains the delay, states impact, gives mitigation, and avoids overtechnical API detail.

**Evaluation criteria:** Facts are preserved; delay and mitigation are clear; tone is professional; length and audience requirements are met; no unsupported reassurance is added.

### Example Item 2: Customer Apology Email

**Input:** A SaaS company experienced a 45-minute dashboard outage affecting EU users. The root cause was a failed cache invalidation deployment. Write an apology email to affected customers. Include what happened, what was done, and what will change. Do not mention individual engineer error.

**Expected output:** A customer-facing email that acknowledges disruption, explains the issue in accessible terms, describes remediation, and avoids blame.

**Evaluation criteria:** Accountability without overdisclosure; accessible language; all required elements included; no confidential or speculative content.

### Example Item 3: Policy Brief For Non-Technical Managers

**Input:** Notes explain that the organisation is adopting multi-factor authentication, conditional access, and device compliance checks. Audience: department managers. Output: one-page brief explaining what changes, why, and what managers must do.

**Expected output:** A structured brief with headings, practical actions, and plain-language security rationale.

**Evaluation criteria:** Correctly explains security changes; avoids jargon; separates background from action items; preserves all source facts.

### Example Item 4: Product Landing Page Copy

**Input:** A startup sells a budgeting app for freelance designers. Features: invoice tracking, tax estimate alerts, project-level expenses, and monthly cash-flow forecasts. Audience: creative freelancers. Constraint: avoid claiming guaranteed tax savings.

**Expected output:** Persuasive landing-page copy with headline, subheading, feature bullets, and call to action.

**Evaluation criteria:** Audience fit; persuasive but not misleading; all key features represented; prohibited guarantee avoided.

### Example Item 5: Release Notes From Technical Changelog

**Input:** Changelog: fixed OAuth token refresh bug; improved CSV export speed by 35 percent in internal tests; added keyboard navigation to settings page; deprecated legacy webhook payload format. Audience: business users. Output: release notes with "New", "Improved", "Fixed", and "Action required" sections.

**Expected output:** Clear release notes that translate technical changes into user impact and flag webhook action required.

**Evaluation criteria:** Correct categorisation; user-facing language; action item is visible; no unexplained technical jargon.

### Example Item 6: Grant Application Summary

**Input:** Research notes describe a project on evaluating LLM benchmark coverage gaps, mixed methods, usage-weighted analysis, and practical toolkit outputs. Audience: university funding panel. Output: 250-word project summary.

**Expected output:** A formal summary explaining purpose, methods, contribution, and expected outputs.

**Evaluation criteria:** Academic tone; no exaggerated claims; clear contribution; includes methods and outputs.

### Example Item 7: Internal Training Announcement

**Input:** HR notes: mandatory data protection refresher; 45-minute online module; completion deadline 30 June; applies to all staff and student workers; managers receive weekly completion reports. Tone: friendly but firm.

**Expected output:** An announcement email with deadline, audience, reason, and next steps.

**Evaluation criteria:** Clear action; correct deadline; tone balance; no ambiguity about who must complete training.

### Example Item 8: Audience Adaptation From Same Facts

**Input:** Facts: the company is moving from annual to quarterly performance conversations; no salary decisions will be made in these conversations; employees should prepare goals and blockers. Produce two versions: one for managers and one for employees.

**Expected output:** Two distinct messages using the same facts but tailored to each audience's responsibilities and concerns.

**Evaluation criteria:** Audience-specific framing; factual consistency across versions; clear next steps for each audience.

### Example Item 9: Technical Documentation Introduction

**Input:** A developer provides notes for an API rate-limit page: 100 requests per minute per API key; 429 response on limit; `Retry-After` header; burst allowance of 20 requests; enterprise customers can request higher limits. Audience: external developers.

**Expected output:** A documentation section with overview, behaviour, error handling, and best practices.

**Evaluation criteria:** Technical accuracy; clear structure; complete coverage of limits and headers; no unsupported implementation detail.

### Example Item 10: Sensitive Rewriting With Constraint Preservation

**Input:** Draft sentence: "We fired the vendor because they were incompetent and wasted months of work." Rewrite for a board report. Facts: contract was terminated after missed delivery milestones and unresolved quality concerns. Tone: neutral, formal.

**Expected output:** A neutral board-report sentence or paragraph that communicates the same business fact without inflammatory language.

**Evaluation criteria:** Professional tone; preserves reason for termination; removes subjective insult; does not hide material information.

## 3. Dataset Composition

The proposed first release should contain **1,000 tasks** across six task families. This scale is appropriate because writing tasks are less costly to execute than repository-level coding tasks but more expensive to score reliably.

Suggested distribution:

- 250 professional communication tasks.
- 150 decision and strategy documents.
- 150 marketing and public communication tasks.
- 150 technical and process documentation tasks.
- 100 academic and formal writing tasks.
- 200 audience and tone adaptation tasks.

Tasks should be constructed from realistic but non-sensitive source briefs. Suitable sources include public-domain business scenarios, synthetic workplace notes written by trained annotators, anonymised and fictionalised examples, public product documentation, public policy documents, and researcher-authored briefs based on observed task patterns from the Phase 1 usage taxonomy. The dataset should not include confidential emails, real employee records, or personal data.

Each item should include metadata:

- C01 sub-category.
- Domain.
- Audience.
- Format.
- Required facts.
- Prohibited claims.
- Tone requirement.
- Expected length.
- Risk level.
- Whether output is single artefact, multi-version artefact, or transformation from notes.

Quality control should require:

- Two reviewers verifying that the brief is clear and realistic.
- One reference answer written by a trained human writer.
- A fact inventory listing source claims that must be preserved.
- A constraint checklist for programmatic or semi-programmatic validation.
- A rubric calibrated against human preferences.

To reduce contamination and benchmark gaming, a portion of tasks should be private or periodically refreshed. Template diversity is important because models can overfit to repeated formats. The benchmark should avoid rewarding overly generic polished prose by using task-specific constraints and factual checklists.

## 4. Evaluation Methodology

WorkWriteBench should use a hybrid scoring approach because workplace writing quality is partly objective and partly judgement-based.

**Primary metric:** weighted writing usefulness score, combining factual preservation, constraint adherence, audience fit, structure, tone, and actionability.

**Suggested rubric dimensions:**

- **Factual fidelity:** all required source facts are included and no unsupported facts are introduced.
- **Constraint adherence:** length, format, required inclusions, exclusions, and style constraints are followed.
- **Audience fit:** language, framing, and detail level match the specified recipient.
- **Purpose fulfilment:** the output accomplishes the user goal, such as persuading, informing, requesting action, or documenting change.
- **Structure and readability:** organisation is clear and usable.
- **Tone control:** tone matches the brief and avoids inappropriate register.
- **Risk management:** avoids prohibited claims, confidentiality breaches, legal overstatement, or unsafe advice.

Automatic checks can assess length, required terms, prohibited phrases, section headings, and factual claim coverage where claims are explicitly listed. Human evaluation or calibrated LLM-judge evaluation should score audience fit, tone, usefulness, and writing quality. LLM-judge scoring should not be used without validation against human ratings because WritingBench and EQ-Bench both illustrate the usefulness and risk of judge-dependent evaluation.

The benchmark should report both total score and dimension-level scores. This prevents a fluent but factually inaccurate answer from receiving an inflated score.

## 5. Validation Strategy

Validation should begin with a 100-item pilot across all task families. Human writers should produce reference outputs for calibration, but model outputs should not be penalised merely for differing from references. The core scoring target is whether the output satisfies the brief.

Validation steps:

1. **Construct alignment:** Map each item to C01 sub-categories from the Phase 1 taxonomy.
2. **Rubric calibration:** Have at least three annotators score a sample of 50 outputs using the rubric.
3. **Reliability check:** Calculate inter-rater reliability for categorical or ordinal rubric decisions, targeting weighted kappa above 0.75 for subjective dimensions and above 0.80 for factual/constraint dimensions.
4. **Judge validation:** If LLM judges are used, compare judge scores against human scores and report correlation and disagreement patterns.
5. **Known-model sanity checks:** Evaluate weaker and stronger models to confirm the benchmark distinguishes quality without saturating immediately.
6. **Bias review:** Check whether tasks systematically favour particular cultural, corporate, or native-English writing conventions.

The validation report should identify which scoring dimensions are reliable enough for headline reporting. Dimensions with weak reliability should remain diagnostic rather than central.

## 6. Implementation Requirements

**Estimated time:** 3-4 months for 1,000 tasks and validated rubrics.

**Personnel:**

- 1 lead researcher for taxonomy alignment and design.
- 3-5 trained writers or annotators for task and reference construction.
- 2-3 reviewers for rubric calibration.
- 1 engineer for scoring harness, automatic checks, and data packaging.

**Infrastructure:**

- Structured task database, preferably CSV/JSON.
- Annotation platform for pairwise and rubric scoring.
- Automatic validators for length, headings, required facts, and prohibited content.
- Evaluation scripts for score aggregation and confidence intervals.

**Estimated cost level:** Medium. The main cost is human review, not compute.

**Deliverables:**

- Public task schema.
- Public development split with example rubrics.
- Private evaluation split.
- Baseline model results.
- Rubric documentation and annotator guidelines.

## 7. Expected Challenges and Mitigations

**Challenge: subjectivity of writing quality.** Different readers may prefer different styles.

**Mitigation:** Use task-specific analytic rubrics rather than a single "good writing" score. Separate factual fidelity and constraint adherence from style preference.

**Challenge: LLM-judge bias.** Automated judges may reward verbosity, familiar style, or models similar to themselves.

**Mitigation:** Calibrate against human ratings, use multiple judges only as secondary evidence, and publish disagreement analysis.

**Challenge: generic outputs can appear polished but fail the brief.**

**Mitigation:** Include fact inventories, audience-specific constraints, and prohibited claims so generic prose is penalised.

**Challenge: privacy and realism.** Real workplace documents often contain sensitive data.

**Mitigation:** Use synthetic and public-domain scenarios modelled on real task patterns, not confidential user documents.

**Challenge: cultural and organisational variation.** "Professional tone" differs by context.

**Mitigation:** Specify audience, organisation type, and register in each task; include diverse sectors and communication norms.

## 8. Comparison to Existing Benchmarks

**IFEval (B011)** provides useful automated constraint checks, but it mainly measures whether explicit instructions are followed. WorkWriteBench incorporates programmatic constraint checks while adding substantive writing quality, factual preservation, audience adaptation, and practical usefulness.

**WritingBench (B012)** is the strongest current open-ended writing benchmark in the inventory. WorkWriteBench narrows the construct to workplace and professional writing, where source facts, stakeholder audience, and risk constraints matter more than general genre quality.

**EQ-Bench Creative Writing v3 (B013)** captures creative style, emotional authenticity, and voice. WorkWriteBench differs by targeting professional artefacts such as memos, release notes, announcements, and decision briefs.

**WildBench (B014)** provides strong real-user grounding, including writing prompts. WorkWriteBench borrows the principle of user-task realism but isolates C01 and gives dimension-level scoring rather than broad checklist judging across many capabilities.

**LiveBench (B010)** includes language and instruction-following elements but does not directly evaluate rich content-generation quality. WorkWriteBench targets that gap explicitly.

The intended contribution is a benchmark that evaluates whether generated text is not only fluent, but usable: factually grounded in the user's brief, suitable for the audience, compliant with constraints, and ready for practical workplace deployment.
