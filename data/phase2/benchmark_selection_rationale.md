# Benchmark Selection Rationale

This document explains why I selected the final Phase 2 benchmark inventory. The version reflects the Phase 1 final taxonomy, the February 2026 Anthropic AEI update, and the alternatives review that replaced weaker or more saturated benchmarks with stronger recent ones.

## Selection Criteria

I used three selection criteria. First, a benchmark had to be publicly documented through a paper, technical report, conference proceeding, official benchmark page, or equivalent source. Second, it needed either multi-lab adoption or a clear role in demonstrating an underserved capability gap. I allowed this second criterion to be flexible because some of the most relevant gap benchmarks are absent from frontier reports, and that absence is itself part of the evidence. Third, each benchmark had to align with at least one capability from the Phase 1 taxonomy.

The final inventory exceeds the original 15 to 20 benchmark target. I made this choice because the final taxonomy contains eight capabilities, not only the original four or five focus areas. If I removed C06, C07, or C08 entirely, the benchmark inventory would no longer match the taxonomy. I therefore treat the 28-benchmark list as a documented scope revision that can still be trimmed if a strict cap is required.

## Capability Scope

The capability scope is driven by the Phase 1 taxonomy and the top 103 Anthropic AEI tasks. The distribution I used is C02 at 34.0 percent, C03 at 21.4 percent, C01 at 17.5 percent, C07 at 10.7 percent, C04 at 7.8 percent, C05 at 3.9 percent, C08 at 2.9 percent, and C06 at 1.9 percent.

The main revision from earlier Phase 2 work is that C07, C08, and C06 could no longer be ignored. C07 rose to 10.7 percent of the top tasks, C08 was small in AEI but much more visible in OpenRouter roleplay usage, and C06 remained a clearly distinct cross-lingual capability. I therefore expanded coverage to all eight capability areas.

The alternatives review also changed the benchmark set. I demoted HumanEval to a legacy anchor because it is saturated. I removed MBPP from the primary inventory for the same reason. I replaced HelloBench and LongBench-Write with WildBench because WildBench has stronger real-user grounding. I replaced TriviaQA and Natural Questions with Humanity's Last Exam and LiveBench because older QA benchmarks are now less discriminating. I replaced QRData, Text2Analysis, and READoc with InfiAgent-DABench, DA-Code, Spider 2.0, and MMLongBench-Doc to strengthen C07. I replaced MRBench with TutorBench, replaced Auto-J and related older critique benchmarks with JudgeBench and RewardBench 2, replaced FIREBALL with CoSER, and replaced Multi-IF with WMT24++.

## C02 Selection Rationale

I allocated five benchmarks to C02 because it is the largest real-world capability. HumanEval and HumanEval+ remain in the database as B001 because they show the historical baseline and saturation problem. SWE-bench Verified is B002 because it is the main current repository-level software engineering benchmark used in frontier reports. LiveCodeBench is B003 because it gives a regularly refreshed contamination-resistant coding signal. BigCodeBench Hard is B004 because it evaluates library and API integration. SWE-Lancer Diamond is B005 because it attaches software task completion to economic value and includes managerial judgement.

I excluded MBPP and MBPP+ because they are saturated in the same way as HumanEval. I also excluded APPS, CodeContests, Aider Polyglot, and Terminal-Bench from the primary set because the five selected benchmarks already cover the main C02 evidence needs within the inventory.

## C03 Selection Rationale

I allocated five benchmarks to C03 because it is the second-largest capability and because factual advisory tasks are central to benchmark use. MMLU-Pro is B006 because it is a stronger current version of the broad knowledge baseline. GPQA Diamond is B007 because it is the frontier expert-reasoning anchor. Humanity's Last Exam is B008 because it has become the new cross-lab frontier knowledge benchmark. SimpleQA and FACTS Grounding are B009 because they directly address factuality and grounded hallucination. LiveBench is B010 because it is dynamic, multi-domain, and contamination-limited.

I excluded older QA tasks such as TriviaQA, Natural Questions, SQuAD, HotpotQA, and DROP from the final primary set because they are either saturated, partially redundant, or less suited to current frontier model comparison.

## C01 Selection Rationale

I allocated four benchmarks to C01. IFEval is B011 because it is the one content-generation-adjacent benchmark that major labs consistently cite. WritingBench is B012 because it is the strongest direct measure of multi-domain writing quality. EQ-Bench Creative Writing v3 is B013 because it captures creative style and voice through an active public leaderboard. WildBench is B014 because it is grounded in real user prompts and therefore supports the project's usage-based methodology.

