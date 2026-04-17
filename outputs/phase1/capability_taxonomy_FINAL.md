# LLM Capability Taxonomy — FINAL

**Project:** Benchmark Coverage Gap: A Systematic Analysis of Real-World AI Capabilities and Evaluation Practices
**Student:** Leon Kamau Kiunga (201759400)
**Supervisor:** Dr Konstantinos Tsakaldis
**Phase:** Phase 1 — Capability Framework Development (Week 4)
**Version:** FINAL
**Method:** Braun & Clarke (2006) six-phase thematic analysis
**Primary sources:** Handa et al. (2025) Anthropic Economic Index (arXiv:2503.04761); O\*NET Detailed Work Activities; Chatterji et al. (2025) How People Use ChatGPT (NBER WP 34255); Aubakirova et al. (2025) State of AI: 100 Trillion Token Study (OpenRouter)

---

## Validation Summary

| Metric                              | Target               | Result                      | Status |
| ----------------------------------- | -------------------- | --------------------------- | ------ |
| Coverage of Anthropic top 100 tasks | ≥95%                | 100/100 (100.0%)            | PASS   |
| Cohen's κ (10% subsample, n=10)    | >0.8                 | 1.0000                      | PASS   |
| Number of core capabilities         | 6–10                | 8                           | PASS   |
| Worked examples per capability      | ≥5                  | 5–8 per capability         | PASS   |
| Decision rules documented           | All                  | All 8 capabilities          | PASS   |
| Edge cases resolved                 | All                  | All 8 capabilities          | PASS   |
| Sources                             | Empirical usage data | Handa et al. (2025); O\*NET | PASS   |

**Phase 1 Completion Criterion: MET.** Taxonomy covers 100% of Anthropic top 100 tasks (target ≥95%) and achieves Cohen's κ = 1.00 (target >0.8).

---

## Capability Distribution in Anthropic Top 100 Tasks

| Capability                                          | Tasks (of 100) | % of Top 100   |
| --------------------------------------------------- | -------------- | -------------- |
| C02 — Code Development & Technical Problem Solving | 36             | 36.0%          |
| C03 — Information Retrieval & Advisory             | 23             | 23.0%          |
| C01 — Content Generation                           | 18             | 18.0%          |
| C07 — Data Analysis & Summarisation                | 8              | 8.0%           |
| C05 — Review & Feedback                            | 6              | 6.0%           |
| C04 — Learning & Education Support                 | 5              | 5.0%           |
| C06 — Translation & Language Processing            | 2              | 2.0%           |
| C08 — Conversational Interaction & Roleplay        | 2              | 2.0%           |
| **Total**                                     | **100**  | **100%** |

---

## Overview

This taxonomy defines **8 core capabilities** representing distinct modes of LLM interaction. It was derived through six-phase thematic analysis (Braun & Clarke, 2006) applied to 123 empirically documented task instances from the Anthropic Economic Index (Handa et al., 2025) and O\*NET occupational task data. It is the primary analytical framework for the benchmark coverage analysis in Phase 3.

| ID  | Capability Name                              | Core Function                                                              |
| --- | -------------------------------------------- | -------------------------------------------------------------------------- |
| C01 | Content Generation                           | Producing new written artefacts from a prompt                              |
| C02 | Code Development & Technical Problem Solving | Writing, debugging, or configuring code and technical systems              |
| C03 | Information Retrieval & Advisory             | Answering questions and providing guidance from domain knowledge           |
| C04 | Learning & Education Support                 | Teaching and scaffolding understanding for a learner                       |
| C05 | Review & Feedback                            | Evaluating and improving a user-provided artefact                          |
| C06 | Translation & Language Processing            | Converting text between languages or supporting language learning          |
| C07 | Data Analysis & Summarisation                | Processing existing data or documents to extract insight or condensed form |
| C08 | Conversational Interaction & Roleplay        | Sustained interactive dialogue, roleplay, or open-ended conversation       |

---

## C01 — Content Generation

### Formal Definition

Content Generation refers to LLM interactions in which the primary output is a novel written artefact — a document, text, plan, script, or creative work — produced in response to a user prompt or partial input. The artefact did not exist before the interaction and is created to serve a specified communicative, professional, academic, or creative purpose. The LLM's role is generative: it authors rather than evaluates, transforms, or retrieves.

### Hierarchical Sub-categories

