# LLM Capability Taxonomy — Version 1

**Project:** Benchmark Coverage Gap: A Systematic Analysis of Real-World AI Capabilities and Evaluation Practices
**Student:** Leon Kamau Kiunga (201759400)
**Supervisor:** Dr Konstantinos Tsakaldis
**Date:** 2026-05-13
**Data sources:** Anthropic AEI (Feb 2026, arXiv:2503.04761); Ouyang et al. (2025) NBER WP 34255; OpenRouter (2025) 100T Token Study
**Methodology:** Braun & Clarke (2006) six-phase thematic analysis
**Status:** Version 1 — pending Week 3 validation

---

## Overview

This taxonomy was derived through systematic thematic analysis of 131 real-world
LLM task instances drawn from three empirical sources covering Claude.ai (Anthropic
AEI, Feb 2026), ChatGPT (Ouyang et al., 2025, NBER WP 34255), and a cross-platform
aggregator (OpenRouter, 2025). Eight core capabilities were identified through
open coding (131 open codes), axial coding (19 intermediate categories), and
selective coding (8 final capabilities).

The taxonomy is intended to provide a usage-grounded foundation for the benchmark
coverage gap analysis in Phase 3. Each capability is defined with sufficient
precision to support reliable classification of both task instances and benchmark
evaluations.

---

## Capability Hierarchy

```
LLM Capability Taxonomy
│
├── C01  Content Generation
│   ├── C01a  Academic and educational writing
│   ├── C01b  Professional and business writing
│   ├── C01c  Marketing and promotional writing
│   ├── C01d  Creative writing (fiction, poetry, scripts)
│   └── C01e  Technical and specialised writing
│
├── C02  Code Development and Technical Problem Solving
│   ├── C02a  Web application development
│   ├── C02b  Software engineering and systems
│   ├── C02c  Code debugging and refactoring
│   ├── C02d  Machine learning and AI development
│   ├── C02e  DevOps and infrastructure
│   └── C02f  Technical troubleshooting
│
├── C03  Information Retrieval and Advisory
│   ├── C03a  Factual and encyclopaedic information
│   ├── C03b  Product and service recommendations
│   ├── C03c  Career, financial, and personal advisory
│   ├── C03d  Research synthesis and literature overview
│   └── C03e  Practical how-to guidance
│
├── C04  Learning and Education Support
│   ├── C04a  Academic assignment support
│   ├── C04b  Concept explanation and tutoring
│   ├── C04c  Skill development
│   └── C04d  Educational material creation
│
├── C05  Review and Feedback
│   ├── C05a  Proofreading and grammar correction
│   ├── C05b  Substantive editing and content improvement
│   ├── C05c  Academic feedback and grading
│   └── C05d  Peer review and manuscript revision
│
├── C06  Translation and Language Processing
│   ├── C06a  Document and text translation
│   ├── C06b  Language learning and grammar support
│   └── C06c  Multilingual content formatting
│
├── C07  Data Analysis and Summarisation
│   ├── C07a  Text summarisation and compression
│   ├── C07b  Data analysis and statistical computing
│   ├── C07c  Document processing and format conversion
│   └── C07d  Business intelligence and forecasting
│
└── C08  Conversational Interaction and Roleplay
    ├── C08a  Personal and emotional support dialogue
    ├── C08b  Interactive roleplay and collaborative fiction
    ├── C08c  Social and conversational practice
    └── C08d  Entertainment and games
```

---

## C01 — Content Generation

### Definition
Content Generation is the capability to produce original, purposeful written or
multimedia text artefacts in response to a user's creative, professional, or
communicative goal. The model acts as an author or co-author, generating content
that serves the user's intended audience and context. This encompasses professional
business documents, creative fiction, marketing copy, scripts, personal
communications, and technical documentation — any task where the primary output
is a newly composed artefact.

### Decision Rule
A task belongs to C01 if and only if:
- (a) the primary user goal is to obtain a new written or multimedia artefact, AND
- (b) the model is the primary producer of that artefact's content (not locating
  existing information or critiquing a user's existing text).