I excluded HelloBench and LongBench-Write because they had weaker adoption than WildBench. I also excluded MT-Bench, Suri, and IFBench because they were either hybrids, narrower variants, or partly redundant with the selected C01 benchmarks.

## C07 Selection Rationale

I allocated four benchmarks to C07 because the February 2026 AEI update raised data analysis and summarisation to 10.7 percent of the top tasks. InfiAgent-DABench is B015 because it is a canonical data-analysis benchmark over CSV files. DA-Code is B016 because it evaluates executable data-science workflows. Spider 2.0 is B017 because it covers enterprise SQL and BI workflows. MMLongBench-Doc is B018 because it covers long-context multimodal document understanding.

I replaced QRData, Text2Analysis, and READoc because the final set gives broader and stronger coverage. I excluded SummEval, FABLES, DS-1000, and TAT-QA because they were either too narrow or better handled under another capability boundary.

## C04 Selection Rationale

I allocated three benchmarks to C04. MathDial is B019 because it establishes tutoring dialogue as a distinct construct. MathTutorBench is B020 because it evaluates pedagogical sub-skills such as scaffolding and mistake localisation. TutorBench is B021 because it extends tutoring evaluation beyond mathematics into multi-subject and multimodal settings.

I excluded MRBench because TutorBench now covers a broader space. I also excluded Bridge and KMP-Bench from the final set because they are narrower or too new, and I treated maths-solving benchmarks such as GSM8K, MATH, and AIME as knowledge or reasoning proxies rather than tutoring benchmarks.

## C05 Selection Rationale

I allocated three benchmarks to C05 because review and feedback remain critically underserved in frontier reports. CriticBench from Tsinghua is B022 because it is the strongest critique-and-correct anchor. JudgeBench is B023 because it evaluates whether model judges can identify objective correctness in difficult comparisons. RewardBench 2 is B024 because reward-model evaluation is closely related to feedback quality and alignment.

I excluded older critique benchmark groupings such as Auto-J, Shepherd, and MetaCritique from the final primary inventory because JudgeBench and RewardBench 2 are more recent and methodologically stronger.

## C08 Selection Rationale

I allocated two benchmarks to C08. PingPong is B025 because it tests dynamic roleplay with user emulation and judge ensembles. CoSER is B026 because it is a broader and more recent roleplay benchmark based on a large set of authentic character conversations.

I excluded FIREBALL because it is more specific to Dungeons and Dragons gameplay. I also excluded broader dialogue benchmarks that do not isolate sustained roleplay or conversational interaction.

## C06 Selection Rationale

I allocated two benchmarks to C06. BenchMAX is B027 because it evaluates multilingual capability across 16 languages and multiple task types. WMT24++ is B028 because it gives strong translation-quality coverage across 55 languages and dialects.

I excluded Multi-IF because WMT24++ provides a stronger direct translation-quality signal, while BenchMAX covers broader multilingual capability. I also treated FLORES and standard MT metrics as relevant background but not the best fit for this LLM-focused benchmark inventory.

## Coverage Assessment Before Phase 3

Before the formal Phase 3 coverage matrix, my provisional assessment is that C02 and C03 are comparatively well covered, although both still have saturation and construct-validity issues. C01 is only partially covered because the field relies heavily on proxies such as instruction following. C07 and C04 are minimally covered by newer benchmarks but have weak frontier-report presence. C05, C08, and C06 are critically underserved in the sense that relevant benchmarks exist but are not central to major model evaluation practice.

The Phase 3 gap score formula will quantify this more formally as `Gap Score = Usage_Frequency x (1 - Normalized_Coverage_Score)`.

## References

Key references for the selected and replacement benchmarks include; Jimenez et al. (2024) for SWE-bench, Miserendino et al. (2025) for SWE-Lancer, Phan et al. (2025) for Humanity's Last Exam, White et al. (2024) for LiveBench, Lin et al. (2024) for WildBench, Hu et al. (2024) for InfiAgent-DABench, Huang et al. (2024) for DA-Code, Lei et al. (2024) for Spider 2.0, Ma et al. (2024) for MMLongBench-Doc, Macina et al. (2025) for MathTutorBench, Srinivasa et al. (2025) for TutorBench, Tan et al. (2024) for JudgeBench, Malik and Lambert et al. (2025) for RewardBench 2, Wang et al. (2025) for CoSER, Deutsch and Freitag et al. (2025) for WMT24++, Huang et al. (2025) for BenchMAX, and Gusev (2024) for PingPong.