<!-- markdownlint-disable MD013 -->

# Benchmark Selection Rationale v2

This version records the second major revision of the Phase 2 benchmark rationale. I updated the inventory to reflect the Phase 1 final taxonomy and the February 2026 Anthropic AEI data. The main change from v1 was that I expanded beyond the original five-capability scope and added coverage for C07 Data Analysis and Summarisation, C06 Translation and Language Processing, and C08 Conversational Interaction and Roleplay.

## Criteria and Scope

I kept three selection criteria. Each benchmark needed public documentation, either multi-lab adoption or strong gap-evidence value, and alignment with at least one Phase 1 capability. At this stage the list reached 25 benchmarks across all eight capabilities. This exceeded the original 15 to 20 cap, but I treated it as a documented scope revision because the taxonomy itself had expanded.

The Phase 1 distribution I used placed C02 first at 34.0 percent of the top 103 tasks, followed by C03 at 21.4 percent, C01 at 17.5 percent, C07 at 10.7 percent, C04 at 7.8 percent, C05 at 3.9 percent, C08 at 2.9 percent, and C06 at 1.9 percent. This made it hard to justify omitting C07, and it also meant that C06 and C08 needed at least minimum benchmark coverage.

## Inclusion Decisions

For C02, I retained HumanEval/HumanEval+, MBPP/MBPP+, SWE-bench Verified, LiveCodeBench, and BigCodeBench Hard. At this stage, HumanEval and MBPP were still included as controlled baselines, even though I already recognised their saturation. SWE-bench Verified represented repository-level issue resolution, LiveCodeBench represented contamination-resistant coding, and BigCodeBench Hard represented library and tool integration.

For C01, I retained IFEval, WritingBench, EQ-Bench Creative Writing v3 plus Longform Writing, and HelloBench/LongBench-Write. IFEval represented the consensus proxy used by labs, while WritingBench and EQ-Bench represented more direct writing-quality evaluation. HelloBench and LongBench-Write were included at this stage to cover long-form generation, although they were later replaced.

For C03, I retained MMLU/MMLU-Pro, GPQA Diamond, TriviaQA/Natural Questions, and SimpleQA/FACTS Grounding. The logic was to combine broad knowledge, frontier expert reasoning, historical open-domain QA, and hallucination or grounding measurement. This later changed because TriviaQA and Natural Questions were too old and saturated for the final list.

For C04, I retained MathDial, MRBench, and MathTutorBench. These were selected because they treat tutoring as a pedagogical task rather than merely a question-answering task. MathDial was the foundational dialogue benchmark, MRBench provided pedagogical dimensions, and MathTutorBench offered a more comprehensive reward-model-based tutoring evaluation.

For C05, I retained CriticBench and a grouped Auto-J, Shepherd, and MetaCritique entry. CriticBench was the strongest critique-and-correct anchor, while the grouped entry represented open-ended critique and feedback work. This grouping was later replaced because newer benchmarks gave stronger coverage.

For C07, I added QRData, Text2Analysis, and READoc. QRData covered data-based statistical and causal reasoning, Text2Analysis covered ambiguous tabular analysis and business-intelligence-style queries, and READoc covered document structured extraction. These were important additions because C07 had risen to 10.7 percent usage, but they were later replaced by stronger alternatives.

For C06, I added BenchMAX and Multi-IF. BenchMAX covered multilingual capability across languages and tasks, while Multi-IF extended instruction following into multilingual and multi-turn settings. Multi-IF was later replaced by WMT24++ because the final inventory needed stronger translation-quality coverage.

For C08, I added PingPong and FIREBALL. PingPong covered dynamic roleplay with user simulation, while FIREBALL covered Dungeons and Dragons actual-play data with structured game state. FIREBALL was later replaced by CoSER because CoSER was broader and more recent.

## Provisional Coverage Assessment

At the v2 stage, I viewed C02 and C03 as comparatively well covered, although both had saturation risks. C01 was partially covered because the most visible lab benchmark was still IFEval, a proxy rather than a full writing-quality benchmark. C07 and C04 were minimally covered because relevant benchmarks existed but had weak frontier-report presence. C05, C08, and C06 were critically underserved because their dedicated benchmarks were mostly absent from major technical reports.

This version was useful because it forced the inventory to match the full taxonomy. Its weakness was that some entries were still legacy, narrow, or superseded. That weakness led directly to the v3 alternatives review.

## References

The new references introduced or emphasised in this version included Liu et al. (2024) for QRData, He et al. (2024) for Text2Analysis, Li et al. (2025) for READoc, Huang et al. (2025) for BenchMAX, Xu et al. (2024) for Multi-IF, Gusev (2024) for PingPong, and Zhu et al. (2023) for FIREBALL.
