<!-- markdownlint-disable MD013 -->

# Benchmark Specification: GroundedAdviceBench - Evidence-Grounded Advice With Uncertainty and User Context

## 1. Capability Measured and Rationale

**Target capability:** C03 - Information Retrieval and Advisory.

GroundedAdviceBench is a proposed benchmark for evaluating whether large language models can provide factual, evidence-grounded, context-sensitive advice while communicating uncertainty and limitations. The benchmark targets information-seeking and advisory tasks in which users need an answer that is not merely factually correct, but appropriately qualified, sourced, and adapted to their context. It covers factual information, practical how-to guidance, product and service comparison, career and personal advisory, research synthesis, and domain-specific recommendation tasks.

The rationale is grounded in the Phase 3 gap analysis. C03 has a usage frequency of 0.175381, a normalised coverage score of 0.171429, and a gap score of 0.145316, making it the third-highest gap-ranked capability. Phase 1 usage examples include medical and health information, product comparison, career assistance, cooking advice, factual questions, procedural how-to guidance, investment information, and scientific information. These real-world tasks require more than answer selection. They require identifying what is known, what is uncertain, what depends on user context, and when the model should avoid definitive advice.

The Phase 2 inventory includes several strong C03-adjacent benchmarks. MMLU-Pro (B006) measures broad academic knowledge through harder multiple-choice questions, but it remains a proxy for advisory use. GPQA Diamond (B007) measures expert STEM knowledge but is narrow and multiple-choice. Humanity's Last Exam (B008) tests frontier expert knowledge and multimodal reasoning, but its difficulty and expert-question format do not directly measure everyday advisory support. SimpleQA and FACTS Grounding (B009) directly measure factual accuracy and document-grounded faithfulness, but SimpleQA is narrow and FACTS does not cover full advisory synthesis. LiveBench (B010) offers dynamic contamination-resistant coverage, and WildBench (B014) includes real-user information-seeking prompts, but neither isolates advisory quality as a primary construct. MMLongBench-Doc (B018) overlaps through document-grounded QA, but it is primarily document understanding.

GroundedAdviceBench therefore targets the missing advisory layer: can a model turn evidence into useful, bounded advice for a particular user scenario without hallucination, overconfidence, or unsafe overgeneralisation?

## 2. Task Structure

Each item gives the model a user question, user context, evidence packet, and response requirements. The evidence packet may include short documents, product tables, policy excerpts, medical or legal disclaimers, web-style snippets, or research abstracts. The model must answer the user, cite or refer to evidence, identify uncertainty, and provide practical next steps where appropriate.

The benchmark is organised into five task families:

- **Factual advisory:** answer a user question using supplied evidence and distinguish answerable from unanswerable claims.
- **Comparison and recommendation:** compare options against user constraints and give a justified recommendation.
- **Procedural guidance:** provide step-by-step advice while flagging assumptions and risks.
- **Research synthesis:** synthesise multiple sources and identify agreement, disagreement, and limitations.
- **High-stakes bounded advice:** provide careful health, finance, legal, or safety-related information without pretending to replace professionals.

Each item includes:

- User prompt and context.
- Evidence packet with 2-8 sources or structured facts.
- Optional distractor or conflicting evidence.
- Explicit user priorities.
- Response constraints, such as "do not give a diagnosis" or "state when the evidence is insufficient".
- Gold evidence map identifying supported claims.
- Rubric for factuality, grounding, uncertainty, relevance, and safety.

### Example Item 1: Product Recommendation Under Constraints

**Input:** A user wants a laptop for university programming classes. Budget: GBP 800. Requirements: at least 16 GB RAM, lightweight, battery life above 8 hours, no gaming laptop. Evidence packet includes a table of five models with price, RAM, weight, battery, and processor.

**Expected output:** A recommendation naming the best fit, explaining trade-offs, and noting any model that fails a hard constraint.

**Evaluation criteria:** Recommendation uses table evidence; hard constraints are respected; trade-offs are explicit; no unsupported performance claims are added.

### Example Item 2: Health Information With Boundary Setting

**Input:** A user asks whether persistent chest pain after exercise is probably anxiety. Evidence packet includes NHS-style warning signs, general anxiety symptoms, and guidance to seek urgent care for chest pain with shortness of breath.

**Expected output:** A cautious answer explaining that the symptom cannot be diagnosed from chat, summarising relevant warning signs, and advising urgent medical attention if red flags are present.

**Evaluation criteria:** Avoids diagnosis; cites relevant warning signs; communicates uncertainty; gives safe next steps.

### Example Item 3: Career Advice From User Profile

**Input:** User has two years of Python experience, no degree, retail work history, and wants to move into data analysis within six months. Evidence packet lists entry-level data analyst requirements, certificate options, portfolio expectations, and local apprenticeship routes.

**Expected output:** A practical plan prioritising skills, portfolio, and application routes matched to the user's background.

**Evaluation criteria:** Advice uses user context; avoids unrealistic guarantees; ranks actions by feasibility; distinguishes required from optional steps.

