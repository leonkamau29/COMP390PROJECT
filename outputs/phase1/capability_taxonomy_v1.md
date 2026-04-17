# LLM Capability Taxonomy — Version 1

**Project:** Benchmark Coverage Gap: A Systematic Analysis of Real-World AI Capabilities and Evaluation Practices
**Student:** Leon Kamau Kiunga (201759400)
**Supervisor:** Dr Konstantinos Tsakaldis
**Phase:** Phase 1 — Capability Framework Development
**Version:** 1.0 (draft — for Week 3 validation)

**Method:** Braun & Clarke (2006) six-phase thematic analysis
**Primary source:** Handa et al. (2025) Anthropic Economic Index (arXiv:2503.04761); O\*NET Detailed Work Activities

---

## Overview

This taxonomy defines **8 core capabilities** representing distinct modes of LLM interaction, derived through thematic analysis of 123 empirically documented task instances from real-world LLM usage data (Handa et al., 2025) and occupational task databases (O\*NET). The taxonomy is designed to cover ≥95% of documented usage patterns and to serve as the analytical framework for Phase 3 coverage analysis.

The 8 capabilities are:

| ID  | Name                                         | Description (one line)                                                     |
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

| Sub-category                            | Description                                                                  | Example tasks                                                                     |
| --------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| C01a — Academic Writing                | Essays, reports, assignments, theses for educational contexts                | "Write an essay on the French Revolution"; "Complete my STEM assignment"          |
| C01b — Professional & Business Writing | Emails, business plans, reports, proposals, marketing copy                   | "Draft a business plan"; "Write a marketing email campaign"                       |
| C01c — Creative Writing                | Fiction, poetry, scripts, song lyrics, creative narratives                   | "Write a short story in the style of Hemingway"; "Draft a video game script"      |
| C01d — Technical Documentation         | API docs, system architecture write-ups, user manuals, README files          | "Write API documentation for this endpoint"; "Create a technical design document" |
| C01e — Personal & Social Writing       | Personal letters, social media posts, relationship messages, religious texts | "Write a condolence message"; "Draft social media posts for my brand"             |
| C01f — Legal & Formal Documents        | Contracts, legal briefs, formal correspondence, dispute letters              | "Draft a cease-and-desist letter"; "Write a service agreement"                    |

### Decision Rule

A task belongs to C01 **if and only if**:

1. The user's primary goal is to obtain a new written artefact (not an improved version of existing work → C05, not a factual answer → C03, not code → C02), **AND**
2. The LLM's contribution is authoring that artefact from scratch or from minimal user-provided material.

### Resolution of Ambiguous Cases

| Ambiguous case                                                        | Resolution       | Rationale                                                           |
| --------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------- |
| User provides a rough outline and asks LLM to write the full document | → C01           | Outline is scaffolding; LLM authors the artefact                    |
| User provides a full draft and asks for improvements                  | → C05           | Existing artefact is primary input; LLM role is evaluative          |
| User asks LLM to "write and then edit" a document                     | → C01 (primary) | Production goal is the first-order task                             |
| Summarising a document for a slide deck                               | → C07           | Condensation of existing material                                   |
| Writing an essay about a topic from memory                            | → C01           | Output is a new document, even though research knowledge is applied |

### Worked Examples (from empirical task instances)

1. **"Complete academic assignments and create educational materials across all subjects"** (Handa et al., 2025, rank 1, 4.98% usage) — The user wants a new written submission produced; → C01a.
2. **"Write, develop, and edit original creative fiction across multiple genres"** (Handa et al., 2025, rank 7, 2.90% usage) — Production of new narrative content; → C01c.
3. **"Draft and revise professional workplace correspondence and business communications"** (Handa et al., 2025, rank 9, 2.44% usage) — New professional writing artefact; → C01b.
4. **"Create and optimize marketing content across multiple formats and industries"** (Handa et al., 2025, rank 10, 2.38% usage) — New marketing copy; → C01b.
5. **"Create technical documentation, diagrams, and architectural designs"** (Handa et al., 2025, rank 17, 1.58% usage) — Technical documentation; → C01d.
6. **"Draft, review, and analyze legal documents and court filings"** (Handa et al., 2025, rank 30, 1.09% usage) — Legal document creation (primary); → C01f.
7. **"Assist with business planning, strategy, and entrepreneurial development"** (Handa et al., 2025, rank 6, 3.00% usage) — Business plan as a new document; → C01b.

