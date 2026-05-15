# Phase 2 Benchmark Inventory Report

**Project:** *Benchmark Coverage Gap — A Systematic Analysis of Real-World AI Capabilities and Evaluation Practices*
**Researcher:** Leon Kamau Kiunga (201759400) 
**Phase:** 2 — Benchmark Inventory (Weeks 5–9)

---

## Executive summary and headline findings

Phase 2 inventories roughly **120 candidate LLM benchmarks** across four sourcing channels and narrows them to a shortlist of **18 benchmarks covering the empirically dominant five capabilities**: C02 Code, C01 Content Generation, C04 Learning & Education Support, C03 Information Retrieval & Advisory, and C05 Review & Feedback. **The researcher's prior capability ranking (C02, C05, C03, C07, C01) is only partly supported by Handa et al. (2025): C01 is strongly under-estimated and C04 is missing entirely, while C07 drops out of the top five.** The strongest conclusion from the inventory itself is that benchmark supply is extreme concentrated on C02 and on factual/STEM reasoning (a proxy for C03/C04-as-solver), while real-world-dominant capabilities such as **open-ended content generation, pedagogical tutoring, artefact review, and persona-consistent dialogue have essentially no presence in frontier model technical reports**. This asymmetry — not a shortage of benchmarks, but a coverage gap concentrated in exactly the capabilities most heavily used — is the empirical spine on which Phase 3 should build.

---

## Step 1 — Top capabilities by real-world usage

### Evidence base

Handa et al. (2025), *Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations* (arXiv:2503.04761), analysed approximately **four million Claude.ai Free + Pro conversations** from December 2024 – January 2025 using the Clio privacy-preserving classifier. Conversations were tagged against O*NET occupational tasks (rolled up to Standard Occupational Classification major groups), the 35-skill O*NET skills taxonomy, and a five-mode collaboration taxonomy (Directive, Feedback Loop, Task Iteration, Learning, Validation). Four subsequent Anthropic Economic Index waves (V2 March 2025, V3 September 2025, V4 January 2026, V5 March 2026) update these figures; the ordering of the top categories is stable across all five waves.

### Observed category shares (Handa V1)

| Rank | SOC major category                          | Share of conversations | Representative tasks                             |
| ---- | ------------------------------------------- | ---------------------- | ------------------------------------------------ |
| 1    | Computer & Mathematical                     | **37.2%**        | Code writing, debugging, network troubleshooting |
| 2    | Arts, Design, Entertainment, Sports & Media | **10.3%**        | Writing and editing, creative writing            |
| 3    | Education, Instruction & Library            | **9.3%**         | Tutoring, explanations, instructional materials  |
| 4    | Office & Administrative Support             | **7.9%**         | Document drafting, formatting                    |
| 5    | Life, Physical & Social Science             | **6.4%**         | Research assistance, analysis                    |
| 6    | Business & Financial Operations             | **5.9%**         | Business/financial analysis and writing          |

Interaction-type shares (orthogonal): **Task Iteration 31.3%, Directive 27.8%, Learning 23.3%, Feedback Loop 14.8%, Validation 2.8%.** The paper states explicitly that "the vast majority of Feedback Loop conversations were coding and debugging," consolidating coding's dominance.

### Mapping Handa categories → C01–C08 (transparent)

| Handa category                                             | Primary C0x   | Secondary                     | Notes                                                                           |
| ---------------------------------------------------------- | ------------- | ----------------------------- | ------------------------------------------------------------------------------- |
| Computer & Mathematical (37.2%)                            | **C02** | C03, C05 (debugging = review) | Debugging overlaps review of an existing artefact.                              |
| Arts/Media (10.3%)                                         | **C01** | C05                           | Paper describes as "writing and editing" — roughly 2/3 generative, 1/3 review. |
| Education/Library (9.3%)                                   | **C04** | C01, C03                      | Tutoring + making instructional content.                                        |
| Office/Admin (7.9%)                                        | **C01** | C07, C05                      | Drafting emails, memos, formatting.                                             |
| Life/Physical/Social Science (6.4%)                        | **C03** | C07, C04                      | Research help, literature synthesis.                                            |
| Business/Financial (5.9%)                                  | **C07** | C03, C01                      | Financial/business analysis.                                                    |
| Management, Healthcare advisory, Legal advisory (residual) | **C03** | C04                           | Advice/information requests.                                                    |

