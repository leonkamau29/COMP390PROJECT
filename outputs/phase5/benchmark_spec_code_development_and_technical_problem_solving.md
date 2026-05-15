<!-- markdownlint-disable MD013 -->

# Benchmark Specification: MaintBench - Realistic Debugging, Integration, and Maintenance

## 1. Capability Measured and Rationale

**Target capability:** C02 - Code Development and Technical Problem Solving.

MaintBench is a proposed benchmark for evaluating whether large language models can diagnose, modify, integrate, and maintain realistic software systems beyond isolated code-generation tasks. The benchmark focuses on multi-file debugging, dependency integration, refactoring under constraints, configuration repair, regression prevention, and handoff-quality explanations. It is designed to test the forms of technical collaboration represented in the Phase 1 taxonomy: web application development, software engineering and systems, code debugging and refactoring, DevOps and infrastructure, and technical troubleshooting.

The rationale is grounded in the Phase 3 gap analysis. C02 is the highest-priority gap in the current project, with a usage frequency of 0.301859, a normalised coverage score of 0.235714, and a gap score of 0.230707. The Phase 1 taxonomy records multiple high-frequency real-world tasks in this capability, including troubleshooting hardware, software, and system issues; developing and modifying web applications; debugging and refactoring code; and implementing authentication and infrastructure systems. These tasks are broader than short-form programming problems because they require interpreting existing project context, identifying root causes, preserving intended behaviour, and producing maintainable changes.

The Phase 2 benchmark inventory shows that C02 is not ignored by the benchmark ecosystem. HumanEval+ (B001), SWE-bench Verified (B002), LiveCodeBench (B003), BigCodeBench (B004), SWE-Lancer Diamond (B005), LiveBench (B010), WildBench (B014), DA-Code (B016), Spider 2.0 (B017), and CriticBench (B022) all provide some coverage. However, the coverage notes show a persistent gap between benchmark convenience and everyday maintenance work. HumanEval+ is strong for isolated unit-tested functions but has high contamination risk and weak ecological validity. LiveCodeBench improves contamination control but remains closer to competitive programming than maintenance. BigCodeBench captures library-oriented API use but is Python-only and task-bounded. SWE-bench Verified and SWE-Lancer Diamond provide strong repository-level realism, but they are operationally expensive and still skew toward issue-resolution tasks with fixed tests. MaintBench is intended to complement these benchmarks by targeting the middle layer of real-world software work: ambiguous bug reports, incremental maintenance requests, integration failures, and regression-sensitive refactoring in modest but realistic repositories.

## 2. Task Structure

Each MaintBench item is a self-contained software maintenance scenario. The model receives a repository snapshot, a user or stakeholder request, relevant logs or test failures, and project constraints. The model must submit a patch plus a short engineering note explaining the diagnosis, change, verification steps, and residual risks.

The benchmark is organised into five task families:

- **Bug diagnosis and repair:** identify a failing behaviour from user report, logs, or tests and patch the implementation.
- **Integration and dependency repair:** connect components, external APIs, package versions, or configuration files without breaking existing behaviour.
- **Regression-sensitive refactoring:** improve code structure while preserving test behaviour and public interfaces.
- **Operational troubleshooting:** repair configuration, environment variables, build pipelines, deployment scripts, or database migrations.
- **Maintenance handoff:** produce concise explanations, migration notes, and verification instructions for a future maintainer.

Each item has the following artefacts:

- Repository archive or container image.
- Issue brief written in realistic user language.
- Optional failing tests, logs, screenshots, or reproduction steps.
- Explicit constraints, such as "do not change the public API", "support Python 3.10 and 3.11", or "do not introduce a new dependency".
- Hidden tests and static checks.
- Expert-written scoring rubric for maintainability, diagnosis, minimality, and communication.

### Example Item 1: Authentication Redirect Regression

**Input:** A small Flask application has recently added role-based routes. Users report that logging in as an admin redirects to `/dashboard` instead of `/admin`. Existing tests cover normal login but not role-specific redirects. The repository includes `auth.py`, `routes.py`, and a failing reproduction script.

**Expected output:** A patch that updates the login flow to select the correct post-login route based on the user's role, adds a regression test for admin and standard-user redirects, and preserves existing session handling.