---

## C02 — Code Development & Technical Problem Solving

### Formal Definition

Code Development & Technical Problem Solving refers to LLM interactions in which the output is executable code, a configuration, a technical specification, or a systematic procedure for resolving a software, hardware, or infrastructure problem. The LLM applies knowledge of programming languages, systems architecture, protocols, and technical tools to produce or repair functional technical artefacts or resolve technical failures.

### Hierarchical Sub-categories

| Sub-category                              | Description                                                     | Example tasks                                                                        |
| ----------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| C02a — Code Generation                   | Writing new functions, modules, scripts, or applications        | "Build a web scraper in Python"; "Create a REST API in Node.js"                      |
| C02b — Debugging & Bug Fixing            | Identifying and correcting errors in existing code              | "Debug this Python function"; "Fix the CSS layout bug"                               |
| C02c — Code Review & Refactoring         | Improving code quality, readability, and efficiency             | "Refactor this function to be more efficient"; "Review this code for best practices" |
| C02d — Infrastructure & DevOps           | Configuring servers, CI/CD pipelines, Docker, cloud, networking | "Set up a CI/CD pipeline"; "Configure an nginx server"                               |
| C02e — Database & Data Engineering       | Writing SQL, designing schemas, managing data pipelines         | "Write a SQL query to find duplicate records"; "Design a database schema"            |
| C02f — Specialised Technical Development | ML/AI systems, embedded systems, game dev, security, blockchain | "Implement a neural network in PyTorch"; "Debug embedded firmware"                   |

### Decision Rule

A task belongs to C02 **if and only if**:

1. The primary output is code, a configuration, a technical specification, or a systematic technical procedure, **AND**
2. The task requires applied knowledge of programming, systems, or technical infrastructure.

### Resolution of Ambiguous Cases

| Ambiguous case                            | Resolution     | Rationale                                                               |
| ----------------------------------------- | -------------- | ----------------------------------------------------------------------- |
| "Explain what this code does"             | → C04         | Explanation without producing code is educational                       |
| "Fix the bug in my code"                  | → C02b        | Output is corrected code                                                |
| "Review my code and suggest improvements" | → C02c or C05 | If output is revised code → C02c; if output is written critique → C05 |
| "What is an API?"                         | → C04         | Conceptual question, no code output                                     |
| "Write a machine learning model"          | → C02f        | Code output despite ML knowledge domain                                 |
| "Troubleshoot my WiFi connection"         | → C02d        | Technical procedure to resolve infrastructure failure                   |

### Worked Examples (from empirical task instances)

1. **"Debug, fix, and refactor code across programming languages and development tasks"** (Handa et al., 2025, rank 2, 4.53% usage) — Code repair and improvement; → C02b/C02c.
2. **"Build, debug, and customize web applications and websites"** (Handa et al., 2025, rank 4, 3.57% usage) — Web application development; → C02a.
3. **"Debug and fix CSS, HTML, and UI layout and styling issues"** (Handa et al., 2025, rank 8, 2.63% usage) — Front-end bug fixing; → C02b.
4. **"Help with machine learning, AI development, and technical implementation"** (Handa et al., 2025, rank 20, 1.35% usage) — ML code development; → C02f.
5. **"Help with SQL queries, database design, and optimization"** (Handa et al., 2025, rank 38, 0.87% usage) — Database query writing; → C02e.
6. **"Troubleshoot and configure Docker, Kubernetes, and virtualization platforms"** (Handa et al., 2025, rank 55, 0.57% usage) — Infrastructure configuration; → C02d.
7. **"Configure and troubleshoot development infrastructure, CI/CD, and deployment systems"** (Handa et al., 2025, rank 68, 0.45% usage) — DevOps configuration; → C02d.

---

## C03 — Information Retrieval & Advisory

### Formal Definition