### Sub-categories
- **C01a** Academic and educational writing: essays, assignment responses, reports
- **C01b** Professional and business writing: emails, strategy documents, CVs, proposals
- **C01c** Marketing and promotional writing: ad copy, social media posts, SEO content
- **C01d** Creative writing: fiction, poetry, scripts, personal messages, song lyrics
- **C01e** Technical and specialised writing: clinical notes, legal drafts, architecture specs

### Worked Examples (from task_instances_coded.csv)

1. *"Draft and refine professional workplace emails and business correspondence"*
   (Anthropic AEI, 2.96%) → C01b. The user wants a new email artefact produced
   by the model. Primary output is a composed professional communication.

2. *"Create marketing content, advertising campaigns, and SEO materials"*
   (Anthropic AEI, 2.88%) → C01c. The model generates promotional copy. The
   output is an original marketing artefact tailored to the user's audience.

3. *"Assist with creative fiction writing, editing, and development"*
   (Anthropic AEI, 1.71%) → C01d. The user wants original narrative content
   generated or substantially developed by the model.

4. *"Create religious content, spiritual guidance, poetry, and creative writing"*
   (Anthropic AEI, 1.51%) → C01d. Poetry and spiritual texts are composed
   artefacts where the model serves as author.

5. *"Write personal communications and messages on behalf of user"*
   (OpenAI study) → C01d. Personal messages written from scratch by the model
   at the user's direction are original artefacts.

6. *"Assist with marketing copy or legal document drafting"*
   (OpenRouter) → C01c/C01e. Drafting legal or marketing documents is originative
   content production, regardless of the specialised domain.

7. *"Develop comprehensive business strategy documents and corporate planning materials"*
   (Anthropic AEI, 2.72%) → C01b. Business strategy documents are professional
   artefacts produced by the model as co-author.

8. *"Create and format professional presentation slides and materials"*
   (Anthropic AEI, 0.71%) → C01b. Slide content creation is originative writing
   even when structured as a presentation.

### Edge Cases
- Writing an email FROM SCRATCH → C01. Editing an email the user already drafted → C05.
- Generating a summary of a document → C07. Writing a narrative essay → C01.
- Translating a document → C06. Writing a bilingual document from scratch → C01.
- "Help me write my thesis chapter" (substantial authorship) → C01.
  "Give me feedback on my thesis chapter" → C05.

---

## C02 — Code Development and Technical Problem Solving

### Definition
Code Development and Technical Problem Solving is the capability to write, debug,
refactor, and maintain software code; to design and implement technical systems;
and to diagnose and resolve technical failures in software, hardware, and networked
infrastructure. The model acts as a technical collaborator, producing or modifying
executable artefacts and providing concrete technical solutions that make systems
function correctly.

### Decision Rule
A task belongs to C02 if and only if the primary output is:
- (a) executable code, a configuration file, or a technical command, OR
- (b) a diagnosis and fix for a technical system failure where the resolution
  involves modifying a technical artefact.

### Sub-categories
- **C02a** Web application development: frontend (HTML/CSS/JS), backend, full-stack, APIs
- **C02b** Software engineering and systems: business apps, mobile apps, databases, automation
- **C02c** Code debugging and refactoring: fixing bugs, improving code quality, performance
- **C02d** Machine learning and AI development: models, training pipelines, AI systems
- **C02e** DevOps and infrastructure: CI/CD, deployment, containers, server configuration
- **C02f** Technical troubleshooting: hardware failures, network issues, system configuration

### Worked Examples (from task_instances_coded.csv)

1. *"Troubleshoot and configure hardware, software, and system technical issues"*
   (Anthropic AEI, 4.16%) → C02f. Resolution requires modifying system configuration;
   the output is a fix, not mere information.

2. *"Develop, debug, and modify websites and web applications"*
   (Anthropic AEI, 3.92%) → C02a. The model produces executable web code that makes
   the application function as intended.

3. *"Debug, fix, and refactor code across multiple languages and systems"*
   (Anthropic AEI, 1.86%) → C02c. The primary output is corrected, improved code.