**Evaluation criteria:** Hidden tests pass; no public route names are changed; the fix is local rather than a broad rewrite; the engineering note identifies the redirect branch as the root cause.

### Example Item 2: Broken CSV Import After Library Upgrade

**Input:** A Django management command imports customer CSV files. After a pandas upgrade, empty date fields are stored as the string `"NaT"` instead of null. The user provides a short error report and two sample CSV rows.

**Expected output:** A patch that normalises missing date values before persistence, updates tests for empty and valid dates, and documents the version-sensitive parsing behaviour.

**Evaluation criteria:** Correct database values are produced; valid dates remain unchanged; the solution does not pin pandas unnecessarily; regression coverage is added.

### Example Item 3: React Form State Lost On Validation Error

**Input:** A React checkout form clears the shipping address when card validation fails. The project uses controlled components and a reducer-based state model.

**Expected output:** A patch that preserves shipping state when payment validation fails, separates validation errors from form data reset logic, and adds component tests for the failure path.

**Evaluation criteria:** Hidden UI tests pass; state update remains idiomatic for the existing reducer; no unrelated redesign is introduced; explanation distinguishes validation state from persisted form state.

### Example Item 4: Docker Compose Database Race Condition

**Input:** A FastAPI service sometimes fails at startup because it connects to Postgres before the database accepts connections. The repository contains `docker-compose.yml`, an entrypoint script, and CI logs.

**Expected output:** A patch that adds a bounded readiness wait or health-check driven startup sequence, keeps local development simple, and documents the chosen approach.

**Evaluation criteria:** Container integration tests pass; startup retries are bounded; credentials are not hardcoded; the solution works on a clean checkout.

### Example Item 5: Refactor Duplicate Validation Without Behaviour Change

**Input:** A TypeScript API duplicates email and phone validation across three endpoints. The user requests refactoring but warns that existing client error messages must not change.

**Expected output:** A patch that extracts shared validation logic, keeps response shape and messages stable, and adds tests confirming unchanged behaviour.

**Evaluation criteria:** Snapshot or exact-message tests pass; code duplication is reduced; public API behaviour remains stable; no new validation rules are introduced.

### Example Item 6: Time Zone Bug In Scheduled Reports

**Input:** A reporting service sends weekly summaries one hour late after daylight-saving changes. The code mixes naive datetimes and local time conversion.

**Expected output:** A patch that uses timezone-aware scheduling, adds tests around daylight-saving transitions, and explains any migration implications.

**Evaluation criteria:** Boundary tests pass; UTC/local conversions are explicit; no global time-zone assumptions are introduced; the note identifies daylight-saving transition handling.

### Example Item 7: API Pagination Integration

**Input:** A data sync job fetches only the first page from a third-party API. The API documentation states that pagination uses a `next_cursor` token.

**Expected output:** A patch that loops through all pages safely, handles empty and missing cursors, adds mocked API tests, and avoids unbounded retries.

**Evaluation criteria:** Hidden mocks verify all pages are fetched; rate-limit errors are handled according to existing project patterns; no duplicated records are inserted.

### Example Item 8: SQL Migration Fails On Existing Data

**Input:** A Rails application adds a non-null column to an orders table. The migration passes on an empty test database but fails on production-like fixtures with existing rows.

**Expected output:** A safe two-step migration or backfill strategy, with tests or migration checks showing existing rows are handled.

**Evaluation criteria:** Migration succeeds on populated fixtures; rollback is considered; data defaults are justified; no destructive schema operation is used.

### Example Item 9: CLI Tool Error Message And Exit Code

**Input:** A Python CLI tool prints a stack trace and exits with code 0 when a required config file is missing. Users need a clear error and non-zero exit code.

**Expected output:** A patch that catches the missing-config case, prints a concise actionable error, returns a non-zero exit status, and preserves debug stack traces behind a verbose flag if the project already supports one.

**Evaluation criteria:** CLI tests verify stderr and exit code; other error paths are unaffected; the message identifies the missing file and remediation.

### Example Item 10: Caching Layer Causes Stale Permissions

**Input:** A Node.js service caches user permission lookups. Revoked permissions remain active until the cache expires. The user asks for a fix that does not remove caching entirely.

