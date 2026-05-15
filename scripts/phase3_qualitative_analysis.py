"""
Write Phase 3 qualitative deep dives and case studies.

Purpose:
    Produce the four capability deep dives and documented deployment-failure
    case studies required by Phase 3.

Inputs:
    data/phase3/coverage_matrix.csv
    data/phase3/gap_scores.csv
    outputs/phase1/capability_taxonomy_FINAL.csv
    outputs/phase2/benchmark_database_FINAL.csv

Outputs:
    outputs/phase3/deep_dive_*.md
    outputs/phase3/case_studies.md
"""

from __future__ import annotations

import re
import textwrap

import numpy as np
import pandas as pd

from phase3_config import (
    CASE_STUDIES_PATH,
    GAP_SCORES_PATH,
    MATRIX_PATH,
    PHASE3_OUTPUTS,
    ensure_directories,
    format_float,
    load_inputs,
    prepare_benchmarks,
)


np.random.seed(42)

CASE_STUDIES = [
    {
        "title": "Autonomous workplace agents complete only a minority of consequential tasks",
        "model": "Frontier LLM agents evaluated in TheAgentCompany",
        "benchmark_performance": "Models report strong scores on standard frontier evaluations, but the best reported autonomous workplace completion rate in TheAgentCompany is about 30%.",
        "context": "A simulated software-company workplace requiring agents to browse, code, communicate, and complete HR, finance, engineering, legal, and administration tasks.",
        "failure": "Agents frequently fail long-horizon task planning, tool use, and context management despite high benchmark performance.",
        "capability_gap": "C02, C03, and C07: technical problem solving, information retrieval, and data/document processing in integrated workflows.",
        "consequences": "The result indicates that benchmark strength does not imply production readiness for autonomous work; human oversight and constrained scope remain necessary.",
        "source": "Xu, F. F. et al. (2025). TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks. arXiv:2412.14161.",
    },
    {
        "title": "Coding scores fall on post-cutoff problems, exposing contamination risk",
        "model": "LLMs evaluated on LiveCodeBench and older code benchmarks",
        "benchmark_performance": "Many models perform strongly on established code benchmarks such as HumanEval, while LiveCodeBench reports performance drops on problems released after training cutoffs for some model families.",
        "context": "Competitive-programming and code-generation tasks collected by release date from LeetCode, AtCoder, and Codeforces.",
        "failure": "Performance on older public problems can overstate generalisation because memorised or contaminated items inflate apparent capability.",
        "capability_gap": "C02: code development and technical problem solving under contamination-resistant, temporally controlled evaluation.",
        "consequences": "Deployment decisions based on saturated coding benchmarks may overestimate reliability on new bugs, libraries, and unseen engineering tasks.",
        "source": "Jain, N. et al. (2024). LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code. arXiv:2403.07974.",
    },
    {
        "title": "Multiple-choice benchmark rankings change under answer-order perturbations",
        "model": "LLMs evaluated on MMLU-style multiple-choice tasks",
        "benchmark_performance": "MMLU-style scores are widely used in model selection and leaderboard reporting.",
        "context": "Multiple-choice factual and reasoning questions where answer options can be reordered without changing the underlying task.",
        "failure": "Option-order sensitivity changes model scores and can shift rankings by up to eight positions, showing that leaderboard outcomes can depend on presentation artefacts.",
        "capability_gap": "C03: information retrieval and advisory evaluation that is robust to prompt and answer-format artefacts.",
        "consequences": "A model selected because of a marginal leaderboard advantage may not be more reliable in real advisory settings.",
        "source": "Pezeshkpour, P. and Hruschka, E. (2024). Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions. Findings of NAACL 2024.",
    },
    {
        "title": "Clinical decision-making failures persist despite medical benchmark success",
        "model": "State-of-the-art medical LLMs and general frontier models",
        "benchmark_performance": "Medical LLMs and frontier models can achieve strong medical-exam or clinical benchmark results.",
        "context": "Clinical decision-making over real or realistic patient cases requiring diagnosis, treatment planning, and interpretation of laboratory and contextual information.",
        "failure": "Studies report failures in diagnostic accuracy, guideline following, patient-context adjustment, and unsafe responses to patient-posed questions.",
        "capability_gap": "C03 and C07: advisory reasoning and context-sensitive analysis of patient information.",
        "consequences": "Aggregate benchmark scores can mask patient-safety-relevant error patterns such as under-triage or unsafe advice.",
        "source": "Kanjee, Z. et al. (2024). Evaluation and mitigation of the limitations of large language models in clinical decision-making. Nature Medicine.",
    },
    {
        "title": "Legal hallucinations lead to false citations and professional sanctions",
        "model": "ChatGPT and specialised legal research LLM systems",
        "benchmark_performance": "General and legal-domain LLMs can appear fluent and authoritative on legal questions.",
        "context": "Legal research and brief drafting where users require accurate cases, quotations, and citations.",
        "failure": "LLMs generated fictitious legal authorities and unreliable legal statements; specialised systems still hallucinated in later evaluations.",
        "capability_gap": "C03, C05, and C01: legal information retrieval, review of generated claims, and professional document generation.",
        "consequences": "False citations can mislead courts and clients, producing sanctions and undermining trust in legal AI tools.",
        "source": "Magesh, V. et al. (2025). Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools. arXiv:2405.20362.",
    },
    {
        "title": "Leaderboard disclosure practices distort model selection",
        "model": "Closed-source and selectively reported model releases",
        "benchmark_performance": "Vendors report strong headline benchmark results across common leaderboards.",
        "context": "Model-selection decisions made from public technical reports and benchmark tables.",
        "failure": "Selective disclosure and leaderboard choices can materially distort rankings, separating reported benchmark success from actual comparative utility.",
        "capability_gap": "Cross-cutting evaluation validity; especially C03 and C02 where organisations rely on benchmark tables for deployment choices.",
        "consequences": "Practitioners may select models based on incomplete or strategically disclosed evidence rather than fit to their real use cases.",
        "source": "Singh, S. et al. (2025). The Leaderboard Illusion. arXiv:2504.20879.",
    },
]