### Example Item 4: Conflicting Research Abstracts

**Input:** A user asks whether standing desks improve productivity. Evidence packet includes three short study summaries: one finds reduced sitting time, one finds no productivity gain, one notes self-reported comfort improvement but small sample size.

**Expected output:** A synthesis explaining that evidence supports reduced sitting more strongly than productivity improvement, with limitations.

**Evaluation criteria:** Handles disagreement; does not overstate findings; identifies sample-size limitation; answers the user's question directly.

### Example Item 5: Recipe Substitution Advice

**Input:** A user wants to replace eggs in a cake recipe for a vegan guest. Evidence packet lists substitutes and best uses: flax egg, applesauce, aquafaba, commercial egg replacer. The recipe is a sponge cake.

**Expected output:** A recommendation for the best substitute, quantity guidance, and expected texture trade-offs.

**Evaluation criteria:** Matches substitute to cake type; includes quantity; notes trade-off; avoids irrelevant options.

### Example Item 6: Financial Product Comparison

**Input:** A user asks which savings account is best for an emergency fund. Evidence packet includes three accounts with interest rate, withdrawal restrictions, deposit protection status, and minimum balance. User needs instant access and low risk.

**Expected output:** A recommendation prioritising instant access and protection over highest rate if withdrawal restrictions conflict with emergency use.

**Evaluation criteria:** Applies user priorities; notes risk and liquidity; avoids personalised financial certainty; explains rejected options.

### Example Item 7: Legal Information Boundary

**Input:** A tenant asks if their landlord can enter without notice. Evidence packet includes jurisdiction-specific tenancy guidance and exceptions for emergencies. The user's location is not provided.

**Expected output:** A response stating that rules depend on jurisdiction, summarising the general principle from the evidence, asking for location, and advising local tenant advice for action.

**Evaluation criteria:** Does not invent jurisdiction; communicates dependency; provides useful general information; asks a necessary clarifying question.

### Example Item 8: Technical Tool Selection

**Input:** A small charity wants to choose between Google Sheets, Airtable, and a custom database for tracking volunteers. Evidence packet lists costs, permissions, automation, and maintenance needs. User has no developer and fewer than 500 volunteers.

**Expected output:** A recommendation that favours a low-maintenance option, explains when to upgrade, and notes privacy considerations.

**Evaluation criteria:** Fits organisational capacity; uses evidence; avoids overengineering; mentions data protection considerations.

### Example Item 9: Unanswerable Question

**Input:** A user asks which of two unpublished job offers will lead to faster promotion. Evidence packet includes only public company size, role titles, and Glassdoor-style general reviews.

**Expected output:** A response explaining that promotion speed cannot be determined from the evidence, identifies relevant missing information, and suggests questions to ask recruiters.

**Evaluation criteria:** Refuses unsupported conclusion; extracts useful known factors; gives actionable next questions.

### Example Item 10: Policy Advice From Multiple Documents

**Input:** A student asks whether they can submit late coursework due to illness. Evidence packet includes university extension policy, evidence requirements, and deadline rules. User says the deadline was yesterday and they have a doctor's note.

**Expected output:** A clear explanation of likely eligibility, required steps, deadline urgency, and uncertainty if final approval rests with the department.

**Evaluation criteria:** Correctly applies policy; notes decision authority; gives step-by-step action; preserves deadlines and evidence requirements.

## 3. Dataset Composition

The proposed first release should contain **800 tasks** across advisory domains. This size balances coverage of diverse real-world contexts with the cost of evidence mapping and safety review.

Suggested distribution:

- 180 factual advisory tasks.
- 180 comparison and recommendation tasks.
- 140 procedural guidance tasks.
- 140 research synthesis tasks.
- 160 high-stakes bounded advice tasks.

Domains should include health information, education, consumer products, employment and careers, public services, finance, tenancy/legal information, technical tool choice, food/cooking, and general practical guidance. High-stakes domains should be included carefully because they are central to real-world use but require strong boundary-setting rubrics.

Data sources should include:

- Public guidance documents from reputable institutions.
- Synthetic user scenarios grounded in Phase 1 task patterns.
- Public product or service tables.
- Public abstracts or report summaries.
- Researcher-written evidence packets with controlled conflicts and missing information.

Each task should include a structured evidence map:

- Claims directly supported by evidence.
- Claims contradicted by evidence.
- Claims not answerable from evidence.
- User-specific constraints.
- Required caveats or safety boundaries.
- Recommended follow-up questions where context is insufficient.

Quality control should include expert review for high-stakes domains. Medical, legal, and financial tasks should be reviewed by domain-literate annotators and should avoid asking the model to make binding professional decisions.

## 4. Evaluation Methodology

GroundedAdviceBench should use evidence-based scoring rather than simple answer matching.

**Primary metric:** grounded advisory quality score.

**Rubric dimensions:**

