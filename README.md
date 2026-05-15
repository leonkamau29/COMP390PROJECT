<!-- markdownlint-disable MD013 -->

# Benchmark Coverage Gap: A Systematic Analysis of Real-World AI Capabilities and Evaluation Practices

**Student:** Leon Kamau Kiunga (201759400)
**Supervisor:** Dr Konstantinos Tsakaldis
**Degree:** Honours Research Project (BCS-aligned)

---

## Project Overview

This project systematically maps what LLM benchmarks actually test against what
users actually do, quantifies gaps weighted by real usage frequency, and provides
actionable recommendations and a reusable assessment toolkit.

## Interactive Assessment Toolkit

The Phase 5 assessment toolkit is available as a static web application:

- Local path: `outputs/phase5/web_toolkit/index.html`
- GitHub Pages path: `https://<github-username>.github.io/<repo-name>/`

The repository root includes `index.html`, which redirects GitHub Pages visitors
directly to the toolkit. No login, installation, backend service, database, or
paid API is required.

To preview locally from the project root:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

### GitHub Pages Setup

1. Open the repository on GitHub.
2. Go to **Settings** > **Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**.
4. Select branch `main` and folder `/root`.
5. Save and use the URL shown by GitHub Pages.

## Setup

```bash
pip install -r requirements.txt
```

## Project Structure

```text
project_root/
├── data/           # Raw and processed data files (by phase)
├── outputs/        # Final outputs, charts, and reports (by phase)
├── scripts/        # Python analysis scripts
└── thesis/         # Thesis chapters and final document
```

## Phases

| Phase | Weeks | Focus |
| ----- | ----- | ----- |
| Phase 1 | 1–4 | Capability Framework Development |
| Phase 2 | 5–9 | Benchmark Inventory |
| Phase 3 | 10–13 | Coverage Analysis |
| Phase 4 | 14–16 | Expert Validation |
| Phase 5 | 17–20 | Recommendations & Toolkit |
| Writing | 21–24 | Thesis Completion |

## Key Reference

See `DATA/CLAUDE.md` for the full project reference document.
