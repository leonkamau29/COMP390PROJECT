# Capability Definitions Draft — Phase 1 Week 2

**Researcher:** Leon Kamau Kiunga (201759400)
**Date:** 2026-05-13
**Dataset:** Anthropic AEI Feb 2026 + OpenAI NBER WP 34255 + OpenRouter 100T Token Study
**Total task instances coded:** 131
**Methodology:** Braun & Clarke (2006) six-phase thematic analysis

---

## Phase 2: Open Coding

Each of the 131 task instances was assigned a short, descriptive, researcher-generated label
(open_code) describing the core user action. Open codes appear in
`data/phase1/task_instances_coded.csv` under the `open_code` column. Examples:

- "help complete academic homework and coursework"
- "fix technical hardware and software problems"
- "build and fix websites and web apps"
- "write professional emails and business communications"
- "proofread and edit written documents"
- "give medical and health information"
- "translate text between different languages"
- "have casual conversational or social exchanges"

Open codes were kept close to the language of the task description, using the
researcher's own words, short phrases, and active-verb constructions. No
theoretical framing was applied at this stage.

---

## Phase 3: Axial Coding

Open codes were grouped into 19 intermediate axial categories based on shared
purpose, domain, and the type of output the user is requesting. Axial categories
appear in `data/phase1/task_instances_coded.csv` under the `axial_category` column.

The 19 axial categories and their approximate task-instance counts are:

| # | Axial Category | Count |
|---|---------------|-------|
| 1 | Software engineering and application development | 35 |
| 2 | Information retrieval and factual advisory | 26 |
| 3 | Professional writing and business communication | 16 |
| 4 | Data analysis and summarisation | 12 |
| 5 | Technical troubleshooting and IT support | 10 |
| 6 | Code debugging and refactoring | 8 |
| 7 | Conversational interaction and personal advisory | 8 |
| 8 | Learning and education support | 7 |
| 9 | Creative writing and narrative generation | 7 |
| 10 | Review and feedback on written work | 6 |
| 11 | Academic assignment support | 6 |
| 12 | Creative and multimedia content production | 4 |
| 13 | Translation and language processing | 4 |
| 14 | Marketing and promotional content creation | 2 |
| 15 | Web application development | 1 |
| 16 | Academic writing and research support | 1 |
| 17 | Clinical and healthcare documentation | 1 |
| 18 | Legal document drafting | 1 |
| 19 | Agentic and multi-step task execution | 1 |

During axial coding it became clear that categories 1, 3, 5, 8, 15, 18, and 19
all relate to technical software work or could logically consolidate. Similarly,
categories 3, 9, 12, 14, 17, and 18 all involve producing new written or
creative content. Categories 6, 11, and 16 all involve supporting learning.
This informed the selective coding collapse below.

---

## Phase 4: Selective Coding — 8 Core Capabilities

The 19 axial categories were collapsed into 8 core capabilities. The collapse
logic is documented below for each resulting capability.

---

### C01 — Content Generation

**Axial categories collapsed:**
Professional writing and business communication (16) +
Creative writing and narrative generation (7) +
Creative and multimedia content production (4) +
Marketing and promotional content creation (2) +
Clinical and healthcare documentation (1) +
Legal document drafting (1) = **31 instances**

**Collapse rationale:** All of these categories involve a user requesting the
model to produce a new text artefact where none existed before, or to
substantially transform a provided input into a new form. The key unifying
feature is originative text production: the model's primary role is author
or co-author. This distinguishes C01 from C05 (where the user's text already
exists and the model critiques it) and from C07 (where the primary output
is structured data or a summary rather than a composed text).

**Formal definition:** Content Generation is the capability to produce original,
purposeful written or multimedia text artefacts in response to a user's
creative, professional, or communicative goal. The model acts as an author
or co-author, generating content that serves the user's intended audience
and context. This encompasses professional business documents, creative fiction,
marketing copy, scripts, personal communications, technical documentation,
and other forms where the primary output is a composed artefact.

**Decision rule:** A task belongs to C01 if and only if (a) the primary user
goal is to obtain a new written or multimedia artefact, AND (b) the model
is the primary producer of that artefact's content (not merely locating
existing information or critiquing a user's existing text).

**Edge cases:**
- Writing an email from scratch → C01. Editing an email the user already drafted → C05.
- Generating a summary of a document → C07 (the goal is extraction/compression,
  not creative authorship). Writing a narrative essay → C01.
- Translating a document → C06 (cross-lingual conversion, not original authorship).
  Writing a bilingual document from scratch → C01.