def capability_benchmark_summary(
    capability_id: str, benchmarks: pd.DataFrame, matrix: pd.DataFrame
) -> pd.DataFrame:
    """Return benchmarks that cover a capability with ratings."""
    ids = matrix.index[matrix[capability_id] >= 1].tolist()
    subset = benchmarks[benchmarks["benchmark_id"].isin(ids)].copy()
    subset["coverage_rating"] = subset["benchmark_id"].map(matrix[capability_id].to_dict())
    return subset.sort_values("coverage_rating", ascending=False)


def deep_dive_examples(capability_id: str) -> list[str]:
    """Return real-world usage examples for a capability."""
    examples = {
        "C01": [
            "Drafting professional workplace emails and business correspondence (Anthropic AEI, 2.9569%).",
            "Creating marketing content, advertising campaigns, and SEO materials (Anthropic AEI, 2.8804%).",
            "Developing business strategy documents and corporate planning materials (Anthropic AEI, 2.7236%).",
        ],
        "C02": [
            "Troubleshooting hardware, software, and system technical issues (Anthropic AEI, 4.1575%).",
            "Developing, debugging, and modifying websites and web applications (Anthropic AEI, 3.9160%).",
            "Debugging, fixing, and refactoring code across languages and systems (Anthropic AEI, 1.8624%).",
        ],
        "C03": [
            "Providing medical and health information across specialties (Anthropic AEI, 2.3787%).",
            "Researching and comparing consumer products for purchase decisions (Anthropic AEI, 2.2478%).",
            "Providing career development and job-transition assistance (Anthropic AEI, 1.6288%).",
        ],
        "C04": [
            "Assisting with academic assignments and coursework across disciplines (Anthropic AEI, 5.1945%).",
            "Creating educational materials and explaining concepts (Anthropic AEI, 1.9390%).",
            "Helping solve and explain mathematics problems across levels (Anthropic AEI, 1.4013%).",
        ],
        "C05": [
            "Editing, proofreading, and reformatting documents and written content (Anthropic AEI, 1.7113%).",
            "Grading student work and creating educational assessments (Anthropic AEI, 0.7811%).",
            "Editing and revising academic writing on AI and research topics (Anthropic AEI, 0.4711%).",
        ],
        "C06": [
            "Language learning assistance, translation, and grammar help across languages (Anthropic AEI, 1.5077%).",
            "Translation and formatting of professional, academic, medical, and religious content (Anthropic AEI, 1.2033%).",
            "Cross-lingual communication support in professional and educational contexts (Phase 1 taxonomy examples).",
        ],
        "C07": [
            "Creating, converting, formatting, and manipulating documents across file types (Anthropic AEI, 2.1915%).",
            "Extracting, analysing, and processing content from images and documents (Anthropic AEI, 1.4706%).",
            "Assisting with data analysis, statistical computing, and database management tasks (Anthropic AEI, 0.9618%).",
        ],
        "C08": [
            "Relationship, dating, parenting, and personal advice across life situations (Anthropic AEI, 1.1517%).",
            "Practising job interviews and roleplaying professional scenarios (Anthropic AEI, 0.6478%).",
            "Providing mental health, behavioural health, and ADHD support resources (Anthropic AEI, 0.3530%).",
        ],
    }
    return examples[capability_id]