| Sub-category                            | Description                                                                  |
| --------------------------------------- | ---------------------------------------------------------------------------- |
| C01a — Academic Writing                | Essays, reports, assignments, theses for educational contexts                |
| C01b — Professional & Business Writing | Emails, business plans, reports, proposals, marketing copy                   |
| C01c — Creative Writing                | Fiction, poetry, scripts, song lyrics, creative narratives                   |
| C01d — Technical Documentation         | API docs, system architecture write-ups, user manuals, README files          |
| C01e — Personal & Social Writing       | Personal letters, social media posts, relationship messages, religious texts |
| C01f — Legal & Formal Documents        | Contracts, legal briefs, formal correspondence, dispute letters              |

### Decision Rule

A task belongs to C01 **if and only if**:

1. The user's primary goal is to obtain a new written artefact (not an improved version of existing work → C05, not a factual answer → C03, not code → C02), **AND**
2. The LLM's contribution is authoring that artefact from scratch or from minimal user-provided material.

### Resolution of Ambiguous Cases

| Ambiguous case                                                     | Resolution | Rationale                                        |
| ------------------------------------------------------------------ | ---------- | ------------------------------------------------ |
| User provides a rough outline; asks LLM to write the full document | → C01     | Outline is scaffolding; LLM authors the artefact |
| User provides a full draft and asks for improvements               | → C05     | Existing artefact is primary input               |
| Summarising a document for a slide deck                            | → C07     | Condensation of existing material                |
| Writing an essay about a topic from memory                         | → C01     | Output is a new document                         |

### Worked Examples

1. "Complete academic assignments and create educational materials across all subjects" (Handa et al., 2025, rank 1, 4.98%) → C01a
2. "Write, develop, and edit original creative fiction across multiple genres" (rank 7, 2.90%) → C01c
3. "Draft and revise professional workplace correspondence and business communications" (rank 9, 2.44%) → C01b
4. "Create and optimize marketing content across multiple formats and industries" (rank 10, 2.38%) → C01b
5. "Create technical documentation, diagrams, and architectural designs" (rank 17, 1.58%) → C01d
6. "Draft, review, and analyze legal documents and court filings" (rank 30, 1.09%) → C01f
7. "Assist with business planning, strategy, and entrepreneurial development" (rank 6, 3.00%) → C01b

---

## C02 — Code Development & Technical Problem Solving

### Formal Definition

Code Development & Technical Problem Solving refers to LLM interactions in which the output is executable code, a configuration, a technical specification, or a systematic procedure for resolving a software, hardware, or infrastructure problem. The LLM applies knowledge of programming languages, systems architecture, protocols, and technical tools to produce or repair functional technical artefacts or resolve technical failures.

### Hierarchical Sub-categories

| Sub-category                              | Description                                                     |
| ----------------------------------------- | --------------------------------------------------------------- |
| C02a — Code Generation                   | Writing new functions, modules, scripts, or applications        |
| C02b — Debugging & Bug Fixing            | Identifying and correcting errors in existing code              |
| C02c — Code Review & Refactoring         | Improving code quality, readability, and efficiency             |
| C02d — Infrastructure & DevOps           | Configuring servers, CI/CD pipelines, Docker, cloud, networking |
| C02e — Database & Data Engineering       | Writing SQL, designing schemas, managing data pipelines         |
| C02f — Specialised Technical Development | ML/AI systems, embedded systems, game dev, security, blockchain |

### Decision Rule

A task belongs to C02 **if and only if**:

1. The primary output is code, a configuration, a technical specification, or a systematic technical procedure, **AND**
2. The task requires applied knowledge of programming, systems, or technical infrastructure.

### Resolution of Ambiguous Cases

| Ambiguous case                    | Resolution | Rationale                                         |
| --------------------------------- | ---------- | ------------------------------------------------- |
| "Explain what this code does"     | → C04     | Explanation without producing code is educational |
| "Fix the bug in my code"          | → C02b    | Output is corrected code                          |
| "What is an API?"                 | → C04     | Conceptual question, no code output               |
| "Troubleshoot my WiFi connection" | → C02d    | Technical resolution procedure                    |

### Worked Examples

