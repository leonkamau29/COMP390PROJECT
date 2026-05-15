"""
Run Phase 3 statistical analyses and write the statistical report.

Purpose:
    Perform Pearson correlation, chi-square goodness-of-fit, and temporal
    regression analyses required by the Phase 3 methodology.

Inputs:
    data/phase3/coverage_matrix.csv
    data/phase3/coverage_matrix_notes.csv
    data/phase3/gap_scores.csv
    outputs/phase2/benchmark_database_FINAL.csv

Outputs:
    data/phase3/statistical_analysis_results.csv
    outputs/phase3/statistical_analysis_report.md
"""

from __future__ import annotations

import math

import numpy as np
import pandas as pd
from scipy import stats

from phase3_config import (
    GAP_SCORES_PATH,
    MATRIX_PATH,
    NOTES_PATH,
    REPORT_PATH,
    STATS_PATH,
    ensure_directories,
    format_float,
    load_inputs,
    prepare_benchmarks,
)


np.random.seed(42)


def pearson_ci(r_value: float, n: int) -> tuple[float, float]:
    """Compute Fisher-transformed 95 percent CI for Pearson r."""
    if n <= 3 or abs(r_value) >= 1:
        return (math.nan, math.nan)
    z_value = np.arctanh(r_value)
    se = 1 / np.sqrt(n - 3)
    return (float(np.tanh(z_value - 1.96 * se)), float(np.tanh(z_value + 1.96 * se)))


def regression_slope_ci(
    x_values: np.ndarray, y_values: np.ndarray, slope: float, intercept: float
) -> tuple[float, float]:
    """Compute a 95 percent confidence interval for a regression slope."""
    n = len(x_values)
    if n <= 2:
        return (math.nan, math.nan)
    predicted = intercept + slope * x_values
    residuals = y_values - predicted
    s_err = np.sqrt(np.sum(residuals**2) / (n - 2))
    x_var = np.sum((x_values - np.mean(x_values)) ** 2)
    if x_var == 0:
        return (math.nan, math.nan)
    slope_se = s_err / np.sqrt(x_var)
    t_crit = stats.t.ppf(0.975, n - 2)
    return (float(slope - t_crit * slope_se), float(slope + t_crit * slope_se))


def bootstrap_cramers_v_ci(
    observed: np.ndarray, expected_probabilities: np.ndarray, iterations: int = 5000
) -> tuple[float, float]:
    """Estimate a 95 percent bootstrap CI for Cramer's V."""
    total = int(observed.sum())
    observed_probabilities = observed / total
    k = len(observed)
    boot_values = []
    for _ in range(iterations):
        sample = np.random.multinomial(total, observed_probabilities)
        expected = expected_probabilities * total
        chi2 = np.sum((sample - expected) ** 2 / np.where(expected == 0, np.nan, expected))
        boot_values.append(np.sqrt(chi2 / (total * (k - 1))))
    return tuple(np.nanpercentile(boot_values, [2.5, 97.5]))