4. *"Develop, debug, and optimize machine learning and AI systems"*
   (Anthropic AEI, 1.50%) → C02d. ML system development produces executable model
   pipelines and training code.

5. *"Learn and troubleshoot DevOps infrastructure and deployment technologies"*
   (Anthropic AEI, 0.97%) → C02e. DevOps troubleshooting produces configuration
   changes and deployment scripts.

6. *"Write or debug computer programming code"*
   (OpenAI study, 4.2% of messages) → C02b/C02c. Direct code production or repair.

7. *"Write or assist with programming and software development tasks"*
   (OpenRouter, 11–50% of token usage) → C02b. Programming assistance produces
   executable code output.

8. *"Implement and troubleshoot authentication, authorization, and security systems"*
   (Anthropic AEI, 0.96%) → C02a. Security system implementation is web/backend
   development producing executable code artefacts.

### Edge Cases
- "Explain how recursion works" → C04 (conceptual understanding, not code production).
  "Write a recursive function to traverse a tree" → C02.
- "Tell me what DevOps tools exist" → C03. "Set up a CI/CD pipeline for me" → C02.
- "Debug this Python script" (user provides code) → C02c.
  "Review my Python script for best practices" → C05.

---

## C03 — Information Retrieval and Advisory

### Definition
Information Retrieval and Advisory is the capability to locate, synthesise, and
deliver factual information, evidence-based recommendations, or domain-specific
advisory guidance in response to a user's question or decision-making need. The
model acts as an informed respondent, drawing on its knowledge base to answer
questions, compare options, or advise on decisions. The primary output is
informational text that transfers knowledge to the user.

### Decision Rule
A task belongs to C03 if and only if:
- (a) the user is seeking factual information or advice to inform a decision
  or satisfy curiosity, AND
- (b) the primary output is informational text (not a composed artefact (C01),
  a technical system output (C02), or a pedagogical explanation building
  toward understanding (C04)).

### Sub-categories
- **C03a** Factual and encyclopaedic information: science, medicine, history, law
- **C03b** Product and service recommendations: consumer research, comparisons
- **C03c** Career, financial, and personal advisory: job guidance, financial advice
- **C03d** Research synthesis and literature overview: summarising fields, papers
- **C03e** Practical how-to guidance: recipes, home maintenance, travel, fitness

### Worked Examples (from task_instances_coded.csv)

1. *"Provide medical information and health information across multiple specialties"*
   (Anthropic AEI, 2.38%) → C03a. Medical fact delivery to inform the user's
   understanding or decision-making.

2. *"Help research, compare, and select consumer products for purchase"*
   (Anthropic AEI, 2.25%) → C03b. Product comparison and recommendation to support
   a purchasing decision.

3. *"Provide comprehensive career development and job transition assistance"*
   (Anthropic AEI, 1.63%) → C03c. Advisory guidance on career moves; the output
   is informational advice, not a written artefact.

4. *"Provide food recipes, cooking advice, nutrition information"*
   (Anthropic AEI, 1.15%) → C03e. Practical how-to guidance delivered as
   informational text.

5. *"Answer specific factual or informational questions from the user"*
   (OpenAI study, 24.4% Seeking Information aggregate) → C03a. Direct Q&A is the
   paradigm case of information retrieval.

6. *"Provide how-to procedural advice for practical tasks"*
   (OpenAI study, 28.8% Practical Guidance aggregate) → C03e. Step-by-step
   procedural guidance delivered as information.

7. *"Assist with earth sciences, environmental research, and natural science tasks"*
   (Anthropic AEI, 0.41%) → C03a/C03d. Scientific information retrieval and
   research overview, not a tutorial.

8. *"Provide investment information, stock analysis, and financial market information"*
   (Anthropic AEI, 0.72%) → C03c. Financial advisory is information delivery
   supporting user decisions.

### Edge Cases
- "What are the symptoms of diabetes?" → C03a. "Explain how the immune system
  works in a way a student can understand" → C04.
