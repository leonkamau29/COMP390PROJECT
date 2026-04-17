# Capability Definitions — Draft

**Phase:** Phase 1, Week 2 — Define and Name Themes (Braun & Clarke, 2006, Phase 5)
**Date:** 2026-04-15
**Researcher:** Leon Kamau Kiunga (201759400)
**Derived from:** Thematic analysis of 111+ task instances (Handa et al., 2025; O\*NET)

---

## Summary of Thematic Analysis Process

### Open Coding (Phase 2)

Each of the 123 task instances in task_instances_coded.csv was assigned a short descriptive label (open_code) in the researcher's own words (e.g., "find and fix bugs in existing code", "write social media posts and content strategy", "condense long texts into structured summaries").

### Axial Coding (Phase 3)

Open codes were grouped into 19 intermediate axial categories:

1. Academic task completion
2. Code debugging and repair
3. Code development and debugging
4. Technical troubleshooting and support
5. Professional writing and communication
6. Professional document and plan creation
7. Creative writing
8. Reviewing and editing existing work
9. Domain knowledge retrieval
10. Research and synthesis
11. Advice and guidance
12. Teaching and concept explanation
13. Mathematical problem solving
14. Language translation
15. Language learning and translation
16. Data analysis and interpretation
17. Document analysis and extraction
18. Summarisation and condensation
19. Conversational and interactive dialogue

### Selective Coding (Phase 4)

The 19 axial categories were collapsed into **8 core capabilities** as follows:

| Axial Categories Collapsed                                                                                                  | Core Capability                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Academic task completion; Professional writing and communication; Professional document and plan creation; Creative writing | C01 – Content Generation                           |
| Code debugging and repair; Code development and debugging; Technical troubleshooting and support                            | C02 – Code Development & Technical Problem Solving |
| Domain knowledge retrieval; Research and synthesis; Advice and guidance                                                     | C03 – Information Retrieval & Advisory             |
| Teaching and concept explanation; Mathematical problem solving; Adaptive instruction                                        | C04 – Learning & Education Support                 |
| Reviewing and editing existing work                                                                                         | C05 – Review & Feedback                            |
| Language translation; Language learning and translation                                                                     | C06 – Translation & Language Processing            |
| Data analysis and interpretation; Document analysis and extraction; Summarisation and condensation                          | C07 – Data Analysis & Summarisation                |
| Conversational and interactive dialogue                                                                                     | C08 – Conversational Interaction & Roleplay        |

---

## Draft Capability Definitions

---

### C01 — Content Generation

**Definition:** The LLM produces new written content from a user prompt or partial input. The primary output is a novel artefact — a document, text, plan, or piece of creative writing — that did not exist prior to the interaction. The task is fulfilled when the LLM has generated original material that meets the user's specified purpose, format, or audience.

**Decision rule:** A task belongs to C01 if and only if:
(a) the primary user goal is to obtain a new piece of written content (e.g., essay, email, story, business plan, marketing copy, script, documentation), AND
(b) the LLM's contribution is producing that content rather than improving pre-existing text (→ C05) or retrieving factual information (→ C03).

**Edge cases:**

- "Write and edit a cover letter": primary goal is a new document → C01. If the user provides a draft and asks for improvements → C05.
- "Help me complete my academic assignment": primary output is new writing → C01, even if research is involved.
- "Draft a business plan": novel document → C01, even if it requires drawing on factual knowledge.
- Legal document drafting: C01 (new document creation), not C03.
- "Summarise this report for a presentation": condensation of existing material → C07.

---

### C02 — Code Development & Technical Problem Solving

**Definition:** The LLM writes, modifies, debugs, optimises, or explains code, or provides step-by-step technical instructions to resolve a software/hardware/infrastructure problem. The task output is working or improved code, a configuration, a technical architecture, or a resolution to a technical failure.

**Decision rule:** A task belongs to C02 if and only if:
(a) the output is code, a configuration file, a technical specification, or a systematic technical procedure, AND
(b) the task requires knowledge of programming languages, systems, protocols, or technical infrastructure.

**Edge cases:**

- "Explain what this Python function does": explanation without producing code → C04 (teaching).
- "Debug this SQL query": code repair → C02.
- "Set up a Docker container step by step": technical procedure → C02.
- "What is a REST API?": conceptual explanation → C04.
- "Build a machine learning model for my data": code production → C02, even if ML knowledge is involved.

---

### C03 — Information Retrieval & Advisory

**Definition:** The LLM retrieves, synthesises, or applies domain-specific knowledge to answer a factual question, provide guidance, or support a decision. The user's goal is to obtain information, recommendations, or advice rather than a new document or code artefact. The LLM serves as a knowledgeable informant or advisor.

**Decision rule:** A task belongs to C03 if and only if:
(a) the user's primary goal is to obtain information, recommendations, or decision support, AND
(b) the output is an answer, explanation of facts, or recommendation — not a new content artefact (→ C01) or executable code (→ C02).

**Edge cases:**

