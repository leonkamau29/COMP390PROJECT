<!-- markdownlint-disable MD013 -->

# Phase 2 Benchmark Inventory Research Notes v1

These notes record my first full pass through the Phase 2 benchmark inventory. At this stage, I was still working with a narrower shortlist of 18 benchmarks across five empirically dominant capabilities: C02 Code Development and Technical Problem Solving, C01 Content Generation, C04 Learning and Education Support, C03 Information Retrieval and Advisory, and C05 Review and Feedback.

My main finding from this first pass was that benchmark supply is not evenly distributed. The field has many benchmarks for coding, factual knowledge, mathematics, and STEM-style reasoning. By contrast, the capabilities that many users rely on in practice, such as workplace writing, tutoring, reviewing work, and open-ended roleplay, have much weaker presence in frontier model technical reports.

## Usage Evidence

I used Handa et al. (2025) as the main empirical source. Their analysis of roughly four million Claude.ai Free and Pro conversations shows that Computer and Mathematical tasks are the largest category, with code writing, debugging, and technical troubleshooting dominating the usage picture. Arts and media, education, office administration, science, and business tasks also appear prominently. The interaction-type data was useful because it showed that task iteration, directive use, learning, feedback loops, and validation all appear in real interactions.

At this early stage, I mapped the Handa categories into five main capabilities. C02 was clearly first because software and technical work dominated. C01 moved up in importance because writing and document drafting were more common than I initially expected. C04 also needed to be included because tutoring and education were too prominent to treat as a minor subcase. C03 remained important for factual and advisory tasks, while C05 stayed in scope because review and feedback are visible in both writing and debugging contexts.

My first conclusion was that the researcher's earlier ranking needed revision. C02 was confirmed as the top capability, but C01 had been underestimated and C04 had been missing. C07 was provisionally dropped from the top five at this stage, although I noted that it might return if the later taxonomy revision gave it stronger usage weight.

## Search Channels

I reconstructed the benchmark landscape through four channels. The first was Papers with Code and related historical sources, since the original Papers with Code leaderboards were no longer maintained. This gave me a broad map of legacy NLP, coding, QA, summarisation, translation, and dialogue benchmarks.

The second channel was frontier model technical reports. I reviewed GPT-4 and GPT-4o, Claude 3 and Claude 3.5, Claude 4 family reports, Gemini 1.0 through Gemini 2.5, and Llama 3 through Llama 4. These reports repeatedly cited benchmarks such as MMLU, GPQA Diamond, BIG-Bench Hard, ARC-C, HellaSwag, WinoGrande, GSM8K, MATH, HumanEval, MBPP, DROP, IFEval, TruthfulQA, MMMU, and Needle-in-a-Haystack. In 2025 releases, SWE-bench Verified, LiveCodeBench, Terminal-Bench, AIME, MMLU-Pro, Humanity's Last Exam, ARC-AGI-2, and Aider Polyglot became more visible.

The third channel was targeted search for underserved capabilities. This was where the most useful gap evidence appeared. WritingBench, HelloBench, LongBench-Write, EQ-Bench, and Suri were relevant to C01. MathDial, Bridge, MRBench, MathTutorBench, and KMP-Bench were relevant to C04. CriticBench, CritiqueLLM, Auto-J, UltraCM, Shepherd, and MetaCritique were relevant to C05. PingPong, RoleBench, CharacterEval, PersonaGym, InCharacter, and related benchmarks were relevant to C08.

The fourth channel was live leaderboards and evaluation platforms. I scanned HELM, Open LLM Leaderboard v2, LMSYS Chatbot Arena, LiveBench, SWE-bench, BigCodeBench, MTEB, Artificial Analysis, and Vellum. These platforms confirmed the same pattern: coding and knowledge benchmarks are highly visible, while writing quality, tutoring, review, and roleplay are either missing or only partially represented.

## First Shortlist

The first shortlist contained 18 benchmarks. For C02, I selected HumanEval/HumanEval+, MBPP/MBPP+, SWE-bench Verified, LiveCodeBench, and BigCodeBench Hard. For C01, I selected IFEval, WritingBench, EQ-Bench Creative Writing v3 plus Longform Writing, and HelloBench/LongBench-Write. For C04, I selected MathDial, MRBench, and MathTutorBench. For C03, I selected MMLU/MMLU-Pro, GPQA Diamond, TriviaQA/Natural Questions, and SimpleQA/FACTS Grounding. For C05, I selected CriticBench and a grouped Auto-J, Shepherd, and MetaCritique entry.

This first shortlist was useful because it fit the supervisor's 15 to 20 benchmark scope, but it also had limitations. It dropped C07, C06, and C08, which later became difficult to justify after the Phase 1 taxonomy revision. It also retained some older or weaker benchmarks that were later replaced.

## Initial Coverage Interpretation

The first inventory suggested that the benchmark gap is structural rather than purely quantitative. There are many benchmarks, but they often measure the wrong construct for real user tasks. STEM problem solving is used as a proxy for learning, even though tutoring requires pedagogy. IFEval is used as a proxy for writing quality, even though it mainly tests constraint following. Debugging and coding benchmarks are sometimes treated as review benchmarks, even though they do not represent prose review, grading, or feedback.

This first pass gave me the foundation for the later Phase 2 revisions. It showed where the field already has consensus benchmarks and where the relevant benchmarks exist but have not been absorbed into frontier reporting practice.