Information Retrieval & Advisory refers to LLM interactions in which the user seeks to obtain factual information, domain-specific knowledge, recommendations, or guidance from the LLM. The LLM acts as a knowledgeable informant, synthesising and applying its training knowledge to answer questions, compare options, or support a decision. The primary output is a response containing information or a recommendation — not a new document (→ C01), executable code (→ C02), or structured pedagogy (→ C04).

### Hierarchical Sub-categories

| Sub-category                             | Description                                                                  | Example tasks                                                                                           |
| ---------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| C03a — Factual Question Answering       | Answering specific factual queries from domain knowledge                     | "What causes Type 2 diabetes?"; "What are the immigration requirements for Canada?"                     |
| C03b — Research & Literature Synthesis  | Synthesising information across sources; summarising a field                 | "What does the literature say about transformer efficiency?"; "Survey recent work on LLM hallucination" |
| C03c — Product & Service Recommendation | Comparing and recommending products, tools, or services                      | "Which laptop should I buy for machine learning?"; "Compare these two cloud providers"                  |
| C03d — Personal & Professional Advisory | Career, finance, health, relationship, and life-skills guidance              | "How should I negotiate my salary?"; "What exercises help with lower back pain?"                        |
| C03e — Domain Expert Consultation       | Advice requiring specialised professional knowledge (law, medicine, finance) | "What are the legal implications of this contract clause?"; "Is this medication safe with metformin?"   |

### Decision Rule

A task belongs to C03 **if and only if**:

1. The user's primary goal is to obtain information, recommendations, or decision support, **AND**
2. The output is an answer, explanation, or recommendation — not a new content artefact (→ C01), code (→ C02), or a pedagogically structured lesson (→ C04).

### Resolution of Ambiguous Cases

| Ambiguous case                                    | Resolution | Rationale                                       |
| ------------------------------------------------- | ---------- | ----------------------------------------------- |
| "What is the capital of France?"                  | → C03a    | Simple factual retrieval                        |
| "Teach me about the French Revolution"            | → C04     | Pedagogical orientation, structured explanation |
| "Write a report on the French Revolution"         | → C01     | New document as output                          |
| "What medication is prescribed for ADHD?"         | → C03e    | Domain knowledge answer                         |
| "Write a prescription letter for ADHD medication" | → C01     | New document                                    |
| "Help me choose between Python and R"             | → C03c    | Recommendation and comparison                   |

### Worked Examples (from empirical task instances)

1. **"Help research, compare, and select consumer products for purchasing decisions"** (Handa et al., 2025, rank 5, 3.10% usage) — Product comparison and recommendation; → C03c.
2. **"Provide medical and health-related information across multiple specialties"** (Handa et al., 2025, rank 24, 1.24% usage) — Medical factual information; → C03e.
3. **"Provide relationship, dating, parenting, and family advice"** (Handa et al., 2025, rank 40, 0.85% usage) — Personal advisory; → C03d.
4. **"Provide personal finance guidance and perform financial calculations"** (Handa et al., 2025, rank 44, 0.71% usage) — Financial advisory; → C03d.
5. **"Assist with multidisciplinary scientific research and academic projects"** (Handa et al., 2025, rank 34, 0.96% usage) — Research synthesis; → C03b.
6. **"Find local information about places, services, restaurants, and cultural topics"** (Handa et al., 2025, rank 60, 0.53% usage) — Factual local information; → C03a.
7. **"Provide general information regarding investment and portfolio management"** (Handa et al., 2025, rank 72, 0.43% usage) — Financial domain advisory; → C03e.

---

## C04 — Learning & Education Support

### Formal Definition

Learning & Education Support refers to LLM interactions in which the LLM acts as a tutor, instructor, or mentor, structuring knowledge to facilitate the user's comprehension of a concept, skill, or procedure. The defining feature distinguishing C04 from C03 is pedagogical intent: the LLM scaffolds understanding (explains why, demonstrates how, provides worked examples, checks understanding) rather than simply delivering a factual answer. The user's goal is to develop capability, not merely obtain information.

### Hierarchical Sub-categories