1. "Debug, fix, and refactor code across programming languages" (rank 2, 4.53%) → C02b/C02c
2. "Build, debug, and customize web applications and websites" (rank 4, 3.57%) → C02a
3. "Debug and fix CSS, HTML, and UI layout and styling issues" (rank 8, 2.63%) → C02b
4. "Help with machine learning, AI development, and technical implementation" (rank 20, 1.35%) → C02f
5. "Help with SQL queries, database design, and optimization" (rank 38, 0.87%) → C02e
6. "Troubleshoot and configure Docker, Kubernetes, and virtualization platforms" (rank 55, 0.57%) → C02d
7. "Configure and troubleshoot development infrastructure, CI/CD, and deployment systems" (rank 68, 0.45%) → C02d

---

## C03 — Information Retrieval & Advisory

### Formal Definition

Information Retrieval & Advisory refers to LLM interactions in which the user seeks to obtain factual information, domain-specific knowledge, recommendations, or guidance from the LLM. The LLM acts as a knowledgeable informant, synthesising and applying its training knowledge to answer questions, compare options, or support a decision. The primary output is a response containing information or a recommendation — not a new document (→ C01), executable code (→ C02), or structured pedagogy (→ C04).

### Hierarchical Sub-categories

| Sub-category                             | Description                                                                  |
| ---------------------------------------- | ---------------------------------------------------------------------------- |
| C03a — Factual Question Answering       | Answering specific factual queries from domain knowledge                     |
| C03b — Research & Literature Synthesis  | Synthesising information across sources; summarising a field                 |
| C03c — Product & Service Recommendation | Comparing and recommending products, tools, or services                      |
| C03d — Personal & Professional Advisory | Career, finance, health, relationship, and life-skills guidance              |
| C03e — Domain Expert Consultation       | Advice requiring specialised professional knowledge (law, medicine, finance) |

### Decision Rule

A task belongs to C03 **if and only if**:

1. The user's primary goal is to obtain information, recommendations, or decision support, **AND**
2. The output is an answer, explanation, or recommendation — not a new content artefact (→ C01), code (→ C02), or a pedagogically structured lesson (→ C04).

### Resolution of Ambiguous Cases

| Ambiguous case                            | Resolution | Rationale                     |
| ----------------------------------------- | ---------- | ----------------------------- |
| "What is the capital of France?"          | → C03a    | Simple factual retrieval      |
| "Teach me about the French Revolution"    | → C04     | Pedagogical orientation       |
| "Write a report on the French Revolution" | → C01     | New document as output        |
| "Help me choose between Python and R"     | → C03c    | Recommendation and comparison |

### Worked Examples

1. "Help research, compare, and select consumer products for purchasing decisions" (rank 5, 3.10%) → C03c
2. "Provide medical and health-related information across multiple specialties" (rank 24, 1.24%) → C03e
3. "Provide relationship, dating, parenting, and family advice" (rank 40, 0.85%) → C03d
4. "Provide personal finance guidance and perform financial calculations" (rank 44, 0.71%) → C03d
5. "Assist with multidisciplinary scientific research and academic projects" (rank 34, 0.96%) → C03b
6. "Find local information about places, services, restaurants, and cultural topics" (rank 60, 0.53%) → C03a
7. "Provide general information regarding investment and portfolio management" (rank 72, 0.43%) → C03e

---

## C04 — Learning & Education Support

### Formal Definition

Learning & Education Support refers to LLM interactions in which the LLM acts as a tutor, instructor, or mentor, structuring knowledge to facilitate the user's comprehension of a concept, skill, or procedure. The defining feature distinguishing C04 from C03 is pedagogical intent: the LLM scaffolds understanding (explains why, demonstrates how, provides worked examples, checks understanding) rather than simply delivering a factual answer. The user's goal is to develop capability, not merely obtain information.

### Hierarchical Sub-categories

| Sub-category                   | Description                                                       |
| ------------------------------ | ----------------------------------------------------------------- |
| C04a — Concept Explanation    | Explaining ideas, theories, or mechanisms at an appropriate level |
| C04b — Worked Problem Solving | Walking through problems step-by-step (maths, science, logic)     |
| C04c — Skill Instruction      | Teaching a skill progressively (programming, language, writing)   |
| C04d — Adaptive Tutoring      | Diagnosing misunderstanding and adjusting instruction level       |

### Decision Rule

A task belongs to C04 **if and only if**:

1. The user's explicit or implicit goal is to develop understanding or competence, **AND**
2. The LLM's response is structured pedagogically (explains, demonstrates, scaffolds), not merely factual, **AND**
3. The interaction is oriented toward building user capability rather than completing a task on the user's behalf.

### Resolution of Ambiguous Cases

| Ambiguous case                   | Resolution | Rationale                        |
| -------------------------------- | ---------- | -------------------------------- |
| "Explain recursion step by step" | → C04b    | Explicit pedagogical structure   |
| "Write recursive code for me"    | → C02a    | Task completion, not instruction |
| "Teach me SQL"                   | → C04c    | Educational instruction          |
| "Write a SQL query for me"       | → C02     | Code production                  |

### Worked Examples

1. "Help me learn programming languages and software development concepts" (rank 15, 1.80%) → C04c
2. "Help solve mathematics problems from basic arithmetic to advanced university-level topics" (rank 22, 1.32%) → C04b
3. "Help with algorithms, data structures, and competitive programming tasks" (rank 50, 0.63%) → C04a/C04c
4. "Help with physics problems, coursework, and educational explanations" (rank 79, 0.36%) → C04a/C04b
5. "Solve engineering physics problems and debug simulation code" (rank 67, 0.46%) → C04b
6. "Assist with quantum mechanics and quantum computing topics" (rank 109, 0.06%) → C04a
7. O\*NET: "Adapt instructional content or delivery methods for different levels or types of learners" (0.134%) → C04d

---

## C05 — Review & Feedback

### Formal Definition

Review & Feedback refers to LLM interactions in which the user submits an existing artefact — a written document, code, argument, or piece of work — and the LLM evaluates, critiques, annotates, or produces an improved version. The primary input is the user's artefact; the primary output is an assessment, edited version, or structured critique. This capability is distinguished from C01 (where the LLM authors from scratch) and C02b (where the LLM corrects code as a technical repair task).

**Note on real-world significance:** Handa et al. (2025) identify "Reviewing work" (editing, feedback, improving content) as the second most common usage category at 58.9% of interactions, yet it has no dedicated evaluation framework in the benchmark literature. This represents a critical gap that this project's Phase 3 analysis quantifies.

### Hierarchical Sub-categories

| Sub-category                             | Description                                                             |
| ---------------------------------------- | ----------------------------------------------------------------------- |
| C05a — Proofreading & Copy-editing      | Correcting grammar, spelling, style, and clarity                        |
| C05b — Substantive Document Revision    | Restructuring, improving argument, rewriting sections                   |
| C05c — Academic Peer Review Simulation  | Providing critique in the style of academic peer review                 |
| C05d — Assessment & Grading             | Evaluating work against defined criteria and assigning a score or grade |
| C05e — Interview & Application Feedback | Reviewing CVs, cover letters, interview answers, personal statements    |

### Decision Rule

A task belongs to C05 **if and only if**:

1. The user provides an existing artefact as primary input, **AND**
2. The LLM's primary role is to evaluate, improve, or provide feedback — not to produce an entirely new artefact (→ C01) or perform a technical code repair (→ C02b).

### Resolution of Ambiguous Cases

| Ambiguous case                                  | Resolution | Rationale                          |
| ----------------------------------------------- | ---------- | ---------------------------------- |
| "Edit this email and make it more professional" | → C05b    | User's draft is the starting point |
| "Write me a professional email"                 | → C01     | No existing artefact               |
| "Fix the bug in my code"                        | → C02b    | Technical repair                   |
| "Review my code for best practices"             | → C05     | Evaluative review                  |

### Worked Examples

1. "Proofread, edit, and correct written documents and communications" (rank 18, 1.51%) → C05a
2. "Revise and format academic documents across multiple disciplines" (rank 25, 1.12%) → C05b
3. "Create, grade, and evaluate educational assessments and student work" (rank 54, 0.60%) → C05d
4. "Draft and revise academic application essays and materials" (rank 84, 0.32%) → C05e
5. "Help prepare for job interviews with questions, answers, and practice" (rank 87, 0.31%) → C05e
6. "Respond to peer reviewers and revise manuscripts for journal submission" (rank 101, 0.14%) → C05c
7. "Evaluate arguments and develop debate positions or counterarguments" (rank 104, 0.11%) → C05c
8. O\*NET: "Review and revise documents to ensure accuracy and clarity" → C05b

---

## C06 — Translation & Language Processing

### Formal Definition

