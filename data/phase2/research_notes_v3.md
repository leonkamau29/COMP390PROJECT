<!-- markdownlint-disable MD013 -->

# Benchmark Selection Rationale v3

This version is my final research-note record of the Phase 2 alternatives review. It updates the v2 inventory by replacing saturated, superseded, or narrow benchmarks with stronger alternatives. The final version contains 28 benchmarks across all eight taxonomy capabilities.

## Selection Criteria

I kept the same basic criteria as in earlier versions. A benchmark needed to be publicly documented, relevant to at least one Phase 1 capability, and either adopted by multiple labs or useful as evidence for an underserved benchmark gap. I used this flexible interpretation because the absence of certain benchmarks from frontier reports is part of the project's argument.

The final count of 28 exceeds the original 15 to 20 benchmark cap. I treat this as a documented scope revision rather than an accidental expansion. The Phase 1 taxonomy covers eight capabilities, and the alternatives review showed that several weaker entries had to be replaced, not simply removed. If a strict cap is later required, I can trim the list while keeping at least minimal coverage for all eight capabilities.

## What Changed from v2

The main change was that I stopped treating legacy or saturated benchmarks as primary evidence where stronger options were available. HumanEval and HumanEval+ were demoted to a legacy historical anchor. MBPP and MBPP+ were removed from the primary inventory. HelloBench and LongBench-Write were replaced by WildBench because WildBench has stronger real-user grounding and better alignment with this project's usage-log methodology.

For C03, I replaced TriviaQA and Natural Questions because they are effectively solved and less useful for frontier comparison. Humanity's Last Exam and LiveBench provided stronger current evidence. For C07, I replaced QRData, Text2Analysis, and READoc because InfiAgent-DABench, DA-Code, Spider 2.0, and MMLongBench-Doc gave broader and more current coverage. For C04, I replaced MRBench with TutorBench because TutorBench is broader, multimodal, and multi-subject. For C05, I replaced the older Auto-J, Shepherd, and MetaCritique grouping with JudgeBench and RewardBench 2. For C08, I replaced FIREBALL with CoSER. For C06, I replaced Multi-IF with WMT24++.

## Final Capability Coverage

For C02, the final set is HumanEval/HumanEval+ as B001, SWE-bench Verified as B002, LiveCodeBench as B003, BigCodeBench Hard as B004, and SWE-Lancer Diamond as B005. This gives the coding capability a historical anchor, a repository-repair benchmark, a contamination-resistant benchmark, a library-integration benchmark, and an economic-value benchmark.

For C03, the final set is MMLU-Pro as B006, GPQA Diamond as B007, Humanity's Last Exam as B008, SimpleQA/FACTS Grounding as B009, and LiveBench as B010. This gives the advisory and factual capability broad knowledge coverage, expert reasoning coverage, frontier knowledge difficulty, hallucination measurement, and dynamic contamination-limited evaluation.

For C01, the final set is IFEval as B011, WritingBench as B012, EQ-Bench Creative Writing v3 as B013, and WildBench as B014. This combination lets me compare the proxy benchmark that labs actually cite with more direct writing and real-user task benchmarks.

For C07, the final set is InfiAgent-DABench as B015, DA-Code as B016, Spider 2.0 as B017, and MMLongBench-Doc as B018. This covers CSV analysis, executable data-science workflows, enterprise SQL and BI, and long multimodal document understanding.

For C04, the final set is MathDial as B019, MathTutorBench as B020, and TutorBench as B021. This captures tutoring dialogue, pedagogical sub-skill evaluation, and broader multisubject tutoring.

For C05, the final set is CriticBench as B022, JudgeBench as B023, and RewardBench 2 as B024. This covers critique-and-correct tasks, objective judge calibration, and reward-model-based feedback quality.

For C08, the final set is PingPong as B025 and CoSER as B026. This gives roleplay and conversational interaction two dedicated anchors: dynamic user-simulated roleplay and large-scale authentic character roleplay.

For C06, the final set is BenchMAX as B027 and WMT24++ as B028. BenchMAX covers multilingual capability broadly, while WMT24++ covers translation quality across a much wider language set.

## Trimming Protocol

If I need to return to a hard cap of 20 benchmarks, I would drop lower-priority or supplementary entries while preserving coverage across all eight capabilities. The first candidate to drop is HumanEval+ because it is already demoted to legacy status. Next would be LiveBench, RewardBench 2, WildBench, DA-Code, TutorBench, WMT24++, and CoSER. Dropping these eight entries would leave exactly 20 benchmarks while keeping every capability represented.

## Pre-Phase 3 Assessment

My pre-Phase 3 judgement is that C02 and C03 are the most benchmarked capabilities, but this does not mean they are perfectly evaluated. C01 is still proxy-dominated because IFEval receives more frontier attention than richer writing benchmarks. C07 has stronger coverage after the alternatives review, but still weak frontier-report visibility. C04 has useful new benchmarks, but mainstream reports still treat knowledge and maths-solving as proxies for teaching. C05, C08, and C06 remain the clearest examples of benchmark underrepresentation.

The final Phase 3 analysis should therefore test not just whether a benchmark exists, but whether it measures the capability at the right level of realism, scoring reliability, and construct validity.

## References

The main references carried into the final set include Jimenez et al. (2024), Miserendino et al. (2025), Phan et al. (2025), White et al. (2024), Lin et al. (2024), Hu et al. (2024), Huang et al. (2024), Lei et al. (2024), Ma et al. (2024), Macina et al. (2025), Srinivasa et al. (2025), Tan et al. (2024), Malik and Lambert et al. (2025), Wang et al. (2025), Deutsch and Freitag et al. (2025), Huang et al. (2025), and Gusev (2024).