**Sub-categories:**
- C01a: Academic and educational writing (essays, assignments, reports)
- C01b: Professional and business writing (emails, strategies, documentation)
- C01c: Marketing and promotional writing (ads, social media, SEO)
- C01d: Creative writing (fiction, poetry, scripts, personal messages)
- C01e: Technical and specialised writing (clinical notes, legal drafts, specs)

---

### C02 — Code Development and Technical Problem Solving

**Axial categories collapsed:**
Software engineering and application development (35) +
Code debugging and refactoring (8) +
Technical troubleshooting and IT support (10) +
Web application development (1) +
Agentic and multi-step task execution (1) = **55 instances**

**Collapse rationale:** All of these categories involve the model working with
technical systems, code, or computational infrastructure. The unifying feature
is that the primary output is either executable code, system configurations,
or technical guidance on making systems behave correctly. Technical
troubleshooting was included here rather than in C03 because it produces
actionable technical outputs (commands, configurations, fixes) rather than
simply providing information about a topic.

**Formal definition:** Code Development and Technical Problem Solving is the
capability to write, debug, refactor, and maintain software code; to design
and implement technical systems; and to diagnose and resolve technical failures
in software, hardware, and networked infrastructure. The model acts as a
technical collaborator, producing or modifying executable artefacts and
providing concrete technical solutions.

**Decision rule:** A task belongs to C02 if and only if the primary output is
(a) executable code, a configuration file, or a technical command, OR
(b) a diagnosis and fix for a technical system failure where the resolution
involves modifying a technical artefact.

**Edge cases:**
- "Explain how recursion works" → C04 (conceptual understanding).
  "Write a recursive function to traverse a tree" → C02.
- "Tell me what DevOps tools exist" → C03 (information retrieval).
  "Help me set up a CI/CD pipeline with GitHub Actions" → C02.
- "Troubleshoot why my WiFi drops" where the answer is a config change → C02.
  "Explain why WiFi channels overlap" → C04.

**Sub-categories:**
- C02a: Web application development (frontend, backend, full-stack)
- C02b: Software engineering and systems (business apps, mobile, databases)
- C02c: Code debugging and refactoring (fixing, improving existing code)
- C02d: Machine learning and AI development (ML models, AI systems)
- C02e: DevOps and infrastructure (deployment, CI/CD, server config)
- C02f: Technical troubleshooting (hardware, network, system failures)

---

### C03 — Information Retrieval and Advisory

**Axial categories collapsed:**
Information retrieval and factual advisory (26) = **26 instances**
(plus cross-source instances from OpenAI Seeking Information 24.4%
and OpenRouter General Q&A)

**Collapse rationale:** This category remained stable through axial coding.
It encompasses all tasks where the user's primary goal is to obtain factual
information, recommendations, or advisory guidance — where the model acts
as a knowledgeable source rather than a producer of original content or
a teacher building understanding.

**Formal definition:** Information Retrieval and Advisory is the capability
to locate, synthesise, and deliver factual information, evidence-based
recommendations, or domain-specific advisory guidance in response to a
user's question or decision-making need. The model acts as an informed
respondent, drawing on its knowledge base to answer questions, compare
options, or advise on decisions.

**Decision rule:** A task belongs to C03 if and only if (a) the user is
seeking factual information or advice to inform a decision or satisfy
curiosity, AND (b) the primary output is informational text rather than a
composed artefact (C01), a technical system output (C02), or a
pedagogical explanation building toward understanding (C04).

**Edge cases:**
- "What are the symptoms of diabetes?" → C03 (factual retrieval).
  "Explain how the immune system responds to infection in a way a student
  can understand" → C04 (educational framing).
- "Give me career advice for moving from law to tech" → C03 (advisory).
  "Help me write a career change cover letter" → C01 (authoring).
- "What is the best Python library for data visualisation?" → C03.
  "Show me how to use matplotlib to plot a histogram" → C04.

**Sub-categories:**
- C03a: Factual and encyclopaedic information (science, medicine, history)
- C03b: Product and service recommendations
- C03c: Career, financial, and personal advisory
- C03d: Research synthesis and literature overview
- C03e: Practical how-to guidance (recipes, home maintenance, travel)

---

### C04 — Learning and Education Support

**Axial categories collapsed:**
Academic assignment support (6) +
Learning and education support (7) +
Academic writing and research support (1) = **14 instances**
(plus OpenAI tutoring 10.2% subcategory)