| Sub-category                   | Description                                                       | Example tasks                                                                              |
| ------------------------------ | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| C04a — Concept Explanation    | Explaining ideas, theories, or mechanisms at an appropriate level | "Explain gradient descent to a beginner"; "What is the difference between RAM and ROM?"    |
| C04b — Worked Problem Solving | Walking through problems step-by-step (maths, science, logic)     | "Solve this integral and explain each step"; "Walk me through this physics problem"        |
| C04c — Skill Instruction      | Teaching a skill progressively (programming, language, writing)   | "Teach me Python from scratch"; "How do I structure an argument in an essay?"              |
| C04d — Adaptive Tutoring      | Diagnosing misunderstanding and adjusting instruction level       | "I don't understand your explanation — can you use an analogy?"; "Explain it more simply" |

### Decision Rule

A task belongs to C04 **if and only if**:

1. The user's explicit or implicit goal is to develop understanding or competence, **AND**
2. The LLM's response is structured pedagogically (explains, demonstrates, scaffolds), not merely factual, **AND**
3. The interaction is oriented toward building user capability rather than completing a task on the user's behalf.

### Resolution of Ambiguous Cases

| Ambiguous case                          | Resolution    | Rationale                                                                                       |
| --------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------- |
| "What is machine learning?"             | → C03 or C04 | If a single factual sentence suffices → C03; if the user wants a structured explanation → C04 |
| "Explain recursion step by step"        | → C04b       | Explicit pedagogical structure requested                                                        |
| "Write recursive code for me"           | → C02a       | Task completion, not instruction                                                                |
| "Help me understand this maths problem" | → C04b       | Understanding is the goal                                                                       |
| "Solve this maths problem for me"       | → C01 or C04 | If answer only → C01/C03; if worked explanation → C04b                                        |

### Worked Examples (from empirical task instances)

1. **"Help me learn programming languages and software development concepts"** (Handa et al., 2025, rank 15, 1.80% usage) — Skill instruction in programming; → C04c.
2. **"Help solve mathematics problems from basic arithmetic to advanced university-level topics"** (Handa et al., 2025, rank 22, 1.32% usage) — Worked mathematical problem solving; → C04b.
3. **"Help with algorithms, data structures, and competitive programming tasks"** (Handa et al., 2025, rank 50, 0.63% usage) — CS concept instruction; → C04a/C04c.
4. **"Help with physics problems, coursework, and educational explanations"** (Handa et al., 2025, rank 79, 0.36% usage) — Physics concept explanation; → C04a/C04b.
5. **"Solve engineering physics problems and debug simulation code"** (Handa et al., 2025, rank 67, 0.46% usage) — Problem-solving with explanation; → C04b.
6. **"Assist with quantum mechanics and quantum computing topics"** (Handa et al., 2025, rank 109, 0.06% usage) — Specialist concept instruction; → C04a.
7. **O\*NET: "Adapt instructional content or delivery methods for different levels or types of learners"** (O\*NET, 0.134%) — Adaptive tutoring; → C04d.

---

## C05 — Review & Feedback

### Formal Definition

Review & Feedback refers to LLM interactions in which the user submits an existing artefact — a written document, code, argument, or piece of work — and the LLM evaluates, critiques, annotates, or produces an improved version. The primary input is the user's artefact; the primary output is an assessment, edited version, or structured critique. This capability is distinguished from C01 (where the LLM authors from scratch) and C02 (where the LLM corrects code as a technical repair task).

### Hierarchical Sub-categories

| Sub-category                             | Description                                                              | Example tasks                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| C05a — Proofreading & Copy-editing      | Correcting grammar, spelling, style, and clarity                         | "Proofread this email"; "Fix the grammar in this paragraph"                     |
| C05b — Substantive Document Revision    | Restructuring, improving argument, rewriting sections                    | "Improve the structure of this essay"; "Rewrite this section more concisely"    |
| C05c — Academic Peer Review Simulation  | Providing critique in the style of academic peer review                  | "Review this abstract as if you were a journal reviewer"                        |
| C05d — Assessment & Grading             | Evaluating work against defined criteria and assigning a score or grade  | "Grade this essay on a scale of 1–10 with justification"                       |
| C05e — Interview & Application Feedback | Reviewing CVs, cover letters, interview answers, and personal statements | "Review my CV and suggest improvements"; "Give feedback on my interview answer" |