def run_statistics(
    gap_scores: pd.DataFrame, matrix: pd.DataFrame, benchmarks: pd.DataFrame
) -> pd.DataFrame:
    """Run Pearson, chi-square, and per-capability temporal regressions."""
    results: list[dict[str, object]] = []

    r_value, p_value = stats.pearsonr(
        gap_scores["usage_frequency"], gap_scores["total_coverage_score"]
    )
    r_ci = pearson_ci(r_value, len(gap_scores))
    results.append(
        {
            "analysis_type": "Pearson correlation",
            "capability_id": "ALL",
            "test_name": "Usage frequency vs normalised coverage score",
            "test_statistic": round(r_value, 4),
            "p_value": round(p_value, 4),
            "effect_size": round(r_value, 4),
            "confidence_interval_95": f"[{r_ci[0]:.4f}, {r_ci[1]:.4f}]",
            "n": len(gap_scores),
            "interpretation": (
                "Higher-usage capabilities tend to receive more benchmark coverage."
                if r_value > 0
                else "Higher-usage capabilities do not receive proportionally more benchmark coverage."
            ),
        }
    )

    observed = gap_scores.sort_values("capability_id")["benchmark_count"].to_numpy(dtype=float)
    expected = (
        gap_scores.sort_values("capability_id")["usage_frequency"].to_numpy(dtype=float)
        / gap_scores["usage_frequency"].sum()
        * observed.sum()
    )
    expected_probabilities = expected / observed.sum()
    chi2, chi_p = stats.chisquare(f_obs=observed, f_exp=expected)
    cramers_v = np.sqrt(chi2 / (observed.sum() * (len(observed) - 1)))
    v_ci = bootstrap_cramers_v_ci(observed.astype(int), expected_probabilities)
    results.append(
        {
            "analysis_type": "Chi-square goodness-of-fit",
            "capability_id": "ALL",
            "test_name": "Benchmark-count distribution vs Anthropic usage distribution",
            "test_statistic": round(chi2, 4),
            "p_value": round(chi_p, 4),
            "effect_size": round(cramers_v, 4),
            "confidence_interval_95": f"Cramer's V bootstrap [{v_ci[0]:.4f}, {v_ci[1]:.4f}]",
            "n": int(observed.sum()),
            "interpretation": (
                "Benchmark coverage is not distributed in proportion to observed usage."
                if chi_p < 0.05
                else "Benchmark coverage is not significantly different from the usage-weighted distribution."
            ),
        }
    )

    years = np.arange(2020, 2026)
    benchmark_years = benchmarks.set_index("benchmark_id")["year_clean"].to_dict()
    cap_names = gap_scores.set_index("capability_id")["capability_name"].to_dict()
    for capability_id in sorted(cap_names):
        annual_counts = []
        for year in years:
            ids_in_year = [
                benchmark_id
                for benchmark_id, benchmark_year in benchmark_years.items()
                if benchmark_year == year
            ]
            annual_counts.append(int((matrix.loc[ids_in_year, capability_id] >= 1).sum()))
        y_values = np.array(annual_counts, dtype=float)
        regression = stats.linregress(years, y_values)
        slope_ci = regression_slope_ci(years, y_values, regression.slope, regression.intercept)
        results.append(
            {
                "analysis_type": "Temporal linear regression",
                "capability_id": capability_id,
                "test_name": f"Annual benchmark count vs publication year for {cap_names[capability_id]}",
                "test_statistic": round(regression.slope, 4),
                "p_value": round(regression.pvalue, 4),
                "effect_size": round(regression.rvalue**2, 4),
                "confidence_interval_95": f"Slope [{slope_ci[0]:.4f}, {slope_ci[1]:.4f}]",
                "n": len(years),
                "interpretation": (
                    "Positive slope indicates increasing benchmark activity over time."
                    if regression.slope > 0
                    else "Non-positive slope indicates flat or declining benchmark activity over time."
                ),
            }
        )

    results_df = pd.DataFrame(results)
    results_df.to_csv(STATS_PATH, index=False)
    return results_df