Translation & Language Processing refers to LLM interactions in which the primary task is converting written text between natural languages (translation) or supporting the acquisition of a foreign language through vocabulary instruction, grammar explanation, pronunciation guidance, or language exercises. The task is fundamentally linguistic — concerned with cross-linguistic equivalence or language learning — rather than general writing in a language (→ C01) or explaining a non-linguistic subject (→ C04).

### Hierarchical Sub-categories

| Sub-category                                    | Description                                                      |
| ----------------------------------------------- | ---------------------------------------------------------------- |
| C06a — Document Translation                    | Converting documents, texts, or passages between languages       |
| C06b — Real-time or Conversational Translation | Translating short phrases, messages, or communication snippets   |
| C06c — Grammar & Linguistics Instruction       | Explaining grammatical rules, syntax, and linguistic features    |
| C06d — Vocabulary & Phrase Learning            | Building vocabulary, learning expressions, or practising phrases |
| C06e — Localisation & Cultural Adaptation      | Adapting content for a target language audience                  |

### Decision Rule

A task belongs to C06 **if and only if**:

1. The task involves converting text between natural languages OR providing instruction specifically in a foreign language, **AND**
2. The primary user goal is linguistic equivalence, comprehension, or language acquisition — not producing a new document in a language (→ C01).

### Resolution of Ambiguous Cases

| Ambiguous case                | Resolution   | Rationale                            |
| ----------------------------- | ------------ | ------------------------------------ |
| "Translate this report"       | → C06a      | Cross-language conversion            |
| "Write me a report in French" | → C01       | New document; language is incidental |
| "Correct my French grammar"   | → C06c      | Linguistic instruction               |
| "Help me learn Korean"        | → C06d/C06c | Language acquisition                 |

### Worked Examples

1. "Translate text and documents between various languages" (rank 14, 1.83%) → C06a
2. "Assist with multilingual vocabulary, grammar, translation, and pronunciation learning" (rank 35, 0.96%) → C06c/C06d
3. O\*NET: "Translate documents or communications between languages" → C06a
4. O\*NET: "Adapt software and accompanying technical documents to another language and culture" → C06e
5. O\*NET: "Adapt translations to students' cognitive and grade levels" → C06a/C06e

---

## C07 — Data Analysis & Summarisation

### Formal Definition

Data Analysis & Summarisation refers to LLM interactions in which the user provides existing data, documents, or information corpora, and the LLM processes them to extract insights, identify patterns, produce condensed representations, or transform unstructured material into structured form. The key distinguishing feature is that the input is a data artefact (not just a topic or question), and the output is a derived product (analysis, summary, extract, or structured output) rather than a new authored document (→ C01) or a factual answer from model memory (→ C03).

### Hierarchical Sub-categories

| Sub-category                                  | Description                                                                 |
| --------------------------------------------- | --------------------------------------------------------------------------- |
| C07a — Text Summarisation                    | Condensing long documents into shorter representations                      |
| C07b — Quantitative Data Analysis            | Statistical analysis or pattern detection on numerical data                 |
| C07c — Document Information Extraction       | Extracting specific entities or structured data from unstructured documents |
| C07d — Financial & Business Analysis         | Analysing financial statements, market data, business metrics               |
| C07e — Content Transformation & Reformatting | Converting content between formats, restructuring for a new purpose         |

### Decision Rule

A task belongs to C07 **if and only if**:

1. The user provides existing data, documents, or content as input, **AND**
2. The LLM's role is to process, analyse, summarise, extract from, or reformat that material — not to generate new content from scratch (→ C01) or answer factual questions from training knowledge (→ C03).

### Resolution of Ambiguous Cases

| Ambiguous case                             | Resolution | Rationale                                       |
| ------------------------------------------ | ---------- | ----------------------------------------------- |
| "Summarise this report"                    | → C07a    | Existing document as input                      |
| "Write a summary of climate change"        | → C01     | No input document; LLM generates from knowledge |
| "Analyse this spreadsheet"                 | → C07b    | Existing data artefact as input                 |
| "Extract the key findings from this paper" | → C07c    | Information extraction                          |

### Worked Examples