- "Give me career advice" → C03c. "Write my career change cover letter" → C01.
- "What is matplotlib?" → C03a. "Show me how to use matplotlib step by step" → C04.
- "Recommend a good laptop" → C03b. "Write a product review of a laptop" → C01.

---

## C04 — Learning and Education Support

### Definition
Learning and Education Support is the capability to assist users in acquiring
knowledge, skills, or academic qualifications through tutoring, explanation,
worked examples, and structured guidance. This includes helping learners understand
concepts, complete assignments, solve problems as learning exercises, and develop
academic competencies. The model acts as tutor, teacher, or study partner, with
the primary goal of building the user's understanding or academic capability.

### Decision Rule
A task belongs to C04 if and only if:
- (a) the user's primary goal is to learn, understand, or develop a skill
  (rather than simply obtain an answer), OR
- (b) the task is framed as an educational or academic obligation (coursework,
  homework, exam preparation).

### Sub-categories
- **C04a** Academic assignment support: completing coursework, homework, exam prep
- **C04b** Concept explanation and tutoring: STEM concepts, humanities, science
- **C04c** Skill development: programming fundamentals, writing skills, languages
- **C04d** Educational material creation: lesson plans, quizzes, teaching resources

### Worked Examples (from task_instances_coded.csv)

1. *"Assist with academic assignments and coursework across multiple disciplines"*
   (Anthropic AEI, 5.19%) → C04a. The task is explicitly framed as academic
   obligation; the model supports learning completion.

2. *"Create educational materials and explain concepts across academic subjects"*
   (Anthropic AEI, 1.94%) → C04d/C04b. Creating educational materials is a
   pedagogical support task; explaining concepts is tutoring.

3. *"Help solve and explain mathematics problems across multiple topics and levels"*
   (Anthropic AEI, 1.40%) → C04b. Problem explanation with the intent to build
   mathematical understanding.

4. *"Tutor or teach academic subjects to the user"*
   (OpenAI study, 10.2% of messages) → C04b. Direct tutoring is the paradigm
   case of this capability.

5. *"Help with programming fundamentals including regex and data structures"*
   (Anthropic AEI, 0.32%) → C04c. Programming fundamentals instruction is
   skill-building, not just code production.

6. *"Help with physics education, problems, and theory"*
   (Anthropic AEI, 0.20%) → C04b. Physics education is concept explanation
   for learning purposes.

7. *"Assist with technical and STEM coursework, homework, and assignments"*
   (Anthropic AEI, 1.07%) → C04a. Coursework assistance is academically framed
   and learning-oriented.

8. *"Perform mathematical calculations or solve numerical problems"*
   (OpenAI study, 3.0% of messages) → C04b. Mathematical problem-solving for
   learning purposes (the OpenAI classification context is practical guidance/tutoring).

### Edge Cases
- "Solve this integral for me" (no learning intent) → C07 or C03.
  "Walk me through how to solve this integral" → C04b.
- "Complete my essay for me" → C01. "Help me understand essay structure" → C04c.
- "Grade these essays" → C05. "Create a rubric for grading essays" → C01.
- "Explain what Docker is" → C03a if brief factual query; C04b if structured
  tutorial is requested.

---

## C05 — Review and Feedback

### Definition
Review and Feedback is the capability to evaluate, critique, edit, and improve
existing written or creative work produced by the user or a third party. The model
acts as a reviewer, editor, or assessor — identifying errors, weaknesses, and
opportunities for improvement in a user-supplied artefact and providing actionable
feedback, corrections, or a revised version. The defining feature is that a
user-produced artefact is the primary input.

### Decision Rule
A task belongs to C05 if and only if:
- (a) the user provides an existing text artefact as the primary input, AND
- (b) the user's goal is evaluation, correction, critique, or improvement of
  that specific artefact (not creation of a new one).

### Sub-categories
- **C05a** Proofreading and grammar correction: spelling, punctuation, syntax
- **C05b** Substantive editing and content improvement: clarity, structure, argument
- **C05c** Academic feedback and grading: marking student work, rubric application
- **C05d** Peer review and manuscript revision: responding to reviewers, journal submission

