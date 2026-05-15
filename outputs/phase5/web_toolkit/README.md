# Benchmark Coverage Gap Toolkit

This folder contains a zero-cost static web toolkit for Phase 5. It implements
the assessment toolkit as an interactive webpage rather than a spreadsheet-only
artifact.

## What It Does

- Lets users choose a predefined use-case profile or create a custom one.
- Converts that use case into capability weights from 0 to 5.
- Ranks benchmarks from the Phase 2 inventory using the Phase 3 coverage matrix.
- Calculates overall ecosystem coverage fit and gap risk.
- Shows supporting capability, benchmark, and evidence views.

## Data Sources

The toolkit loads these project files at runtime:

- `outputs/phase1/capability_taxonomy_FINAL.csv`
- `data/phase2/benchmark_database.csv`
- `data/phase3/coverage_matrix.csv`
- `data/phase3/gap_scores.csv`

The recommendation pool is intentionally bounded to the benchmarks analysed in
Phase 2. This keeps the output reproducible and avoids implying coverage of
every benchmark in existence.

## Run Locally

From the project root:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/outputs/phase5/web_toolkit/
```

Opening `index.html` directly from the file system may block CSV loading in some
browsers. A local static server avoids that.

## Deployment

This can be deployed for free with GitHub Pages because it has:

- No backend.
- No database.
- No paid API calls.
- No build step.
- No external JavaScript dependencies.

If publishing the repository, confirm that the source CSV files do not contain
personal data or unpublished sensitive research data.
