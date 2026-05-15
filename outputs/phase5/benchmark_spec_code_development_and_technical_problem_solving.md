<!-- markdownlint-disable MD013 -->

# Benchmark Specification: MaintBench

## 1. Capability Measured and Rationale

MaintBench is my proposed benchmark for C02, Code Development and Technical Problem Solving. I designed it to test whether large language models can diagnose, modify, integrate, and maintain realistic software systems rather than only solve isolated coding prompts. The benchmark focuses on multi-file debugging, dependency integration, refactoring under constraints, configuration repair, regression prevention, and handoff-quality explanations.

The rationale comes directly from the Phase 3 gap analysis. C02 has a usage frequency of 0.301859, a normalised coverage score of 0.235714, and a gap score of 0.230707, making it the highest-priority gap in the project. The Phase 1 taxonomy shows that users ask for troubleshooting, web application changes, debugging, refactoring, authentication work, infrastructure support, and other practical technical tasks. These are broader than short code-generation exercises because they require the model to interpret project context, identify root causes, preserve existing behaviour, and produce maintainable changes.

The existing C02 benchmark landscape is active but uneven. HumanEval+ is useful as a historical isolated-function benchmark, LiveCodeBench improves contamination control, BigCodeBench tests library use, and SWE-bench Verified and SWE-Lancer Diamond provide stronger repository-level realism. However, there is still a middle layer of everyday maintenance work that is not covered cleanly: ambiguous bug reports, incremental integration failures, safe refactoring, configuration repair, and practical explanations for maintainers. MaintBench is designed to target that layer.

## 2. Task Structure

Each MaintBench item would be a self-contained software maintenance scenario. The model receives a repository snapshot, a stakeholder request, relevant logs or failing tests, and project constraints. The required output is a patch plus a short engineering note explaining the diagnosis, the change, the verification steps, and any remaining risks.

The benchmark would cover bug diagnosis and repair, integration and dependency repair, regression-sensitive refactoring, operational troubleshooting, and maintenance handoff. Each task would include a repository archive or container image, a realistic issue brief, optional logs or reproduction steps, explicit constraints such as API stability or dependency restrictions, hidden tests, static checks, and an expert rubric for maintainability and communication.

The following bullet points are examples of tasks that could exist in the proposed MaintBench benchmark. They are illustrative task designs rather than the final dataset.

- A Flask authentication regression where admin users are redirected to `/dashboard` instead of `/admin`. The expected output would be a local patch to the login flow, a regression test for role-specific redirects, and an explanation identifying the redirect branch as the root cause.
- A Django CSV import command where a pandas upgrade causes empty dates to be stored as `"NaT"` instead of null. The expected output would normalise missing date values, add tests for empty and valid dates, and explain the version-sensitive parsing behaviour.
- A React checkout form that clears shipping state after card validation fails. The model would separate validation errors from form reset logic, preserve controlled component state, and add component tests for the failure path.
- A Docker Compose startup race where a FastAPI service connects to Postgres too early. The expected patch would add a bounded readiness wait or health-check-driven startup sequence without hardcoding credentials or making local development unnecessarily complex.
- A TypeScript API refactoring task where duplicated validation logic must be removed while exact client-facing error messages stay the same. The evaluation would check that behaviour remains stable and duplication is reduced without changing the public API.
- A daylight-saving bug in a scheduled-reporting service. The model would introduce timezone-aware scheduling, add boundary tests, and explain migration implications.
- A data-sync job that only fetches the first page of a third-party API. The expected fix would handle `next_cursor`, empty cursors, mocked API tests, and rate-limit behaviour according to existing project patterns.
- A Rails migration that adds a non-null column but fails on existing production-like data. The model would propose a safe migration or backfill strategy and consider rollback risk.
- A Python CLI that prints a stack trace and exits with code 0 when a required config file is missing. The model would return a clear error, use a non-zero exit status, and preserve debug detail only where the project already supports it.
- A Node.js permission cache bug where revoked permissions remain active until expiry. The expected fix would invalidate permission cache entries on role changes or use versioned cache keys, with security regression tests for permission revocation.

## 3. Dataset Composition

The first release should contain around 600 tasks across roughly 60 repositories, with each repository contributing about 8 to 12 tasks. This is large enough to support sub-capability reporting while remaining feasible for expert review. I would distribute the tasks across bug repair, integration repair, refactoring, operational troubleshooting, and handoff-related maintenance tasks.