### Worked Examples (from task_instances_coded.csv)

1. *"Edit, proofread, and reformat documents and written content"*
   (Anthropic AEI, 1.71%) → C05a/C05b. The user provides an existing document
   for correction and reformatting.

2. *"Edit or critique provided text to improve writing quality"*
   (OpenAI study, Writing aggregate ~two-thirds of 23.9%) → C05b. The paradigm
   case from OpenAI data: editing user-provided text.

3. *"Grade student work and create educational assessments"*
   (Anthropic AEI, 0.78%) → C05c. Grading involves evaluating existing student
   artefacts.

4. *"Edit and revise academic writing on AI and research topics"*
   (Anthropic AEI, 0.47%) → C05b. Academic writing revision is improvement of
   an existing scholarly artefact.

5. *"Respond to peer reviewers and revise manuscripts for journal submission"*
   (Anthropic AEI, 0.12%) → C05d. Responding to peer review involves critiquing
   and improving an existing manuscript.

6. *"Revise and format academic documents across multiple disciplines"*
   (previous AEI dataset, referenced in earlier analysis) → C05b. Revision implies
   an existing artefact is being improved.

7. *"Proofread this email before I send it"*
   (illustrative instance consistent with C05a pattern) → C05a. The user's email
   is the input; correction is the output.

8. *"Provide feedback on my business plan"*
   (consistent with C05b patterns across sources) → C05b. Business plan critique
   is substantive review of an existing artefact.

### Edge Cases
- "Edit my essay" → C05b. "Write me an essay" → C01.
- "Fix the grammar in my cover letter" → C05a. "Write my cover letter" → C01.
- "Grade this student's essay using the rubric" → C05c.
  "Create a grading rubric" → C01.
- Peer review response → C05d. Writing a new paper → C01.

---

## C06 — Translation and Language Processing

### Definition
Translation and Language Processing is the capability to convert text between
natural languages, assist users in learning or practising a foreign language, and
perform language-specific transformations such as grammar checking in a non-native
language context. The model acts as a linguist or language tutor, bridging
linguistic systems. The defining feature is a cross-lingual purpose.

### Decision Rule
A task belongs to C06 if and only if:
- (a) the primary user goal involves a cross-lingual transformation (translating
  text from one language to another), OR
- (b) the user is seeking support for competence in a language they are learning
  (vocabulary, grammar, expression in the target language).

### Sub-categories
- **C06a** Document and text translation: legal, medical, technical, general
- **C06b** Language learning and grammar support: vocabulary, grammar, fluency
- **C06c** Multilingual content formatting: producing content in multiple languages

### Worked Examples (from task_instances_coded.csv)

1. *"Provide language learning assistance, translation, and grammar help across multiple languages"*
   (Anthropic AEI, 1.51%) → C06a/C06b. Covers both translation and language learning
   support in a single cluster.

2. *"Translate and format diverse professional, academic, medical, and religious content between languages"*
   (Anthropic AEI, 1.20%) → C06a. Cross-lingual document conversion across
   professional domains.

3. *"Translate text between languages for the user"*
   (OpenAI study, Writing subcategory) → C06a. Direct translation is the paradigm case.

4. *"Translate written content between different natural languages"*
   (OpenRouter) → C06a. Platform-level confirmation that translation is a distinct
   usage category.

5. *"Help me learn Spanish vocabulary"*
   (illustrative instance consistent with C06b) → C06b. Language acquisition
   support, not mere factual information about Spanish.

6. *"Check the grammar of my French essay and suggest natural phrasing"*
   (illustrative instance consistent with C06b) → C06b. Language learner grammar
   support is cross-lingual in character.

7. *"Translate a legal contract from German to English and preserve formatting"*
   (illustrative instance consistent with C06a) → C06a. Legal document translation
   with formatting preservation.

8. *"Help me practise conversational Arabic"*
   (illustrative instance consistent with C06b) → C06b. Conversational language
   practice is language learning support, even in dialogue form.

### Edge Cases
- "Translate this document from French to English" → C06a.
  "Write a document in English" → C01.
