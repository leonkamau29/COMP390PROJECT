<!-- markdownlint-disable MD013 -->

# Phase 2 Final Benchmark List

This is my final Phase 2 benchmark list after the alternatives review. The list contains 28 benchmarks across the eight capabilities from the Phase 1 taxonomy. I kept the inventory broader than the original 15 to 20 target because the final taxonomy covers eight distinct capability areas, and leaving C06, C07, or C08 without any benchmark coverage would make the inventory inconsistent with the usage analysis.

The final allocation is 5 benchmarks for C02 Code Development and Technical Problem Solving, 5 for C03 Information Retrieval and Advisory, 4 for C01 Content Generation, 4 for C07 Data Analysis and Summarisation, 3 for C04 Learning and Education Support, 3 for C05 Review and Feedback, 2 for C08 Conversational Interaction and Roleplay, and 2 for C06 Translation and Language Processing.

## C02: Code Development and Technical Problem Solving

C02 is the highest-priority capability, with 34.0 percent of the top 103 Anthropic AEI tasks. I retained HumanEval and HumanEval+ as B001, but only as a historical anchor. They remain useful for showing how older coding benchmarks became saturated, since frontier models now exceed 90 percent on the task format. They should not be treated as the main Phase 3 evidence for current C02 coverage.

B002 is SWE-bench Verified, which I selected as the primary benchmark for agentic real-world software issue resolution. It contains 500 human-verified GitHub issues and requires models to produce patches that pass real tests. B003 is LiveCodeBench, which I selected because its post-cutoff and regularly refreshed coding problems provide a stronger contamination-control signal than older static coding datasets. B004 is BigCodeBench Hard, which I included because it measures library and API integration rather than only algorithmic problem solving. B005 is SWE-Lancer Diamond, which I added because it links software tasks to economic value and includes both individual software engineering tasks and managerial judgement over proposals.

Together, these five entries let me describe C02 as a benchmark-rich area, but not a perfectly covered one. The benchmarks cover isolated coding, repository repair, contamination-resistant coding, API integration, and economically framed software tasks.

## C03: Information Retrieval and Advisory

C03 is the second-ranked capability, with 21.4 percent of the top 103 tasks. I selected B006 MMLU-Pro as the broad knowledge baseline because it is harder and more current than plain MMLU. B007 GPQA Diamond is included as the expert-level science reasoning ceiling and appears in major frontier model release tables. B008 Humanity's Last Exam is included because it has become a major frontier knowledge benchmark across OpenAI, Anthropic, Google, xAI, and DeepSeek reports.

B009 combines SimpleQA and FACTS Grounding because together they cover factuality and grounded faithfulness, which are central to advisory reliability. B010 is LiveBench, which I included because it is refreshed, contamination-limited, and multi-domain. It also helps bridge C03 and C07 because it includes reasoning and data-analysis style tasks.

This set replaces older open-domain QA anchors such as TriviaQA and Natural Questions, which are now less useful for frontier evaluation because they are old, saturated, and more exposed to contamination.

## C01: Content Generation

C01 accounts for 17.5 percent of the top 103 tasks. I selected B011 IFEval because it is the one content-generation-adjacent benchmark that is widely cited by frontier labs. Its value in my analysis is partly critical: it shows that labs often measure verifiable instruction following rather than substantive writing quality.

B012 is WritingBench, which I treat as the strongest direct benchmark for open-ended writing quality across domains. B013 is EQ-Bench Creative Writing v3, which adds live community evaluation of creative style, character voice, emotional authenticity, and longform writing quality. B014 is WildBench, which I selected because it is built from real user tasks and therefore aligns well with the usage-log logic of this project.

This capability remains only partially covered because the strongest writing-quality benchmarks are not yet central in frontier technical reports.

## C07: Data Analysis and Summarisation

C07 accounts for 10.7 percent of the top 103 tasks and was elevated by the Phase 1 revision. I selected B015 InfiAgent-DABench because it is a canonical benchmark for agentic data analysis over CSV files. B016 DA-Code extends this area into executable data-science workflows across wrangling, machine learning, and exploratory analysis. B017 Spider 2.0 covers enterprise text-to-SQL and business intelligence workflows at a scale that is much closer to real organisational data use than older Spider-style benchmarks.

B018 MMLongBench-Doc covers long-context multimodal document understanding over PDFs, including text, charts, images, and tables. I selected it over narrower document extraction benchmarks because it better represents the combined document-processing and analysis tasks that users actually ask models to perform.

This group gives C07 more serious coverage than in earlier versions of the inventory, although it still lacks strong presence in frontier model reports.

## C04: Learning and Education Support

C04 accounts for 7.8 percent of the top 103 tasks. I selected B019 MathDial as the earliest foundation for tutoring dialogue because it distinguishes teaching from simply solving maths problems. B020 MathTutorBench is included because it evaluates pedagogical tasks such as scaffolding and mistake localisation, and its finding that stronger solvers can be weaker tutors is important for the thesis argument. B021 TutorBench is included because it broadens tutoring beyond mathematics into multi-subject and multimodal scenarios.

These benchmarks show that education evaluation is emerging, but still weakly represented in frontier model technical reports. They are important because academic knowledge benchmarks such as MMLU-Pro or GPQA do not test whether a model can teach.

## C05: Review and Feedback

C05 accounts for 3.9 percent of the top 103 tasks, but it is especially important because review and critique are common practical behaviours that frontier reports rarely isolate. I selected B022 CriticBench from Tsinghua as the main critique-and-correct benchmark across reasoning domains. B023 JudgeBench is included because it evaluates whether LLM judges can identify the better answer on objective correctness rather than merely produce plausible feedback. B024 RewardBench 2 is included because reward-model evaluation is closely linked to feedback quality in alignment pipelines.

I replaced the older grouped Auto-J, Shepherd, and MetaCritique entry because these were less current and less methodologically strong than JudgeBench and RewardBench 2.

## C08: Conversational Interaction and Roleplay

C08 has a smaller AEI share at 2.9 percent, but OpenRouter's evidence suggests that roleplay and interactive fiction are much more important in open-source model usage. I selected B025 PingPong because it evaluates dynamic multi-turn roleplay with user emulation and judge ensembles, including human-validation evidence. B026 CoSER replaces FIREBALL because it is broader, more recent, and built from a much larger set of authentic character conversations.

I treat C08 as a capability where the benchmark gap is especially visible because the field has roleplay benchmarks, but they do not appear meaningfully in frontier technical reports.

## C06: Translation and Language Processing

C06 accounts for 1.9 percent of the top 103 tasks. I selected B027 BenchMAX because it provides a broad multilingual evaluation suite across 16 languages and multiple task types. I selected B028 WMT24++ because it gives strong translation-quality coverage across 55 languages and dialects, with human-written references and post-edits.

This pair gives C06 a minimum but defensible benchmark base. BenchMAX covers multilingual capability more broadly, while WMT24++ covers translation quality more directly.

## Final Alignment

My final inventory therefore uses B001 to B028 as the working benchmark set for later phases. B001 is retained as a legacy historical anchor, while B002 to B028 provide the primary cross-capability evidence base. The final list is deliberately not just a list of famous benchmarks. It is a usage-aligned inventory designed to show which real-world capabilities are strongly measured, weakly measured, or mainly represented by proxies.
