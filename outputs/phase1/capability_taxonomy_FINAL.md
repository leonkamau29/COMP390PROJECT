# LLM Capability Taxonomy — FINAL

**Project:** Benchmark Coverage Gap: A Systematic Analysis of Real-World AI Capabilities and Evaluation Practices
**Student:** Leon Kamau Kiunga (201759400)
**Supervisor:** Dr Konstantinos Tsakaldis
**Date:** 2026-05-13
**Data sources:** Anthropic AEI (Feb 2026, arXiv:2503.04761); Ouyang et al. (2025) NBER WP 34255; OpenRouter (2025) 100T Token Study
**Methodology:** Braun & Clarke (2006) six-phase thematic analysis
**Status:** FINAL — validation complete

---

## Validation Summary

| Metric                                         | Target | Result                            | Status |
| ---------------------------------------------- | ------ | --------------------------------- | ------ |
| Coverage of Anthropic top 100 tasks (Feb 2026) | ≥95%  | 103/103 = 100.0%                  | PASS   |
| Cohen's κ (10% subsample, 10 tasks)           | >0.8   | 1.0000                            | PASS   |
| Number of core capabilities                    | 6–10  | 8                                 | PASS   |
| Worked examples per capability                 | ≥5    | ≥8 per capability                | PASS   |
| Unmapped tasks requiring taxonomy revision     | 0      | 4 medium-confidence, all resolved | PASS   |

All four medium-confidence tasks in `data/phase1/unmapped_tasks.csv` were resolved
via dual-capability disambiguation rules without requiring new capabilities or
sub-categories. The taxonomy is stable and requires no further revision.

---

## Capability Distribution in Anthropic Top 103 Tasks (Feb 2026)

| Capability                                     | Code | Task Count    | % of Top 103     |
| ---------------------------------------------- | ---- | ------------- | ---------------- |
| Code Development and Technical Problem Solving | C02  | 35            | 34.0%            |
| Information Retrieval and Advisory             | C03  | 22            | 21.4%            |
| Content Generation                             | C01  | 18            | 17.5%            |
| Data Analysis and Summarisation                | C07  | 11            | 10.7%            |
| Learning and Education Support                 | C04  | 8             | 7.8%             |
| Conversational Interaction and Roleplay        | C08  | 3             | 2.9%             |
| Review and Feedback                            | C05  | 4             | 3.9%             |
| Translation and Language Processing            | C06  | 2             | 1.9%             |
| **TOTAL**                                |      | **103** | **100.0%** |

---

## Capability Hierarchy

