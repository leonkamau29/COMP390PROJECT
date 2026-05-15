<!-- markdownlint-disable MD013 -->

# Capability Definitions Draft: Phase 1 Week 2

This draft records how I moved from open coding to axial coding and then to the eight core capabilities used in the Phase 1 taxonomy. The dataset combines the Anthropic AEI February 2026 update, OpenAI's NBER working paper 34255, and the OpenRouter 100T token study. In total, I coded 131 task instances using Braun and Clarke's thematic analysis approach.

## Open Coding

For open coding, I assigned each task a short label that described the user's main action in plain language. I kept the codes close to the task descriptions and avoided adding theory too early. Examples included helping with academic coursework, fixing technical problems, building web applications, writing professional emails, proofreading documents, giving medical information, translating text, and having casual conversational exchanges. These codes are recorded in `data/phase1/task_instances_coded.csv` under the `open_code` column.

## Axial Coding

After open coding, I grouped similar codes into 19 intermediate axial categories. The largest groups were software engineering and application development, information retrieval and factual advisory, professional writing and business communication, data analysis and summarisation, technical troubleshooting and IT support, code debugging and refactoring, conversational interaction, learning support, creative writing, review and feedback, academic assignment support, multimedia content production, translation, marketing content, web application development, academic writing, clinical documentation, legal drafting, and agentic multi-step task execution.

This stage showed that several categories were separate in wording but close in function. Software engineering, debugging, troubleshooting, web application development, and agentic technical work all pointed toward one technical capability. Professional writing, creative writing, marketing, clinical documentation, and legal drafting all involved producing new artefacts. Academic assignment support, tutoring, and academic writing support were also connected by their educational purpose. This was the basis for collapsing the 19 categories into eight core capabilities.

## C01: Content Generation

I define Content Generation as the capability to produce original written or multimedia artefacts for a user's creative, professional, educational, or communicative goal. The model acts as an author or co-author, producing content for a particular audience and context. This capability covers professional writing, business communication, marketing copy, creative writing, technical or specialised documentation, legal drafting, clinical documentation, personal messages, and similar outputs.

I place a task in C01 when the user's main goal is to obtain a new artefact and the model is primarily responsible for producing that artefact. The important distinction is authorship. If the user already has a text and asks for critique or editing, I classify it as C05. If the user asks for a summary of existing material, I classify it as C07. If the user asks for translation, I classify it as C06 because the defining feature is cross-lingual conversion rather than original authorship.

The sub-categories I use for C01 are academic and educational writing, professional and business writing, marketing and promotional writing, creative writing, and technical or specialised writing.

## C02: Code Development and Technical Problem Solving

I define Code Development and Technical Problem Solving as the capability to write, debug, refactor, and maintain software code, design and implement technical systems, and diagnose technical failures in software, hardware, or networked infrastructure. The model acts as a technical collaborator that produces or modifies executable artefacts, configurations, commands, or concrete fixes.

I place a task in C02 when the expected output is executable code, a configuration, a technical command, or a diagnosis and fix for a technical system. This includes software engineering, web development, debugging, refactoring, DevOps, infrastructure work, hardware troubleshooting, network troubleshooting, and some agentic technical tasks. I classify "explain recursion" as C04 because it is about learning, but "write a recursive function" as C02 because it asks for code. I classify "tell me what DevOps tools exist" as C03, but "help me set up a GitHub Actions pipeline" as C02.

The sub-categories I use for C02 are web application development, software engineering and systems, code debugging and refactoring, machine learning and AI development, DevOps and infrastructure, and technical troubleshooting.

## C03: Information Retrieval and Advisory

I define Information Retrieval and Advisory as the capability to locate, synthesise, and provide factual information, recommendations, or domain-specific advice in response to a user's question or decision need. The model acts as an informed respondent, helping the user understand options, compare choices, or obtain facts.

I place a task in C03 when the user is mainly seeking information or advice rather than a new artefact, a technical system change, or a learning sequence. Medical information, consumer product advice, career advice, factual Q&A, research overviews, travel guidance, recipes, and general how-to advice all fit here. If the task is framed as teaching the user so they can develop understanding, I classify it as C04. If it produces a document, I classify it as C01.

The sub-categories I use for C03 are factual and encyclopaedic information, product and service recommendations, career and personal advisory, research synthesis, and practical how-to guidance.