### Decision Rule

A task belongs to C05 **if and only if**:

1. The user provides an existing artefact as primary input, **AND**
2. The LLM's primary role is to evaluate, improve, or provide feedback — not to produce an entirely new artefact (→ C01) or perform a technical code repair (→ C02b).

### Resolution of Ambiguous Cases

| Ambiguous case                                    | Resolution       | Rationale                                      |
| ------------------------------------------------- | ---------------- | ---------------------------------------------- |
| "Edit this email and make it more professional"   | → C05b          | User's draft is the starting point             |
| "Write me a professional email"                   | → C01           | No existing artefact; LLM authors from scratch |
| "Fix the bug in my code"                          | → C02b          | Technical repair, not quality feedback         |
| "Review my code for best practices"               | → C05 (or C02c) | Evaluative review of existing code             |
| "Respond to peer reviewers and revise manuscript" | → C05c          | Revision driven by existing reviewer comments  |
| "Grade this student essay and explain the grade"  | → C05d          | Assessment of submitted work                   |

### Worked Examples (from empirical task instances)

1. **"Proofread, edit, and correct written documents and communications"** (Handa et al., 2025, rank 18, 1.51% usage) — Copy-editing existing text; → C05a.
2. **"Revise and format academic documents across multiple disciplines"** (Handa et al., 2025, rank 25, 1.12% usage) — Document revision; → C05b.
3. **"Create, grade, and evaluate educational assessments and student work"** (Handa et al., 2025, rank 54, 0.60% usage) — Assessment and grading; → C05d.
4. **"Draft and revise academic application essays and materials"** (Handa et al., 2025, rank 84, 0.32% usage) — Application feedback; → C05e.
5. **"Help prepare for job interviews with questions, answers, and practice"** (Handa et al., 2025, rank 87, 0.31% usage) — Interview answer feedback; → C05e.
6. **"Respond to peer reviewers and revise manuscripts for journal submission"** (Handa et al., 2025, rank 101, 0.14% usage) — Academic peer review; → C05c.
7. **"Evaluate arguments and develop debate positions or counterarguments"** (Handa et al., 2025, rank 104, 0.11% usage) — Evaluating an existing argument; → C05c.
8. **O\*NET: "Review and revise documents to ensure accuracy and clarity"** (O\*NET) — Document revision in professional context; → C05b.

---

## C06 — Translation & Language Processing

### Formal Definition

Translation & Language Processing refers to LLM interactions in which the primary task is converting written text between natural languages (translation) or supporting the acquisition of a foreign language through vocabulary instruction, grammar explanation, pronunciation guidance, or language exercises. The task is fundamentally linguistic — concerned with cross-linguistic equivalence or language learning — rather than general writing in a language (→ C01) or explaining a non-linguistic subject (→ C04).

### Hierarchical Sub-categories

| Sub-category                                    | Description                                                                 | Example tasks                                                                  |
| ----------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| C06a — Document Translation                    | Converting documents, texts, or passages between languages                  | "Translate this contract from Spanish to English"                              |
| C06b — Real-time or Conversational Translation | Translating short phrases, messages, or communication snippets              | "How do I say 'I need a doctor' in Japanese?"                                  |
| C06c — Grammar & Linguistics Instruction       | Explaining grammatical rules, syntax, and linguistic features of a language | "Explain the subjunctive mood in French"                                       |
| C06d — Vocabulary & Phrase Learning            | Building vocabulary, learning expressions, or practising phrases            | "Give me 20 common French business phrases"; "What does 'schadenfreude' mean?" |
| C06e — Localisation & Cultural Adaptation      | Adapting content for a target language audience, including cultural nuance  | "Adapt this marketing copy for a Japanese audience"                            |

### Decision Rule

A task belongs to C06 **if and only if**:

1. The task involves converting text between natural languages OR providing instruction specifically in a foreign language, **AND**
2. The primary user goal is linguistic equivalence, comprehension, or language acquisition — not producing a new document in a language (→ C01).

### Resolution of Ambiguous Cases