### Empirically-supported top-five capabilities

| Rank | Capability                                                 | Estimated share | Source of weight                                                                          |
| ---- | ---------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------------- |
| 1    | **C02 Code Development & Technical Problem Solving** | ~37–42%        | 37.2% Computer & Math + most of the 14.8% Feedback-Loop interactions                      |
| 2    | **C01 Content Generation**                           | ~15–20%        | ~2/3 of Arts/Media + most of Office/Admin + portion of Management/Business writing        |
| 3    | **C04 Learning & Education Support**                 | ~10–14%        | 9.3% Education SOC + portion of the 23.3% Learning interactions cutting across categories |
| 4    | **C03 Information Retrieval & Advisory**             | ~9–12%         | Life/Science (6.4%) + advisory portion of Management, Healthcare, Legal                   |
| 5    | **C05 Review & Feedback**                            | ~7–10%         | Validation (2.8%) + review share of Arts/Media + debugging-as-review within coding        |

C07 Data Analysis (~5–7%), C06 Translation (~1–3%), and C08 Conversational/Roleplay (<3% in this filtered sample) fall outside the top five.

### Verdict on the researcher's prior (C02, C05, C03, C07, C01)

The prior was partially correct: **C02 is confirmed as #1 by a very wide margin**, and C03 and C05 both belong in the top five. But two revisions are required. First, **C01 was strongly under-ranked** — writing is the second-largest real-world cluster, not the fifth. Second, **C04 was missing from the prior entirely**, yet empirically ranks third and has been the fastest-growing category across the five Index waves (9.3% → ~13% between January 2025 and February 2026, tracking the launch of Claude for Education). C07 should be dropped from the top five; it can still be included as an honourable-mention secondary capability for benchmark coverage purposes, but it does not merit a dedicated slot under the 15–20 benchmark scope cap.

**Recommended Phase 2 capability scope:** C02, C01, C04, C03, C05 (five capabilities — the upper end of the 4–5 range).

---

## Step 2 — Benchmark inventory across four channels

### Channel 1: Papers with Code

An important context note: Papers with Code was **sunsetted by Meta on 24–25 July 2025** and its leaderboards are no longer maintained; the domain now redirects to Hugging Face's Trending Papers. Historical snapshots, cached search data, and NLP-progress (Sebastian Ruder) were used to reconstruct its task-level benchmark inventory. The site's main NLP task clusters yielded the following principal benchmarks: **HumanEval, MBPP, APPS, DS-1000, CodeContests, SWE-bench, BigCodeBench, LiveCodeBench** (C02); **SQuAD 1.1/2.0, RACE, NewsQA, TriviaQA, NarrativeQA, TruthfulQA, DROP, HotpotQA, StrategyQA, CoQA, MLQA** (C03); **HellaSwag, WinoGrande, PIQA, SocialIQa, CommonsenseQA, ARC-C/E, OpenBookQA, BoolQ** (C03 reasoning); **GSM8K, MATH, GSM8K-Platinum, MultiArith, GSM-PLUS** (C04 math-as-proxy); **MMLU, MMLU-Pro, GLUE, SuperGLUE** (C03); **WMT14/16/18/20, FLORES-101/200, Europarl** (C06); **CNN/DailyMail, XSum, Gigaword, PubMed, arXiv, BigPatent, BillSum, SAMSum, Multi-News, WikiHow** (C07); **PersonaChat/ConvAI2, Wizard of Wikipedia, EmpatheticDialog, DailyDialog** (C08); **CoNLL-2014 GEC, JFLEG, BEA-2019** (C05 proxy).

### Channel 2: Frontier model technical reports