1. "Summarize documents and conversation histories to specified formats" (rank 74, 0.39%) → C07a
2. "Extract and analyze content from images, PDFs, and documents" (rank 27, 1.12%) → C07c
3. "Assist with data analysis, statistical computing, and programming tasks" (rank 46, 0.68%) → C07b
4. "Perform corporate financial analysis and business research" (rank 37, 0.88%) → C07d
5. "Create and format presentation slides, scripts, and speaker notes from source materials" (rank 93, 0.25%) → C07e
6. "Analyze financial markets and summarize cryptocurrency news" (rank 97, 0.22%) → C07a/C07d
7. O\*NET: "Analyse data to identify operational trends and inform decisions" → C07b

---

## C08 — Conversational Interaction & Roleplay

### Formal Definition

Conversational Interaction & Roleplay refers to LLM interactions in which the primary value lies in the conversational experience itself — the sustained, interactive exchange — rather than in a specific artefact, answer, or learned concept as output. This includes interactive fiction, persona-based roleplay, open-ended intellectual dialogue, companionship interactions, and interactive practice scenarios. The LLM is expected to maintain a conversational dynamic over multiple turns.

### Hierarchical Sub-categories

| Sub-category                                | Description                                                                |
| ------------------------------------------- | -------------------------------------------------------------------------- |
| C08a — Interactive Fiction & Roleplay      | Collaborative storytelling, character roleplay, fantasy or narrative games |
| C08b — Open-ended Intellectual Dialogue    | Discussion-based exploration of ideas, philosophy, ethics, speculation     |
| C08c — Interactive Practice Scenarios      | Simulated professional or social situations for skill practice             |
| C08d — Casual Conversation & Companionship | Social chitchat, emotional support, casual interaction                     |

### Decision Rule

A task belongs to C08 **if and only if**:

1. The user's goal is sustained interactive engagement over multiple turns, **AND**
2. The value lies in the conversational experience — not in a specific information product (→ C03), document (→ C01), or educational lesson (→ C04), **AND**
3. The LLM is expected to maintain a persona, narrative thread, or interactive dynamic.

### Resolution of Ambiguous Cases

| Ambiguous case                                             | Resolution | Rationale                          |
| ---------------------------------------------------------- | ---------- | ---------------------------------- |
| "Write me a fantasy story"                                 | → C01c    | Single output requested            |
| "Let's collaboratively build a fantasy story turn by turn" | → C08a    | Multi-turn interactive experience  |
| "Discuss AI ethics with me"                                | → C08b    | Open-ended dialogue                |
| "Explain AI ethics"                                        | → C04     | Structured pedagogical explanation |

### Worked Examples

1. "Facilitate interactive roleplay sessions and initiate basic conversations" (rank 58, 0.54%) → C08a/C08d
2. "Discuss philosophy, mythology, AI ethics, and abstract intellectual topics" (rank 65, 0.47%) → C08b
3. "Generate guidance for speculative and aleatory activities" (rank 75, 0.38%) → C08b
4. Simulated doctor–patient consultations for medical training → C08c
5. AI companion interactions for emotional support → C08d

---

## Axial Category to Core Capability Mapping

| Axial Category                          | Core Capability |
| --------------------------------------- | --------------- |
| Academic task completion                | C01             |
| Professional writing and communication  | C01             |
| Professional document and plan creation | C01             |
| Creative writing                        | C01             |
| Code debugging and repair               | C02             |
| Code development and debugging          | C02             |
| Technical troubleshooting and support   | C02             |
| Domain knowledge retrieval              | C03             |
| Research and synthesis                  | C03             |
| Advice and guidance                     | C03             |
| Teaching and concept explanation        | C04             |
| Mathematical problem solving            | C04             |
| Adaptive instruction                    | C04             |
| Reviewing and editing existing work     | C05             |
| Language translation                    | C06             |
| Language learning and translation       | C06             |
| Data analysis and interpretation        | C07             |
| Document analysis and extraction        | C07             |
| Summarisation and condensation          | C07             |
| Conversational and interactive dialogue | C08             |

---

## References

- Aubakirova, M. et al. (2025). State of AI: An Empirical 100 Trillion Token Study with OpenRouter. OpenRouter / a16z. December 2025.
- Braun, V. and Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), pp. 77–101.
- Chatterji, A. et al. (2025). How People Use ChatGPT. NBER Working Paper No. 34255. September 2025.
- Handa, K. et al. (2025). Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations. arXiv:2503.04761.
- O\*NET OnLine (n.d.). Detailed Work Activities. US Department of Labor.
