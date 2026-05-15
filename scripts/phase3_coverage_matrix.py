"""
Build the Phase 3 capability-benchmark coverage matrix.

Purpose:
    Store justified 0-5 coverage ratings, write the matrix and companion notes,
    and compute aggregate per-capability coverage metrics.

Inputs:
    outputs/phase1/capability_taxonomy_FINAL.csv
    outputs/phase2/benchmark_database_FINAL.csv

Outputs:
    data/phase3/coverage_matrix.csv
    data/phase3/coverage_matrix_notes.csv
    data/phase3/capability_coverage_metrics.csv
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from phase3_config import METRICS_PATH, MATRIX_PATH, NOTES_PATH, ensure_directories, load_inputs, prepare_benchmarks


np.random.seed(42)

COVERAGE_RATINGS: dict[str, dict[str, tuple[int, str]]] = {
    "B001": {
        "C02": (
            3,
            "HumanEval+ directly tests isolated Python code generation with robust unit tests, but its narrow single-function format and high contamination risk limit real-world C02 coverage.",
        )
    },
    "B002": {
        "C02": (
            5,
            "SWE-bench Verified evaluates real GitHub issue resolution with repository context, patch generation, and test-based scoring, making it a high-fidelity C02 benchmark.",
        )
    },
    "B003": {
        "C02": (
            4,
            "LiveCodeBench tests code generation, self-repair, execution reasoning, and post-cutoff algorithmic problems, but remains closer to competitive programming than everyday maintenance work.",
        )
    },
    "B004": {
        "C02": (
            5,
            "BigCodeBench tests library-oriented Python API use and executable integration tasks, giving strong coverage of practical software development beyond toy functions.",
        )
    },
    "B005": {
        "C02": (
            5,
            "SWE-Lancer Diamond uses economically valued freelance engineering tasks with verified tests and expert review, giving strong coverage of real technical problem solving.",
        )
    },
    "B006": {
        "C03": (
            3,
            "MMLU-Pro provides broad factual and academic reasoning coverage, but multiple-choice academic items are a proxy for real advisory or information-seeking use.",
        ),
        "C04": (
            2,
            "The benchmark overlaps with educational knowledge tasks, but it measures answer selection rather than tutoring, scaffolding, or learner support.",
        ),
    },
    "B007": {
        "C03": (
            4,
            "GPQA Diamond provides expert-vetted graduate science questions that strongly test factual retrieval and expert reasoning, although its STEM scope is narrow.",
        ),
        "C04": (
            2,
            "The expert academic content is relevant to learning contexts, but the task does not evaluate pedagogy or learner interaction.",
        ),
    },
    "B008": {
        "C03": (
            4,
            "Humanity's Last Exam tests broad expert knowledge and multimodal reasoning with expert-vetted items, giving strong frontier C03 coverage despite limited advisory context.",
        ),
        "C04": (
            2,
            "The benchmark covers difficult academic subject matter but does not test explanation quality or learner-oriented teaching.",
        ),
    },
    "B009": {
        "C03": (
            4,
            "SimpleQA and FACTS Grounding directly evaluate factual accuracy and groundedness, central risks for information retrieval and advisory use.",
        ),
        "C07": (
            3,
            "FACTS Grounding requires use of supplied documents, giving moderate document-processing coverage without full summarisation or analysis workflows.",
        ),
    },
    "B010": {
        "C03": (
            4,
            "LiveBench includes dynamic knowledge and reasoning tasks sourced after common training cutoffs, giving strong contamination-resistant C03 signal.",
        ),
        "C07": (
            3,
            "LiveBench includes data analysis tasks, but C07 is only one part of a broad multi-domain suite.",
        ),
        "C02": (
            2,
            "LiveBench includes coding tasks, but it is not primarily a software development benchmark.",
        ),
        "C01": (
            2,
            "LiveBench includes language and instruction-following tasks, but it does not directly assess rich content-generation quality.",
        ),
    },
    "B011": {
        "C01": (
            3,
            "IFEval tests instruction-constrained text generation with programmatic checks, useful for C01 compliance but weak for substantive writing quality.",
        )
    },
    "B012": {
        "C01": (
            5,
            "WritingBench directly evaluates open-ended writing quality across multiple genres and subdomains with task-dependent criteria, making it the strongest C01 benchmark in the inventory.",
        )
    },
    "B013": {
        "C01": (
            4,
            "EQ-Bench Creative Writing v3 evaluates creative and longform generation quality, but small prompt sets and LLM-judge dependence limit reliability.",
        ),
        "C08": (
            2,
            "Creative character and voice evaluation overlaps weakly with roleplay, but the benchmark is not built around sustained interaction.",
        ),
    },
    "B014": {
        "C01": (
            4,
            "WildBench is grounded in real-user tasks and includes many writing prompts, giving strong ecological validity for C01 despite broad construct attribution.",
        ),
        "C02": (
            3,
            "WildBench includes real-user coding tasks, but coding is one component rather than the central construct.",
        ),
        "C08": (
            3,
            "WildBench includes roleplay and conversational tasks from WildChat, giving moderate C08 coverage.",
        ),
        "C04": (
            2,
            "Some WildBench tasks involve math and educational assistance, but pedagogy is not the benchmark focus.",
        ),
        "C07": (
            2,
            "Some WildBench tasks require analysis or planning over supplied information, but the suite is not a dedicated C07 benchmark.",
        ),
        "C03": (
            2,
            "The real-user task mix includes information-seeking prompts, but factual advisory evaluation is not isolated.",
        ),
    },
    "B015": {
        "C07": (
            5,
            "InfiAgent-DABench directly evaluates agentic data analysis over CSV files with open-ended analytical questions, making it a high-fidelity C07 benchmark.",
        )
    },
    "B016": {
        "C07": (
            5,
            "DA-Code evaluates executable data-science workflows across wrangling, machine learning, and exploratory analysis, giving strong practical C07 coverage.",
        ),
        "C02": (
            2,
            "The executable environment involves code production, but coding is instrumental to data analysis rather than the primary capability.",
        ),
    },
    "B017": {
        "C07": (
            5,
            "Spider 2.0 tests enterprise SQL and BI workflows over realistic database environments, giving strong coverage of data analysis and business intelligence.",
        ),
        "C02": (
            2,
            "SQL generation is executable technical output, but the benchmark's construct is primarily data analysis and BI.",
        ),
    },
    "B018": {
        "C07": (
            5,
            "MMLongBench-Doc evaluates long-context multimodal document understanding, extraction, and evidence-supported QA over complex PDFs, giving strong C07 document-processing coverage.",
        ),
        "C03": (
            3,
            "The document QA format produces factual answers from supplied evidence, overlapping with grounded information retrieval.",
        ),
    },
    "B019": {
        "C04": (
            4,
            "MathDial directly evaluates multi-turn mathematics tutoring dialogue, although it is limited to math and reference-based pedagogy.",
        ),
        "C08": (
            3,
            "The multi-turn tutor-student dialogue format tests sustained conversational interaction, but the goal is educational rather than social or entertainment-focused.",
        ),
    },
    "B020": {
        "C04": (
            5,
            "MathTutorBench targets tutoring sub-skills such as scaffolding and mistake localisation, making it a strong C04 pedagogical benchmark.",
        ),
        "C05": (
            2,
            "Mistake localisation and feedback tasks overlap with review, but the benchmark's core construct is tutoring.",
        ),
    },
    "B021": {
        "C04": (
            5,
            "TutorBench evaluates multisubject multimodal tutoring with expert-curated rubrics, giving strong C04 coverage beyond mathematics-only settings.",
        ),
        "C05": (
            3,
            "Rubric-based feedback on student work overlaps with review and assessment, though the benchmark is framed around tutoring support.",
        ),
    },
    "B022": {
        "C05": (
            4,
            "CriticBench directly evaluates critique and correction across reasoning, math, code, and symbolic tasks, but prose editing and stylistic review remain weakly covered.",
        ),
        "C02": (
            2,
            "Some critique-and-correction items involve code, but software development is not the primary benchmark construct.",
        ),
        "C04": (
            2,
            "Critique tasks can resemble educational feedback, but the benchmark does not evaluate tutoring interaction.",
        ),
    },
    "B023": {
        "C05": (
            5,
            "JudgeBench directly evaluates judgement quality over paired model answers with objective correctness labels, making it a strong C05 benchmark for evaluative review.",
        )
    },
    "B024": {
        "C05": (
            4,
            "RewardBench 2 evaluates preference and reward-model judgement across domains, giving strong but indirect coverage of feedback quality.",
        )
    },
    "B025": {
        "C08": (
            5,
            "PingPong dynamically evaluates multi-turn roleplay with simulated users and judge ensembles, giving high-fidelity C08 coverage.",
        )
    },
    "B026": {
        "C08": (
            5,
            "CoSER evaluates authentic character roleplay and character fidelity across a large literary corpus, giving strong C08 coverage of collaborative roleplay.",
        ),
        "C01": (
            2,
            "The roleplay tasks produce creative text, but the value lies in interaction and persona fidelity rather than standalone content generation.",
        ),
    },
    "B027": {
        "C06": (
            5,
            "BenchMAX evaluates multilingual LLM capability across 16 languages with native post-editing and validation, giving high-quality C06 coverage.",
        )
    },
    "B028": {
        "C06": (
            5,
            "WMT24++ is a strong human-referenced machine-translation benchmark across 55 languages and dialects, giving direct C06 translation coverage.",
        )
    },
}


def build_coverage_outputs(
    taxonomy: pd.DataFrame, benchmarks: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Create coverage matrix, notes, and aggregate capability metrics."""
    capability_ids = taxonomy["capability_id"].tolist()
    matrix = pd.DataFrame(0, index=benchmarks["benchmark_id"], columns=capability_ids)
    notes: list[dict[str, object]] = []

    for benchmark_id, ratings in COVERAGE_RATINGS.items():
        if benchmark_id not in set(benchmarks["benchmark_id"]):
            raise ValueError(f"Coverage rating references missing benchmark_id: {benchmark_id}")
        for capability_id, (rating, justification) in ratings.items():
            if capability_id not in capability_ids:
                raise ValueError(f"Coverage rating references missing capability_id: {capability_id}")
            matrix.loc[benchmark_id, capability_id] = rating
            notes.append(
                {
                    "benchmark_id": benchmark_id,
                    "capability_id": capability_id,
                    "rating": rating,
                    "justification": justification,
                }
            )

    notes_df = pd.DataFrame(notes).sort_values(["benchmark_id", "capability_id"])
    max_possible = len(benchmarks) * 5
    metrics = pd.DataFrame(
        {
            "capability_id": capability_ids,
            "capability_name": taxonomy.set_index("capability_id").loc[capability_ids, "capability_name"].values,
            "total_coverage_score": [matrix[c].sum() / max_possible for c in capability_ids],
            "coverage_points": [int(matrix[c].sum()) for c in capability_ids],
            "max_possible_points": max_possible,
            "benchmark_count": [(matrix[c] >= 1).sum() for c in capability_ids],
            "average_quality": [matrix.loc[matrix[c] >= 1, c].mean() for c in capability_ids],
        }
    )

    matrix.reset_index().rename(columns={"index": "benchmark_id"}).to_csv(MATRIX_PATH, index=False)
    notes_df.to_csv(NOTES_PATH, index=False)
    metrics.to_csv(METRICS_PATH, index=False)
    return matrix, notes_df, metrics


def main() -> None:
    """Generate Phase 3 coverage matrix files."""
    ensure_directories()
    taxonomy, benchmarks, _, _ = load_inputs()
    benchmarks = prepare_benchmarks(benchmarks)
    _, notes_df, _ = build_coverage_outputs(taxonomy, benchmarks)
    print(f"Coverage ratings justified: {len(notes_df)}")


if __name__ == "__main__":
    main()