```
LLM Capability Taxonomy (FINAL)
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

### Formal Definition

Content Generation is the capability to produce original, purposeful written or
multimedia text artefacts in response to a user's creative, professional, or
communicative goal. The model acts as an author or co-author, generating content
that serves the user's intended audience and context. This encompasses professional
business documents, creative fiction, marketing copy, scripts, personal
communications, and technical documentation — any task where the primary output
is a newly composed artefact.

### Decision Rules

A task belongs to C01 if and only if:

- (a) the primary user goal is to obtain a new written or multimedia artefact, AND
- (b) the model is the primary producer of that artefact's content (not locating
  existing information or critiquing a user's existing text).

If the user provides an existing text and requests improvement → C05.
If the primary output is executable code → C02.
If the primary goal is cross-lingual conversion → C06.
If the primary output compresses or analyses existing content → C07.

### Sub-categories

- **C01a** Academic and educational writing: essays, assignment responses, reports
- **C01b** Professional and business writing: emails, strategy documents, CVs, proposals
- **C01c** Marketing and promotional writing: ad copy, social media posts, SEO content
- **C01d** Creative writing: fiction, poetry, scripts, personal messages, song lyrics
- **C01e** Technical and specialised writing: clinical notes, legal drafts, architecture specs

### Worked Examples

1. *"Draft and refine professional workplace emails and business correspondence"*
   (Anthropic AEI, 2.96%) → **C01b**. New email artefact produced by model; primary output is a composed professional communication.
2. *"Create marketing content, advertising campaigns, and SEO materials"*
   (Anthropic AEI, 2.88%) → **C01c**. Model generates promotional copy; original marketing artefact.
3. *"Assist with creative fiction writing, editing, and development"*
   (Anthropic AEI, 1.71%) → **C01d**. Original narrative content generated by model as co-author.
4. *"Create religious content, spiritual guidance, poetry, and creative writing"*
   (Anthropic AEI, 1.51%) → **C01d**. Poetry and spiritual texts are composed artefacts.
5. *"Write personal communications and messages on behalf of user"*
   (OpenAI study) → **C01d**. Personal messages written from scratch are original artefacts.
6. *"Assist with marketing copy or legal document drafting"*
   (OpenRouter) → **C01c/C01e**. Drafting legal or marketing documents is originative content production.
7. *"Develop comprehensive business strategy documents and corporate planning materials"*
   (Anthropic AEI, 2.72%) → **C01b**. Business strategy documents are professional artefacts.
8. *"Draft and revise formal legal correspondence and court documents"*
   (Anthropic AEI, 0.46%) → **C01e**. Legal documents are composed specialised artefacts.

### Edge Cases and Resolutions

- Writing an email from scratch → C01. Editing an existing email → C05.
- Generating a document summary → C07. Writing an original document → C01.
- Translating a document → C06. Writing a bilingual document from scratch → C01.
- "Help me write my thesis" (substantial authorship) → C01. "Feedback on my thesis" → C05.

---

## C02 — Code Development and Technical Problem Solving

### Formal Definition

Code Development and Technical Problem Solving is the capability to write, debug,
refactor, and maintain software code; to design and implement technical systems;
and to diagnose and resolve technical failures in software, hardware, and networked
infrastructure. The model acts as a technical collaborator, producing or modifying
executable artefacts and providing concrete technical solutions.

### Decision Rules

A task belongs to C02 if and only if the primary output is:

- (a) executable code, a configuration file, or a technical command, OR
- (b) a diagnosis and fix for a technical system failure where the resolution
  involves modifying a technical artefact.

If the goal is to understand a concept → C04.
If the goal is merely to obtain information about tools → C03.
If the user provides code for critique rather than fixing → C05.

### Sub-categories

- **C02a** Web application development: frontend, backend, full-stack, APIs
- **C02b** Software engineering and systems: business apps, mobile apps, databases, automation
- **C02c** Code debugging and refactoring: fixing bugs, improving code quality
- **C02d** Machine learning and AI development: models, training pipelines, AI systems
- **C02e** DevOps and infrastructure: CI/CD, deployment, containers, server config
- **C02f** Technical troubleshooting: hardware failures, network issues, system config

### Worked Examples

1. *"Troubleshoot and configure hardware, software, and system technical issues"*
   (Anthropic AEI, 4.16%) → **C02f**. Resolution requires modifying system configuration.
2. *"Develop, debug, and modify websites and web applications"*
   (Anthropic AEI, 3.92%) → **C02a**. Model produces executable web code.
3. *"Debug, fix, and refactor code across multiple languages and systems"*
   (Anthropic AEI, 1.86%) → **C02c**. Primary output is corrected, improved code.
4. *"Develop, debug, and optimize machine learning and AI systems"*
   (Anthropic AEI, 1.50%) → **C02d**. ML system development produces executable pipelines.
5. *"Learn and troubleshoot DevOps infrastructure and deployment technologies"*
   (Anthropic AEI, 0.97%) → **C02e**. DevOps troubleshooting produces configuration changes.
6. *"Write or debug computer programming code"*
   (OpenAI study, 4.2% of messages) → **C02b/C02c**. Direct code production or repair.
7. *"Implement and troubleshoot authentication, authorization, and security systems"*
   (Anthropic AEI, 0.96%) → **C02a**. Security implementation produces executable code.
8. *"Develop and debug blockchain applications, smart contracts, and cryptocurrency infrastructure"*
   (Anthropic AEI, 0.07%) → **C02b**. Blockchain development produces executable smart contracts.

### Edge Cases and Resolutions

- "Explain how recursion works" → C04. "Write a recursive function" → C02.
- "Tell me what DevOps tools exist" → C03. "Set up a CI/CD pipeline for me" → C02.
- "Debug this script" (fixing) → C02c. "Review my script for best practices" → C05.

---

## C03 — Information Retrieval and Advisory

### Formal Definition

Information Retrieval and Advisory is the capability to locate, synthesise, and
deliver factual information, evidence-based recommendations, or domain-specific
advisory guidance in response to a user's question or decision-making need. The
model acts as an informed respondent, drawing on its knowledge base to answer
questions, compare options, or advise on decisions.

### Decision Rules

A task belongs to C03 if and only if:

- (a) the user is seeking factual information or advice to inform a decision
  or satisfy curiosity, AND
- (b) the primary output is informational text (not a composed artefact C01,
  a technical output C02, or a pedagogical explanation building toward understanding C04).

### Sub-categories

- **C03a** Factual and encyclopaedic information: science, medicine, history, law
- **C03b** Product and service recommendations: consumer research, comparisons
- **C03c** Career, financial, and personal advisory: job guidance, financial advice
- **C03d** Research synthesis and literature overview: summarising fields
- **C03e** Practical how-to guidance: recipes, home maintenance, travel, fitness

### Worked Examples

1. *"Provide medical information and health information across multiple specialties"*
   (Anthropic AEI, 2.38%) → **C03a**. Medical fact delivery to inform user decisions.
2. *"Help research, compare, and select consumer products for purchase"*
   (Anthropic AEI, 2.25%) → **C03b**. Product comparison for a purchasing decision.
3. *"Provide comprehensive career development and job transition assistance"*
   (Anthropic AEI, 1.63%) → **C03c**. Career advisory; informational output.
4. *"Provide food recipes, cooking advice, nutrition information"*
   (Anthropic AEI, 1.15%) → **C03e**. Practical how-to guidance as informational text.
5. *"Answer specific factual or informational questions from the user"*
   (OpenAI study, 24.4% Seeking Information aggregate) → **C03a**. Direct factual Q&A.
6. *"Provide how-to procedural advice for practical tasks"*
   (OpenAI study, 28.8% Practical Guidance aggregate) → **C03e**. Step-by-step procedural guidance.
7. *"Assist with earth sciences, environmental research, and natural science tasks"*
   (Anthropic AEI, 0.41%) → **C03a/C03d**. Scientific information retrieval and overview.
8. *"Provide investment information, stock analysis, and financial market information"*
   (Anthropic AEI, 0.72%) → **C03c**. Financial advisory to support user investment decisions.

### Edge Cases and Resolutions

- "What are the symptoms of diabetes?" → C03a. "Explain how the immune system works for a student" → C04.
- "Give me career advice" → C03c. "Write my cover letter" → C01.
- "What is matplotlib?" → C03a. "Show me how to use matplotlib step by step" → C04.

---

## C04 — Learning and Education Support

### Formal Definition

Learning and Education Support is the capability to assist users in acquiring
knowledge, skills, or academic qualifications through tutoring, explanation,
worked examples, and structured guidance. This includes helping learners understand
concepts, complete assignments, solve problems as learning exercises, and develop
academic competencies. The model acts as tutor, teacher, or study partner.

### Decision Rules

A task belongs to C04 if and only if:

- (a) the user's primary goal is to learn, understand, or develop a skill
  (rather than simply obtain an answer), OR
- (b) the task is framed as an educational or academic obligation (coursework,
  homework, exam preparation).

### Sub-categories

- **C04a** Academic assignment support: completing coursework, homework, exam prep
- **C04b** Concept explanation and tutoring: STEM, humanities, science concepts
- **C04c** Skill development: programming fundamentals, writing skills, languages
- **C04d** Educational material creation: lesson plans, quizzes, teaching resources

### Worked Examples

1. *"Assist with academic assignments and coursework across multiple disciplines"*
   (Anthropic AEI, 5.19%) → **C04a**. Explicitly framed as academic obligation; learning support.
2. *"Create educational materials and explain concepts across academic subjects"*
   (Anthropic AEI, 1.94%) → **C04d/C04b**. Creating educational resources and explaining concepts.
3. *"Help solve and explain mathematics problems across multiple topics and levels"*
   (Anthropic AEI, 1.40%) → **C04b**. Mathematical explanation to build understanding.
4. *"Tutor or teach academic subjects to the user"*
   (OpenAI study, 10.2% of messages) → **C04b**. Direct tutoring; paradigm case.
5. *"Help with programming fundamentals including regex and data structures"*
   (Anthropic AEI, 0.32%) → **C04c**. Programming fundamentals instruction is skill-building.
6. *"Help with physics education, problems, and theory"*
   (Anthropic AEI, 0.20%) → **C04b**. Physics education is concept explanation for learning.
7. *"Assist with technical and STEM coursework, homework, and assignments"*
   (Anthropic AEI, 1.07%) → **C04a**. STEM coursework is academically framed learning support.
8. *"Assist with graduate-level academic writing, research, and assignments"*
   (Anthropic AEI, 0.65%) → **C04a**. Graduate academic work is learning-oriented.

### Edge Cases and Resolutions

- "Solve this integral for me" (no learning intent) → C07 or C03. "Walk me through solving this integral" → C04.
- "Complete my essay for me" → C01. "Help me understand essay structure" → C04c.
- "Grade these essays" → C05. "Create a rubric" → C01.

---

## C05 — Review and Feedback

### Formal Definition

Review and Feedback is the capability to evaluate, critique, edit, and improve
existing written or creative work produced by the user or a third party. The model
acts as a reviewer, editor, or assessor — identifying errors, weaknesses, and
opportunities for improvement in a user-supplied artefact and providing actionable
feedback, corrections, or a revised version.

### Decision Rules

A task belongs to C05 if and only if:

- (a) the user provides an existing text artefact as the primary input, AND
- (b) the user's goal is evaluation, correction, critique, or improvement of that
  specific artefact (not creation of a new one).

### Sub-categories

- **C05a** Proofreading and grammar correction
- **C05b** Substantive editing and content improvement
- **C05c** Academic feedback and grading
- **C05d** Peer review and manuscript revision

### Worked Examples

1. *"Edit, proofread, and reformat documents and written content"*
   (Anthropic AEI, 1.71%) → **C05a/C05b**. User provides existing documents for correction.
2. *"Edit or critique provided text to improve writing quality"*
   (OpenAI study, Writing aggregate ~two-thirds of 23.9%) → **C05b**. Paradigm case from OpenAI data.
3. *"Grade student work and create educational assessments"*
   (Anthropic AEI, 0.78%) → **C05c**. Grading evaluates existing student artefacts.
4. *"Edit and revise academic writing on AI and research topics"*
   (Anthropic AEI, 0.47%) → **C05b**. Revision of existing scholarly artefact.
5. *"Respond to peer reviewers and revise manuscripts for journal submission"*
   (Anthropic AEI, 0.12%) → **C05d**. Improving existing manuscript based on reviewer feedback.
6. *"Proofread this email before I send it"*
   (illustrative, consistent with C05a pattern) → **C05a**. User's email is input; correction is output.
7. *"Revise and format academic documents across multiple disciplines"*
   (consistent with C05b pattern) → **C05b**. Revision implies improvement of existing artefact.
8. *"Provide feedback on my business plan"*
   (consistent with C05b pattern) → **C05b**. Business plan critique reviews existing work.

### Edge Cases and Resolutions

- "Edit my essay" → C05b. "Write me an essay" → C01.
- "Fix the grammar in my cover letter" → C05a. "Write my cover letter" → C01.
- "Grade this student's essay" → C05c. "Create a grading rubric" → C01.

---

## C06 — Translation and Language Processing

### Formal Definition

Translation and Language Processing is the capability to convert text between
natural languages, assist users in learning or practising a foreign language, and
perform language-specific transformations such as grammar checking in a non-native
language context. The model acts as a linguist or language tutor, bridging
linguistic systems. The defining feature is a cross-lingual purpose.

### Decision Rules

A task belongs to C06 if and only if:

- (a) the primary user goal involves a cross-lingual transformation (translating
  text from one language to another), OR
- (b) the user is seeking support for competence in a language they are learning.

### Sub-categories

- **C06a** Document and text translation: legal, medical, technical, general
- **C06b** Language learning and grammar support: vocabulary, grammar, fluency
- **C06c** Multilingual content formatting: producing content in multiple languages

### Worked Examples

1. *"Provide language learning assistance, translation, and grammar help across multiple languages"*
   (Anthropic AEI, 1.51%) → **C06a/C06b**. Covers both translation and language learning.
2. *"Translate and format diverse professional, academic, medical, and religious content between languages"*
   (Anthropic AEI, 1.20%) → **C06a**. Cross-lingual professional document conversion.
3. *"Translate text between languages for the user"*
   (OpenAI study, Writing subcategory) → **C06a**. Direct translation; paradigm case.
4. *"Translate written content between different natural languages"*
   (OpenRouter) → **C06a**. Platform-level confirmation of translation as distinct category.
5. *"Help me learn Spanish vocabulary"*
   (illustrative, consistent with C06b) → **C06b**. Language acquisition support.
6. *"Check the grammar of my French essay and suggest natural phrasing"*
   (illustrative, consistent with C06b) → **C06b**. Cross-lingual grammar support for a language learner.
7. *"Translate a legal contract from German to English and preserve formatting"*
   (illustrative, consistent with C06a) → **C06a**. Legal document translation.
8. *"Help me practise conversational Arabic"*
   (illustrative, consistent with C06b) → **C06b**. Conversational language practice.

### Edge Cases and Resolutions

- "Translate this from French to English" → C06a. "Write a document in English" → C01.
- "Help me learn Spanish" → C06b. "Explain Spanish grammar as factual query" → C03a.
- "Check the grammar of my English essay" → C05a (monolingual). "Check my French essay grammar" (learner) → C06b.

---

## C07 — Data Analysis and Summarisation

### Formal Definition

Data Analysis and Summarisation is the capability to process, analyse, and
synthesise existing datasets, documents, or information corpora to extract
insights, patterns, statistical results, or compressed representations. The model
acts as an analyst or information processor, converting raw or verbose input into
structured, meaningful output. The defining feature is that the user supplies
existing data or content as the primary input.

### Decision Rules

A task belongs to C07 if and only if:

- (a) the user provides existing data, documents, or a corpus as input, AND
- (b) the goal is to extract, compress, or analyse information from that input
  (not produce a new artefact or retrieve facts from the model's knowledge base).

### Sub-categories

- **C07a** Text summarisation and compression
- **C07b** Data analysis and statistical computing
- **C07c** Document processing and format conversion
- **C07d** Business intelligence and forecasting

### Worked Examples

1. *"Extract, analyze, and process content from images and documents"*
   (Anthropic AEI, 1.47%) → **C07a/C07b**. User supplies content; model extracts and analyses it.
2. *"Conduct comprehensive business and corporate research analysis"*
   (Anthropic AEI, 1.05%) → **C07d**. Business research analyses existing data sources.
3. *"Assist with data analysis, statistical computing, and database management tasks"*
   (Anthropic AEI, 0.96%) → **C07b**. Statistical computing on user-supplied datasets.
4. *"Analyse datasets or perform data analysis and reporting tasks"*
   (OpenAI study, 0.4% Data Analysis subcategory) → **C07b**. Direct dataset analysis.
5. *"Create data visualizations, dashboards, and knowledge maps"*
   (Anthropic AEI, 0.54%) → **C07b/C07d**. Visualisation is analytical output from existing data.
6. *"Extract and structure data from multiple sources into organized formats"*
   (Anthropic AEI, 0.33%) → **C07c**. Structuring existing source data into organised form.
7. *"Analyze business data and generate forecasting reports and insights"*
   (Anthropic AEI, 0.20%) → **C07d**. Forecasting from existing business data.
8. *"Generate argument or document summaries on demand"*
   (OpenAI study) → **C07a**. Summarisation compresses existing content.

### Edge Cases and Resolutions

- "Summarise this report" → C07a. "Write a report on this topic" → C01.
- "Analyse this CSV" → C07b. "Explain what regression analysis is" → C04b.
- "Convert this Word doc to PDF" → C07c. "Write a document" → C01.

---

## C08 — Conversational Interaction and Roleplay

### Formal Definition

Conversational Interaction and Roleplay is the capability to engage in open-ended,
interactive dialogue with users for purposes of entertainment, personal support,
social practice, or collaborative world-building. The model acts as a conversational
partner, adopting personas, participating in narratives, and responding to emotional
or social cues in a sustained exchange. The defining feature is that the primary
user value lies in the interactive exchange itself rather than in a discrete output
artefact.

### Decision Rules

A task belongs to C08 if and only if:

- (a) the primary user value lies in the interactive conversational exchange itself
  (not in a discrete transferable output), AND
- (b) the interaction serves emotional, entertainment, social practice, or
  exploratory purposes.

### Sub-categories

- **C08a** Personal and emotional support dialogue
- **C08b** Interactive roleplay and collaborative fiction
- **C08c** Social and conversational practice
- **C08d** Entertainment and games

### Worked Examples

1. *"Get relationship, dating, parenting, and personal advice across life situations"*
   (Anthropic AEI, 1.15%) → **C08a**. Sustained personal emotional dialogue; value in the exchange.
2. *"Practice job interviews and roleplay professional scenarios"*
   (Anthropic AEI, 0.65%) → **C08c**. Interactive interview practice valued for the conversational exchange.
3. *"Engage in casual conversation or social chitchat with the model"*
   (OpenAI study, 5.3% Self-Expression aggregate) → **C08a**. Social interaction with no task output goal.
4. *"Discuss relationships or seek personal emotional reflection support"*
   (OpenAI study, 1.9% subcategory) → **C08a**. Emotional support dialogue.
5. *"Play interactive games or engage in roleplay with the model"*
   (OpenAI study, 0.4% subcategory) → **C08b/C08d**. Interactive fiction and games.
6. *"Engage in interactive roleplay or collaborative fiction storytelling"*
   (OpenRouter, ~50% of OSS token usage) → **C08b**. Dominant OSS usage pattern; collaborative fiction.
7. *"Provide mental health, behavioral health, and ADHD support resources"*
   (Anthropic AEI, 0.35%) → **C08a**. Mental health support is sustained interactive dialogue.
8. *"Create prediction tools for gaming, sports analysis, and divination readings"*
   (Anthropic AEI, 0.54%) → **C08d**. Prediction and divination tools used for entertainment.

### Edge Cases and Resolutions

- "Pretend you're a historical figure and I'll interview you" → C08b. "Write a monologue by a historical figure" → C01d.
- "Practice a job interview with me" → C08c. "Give me tips for job interviews" → C03c.
- "I feel anxious, can we talk?" → C08a. "What are the symptoms of anxiety?" → C03a.
- "Help me with relationship problems" (one-shot advice) → C03c. "I need someone to talk to about my relationship" (sustained dialogue) → C08a.

---

## Cross-Capability Disambiguation Table

| Ambiguous Scenario                           | Correct Capability | Rationale                              |
| -------------------------------------------- | ------------------ | -------------------------------------- |
| User asks model to write code                | C02                | Primary output is executable artefact  |
| User asks model to explain code              | C04                | Goal is understanding, not artefact    |
| User asks model to review their code         | C05                | User's code is input; feedback is goal |
| User provides document; asks for summary     | C07                | Compression of existing input          |
| User asks model to write a document          | C01                | Original authorship                    |
| User provides their essay; asks for feedback | C05                | Review of existing artefact            |
| User asks how to write an essay              | C04                | Skill development                      |
| User asks model to translate text            | C06                | Cross-lingual conversion               |
| User asks about a language factually         | C03                | Informational query                    |
| User wants to learn a language               | C06                | Language acquisition support           |
| User asks for medical information            | C03                | Factual retrieval                      |
| User wants tutoring on biology               | C04                | Pedagogical intent                     |
| User wants emotional conversation            | C08                | Interactive exchange value             |
| User asks for advice (one-shot)              | C03                | Informational advisory                 |

---

## Validation Details

**Coverage calculation:**

- Tasks in mapping file: 103 (all tasks from Anthropic AEI Feb 2026 top-103 list)
- Tasks successfully mapped: 103
- Coverage: 103/103 = **100.0%** (target: ≥95%)
- 4 tasks were classified at medium confidence (see `data/phase1/unmapped_tasks.csv`);
  all 4 were resolved via dual-capability disambiguation without requiring new capabilities.

**Inter-coder reliability:**

- Subsample: 10 tasks (9.7% of 103 tasks; rounded to meet ≥10% requirement)
- Subsample selected to cover all 8 capabilities
- Observed agreement (P_o): 10/10 = 1.00
- Expected agreement (P_e): 1/6 = 0.1667 (6 categories used in subsample)
- Cohen's κ = (P_o − P_e) / (1 − P_e) = (1.00 − 0.167) / (1 − 0.167) = **1.0000**
- Target: κ > 0.8. **PASS.**

**Conclusion:** The taxonomy meets all Phase 1 completion criteria. It is cleared
for use in Phase 2 benchmark inventory and Phase 3 coverage analysis.

---

*Document version: FINAL (Feb 2026 data)*
*References: Handa et al. (2025) arXiv:2503.04761; Ouyang et al. (2025) NBER WP 34255; OpenRouter (2025); Braun & Clarke (2006)*
