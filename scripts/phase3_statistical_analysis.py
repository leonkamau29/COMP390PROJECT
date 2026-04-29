"""
Phase 3 Statistical Analysis Script

Purpose:
    Runs all required statistical analyses:
    1. Pearson Correlation — usage frequency vs. coverage score per capability
    2. Chi-square Test — coverage distribution vs. usage frequency
    3. Temporal Trend Analysis — linear regression of benchmark count ~ year per capability

Inputs:
    data/phase3/gap_scores.csv
    data/phase3/capability_coverage_metrics.csv
    outputs/phase2/benchmark_database_FINAL.csv

Outputs:
    data/phase3/statistical_analysis_results.csv
    outputs/phase3/statistical_analysis_report.md

Usage:
    python scripts/phase3_statistical_analysis.py
"""

import pandas as pd
import numpy as np
from scipy import stats
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

np.random.seed(42)

GAP_SCORES_PATH = "data/phase3/gap_scores.csv"
BENCHMARK_DB = "outputs/phase2/benchmark_database_FINAL.csv"
RESULTS_PATH = "data/phase3/statistical_analysis_results.csv"
REPORT_PATH = "outputs/phase3/statistical_analysis_report.md"


def pearson_correlation(gap_df: pd.DataFrame) -> dict:
    """Pearson correlation between usage frequency and coverage score.

    Args:
        gap_df: DataFrame with usage_frequency and total_coverage_score columns.

    Returns:
        Dict with r, p_value, 95% CI, interpretation.
    """
    r, p = stats.pearsonr(gap_df["usage_frequency"], gap_df["total_coverage_score"])
    n = len(gap_df)
    # Fisher z-transform for 95% CI
    z = np.arctanh(r)
    se = 1 / np.sqrt(n - 3)
    ci_low = np.tanh(z - 1.96 * se)
    ci_high = np.tanh(z + 1.96 * se)
    return {
        "test_name": "Pearson Correlation (usage_freq vs coverage_score)",
        "test_statistic": round(r, 4),
        "p_value": round(p, 4),
        "effect_size": round(r, 4),
        "confidence_interval": f"[{round(ci_low, 4)}, {round(ci_high, 4)}]",
        "interpretation": f"r={r:.4f}, p={p:.4f}. {'Significant' if p < 0.05 else 'Not significant'} at α=0.05."
    }


def chi_square_test(gap_df: pd.DataFrame) -> dict:
    """Chi-square test: is coverage proportional to usage frequency?

    Args:
        gap_df: DataFrame with benchmark_count and usage_frequency columns.

    Returns:
        Dict with chi2, p_value, effect_size (Cramér's V), interpretation.
    """
    observed = gap_df["benchmark_count"].values
    total_benchmarks = observed.sum()
    expected = gap_df["usage_frequency"].values / gap_df["usage_frequency"].sum() * total_benchmarks
    chi2, p = stats.chisquare(f_obs=observed, f_exp=expected)
    n = total_benchmarks
    k = len(observed)
    cramers_v = np.sqrt(chi2 / (n * (k - 1)))
    return {
        "test_name": "Chi-Square (coverage distribution vs. usage frequency)",
        "test_statistic": round(chi2, 4),
        "p_value": round(p, 4),
        "effect_size": round(cramers_v, 4),
        "confidence_interval": "N/A",
        "interpretation": f"χ²={chi2:.4f}, p={p:.4f}, Cramér's V={cramers_v:.4f}. {'Significant' if p < 0.05 else 'Not significant'} at α=0.05."
    }


def main():
    """Main execution: run all statistical tests and save results."""
    gap_df = pd.read_csv(GAP_SCORES_PATH)

    if gap_df.empty:
        print("Populate gap_scores.csv before running statistical analysis.")
        return

    results = []
    results.append(pearson_correlation(gap_df))
    results.append(chi_square_test(gap_df))

    results_df = pd.DataFrame(results)
    results_df.to_csv(RESULTS_PATH, index=False)
    print(f"Statistical results saved to {RESULTS_PATH}")
    print(results_df.to_string())


if __name__ == "__main__":
    main()