Reports examined: GPT-4 (2023), GPT-4o system card (2024), Claude 3 model card (March 2024), Claude 3.5 Sonnet addendum (June/October 2024), Claude 4 family (Opus/Sonnet/4.1/4.5, 2025), Gemini 1.0 (December 2023), Gemini 1.5 Pro/Flash (2024), Gemini 2.0/2.5 (2024–2025), Llama 3 and 3.1 (2024), Llama 4 (April 2025).

**Cross-lab consensus (benchmarks appearing in ≥3 frontier release tables):** MMLU, Multilingual MMLU, GPQA Diamond, BIG-Bench Hard, ARC-C, HellaSwag, WinoGrande, GSM8K, MATH, MGSM, HumanEval, MBPP(+), DROP, IFEval, TruthfulQA, MMMU, MathVista, ChartQA, Needle-in-a-Haystack.

**Frontier-only consensus (Claude 4 / Gemini 2.5 / Llama 4 headlines, 2025):** SWE-bench Verified, LiveCodeBench, Terminal-Bench, TAU-bench / τ²-Bench, AIME 2024/2025, MMLU-Pro, Humanity's Last Exam, ARC-AGI-2, Aider Polyglot.

**Single-lab signatures:** Google reports translation heavily (Flores, WMT23, XLSum, Indic-GenBench, MTOB Kalamang); Llama 3 reports BFCL/Nexus/API-Bank function-calling; Claude reports OSWorld computer-use; Anthropic alone reports internal bias suites (Winogender, Winobias, BBQ).

**Capability coverage in technical reports:**

| Capability                        | Distinct benchmarks in frontier reports                  | Verdict                              |
| --------------------------------- | -------------------------------------------------------- | ------------------------------------ |
| C01 Content Generation            | ~2 (IFEval/IFBench, MT-Bench) — both proxies            | **Major gap**                  |
| C02 Code                          | 10+                                                      | Saturated                            |
| C03 Factual QA / knowledge        | 15+                                                      | Saturated                            |
| C04 Tutoring                      | 0 (math-solving ≠ teaching); ~6 math-solving benchmarks | **Major gap on pedagogy**      |
| C05 Review & Feedback             | 0                                                        | **Major gap**                  |
| C06 Translation                   | ~6 (Google-heavy)                                        | Moderate, lab-dependent              |
| C07 Data Analysis & Summarisation | ~6 retrieval-focused, ~0 summarisation-quality           | Moderate gap                         |
| C08 Conversational & Roleplay     | ~2 narrow (TAU-bench variants)                           | **Major gap on open roleplay** |

### Channel 3: LLM evaluation surveys and the underserved-capability search

Because a broader survey-harvest subagent hit context-window limits, under-served capability benchmarks were collected through targeted search. The strongest results came from the literature, not from leaderboards.

**C01 creative/long-form generation benchmarks (none in frontier reports):** **WritingBench** (Shao et al., NeurIPS 2025; 1,239 queries across 6 domains and 100 subdomains with a query-dependent critic model), **HelloBench** (Que et al., 2024; long-form text generation, task-specific dimensions), **LongBench-Write** (Bai et al., 2024; six fixed dimensions), **EQ-Bench Creative Writing v3 and Longform Writing** (Paech, live on eqbench.com; LLM-judged with Elo + rubric, evaluates humour, romance, spatial awareness, character voice), **Suri** (Pham et al., EMNLP 2024; multi-constraint long-form following).

**C04 tutoring/pedagogy benchmarks:** **MathDial** (Macina et al., EMNLP 2023; 2,900 student–tutor dialogues over GSM8K problems), **Bridge** (Wang et al., 2024; elementary-school remediation with novice vs expert tutor responses), **MRBench** (Maurya et al., NAACL 2025; 192 dialogues × 7 LLM tutors × 8 pedagogical dimensions using the Desired Annotation Match Rate metric), **MathTutorBench** (Macina et al., 2025; seven pedagogical tasks including scaffolding, mistake localisation, pedagogy-following with a reward model), **KMP-Bench** (2026; covers follow-up questioning, confusion clarification, and practice-problem generation beyond remediation).