def write_statistical_report(
    gap_scores: pd.DataFrame, stats_df: pd.DataFrame, matrix: pd.DataFrame, notes_df: pd.DataFrame
) -> None:
    """Write the Phase 3 statistical analysis report."""
    top_gap = gap_scores.iloc[0]
    best_covered = gap_scores.sort_values("total_coverage_score", ascending=False).iloc[0]
    content = [
        "# Phase 3 Statistical Analysis Report",
        "",
        "**Project:** Benchmark Coverage Gap: A Systematic Analysis of Real-World AI Capabilities and Evaluation Practices",
        "**Date generated:** 2026-05-14",
        "**Methodological basis:** Phase 3 instructions in `CLAUDE.md`, using the Phase 1 taxonomy and updated 28-row Phase 2 benchmark database.",
        "",
        "## Data Inputs",
        "",
        f"- Benchmarks analysed: {len(matrix)} from `outputs/phase2/benchmark_database_FINAL.csv`.",
        f"- Capabilities analysed: {len(gap_scores)} from `outputs/phase1/capability_taxonomy_FINAL.csv`.",
        f"- Non-zero coverage judgements: {len(notes_df)} justified ratings in `data/phase3/coverage_matrix_notes.csv`.",
        "- Usage frequencies were calculated by summing Anthropic AEI top-task `usage_pct` values after mapping each task to the Phase 1 capability taxonomy.",
        "",
        "## Key Results",
        "",
        f"- Highest usage-weighted gap: **{top_gap['capability_name']}** ({top_gap['capability_id']}), gap score {top_gap['gap_score']:.4f}.",
        f"- Highest normalised benchmark coverage: **{best_covered['capability_name']}** ({best_covered['capability_id']}), coverage score {best_covered['total_coverage_score']:.4f}.",
        "- The gap score formula used was: `Gap Score = Usage_Frequency x (1 - Normalized_Coverage_Score)`.",
        "",
        "## Gap Score Ranking",
        "",
        "| Rank | Capability | Usage frequency | Coverage score | Benchmark count | Average quality | Gap score | Severity |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for _, row in gap_scores.iterrows():
        content.append(
            f"| {int(row['gap_rank'])} | {row['capability_id']} {row['capability_name']} | "
            f"{row['usage_frequency']:.4f} | {row['total_coverage_score']:.4f} | "
            f"{int(row['benchmark_count'])} | {format_float(row['average_quality'])} | "
            f"{row['gap_score']:.4f} | {row['severity']} |"
        )
    content.extend(
        [
            "",
            "## Statistical Tests",
            "",
            "| Analysis | Capability | Statistic | p-value | Effect size | 95% CI | Interpretation |",
            "| --- | --- | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for _, row in stats_df.iterrows():
        content.append(
            f"| {row['analysis_type']} | {row['capability_id']} | {row['test_statistic']} | "
            f"{row['p_value']} | {row['effect_size']} | {row['confidence_interval_95']} | "
            f"{row['interpretation']} |"
        )
    content.extend(
        [
            "",
            "## Interpretation",
            "",
            "The coverage matrix shows that benchmark availability is shaped by research-community priorities rather than by measured usage alone. Code, data-analysis, knowledge, and newer tutoring benchmarks now have visible coverage, while coverage remains thinner for capabilities whose validity depends on subjective or context-sensitive judgement, such as review, roleplay, and multilingual language support.",
            "",
            "The chi-square test should be interpreted as a distributional diagnostic rather than a causal claim. The expected distribution assumes benchmark counts should track Anthropic usage frequencies, which is a defensible gap-analysis baseline but not the only possible allocation rule. Some low-usage capabilities, such as translation, are intentionally represented by mature specialised benchmarks because they have high deployment risk despite lower frequency in the Anthropic top-task file.",
            "",
            "The temporal regressions use only six annual observations (2020-2025), so slopes should be read as descriptive signals. They are most useful for identifying where recent benchmark activity is accelerating, not for forecasting long-term research investment.",
            "",
            "## Visualisations Produced",
            "",
            "- `outputs/phase3/charts/coverage_heatmap.png`",
            "- `outputs/phase3/charts/gap_scores.png`",
            "- `outputs/phase3/charts/usage_vs_coverage_scatter.png`",
            "- `outputs/phase3/charts/temporal_trends.png`",
            "- `outputs/phase3/charts/quality_radar.png`",
        ]
    )
    REPORT_PATH.write_text("\n".join(content) + "\n", encoding="utf-8")


def main() -> None:
    """Run Phase 3 statistical analysis from existing generated CSVs."""
    ensure_directories()
    _, benchmarks, _, _ = load_inputs()
    benchmarks = prepare_benchmarks(benchmarks)
    gap_scores = pd.read_csv(GAP_SCORES_PATH)
    matrix = pd.read_csv(MATRIX_PATH, index_col=0)
    notes_df = pd.read_csv(NOTES_PATH)
    stats_df = run_statistics(gap_scores, matrix, benchmarks)
    write_statistical_report(gap_scores, stats_df, matrix, notes_df)
    print(f"Statistical results saved to {STATS_PATH}")


if __name__ == "__main__":
    main()