| Ambiguous case                   | Resolution   | Rationale                                         |
| -------------------------------- | ------------ | ------------------------------------------------- |
| "Translate this report"          | → C06a      | Cross-language conversion is the goal             |
| "Write me a report in French"    | → C01       | New document production; language is incidental   |
| "Correct my French grammar"      | → C06c      | Linguistic instruction/feedback                   |
| "Proofread this French document" | → C05a      | Quality review of existing text (not translation) |
| "Help me learn Korean"           | → C06d/C06c | Language acquisition                              |
| "What does 'Zeitgeist' mean?"    | → C06d      | Vocabulary/linguistic explanation                 |

### Worked Examples (from empirical task instances)

1. **"Translate text and documents between various languages"** (Handa et al., 2025, rank 14, 1.83% usage) — Document translation; → C06a.
2. **"Assist with multilingual vocabulary, grammar, translation, and pronunciation learning"** (Handa et al., 2025, rank 35, 0.96% usage) — Language learning support; → C06c/C06d.
3. **O\*NET: "Translate documents or communications between languages"** (O\*NET) — Occupational translation task; → C06a.
4. **O\*NET: "Adapt software and accompanying technical documents to another language and culture"** (O\*NET) — Technical localisation; → C06e.
5. **O\*NET: "Adapt translations to students' cognitive and grade levels"** (O\*NET) — Pedagogically-adapted translation; → C06a/C06e.

---

## C07 — Data Analysis & Summarisation

### Formal Definition

Data Analysis & Summarisation refers to LLM interactions in which the user provides existing data, documents, or information corpora, and the LLM processes them to extract insights, identify patterns, produce condensed representations, or transform unstructured material into structured form. The key distinguishing feature is that the input is a data artefact (not just a topic or question), and the output is a derived product (analysis, summary, extract, or structured output) rather than a new authored document (→ C01) or a factual answer from model memory (→ C03).

### Hierarchical Sub-categories

| Sub-category                                  | Description                                                                           | Example tasks                                                                                   |
| --------------------------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| C07a — Text Summarisation                    | Condensing long documents into shorter representations                                | "Summarise this 50-page report in 5 bullet points"                                              |
| C07b — Quantitative Data Analysis            | Performing calculations, statistical analysis, or pattern detection on numerical data | "Analyse this sales dataset and identify trends"                                                |
| C07c — Document Information Extraction       | Extracting specific entities, facts, or structured data from unstructured documents   | "Extract all dates and named parties from this contract"                                        |
| C07d — Financial & Business Analysis         | Analysing financial statements, market data, and business metrics                     | "Analyse this income statement and identify risks"                                              |
| C07e — Content Transformation & Reformatting | Converting content between formats, restructuring for a new purpose                   | "Convert this Word document to a structured JSON"; "Turn these meeting notes into action items" |

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
| "What are trends in AI investment?"        | → C03b    | Knowledge-based answer, no data artefact        |
| "Convert these meeting notes into a table" | → C07e    | Reformatting existing content                   |
| "Extract the key findings from this paper" | → C07c    | Information extraction from existing document   |

### Worked Examples (from empirical task instances)

1. **"Summarize documents and conversation histories to specified formats"** (Handa et al., 2025, rank 74, 0.39% usage) — Text summarisation; → C07a.
2. **"Extract and analyze content from images, PDFs, and documents"** (Handa et al., 2025, rank 27, 1.12% usage) — Document extraction; → C07c.
3. **"Assist with data analysis, statistical computing, and programming tasks"** (Handa et al., 2025, rank 46, 0.68% usage) — Quantitative analysis; → C07b.
4. **"Perform corporate financial analysis and business research"** (Handa et al., 2025, rank 37, 0.88% usage) — Financial analysis; → C07d.
5. **"Create and format presentation slides, scripts, and speaker notes from source materials"** (Handa et al., 2025, rank 93, 0.25% usage) — Content transformation; → C07e.
6. **"Analyze financial markets and summarize cryptocurrency news"** (Handa et al., 2025, rank 97, 0.22% usage) — Financial summarisation; → C07a/C07d.
7. **O\*NET: "Analyse data to identify operational trends and inform decisions"** (O\*NET) — Occupational data analysis; → C07b.