**C05 critique/review benchmarks:** **CriticBench (Tsinghua, Lin et al., ACL 2024 Findings)** — 15 datasets across math, commonsense, symbolic, code and algorithmic critique-and-correct; **CriticBench (Tencent, Lan et al., 2024)** — 3K queries, nine tasks including CodeExec; **CritiqueLLM** (Ke et al., 2024; scaling critique with LLM-as-critic evaluation); **Auto-J** (Li et al., 2024) and **UltraCM** (Cui et al., 2023) — critique-tuned model benchmarks; **Shepherd** (Wang et al., 2023); **MetaCritique** (Sun et al., 2024).

**C07 summarisation-quality benchmarks (for honourable-mention coverage):** **SummEval, SummHay, BookSum, GovReport, Multi-News, FABLES.**

**C08 roleplay benchmarks:** **RoleLLM/RoleBench** (Wang et al., ACL 2024 Findings), **CharacterEval** (Tu et al., ACL 2024; Chinese), **PingPong** (Gusev, 2024; dynamic multi-turn with user-simulator, 40+ models, character consistency/entertainment/fluency), **PersonaGym** (Samuel et al., 2024), **InCharacter, ECHO, TimeChara, CharacterBox, RPEval, RPBench-Auto, RVBench.** None appears in any frontier release table.

### Channel 4: Leaderboards and evaluation platforms

Platforms scanned (access date 17 April 2026): **HELM** (Classic, Lite, Instruct, Safety v1.0, Capabilities v1.0, MMLU, MedHELM, VHELM, FinanceBench), **Open LLM Leaderboard v2** (6 benchmarks — IFEval, BBH, MATH Lvl 5, GPQA, MuSR, MMLU-Pro), **LMSYS Chatbot Arena** (pairwise human preference with category sub-leaderboards including Creative Writing and Roleplay, plus MT-Bench and Arena-Hard-Auto derivatives), **LiveBench** (six monthly-rotated categories), **SWE-bench leaderboard** (Full / Lite / Verified / Multimodal / Multilingual), **BigCodeBench** (Complete / Instruct / Hard), **MTEB / MMTEB**, **Artificial Analysis Intelligence Index v3** (MMLU-Pro, HLE, AA-LCR, GPQA Diamond, AIME, IFBench, SciCode, LiveCodeBench, Terminal-Bench Hard, τ²-Bench Telecom), **Vellum LLM Leaderboard** (GPQA Diamond, AIME 2025, MATH-500, SWE-bench Verified, LiveCodeBench, HLE, ARC-AGI 2, MMMLU, BFCL).

**Top consensus benchmarks (≥3 leaderboards):** MMLU-Pro, GPQA Diamond, IFEval, MATH/MATH-500, AIME, SWE-bench Verified, LiveCodeBench, Humanity's Last Exam, Chatbot Arena Elo.

**Leaderboard coverage by capability:** C02 ~10, C03 ~15, C04 (math-as-proxy) ~10, C07 ~6, C08 ~5 (mostly Arena-derived), C01 ~4, C06 ~3 (WMT-2014 is twelve years old), **C05 ~3** (IMDB sentiment, CivilComments, MTEB Classification — none modern). LMSYS Arena's Creative-Writing and Roleplay sub-category leaderboards are the only live, widely-cited public trackers for C01 and C08 respectively, and Arena scores are not decomposable into the C0x taxonomy without access to the raw battle data.

---

## Final Phase 2 shortlist — 18 benchmarks across five capabilities

The shortlist balances three criteria: cross-lab/cross-platform consensus (so the thesis can credibly claim the benchmarks are "what the field tests"), coverage of underserved capabilities (so the coverage-gap argument rests on live, defensible alternatives), and diversity of format (multiple-choice, open-ended generation with LLM-as-judge, agentic, multi-turn). Publication dates, formats, and status are reconciled against primary sources.