**Collapse rationale:** These axial categories all involve the model supporting
the user's acquisition of knowledge or skills, or helping a user complete
a learning-oriented task. The distinguishing feature from C03 is pedagogical
intent: the model's role is to build the user's understanding, not merely
to answer a question.

**Formal definition:** Learning and Education Support is the capability to
assist users in acquiring knowledge, skills, or academic qualifications
through tutoring, explanation, worked examples, and structured guidance.
This includes helping learners understand concepts, complete assignments,
solve problems as learning exercises, and develop academic competencies.
The model acts as tutor, teacher, or study partner.

**Decision rule:** A task belongs to C04 if and only if the user's primary
goal is to learn, understand, or develop a skill (rather than simply
obtain an answer), OR the task is framed as an educational or academic
obligation (e.g., coursework, homework, exam preparation).

**Edge cases:**
- "Solve this integral for me" with no learning intent → C07 or C03.
  "Explain how to solve this integral step-by-step so I understand" → C04.
- "Complete my essay for me" → C01 (the goal is the artefact, not learning).
  "Help me understand how to structure an argument essay" → C04.
- "Grade these student essays and explain the criteria" → C05 (grading
  and feedback is review, not tutoring).

**Sub-categories:**
- C04a: Academic assignment support (coursework, homework, exams)
- C04b: Concept explanation and tutoring (STEM, humanities, languages)
- C04c: Skill development (programming fundamentals, writing skills)
- C04d: Educational material creation (lesson plans, teaching resources)

---

### C05 — Review and Feedback

**Axial categories collapsed:**
Review and feedback on written work (6) = **6 instances**
(plus OpenAI Writing subcategory: "edit/critique provided text" ~two-thirds
of Writing 23.9%)

**Collapse rationale:** This category is defined by the user providing an
existing text artefact and asking for critique, editing, grading, or
improvement suggestions. It is distinct from C01 (producing content from
scratch) and from C04 (pedagogical explanation) because the user already
has a text and wants evaluation or improvement of that specific text.

**Formal definition:** Review and Feedback is the capability to evaluate,
critique, edit, and improve existing written or creative work produced by
the user. The model acts as a reviewer, editor, or assessor — identifying
errors, weaknesses, and opportunities for improvement in a user-supplied
artefact and providing actionable feedback or a revised version.

**Decision rule:** A task belongs to C05 if and only if (a) the user
provides an existing text artefact as the primary input, AND (b) the
user's goal is evaluation, correction, critique, or improvement of that
specific artefact (not creation of a new one).

**Edge cases:**
- "Edit my essay to fix grammar" → C05. "Write me an essay on climate change" → C01.
- "Proofread this email before I send it" → C05.
  "Write me an email to send to my client" → C01.
- "Grade this student's essay using the rubric" → C05.
  "Create a grading rubric" → C01.
- Peer review response (revising a manuscript based on reviewer comments)
  → C05 (improving an existing artefact based on external feedback).

**Sub-categories:**
- C05a: Proofreading and grammar correction
- C05b: Substantive editing and content improvement
- C05c: Academic feedback and grading
- C05d: Peer review and manuscript revision

---

### C06 — Translation and Language Processing

**Axial categories collapsed:**
Translation and language processing (4) = **4 instances**
(cross-validated with OpenAI Translation subcategory and
OpenRouter Translation category)

**Collapse rationale:** Translation tasks share the distinguishing feature
that the primary transformation is cross-lingual: the user supplies content
in one language and requires it in another, or needs language learning
support. This is qualitatively distinct from C01 (original text in a single
language), C05 (improving existing monolingual text), and C03 (factual
information about language).

**Formal definition:** Translation and Language Processing is the capability
to convert text between natural languages, assist users in learning or
practising a foreign language, and perform language-specific transformations
such as grammar checking in a non-native language. The model acts as a
linguist or language tutor, bridging linguistic systems.

**Decision rule:** A task belongs to C06 if and only if the primary user
goal involves a cross-lingual transformation (translating text from one
language to another) OR supporting the user's competence in a language
they are learning.

**Edge cases:**
- "Translate this legal document from French to English" → C06.
  "Write a legal memo in English" → C01.
- "Help me learn Spanish vocabulary" → C06 (language acquisition support).
  "Explain Spanish grammar rules as factual information" → C03.
- "Check the grammar of my English essay" → C05 (monolingual editing).
  "Check the grammar of my French essay and suggest natural phrasing" → C06
  (cross-lingual grammar support for a language learner).