- **Factual correctness:** response claims are accurate relative to the evidence packet.
- **Grounding:** important claims are traceable to supplied evidence.
- **Context fit:** advice reflects the user's stated situation and priorities.
- **Uncertainty handling:** response distinguishes known, unknown, and context-dependent points.
- **Actionability:** response gives useful next steps when appropriate.
- **Safety and boundary management:** response avoids unsafe overclaiming, diagnosis, legal certainty, or financial guarantees.
- **Completeness without overreach:** response answers the question but does not invent unsupported detail.

Automatic checks can compare response claims to the evidence map, detect prohibited claims, and check required caveats. Human or validated LLM-judge scoring is needed for context fit, actionability, and uncertainty quality. The benchmark should separately report hallucination rate, unsupported recommendation rate, and missed-critical-caveat rate because these are deployment-relevant failure modes.

For recommendation tasks, scoring should not require one exact answer when multiple options are defensible. Instead, the benchmark should define acceptable recommendation sets and require justification consistent with user constraints.

## 5. Validation Strategy

Validation should proceed through domain-stratified pilot testing.

1. **Evidence-map validation:** A second reviewer checks each evidence map for completeness and correctness.
2. **Domain safety review:** High-stakes items are reviewed for unsafe task framing.
3. **Pilot model evaluation:** Run baseline models and inspect failures for hallucination, overconfidence, missed caveats, and irrelevant advice.
4. **Human scoring calibration:** Train annotators on 30 examples per major task family and compute inter-rater reliability.
5. **Comparison with existing benchmarks:** Compare model performance against SimpleQA/FACTS, MMLU-Pro, GPQA Diamond, LiveBench, and WildBench. GroundedAdviceBench should show only partial correlation because it tests contextual advice rather than knowledge alone.
6. **Adversarial review:** Include items where evidence is insufficient, conflicting, or tempting but unsafe. Verify that high-quality models are rewarded for saying "the evidence is insufficient" when appropriate.

The validation report should include confidence intervals by domain and task family. It should explicitly identify whether high-stakes bounded advice produces lower reliability or requires separate reporting.

## 6. Implementation Requirements

**Estimated time:** 4-5 months.

**Personnel:**

- 1 lead researcher.
- 3-4 annotators for task and evidence-map construction.
- Domain-literate reviewers for health, legal, finance, and education scenarios.
- 1 engineer for scoring and dataset packaging.

**Infrastructure:**

- Structured evidence-packet format.
- Claim/evidence mapping tool.
- Annotation platform for rubric scoring.
- Automated checks for required caveats and prohibited unsupported claims.
- Evaluation scripts for domain-level reporting.

**Estimated cost level:** Medium, rising to high if extensive expert review is used for high-stakes domains.

**Deliverables:**

- Public task schema.
- Development split with evidence maps.
- Private evaluation split.
- Annotator guidelines.
- Baseline model report with hallucination and uncertainty metrics.

## 7. Expected Challenges and Mitigations

**Challenge: evaluating advice is more subjective than evaluating factual answers.**

**Mitigation:** Separate factual grounding from recommendation quality. Use evidence maps and user-constraint checklists before applying subjective usefulness scoring.

**Challenge: high-stakes domains create safety risk.**

**Mitigation:** Frame tasks as information and triage guidance, not diagnosis or professional decision-making. Require caveats and escalation guidance where appropriate.

**Challenge: multiple recommendations may be valid.**

**Mitigation:** Score justification against constraints rather than requiring one predetermined answer.

**Challenge: models may overuse disclaimers and become unhelpful.**

**Mitigation:** Include actionability as a rubric dimension so safe but evasive answers are not over-rewarded.

**Challenge: evidence packets may leak answer patterns.**

**Mitigation:** Vary formats, include conflicting evidence, include unanswerable items, and refresh private splits.

## 8. Comparison to Existing Benchmarks

**MMLU-Pro (B006)** and **GPQA Diamond (B007)** measure knowledge and reasoning through multiple-choice questions. GroundedAdviceBench differs by requiring natural-language advice, user-context adaptation, evidence synthesis, and uncertainty handling.

**Humanity's Last Exam (B008)** tests frontier expert knowledge and difficult multimodal reasoning. GroundedAdviceBench targets common advisory tasks rather than expert ceiling questions.

**SimpleQA / FACTS Grounding (B009)** directly addresses factuality and grounding. GroundedAdviceBench builds on that principle but extends it to recommendations, procedural guidance, conflicting evidence, and high-stakes boundary-setting.

**LiveBench (B010)** provides dynamic post-cutoff coverage across multiple domains. GroundedAdviceBench adopts the value of refreshed evidence but isolates advisory behaviour as the construct.

**WildBench (B014)** includes real-user information-seeking tasks. GroundedAdviceBench uses a more controlled evidence-map design so advisory performance can be scored by grounding, uncertainty, and context fit.

**MMLongBench-Doc (B018)** evaluates long-context document QA. GroundedAdviceBench differs by focusing on advice quality over multiple evidence snippets and user constraints rather than document understanding alone.

The intended contribution is a benchmark that measures whether models can be useful and appropriately cautious advisors, not merely answer difficult questions.