| #  | Benchmark                                                 | Year           | Format                                                              | Primary C0x | Rationale for inclusion                                                                       |
| -- | --------------------------------------------------------- | -------------- | ------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------- |
| 1  | **HumanEval / HumanEval+**                          | 2021 / 2023    | pass@k, 164 Python problems                                         | C02         | Most-cited code benchmark, acknowledged saturated — a controlled "baseline"                  |
| 2  | **MBPP / MBPP+ (EvalPlus)**                         | 2021 / 2023    | pass@k, ~974 problems                                               | C02         | Broader Python coverage than HumanEval                                                        |
| 3  | **SWE-bench Verified**                              | 2024           | Agentic patch-gen, 500 human-verified GitHub issues                 | C02         | De-facto agentic-coding standard; exposes the HumanEval→real-software gap                    |
| 4  | **LiveCodeBench**                                   | 2023–         | Contamination-limited code gen, monthly refresh                     | C02         | Addresses contamination; Claude 4, Gemini 2.5, Llama 4 all cite it                            |
| 5  | **BigCodeBench (Hard)**                             | 2024           | 148 library-integration tasks                                       | C02         | Richer than HumanEval; measures library and tool use                                          |
| 6  | **IFEval**                                          | 2023           | Verifiable constraint-following, generated text                     | C01         | The only C01 benchmark with cross-lab consensus — surfaces the proxy problem                 |
| 7  | **WritingBench**                                    | 2025 (NeurIPS) | 1,239 queries, query-dependent critic                               | C01         | Covers creative, persuasive, informative and technical writing; addresses the C01 gap head-on |
| 8  | **EQ-Bench Creative Writing v3 + Longform Writing** | 2023–         | LLM-judged, Elo + rubric, live leaderboard                          | C01         | Captures style/voice dimensions; has an active public leaderboard                             |
| 9  | **HelloBench / LongBench-Write**                    | 2024           | Long-form generation with task-specific dimensions                  | C01         | Closes the "single-sentence prompt" limitation of older writing tests                         |
| 10 | **MathDial**                                        | 2023           | 2,900 tutoring dialogues                                            | C04         | Foundational tutoring-dialogue dataset, grounds subsequent work                               |
| 11 | **MRBench**                                         | 2025 (NAACL)   | 192 dialogues × 7 models × 8 pedagogical dimensions               | C04         | Explicit pedagogical taxonomy (Desired Annotation Match Rate)                                 |
| 12 | **MathTutorBench**                                  | 2025           | 7 tasks incl. scaffolding, mistake localisation, pedagogy-following | C04         | The first benchmark with a pedagogy reward model and public leaderboard                       |
| 13 | **MMLU / MMLU-Pro**                                 | 2020 / 2024    | 57/14-subject multiple-choice                                       | C03         | Universal factual-knowledge benchmark; MMLU-Pro is the contamination-resistant update         |
| 14 | **GPQA Diamond**                                    | 2023           | Graduate-level science MCQ, gated                                   | C03         | Replaced MMLU at the frontier; on every major release table                                   |
| 15 | **TriviaQA / Natural Questions**                    | 2017 / 2019    | Open-domain short-answer QA                                         | C03         | Classic open-domain retrieval/QA; still cited by Llama 3 and Gemini 1.5                       |
| 16 | **SimpleQA / FACTS Grounding**                      | 2024 / 2024    | Short-form factual QA, grounding                                    | C03         | Directly measure hallucination, Google/OpenAI respectively                                    |
| 17 | **CriticBench (Tsinghua, 2024)**                    | 2024           | 15 datasets, 5 reasoning domains, critique-and-correct              | C05         | The most comprehensive C05 benchmark; only critique benchmark with cross-reasoning coverage   |
| 18 | **Auto-J + Shepherd + MetaCritique** (grouped)      | 2023–2024     | Critique-tuned model evaluations with human-annotated references    | C05         | Complement CriticBench by covering open-ended critique tasks (essay feedback, code review)    |

This gives **five benchmarks for C02, four for C01, three for C04, four for C03, and two for C05** — matching the empirically dominant capability order (C02 > C01 > C04 > C03 > C05) with a benchmark count that loosely mirrors real-world prevalence, except deliberately *inverted* for C05 to let the thesis expose the asymmetry.

### Adjustments from the researcher's prior