- "What are the symptoms of Type 2 diabetes?": factual answer → C03.
- "Write a report on Type 2 diabetes": new document → C01.
- "Help me choose a laptop": recommendation and comparison → C03.
- "Research the history of blockchain and write an essay": essay output → C01 (even though research is involved).
- "How do I negotiate a salary raise?": advisory guidance → C03.

---

### C04 — Learning & Education Support

**Definition:** The LLM serves as a tutor or instructor, structuring knowledge to facilitate understanding, teaching a concept, or scaffolding a learner through a problem. The defining feature is that the interaction is oriented toward the learner's comprehension, not simply delivering a factual answer.

**Decision rule:** A task belongs to C04 if and only if:
(a) the user's goal is to learn or develop understanding of a concept, skill, or procedure, AND
(b) the LLM's role is to explain, demonstrate, or guide (not merely retrieve a fact → C03), AND
(c) the interaction is oriented toward building the user's capability rather than completing a task on their behalf.

**Edge cases:**

- "Explain recursion to me step by step": pedagogically structured explanation → C04.
- "Write recursive code to solve this problem": task completion → C02.
- "Teach me SQL": educational instruction → C04.
- "Write a SQL query for me": code production → C02.
- "What is the quadratic formula?": simple fact retrieval → C03; "Walk me through how to derive the quadratic formula" → C04.

---

### C05 — Review & Feedback

**Definition:** The LLM evaluates, edits, critiques, or improves an existing piece of work produced by the user. The primary input is a user-generated artefact; the LLM's role is to assess quality, identify weaknesses, suggest improvements, or produce a revised version. The output is a critique, annotated version, or improved draft of the original.

**Decision rule:** A task belongs to C05 if and only if:
(a) the user provides an existing artefact (text, code, argument, document) as input, AND
(b) the LLM's primary role is to evaluate, improve, or provide feedback on that artefact — not to produce an entirely new one (→ C01).

**Edge cases:**

- "Proofread this email": reviewing existing text → C05.
- "Write a new email for me": new content → C01.
- "Review my code and suggest improvements": → C05.
- "Fix the bug in my code": if the task is primarily repair → C02; if the task is holistic quality review → C05.
- "Grade this student essay and provide feedback": → C05.
- "Respond to peer reviewers and revise my manuscript": revision driven by external feedback → C05.

---

### C06 — Translation & Language Processing

**Definition:** The LLM converts text from one natural language to another, or assists with language-learning tasks including grammar explanation, vocabulary acquisition, and pronunciation guidance. The task is fundamentally linguistic transformation or language instruction, not general writing (→ C01) or teaching a non-linguistic subject (→ C04).

**Decision rule:** A task belongs to C06 if and only if:
(a) the task involves converting text between natural languages OR providing instruction in a foreign language, AND
(b) the primary user goal is linguistic equivalence, comprehension, or language acquisition — not writing a new document in a language (→ C01).

**Edge cases:**

- "Translate this document from French to English": → C06.
- "Write me an email in French": producing content in a foreign language → C01.
- "Explain the difference between subjunctive and indicative mood in Spanish": language teaching → C06 (linguistic instruction).
- "Help me learn Spanish vocabulary": → C06.
- "Adapt this text for a French-speaking audience": localisation, primarily → C06 if translation is the core task.

---

### C07 — Data Analysis & Summarisation

**Definition:** The LLM processes, analyses, or condenses existing information — numerical data, documents, datasets, or large text corpora — to extract patterns, generate insights, or produce condensed representations. The input is a data artefact; the output is an analysis, summary, visualisation specification, or structured extract.

**Decision rule:** A task belongs to C07 if and only if:
(a) the user provides existing data, documents, or a dataset as input, AND
(b) the LLM's role is to analyse, summarise, extract, or visualise — not to generate new content (→ C01) or answer a factual question from memory (→ C03).

**Edge cases:**

- "Summarise this 50-page report": condensation of existing material → C07.
- "Write a summary of climate change": producing new content from knowledge → C01.
- "Analyse this CSV file and find trends": → C07.
- "What are current trends in climate science?": knowledge-based answer → C03.
- "Extract key dates from this legal document": information extraction → C07.
- "Create a bar chart from this data": visualisation → C07.

---

### C08 — Conversational Interaction & Roleplay

**Definition:** The LLM engages in open-ended dialogue, roleplay, or interactive conversation where the primary value is the conversational experience itself — entertainment, companionship, philosophical exploration, or interactive fiction — rather than a specific informational, creative, or technical output.

**Decision rule:** A task belongs to C08 if and only if:
(a) the user's goal is sustained interactive engagement rather than obtaining a specific artefact or answer, AND
(b) the LLM is expected to maintain a persona, narrative, or conversational dynamic over multiple turns.

**Edge cases:**

- "Let's roleplay a fantasy adventure": interactive fiction → C08.
- "Write me a fantasy adventure story": one-time content production → C01.
- "Discuss the ethics of AI with me": open-ended intellectual dialogue → C08.
- "Explain AI ethics to me": structured explanation → C04.
- "Act as a job interviewer and ask me questions": interactive practice → C08 (the experience is the value, not just information).

---

## Axial Category to Core Capability Mapping Summary

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

*Braun & Clarke (2006) Phase 5: Defining and naming themes.*