**Sub-categories:**
- C06a: Document and text translation
- C06b: Language learning and grammar support
- C06c: Multilingual content formatting

---

### C07 — Data Analysis and Summarisation

**Axial categories collapsed:**
Data analysis and summarisation (12) = **12 instances**
(plus OpenAI Data Analysis 0.4% and document-processing tasks)

**Collapse rationale:** These tasks involve the model processing existing
datasets, documents, or information to extract patterns, insights, or
compressed representations. The primary output is structured or summarised
information derived from inputs, rather than original content (C01) or
information retrieved from the model's knowledge base (C03).

**Formal definition:** Data Analysis and Summarisation is the capability
to process, analyse, and synthesise existing datasets, documents, or
information corpora to extract insights, patterns, statistical results,
or compressed representations. The model acts as an analyst, converting
raw or verbose input into structured, meaningful output.

**Decision rule:** A task belongs to C07 if and only if (a) the user
provides existing data or documents as input, AND (b) the goal is to
extract, compress, or analyse information from that input (rather than
produce a new creative artefact or retrieve facts from the model's
knowledge base).

**Edge cases:**
- "Summarise this 50-page report" → C07 (compressing existing content).
  "Write a report on AI regulation" → C01 (producing new content).
- "Analyse this CSV and find sales trends" → C07.
  "Explain what regression analysis is" → C04.
- "Convert this Word document to PDF format" → C07 (document manipulation).
  "Write a document I can save as a PDF" → C01.

**Sub-categories:**
- C07a: Text summarisation and compression
- C07b: Data analysis and statistical computing
- C07c: Document processing and format conversion
- C07d: Business intelligence and forecasting

---

### C08 — Conversational Interaction and Roleplay

**Axial categories collapsed:**
Conversational interaction and personal advisory (8) = **8 instances**
(plus OpenAI Self-Expression 5.3% and OpenRouter Roleplay ~50% OSS)

**Collapse rationale:** These tasks involve the model as an interactive
conversational partner rather than as a producer of a discrete artefact
or a retriever of information. The interaction has value in itself —
for emotional support, entertainment, practice, or exploratory dialogue
— rather than producing a transferable output.

**Formal definition:** Conversational Interaction and Roleplay is the
capability to engage in open-ended, interactive dialogue with users for
purposes of entertainment, personal support, social practice, or
collaborative world-building. The model acts as a conversational partner,
adopting personas, participating in narratives, and responding to
emotional or social cues in a sustained exchange.

**Decision rule:** A task belongs to C08 if and only if the primary user
value lies in the interactive conversational exchange itself (rather than
a discrete output artefact), AND the interaction serves emotional,
entertainment, social practice, or exploratory purposes.

**Edge cases:**
- "Pretend you're a historical figure and I'll interview you" → C08
  (interactive roleplay). "Write a monologue by a historical figure" → C01.
- "I'm feeling lonely and want to chat" → C08.
  "Help me understand why I feel lonely" → C03 or C04.
- "Practice a job interview with me" → C08 (interactive conversational
  practice). "Give me tips for job interviews" → C03.

**Sub-categories:**
- C08a: Personal and emotional support dialogue
- C08b: Interactive roleplay and collaborative fiction
- C08c: Social and conversational practice (interviews, language)
- C08d: Entertainment and games

---

## Capability Distribution Summary (131 coded instances)

| Capability | Code | Instance Count | % of Coded Instances |
|-----------|------|---------------|---------------------|
| Code Development and Technical Problem Solving | C02 | 55 | 42.0% |
| Information Retrieval and Advisory | C03 | 26 | 19.8% |
| Content Generation | C01 | 16 | 12.2% |
| Data Analysis and Summarisation | C07 | 13 | 9.9% |
| Learning and Education Support | C04 | 11 | 8.4% |
| Conversational Interaction and Roleplay | C08 | 8 | 6.1% |
| Review and Feedback | C05 | 7 | 5.3% |
| Translation and Language Processing | C06 | 4 | 3.1% |
| **TOTAL** | | **140** | **~107%*** |

*Note on C02 dominance:* The Feb 2026 AEI dataset uses O*NET task labels that
consolidate many software sub-tasks into broad occupational buckets, causing a
higher apparent proportion of C02 tasks compared to OpenAI data where Technical
Help is only 5.1% of messages. This reflects different classification granularity
rather than a genuine platform difference, and both perspectives are retained.

---

*Document version: 2.0 (Feb 2026 data)*
*Produced as part of Phase 1 Week 2 (Braun & Clarke, 2006)*