**Expected output:** A patch that invalidates permission cache entries on role changes or uses a versioned cache key, with tests for revocation and normal cached reads.

**Evaluation criteria:** Security regression tests pass; performance-sensitive caching remains; invalidation logic is located near existing role-change code; explanation identifies stale authorisation as the risk.

## 3. Dataset Composition

The proposed initial benchmark should contain **600 tasks** across approximately **60 repositories**, with each repository contributing 8-12 tasks. This size is large enough to support capability-level reporting while remaining feasible for academic construction and expert review.

Suggested distribution:

- 180 bug diagnosis and repair tasks.
- 120 integration and dependency repair tasks.
- 100 regression-sensitive refactoring tasks.
- 100 operational troubleshooting tasks.
- 100 maintenance handoff and documentation-linked tasks.

Repositories should be intentionally modest in size: large enough to require navigation across files, but small enough to run in reproducible containers. A target range of 1,000-20,000 lines of code per repository is appropriate. Languages should include Python, JavaScript/TypeScript, Java, and SQL-backed web projects, reflecting common real-world technical assistance use. The first version should not attempt full coverage of every programming ecosystem; it should prioritise reproducibility, task clarity, and scoring reliability.

Data sources should combine:

- Public open-source repositories with permissive licences.
- Synthetic but realistic maintenance tasks seeded by experts into repository snapshots.
- Public issue patterns rewritten into new task instances to reduce direct contamination.
- Post-cutoff repository commits and private holdout tasks where possible.

Quality control should include:

- Expert verification that each issue is realistic and solvable.
- Independent patch construction by at least one maintainer-level reviewer.
- Hidden test creation by a reviewer different from the patch author.
- Containerised execution to ensure reproducibility.
- Metadata recording for language, framework, task family, difficulty, files touched, and expected reasoning steps.

The benchmark should maintain public development, validation, and private holdout splits. Public examples support reproducibility and method development. A private or periodically refreshed split reduces overfitting and contamination risk, following the motivation behind LiveCodeBench's post-cutoff updates and Humanity's Last Exam's private holdout design.

## 4. Evaluation Methodology

MaintBench should use a mixed evaluation design because software maintenance quality cannot be captured by a single pass/fail metric.

**Primary metric: resolved task rate.** A task is resolved if the submitted patch passes all visible and hidden tests, satisfies static checks, and does not violate explicit constraints.

**Secondary metrics:**

- **Regression safety:** percentage of pre-existing tests still passing after the patch.
- **Patch minimality:** expert or rule-assisted score indicating whether the patch changes only relevant code.
- **Maintainability:** rubric score for readability, idiomatic fit, and long-term maintainability.
- **Diagnosis quality:** score for whether the engineering note correctly identifies the root cause.
- **Constraint adherence:** binary and graded checks for user constraints, such as no new dependencies or API stability.
- **Operational efficiency:** runtime, number of tool calls if evaluated in an agentic environment, and failure recovery behaviour.

Automated scoring should handle tests, linting, type checks, migration checks, and build execution. Human or expert judgement should be reserved for maintainability, diagnosis quality, and whether a patch is overbroad. To reduce subjectivity, each human-judged item should use a five-point analytic rubric with descriptors. At least 10 percent of judged items should be double-coded, with Cohen's kappa or weighted kappa reported for categorical rubric decisions.

The benchmark should report aggregate results by task family, language, repository size, and difficulty. A single headline score is insufficient because a model may perform well on isolated repairs but fail on migrations, configuration, or refactoring.

## 5. Validation Strategy

Validation should occur in four stages.

**Stage 1: Construct validation.** Map each task to C02 sub-categories from the Phase 1 taxonomy. The task set should cover C02a web application development, C02b software engineering and systems, C02c debugging and refactoring, C02e DevOps and infrastructure, and C02f technical troubleshooting. C02d machine learning development may be included in a later extension because it introduces specialised dependencies.

**Stage 2: Pilot testing.** Run a pilot with 50 tasks across 5 repositories. The pilot should be attempted by at least two baseline models and one human developer or expert patch author. Remove tasks that are ambiguous, unsolvable, too environment-sensitive, or trivially solved by search.