## C04: Learning and Education Support

I define Learning and Education Support as the capability to help users acquire knowledge, skills, or academic competence through tutoring, explanations, worked examples, feedback, and structured guidance. The model acts as a tutor, teacher, or study partner. The central feature is that the user's goal is learning, not just obtaining an answer.

I place a task in C04 when the user wants to understand a concept, prepare for academic work, practise a skill, receive tutoring, or complete a learning-oriented task. "Explain how to solve this integral step by step" belongs here because the goal is understanding. "Complete my essay for me" belongs in C01 because the goal is the finished artefact. "Grade this essay using a rubric" belongs in C05 because the model is reviewing an existing artefact.

The sub-categories I use for C04 are academic assignment support, concept explanation and tutoring, skill development, and educational material creation.

## C05: Review and Feedback

I define Review and Feedback as the capability to evaluate, critique, edit, and improve existing work supplied by the user. The model acts as a reviewer, editor, assessor, or critic. The defining feature is that the user already has an artefact and wants it assessed or improved.

I place a task in C05 when the user provides existing text, code, or creative work and asks for correction, critique, grading, proofreading, revision, or improvement. Editing an email, proofreading an essay, grading student work, reviewing a manuscript, and improving a draft all fit here. Writing a new email from scratch belongs in C01, and creating a grading rubric also belongs in C01 because the model is generating a new artefact.

The sub-categories I use for C05 are proofreading and grammar correction, substantive editing, academic feedback and grading, and peer review or manuscript revision.

## C06: Translation and Language Processing

I define Translation and Language Processing as the capability to convert text between languages, support foreign-language learning, and perform language-specific transformations in a non-native or multilingual context. The model acts as a linguist or language tutor, bridging linguistic systems.

I place a task in C06 when the primary purpose is cross-lingual transformation or language-learning support. Translating a legal document from French to English belongs here. Helping someone learn Spanish vocabulary belongs here. Checking the grammar of an English essay is usually C05, but checking a French essay for a learner and suggesting more natural phrasing belongs in C06 because the language-learning and cross-lingual context is central.

The sub-categories I use for C06 are document and text translation, language learning and grammar support, and multilingual content formatting.

## C07: Data Analysis and Summarisation

I define Data Analysis and Summarisation as the capability to process, analyse, and synthesise existing datasets, documents, or information corpora in order to extract insights, patterns, statistical results, or compressed representations. The model acts as an analyst or information processor.

I place a task in C07 when the user provides existing data or documents and wants the model to extract, compress, transform, or analyse information from that input. Summarising a 50-page report, analysing a CSV for sales trends, converting documents, and extracting information from files all fit here. Writing a new report belongs in C01. Explaining what regression analysis is belongs in C04 because it is educational.

The sub-categories I use for C07 are text summarisation and compression, data analysis and statistical computing, document processing and format conversion, and business intelligence or forecasting.

## C08: Conversational Interaction and Roleplay

I define Conversational Interaction and Roleplay as the capability to engage in open-ended dialogue for entertainment, personal support, social practice, roleplay, or collaborative world-building. The model acts as a conversational partner, and the exchange itself is the main value.

I place a task in C08 when the user wants interaction rather than a discrete output artefact. Roleplaying a historical figure, chatting for companionship, practising a job interview, playing a game, or developing a fictional scene through dialogue all fit here. If the user asks for a monologue by a historical figure, I classify it as C01 because the goal is a written artefact. If the user asks for job-interview advice, I classify it as C03.

The sub-categories I use for C08 are personal and emotional support dialogue, interactive roleplay and collaborative fiction, social or conversational practice, and entertainment or games.

## Capability Distribution Summary

The coded data shows C02 as the largest capability, with 55 coded instances, followed by C03 with 26 instances. C01 has 16 instances, C07 has 13, C04 has 11, C08 has 8, C05 has 7, and C06 has 4. These totals reflect coding and consolidation decisions rather than a simple one-to-one count of independent tasks, so they should be read as evidence of relative emphasis rather than a final statistical distribution.

The main conclusion from this draft is that the eight-capability taxonomy captures the major patterns in the empirical task corpus while preserving distinctions that matter for benchmark analysis. The clearest distinctions are between producing new artefacts, reviewing existing artefacts, answering informational questions, teaching users, and processing supplied data.