The repositories should be modest in size, ideally around 1,000 to 20,000 lines of code. They should be large enough to require file navigation but small enough to run reproducibly in containers. Python, JavaScript or TypeScript, Java, and SQL-backed web projects would be appropriate starting languages because they reflect common real-world technical assistance requests.

The data should combine permissively licensed open-source repositories, synthetic but realistic maintenance tasks seeded by experts, rewritten public issue patterns, post-cutoff commits, and private holdout tasks where possible. Quality control should include expert verification, independent reference patching, hidden-test construction by a separate reviewer, containerised execution, and metadata for language, framework, task family, difficulty, files touched, and expected reasoning steps.

## 4. Evaluation Methodology

MaintBench should use mixed evaluation because software maintenance quality cannot be reduced to a single pass/fail metric. The primary metric should be resolved task rate, meaning that the patch passes visible and hidden tests, satisfies static checks, and does not violate explicit constraints.

Secondary metrics should capture regression safety, patch minimality, maintainability, diagnosis quality, constraint adherence, and operational efficiency. Automated checks can handle tests, linting, type checks, build execution, and migrations. Human or expert judgement should be used for maintainability, diagnosis quality, and whether the patch is overbroad.

I would report results by task family, language, repository size, and difficulty rather than relying only on one headline score. A model may perform well on local bug fixes but fail on migrations, configuration, refactoring, or operational issues.

## 5. Validation Strategy

Validation should begin by mapping every task to the C02 sub-categories from the Phase 1 taxonomy. A 50-task pilot across 5 repositories should then be run with at least two baseline models and one human developer or expert patch author. Tasks that are ambiguous, unsolvable, environment-sensitive, or trivially searchable should be removed.

Scoring reliability should be tested by verifying that hidden tests distinguish correct patches from plausible but wrong patches. For human-judged dimensions, annotators should be trained on calibration patches and weighted kappa should be reported, with a target above 0.80. External validity should be checked by comparing rankings with SWE-bench Verified, BigCodeBench, LiveCodeBench, and SWE-Lancer Diamond. I would expect moderate correlation, not perfect correlation, because MaintBench is intended to measure a different part of software work.

## 6. Implementation Requirements

A strong first release would likely take 4 to 6 months. It would require software engineering researchers, experienced developers for task construction and validation, an infrastructure engineer for containers and the evaluation harness, and optional domain reviewers for security or database tasks.

The infrastructure would need reproducible Docker images, a Git-based task package format, a test runner with timeouts and resource limits, a sandboxed patch application service, and an annotation interface for maintainability and diagnosis scoring. The cost level is medium to high because expert engineering time and reliable execution infrastructure are the main costs.

The expected deliverables are a public task schema, a public development split, a private or refreshed evaluation split, baseline model results, and documentation explaining task families, scoring, and limitations.

## 7. Expected Challenges and Mitigations

The main challenge is environment fragility. Repository-level tasks can fail because of dependency drift rather than model error, so the benchmark should use locked containers, pinned versions, checksum validation, and regular health checks. Hidden tests can also be incomplete, so test-based scoring should be combined with expert judgement for minimality, maintainability, and diagnosis.

Contamination is another issue because open-source repositories and issues may appear in training data. I would mitigate this with post-cutoff tasks, synthetic issue injection, private holdouts, and refreshes. Operational cost can be managed with tiered evaluation: a smoke-test split, a standard split, and a full agentic split. Task ambiguity should be included only where the rubric can distinguish sensible clarification from unsafe implementation.

## 8. Comparison to Existing Benchmarks

MaintBench is not intended to replace HumanEval+, SWE-bench Verified, LiveCodeBench, BigCodeBench, SWE-Lancer Diamond, or WildBench. Its contribution is to fill the space between isolated code-generation tasks and expensive full issue-resolution suites. Compared with HumanEval+, it requires repository navigation and maintenance-quality explanation. Compared with SWE-bench Verified, it broadens beyond issue patches into integration, refactoring, configuration, and handoff. Compared with LiveCodeBench, it applies the refresh principle to maintenance rather than competitive programming. Compared with BigCodeBench, it extends library use into multi-file systems and stateful services. Compared with SWE-Lancer Diamond, it keeps the emphasis on real task value while aiming for broader public reproducibility.

The intended contribution is a benchmark for everyday software maintenance, which is exactly the kind of technical work users often ask models to perform but which current coding benchmarks only partially measure.