- "Help me learn Spanish" → C06b. "Explain Spanish grammar" as factual query → C03a.
- "Check the grammar of my English essay" → C05a (monolingual editing).
  "Check the grammar of my French essay" (user is a French learner) → C06b.
- "Write a bilingual brochure in English and Mandarin" → C01c (original content
  production in multiple languages is authorship, not translation).

---

## C07 — Data Analysis and Summarisation

### Definition
Data Analysis and Summarisation is the capability to process, analyse, and
synthesise existing datasets, documents, or information corpora to extract
insights, patterns, statistical results, or compressed representations. The model
acts as an analyst or information processor, converting raw or verbose input into
structured, meaningful output. The defining feature is that the user supplies
existing data or content as the primary input.

### Decision Rule
A task belongs to C07 if and only if:
- (a) the user provides existing data, documents, or a corpus as input, AND
- (b) the goal is to extract, compress, or analyse information from that input
  (not to produce a new creative artefact or retrieve facts from the model's
  knowledge base).

### Sub-categories
- **C07a** Text summarisation and compression: summarising documents, reports, papers
- **C07b** Data analysis and statistical computing: processing datasets, statistics
- **C07c** Document processing and format conversion: reformatting, converting files
- **C07d** Business intelligence and forecasting: business data analysis, reporting

### Worked Examples (from task_instances_coded.csv)

1. *"Extract, analyze, and process content from images and documents"*
   (Anthropic AEI, 1.47%) → C07a/C07b. The user supplies images or documents;
   the model extracts and analyses their content.

2. *"Conduct comprehensive business and corporate research analysis"*
   (Anthropic AEI, 1.05%) → C07d. Business research analysis processes existing
   data sources to generate business intelligence.

3. *"Assist with data analysis, statistical computing, and database management tasks"*
   (Anthropic AEI, 0.96%) → C07b. Statistical computing on user-supplied datasets.

4. *"Analyse datasets or perform data analysis and reporting tasks"*
   (OpenAI study, 0.4% Data Analysis subcategory) → C07b. Direct dataset
   analysis and reporting.

5. *"Create data visualizations, dashboards, and knowledge maps"*
   (Anthropic AEI, 0.54%) → C07b/C07d. Visualisation is a form of analytical
   output derived from existing data.

6. *"Extract and structure data from multiple sources into organized formats"*
   (Anthropic AEI, 0.33%) → C07c. Data extraction and structuring processes
   existing sources into a new structured form.

7. *"Analyze business data and generate forecasting reports and insights"*
   (Anthropic AEI, 0.20%) → C07d. Forecasting reports are analytical outputs
   derived from existing business data.

8. *"Generate argument or document summaries on demand"*
   (OpenAI study) → C07a. Document summarisation compresses existing content
   into a shorter representation.

### Edge Cases
- "Summarise this report" → C07a. "Write a report on this topic" → C01.
- "Analyse this CSV" → C07b. "Explain what regression analysis is" → C04b.
- "Convert this Word doc to PDF" → C07c. "Write a document" → C01.
- "Solve this equation" without data input → C04b (learning context) or C03.
  "Analyse these survey results and run descriptive statistics" → C07b.

---

## C08 — Conversational Interaction and Roleplay

### Definition
Conversational Interaction and Roleplay is the capability to engage in open-ended,
interactive dialogue with users for purposes of entertainment, personal support,
social practice, or collaborative world-building. The model acts as a conversational
partner, adopting personas, participating in narratives, and responding to emotional
or social cues in a sustained exchange. The defining feature is that the primary
user value lies in the interactive exchange itself rather than in a discrete output
artefact.

### Decision Rule
A task belongs to C08 if and only if:
- (a) the primary user value lies in the interactive conversational exchange itself
  (not in a discrete transferable output), AND
- (b) the interaction serves emotional, entertainment, social practice, or
  exploratory purposes.

### Sub-categories
- **C08a** Personal and emotional support dialogue: loneliness, mental wellness,
  relationship reflection