**Stage 3: Scoring reliability.** Verify that hidden tests distinguish correct from superficially plausible patches. For human-judged dimensions, train annotators using 20 calibration patches and target weighted kappa above 0.80 before full annotation.

**Stage 4: External validity checks.** Compare model rankings against related benchmarks such as SWE-bench Verified, BigCodeBench, LiveCodeBench, and SWE-Lancer Diamond. The expected result is moderate correlation, not perfect correlation. If MaintBench correlates perfectly with HumanEval+, it is likely failing to measure the intended maintenance construct.

Ground truth should be versioned. Each task should include an expert reference patch, but scoring should accept any patch that passes tests and satisfies constraints. This prevents overfitting to a single implementation style.

## 6. Implementation Requirements

**Estimated time:** 4-6 months for a strong first release with 600 tasks.

**Personnel:**

- 2-3 software engineering researchers.
- 4-6 experienced developers for task construction and patch validation.
- 1 infrastructure engineer for containerisation and evaluation harness design.
- Optional domain reviewers for security-sensitive or database-migration tasks.

**Infrastructure:**

- Container registry and reproducible Docker images.
- Git-based task packaging.
- Automated test runner with timeouts and resource limits.
- Patch application and sandbox execution service.
- Annotation interface for maintainability and diagnosis scoring.

**Estimated cost level:** Medium to high. The largest cost is expert software engineering time and reliable execution infrastructure.

**Deliverables:**

- Public task schema and scoring harness.
- Public development split.
- Private or refreshed evaluation split.
- Baseline results for several open and closed models.
- Documentation explaining task families, scoring, and known limitations.

## 7. Expected Challenges and Mitigations

**Challenge: environment fragility.** Repository-level tasks can fail because of dependency drift rather than model error.

**Mitigation:** Use locked containers, pinned package versions, checksum validation, and continuous benchmark health checks.

**Challenge: hidden tests can be incomplete.** A patch may pass tests while violating maintainability or user intent.

**Mitigation:** Combine hidden tests with expert rubric scoring for patch minimality, maintainability, and diagnosis.

**Challenge: contamination from public repositories.** Open-source issues and commits may have appeared in training data.

**Mitigation:** Use post-cutoff tasks, synthetic issue injection, private holdouts, and periodic refreshes.

**Challenge: operational cost.** Full repository evaluation is slower and more expensive than unit-test benchmarks.

**Mitigation:** Provide tiered evaluation: a small smoke-test split, a standard split, and a full agentic split.

**Challenge: task ambiguity.** Realistic maintenance requests are often underspecified.

**Mitigation:** Include ambiguity intentionally only when the scoring rubric can distinguish appropriate clarification, conservative assumptions, and unsafe implementation.

## 8. Comparison to Existing Benchmarks

MaintBench is not intended to replace current C02 benchmarks. It fills a specific gap between isolated code generation and expensive full issue-resolution suites.

**HumanEval+ (B001)** provides efficient unit-test scoring for isolated Python functions. MaintBench differs by requiring navigation of existing repositories, preservation of surrounding behaviour, and maintenance-quality explanations.

**SWE-bench Verified (B002)** is the closest existing benchmark in ecological validity. MaintBench differs by broadening the task set beyond issue-resolution patches to include integration failures, operational troubleshooting, refactoring, and handoff documentation in smaller reproducible repositories.

**LiveCodeBench (B003)** improves contamination resistance through refreshed algorithmic problems. MaintBench adopts the principle of refresh but applies it to maintenance scenarios rather than competitive programming.

**BigCodeBench (B004)** evaluates library-oriented Python API use. MaintBench extends the integration idea across multi-file systems, configuration, stateful services, and regression-sensitive tasks.

**SWE-Lancer Diamond (B005)** links software tasks to economic value. MaintBench borrows the emphasis on real task value but aims for broader public reproducibility and more granular sub-capability reporting.

**WildBench (B014)** includes real-user coding prompts, but its broadness makes construct attribution difficult. MaintBench isolates C02 and reports by maintenance task family.

The intended contribution is therefore a targeted benchmark for everyday software maintenance: the kind of technical work that users frequently ask models to perform, but which is only partially measured by current code-generation and agentic issue-resolution benchmarks.
