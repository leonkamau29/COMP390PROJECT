# Benchmark Access Log

**Phase:** Phase 2, Weeks 6–8
**Researcher:** Leon Kamau Kiunga (201759400)

---

## Summary

All 18 shortlisted benchmarks were accessed during the inventory period (Weeks 6–8).
Primary access routes: arXiv (papers), GitHub (code/datasets), Hugging Face (datasets),
and official leaderboard websites. No paywalls blocked access to any primary paper.
One benchmark (GPQA Diamond) has gated dataset access by design; the paper and
evaluation protocol are fully public.

---

## Access Log by Benchmark

| Benchmark                             | Paper Access                                                                              | Dataset/Code Access                                                                                                                           | Issues                                                                                                                        | Resolution                                                                                                                      |
| ------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| B001 HumanEval / HumanEval+           | Full — arXiv:2107.03374; arXiv:2305.01210                                                | Full public — github.com/openai/human-eval; EvalPlus GitHub                                                                                  | None                                                                                                                          | N/A                                                                                                                             |
| B002 MBPP / MBPP+                     | Full — arXiv:2108.07732; arXiv:2305.01210                                                | Full public — Google Research GitHub; EvalPlus GitHub                                                                                        | None                                                                                                                          | N/A                                                                                                                             |
| B003 SWE-bench Verified               | Full — arXiv:2310.06770; OpenAI verification blog                                        | Full public — github.com/princeton-nlp/SWE-bench                                                                                             | Verified subset requires downloading from HuggingFace (swe-bench/verified)                                                    | Downloaded successfully; no access barrier                                                                                      |
| B004 LiveCodeBench                    | Full — arXiv:2403.07974                                                                  | Full public — github.com/LiveCodeBench/LiveCodeBench                                                                                         | Requires API keys for LeetCode problem scraping (for running fresh evaluation); pre-collected problems available without keys | Used pre-collected problem set; no blocking issue                                                                               |
| B005 BigCodeBench (Hard)              | Full — arXiv:2406.15877                                                                  | Full public — github.com/bigcode-project/bigcodebench; HuggingFace dataset                                                                   | Requires Docker/sandboxed execution environment for safe evaluation                                                           | Metadata and task descriptions fully accessible; execution environment noted as requirement for Phase 3                         |
| B006 IFEval                           | Full — arXiv:2311.07911                                                                  | Full public — google-research GitHub                                                                                                         | None                                                                                                                          | N/A                                                                                                                             |
| B007 WritingBench                     | Full — NeurIPS 2025 proceedings (open access)                                            | Expected public post-publication; GitHub not yet live as of April 2026                                                                        | Dataset not yet publicly released as of 17 April 2026 (NeurIPS 2025 paper; typical release lag)                               | Paper and evaluation methodology fully documented; dataset release expected before Phase 3 coding begins; flagged for follow-up |
| B008 EQ-Bench CW v3 + Longform        | Full — arXiv:2312.06281; eqbench.com                                                     | Full public — github.com/EQ-bench/EQ-Bench; live leaderboard                                                                                 | None                                                                                                                          | N/A                                                                                                                             |
| B009 HelloBench / LongBench-Write     | Partial — arXiv preprints; no peer-reviewed venue as of April 2026                       | HelloBench: github.com/Quehry/HelloBench (public); LongBench-Write: HuggingFace THUDM                                                         | Minor: LongBench-Write GitHub repo had incomplete documentation at time of access                                             | Used HuggingFace dataset card and paper for metadata; complete enough for inventory purposes                                    |
| B010 MathDial                         | Full — ACL Anthology (EMNLP 2023 Findings)                                               | Full public — github.com/eth-nlped/mathdial                                                                                                  | None                                                                                                                          | N/A                                                                                                                             |
| B011 MRBench                          | Full — ACL Anthology (NAACL 2025)                                                        | Expected public post-publication; GitHub link not yet active as of April 2026                                                                 | Dataset not yet publicly released (NAACL 2025 paper; recent publication)                                                      | Paper and DAMR metric fully documented; dataset release expected; flagged for follow-up                                         |
| B012 MathTutorBench                   | Partial — arXiv preprint (2025); under review at TMLR                                    | Partial — github.com/eth-nlped/mathtutorbench (paper repository); full leaderboard data accessible at leaderboard site                       | arXiv preprint only; peer-reviewed version not yet available; leaderboard is live                                             | Sufficient for inventory; peer-review status noted in quality_notes; flagged for citation update post-acceptance                |
| B013 MMLU / MMLU-Pro                  | Full — arXiv:2009.03300; arXiv:2406.01574                                                | Full public — github.com/hendrycks/test (MMLU); github.com/TIGER-Lab/MMLU-Pro                                                                | None                                                                                                                          | N/A                                                                                                                             |
| B014 GPQA Diamond                     | Full — arXiv:2311.12022                                                                  | Gated by design — dataset access requires email request to authors; paper and evaluation protocol fully public                               | Dataset not downloadable without author permission (intentional contamination-resistance measure)                             | Paper metadata fully sufficient for inventory; evaluation protocol documented; gated access noted in public_availability field  |
| B015 TriviaQA / Natural Questions     | Full — arXiv:1705.03551; TACL 2019 (open access)                                         | Full public — github.com/mandarjoshi90/triviaqa; ai.google.com/research/NaturalQuestions                                                     | None                                                                                                                          | N/A                                                                                                                             |
| B016 SimpleQA / FACTS Grounding       | Partial — OpenAI technical blog (SimpleQA); arXiv 2024 (FACTS)                           | SimpleQA: github.com/openai/simple-evals (public); FACTS: dataset access via Google Research (public)                                         | SimpleQA paper is a blog post not a peer-reviewed paper; citation details are less formal                                     | OpenAI blog post is sufficient documentation; noted in venue field as "OpenAI technical blog 2024"                              |
| B017 CriticBench (Tsinghua)           | Full — ACL 2024 Findings (open access)                                                   | Full public — github.com/CriticBench/CriticBench                                                                                             | None                                                                                                                          | N/A                                                                                                                             |
| B018 Auto-J + Shepherd + MetaCritique | Full — arXiv:2310.05470 (Auto-J); arXiv:2308.01825 (Shepherd); arXiv 2024 (MetaCritique) | Auto-J: github.com/GAIR-NLP/auto-j (public); Shepherd: github.com/facebookresearch/shepherd (public); MetaCritique: GitHub link not confirmed | MetaCritique GitHub not located during access period                                                                          | Used paper for metadata; noted as "GitHub link not confirmed" in database; does not affect analysis                             |

---

## Papers with Code Sunset Note

Papers with Code was sunsetted by Meta on 24–25 July 2025. Historical benchmark data
was reconstructed from:

- Cached search results from the Internet Archive (Wayback Machine)
- NLP-Progress (nlpprogress.com — Sebastian Ruder's maintained list)
- Direct searches on arXiv and ACL Anthology
- Cross-referencing with frontier model technical reports

---

## Pending Follow-Ups

The following items should be rechecked before Phase 3 begins:

1. **WritingBench dataset** — check for public GitHub release (expected mid-2026).
2. **MRBench dataset** — check for public GitHub release following NAACL 2025 proceedings.
3. **MathTutorBench** — update citation when TMLR peer-review decision is published.
4. **MetaCritique GitHub** — locate and verify repository URL.
5. **GPQA Diamond** — request dataset access via authors if needed for Phase 3 direct evaluation.