def write_deep_dive(
    capability_id: str,
    profile_label: str,
    taxonomy: pd.DataFrame,
    benchmarks: pd.DataFrame,
    matrix: pd.DataFrame,
    gap_scores: pd.DataFrame,
) -> None:
    """Write one qualitative capability deep dive."""
    cap_row = taxonomy.set_index("capability_id").loc[capability_id]
    gap_row = gap_scores.set_index("capability_id").loc[capability_id]
    covered = capability_benchmark_summary(capability_id, benchmarks, matrix)
    if covered.empty:
        landscape = "No benchmark in the updated Phase 2 inventory receives a non-zero coverage rating for this capability."
    else:
        landscape = "\n".join(
            f"- {row['benchmark_id']} {row['name']} ({row['abbreviation']}): coverage rating {int(row['coverage_rating'])}/5; task type: {row['task_type']}; limitation noted in Phase 2: {row['known_limitations']}"
            for _, row in covered.iterrows()
        )

    examples = "\n".join(f"- {item}" for item in deep_dive_examples(capability_id))
    safe_name = re.sub(r"[^a-z0-9]+", "_", str(cap_row["capability_name"]).lower()).strip("_")
    path = PHASE3_OUTPUTS / f"deep_dive_{safe_name}.md"
    text = f"""# Deep Dive: {cap_row['capability_name']}

**Coverage profile:** {profile_label}
**Capability ID:** {capability_id}
**Usage frequency:** {gap_row['usage_frequency']:.4f}
**Normalised coverage score:** {gap_row['total_coverage_score']:.4f}
**Gap score:** {gap_row['gap_score']:.4f}
**Benchmark count:** {int(gap_row['benchmark_count'])}
**Average quality among covering benchmarks:** {format_float(gap_row['average_quality'])}

## 1. Current Evaluation Landscape

{cap_row['capability_name']} is defined in the Phase 1 taxonomy as follows: {cap_row['definition']}

The updated Phase 2 benchmark inventory provides the following coverage:

{landscape}

This landscape shows that coverage is not only a question of benchmark count. A capability can have multiple benchmarks while still lacking direct coverage of the real-world situations described in the Phase 1 taxonomy. The coverage ratings therefore treat benchmark construct validity, task realism, scoring reliability, and update strategy as distinct from mere benchmark presence.

## 2. Technical and Practical Challenges to Evaluation

Evaluating {cap_row['capability_name']} is difficult because the capability definition spans several sub-categories: {cap_row['sub_categories']}. Benchmark design must decide which sub-categories are in scope, how user context is represented, and what counts as a valid response. Static answer-key scoring is easiest where outputs are short and objectively checkable, but many tasks in this capability require contextual judgement, long-form outputs, human preference, or multi-step tool use.

The Phase 2 quality notes indicate recurring constraints: contamination risk for static public datasets, operational cost for agentic environments, judge reliability for open-ended outputs, and reduced ecological validity when a benchmark uses a proxy format such as multiple choice. These constraints are especially important because the project aims to compare benchmark coverage against actual usage rather than against historically convenient evaluation formats.

## 3. Real-World Importance

The importance of this capability is grounded in mapped Anthropic AEI top-task usage. Examples include:

{examples}

These examples show why usage-weighted analysis is necessary. A benchmark ecosystem can look active in aggregate while leaving everyday user workflows under-tested, particularly when common tasks require judgement, context preservation, or end-to-end completion rather than isolated answer production.

## 4. Consequences of Inadequate Evaluation

Inadequate evaluation can produce three deployment risks. First, model-selection decisions may reward benchmark-specific competence rather than capability fit. Second, teams may deploy models into user workflows where the highest-risk failure modes were not measured. Third, improvements may be optimised toward visible leaderboards while lower-visibility but high-usage behaviours receive less research attention.

For {cap_row['capability_name']}, the most direct consequence is mismatch between benchmark confidence and user-facing reliability. If the benchmark primarily tests simplified or proxy tasks, high scores may not imply performance on realistic inputs, ambiguous user goals, domain constraints, or longer interaction histories.

## 5. Requirements for Adequate Coverage

Adequate coverage for this capability would require:

- Task samples drawn from realistic user workflows and documented source distributions.
- Clear separation of sub-capabilities so that aggregate scores do not hide weak areas.
- Scoring methods matched to output type, combining automated checks where possible with calibrated human or expert judgement where necessary.
- Contamination controls, including post-cutoff data, private holdouts, or continuously refreshed task pools.
- Reporting that links benchmark scores to use-case assumptions, limitations, and confidence intervals rather than headline accuracy alone.

For Phase 5, this capability should be considered for new benchmark design if it remains high in the gap ranking or if existing benchmarks fail to cover the most deployment-relevant sub-categories.
"""
    path.write_text(textwrap.dedent(text).strip() + "\n", encoding="utf-8")


