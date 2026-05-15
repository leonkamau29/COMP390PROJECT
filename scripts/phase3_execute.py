"""
Execute the full modular Phase 3 coverage-analysis pipeline.

Purpose:
    Orchestrate the Phase 3 modules in methodology order: coverage matrix,
    usage-weighted gap scores, statistical analysis/reporting, visualisations,
    qualitative deep dives, and case studies.

Inputs:
    Phase 1 taxonomy and usage mapping files.
    Updated Phase 2 benchmark database.

Outputs:
    All Phase 3 CSV, Markdown, and chart deliverables.
"""

from __future__ import annotations

from phase3_config import ensure_directories, load_inputs, prepare_benchmarks, validate_outputs
from phase3_coverage_matrix import build_coverage_outputs
from phase3_gap_scores import compute_gap_scores, compute_usage_frequencies
from phase3_qualitative_analysis import write_case_studies, write_deep_dives
from phase3_statistical_analysis import run_statistics, write_statistical_report
from phase3_visualisations import plot_charts


def main() -> None:
    """Execute the full Phase 3 pipeline."""
    ensure_directories()
    taxonomy, benchmarks, mapping, usage = load_inputs()
    benchmarks = prepare_benchmarks(benchmarks)

    matrix, notes_df, metrics = build_coverage_outputs(taxonomy, benchmarks)
    usage_by_capability = compute_usage_frequencies(taxonomy, mapping, usage)
    gap_scores = compute_gap_scores(metrics, usage_by_capability)
    stats_df = run_statistics(gap_scores, matrix, benchmarks)
    write_statistical_report(gap_scores, stats_df, matrix, notes_df)
    plot_charts(taxonomy, benchmarks, matrix, gap_scores)
    write_deep_dives(taxonomy, benchmarks, matrix, gap_scores)
    write_case_studies()
    validate_outputs()

    print("Phase 3 execution complete.")
    print(f"Benchmarks analysed: {len(benchmarks)}")
    print(f"Coverage ratings justified: {len(notes_df)}")
    print(f"Statistical tests reported: {len(stats_df)}")
    print(
        "Highest gap: "
        f"{gap_scores.iloc[0]['capability_id']} "
        f"{gap_scores.iloc[0]['capability_name']} "
        f"({gap_scores.iloc[0]['gap_score']:.4f})"
    )


if __name__ == "__main__":
    main()