---

## C08 — Conversational Interaction & Roleplay

### Formal Definition

Conversational Interaction & Roleplay refers to LLM interactions in which the primary value lies in the conversational experience itself — the sustained, interactive exchange — rather than in a specific artefact, answer, or learned concept as output. This includes interactive fiction, persona-based roleplay, open-ended intellectual dialogue, companionship interactions, and interactive practice scenarios. The LLM is expected to maintain a conversational dynamic over multiple turns, responding coherently to the unfolding interaction rather than delivering a single output.

### Hierarchical Sub-categories

| Sub-category                                | Description                                                                | Example tasks                                                                                   |
| ------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| C08a — Interactive Fiction & Roleplay      | Collaborative storytelling, character roleplay, fantasy or narrative games | "Let's play a D\&D campaign"; "Roleplay as a historical figure"                                 |
| C08b — Open-ended Intellectual Dialogue    | Discussion-based exploration of ideas, philosophy, ethics, speculation     | "Debate the ethics of AI consciousness with me"; "Discuss whether free will exists"             |
| C08c — Interactive Practice Scenarios      | Simulated professional or social situations for skill practice             | "Act as a difficult client and let me practise handling objections"; "Simulate a job interview" |
| C08d — Casual Conversation & Companionship | Social chitchat, emotional support, casual interaction                     | "Just talk to me"; "I'm feeling anxious — can we chat?"                                        |

### Decision Rule

A task belongs to C08 **if and only if**:

1. The user's goal is sustained interactive engagement over multiple turns, **AND**
2. The value of the interaction lies in the conversational experience — not in a specific information product (→ C03), document (→ C01), or educational lesson (→ C04), **AND**
3. The LLM is expected to maintain a persona, narrative thread, or interactive dynamic.

### Resolution of Ambiguous Cases

| Ambiguous case                                             | Resolution | Rationale                                         |
| ---------------------------------------------------------- | ---------- | ------------------------------------------------- |
| "Write me a fantasy story"                                 | → C01c    | Single output requested                           |
| "Let's collaboratively build a fantasy story turn by turn" | → C08a    | Multi-turn interactive experience                 |
| "Discuss AI ethics with me"                                | → C08b    | Open-ended dialogue, no specific output requested |
| "Explain AI ethics"                                        | → C04     | Structured pedagogical explanation                |
| "Simulate a job interview"                                 | → C08c    | Interactive scenario practice                     |
| "Help me prepare for interviews" (without simulation)      | → C05e    | Feedback on existing answers                      |

### Worked Examples (from empirical task instances)

1. **"Facilitate interactive roleplay sessions and initiate basic conversations"** (Handa et al., 2025, rank 58, 0.54% usage) — Roleplay and conversational interaction; → C08a/C08d.
2. **"Discuss philosophy, mythology, AI ethics, and abstract intellectual topics"** (Handa et al., 2025, rank 65, 0.47% usage) — Intellectual dialogue; → C08b.
3. **"Generate guidance for speculative and aleatory activities"** (Handa et al., 2025, rank 75, 0.38% usage) — Speculative interactive engagement; → C08b.
4. Simulated doctor–patient consultations for medical training — → C08c.
5. AI companion interactions for emotional support — → C08d.

---

## Taxonomy Validation Summary (Week 3 target)

| Metric                               | Target           | Status                    |
| ------------------------------------ | ---------------- | ------------------------- |
| Coverage of Anthropic top 100 tasks  | ≥95%            | Pending Week 3 validation |
| Cohen's κ (inter-coder reliability) | >0.8             | Pending Week 3 validation |
| Number of core capabilities          | 6–10            | 8 ✓                      |
| Worked examples per capability       | ≥5              | 5–8 per capability ✓    |
| Decision rules documented            | All capabilities | ✓                        |
| Edge cases resolved                  | All capabilities | ✓                        |

---

## Mapping of Axial Categories to Core Capabilities

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

- Braun, V. and Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), pp. 77–101.
- Handa, K. et al. (2025). Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations. arXiv:2503.04761.
- O\*NET OnLine (n.d.). Detailed Work Activities. US Department of Labor.

---