- **C08b** Interactive roleplay and collaborative fiction: character roleplay,
  interactive stories, games
- **C08c** Social and conversational practice: interview rehearsal, language conversation
- **C08d** Entertainment and games: trivia, casual games, divination, sports prediction

### Worked Examples (from task_instances_coded.csv)

1. *"Get relationship, dating, parenting, and personal advice across life situations"*
   (Anthropic AEI, 1.15%) → C08a. Personal advisory in a sustained emotional
   dialogue context. (Distinguish from C03c: this is ongoing personal support,
   not one-shot advice delivery.)

2. *"Practice job interviews and roleplay professional scenarios"*
   (Anthropic AEI, 0.65%) → C08c. Interactive interview practice is valued for
   the conversational exchange, not a specific output document.

3. *"Engage in casual conversation or social chitchat with the model"*
   (OpenAI study, 5.3% Self-Expression aggregate) → C08a. Social interaction
   with no task output goal.

4. *"Discuss relationships or seek personal emotional reflection support"*
   (OpenAI study, 1.9% subcategory) → C08a. Emotional support dialogue.

5. *"Play interactive games or engage in roleplay with the model"*
   (OpenAI study, 0.4% subcategory) → C08b/C08d. Interactive fiction and games.

6. *"Engage in interactive roleplay or collaborative fiction storytelling"*
   (OpenRouter, ~50% of OSS token usage) → C08b. The dominant OSS usage pattern
   on OpenRouter; collaborative fiction as interactive exchange.

7. *"Provide mental health, behavioral health, and ADHD support resources"*
   (Anthropic AEI, 0.35%) → C08a. Mental health support is sustained interactive
   dialogue, not one-shot information delivery.

8. *"Create prediction tools for gaming, sports analysis, and divination readings"*
   (Anthropic AEI, 0.54%) → C08d. Prediction and divination tools are used for
   entertainment in interactive exchanges.

### Edge Cases
- "Pretend you're a historical figure and I'll interview you" → C08b (interactive
  roleplay). "Write a monologue by a historical figure" → C01d.
- "Practice a job interview with me" → C08c. "Give me tips for job interviews" → C03c.
- "I feel anxious, can we talk?" → C08a. "What are the symptoms of anxiety?" → C03a.
- "Help me with relationship problems" (one-shot advice) → C03c.
  "I need someone to talk to about my relationship" (sustained emotional dialogue) → C08a.

---

## Cross-Capability Disambiguation Table

| Ambiguous Scenario | Correct Capability | Rationale |
|---|---|---|
| User asks model to write code | C02 | Primary output is executable artefact |
| User asks model to explain code | C04 | Goal is understanding, not artefact |
| User asks model to review their code | C05 | User's code is the input; feedback is the goal |
| User provides document; asks for summary | C07 | Compression of existing input |
| User asks model to write a document | C01 | Original authorship |
| User provides their essay; asks for feedback | C05 | Review of existing artefact |
| User asks how to write an essay | C04 | Skill development |
| User asks model to translate text | C06 | Cross-lingual conversion |
| User asks about a language (factually) | C03 | Informational query |
| User wants to learn a language | C06 | Language acquisition support |
| User asks for medical information | C03 | Factual retrieval |
| User wants tutoring on biology | C04 | Pedagogical intent |
| User wants emotional conversation | C08 | Interactive exchange value |
| User asks for advice (one-shot) | C03 | Informational advisory |

---

## Validation Status (Week 3 pending)

| Metric | Target | Status |
|--------|--------|--------|
| Taxonomy coverage of Anthropic top 100 tasks | ≥95% | Pending Week 3 mapping |
| Cohen's κ (10% subsample) | >0.8 | Pending inter-coder reliability exercise |
| Number of core capabilities | 6–10 | 8 ✓ |
| Worked examples per capability | ≥5 | 8 per capability ✓ |

---

*Document produced as part of Phase 1 Week 2 (Braun & Clarke, 2006)*
*Data sources: Handa et al. (2025) arXiv:2503.04761; Ouyang et al. (2025) NBER WP 34255; OpenRouter (2025)*