def select_deep_dive_capabilities(gap_scores: pd.DataFrame) -> list[tuple[str, str]]:
    """Select the four required deep-dive capability profiles."""
    highest_gap = gap_scores.iloc[0]["capability_id"]
    well_covered = gap_scores[
        gap_scores["capability_id"] != highest_gap
    ].sort_values("total_coverage_score", ascending=False).iloc[0]["capability_id"]
    available = gap_scores[~gap_scores["capability_id"].isin([highest_gap, well_covered])].copy()
    median_gap_value = gap_scores["gap_score"].median()
    available["median_distance"] = (available["gap_score"] - median_gap_value).abs()
    moderate = available.sort_values("median_distance").iloc[0]["capability_id"]
    available = gap_scores[
        ~gap_scores["capability_id"].isin([highest_gap, well_covered, moderate])
    ].copy()
    low_usage_cutoff = available["usage_frequency"].median()
    niche_candidates = available[available["usage_frequency"] <= low_usage_cutoff]
    niche = niche_candidates.sort_values("total_coverage_score").iloc[0]["capability_id"]
    return [
        (highest_gap, "Highest Gap Capability"),
        (well_covered, "Well-Covered Capability"),
        (moderate, "Moderate Coverage Capability"),
        (niche, "Niche Gap Capability"),
    ]


def write_deep_dives(
    taxonomy: pd.DataFrame, benchmarks: pd.DataFrame, matrix: pd.DataFrame, gap_scores: pd.DataFrame
) -> None:
    """Write all four required qualitative deep dives."""
    for capability_id, label in select_deep_dive_capabilities(gap_scores):
        write_deep_dive(capability_id, label, taxonomy, benchmarks, matrix, gap_scores)


def write_case_studies() -> None:
    """Write documented real-world benchmark/deployment mismatch case studies."""
    lines = [
        "# Phase 3 Case Studies: Benchmark Scores and Real-World Deployment Failures",
        "",
        "**Objective:** Document real-world cases where strong benchmark performance or benchmark confidence did not translate into reliable deployment behaviour.",
        "**Scope:** Six cases are included, exceeding the minimum acceptable three cases in the Phase 3 protocol.",
        "",
        "## Search Strategy",
        "",
        "Searches covered academic and industry sources for `LLM deployment failure`, `benchmark performance gap`, `AI evaluation mismatch`, medical LLM failures, legal hallucination failures, benchmark contamination, leaderboard instability, and the project core papers. The cases below prioritise sources already named in `CLAUDE.md` and additional peer-reviewed or preprint evidence where directly relevant.",
        "",
    ]
    for index, case in enumerate(CASE_STUDIES, start=1):
        lines.extend(
            [
                f"## Case {index}: {case['title']}",
                "",
                f"**Model name and benchmark performance:** {case['model']}. {case['benchmark_performance']}",
                "",
                f"**Real-world deployment context:** {case['context']}",
                "",
                f"**Specific failure mode observed:** {case['failure']}",
                "",
                f"**Capability gap implicated:** {case['capability_gap']}",
                "",
                f"**Consequences:** {case['consequences']}",
                "",
                f"**Source documentation:** {case['source']}",
                "",
            ]
        )
    lines.extend(
        [
            "## Cross-Case Pattern",
            "",
            "Across these cases, the recurring problem is not that benchmarks are useless. It is that benchmark scores are often treated as general evidence of deployment reliability when they are actually evidence for a narrower task format, data distribution, scoring method, or disclosure context. Phase 3 therefore treats coverage as a capability-specific construct-validity question rather than as a count of available leaderboards.",
        ]
    )
    CASE_STUDIES_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """Write Phase 3 qualitative outputs from existing generated CSVs."""
    ensure_directories()
    taxonomy, benchmarks, _, _ = load_inputs()
    benchmarks = prepare_benchmarks(benchmarks)
    matrix = pd.read_csv(MATRIX_PATH, index_col=0)
    gap_scores = pd.read_csv(GAP_SCORES_PATH)
    write_deep_dives(taxonomy, benchmarks, matrix, gap_scores)
    write_case_studies()
    print("Qualitative deep dives and case studies written.")


if __name__ == "__main__":
    main()