The 18-benchmark shortlist drops C07 and makes room for C04 in line with the empirical evidence. Should Dr Tsakaldis prefer to retain C07, a natural 20-benchmark variant would add **SummEval** (generic summarisation quality, Fabbri et al.) and **FABLES** (Kim et al., 2024; long-document narrative faithfulness) in slots 19–20, covering C07 at minimum viability without displacing C04 or C05.

---

## What the inventory reveals about the coverage gap

### The gap is not quantitative — it is structural

The academic community has published well over a hundred LLM benchmarks; the shortlist above selects from an inventory of ~120 and leaves many reasonable alternatives on the cutting-room floor. The coverage gap emerges only when benchmarks are grouped by *what they actually measure* against *what users actually do*. **Three structural mismatches stand out.**

**First, industry benchmarks over-weight STEM problem-solving as a proxy for everything reasoning-adjacent.** Every frontier release table in 2025 included GPQA, AIME, and at least one of MATH-500 or Omni-MATH; not one included a benchmark whose task is to *teach* a student to solve those problems. C04 in Handa et al. is about learning support — yet the field evaluates C04 using the model's own solving skill, which MathTutorBench shows is *negatively* correlated with tutoring ability once pedagogical specialisation is introduced (stronger solvers are often worse teachers).

**Second, C01 and C05 are measured almost exclusively by proxies.** IFEval and MT-Bench are the only C01 benchmarks in any 2025 frontier release table, and both measure short-prompt constraint-following rather than the quality of a 500-word memo or a marketing brief. For C05, frontier reports cite *zero* benchmarks — debugging performance on SWE-bench is treated as the implicit proxy, even though it conflates fault-localisation (genuinely C05) with patch generation (C02). Meanwhile, real benchmarks exist: WritingBench (2025) and CriticBench (2024) both have live results but are absent from every frontier-model technical report reviewed.

**Third, the benchmarks that *do* exist for underserved capabilities are younger, smaller, and judge-dependent.** WritingBench, MathTutorBench, CriticBench, PingPong and MRBench were all published 2023–2025, all use LLM-as-judge or trained critic models rather than string-match metrics, and none has achieved the multi-lab citation pattern enjoyed by HumanEval or MMLU. This creates a self-reinforcing cycle: labs cite what other labs cite, so judge-based benchmarks for subjective capabilities get stranded outside the consensus even when they measure the capabilities users actually exercise.

### Implications for Phase 3

Phase 3 (content analysis of the 18 benchmarks) should foreground three coding dimensions: *what task the benchmark literally asks the model to do*, *what evaluation signal it uses* (pass/fail unit test, string match, MCQ, LLM-judge rubric, human preference), and *the minimum unit of model output* (token, sentence, function, document). Cross-tabulating these against the Handa interaction types (Directive, Task Iteration, Learning, Feedback Loop, Validation) should generate the paper's central figure: a matrix showing where benchmark supply and real-world demand diverge. The prediction — verifiable in Phase 3 — is that Directive and Feedback-Loop interactions are well covered (because SWE-bench and HumanEval map onto them), while Task Iteration, Learning and Validation interactions are systematically under-measured despite being 57% of all Claude use.

---

## Conclusion

Phase 2 closes with three decisions locked in and one open for supervisor review. The locked decisions: (a) the top-five capabilities are **C02, C01, C04, C03, C05**, replacing the original prior's C07 with C04 and elevating C01 into the number-two slot; (b) the shortlist comprises **18 benchmarks** within the 15–20 scope cap, with explicit provisions to expand to 20 if C07 coverage is desired; (c) the inventory confirms that the benchmark coverage gap is a problem of *structure*, not *quantity*, concentrated on C01 creative generation, C04 pedagogy, C05 critique, and open-ended C08 roleplay. The open decision is whether the thesis should treat the emerging C01/C04/C05 benchmarks (WritingBench, MathTutorBench, CriticBench) as solutions to the gap or as further evidence of the gap's depth — a framing question best resolved once Phase 3 content coding begins and the evaluation-signal patterns become quantitatively visible.
